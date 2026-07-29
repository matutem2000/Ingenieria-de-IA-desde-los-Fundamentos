# Módulo 12 – Capítulo 07 – Sección 01

# Framework de evaluación end-to-end: métricas del RAG, del agente y del sistema completo

El framework de evaluación del proyecto final integra métricas en tres niveles: evaluación del pipeline RAG (calidad de recuperación y generación), evaluación del agente (completitud de tareas y eficiencia de razonamiento) y evaluación del sistema completo (latencia end-to-end, costo y disponibilidad). En el nivel RAG, las métricas RAGAS (faithfulness, answer relevance, context precision, context recall) se calculan automáticamente sobre el golden dataset en cada deploy y de forma continua sobre muestras aleatorias en producción. En el nivel agéntico, las métricas son: task completion rate, iterations per task (media y distribución), tool usage accuracy (herramienta correcta para cada subtarea) y hallucination rate evaluada por LLM-as-judge. En el nivel de sistema, se miden: latencia P50/P95/P99 con OpenTelemetry, throughput en peticiones por segundo, costo por petición en USD y error rate por tipo de error. Las tres capas de métricas se visualizan en un dashboard Grafana unificado con correlación entre degradación de calidad RAG y aumento de hallucination rate agéntica.

## Métricas por capa del framework de evaluación

- Capa RAG: RAGAS faithfulness, answer_relevance, context_precision, context_recall (continuo en producción, cada deploy)
- Capa agéntica: task_completion_rate, iterations_per_task, tool_call_accuracy, hallucination_rate por LLM-as-judge
- Capa de sistema: latencia P50/P95/P99 (OpenTelemetry), throughput req/s, costo/req USD, error_rate por tipo
- Correlación cross-layer: alertas que correlacionan caída de context_precision con aumento de hallucination_rate
- Evaluación offline vs online: golden dataset para evaluación offline, muestreo 5% del tráfico real para evaluación online

## Para recordar

Un framework de evaluación end-to-end mide el sistema completo, no solo las partes — una mejora en context precision que aumenta la latencia P95 por encima del SLA no es una mejora aceptable para producción.
