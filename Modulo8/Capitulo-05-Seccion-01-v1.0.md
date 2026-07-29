# Módulo 8 – Capítulo 05 – Sección 01

# vLLM: PagedAttention y continuous batching para maximizar el throughput en GPU

vLLM es el motor de serving de LLMs de mayor adopción en producción GPU, desarrollado por el Sky Computing Lab de UC Berkeley, que resuelve el problema fundamental de la gestión ineficiente del KV cache mediante PagedAttention: un mecanismo inspirado en la paginación de memoria virtual del sistema operativo que divide el KV cache en bloques de tamaño fijo (páginas) asignados dinámicamente solo cuando son necesarios. Sin PagedAttention, los sistemas de inferencia tradicionales pre-reservan una región contigua de VRAM para el KV cache de cada request basada en la longitud máxima de contexto configurada, desperdiciando entre 60-80% de la VRAM en fragmentación interna; PagedAttention reduce este desperdicio a menos del 4%, permitiendo servir 3-4x más peticiones simultáneas con el mismo hardware. El continuous batching (también llamado iteration-level scheduling) de vLLM permite que requests nuevas se unan al batch en cada iteración de decode en lugar de esperar a que el batch completo termine, eliminando el problema de "bubble time" donde las GPU esperan idle a que las requests largas terminen. En benchmarks comparativos, vLLM en una A100 de 40 GB sirve Llama 2-13B con throughput de 1.500-2.000 tokens/s en modo batch, comparado con 300-400 tokens/s de Hugging Face Transformers con el mismo hardware.

## Componentes técnicos de vLLM

- PagedAttention: divide el KV cache en bloques de 16 tokens (configurable); asigna bloques desde un pool centralizado; soporta compartición de bloques entre múltiples requests que comparten el mismo prefijo (prefix caching)
- Continuous batching: el scheduler de vLLM evalúa en cada iteración qué requests pueden unirse al batch activo; una request que llega mientras otras están en decode puede empezar su prefill en el siguiente ciclo; elimina latencias de espera en cola FIFO
- Prefix caching: cuando múltiples requests comparten el mismo system prompt o prefijo largo, vLLM comparte los bloques del KV cache entre todas, reduciendo el compute de prefill y el uso de VRAM; especialmente efectivo en aplicaciones con system prompts estáticos
- Tensor parallelism: `tensor_parallel_size=N` distribuye el modelo entre N GPUs usando sharding de pesos; requiere GPUs conectadas via NVLink para máxima eficiencia; pipeline parallelism disponible para modelos que no caben en multi-GPU tensor-parallel
- Gestión de memoria dinámica: vLLM usa un mecanismo de copy-on-write para beam search y un garbage collector de bloques para liberación de memoria cuando las requests completan; el uso de VRAM es predecible y máximo por diseño

## Para recordar

vLLM es la elección por defecto para serving de LLMs en GPU en producción: PagedAttention y continuous batching no son optimizaciones opcionales sino la razón por la que el mismo hardware puede servir a 3-4x más usuarios concurrentes que alternativas tradicionales.
