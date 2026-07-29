# Módulo 10 – Capítulo 02 – Sección 01

# Arquitectura de referencia para una plataforma de IA empresarial

Una arquitectura de referencia para una plataforma de IA empresarial define las capas, contratos de interfaz y patrones de integración que todos los equipos deben seguir, eliminando decisiones de infraestructura ad-hoc y permitiendo que las decisiones de diseño se tomen una sola vez y se beneficien todos. La arquitectura más adoptada en la industria, documentada por empresas como Lyft, Netflix y Meta, organiza la plataforma en cuatro planos: el plano de datos (ingesta con Kafka o Pub/Sub, almacenamiento en Delta Lake o Iceberg sobre S3, feature store con Feast o Tecton), el plano de experimentación (cluster de entrenamiento en Kubernetes con GPU, tracking con MLflow, hyperparameter optimization con Optuna o Ray Tune), el plano de serving (KServe o Triton detrás de un API Gateway como Kong, con canary y blue-green routing), y el plano de control (model registry, pipeline orchestration con Kubeflow o Prefect, y observabilidad con Prometheus/Grafana/Evidently). Cada plano expone contratos de API versionados y documentados en un portal interno (Backstage), y los equipos de AI Engineering interactúan con la plataforma principalmente a través de un CLI interno o un SDK Python que abstrae la complejidad subyacente.

## Componentes principales de la arquitectura de referencia

- Data plane: ingesta streaming (Kafka) y batch (Spark en EMR o Dataproc), almacenamiento en object store con formato columnar versionado (Delta Lake), feature store con consistencia online/offline
- Training plane: Kubernetes con GPU pools segmentados por prioridad (interactivo vs batch), job scheduling con Volcano o Kueue, distributed training con PyTorch DDP y checkpointing en S3
- Serving plane: model server (Triton/KServe) con autoscaling vía KEDA, API Gateway con rate limiting y autenticación JWT, load balancer con routing por canary weight o header-based routing
- Control plane: model registry con webhooks de promoción, pipeline orchestrator con DAGs declarativos, configuration management vía GitOps (ArgoCD), y secret management (HashiCorp Vault)
- Observability plane: métricas de sistema en Prometheus, métricas de modelo en Evidently con drift detection, logs estructurados en Elasticsearch, traces distribuidos en Jaeger u OpenTelemetry

## Principio rector

Una arquitectura de referencia no es un diagrama: es un conjunto de decisiones implementadas, testeadas y documentadas que los equipos pueden adoptar sin tener que redescubrir los mismos problemas de infraestructura.
