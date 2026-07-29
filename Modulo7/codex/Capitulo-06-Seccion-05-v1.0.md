# Módulo 7 – Capítulo 06 – Sección 05

# Consistencia y reconciliación: qué sucede cuando dos agentes producen resultados contradictorios

La inconsistencia entre agentes es un problema emergente en sistemas multiagente que no existe en agentes individuales: cuando dos agentes especializados producen resultados contradictorios sobre el mismo aspecto de una tarea —un agente clasifica un código como seguro mientras otro lo clasifica como vulnerable, o un agente propone aumentar el precio mientras otro propone reducirlo— el sistema necesita un mecanismo explícito de reconciliación para resolver la contradicción y producir una decisión coherente. La ausencia de este mecanismo lleva a uno de tres resultados problemáticos: el orquestador elige arbitrariamente uno de los dos resultados (sin racionalidad explícita), el sistema propaga la contradicción al output final (lo que confunde al usuario), o el sistema queda bloqueado esperando una resolución que no llegará. Los mecanismos de reconciliación incluyen voting (mayoría entre k agentes), aggregation (promedio de scores numéricos), debate (los agentes explican sus razonamientos y un judge decide), y escalado a humano (cuando la contradicción supera un threshold de divergencia).

## Puntos críticos

- **Detección de contradicciones**: el orquestador debe verificar activamente si los outputs de los agentes son consistentes entre sí antes de sintetizarlos; métricas de divergencia: coseno entre embeddings de respuestas (<0.7 indica contradicción potencial), NLI (Natural Language Inference) para detectar contradicción semántica, o verificación programática para outputs estructurados
- **Voting y majority**: para K agentes que producen outputs categóricos, la respuesta mayoritaria gana; efectivo para K≥3 impar; requiere que todos los agentes evalúen el mismo aspecto de la tarea y que su output sea comparable
- **Aggregation de scores**: para outputs numéricos (scores de confianza, estimaciones de tiempo, ratings), promediar o usar mediana; el orquestador debe saber qué agentes tienen mayor autoridad sobre qué aspectos para ponderar sus outputs apropiadamente
- **Debate estructurado**: presentar a cada agente el output del otro con una instrucción de revisión ("El agente B argumenta X; ¿cambia esto tu evaluación?"); iterar 1-2 rondas y usar un LLM judge para determinar qué posición es más fundamentada
- **Escalado a humano por threshold**: cuando la divergencia supera un umbral predefinido (p.ej. dos agentes con outputs diametralmente opuestos con alta confianza ambos), el sistema debe pausar y solicitar decisión humana en lugar de resolver artificialmente la contradicción

## Para recordar

La reconciliación de resultados contradictorios no es un caso límite sino un requisito de diseño en cualquier sistema multiagente donde múltiples agentes evalúan el mismo aspecto de un problema: el mecanismo de reconciliación debe ser diseñado antes de que aparezcan las primeras contradicciones en producción.
