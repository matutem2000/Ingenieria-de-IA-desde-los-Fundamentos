# Módulo 8 – Capítulo 04 – Sección 02

# VRAM como restricción principal: calcular los requisitos de memoria por modelo y cuantización

La VRAM (Video RAM) es la restricción primaria en el despliegue de LLMs en GPU: a diferencia de la RAM del sistema, no puede ampliarse dinámicamente y su uso se divide entre los pesos del modelo, el KV cache para el contexto en proceso y el overhead del framework de inferencia. La fórmula base para estimar la VRAM necesaria para los pesos de un modelo es `parámetros × bytes_por_parámetro`: un modelo de 7B parámetros en BF16 (2 bytes) requiere 14 GB, en INT8 (1 byte) requiere 7 GB, y en INT4 (0.5 bytes efectivos) requiere 3.5 GB de pesos, más un overhead de 10-15% para buffers de activación y el framework de inferencia. El KV cache es el segundo componente de memoria y crece con el contexto: para un modelo de 7B con 32 capas, 32 cabezas de atención, dimensión de cabeza de 128 y contexto de 4096 tokens en FP16, el KV cache requiere `2 (K+V) × 32 capas × 32 cabezas × 128 dim × 4096 tokens × 2 bytes = 2.1 GB` adicionales, cantidad que se multiplica linealmente con el tamaño del contexto y el número de peticiones paralelas. Entender esta fórmula permite planificar el hardware correcto antes de intentar cargar un modelo y obtener un error de OOM (Out Of Memory) en tiempo de ejecución.

## Cálculo de requisitos de VRAM

- Fórmula de pesos: `VRAM_pesos (GB) = parámetros × bits_cuantización / 8 / 1e9`; para 7B en Q4: `7e9 × 4 / 8 / 1e9 = 3.5 GB`; en Q8: `7 GB`; en BF16: `14 GB`
- KV cache por token: `KV_cache (bytes) = 2 × n_layers × n_heads × head_dim × precision_bytes`; para Llama 3 8B con contexto de 8192 tokens en FP16: aproximadamente 4 GB de KV cache
- Regla práctica de overhead: suma 10-15% al total de pesos + KV cache para buffers de activación, gradientes temporales y el overhead del runtime (CUDA context, PyTorch memory allocator, etc.)
- VRAM para fine-tuning con QLoRA: el modelo base en NF4 (cuantización de 4 bits) ocupa la mitad que en FP16, pero los gradientes de los adaptadores LoRA y el optimizador (AdamW de 8 bits) requieren 2-3 GB adicionales; fine-tunar un 7B con QLoRA requiere un mínimo de 8 GB de VRAM
- Multi-GPU (tensor parallelism): vLLM y otros motores permiten dividir el modelo entre múltiples GPUs con `tensor_parallel_size=N`; la VRAM total disponible es la suma de todas las GPUs del grupo, pero el overhead de comunicación (NVLink o PCIe) reduce el throughput efectivo

## Para recordar

Antes de adquirir hardware o escalar a la nube, calcula la VRAM requerida con la fórmula exacta para el modelo y la cuantización elegidos: una planificación incorrecta resulta en OOM errors en tiempo de ejecución que requieren cambiar de hardware o de cuantización.
