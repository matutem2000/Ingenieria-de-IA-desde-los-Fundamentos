# Módulo 5 – Capítulo 02 – Sección 03

# Streaming de respuestas: implementación y casos de uso

El streaming permite que la aplicación reciba y renderice tokens a medida que el modelo los genera, en lugar de esperar a que la respuesta completa esté disponible; esto reduce drásticamente la latencia percibida por el usuario en interfaces conversacionales pasando de 5-15 segundos de espera en blanco a un tiempo de first-token de 200-800ms. Los proveedores implementan streaming mediante Server-Sent Events (SSE): el servidor mantiene la conexión HTTP abierta y envía eventos `data: {...}\n\n` con deltas de tokens; el cliente consume este stream con un iterador. En OpenAI se activa con `stream=True` en `client.chat.completions.create()`; en Anthropic con el context manager `with client.messages.stream() as stream: for text in stream.text_stream:`. El streaming tiene implicaciones en el manejo de errores: si el modelo genera JSON y el streaming se interrumpe a mitad de la respuesta, el JSON parcial es inválido y debe manejarse con buffers acumuladores.

## Aspectos técnicos del streaming

- Implementación en Python: iteración sobre el stream devuelve objetos delta con `chunk.choices[0].delta.content` (OpenAI) o `event.delta.text` (Anthropic); la acumulación manual del string completo es necesaria si se requiere la respuesta entera para procesamiento posterior
- FastAPI y streaming HTTP: `StreamingResponse` con `media_type="text/event-stream"` y un generador async permite re-transmitir el stream del proveedor al cliente web en menos de 5 líneas de código
- Manejo de herramientas (tool calls) en streaming: los tool calls llegan como deltas parciales de JSON que deben acumularse antes de parsear; el stream termina con un evento `finish_reason: "tool_calls"` que indica que el modelo quiere ejecutar una herramienta
- Timeout en conexiones streaming: las conexiones SSE deben configurarse con `timeout=httpx.Timeout(connect=10, read=300)` o equivalente para tolerar respuestas largas sin que el proxy o load balancer cierre la conexión prematuramente
- Casos donde no usar streaming: en pipelines batch donde la respuesta completa se procesa antes de continuar (extracción de JSON, clasificación, embeddings), el streaming añade complejidad sin beneficio de UX y puede dificultar el manejo de errores

## Idea central

El streaming no es solo una optimización de UX: en interfaces conversacionales reduce la tasa de abandono medida en A/B tests, porque los usuarios perciben que el sistema está activo y respondiendo aunque la respuesta completa tome varios segundos.
