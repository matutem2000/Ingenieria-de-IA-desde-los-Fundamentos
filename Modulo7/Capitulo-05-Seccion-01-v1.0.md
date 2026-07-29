# Módulo 7 – Capítulo 05 – Sección 01

# LangGraph: grafos de estado para flujos agénticos deterministas y cíclicos

LangGraph es el framework de agentes de LangChain que modela el comportamiento agéntico como un grafo de estado explícito: cada nodo es una función Python que procesa y modifica el `AgentState`, y cada arista (condicional o directa) define las transiciones entre estados. A diferencia del AgentExecutor de LangChain clásico —que usa un bucle while implícito difícil de inspeccionar y modificar—, LangGraph expone el grafo completo del agente como un objeto visual e inspeccionable que puede ser compilado, trazado y ejecutado con control preciso sobre cada transición de estado. La estructura de grafo permite implementar nativamente patrones que son difíciles en frameworks lineales: ciclos de corrección (el agente puede volver a un nodo anterior tras un fallo), flujos paralelos (múltiples nodos ejecutándose concurrentemente con `asyncio`), y subgrafos (grafos anidados para sub-agentes especializados). LangGraph Cloud añade persistencia de estado entre sesiones, checkpointing automático y streaming de pasos individuales.

## Componentes principales

- **StateGraph y AgentState**: el grafo se define tipando el estado (`TypedDict` con los campos que persisten entre nodos) y registrando nodos con `graph.add_node(name, function)`; el estado es el único mecanismo de comunicación entre nodos
- **Aristas condicionales**: `graph.add_conditional_edges(node, condition_fn, {outcome: next_node})` permiten routing dinámico basado en el estado; la `condition_fn` inspecciona el estado actual y devuelve la clave del próximo nodo
- **Checkpointing**: `MemorySaver` y `SqliteSaver` permiten persistir el estado del grafo entre llamadas; habilitado con `graph.compile(checkpointer=checkpointer)` y usando un `thread_id` para identificar cada sesión
- **Streaming de pasos**: `graph.stream(input, config)` devuelve un generador que emite el estado después de cada nodo; permite visualizar el progreso del agente en tiempo real en el UI o logearlo en sistemas de observabilidad
- **Human-in-the-loop nativo**: LangGraph soporta `interrupt_before` y `interrupt_after` para pausar la ejecución del grafo antes o después de nodos críticos, esperar confirmación humana y reanudar con el estado actualizado

## Principio rector

LangGraph convierte el flujo de control del agente de un comportamiento emergente implícito a un grafo explícito e inspeccionable: cada decisión de routing es una función Python auditable, y cada estado intermedio puede ser persistido, reproducido y analizado.
