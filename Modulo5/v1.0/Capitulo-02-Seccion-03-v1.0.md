# Módulo 5 – Capítulo 02 – Sección 03

## Streaming de respuestas: implementación y casos de uso

Cuando un usuario envía un mensaje a un asistente conversacional y ve la pantalla en blanco durante cinco segundos antes de que aparezca cualquier texto, la experiencia percibida es la de un sistema lento, aunque el tiempo total de generación sea idéntico al de un sistema que transmite tokens en tiempo real. Esta diferencia de percepción es la razón fundamental por la que el streaming es el modo de entrega estándar en interfaces conversacionales: no reduce el tiempo de generación total, sino que elimina la espera en blanco al entregar el primer token entre 200 y 800 milisegundos después de enviar el request.

El mecanismo técnico detrás del streaming es Server-Sent Events (SSE), un protocolo HTTP donde el servidor mantiene la conexión abierta y envía eventos delimitados por `data: {...}\n\n` a medida que los tokens se generan. Cuando el cliente activa `stream=True` en OpenAI, recibe un iterador de objetos `ChatCompletionChunk` donde cada chunk tiene un campo `choices[0].delta.content` con el fragmento de texto generado. En Anthropic, el patrón preferido es el context manager: `with client.messages.stream(...) as stream: for text in stream.text_stream:`, que proporciona un iterador de strings directamente, ocultando la complejidad de los eventos SSE subyacentes. En ambos casos, acumular el texto completo para procesamiento posterior requiere concatenar manualmente los fragmentos en un buffer.

Exponer streaming desde un servidor FastAPI al cliente web requiere menos código de lo que parece: `StreamingResponse` con `media_type="text/event-stream"` y un generador `async` que re-transmite los chunks del proveedor hacia el cliente. Esta arquitectura de proxy de streaming tiene una ventaja importante: el servidor puede aplicar transformaciones sobre los chunks antes de enviarlos (redactar PII, filtrar contenido, enriquecer con metadata) sin que el cliente perciba latencia adicional.

El streaming tiene implicaciones importantes en el manejo de errores que no existen en el modo no-streaming. Si el modelo está generando JSON y la conexión se interrumpe a mitad de la respuesta, el JSON parcial es inválido. Los sistemas que necesitan parsear JSON deben acumular el stream completo antes de intentar el parseo, no parsearlo incrementalmente. De manera similar, los tool calls llegan como deltas de JSON que se van acumulando hasta que el evento `finish_reason: "tool_calls"` indica que el bloque está completo y puede parsearse. Este manejo diferente de las respuestas estructuradas en modo streaming vs modo completo es uno de los aspectos más frecuentes de error en la implementación inicial.

Los timeouts en conexiones streaming merecen configuración explícita. Un proxy inverso o un load balancer con timeout de lectura de 60 segundos cerrará silenciosamente una conexión SSE si no llega ningún byte en ese intervalo, lo que ocurre en respuestas largas. La solución es configurar `timeout=httpx.Timeout(connect=10, read=300)` en el cliente HTTP subyacente y, en el lado del servidor, enviar comentarios SSE keep-alive periódicos (`: keep-alive\n\n`) si la arquitectura de red lo requiere.

## Aspectos técnicos del streaming

- **Implementación en Python (OpenAI):** iterar sobre el stream devuelve objetos `ChatCompletionChunk`; el texto está en `chunk.choices[0].delta.content`; acumular con `full_text += chunk.choices[0].delta.content or ""` construye la respuesta completa.
- **Context manager en Anthropic:** `with client.messages.stream(...) as stream:` expone `stream.text_stream` para texto puro y `stream.get_final_message()` para obtener el objeto `Message` completo con tokens y metadatos al finalizar.
- **FastAPI StreamingResponse:** generador async que yield-ea `f"data: {json.dumps({'text': chunk})}\n\n"` con `media_type="text/event-stream"` permite re-transmitir el stream del proveedor al cliente web de forma proxied.
- **Tool calls en streaming:** acumular los deltas de JSON del tool call en un buffer hasta `finish_reason == "tool_calls"`, luego parsear el buffer completo; nunca parsear deltas parciales de JSON.
- **Casos donde no usar streaming:** pipelines batch donde la respuesta se procesa antes de continuar (extracción de JSON, clasificación, embeddings) no se benefician del streaming y añaden complejidad de manejo de buffer sin ventaja de UX.

> **Nota del Arquitecto:** Los experimentos de A/B testing sobre interfaces conversacionales muestran consistentemente que la tasa de abandono sube entre el 15% y el 30% cuando se reemplaza streaming por respuesta completa, incluso manteniendo idéntico el tiempo total de generación. El usuario que ve texto aparecer progresivamente percibe que el sistema está trabajando; el usuario que ve una pantalla en blanco durante el mismo intervalo percibe que el sistema no responde. Esta asimetría de percepción hace que el streaming sea una decisión de producto, no solo de implementación técnica.

En la sección siguiente abordaremos la gestión de errores: cómo manejar rate limits, timeouts y fallos del proveedor con estrategias de reintento que mantienen la resiliencia del sistema sin amplificar el problema ante degradaciones del servicio externo.

---

**Idea central:** El streaming no es solo una optimización de UX: en interfaces conversacionales elimina la espera en blanco que los usuarios interpretan como fallo del sistema, reduciendo la tasa de abandono y aumentando la percepción de calidad independientemente del tiempo total de generación.
