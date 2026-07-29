# Módulo 10 – Capítulo 01 – Sección 01

# Qué es una plataforma de IA: infraestructura compartida para equipos de AI Engineering

Una plataforma de IA es un conjunto de servicios internos reutilizables que abstraen la infraestructura de cómputo, almacenamiento y orquestación para que los equipos de AI Engineering puedan desarrollar, entrenar y desplegar modelos sin gestionar directamente clusters de GPU, buckets de S3, o configuraciones de Kubernetes. A diferencia de un entorno de desarrollo individual, la plataforma expone APIs y CLI unificados que permiten a múltiples equipos compartir capacidad de cómputo (por ejemplo, un cluster de A100s en AWS o on-premises), feature stores como Feast, y registros de modelos como MLflow o SageMaker Model Registry. El principio de diseño central es el mismo que el de una plataforma de software tradicional: reducir la carga cognitiva de los ingenieros que la consumen y estandarizar las prácticas de operación a escala. En la práctica, esto significa que un data scientist puede lanzar un experimento de fine-tuning con un solo comando `platform run --config experiment.yaml` sin conocer los detalles de Kubeflow Pipelines o de la configuración de NCCL para comunicación multi-GPU.

## Componentes fundamentales de una plataforma de IA

- Capa de cómputo gestionada: scheduling de jobs sobre Kubernetes con soporte para GPU fractionalization vía NVIDIA MIG o Time-Slicing
- Almacenamiento de artefactos: object storage (S3, GCS) con versionado y rutas estandarizadas por proyecto y experimento
- Plano de control de experimentos: tracking de hiperparámetros, métricas y artefactos (MLflow Tracking Server o Weights & Biases)
- Serving unificado: endpoints HTTP/gRPC generados automáticamente desde un modelo registrado (KServe, BentoML, o Ray Serve)
- Observabilidad integrada: métricas de sistema y negocio enviadas automáticamente a Prometheus con dashboards predefinidos en Grafana

## Idea central

Una plataforma de IA no es un conjunto de herramientas instaladas, sino un producto interno con contratos de API, SLOs propios y un equipo responsable de su evolución.
