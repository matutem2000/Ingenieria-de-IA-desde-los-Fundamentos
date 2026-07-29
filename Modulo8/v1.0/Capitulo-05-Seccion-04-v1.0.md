# Módulo 8 – Capítulo 05 – Sección 04

## TensorRT-LLM: optimización de inferencia para GPUs NVIDIA

Cuando vLLM con sus optimizaciones de PagedAttention y continuous batching no es suficiente para satisfacer los requisitos de throughput o costo por token de una operación de LLM a escala, TensorRT-LLM (TRT-LLM) de NVIDIA es el siguiente nivel de optimización disponible. La diferencia fundamental entre vLLM y TRT-LLM no es de algoritmos de gestión de KV cache —ambos tienen implementaciones eficientes— sino de la profundidad de la optimización del hardware: vLLM opera sobre el modelo en su forma de PyTorch estándar con optimizaciones en tiempo de ejecución; TRT-LLM compila el modelo ahead-of-time a un engine específico para la GPU objetivo, eliminando toda la abstracción de PyTorch y generando código de máquina directamente optimizado para los Tensor Cores y el layout de SRAM de esa GPU específica.

El proceso de uso de TRT-LLM tiene dos fases separadas. La primera es la compilación, que transforma el modelo descargado de Hugging Face en un engine TensorRT para la GPU disponible. El proceso completo involucra dos pasos: primero, `python convert_checkpoint.py --model_dir <ckpt_dir> --output_dir <checkpoint_dir> --dtype bfloat16` convierte los pesos al formato interno de TRT-LLM; segundo, `trtllm-build --checkpoint-dir <checkpoint_dir> --output-dir <engine_dir> --gemm-plugin float16 --max-batch-size 32 --max-input-len 2048 --max-output-len 512` compila el engine. Este proceso tarda entre 30 y 90 minutos para modelos de 7B-70B y produce un archivo `.engine` que solo funciona en la GPU exacta en que fue compilado, con los parámetros de forma exactos especificados en el build.

La segunda fase es la inferencia, donde el engine compilado se ejecuta con el executor de TRT-LLM a través de la integración con Triton usando el backend `tensorrtllm_backend`. Una vez compilado, el engine ejecuta las mismas operaciones que vLLM pero con una eficiencia dramáticamente mayor: en H100 con precisión FP8 nativa (activada con `--use-fp8-context-fmha` durante la compilación), TRT-LLM logra throughput entre 2x y 3.5x superior a vLLM en BF16 para cargas de alta concurrencia en modelos de 7B-70B. Esta mejora proviene de la fusión de kernels (múltiples operaciones de PyTorch que se ejecutan como kernels CUDA separados se funden en un único kernel optimizado), de la eliminación del overhead de JIT compilation de PyTorch, y del uso de las instrucciones de hardware específicas más eficientes para cada operación en la GPU compilada.

La restricción más importante de TRT-LLM es la especificidad del engine compilado. El mismo modelo compilado en una A100 con `max-batch-size 32` no funciona en una H100, no puede procesar batches de 64 requests, y no puede aceptar inputs más largos que `max-input-len 2048`. Cada cambio en cualquiera de estos parámetros requiere recompilación completa. Esto convierte el proceso de despliegue en una operación más rígida que vLLM: actualizar el modelo base implica recompilación de 30-90 minutos, escalar el batch máximo para un pico de tráfico requiere tener un engine pre-compilado con el nuevo tamaño, y migrar entre tipos de GPU requiere recompilar para cada uno.

El análisis costo-beneficio de TRT-LLM vs vLLM es claro: para organizaciones donde el throughput por GPU-hora determina directamente la rentabilidad del producto (servicios de IA que cobran por token y tienen márgenes ajustados), el 2-3x de mejora de TRT-LLM se traduce directamente en 2-3x más ingresos por unidad de hardware, amortizando el costo operativo adicional de compilación y la rigidez del despliegue en poco tiempo.

## Componentes técnicos de TRT-LLM

- **Proceso de build:** conversión de checkpoint con `convert_checkpoint.py` seguida de compilación con `trtllm-build`; 30-90 minutos para modelos de 7B-70B; engine específico para GPU y parámetros de forma.
- **Plugins optimizados:** `--gemm-plugin float16/bfloat16/float8` activa kernels GEMM optimizados de cuBLAS-LT; `--gpt-attention-plugin` activa Flash Attention y KV cache paginado; `--remove-input-padding` elimina padding en batches con longitudes variables.
- **Precisión FP8 en H100:** `--use-fp8-context-fmha` con calibración previa; incrementa throughput 40-80% respecto a FP16 con degradación de calidad mínima en modelos de 7B+.
- **Integración con Triton:** engines desplegados via backend `tensorrtllm_backend`; configuración de `config.pbtxt` para rutas a engines, instancias y parámetros del executor.
- **Speculative decoding:** soporte para Medusa heads, Eagle drafts y modelos draft separados; aceleración de 2-4x en generación dependiendo del dominio.

> **Nota del Arquitecto:** TRT-LLM es la herramienta correcta cuando ya tienes vLLM en producción, has medido el throughput real con las métricas de Prometheus, y calculas que el 2-3x de mejora de TRT-LLM recupera su costo de implementación (tiempo de ingeniero + rigidez operativa) en menos de 3 meses. Sin ese análisis de ROI, la complejidad adicional no se justifica: vLLM con prefix caching y chunked prefill ya resuelve el 90% de los problemas de throughput.

TRT-LLM cierra el espectro de motores de serving para máxima eficiencia en NVIDIA. La sección siguiente establece el lenguaje común de métricas (TTFT, TBT, throughput) que permite comparar objetivamente el rendimiento de cualquier motor de serving.

---
