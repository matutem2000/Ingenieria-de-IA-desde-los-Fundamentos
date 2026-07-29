# Módulo 10 – Capítulo 07 – Sección 04

# Caching en el gateway: reducción de costos para peticiones repetidas

El caching en un LLM Gateway es una de las optimizaciones de costo más efectivas disponibles: para aplicaciones donde los mismos prompts o prompts muy similares se envían repetidamente (documentación generada con el mismo template, respuestas a FAQ, generación de contenido estructurado con el mismo schema), retornar respuestas cacheadas puede reducir el costo de inferencia entre un 20% y un 90% dependiendo del ratio de cache hit. Existen dos niveles de caching para LLMs: exact matching cache (almacena la respuesta para un prompt exactamente igual usando el hash SHA256 del prompt + sistema de caché como Redis o Memcached) y semantic cache (almacena respuestas para prompts semánticamente similares usando embeddings + búsqueda por similitud coseno en una base de datos vectorial como Pinecone, Weaviate o Redis con el módulo RedisSearch). El exact cache es trivial de implementar y tiene cero riesgo de retornar respuestas incorrectas, pero su hit rate es bajo en aplicaciones con prompts variables; el semantic cache puede tener hit rates significativamente más altos pero introduce riesgo de retornar respuestas de un prompt anterior para un prompt diferente, requiriendo un umbral de similitud (típicamente cosine similarity > 0.95) calibrado cuidadosamente para evitar falsos positivos. Las consideraciones de TTL (time-to-live) son críticas: las respuestas en caché deben invalidarse cuando el modelo subyacente cambia de versión, cuando el contexto del sistema (system prompt) cambia, y cuando el TTL de negocio del contenido generado expira.

## Aspectos técnicos del caching en LLM Gateway

- Exact match cache: hash SHA256 del (model_name + system_prompt + user_message) como clave de Redis; TTL configurable por modelo (más corto para modelos que se actualizan frecuentemente, más largo para modelos estables)
- Semantic cache: embedding del prompt con un modelo de embedding liviano (text-embedding-3-small, all-MiniLM-L6-v2); búsqueda de nearest neighbor con threshold de similitud; retorna respuesta cacheada si similarity > 0.95
- Cache key design: incluir en la clave todos los parámetros que afectan la respuesta: model, temperature, max_tokens, system_prompt hash, user_message; excluir metadatos que no afectan la respuesta (request_id, timestamp)
- Invalidación por versión de modelo: al actualizar un modelo en el registry, invalidar automáticamente todas las entradas de caché asociadas a esa versión; usar prefijos de clave por versión para facilitar invalidación masiva
- Cache analytics: medir hit rate global y por equipo, distribución de TTL efectivo de las entradas, y savings estimados (tokens evitados × precio/token); exponer estas métricas en el dashboard de FinOps de la plataforma

## Buena práctica

El threshold de similitud del semantic cache debe calibrarse con datos reales de producción: empezar conservadoramente (0.98) y bajar gradualmente mientras se valida que las respuestas retornadas son apropiadas para los prompts que disparan el cache hit.
