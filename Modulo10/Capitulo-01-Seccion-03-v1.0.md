# Módulo 10 – Capítulo 01 – Sección 03

# Componentes de una plataforma de IA: modelo serving, pipelines, registry y observabilidad

Una plataforma de IA empresarial se articula en cuatro capas funcionales que trabajan de forma integrada: la capa de serving gestiona el ciclo de vida de endpoints de inferencia (KServe, Ray Serve, Triton Inference Server), la capa de pipelines orquesta los flujos de entrenamiento y procesamiento de datos (Kubeflow Pipelines, Prefect, Airflow), el model registry centraliza artefactos y metadatos con gestión de estados (Staging, Production, Archived) como lo hace MLflow o SageMaker Model Registry, y la capa de observabilidad recopila métricas de sistema y calidad de modelo vía Prometheus, Grafana y herramientas especializadas como Evidently AI o WhyLabs. Estos cuatro componentes se interconectan mediante contratos de API internos: el pipeline publica artefactos al registry, el registry dispara el serving, y el serving emite métricas a la capa de observabilidad. La capa de identidad y control de acceso (RBAC via Kubernetes ServiceAccounts o un IdP como Okta) actúa horizontalmente sobre todos los componentes para garantizar aislamiento entre equipos y trazabilidad de operaciones.

## Componentes principales

- Model serving layer: endpoint HTTP/gRPC con autoscaling basado en custom metrics (ej. pending requests via KEDA) y soporte para batch inference
- Pipeline orchestration: DAGs declarativos con retry logic, alertas por SLA y gestión de dependencias entre tareas de preprocesamiento, entrenamiento y evaluación
- Model registry: almacén de artefactos (pesos, tokenizers, configuraciones) con estado de ciclo de vida, comentarios de revisión y webhook de notificación al cambiar de estado
- Observabilidad de modelos: tracking de métricas de calidad (accuracy, F1, BLEU, ROUGE) junto a métricas de sistema (latencia p50/p95/p99, error rate, GPU utilization)
- Feature store: repositorio online (Redis, DynamoDB) y offline (Parquet en S3) de features compartidas con point-in-time correctness para evitar data leakage

## Para recordar

Cada componente de la plataforma debe tener un SLO definido: el registry un uptime de 99.9%, el serving un p99 de latencia bajo contrato, y los pipelines una tasa de éxito mínima medida semanalmente.
