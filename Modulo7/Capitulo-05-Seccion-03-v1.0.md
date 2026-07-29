# Módulo 7 – Capítulo 05 – Sección 03

# CrewAI: orquestación de equipos de agentes con roles definidos

CrewAI es un framework de agentes de alto nivel que abstrae la complejidad de la coordinación multi-agente detrás de una metáfora organizacional: un `Crew` es un equipo de `Agents` con roles específicos (researcher, analyst, writer, reviewer) que colaboran en `Tasks` para lograr un objetivo común. La fortaleza de CrewAI es su API declarativa: en lugar de programar la lógica de coordinación explícitamente, el desarrollador define el rol de cada agente (como texto en lenguaje natural), las herramientas a las que tiene acceso, las tareas que componen el workflow y el proceso de ejecución (secuencial o jerárquico). CrewAI soporta dos modos de proceso: `Process.sequential` (las tareas se ejecutan en orden, con el output de cada tarea disponible como contexto para la siguiente) y `Process.hierarchical` (un agente manager orquesta la distribución de tareas a agentes especializados según sus capacidades). La integración nativa con LangChain tools permite reutilizar el ecosistema de herramientas existente.

## Componentes principales

- **Agent definition**: cada agente se define con `role` (su función en el equipo), `goal` (su objetivo específico), `backstory` (contexto que forma su "personalidad" y conocimiento de dominio) y `tools` (lista de herramientas disponibles)
- **Task definition**: cada tarea especifica `description` (qué debe producir), `expected_output` (formato y contenido esperado del resultado), `agent` (agente responsable) y opcionalmente `context` (resultados de otras tasks que deben considerarse)
- **Process.sequential vs hierarchical**: secuencial es más predecible y trazable; jerárquico permite al manager LLM decidir dinámicamente qué agente realiza qué tarea, añadiendo flexibilidad pero reduciendo determinismo
- **Memory en CrewAI**: soporta short-term memory (conversación actual), long-term memory (SQLite por defecto), entity memory (hechos sobre entidades mencionadas) y user memory (preferencias del usuario); configurables por crew con `memory=True`
- **Kickoff asíncrono**: `crew.kickoff_async()` permite ejecutar el crew sin bloquear el hilo principal; `kickoff_for_each_async()` procesa múltiples inputs en paralelo sobre el mismo crew, útil para procesar batches de datos

## Principio rector

CrewAI intercambia flexibilidad de bajo nivel por velocidad de desarrollo: su API declarativa permite construir un sistema multi-agente funcional en pocas líneas de código, a costa de menor control sobre la lógica de coordinación que LangGraph o AutoGen ofrecen.
