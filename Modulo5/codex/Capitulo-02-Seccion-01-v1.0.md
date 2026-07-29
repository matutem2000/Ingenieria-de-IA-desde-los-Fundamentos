# Módulo 5 – Capítulo 02 – Sección 01

# Anatomía de una llamada a la API: messages, system, role y contenido

Una llamada a la API de un LLM es un POST HTTP con un cuerpo JSON que contiene, como mínimo, el identificador del modelo y la lista de mensajes que forman la conversación; entender la semántica exacta de cada campo es la diferencia entre una integración frágil y una robusta. El campo `messages` es un array ordenado de objetos donde cada objeto tiene un `role` (`system`, `user`, `assistant`) y un `content` que puede ser una cadena simple o un array de bloques de contenido para mensajes multimodales. El rol `system` en OpenAI va como primer mensaje del array con `role: "system"`; en Anthropic se ubica fuera del array `messages` como campo de primer nivel, lo que tiene implicaciones en cómo se aplica el caching de prefijos. El campo `content` puede contener texto plano, referencias a imágenes vía URL o base64, bloques de audio (Gemini), o resultados de tool calls que cierran el ciclo de una invocación de herramienta.

## Conceptos clave de la estructura de mensajes

- Campo `model`: especifica el identificador exacto del modelo incluyendo versión (ej. `claude-3-5-sonnet-20241022`, `gpt-4o-2024-08-06`), lo que determina capacidades, ventana de contexto y costo por token
- Rol `system`: establece el comportamiento, formato de salida, restricciones y personalidad del modelo antes del turno conversacional; tiene mayor peso en el comportamiento del modelo que las instrucciones en mensajes `user`
- Rol `assistant`: representa respuestas previas del modelo en conversaciones multi-turno; también se usa para pre-fill (Anthropic) comenzando la respuesta del modelo con un prefijo controlado como `{` para forzar JSON
- Bloques de contenido multimodal: `{"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}` en OpenAI o `{"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": "..."}}` en Anthropic
- Campo `stop_sequences`: array de strings que detienen la generación cuando el modelo los produce, útil para delimitar secciones de salida estructurada o prevenir desbordamiento de formato

## Principio rector

La estructura del array `messages` es el contrato principal entre la aplicación y el modelo; mantenerla consistente y validarla antes de cada llamada previene errores sutiles de contexto que son difíciles de diagnosticar en producción.
