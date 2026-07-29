# Módulo 7 – Capítulo 01 – Sección 04

# El ciclo agéntico: observe → think → act → evaluate

El ciclo agéntico es el patrón de ejecución fundamental que describe cómo un agente opera en iteraciones: primero observa el estado actual del entorno (resultados de herramientas, mensajes del usuario, contexto acumulado), luego razona sobre qué hacer a continuación (generando pensamiento interno en scratchpad o usando cadenas de razonamiento explícitas), después ejecuta la acción elegida (invocando una herramienta, escribiendo código, enviando una respuesta), y finalmente evalúa si el objetivo ha sido cumplido o si debe continuar iterando. Este patrón —conocido también como el bucle de agente o agent loop— está implementado explícitamente en LangGraph como un grafo de nodos donde cada nodo representa una fase del ciclo y las aristas condicionales determinan si continuar o terminar. La eficiencia del ciclo depende de la calidad del razonamiento en la fase "think": un razonamiento deficiente genera acciones innecesarias que aumentan tokens consumidos, latencia y probabilidad de error acumulado.

## Puntos críticos

- **Observe**: recopilación y serialización del estado del entorno en el contexto del LLM; incluye resultados de llamadas previas a herramientas, historial de mensajes y cualquier dato de entrada del sistema
- **Think**: fase de razonamiento donde el LLM decide qué acción ejecutar; puede incluir scratchpad interno (pensamiento en voz alta), reflexión sobre intentos anteriores o planificación de sub-pasos
- **Act**: ejecución de la herramienta o acción elegida; debe ser idempotente cuando sea posible para facilitar reintentos seguros ante fallos parciales
- **Evaluate**: verificación de si la tarea fue completada; puede implementarse como un LLM-judge separado, como una condición programática o como autoevaluación del mismo agente
- **Gestión de iteraciones**: el ciclo requiere un contador de pasos y una condición de parada explícita; la ausencia de estos genera bucles infinitos con consumo descontrolado de tokens y costo

## Para recordar

El ciclo observe → think → act → evaluate no es solo un patrón conceptual; en sistemas como LangGraph es un grafo de estados explícito donde cada transición es condicionalmente programada, y la ausencia de una condición de terminación es un bug de producción.
