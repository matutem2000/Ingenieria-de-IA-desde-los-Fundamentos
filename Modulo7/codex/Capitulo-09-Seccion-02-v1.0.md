# Módulo 7 – Capítulo 09 – Sección 02

# Gestión del estado entre sesiones: persistencia y recuperación de contexto

Un agente en producción puede ser interrumpido en cualquier punto de su ejecución: el proceso puede crashear, la instancia puede ser reemplazada en un rolling deployment, el usuario puede cerrar la sesión antes de que la tarea termine, o la tarea puede pausarse explícitamente para revisión humana. En todos estos casos, el estado del agente —el progreso acumulado, las observaciones recopiladas, las decisiones tomadas, los pasos completados— debe poder persistirse en almacenamiento durable y recuperarse para reanudar la ejecución desde el punto de interrupción sin perder trabajo ya realizado. LangGraph Cloud implementa esto mediante `checkpointers` que serializan el `StateGraph` completo (incluyendo el estado del grafo, el historial de mensajes y las variables del AgentState) a PostgreSQL después de cada nodo, permitiendo reanudar exactamente desde el último nodo completado con `graph.invoke(None, config={"configurable": {"thread_id": "..."}})`. Para agentes asíncronos, el checkpointing es especialmente crítico: una tarea de 30 minutos que falla en el minuto 28 no debe reiniciarse desde cero.

## Aspectos técnicos

- **Checkpointing por nodo**: serializar el estado del agente después de completar cada nodo del grafo de estado; el granulo de checkpointing determina cuánto trabajo puede perderse en un fallo: checkpointing por nodo = pérdida máxima de 1 nodo de trabajo
- **Serialización del estado**: el `AgentState` debe ser completamente serializable a JSON o a tipos nativos de la base de datos; objetos Python no serializables (conexiones de DB, file handles, objetos de configuración) deben reconstruirse al reanudar, no serializarse
- **Thread_id como identificador de sesión**: cada sesión del agente tiene un `thread_id` único que actúa como clave primaria en el checkpointer; permite múltiples sesiones concurrentes del mismo agente sin interferencia entre ellas
- **Reanudación parcial**: al reanudar una sesión interrumpida, el agente debe identificar el último estado guardado, reconstruir el contexto necesario (reconectarse a APIs, recargar configuración) y continuar desde el nodo siguiente al último completado, sin re-ejecutar trabajo ya hecho
- **Retención y limpieza de checkpoints**: los checkpoints de sesiones completadas o expiradas deben purgarse periódicamente para evitar crecimiento indefinido del almacenamiento; implementar TTL (p.ej. 7 días para sesiones completadas, 30 días para sesiones pausadas pendientes de revisión humana)

## Para recordar

El checkpointing no es un lujo de sistemas de alta disponibilidad; es un requisito de correctitud para cualquier agente que ejecuta tareas largas: sin checkpointing, un fallo en el paso 95 de 100 reinicia la tarea completa, desperdiciando recursos y degradando la experiencia del usuario.
