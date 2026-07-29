# Módulo 7 – Capítulo 05 – Sección 02

# AutoGen: conversaciones multi-agente y colaboración entre especialistas

AutoGen, desarrollado por Microsoft Research, es un framework que modela la colaboración agéntica como conversaciones estructuradas entre múltiples agentes —cada uno con su propio system prompt, modelo base y conjunto de herramientas— donde los mensajes entre agentes son el mecanismo principal de coordinación. La primitiva central de AutoGen es el `ConversableAgent`: un agente que puede iniciar conversaciones, responder a otros agentes, ejecutar código en un subprocess local o Docker, y terminar la conversación cuando detecta una condición de finalización. El patrón más común en AutoGen es el duo `AssistantAgent` (LLM con herramientas y razonamiento) + `UserProxyAgent` (ejecuta código Python generado por el AssistantAgent en un entorno local y devuelve los resultados): este patrón de code execution es particularmente efectivo para tareas de análisis de datos, debugging y automatización de scripts. AutoGen 0.4 introdujo un modelo de actores asíncrono que mejora la escalabilidad de sistemas con muchos agentes concurrentes.

## Aspectos técnicos

- **ConversableAgent API**: cada agente se configura con `name`, `system_message` (su rol y capacidades), `llm_config` (modelo y herramientas) y `human_input_mode` (NEVER, TERMINATE, ALWAYS para controlar cuándo se solicita intervención humana)
- **Code execution sandbox**: el `UserProxyAgent` con `code_execution_config` ejecuta bloques de código Python extraídos de los mensajes del AssistantAgent en un subprocess local o en un contenedor Docker; los resultados se devuelven como siguiente mensaje en la conversación
- **GroupChat y GroupChatManager**: para orquestar más de dos agentes, `GroupChat` define el conjunto de participantes y `GroupChatManager` (un LLM especializado en moderación) decide qué agente debe hablar a continuación basándose en el contexto de la conversación
- **Termination conditions**: las condiciones de terminación se definen como funciones que inspeccionan el último mensaje; el patrón más común es terminar cuando el mensaje contiene "TERMINATE" o cuando se alcanza `max_turns`
- **Nested conversations**: AutoGen soporta conversaciones anidadas donde un agente puede iniciar una sub-conversación con otro agente para resolver un sub-problema, recopila el resultado y lo incorpora a la conversación principal

## Para recordar

AutoGen es especialmente efectivo para flujos donde la generación de código y su ejecución deben alternarse múltiples veces: el patrón AssistantAgent-UserProxyAgent externaliza la ejecución de código del LLM a un entorno real, produciendo feedback basado en resultados reales en lugar de razonamiento hipotético.
