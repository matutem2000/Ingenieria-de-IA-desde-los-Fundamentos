# Módulo 7 – Capítulo 04 – Sección 02

# Memoria de corto plazo: gestión del historial de conversación en la ventana de contexto

La memoria de corto plazo de un agente es su ventana de contexto activa: el conjunto de tokens que el LLM recibe como entrada en cada llamada de inferencia y que incluye el system prompt, el historial de mensajes, los resultados de herramientas y cualquier contexto adicional inyectado. A medida que la conversación avanza o la cadena de acciones se alarga, el historial crece y amenaza superar el límite de la ventana de contexto, lo que requiere estrategias explícitas de gestión: truncación de mensajes más antiguos (rolling window), summarization del historial (comprimir N mensajes en un resumen conciso), o extracción selectiva de información relevante. LangChain implementa este patrón mediante `ConversationSummaryMemory` y `ConversationBufferWindowMemory`; LangGraph permite customizar la función de reducción del estado para controlar qué información persiste entre iteraciones. El lost-in-the-middle problem —la dificultad de los LLMs para atender a información en el medio de contextos largos— es un argumento adicional para mantener el historial acotado y la información crítica cerca del comienzo o el final del contexto.

## Aspectos técnicos

- **Rolling window**: mantener solo los últimos k mensajes en el contexto (k=10-20 típicamente); simple de implementar pero puede perder información crítica de mensajes anteriores si no se compensas con summarization
- **Summarization del historial**: cuando el historial supera un umbral de tokens (p.ej. 80% de la ventana), comprimir los mensajes más antiguos en un resumen usando una llamada LLM separada; costo adicional pero preserva información semántica importante
- **Extracción de entidades**: en lugar de resumir, extraer y mantener entidades clave mencionadas en mensajes anteriores (nombres, fechas, IDs, decisiones tomadas) como un bloque de "hechos establecidos" al inicio del contexto
- **Token counting**: calcular el número de tokens del historial antes de cada llamada al LLM usando la librería `tiktoken` (OpenAI) o el método `count_tokens` de las APIs de Anthropic y Google; evitar llamadas que excedan el límite y produzcan errores 400
- **Priorización de información reciente**: los LLMs atienden mejor a la información al inicio y al final del contexto; colocar el sistema prompt y las instrucciones críticas al inicio, y la última acción/observación al final, para maximizar la atención del modelo sobre la información más relevante

## Buena práctica

Monitorear en producción la distribución de longitud de contexto por sesión y configurar alertas cuando el percentil 95 supere el 70% de la ventana disponible: ese umbral señala que la estrategia de gestión de memoria de corto plazo está próxima a fallar.
