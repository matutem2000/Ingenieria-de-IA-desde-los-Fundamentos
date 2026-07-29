# Módulo 7 – Capítulo 04 – Sección 03

# Memoria de largo plazo: almacenamiento persistente y recuperación selectiva

La memoria de largo plazo permite a un agente recordar información de sesiones anteriores, aprender de interacciones pasadas y mantener contexto personalizado por usuario sin que ese contexto deba estar presente en cada ventana de contexto. La implementación técnica combina almacenamiento persistente —PostgreSQL para datos estructurados, MongoDB para documentos, Redis para cache de acceso rápido— con un mecanismo de recuperación selectiva que decide qué subconjunto de la memoria disponible es relevante para la tarea actual. La recuperación selectiva puede basarse en reglas (recuperar siempre las preferencias del usuario, recuperar las últimas N sesiones), en búsqueda por metadata (filtrar por user_id, date_range, task_type) o en búsqueda semántica sobre el contenido de la memoria. Sistemas como MemGPT (ahora Letta) y el Memory Store de LangGraph Cloud implementan este patrón con APIs de lectura/escritura de memoria que el agente puede invocar como herramientas durante su ejecución.

## Aspectos técnicos

- **Schema de memoria persistente**: estructura de datos para cada unidad de memoria; mínimo recomendado: `{id, user_id, session_id, timestamp, content, type, embedding, metadata}`; el campo `type` permite filtrar por categoría (preferencia, hecho, error, decisión)
- **Write to memory trigger**: el agente debe decidir cuándo escribir en memoria de largo plazo; puede ser al final de cada sesión (batch write), cuando el agente identifica información importante durante la conversación (selective write) o de forma automática basada en reglas de extracción
- **Retrieval selectivo**: antes de cada sesión o tarea, recuperar el subconjunto más relevante de la memoria; criterios de recuperación: recencia (últimas N sesiones), relevancia semántica (top-k por similaridad coseno con la query actual), importancia (ítems marcados como high-priority)
- **Memory decay**: implementar TTL (Time-To-Live) para memorias que pierden relevancia con el tiempo; preferencias de UI del usuario pueden expirar en 30 días, mientras que hechos del dominio pueden ser permanentes
- **Privacidad y aislamiento**: la memoria debe ser estrictamente aislada por user_id; un bug de filtrado que exponga memorias de un usuario a otro es una vulnerabilidad de privacidad crítica que debe prevenirse con filtros a nivel de query, no solo de aplicación

## Principio rector

La memoria de largo plazo transforma cada nueva sesión del agente de una interacción sin contexto previo a una conversación que construye sobre el historial acumulado; pero ese poder requiere controles estrictos de privacidad, relevancia y expiración para no degradar la calidad con información obsoleta o irrelevante.
