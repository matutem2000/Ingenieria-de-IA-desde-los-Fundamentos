# Módulo 12 – Capítulo 08 – Sección 01

# Stack de observabilidad del proyecto: trazas, métricas, logs y alertas

El stack de observabilidad del sistema integrador implementa los tres pilares de la observabilidad moderna (trazas, métricas y logs) más una capa de alertas, siguiendo el estándar OpenTelemetry para instrumentación vendor-neutral. Las trazas distribuidas se capturan con el SDK de OpenTelemetry para Python, exportadas a Grafana Tempo a través del OTEL Collector; cada petición genera un trace que contiene spans para cada etapa del pipeline: validación de input, embedding, búsqueda en Qdrant, reranking, cada paso del agente ReAct y generación del LLM. Las métricas se exponen vía Prometheus scraping del endpoint `/metrics` de FastAPI con el middleware `prometheus_fastapi_instrumentator`, exportadas a Grafana para visualización. Los logs estructurados se emiten en formato JSON con nivel, timestamp, trace_id, span_id y campos específicos del dominio (tool_name, chunk_count, tokens_used), exportados a Grafana Loki para correlación con trazas y métricas.

## Componentes del stack de observabilidad

- OpenTelemetry SDK: instrumentación de FastAPI, httpx, SQLAlchemy y cliente Qdrant con propagación automática de trace context
- Grafana Tempo: almacenamiento y visualización de trazas distribuidas con correlación a métricas y logs
- Prometheus + Grafana: métricas de sistema (latencia, throughput, error rate) y de negocio (faithfulness, tool_usage_rate)
- Grafana Loki: logs estructurados JSON con query language LogQL para correlación con trazas y alertas
- OTEL Collector: pipeline de procesamiento, filtrado y exportación de señales a los backends correspondientes

## Para recordar

Un stack de observabilidad solo es útil si los tres pilares están correlacionados — la capacidad de ir de una alerta de latencia alta a la traza específica que causó el problema, y de ahí a los logs de esa ejecución, es lo que permite diagnosticar incidentes en minutos en lugar de horas.
