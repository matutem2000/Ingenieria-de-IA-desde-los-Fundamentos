# Módulo 5 – Capítulo 03 – Sección 02

# LangChain: arquitectura, cadenas, runnables y componentes principales

LangChain es el framework de orquestación de IA más adoptado en producción, con más de 90.000 estrellas en GitHub y una arquitectura modular organizada en paquetes: `langchain-core` (interfaces base y LCEL), `langchain` (cadenas y agentes de alto nivel), `langchain-community` (integraciones de terceros), y paquetes específicos de proveedor como `langchain-openai`, `langchain-anthropic`. La columna vertebral del framework en su versión moderna es LCEL (LangChain Expression Language): un protocolo que implementa la interface `Runnable` con métodos `invoke(input)`, `stream(input)`, `batch(inputs)` y sus variantes async, permitiendo componer cadenas con el operador pipe `|`. Los componentes fundamentales son: `ChatPromptTemplate` para formatear prompts con variables, `ChatOpenAI` o `ChatAnthropic` como wrappers de LLM, `StrOutputParser` o `PydanticOutputParser` para parsear la respuesta, y `RunnableParallel` o `RunnableBranch` para flujos paralelos o condicionales. LangGraph, la extensión de LangChain para flujos cíclicos y agentes con estado persistente, extiende el modelo de cadenas a grafos dirigidos con nodos, aristas condicionales y checkpointing.

## Componentes principales de LangChain

- `ChatPromptTemplate.from_messages()`: define la estructura del prompt con variables placeholder `{variable}` y slots para el historial conversacional, generando el array `messages` formateado listo para el LLM
- Wrappers de LLM (`ChatOpenAI`, `ChatAnthropic`): encapsulan el SDK del proveedor con la interface Runnable, aceptando parámetros como `model`, `temperature`, `max_tokens` y `streaming`, intercambiables sin cambiar el resto de la cadena
- `PydanticOutputParser` + `with_structured_output()`: fuerzan al modelo a devolver JSON compatible con un schema Pydantic, con reintentos automáticos cuando el parseo falla usando `OutputFixingParser`
- `RunnableParallel`: ejecuta múltiples runnables en paralelo con asyncio, combinando sus salidas en un dict; útil para llamar a múltiples fuentes de datos o modelos simultáneamente y reducir latencia total
- LangGraph: extiende LangChain con grafos de estado donde los nodos son funciones Python y las aristas pueden ser condicionales; el `MemorySaver` persiste el estado del grafo entre sesiones en memoria o en una base de datos

## Para recordar

LangChain tiene alta velocidad de cambio de API entre versiones principales; anclar la versión exacta en `requirements.txt` o `pyproject.toml` y revisar el changelog antes de actualizar previene regresiones inesperadas en producción.
