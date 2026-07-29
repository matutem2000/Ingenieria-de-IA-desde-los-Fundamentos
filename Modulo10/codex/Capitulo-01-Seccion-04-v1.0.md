# Módulo 10 – Capítulo 01 – Sección 04

# Platform engineering vs MLOps: convergencia y diferencias de foco

Platform engineering es la disciplina que construye y opera la infraestructura compartida para que los equipos de producto puedan desplegar software sin fricción, siendo el Internal Developer Platform (IDP) el artefacto central documentado por la CNCF Platforms Working Group. MLOps, definido por Google en su paper seminal de 2017, es el conjunto de prácticas para automatizar el ciclo de vida de modelos de ML desde la experimentación hasta la operación continua. La convergencia entre ambas disciplinas es inevitable: un IDP moderno debe incluir primitivas de ML (GPU scheduling, experiment tracking, serving endpoints) para ser útil para equipos de AI Engineering, mientras que los equipos de MLOps están adoptando prácticas de platform engineering como Platform as a Product, developer portals (Backstage) y golden paths para estandarizar cómo se despliegan modelos. La diferencia de foco principal es que platform engineering prioriza la experiencia del desarrollador y la reducción de cognitive load, mientras que MLOps prioriza la reproducibilidad, el monitoreo de calidad de modelos y el reentrenamiento automatizado.

## Aspectos técnicos diferenciadores

- Platform engineering: Internal Developer Platform con Service Catalog (Backstage), Infrastructure as Code (Terraform, Pulumi), y self-service vía portales web
- MLOps: experiment tracking con hiperparámetros y métricas, model registry con estados de ciclo de vida, y continuous training pipelines con triggers automáticos
- Punto de convergencia en CI/CD: platform engineering aporta los runners y pipelines (GitHub Actions, Tekton), MLOps aporta las validaciones específicas de modelos (eval gates, canary analysis de métricas de negocio)
- Gestión de compute: platform engineering abstrae Kubernetes namespaces y resource quotas, MLOps abstrae GPU scheduling y distributed training con frameworks como PyTorch DDP o DeepSpeed
- Observabilidad: platform engineering entrega la stack de Prometheus/Grafana/Jaeger, MLOps la extiende con métricas de modelo como data drift, prediction confidence y business KPIs

## Buena práctica

Un equipo de AI Platform Engineering exitoso habla ambos idiomas: entiende los primitivos de Kubernetes y Terraform, y también las necesidades específicas de los ML Engineers como reproducibilidad de experimentos y rollback de modelos en producción.
