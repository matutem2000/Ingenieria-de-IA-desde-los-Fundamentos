# Módulo 5 – Capítulo 02 – Sección 05

# Gestión de costos: conteo de tokens, caché de prompts y optimización de llamadas

El costo de consumir APIs de LLM se calcula por tokens, no por caracteres ni palabras: un token equivale aproximadamente a 4 caracteres en inglés o 2-3 en español, y cada proveedor cobra de forma diferenciada por tokens de entrada y de salida, siendo los de salida generalmente 3-5x más caros. Anthropic cobra gpt-4o a $2.50/M tokens de entrada y $10/M de salida (gpt-4o); Claude 3.5 Sonnet a $3/M entrada y $15/M salida; Claude 3.5 Haiku a $0.80/M entrada y $4/M salida. El prompt caching de Anthropic permite reutilizar prefijos de prompt marcados con `cache_control: {type: "ephemeral"}` a 10% del costo de escritura, con un ahorro del 90% en llamadas repetidas con el mismo contexto largo (documentos, instrucciones del sistema extendidas). La estimación precisa del costo antes de hacer una llamada se logra con librerías de conteo de tokens: `tiktoken` para modelos OpenAI y el método `client.messages.count_tokens()` de Anthropic SDK, que permiten calcular el costo esperado antes de ejecutar la llamada.

## Estrategias de optimización de costos en APIs de LLM

- Conteo de tokens previo: usar `tiktoken.encoding_for_model("gpt-4o").encode(text)` o `anthropic.count_tokens()` antes de llamadas costosas para detectar prompts que exceden el presupuesto o alertar sobre contextos anormalmente grandes
- Prompt caching estructurado: en Anthropic, colocar el contenido estático (instrucciones del sistema, documentos de referencia, ejemplos few-shot) al inicio del prompt con `cache_control` y el contenido variable (la pregunta del usuario) al final maximiza el hit rate del caché
- Elección de modelo por tarea: usar modelos pequeños (Haiku, gpt-4o-mini) para clasificación, extracción de entidades y tareas de routing, reservando modelos grandes para generación de contenido complejo y razonamiento multi-paso
- Batching de requests: consolidar múltiples consultas independientes en una sola llamada usando XML o JSON delimitado cuando la latencia no es crítica, reduciendo el overhead por request y el costo de tokens del sistema repetido
- Truncación inteligente de contexto: implementar algoritmos de compresión de historial conversacional (resumir turnos anteriores, eliminar mensajes irrelevantes) para mantener el contexto útil dentro de un límite de tokens predefinido

## Principio rector

El costo de los tokens de salida domina el gasto en sistemas de generación intensiva; cada token de salida innecesario es un costo evitable, por lo que prompts que instruyen al modelo a ser conciso y formatear en JSON compacto reducen costos sin degradar calidad.
