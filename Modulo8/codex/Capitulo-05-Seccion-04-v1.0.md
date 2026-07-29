# Módulo 8 – Capítulo 05 – Sección 04

# TensorRT-LLM: optimización de inferencia para GPUs NVIDIA

TensorRT-LLM (TRT-LLM) es la librería de NVIDIA para compilar y ejecutar LLMs con la máxima eficiencia posible en GPUs NVIDIA, aplicando un conjunto de optimizaciones a nivel de grafo y kernel que van más allá de lo que puede lograr PyTorch estándar: fusión de kernels para eliminar launches de GPU intermedios, operaciones en FP8 con Transformer Engine en H100/H200, paginación eficiente del KV cache y compilación ahead-of-time que elimina el overhead de JIT durante la inferencia. El proceso de uso de TRT-LLM comienza compilando el modelo a un engine TensorRT específico para la GPU objetivo y la precisión elegida: `trtllm-build --checkpoint-dir <ckpt> --output-dir <engine> --gemm-plugin float16 --max-batch-size 32 --max-input-len 2048 --max-output-len 512` genera un archivo `.engine` compilado para la GPU disponible. Los engines TRT-LLM son específicos de la GPU en que fueron compilados y de los parámetros de forma (batch size, secuencia máxima): un engine compilado en una A100 con batch_size=32 no funciona en una H100, ni puede servir batches de 64 sin recompilación. En benchmarks de NVIDIA, TRT-LLM sobre H100 con FP8 logra throughput entre 2x y 3.5x superior a vLLM en BF16 para modelos de 7B-70B en cargas de alta concurrencia, justificando la complejidad adicional de compilación en contextos donde el costo por token es crítico.

## Componentes técnicos de TRT-LLM

- Proceso de build: primero se convierte el modelo a checkpoint TRT-LLM con `convert_checkpoint.py`, luego se compila con `trtllm-build`; el proceso completo para Llama 3 70B en FP8 en 4 H100 tarda entre 30 y 90 minutos
- Plugins optimizados: `--gemm-plugin float16/bfloat16/float8` activa kernels GEMM optimizados de cuBLAS-LT; `--gpt-attention-plugin` activa Flash Attention y KV cache paginado integrado; `--remove-input-padding` elimina padding de tokens de relleno para eficiencia en batches con longitudes variables
- Precisión FP8 en H100: `--use-fp8-context-fmha` habilita atención en FP8; requiere calibración con dataset representativo vía `quantize.py --calib-dataset cnn_dailymail --dtype float8`; incrementa throughput 40-80% respecto a FP16 con degradación de calidad mínima
- Integración con Triton: los engines TRT-LLM se despliegan en Triton vía el backend `tensorrtllm_backend`; la configuración `config.pbtxt` especifica rutas a los engines, número de instancias y parámetros del executor de TRT-LLM
- Speculative decoding en TRT-LLM: soporte para Medusa heads (múltiples cabezas de predicción paralela), Eagle drafts y modelos draft separados; puede acelerar la generación 2-4x dependiendo del dominio y la tasa de aceptación

## Para recordar

TRT-LLM es la opción de máximo rendimiento en GPUs NVIDIA para producción de alta demanda: el overhead de compilación (30-90 minutos por modelo y configuración) se amortiza rápidamente cuando el throughput y el costo por token son métricas críticas del negocio.
