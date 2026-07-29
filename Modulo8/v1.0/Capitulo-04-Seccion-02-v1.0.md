# Módulo 8 – Capítulo 04 – Sección 02

## VRAM como restricción principal: calcular los requisitos de memoria por modelo y cuantización

El Capítulo 2 estableció la fórmula canónica de VRAM para los pesos del modelo: `parámetros × bits_cuantización / 8 / 1e9`. Esta fórmula es el punto de partida del análisis de memoria, pero es insuficiente para planificar un despliegue real porque omite el componente que frecuentemente causa los OOM errors en producción: el KV cache. Los pesos del modelo son estáticos —se cargan una vez y permanecen en memoria mientras el servidor está activo— pero el KV cache crece con cada petición activa, se multiplica con el número de peticiones concurrentes y escala con la longitud del contexto. Un equipo que planifica la VRAM solo considerando los pesos puede encontrar que su modelo de 7B en Q4_K_M, que ocupa 3.5 GB de pesos, necesita 6-8 GB de VRAM total cuando se incluye el KV cache para servir cuatro peticiones simultáneas con contexto de 4096 tokens.

La fórmula de VRAM para el KV cache de una petición activa es:

```
KV_bytes = 2 × n_layers × n_heads × head_dim × context_tokens × bytes_por_elemento
```

Para Llama 3 8B con sus 32 capas, 32 cabezas de atención, dimensión de cabeza de 128 y contexto de 8192 tokens en FP16 (2 bytes por elemento):

```
KV_bytes = 2 × 32 × 32 × 128 × 8192 × 2 = 4.3 GB
```

Este cálculo explica por qué incrementar el contexto máximo tiene un costo de VRAM lineal: pasar de 4096 a 8192 tokens duplica el KV cache de esa petición. En vLLM con `--max-model-len 8192`, el engine reserva VRAM para el KV cache pool asumiendo que el sistema puede estar sirviendo hasta N peticiones simultáneas con contextos de esa longitud máxima. Si se especifica `--gpu-memory-utilization 0.9` en un servidor con 24 GB de VRAM, con el modelo de 7B Q4 ocupando 3.5 GB, quedan ~18 GB disponibles para el KV cache pool —suficiente para aproximadamente 4-5 peticiones simultáneas con contexto de 8192 tokens en FP16.

Los modelos con GQA (Grouped Query Attention), como Llama 3, reducen el tamaño del KV cache significativamente respecto a la atención multi-cabeza estándar. En Llama 3 8B, el número de cabezas de atención de las claves y valores (KV heads) es 8 en lugar de las 32 cabezas de query, lo que reduce el KV cache a un cuarto del tamaño que tendría con atención multi-cabeza completa. Esta es una de las razones por las que los modelos con GQA son más eficientes en serving concurrente: el mismo hardware puede servir más peticiones simultáneas con el mismo presupuesto de VRAM.

El overhead del framework es el tercer componente de memoria, frecuentemente fijo entre 500 MB y 1.5 GB dependiendo del runtime: el contexto CUDA reserva ~500 MB en GPUs NVIDIA, el PyTorch memory allocator retiene bloques liberados para reutilización futura, y vLLM mantiene buffers internos para el scheduler y el continuous batching. La regla práctica es añadir un 10-15% al total de pesos + KV cache para este overhead, verificando siempre con `nvidia-smi` tras el inicio del servidor que los números coinciden con la planificación.

## Cálculo de requisitos de VRAM

- **Fórmula de pesos** (de Cap. 2): `VRAM_pesos = parámetros × bits_cuantización / 8 / 1e9`; para 7B Q4: 3.5 GB; Q8: 7 GB; BF16: 14 GB.
- **KV cache por petición:** `2 × n_layers × n_heads_kv × head_dim × context_len × bytes_por_elemento`; para Llama 3 8B con 8K tokens en FP16: ~4.3 GB; con GQA (8 KV heads): ~1.1 GB.
- **Overhead del framework:** 10-15% adicional sobre pesos + KV cache; ~500 MB a 1.5 GB fijos para el runtime CUDA/Metal.
- **VRAM para fine-tuning con QLoRA:** modelo base en NF4 (mitad que BF16) + gradientes de adaptadores LoRA + optimizador AdamW 8-bit = ~8 GB mínimo para fine-tuning de 7B.
- **Multi-GPU con tensor parallelism:** vLLM con `--tensor-parallel-size=N` divide los pesos entre N GPUs; la VRAM disponible es la suma de todas, con overhead de comunicación que reduce el throughput efectivo ~10-15%.

> **Nota del Arquitecto:** El error de planificación de VRAM más común que he visto es ignorar el KV cache y lanzar el servidor solo para obtener un OOM error al recibir las primeras peticiones largas. El proceso correcto es: (1) calcular VRAM_pesos con la fórmula del Cap. 2; (2) calcular el KV cache máximo para el número de peticiones concurrentes esperadas con el contexto máximo del producto; (3) sumar el overhead del 12%; (4) comparar con la VRAM disponible; (5) si no cabe, reducir la longitud máxima de contexto o el número de peticiones concurrentes antes de cambiar el hardware.

Con la fórmula completa de VRAM en mano, el AI Engineer puede planificar el hardware de cualquier despliegue con precisión. La sección siguiente traduce este análisis cuantitativo al catálogo de GPUs disponibles en el mercado en 2025, con sus características técnicas concretas.

---
