# Módulo 10 – Capítulo 06 – Sección 01

# Definición de pipeline de MLOps: desde datos hasta predicción en producción

Un pipeline de MLOps es un flujo de trabajo automatizado y reproducible que encadena todas las etapas necesarias para transformar datos crudos en un modelo de ML desplegado en producción y monitoreado de forma continua, con la propiedad de que puede re-ejecutarse de principio a fin de forma determinista dado el mismo conjunto de inputs (datos, código, configuración). La estructura estándar de un pipeline de MLOps se articula en seis etapas: ingesta y validación de datos (data pipeline con validaciones de schema y calidad), ingeniería de features (transformaciones y materialización al feature store), entrenamiento del modelo (con tracking de hiperparámetros y métricas en MLflow o W&B), evaluación y validación offline (comparación contra el modelo champion en producción usando eval datasets con ground truth), publicación al registry (registro del modelo con todos sus metadatos de linaje si pasa los gates de calidad), y despliegue y monitoreo (actualización del endpoint de serving y activación del monitoreo de drift). A diferencia de un script de Python que ejecuta estas etapas secuencialmente, un pipeline de MLOps gestionado por un orquestador (Kubeflow, Airflow, Prefect) añade: gestión de fallos y retry automático por etapa, paralelización de etapas independientes, auditabilidad completa de cada ejecución con inputs/outputs registrados, y triggers automáticos basados en eventos (nuevo dataset disponible, degradación de calidad detectada por monitoreo).

## Componentes técnicos de un pipeline de MLOps

- Data validation step: Great Expectations o Deequ validan schema, completitud y distribución; el pipeline falla explícitamente si los datos no cumplen las expectativas definidas
- Feature engineering step: cálculo de features con Spark o pandas, materialización al feature store offline, y registro de las URIs de features en el MLflow run para trazabilidad
- Training step: job de entrenamiento distribuido (PyTorch DDP, DeepSpeed) con logging automático de métricas, checkpointing periódico en S3, y registro final en MLflow al completar
- Evaluation gate: comparación automática de métricas del nuevo modelo vs el modelo champion en producción; el pipeline solo avanza si el nuevo modelo supera el umbral definido (ej. accuracy_new > accuracy_champion * 0.99)
- Deployment step: actualización del InferenceService en Kubernetes vía kubectl o ArgoCD, con canary routing inicial (10% del tráfico) y rollback automático si las métricas de producción se degradan

## Para recordar

La diferencia entre un pipeline de MLOps y un script es la resistencia a fallos y la trazabilidad: un pipeline bien construido puede fallar en cualquier etapa, ser reparado y re-ejecutarse desde el punto de fallo sin perder el trabajo previo.
