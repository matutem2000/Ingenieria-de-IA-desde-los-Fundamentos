# Módulo 11 – Capítulo 07 – Sección 02

# Token optimization a escala: compresión de prompts, caché y batching para millones de peticiones

La optimización de tokens en sistemas de LLM enterprise opera en tres dimensiones complementarias que juntas pueden reducir el costo de inferencia entre un 40% y un 70% respecto a una implementación naïve: la compresión del prompt (reducir el número de tokens de entrada sin degradar la calidad de la respuesta), el semantic caching (evitar llamadas al LLM para peticiones similares a preguntas ya respondidas), y el batching de peticiones (agrupar múltiples peticiones independientes en una sola llamada a la API para aprovechar el throughput máximo del endpoint). La compresión de prompts tiene múltiples técnicas con diferentes trade-offs: la eliminación de tokens de relleno mediante herramientas como LLMLingua o PromptCompressor puede reducir el número de tokens del contexto en un 50-80% con una degradación de calidad del 5-15% — aceptable para algunos casos de uso (categorización, extracción de información estructurada) pero no para otros (generación de contratos, soporte médico). El semantic caching — implementado con Redis y una base de datos vectorial ligera para comparar la similitud de la pregunta actual con preguntas previamente respondidas — puede eliminar del 20% al 40% de las llamadas al LLM en sistemas con alta repetición de preguntas similares (FAQ corporativas, soporte de primer nivel), pero requiere calibrar el umbral de similitud con cuidado: un umbral demasiado bajo genera cache hits en preguntas que son semánticamente similares pero contextualmente distintas, produciendo respuestas incorrectas.

## Técnicas de optimización de tokens

- LLMLingua para compresión de contexto RAG: reduce los chunks del contexto RAG eliminando tokens de baja información (artículos, conectores, redundancias) con ratio de compresión configurable de 2x a 10x, preservando los tokens de mayor contenido semántico
- Semantic caching con Redis + pgvector: genera el embedding de cada petición entrante, busca en el caché de respuestas anteriores, y retorna la respuesta cacheada si la similitud coseno supera el threshold configurado (típicamente 0.92-0.97)
- Context window management: estrategias de selección de mensajes del historial conversacional para no superar el context window del modelo — sliding window (últimos N mensajes), summarization (resumir el historial antiguo), y message pruning (eliminar mensajes de baja relevancia para la pregunta actual)
- Batching de peticiones de embeddings: acumular documentos para indexación en batches de 100-1.000 antes de llamar a la API de embeddings, reduciendo el overhead por petición HTTP y aprovechando las tarifas de batch de OpenAI (hasta 50% de descuento)
- Prompt caching: la mayoría de los proveedores de LLM (Anthropic, OpenAI) ofrecen descuentos del 50-90% en tokens de entrada que se repiten entre peticiones (system prompt, instrucciones fijas) mediante prompt caching — activarlo explícitamente puede reducir el costo del 60-80% del prompt de sistema

## Buena práctica

Implementar un dashboard de FinOps de IA que muestre en tiempo real el costo por petición desglosado por componente (embedding, LLM input, LLM output, caching hit rate), permitiendo identificar cuáles optimizaciones tienen el mayor impacto en el costo total.
