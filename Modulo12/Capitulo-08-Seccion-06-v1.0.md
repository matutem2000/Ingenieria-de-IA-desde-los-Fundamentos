# Módulo 12 – Capítulo 08 – Sección 06

# Cierre: operar sin observabilidad es conducir con los ojos cerrados

La observabilidad del sistema integrador es lo que hace posible operar con confianza en producción: las trazas distribuidas permiten diagnosticar en minutos la causa de un incidente de latencia; las métricas RAGAS en tiempo real detectan drifts de calidad antes de que el usuario los reporte; las alertas con runbooks reducen el tiempo de respuesta ante incidentes al eliminar la investigación inicial; y el monitoreo de drift de datos y modelo garantiza que el sistema siga siendo útil semanas y meses después del despliegue inicial. La instrumentación con OpenTelemetry, la stack Grafana (Tempo + Prometheus + Loki) y las alertas configuradas son inversiones que pagan su costo en el primer incidente de producción que se diagnostica en 10 minutos en lugar de 2 horas. La observabilidad no es una capa que se agrega al sistema — es parte del diseño desde el inicio, porque un sistema que no puede observarse no puede mantenerse, y un sistema que no puede mantenerse se degrada inevitablemente.

## Aspectos técnicos que integra este capítulo

- Stack OpenTelemetry: trazas en Grafana Tempo, métricas en Prometheus, logs estructurados en Grafana Loki
- Tracing distribuido: spans por etapa (auth, input validation, agente ReAct, herramientas, LLM) con correlación cross-service
- Dashboard operativo: overview KPIs, calidad RAG, comportamiento agéntico y métricas de seguridad en paneles correlacionados
- Alertas con runbooks: CRITICAL (error_rate, latencia, dependencias) y WARNING (faithfulness, costo) con procedimientos documentados
- Monitoreo de drift: análisis de distribución de reranking scores, evaluación semanal del golden dataset, clustering de queries

## Para recordar

La observabilidad de un sistema de IA en producción no termina en las métricas de infraestructura — requiere métricas de calidad continuas que detecten la degradación del comportamiento del modelo antes de que afecte a los usuarios.

*"You cannot improve what you cannot measure." — Peter Drucker*
