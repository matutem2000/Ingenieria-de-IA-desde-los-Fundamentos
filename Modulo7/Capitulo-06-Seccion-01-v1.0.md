# Módulo 7 – Capítulo 06 – Sección 01

# Por qué multiagente: especialización, paralelismo y reducción del contexto por agente

Los sistemas multiagente no son una extensión caprichosa de los agentes individuales: responden a limitaciones concretas de los LLMs individuales en tareas complejas. La primera motivación es la especialización: un agente con un system prompt de 500 palabras enfocado en análisis de seguridad de código produce mejores resultados que un agente genérico con 2000 palabras que también analiza código, lo optimiza y escribe tests; la especialización reduce la ambigüedad del rol y mejora la precisión en el dominio específico. La segunda motivación es el paralelismo: tareas decomponibles en subtareas independientes pueden ejecutarse simultáneamente en múltiples agentes, reduciendo la latencia total de horas a minutos en workflows de procesamiento masivo. La tercera es la gestión del contexto: un agente que debe mantener el contexto completo de una tarea larga consume más ventana de contexto que la suma de múltiples agentes especializados trabajando en subtareas acotadas, donde cada agente solo necesita el contexto de su fragmento.

## Conceptos clave

- **Especialización de roles**: cada agente tiene un system prompt acotado a su dominio (researcher, coder, reviewer, planner); la reducción del scope del rol mejora la coherencia y la precisión de las respuestas dentro de ese dominio
- **Paralelismo de subtareas**: en LangGraph, nodos paralelos (`graph.add_node` con `asyncio`) permiten ejecutar múltiples agentes concurrentemente; en AutoGen, múltiples `ConversableAgent` pueden ejecutarse en paralelo con gestión de resultados mediante `asyncio.gather`
- **Reducción de contexto por agente**: un agente especializado solo necesita el contexto relevante para su tarea específica; en lugar de pasar 50K tokens de contexto global a un agente único, se pasan 2-5K tokens por agente especializado, reduciendo costo y mejorando la atención del modelo
- **División del espacio de herramientas**: en lugar de exponer todas las herramientas disponibles a un único agente (lo que aumenta la ambigüedad de selección), cada agente especializado recibe solo las herramientas relevantes para su rol
- **Overhead de coordinación**: la ganancia del multiagente debe superar el costo de coordinación; para tareas con menos de 3-4 pasos bien definidos y sin paralelismo natural, un agente único suele ser más eficiente que un sistema multiagente

## Principio rector

El multiagente es la solución correcta cuando la tarea supera la capacidad de un agente individual en términos de context window, especialización de dominio o paralelismo de subtareas; no es la solución correcta por defecto para cualquier tarea compleja.
