# Módulo 8 – Capítulo 05 – Sección 05

# Métricas de serving: throughput (tokens/s), latencia TTFT y latencia TBT

Las métricas de rendimiento de un sistema de serving de LLMs se dividen en dos dimensiones ortogonales: las métricas de latencia que importan para la experiencia de usuario individual (TTFT y TBT) y las métricas de throughput que determinan la eficiencia económica del sistema (tokens por segundo por GPU). El Time To First Token (TTFT) mide el tiempo desde que se recibe una request hasta que se genera el primer token de la respuesta; incluye el tiempo de cola, el tiempo de prefill (procesar todos los tokens de entrada en la GPU) y el overhead del sistema; para aplicaciones interactivas, un TTFT menor a 200-300ms es percibido como "inmediato" por los usuarios. El Time Between Tokens (TBT), también llamado inter-token latency, mide el tiempo entre tokens consecutivos en la fase de decode; para texto que aparece fluidamente en una interfaz, el TBT debe ser inferior a 50-80ms (equivalente a 12-20 tokens/s por request), ya que latencias mayores producen la percepción de "typing lento". El throughput total del sistema (tokens/s agregados) es la métrica económica: determina cuántos tokens se pueden generar por hora en un GPU, lo que directamente determina el costo por millón de tokens (CPMTokens) y la capacidad máxima de usuarios concurrentes del sistema.

## Métricas clave de serving de LLMs

- TTFT (Time To First Token): incluye latencia de red + tiempo en cola + tiempo de prefill; el tiempo de prefill crece linealmente con la longitud del input (prompt tokens); en vLLM con chunked prefill, requests largas no bloquean el decode de otras requests
- TBT (Time Between Tokens): determinado principalmente por el tiempo de una iteración de decode; depende del tamaño del modelo, la GPU y el batch size actual; con continuous batching, el TBT de una request individual aumenta cuando el batch tiene más requests simultáneas
- Throughput agregado (tokens/s): la métrica de eficiencia de infraestructura; un A100 con vLLM sirve Llama 3 8B a ~2.000-3.000 tokens/s en modo batch; un H100 con TRT-LLM puede superar 6.000-8.000 tokens/s
- E2E latency (latencia end-to-end): suma de TTFT + (TBT × output_tokens); relevante para aplicaciones que necesitan la respuesta completa antes de procesarla (clasificación, extracción de datos)
- P50/P95/P99 vs promedio: los percentiles son más representativos que el promedio para métricas de latencia; el P99 de TTFT indica el peor caso experimentado por el 1% de los usuarios; SLOs de producción se definen típicamente sobre P95 y P99

## Para recordar

Define los SLOs de serving en términos de TTFT-P95 y TBT-P95 antes de seleccionar el motor de serving y el hardware: estos dos números determinan si un modelo es viable para tu caso de uso sin importar cuán impresionante sea su throughput máximo en benchmark.
