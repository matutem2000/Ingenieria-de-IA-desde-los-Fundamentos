# Módulo 8 – Capítulo 02 – Sección 02

## GGUF: formato para inferencia en CPU y GPU con llama.cpp

El trabajo de construir y distribuir modelos cuantizados requiere un formato estándar que encapsule todo lo necesario para la inferencia en un único archivo portátil: los pesos cuantizados, la configuración de arquitectura del modelo, el tokenizador y los metadatos de cuantización. Antes de GGUF, los ingenieros que querían ejecutar modelos localmente necesitaban gestionar múltiples archivos de configuración separados, aplicar parches de cuantización manualmente y lidiar con incompatibilidades entre versiones de librerías. GGUF resolvió este problema de distribución con un diseño de archivo único autocontenido que funciona en cualquier plataforma donde compile llama.cpp.

GGUF (GPT-Generated Unified Format) es el formato de archivo binario diseñado por Georgi Gerganov como sucesor de GGML. Su característica más importante desde el punto de vista operativo es que el archivo es completamente **autocontenido y multiplataforma**: contiene los pesos cuantizados, la configuración del modelo (número de capas, cabezas de atención, dimensión oculta, frecuencia base de RoPE), el vocabulario y los templates de chat, y los factores de escala de cuantización por grupo. Para el AI Engineer, esto significa que copiar un archivo `.gguf` de una máquina a otra es suficiente para ejecutar el modelo en el destino sin instalación adicional de modelos o configuraciones externas.

La portabilidad multiplataforma es consecuencia directa del diseño de GGUF: llama.cpp compila con soporte para Metal (Apple Silicon), CUDA (NVIDIA), ROCm (AMD), Vulkan (cross-platform) y CPU pura con instrucciones AVX2/AVX-512. El mismo archivo `.gguf` ejecuta sin modificación en todas estas plataformas; lo que cambia entre plataformas es el backend de aceleración que llama.cpp utiliza en tiempo de ejecución.

La nomenclatura estándar de los archivos GGUF codifica la variante de cuantización directamente en el nombre. Un archivo `llama-3-8b-instruct.Q4_K_M.gguf` indica cuantización K-quant de 4 bits con mezcla media (M). Esta convención de nomenclatura permite identificar inmediatamente el nivel de cuantización sin necesitar abrir el archivo ni leer metadatos. Las variantes K-quant disponibles son: Q2_K, Q3_K (en variantes S/M/L), Q4_K (S/M), Q5_K (S/M), Q6_K y Q8_0, donde el número indica los bits por peso predominantes y la letra final el tamaño del grupo de cuantización utilizado (S=small, M=medium, L=large); grupos mayores ofrecen mejor calidad al costo de mayor overhead de memoria para los factores de escala.

Una característica operativamente relevante de GGUF es el soporte de **carga parcial en GPU mediante offloading por capas**. Si el modelo no cabe completamente en la VRAM disponible, llama.cpp puede cargar las primeras N capas en GPU (donde ocurre la mayor parte del cómputo intensivo) y las capas restantes en la RAM del sistema, ejecutándolas en CPU. Esto se controla con el flag `--n-gpu-layers N` y permite hacer viable la inferencia de modelos que exceden la VRAM disponible, aunque con menor velocidad que la carga completa en GPU. La selección del número óptimo de capas a cargar en GPU es un problema de optimización empírico que depende del tamaño del modelo, la cuantización y las memorias disponibles.

## Componentes del formato GGUF

- **Estructura del archivo:** cabecera de identificación seguida de metadatos key-value (configuración del modelo, tokenizador, template de chat, información de cuantización) y los tensores cuantizados almacenados en orden de dependencia de inferencia.
- **Metadatos embebidos:** incluye toda la información necesaria para cargar y usar el modelo: número de capas, cabezas de atención, dimensión oculta, tipo de RoPE, vocabulario completo, tokens especiales y template de chat en formato Jinja2.
- **Variantes K-quant:** Q2_K, Q3_K_S/M/L, Q4_K_S/M, Q5_K_S/M, Q6_K; variantes con más bits son de mayor calidad pero mayor tamaño.
- **Offloading parcial:** el flag `--n-gpu-layers N` de llama.cpp permite cargar las N primeras capas en VRAM y las restantes en RAM del sistema; balance dinámico entre velocidad y disponibilidad de memoria.
- **Compatibilidad multiplataforma:** el mismo archivo funciona con backends Metal, CUDA, ROCm, Vulkan y CPU sin recompilar el modelo.

> **Nota del Arquitecto:** Cuando descargues un modelo GGUF de Hugging Face, el repositorio suele ofrecer múltiples variantes de cuantización del mismo modelo. Si el hardware tiene 8 GB de VRAM, Q4_K_M es casi siempre el punto de inicio correcto. Si tienes 12-16 GB, considera Q5_K_M para mejor calidad. La variante Q8_0 es útil cuando necesitas la mayor calidad posible sin recurrir a BF16 completo, especialmente para tareas de razonamiento matemático o generación de código crítico.

GGUF es el formato que hace que llama.cpp y Ollama sean posibles como herramientas de distribución de modelos: sin un formato binario único y autocontenido, la experiencia de "descargar y ejecutar" un modelo local sería tan compleja como configurar PyTorch, CUDA y los modelos por separado. La sección siguiente examina GPTQ, el formato alternativo optimizado para el máximo throughput en GPU NVIDIA cuando el tiempo de inferencia es la métrica crítica.

---
