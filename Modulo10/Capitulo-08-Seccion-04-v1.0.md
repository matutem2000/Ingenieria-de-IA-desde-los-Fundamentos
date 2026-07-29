# Módulo 10 – Capítulo 08 – Sección 04

# Auditoría de uso: quién usó qué modelo con qué datos y cuándo

La auditoría de uso en una plataforma de IA es la capacidad de responder retroactivamente a cualquier pregunta sobre cómo se usaron los modelos y los datos: ¿qué modelos procesaron datos de usuarios europeos en los últimos 30 días? (GDPR), ¿quién ejecutó el training job que generó el modelo actualmente en producción? (incident investigation), ¿cuántos tokens de datos confidenciales procesó el equipo de fraude el mes pasado? (FinOps y compliance). Este tipo de auditoría requiere instrumentación en tres capas: el audit log del LLM Gateway (quién llamó a qué modelo con qué prompt), el audit log del model registry (quién registró, aprobó y desplegó cada versión de cada modelo), y el audit log del sistema de datos (qué datasets fueron accedidos y descargados por qué identidad y cuándo). La implementación técnica más robusta centraliza todos estos eventos en un sistema de audit log inmutable (CloudTrail en AWS, Cloud Audit Logs en GCP, o un sistema propio sobre S3 con Object Lock) con un schema estandarizado (quién, qué, cuándo, desde dónde, sobre qué recurso, con qué resultado) que permite queries across systems. Las queries de auditoría más comunes se precomputan como reportes programados (uso mensual por equipo, accesos a datos sensibles en tiempo real, modelos desplegados por semana) disponibles en un dashboard de governance, en lugar de requerir acceso directo al sistema de logs para cada consulta.

## Aspectos técnicos de la auditoría de uso

- Event schema estándar: CloudEvents o un schema propio con campos: `event_type`, `actor` (human/service), `actor_id`, `resource_type`, `resource_id`, `action`, `timestamp`, `ip_address`, `result` (success/failure), `metadata`
- Audit log del serving layer: cada inferencia registra model_id, version, input_token_count, output_token_count, latency, caller_identity, project_id; los prompts solo si la política de retención de la organización lo permite
- Cross-system correlation: `request_id` como correlación universal que conecta el log del LLM Gateway con el log del modelo en el registry con el log del feature store con el log de la aplicación cliente
- Real-time alerts de auditoría: alertas inmediatas cuando un usuario accede a datos de clasificación "restricted" fuera de su horario habitual, cuando se descarga un dataset de producción desde una IP no corporativa, o cuando un modelo se despliega sin aprobación
- Retention y querability: logs de auditoría retenidos mínimo 7 años para compliance financiero, 5 años para GDPR; indexados en Elasticsearch o BigQuery para queries interactivos en segundos sobre años de eventos

## Para recordar

Un audit trail incompleto es tan inútil como ningún audit trail: la efectividad de la auditoría depende de que el 100% de las operaciones relevantes sean registradas de forma confiable, no del 95%.
