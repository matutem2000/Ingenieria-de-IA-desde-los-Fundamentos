# Módulo 7 – Capítulo 06 – Sección 03

# Comunicación entre agentes: mensajes, handoffs y contratos de interfaz

La comunicación entre agentes en un sistema multiagente no puede ser informal: cada mensaje que pasa de un agente a otro es una transferencia de contexto que debe ser estructurada, completa y sin ambigüedad para que el agente receptor pueda actuar sobre ella sin conocimiento implícito del estado del sistema. Los mecanismos de comunicación principales son mensajes estructurados (objetos JSON o modelos Pydantic que encapsulan el output del agente junto con metadata relevante: agente origen, timestamp, confianza, estado de la tarea), handoffs (transferencia explícita de control de un agente a otro, con todo el contexto necesario para que el receptor continúe desde el punto exacto donde el emisor se detuvo) y contratos de interfaz (schemas formales que definen el formato exacto de input y output de cada agente, equivalentes a las interfaces en programación orientada a objetos). La ausencia de contratos formales entre agentes es una fuente común de bugs difíciles de detectar: el agente emisor produce output en formato A mientras el receptor espera formato B, y el error solo se manifiesta silenciosamente en la calidad degradada de la tarea final.

## Aspectos técnicos

- **Mensajes estructurados**: el output de cada agente debe incluir el resultado principal + metadata de ejecución (`agent_id`, `task_id`, `confidence_score`, `error_if_any`, `tokens_used`); la metadata permite al orquestador tomar decisiones informadas sobre cómo proceder
- **Handoff pattern (Anthropic)**: el mecanismo de handoff explícito de Anthropic transfiere control entre agentes pasando el historial de conversación completo al agente receptor; implementado en Claude mediante herramientas que retornan control a otro agente con contexto actualizado
- **Contratos de interfaz (Pydantic schemas)**: definir los modelos de input y output de cada agente como clases Pydantic; al llamar a un agente, validar el input contra su schema antes de enviarlo; al recibir el output, validar contra el schema de salida antes de procesarlo
- **Message passing vs shared state**: dos paradigmas de comunicación con trade-offs distintos; message passing (mensajes explícitos entre agentes) es más desacoplado y escalable; shared state (pizarra compartida tipo LangGraph StateGraph) es más conveniente para agentes que colaboran estrechamente sobre el mismo problema
- **Serialización y deserialización**: todos los mensajes entre agentes que cruzan boundaries de proceso (distintos workers, distintos servicios) deben ser serializables; preferir JSON sobre pickle para garantizar compatibilidad entre versiones y lenguajes de programación

## Principio rector

Los contratos de interfaz entre agentes son tan importantes como los contratos de API entre microservicios: la informalidad en la comunicación inter-agente produce bugs que son difíciles de atribuir a un agente específico porque el error es una propiedad emergente de la interacción, no de ningún agente individual.
