# Módulo 8 – Capítulo 03 – Sección 01

## llama.cpp: inferencia eficiente en CPU y GPU para modelos GGUF

Con el modelo seleccionado y la variante de cuantización elegida, el siguiente paso es ejecutarlo. La pregunta práctica es directa: ¿qué software convierte un archivo GGUF de 4 GB en un servidor de inferencia funcional? La respuesta más universal del ecosistema es llama.cpp, el motor de inferencia escrito en C/C++ puro por Georgi Gerganov que puede ejecutar modelos cuantizados en prácticamente cualquier hardware moderno sin depender de PyTorch, CUDA ni ningún framework de aprendizaje automático.

llama.cpp nació en enero de 2023 como un experimento para ejecutar LLaMA 1 en una MacBook, y en dos años se convirtió en la capa de inferencia más universal del ecosistema de modelos locales. Su decisión de diseño central es la portabilidad: el mismo binario compila con soporte para múltiples backends de aceleración mediante flags de cmake. `-DLLAMA_CUDA=ON` activa soporte para GPUs NVIDIA via CUDA; `-DLLAMA_METAL=ON` para Apple Silicon via Metal; `-DLLAMA_HIPBLAS=ON` para GPUs AMD via ROCm; `-DLLAMA_VULKAN=ON` para GPUs genéricas compatibles con Vulkan. Sin ningún flag especial, compila con kernels SIMD optimizados para CPU usando AVX2 o AVX-512 cuando están disponibles. El mismo archivo GGUF funciona en todos estos backends sin modificación.

El rendimiento en CPU es el que más sorprende a los ingenieros que vienen del mundo PyTorch: en un procesador moderno (Ryzen 9 7950X o Apple M3 Max), un modelo Llama 3 8B en Q4_K_M genera entre 15 y 40 tokens por segundo dependiendo de cuántas capas se han descargado a GPU con el flag `--n-gpu-layers`. Este rango es suficiente para la mayoría de las aplicaciones interactivas donde la latencia percibida está en el orden de segundos, no milisegundos. Para contextos donde llama.cpp opera puramente en CPU con RAM del sistema en lugar de VRAM dedicada, el rendimiento depende principalmente del ancho de banda de memoria del procesador y del número de capas activas, no tanto de los FLOPS de cómputo —porque el decode de LLMs es una operación memory-bound, no compute-bound.

El mecanismo de offloading por capas es una de las contribuciones arquitectónicas más prácticas de llama.cpp. El flag `--n-gpu-layers N` descarga las N capas más profundas del modelo a la GPU, ejecutándolas en VRAM a plena velocidad, mientras el resto de las capas se ejecutan en CPU usando RAM del sistema. Esto permite un balance dinámico que no es posible en PyTorch tradicional: si tienes una GPU de 8 GB de VRAM y un modelo de 7B en Q4_K_M que ocupa 4.1 GB más KV cache, puedes asignar 28 capas (de 32 totales) a la GPU y las 4 restantes a la CPU. El resultado es una velocidad de generación intermedia entre el rendimiento puro de CPU y el puro de GPU —significativamente mejor que la CPU sola, con una fracción del costo del hardware que requeriría cargar el modelo completo en VRAM.

llama.cpp también expone un servidor HTTP con API compatible con OpenAI, iniciado con `./llama-server -m modelo.gguf --port 8080 --api-key mi_clave`, que habilita los endpoints `/v1/chat/completions` y `/v1/completions` para integración directa con cualquier SDK de OpenAI. Este servidor es el componente que Ollama usa internamente como motor de inferencia, y es accesible directamente cuando se necesita mayor control sobre la configuración de bajo nivel.

## Aspectos técnicos de llama.cpp

- **KV cache management:** el KV cache crece linealmente con el número de capas, cabezas de atención y el tamaño de contexto configurado con `--ctx-size`; para Llama 3 8B con contexto de 8192 tokens en FP16, el KV cache requiere aproximadamente 4 GB adicionales sobre los pesos.
- **Offloading por capas:** `--n-gpu-layers N` descarga N capas del transformer a VRAM; permite ejecutar modelos que no caben completamente en VRAM usando GPU para las capas más intensivas computacionalmente.
- **Speculative decoding:** soporte con el flag `--draft-model` para usar un modelo más pequeño como draft; puede acelerar la generación 2-3x en modelos lentos con alta tasa de aceptación del draft.
- **Formatos de compilación:** binario standalone, librería estática `.a` para integración C/C++, y bindings Python via `llama-cpp-python` con API OpenAI-compatible.
- **Benchmarking:** el binario `llama-bench` mide throughput en modo prompt processing y token generation por separado; fundamental para comparar configuraciones de hardware antes del despliegue.

> **Nota del Arquitecto:** llama.cpp es mi punto de inicio cuando evalúo un nuevo modelo para producción. En diez minutos tengo el modelo ejecutándose, puedo benchmarcar con `llama-bench` las tres variantes de cuantización relevantes, y tomar una decisión de hardware informada. El hecho de que funcione en CPU, GPU y Apple Silicon sin reconfiguración lo convierte en la herramienta más versátil del ecosistema para la etapa de evaluación.

llama.cpp provee la base de inferencia sobre la que se construyen las herramientas de más alto nivel. La sección siguiente presenta Ollama, que abstrae la complejidad de descarga, configuración y gestión del ciclo de vida de llama.cpp detrás de una CLI y una API HTTP que hacen que el despliegue de un modelo local sea accesible en minutos.

---
