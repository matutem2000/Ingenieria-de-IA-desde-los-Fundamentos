# Módulo 7 – Capítulo 08 – Sección 04

## Human-in-the-loop: cuándo y cómo insertar confirmación humana en el ciclo agéntico

El human-in-the-loop (HITL) es el patrón de diseño más efectivo y más subutilizado en la seguridad agéntica. Mientras que la mayoría de las discusiones sobre seguridad de agentes se enfocan en mitigaciones técnicas —sandboxing, validación de inputs, restricción de herramientas—, la defensa más robusta para acciones de alto impacto no es técnica sino arquitectónica: diseñar el sistema para que ciertas categorías de acciones nunca se ejecuten automáticamente, sin importar cuán confiable parezca el razonamiento del agente. El HITL no es una señal de que el agente falla; es una decisión deliberada de diseño que define el nivel de autonomía apropiado para el contexto operativo.

La motivación del HITL como patrón de seguridad proviene directamente de los riesgos identificados en las secciones anteriores. Si un agente puede ser comprometido por prompt injection para ejecutar acciones irreversibles, la mitigación más efectiva no es mejorar la resistencia del LLM al prompt injection (que es inherentemente probabilística) sino asegurar que las acciones de mayor riesgo requieren aprobación humana independientemente del razonamiento del agente. Un humano en el loop puede detectar que "eliminar todos los registros de usuarios anteriores a 2020" es una acción inusual que no corresponde al objetivo de la tarea, incluso si el agente tiene un argumento plausible para justificarla.

La **clasificación de acciones por reversibilidad** es el punto de partida del diseño HITL. Cuatro categorías definen la política de confirmación:

1. **Read-only e idempotente**: lecturas de datos, búsquedas, consultas de APIs que no modifican estado. Ejecutar sin confirmación adicional, con logging completo.
2. **Reversible con costo**: escrituras que pueden deshacerse (crear un registro que puede eliminarse, añadir texto que puede editarse). Ejecutar con logging detallado y mecanismo de rollback documentado; considerar notificación post-ejecución al operador.
3. **Parcialmente irreversible**: acciones con efectos duraderos pero no catastróficos (enviar un email interno, publicar en un canal de Slack privado). Confirmar antes de ejecutar con preview de la acción específica.
4. **Completamente irreversible o de alto impacto**: borrar datos, enviar emails a clientes externos, ejecutar transacciones financieras, modificar configuración de producción. Confirmar con doble confirmación y documentación del razonamiento del agente.

**LangGraph** implementa HITL nativamente mediante `interrupt_before` e `interrupt_after`. Al compilar el grafo con `interrupt_before=["action_node"]`, la ejecución se pausa antes del nodo de acción especificado: el estado completo del grafo se persiste en el checkpointer (`SqliteSaver` o `PostgresSaver`), y el sistema queda en estado de espera. El operador humano recibe una notificación con el estado actual del agente y la acción propuesta, revisa el razonamiento que la justifica, y toma la decisión de aprobar (`graph.invoke(Command(resume={"approved": True}), config)`) o rechazar (`graph.invoke(Command(resume={"approved": False, "reason": "..."}), config)`). El grafo reanuda exactamente desde el punto de interrupción con la decisión del humano incorporada al estado.

El **confidence threshold** automatiza la decisión de cuándo invocar HITL basándose en el nivel de certeza del agente. Si el agente expresa incertidumbre explícita en su razonamiento —"No estoy seguro de si este es el registro correcto", "Encontré dos opciones posibles, no puedo determinar cuál es la correcta"— o si métricas proxy de confianza (baja probabilidad de los tokens en la decisión) indican incertidumbre, el sistema puede escalar automáticamente a revisión humana antes de la acción, sin esperar a que el agente lo solicite.

El **timeout y expiración de revisiones pendientes** es una consideración operativa crítica que frecuentemente se omite en el diseño inicial. ¿Qué ocurre si el humano no responde a la solicitud de confirmación en N minutos? Las opciones son: abortar la acción y notificar al usuario que la tarea no se completó, continuar con la acción más conservadora disponible (dry_run o skip), escalar a otro humano con más disponibilidad, o extender el timeout. La elección debe estar documentada en el diseño del sistema y codificada en la lógica del grafo.

## Aspectos técnicos

- **Clasificación de acciones por reversibilidad**: 4 categorías (read-only, reversible con costo, parcialmente irreversible, completamente irreversible); cada categoría tiene una política de confirmación diferente que se aplica sistemáticamente a todas las herramientas de esa categoría
- **Interrupt patterns en LangGraph**: `interrupt_before=["action_node"]` pausa el grafo antes del nodo de acción; el estado persiste en el checkpointer; el humano aprueba con `graph.invoke(Command(resume=value), config)` y la ejecución reanuda desde el punto de interrupción
- **Confidence threshold**: escalar a HITL automáticamente cuando el agente expresa incertidumbre en su razonamiento o cuando métricas proxy (probabilidad de tokens en la decisión clave) indican baja confianza
- **Timeout y expiración**: política explícita para el caso en que el humano no responde en N minutos; documentada en el diseño del sistema y codificada en la lógica del grafo; no dejar este caso como comportamiento indefinido
- **UI de revisión de acciones**: la interfaz para el operador humano debe mostrar: la acción específica con parámetros, el razonamiento del agente que la justifica, el impacto estimado, y botones claros de aprobar/rechazar/modificar

## Principio rector

Human-in-the-loop no es una señal de que el agente falla; es una decisión de diseño que define el nivel de autonomía apropiado para el contexto. El nivel de autonomía de un agente debe ser proporcional a la madurez del sistema, la reversibilidad de sus acciones, y la confianza establecida mediante el historial de comportamiento verificado en producción, no a la aspiración de autonomía completa.

La sección siguiente examina el sandboxing de herramientas: la defensa que protege al sistema host cuando todas las otras defensas han fallado y el agente ejecuta código potencialmente malicioso.
