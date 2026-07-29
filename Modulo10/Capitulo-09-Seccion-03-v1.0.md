# Módulo 10 – Capítulo 09 – Sección 03

# Optimización de inferencia: batching, caché y selección de modelo por tier de calidad

La optimización del costo de inferencia es el área de mayor impacto económico en la mayoría de las plataformas de IA, porque el costo de inferencia escala linealmente con el volumen de uso mientras que el costo de entrenamiento es puntual. Las tres estrategias de optimización más efectivas son: batching (agrupar múltiples requests en un solo forward pass del modelo), caching (retornar respuestas previas para requests idénticos o semánticamente similares), y tiering (seleccionar el modelo más barato que sea suficientemente bueno para cada tipo de request). El batching dinámico (dynamic batching o continuous batching) es la optimización más importante para throughput en modelos self-hosted: servidores como vLLM implementan continuous batching que procesa múltiples requests simultáneamente rellenando los slots disponibles en el batch conforme se completan requests anteriores, pudiendo aumentar el throughput de un GPU hasta 10-23x respecto a servir requests de uno en uno; Triton Inference Server también soporta dynamic batching con `preferred_batch_size` configurable. El tiering de modelos es la optimización más impactante para costo en aplicaciones que usan APIs externas: definir cuándo usar GPT-4o vs GPT-4o-mini vs un modelo fine-tuneado self-hosted, basándose en un análisis de la complejidad de la tarea, puede reducir el costo en un 80-90% manteniendo la calidad aceptable para la mayoría de las requests.

## Estrategias de optimización de costos de inferencia

- Continuous batching (vLLM): el motor de inferencia procesa múltiples requests en paralelo con PagedAttention para gestionar el KV cache de forma eficiente; aumenta throughput hasta 23x vs serving secuencial sin impacto en TTFT
- Semantic caching: embeddings + búsqueda vectorial para retornar respuestas cacheadas para prompts similares; efectivo en aplicaciones con consultas repetitivas (FAQ, generación templated); puede reducir costos 30-70% con threshold de similitud bien calibrado
- Model tiering: clasificar requests por complejidad (simple: clasificación, extracción; compleja: razonamiento, generación creativa) y enrutar a modelos de diferente tier; GPT-4o-mini es 20x más barato que GPT-4o con calidad equivalente para el 60-80% de las tareas
- Prompt compression: técnicas de compresión del contexto (LLMLingua, Selective Context) que reducen el número de tokens del prompt manteniendo la información relevante; puede reducir tokens de input un 20-40% para prompts largos
- Quantization para modelos self-hosted: INT8 (GPTQ, AWQ) o INT4 quantization de modelos de Hugging Face reduce los requerimientos de VRAM a la mitad y aumenta throughput 1.5-2x con degradación de calidad de <2% en la mayoría de las tareas

## Para recordar

La optimización del costo de inferencia no es una tarea única: es un proceso continuo de perfilado del uso real en producción (qué tipos de requests, qué modelos, qué tamaños de contexto) y calibración de las estrategias de optimización basadas en esos datos reales.
