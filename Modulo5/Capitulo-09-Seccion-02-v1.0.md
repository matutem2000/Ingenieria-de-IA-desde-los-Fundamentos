# Módulo 5 – Capítulo 09 – Sección 02

# Estrategias de reducción: compresión de contexto, caché semántica y batching

Las estrategias de reducción de costo en sistemas de IA atacan el problema desde tres ángulos: reducir la cantidad de tokens enviados en cada llamada (compresión de contexto), reutilizar respuestas de llamadas anteriores cuando la pregunta es suficientemente similar (caché semántica), y consolidar múltiples peticiones en una sola llamada cuando el caso de uso lo permite (batching). La compresión de contexto en sistemas conversacionales implementa un sliding window sobre el historial: mantener los últimos K turnos completos y un resumen comprimido de los turnos anteriores, donde el resumen se genera con el propio LLM a temperatura 0 y cuesta entre el 10% y 20% de los tokens originales. La caché semántica va más allá del caching de prefijos del proveedor: almacena en Redis o en un vector store los embeddings de preguntas previas y sus respuestas; cuando una nueva pregunta tiene una similitud coseno > threshold (ej. 0.95) con una pregunta cacheada, se devuelve la respuesta cacheada sin llamar al LLM; para preguntas frecuentes en dominios estables (FAQs, consultas sobre productos fijos), la hit rate puede superar el 40%, con ahorro equivalente en costo.

## Estrategias técnicas de reducción de costos

- Compresión de historial conversacional: definir `MAX_CONTEXT_TOKENS = 8000` (ajustable); calcular `total_tokens = sum(count_tokens(m) for m in messages)`; cuando supera el umbral, comprimir los mensajes más antiguos con `llm.compress_history(old_messages)` y reemplazarlos por el resumen
- Caché semántica con Redis + embeddings: generar embedding de la query del usuario (`text-embedding-3-small`, 1536 dims), buscar en Redis con `redis.FT.SEARCH` o en Qdrant por similitud coseno, devolver la respuesta cacheada si `score > 0.95`; el TTL del caché debe alinearse con la frecuencia de cambio de los datos del dominio
- Batching de requests independientes: para N documentos que deben procesarse con el mismo prompt (clasificación, extracción, resumen), construir un único prompt con todos los documentos separados por delimitadores XML en lugar de N llamadas individuales; reduce overhead por request y puede usar tokens de sistema compartidos
- Truncación selectiva de documentos RAG: en lugar de incluir el documento completo en el contexto, incluir solo los chunks más relevantes con score > threshold; reducir de 5 chunks a 3 chunks de 500 tokens cada uno puede ahorrar 1.000 tokens de entrada por request
- Reuse de prefix en multi-turno: en sistemas con system prompt largo (>1.000 tokens) y contexto de documentos fijo, usar prompt caching del proveedor para que el prefix se cachée y las sucesivas llamadas en la misma sesión paguen solo el costo de cache read

## Buena práctica

Medir el impacto de cada estrategia de reducción de costo con el sistema de observabilidad antes de implementarla: la compresión de contexto reduce costo pero puede degradar la calidad si el resumen pierde información crítica; instrumentar la evaluación de calidad antes y después de cada optimización es la única forma de confirmar que el ahorro no degrada la experiencia.
