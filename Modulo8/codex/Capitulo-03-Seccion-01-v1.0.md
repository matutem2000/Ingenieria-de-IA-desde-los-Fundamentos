# Módulo 8 – Capítulo 03 – Sección 01

# llama.cpp: inferencia eficiente en CPU y GPU para modelos GGUF

llama.cpp es un motor de inferencia de LLMs escrito en C/C++ puro por Georgi Gerganov, diseñado desde el primer día para ejecutar modelos cuantizados con máxima eficiencia en hardware heterogéneo sin dependencias de PyTorch, CUDA ni drivers propietarios más allá de los opcionales para aceleración GPU. El proyecto compila con soporte para múltiples backends de aceleración mediante flags de cmake: `-DLLAMA_CUDA=ON` para NVIDIA, `-DLLAMA_METAL=ON` para Apple Silicon, `-DLLAMA_HIPBLAS=ON` para AMD ROCm, `-DLLAMA_VULKAN=ON` para GPUs genéricas, y compilación por defecto para CPU con instrucciones AVX2/AVX-512 cuando están disponibles. En CPU, llama.cpp utiliza kernels SIMD optimizados para las operaciones de dequantización y multiplicación matricial de las variantes K-quant: en un procesador moderno (Ryzen 9 7950X o Apple M3 Max), un modelo Llama 3 8B en Q4_K_M genera entre 15 y 40 tokens por segundo dependiendo del número de capas y la longitud del contexto. La arquitectura de llama.cpp expone una API C de bajo nivel y un servidor HTTP con API compatible con OpenAI, lo que permite integrarlo directamente en sistemas embebidos o reutilizarlo como backend de herramientas de alto nivel como Ollama y LM Studio.

## Aspectos técnicos de llama.cpp

- KV cache management: llama.cpp implementa KV cache en la memoria del dispositivo seleccionado (VRAM o RAM); el tamaño del cache crece linealmente con el número de capas, cabezas de atención y longitud de contexto máxima configurada con `--ctx-size`
- Offloading por capas: el flag `--n-gpu-layers N` permite descargar N capas del modelo a GPU y el resto a CPU+RAM; permite ejecutar modelos que no caben completamente en VRAM usando GPU para las capas más computacionalmente intensivas (transformer blocks)
- Especulative decoding: llama.cpp soporta especulative decoding con el flag `--draft-model` para usar un modelo más pequeño como draft; puede acelerar la generación 2-3x en modelos lentos con alta tasa de aceptación del draft
- Formatos de compilación: disponible como binario standalone, librería estática `.a` para integración C/C++, y bindings Python vía `llama-cpp-python` que expone una API de alto nivel y un servidor OpenAI-compatible en Python
- Benchmarking: el binario `llama-bench` mide throughput (tokens/s) en modo prompt processing y token generation por separado; fundamental para comparar configuraciones de hardware y variantes de cuantización antes del despliegue

## Para recordar

llama.cpp es la capa de inferencia más universal del ecosistema de LLMs locales: si un modelo existe en formato GGUF y tienes hardware con suficiente RAM o VRAM, llama.cpp puede ejecutarlo sin dependencias adicionales.
