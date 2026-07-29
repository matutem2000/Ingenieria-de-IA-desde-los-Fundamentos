# Módulo 7 – Capítulo 08 – Sección 04

# Human-in-the-loop: cuándo y cómo insertar confirmación humana en el ciclo agéntico

Human-in-the-loop (HITL) en sistemas agénticos es el mecanismo por el cual el agente pausa su ejecución y solicita confirmación, corrección o autorización de un humano antes de continuar, en lugar de actuar de forma completamente autónoma. Este mecanismo es esencial para las categorías de acciones donde el costo de un error es mayor que el overhead de la revisión humana: acciones irreversibles (borrar datos, enviar comunicaciones masivas, realizar transacciones financieras), acciones de alto impacto (modificar configuración en producción, otorgar permisos, publicar contenido), y situaciones de alta ambigüedad (el agente no tiene suficiente información para decidir con confianza). LangGraph implementa HITL nativamente mediante `interrupt_before` y `interrupt_after`: el grafo se pausa en un nodo específico, el estado actual se persiste en el checkpointer, y la ejecución se reanuda cuando el humano aprueba (opcionalmente modificando el estado) o rechaza la acción propuesta.

## Aspectos técnicos

- **Clasificación de acciones por reversibilidad**: categorizar cada herramienta del agente en: (1) read-only/reversible — ejecutar sin HITL, (2) reversible con costo — ejecutar con log, (3) parcialmente irreversible — confirmar antes de ejecutar, (4) completamente irreversible — confirmar + doble confirmación; esta taxonomía determina qué acciones requieren HITL
- **Interrupt patterns en LangGraph**: `interrupt_before=["action_node"]` pausa el grafo antes del nodo de acción; el estado persiste en el `SqliteSaver` o `PostgresSaver`; el humano revisa el estado, puede modificarlo y llama `graph.invoke(Command(resume=value), config)` para reanudar
- **Confidence threshold**: automatizar la decisión de cuándo invocar HITL basándose en un score de confianza del agente; si el agente expresa incertidumbre (tokens de baja probabilidad en la decisión, falta de evidencia suficiente en el contexto), escalar automáticamente antes de actuar
- **Timeout y expiración**: definir qué ocurre si el humano no responde en N minutos; opciones: abortar la acción y notificar, continuar con la acción más conservadora disponible, o escalar a otro humano; el timeout debe estar documentado en el diseño del sistema
- **UI de revisión de acciones**: la interfaz donde el humano revisa las acciones propuestas por el agente debe mostrar: la acción específica y sus parámetros, el razonamiento del agente que la justifica, el impacto estimado de la acción, y botones claros de aprobar/rechazar/modificar

## Principio rector

Human-in-the-loop no es una señal de que el agente falla; es una decisión de diseño que define el nivel de autonomía apropiado para el contexto: el nivel de autonomía de un agente debe ser proporcional a la madurez del sistema, la reversibilidad de sus acciones y la confianza establecida en su comportamiento.
