# Módulo 7 – Capítulo 01 – Sección 01

# Qué es un agente: percepción, razonamiento, memoria, herramientas y acción

Un agente de IA es un sistema que percibe su entorno a través de entradas estructuradas (texto, JSON, resultados de API, contenido de archivos), razona sobre esa percepción usando un modelo de lenguaje como motor de inferencia, y ejecuta acciones con efectos en el mundo real: llamadas HTTP, ejecución de código, escritura en bases de datos o interacción con sistemas externos. A diferencia de una función determinista, un agente opera en bucles iterativos donde cada acción puede modificar el estado del entorno y generar nueva percepción. La arquitectura clásica de un agente —inspirada en los sistemas de agentes inteligentes de Russell y Norvig— descompone el comportamiento en cinco componentes funcionales: percepción, razonamiento, memoria, herramientas y acción.

## Componentes principales

- **Percepción**: entrada al agente en cada paso del ciclo; puede ser texto del usuario, resultados de herramientas, contenido de archivos o respuestas HTTP serializadas en el contexto
- **Razonamiento**: el LLM (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro) actúa como motor de inferencia que decide qué hacer a continuación dado el contexto acumulado
- **Memoria**: estado que persiste entre pasos del ciclo; se divide en memoria in-context (historial en la ventana de contexto) y memoria externa (vectorstores como Pinecone, bases de datos como PostgreSQL)
- **Herramientas**: funciones con esquema JSON que el LLM puede invocar; desde búsqueda web (Tavily, SerpAPI) hasta ejecución de código (Python REPL, E2B sandbox) o llamadas a APIs REST
- **Acción**: la operación concreta que el agente ejecuta tras decidir; puede ser una llamada de herramienta, un mensaje al usuario, una escritura en base de datos o la finalización de la tarea

## Principio rector

Un agente no es una secuencia fija de pasos sino un sistema que decide dinámicamente qué operación ejecutar a continuación, condicionado por el estado actual del entorno y su historial de percepción acumulado.
