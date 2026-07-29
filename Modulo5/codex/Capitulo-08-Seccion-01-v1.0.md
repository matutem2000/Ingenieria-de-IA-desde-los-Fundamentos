# Módulo 5 – Capítulo 08 – Sección 01

# Pilares de la observabilidad: trazas, métricas y logs en sistemas de IA

La observabilidad de un sistema de IA extiende los tres pilares del modelo de observabilidad de software distribuido (trazas, métricas, logs) con la dimensión específica de IA: el contenido y la calidad de los prompts y respuestas, que no tienen equivalente en sistemas de software tradicionales. Las trazas distribuidas capturan el ciclo de vida completo de un request de IA: desde la entrada del usuario hasta cada llamada al LLM, cada consulta al vector store, cada invocación de herramienta, y la respuesta final, con timing de cada segmento. Las métricas son series temporales de agregados: tokens por minuto, latencia P50/P95/P99, tasa de errores, costo por request, score de calidad promedio; permiten detectar tendencias y anomalías que los logs individuales no revelan. Los logs estructurados capturan los detalles de cada evento: el prompt completo, la respuesta, los tokens de entrada y salida, el `request_id`, el `model_id`, el `user_id` y cualquier metadata de negocio relevante, en formato JSON parseable por ElasticSearch, Datadog o CloudWatch Logs Insights. La instrumentación efectiva de los tres pilares simultáneamente es lo que convierte un sistema de IA opaco en uno que puede diagnosticarse, optimizarse y mejorarse con evidencia objetiva.

## Conceptos clave de la observabilidad en IA

- Traza completa de un request RAG: `span[http_request] → span[retriever] → span[vector_db_query] → span[llm_call] → span[parser] → span[response]`, con el tiempo de cada span y los tokens consumidos en `span[llm_call]`
- Métricas de negocio vs métricas técnicas: además de latencia y errores, capturar métricas de negocio como tasa de resolución en primer turno, tasa de abandono de sesión, y score de satisfacción del usuario que conectan la operación técnica con el valor del sistema
- Logs estructurados en JSON: `{"timestamp": "...", "request_id": "...", "model": "...", "input_tokens": 1250, "output_tokens": 342, "latency_ms": 2840, "cost_usd": 0.0087, "user_id": "...", "session_id": "..."}` permite queries SQL-like en cualquier plataforma de logging
- Cardinality del tracing: los sistemas de IA con muchos usuarios tienen alta cardinality en atributos como `user_id` y `session_id`; configurar el sampling rate del tracing (ej. 10% del tráfico en producción) evita el costo prohibitivo de tracear el 100%
- Correlación entre pilares: el `request_id` como campo común en trazas, métricas y logs permite correlacionar un spike de latencia en métricas con los logs específicos de los requests afectados y las trazas que muestran qué span fue el cuello de botella

## Principio rector

Un sistema de IA sin los tres pilares de observabilidad instrumentados desde el primer despliegue es un sistema que requerirá instrumentación de emergencia durante un incidente, que es el peor momento posible para añadir observabilidad.
