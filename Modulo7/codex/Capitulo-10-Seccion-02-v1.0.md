# Módulo 7 – Capítulo 10 – Sección 02

# Métricas de razonamiento: coherencia del plan y calidad de las decisiones intermedias

Las métricas de razonamiento evalúan la calidad del proceso de pensamiento del agente, no solo sus resultados finales: ¿el plan inicial es coherente con el objetivo? ¿las decisiones de qué herramienta usar en cada paso son razonables dado el contexto? ¿el agente incorpora correctamente las observaciones de herramientas para actualizar su razonamiento? Estas métricas son más difíciles de automatizar que las métricas de tarea porque requieren evaluar texto de razonamiento en lenguaje natural, lo que típicamente involucra un LLM-judge. La coherencia del plan mide si la secuencia de acciones planificadas es lógicamente consistente y conducente al objetivo declarado; una puntuación baja indica que el agente está actuando sin un plan claro o que su plan no se alinea con el objetivo del usuario. La calidad de las decisiones intermedias evalúa si, dado el estado actual del conocimiento (contexto acumulado + observaciones), la siguiente acción elegida es la más adecuada entre las alternativas disponibles.

## Aspectos técnicos

- **Plan coherence score**: LLM-judge evalúa si el plan inicial del agente (cuando usa planificación explícita) es internamente consistente, completo para lograr el objetivo y libre de acciones contradictorias; score 0-1 con justificación textual para diagnóstico
- **Grounding score**: mide si el razonamiento del agente está basado en evidencia del contexto (observaciones de herramientas, datos del usuario) o en alucinaciones; un agente que toma decisiones contradictorias a las evidencias disponibles en el contexto tiene un grounding score bajo
- **Decision quality**: dado el estado del agente en el paso N, ¿cuán óptima es la acción elegida comparada con las alternativas? Evaluado por LLM-judge que recibe el estado completo y las opciones disponibles; identifica patrones sistemáticos de decisiones subóptimas
- **Observation utilization**: mide si el agente incorpora activamente las observaciones de herramientas en su razonamiento posterior; un agente que ignora sistemáticamente los resultados de búsquedas o ejecuta la misma herramienta con los mismos parámetros múltiples veces tiene baja observation utilization
- **Reasoning faithfulness**: para agentes que exponen razonamiento scratchpad, verificar si el razonamiento visible predice correctamente la acción que sigue; razonamiento que lleva a una herramienta A pero el agente invoca la herramienta B indica unfaithful reasoning

## Para recordar

Las métricas de razonamiento son el diagnóstico clínico del agente: mientras las métricas de tarea dicen si el paciente está sano, las métricas de razonamiento dicen por qué está enfermo y dónde está el problema específico que hay que tratar.
