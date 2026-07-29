# Módulo 5 – Capítulo 04 – Sección 04

# Manejo de estado y sesión en aplicaciones conversacionales

Las aplicaciones conversacionales con LLMs son inherentemente stateful: cada turno de la conversación requiere acceso al historial previo para mantener coherencia, lo que contrasta con el modelo stateless de las APIs REST donde cada request es independiente. El historial conversacional se mantiene en el cliente (el frontend envía todo el historial en cada request), en el servidor en memoria (adecuado solo para sesiones cortas de un único proceso), o en una capa de persistencia externa como Redis (para sesiones cortas con TTL de horas) o una base de datos relacional o documental (para historial permanente recuperable por sesión y usuario). La ventana de contexto del modelo es el límite físico del historial: con Claude 3.5 Sonnet (200K tokens) y conversaciones largas, cada turno del usuario puede costar entre 1.000 y 50.000 tokens de entrada dependiendo del historial acumulado, por lo que es necesario implementar estrategias de compresión: sliding window (mantener solo los últimos N turnos), summarization (comprimir el historial anterior con el propio LLM) o RAG sobre el historial (recuperar solo los turnos semánticamente relevantes).

## Componentes principales del manejo de estado conversacional

- Estructura de sesión: `{session_id, user_id, created_at, last_active, messages: [{role, content, timestamp, tokens}], metadata: {model, total_tokens}}` almacenada en Redis (hash o JSON) con TTL de 24-48 horas para sesiones activas
- Redis para sesiones con TTL: `redis.setex(f"session:{session_id}", 86400, json.dumps(session_data))` y `redis.get()` para recuperar; el TTL automático elimina sesiones inactivas sin requerir un job de limpieza explícito
- Compresión por sliding window: mantener los últimos K turnos completos y un resumen del historial anterior; `messages[-2*k:]` + `summary_message` controla el crecimiento del contexto con costo predecible
- Compresión por summarization: usar el propio LLM con `temperature=0` para generar un resumen del historial cuando supera un umbral de tokens (`if total_tokens > threshold: summary = llm.summarize(old_messages)`)
- Sesiones multi-dispositivo: usar `user_id` como clave de sesión en lugar de `session_id` de browser para que el historial sea consistente entre dispositivos del mismo usuario, con locking optimista para prevenir escrituras concurrentes

## Principio rector

La estrategia de gestión de sesión determina directamente el costo de cada turno conversacional y la calidad de la coherencia del diálogo; diseñarla antes de la primera línea de código de la UI previene refactorizaciones costosas en producción.
