# Módulo 10 – Capítulo 03 – Sección 05

# Linaje de modelos: trazabilidad desde los datos de entrenamiento hasta el despliegue

El linaje de modelos (model lineage) es la capacidad de reconstruir la historia completa de cómo se llegó a un modelo en producción: desde qué datos se usaron para entrenarlo (con sus versiones exactas), qué código y configuración se ejecutó, qué hiperparámetros se usaron, qué métricas de evaluación se obtuvieron, quién lo aprobó para producción, y cuándo y cómo fue desplegado. Esta trazabilidad completa es imprescindible para tres escenarios críticos: auditorías de compliance (saber exactamente qué datos de clientes fueron usados en un modelo y si cumplían las políticas de uso), investigación de incidentes (reproducir el comportamiento del modelo en el momento de un fallo comparando con el modelo actual), y reproducibilidad de experimentos (replicar exactamente un resultado de un año atrás para compararlo con un nuevo enfoque). La implementación técnica del linaje conecta cuatro sistemas: el sistema de versionado de datos (DVC o LakeFS), el experiment tracker (MLflow), el model registry, y el sistema de despliegue (Kubernetes con ArgoCD), con punteros explícitos entre ellos almacenados en el registry como metadatos. Herramientas como OpenLineage y Marquez implementan el estándar de linaje abierto que permite que esta trazabilidad sea agnóstica al sistema de orquestación utilizado.

## Aspectos técnicos del linaje de modelos

- Dataset lineage: cada entrenamiento registra el URI de los datos con versión explícita (ej. `s3://data-lake/features/user_events/v2.3.1@sha256:abc123`), no solo la ruta del directorio
- Code lineage: referencia al commit SHA del repositorio de entrenamiento, la imagen Docker con su digest, y el hash del archivo de configuración de hiperparámetros
- Experiment lineage: el run_id de MLflow, el experiment_id, y los links a los artefactos intermedios (checkpoints, plots de training curves, eval reports)
- Deployment lineage: registro en el model registry de cuándo, quién y con qué configuración de Kubernetes fue desplegado el modelo, incluyendo el ArgoCD Application y el Helm chart version
- Downstream impact tracking: registro de qué servicios consumen cada versión de cada modelo, permitiendo evaluar el impacto antes de una actualización y notificar a los equipos afectados

## Buena práctica

El linaje de modelos debe ser automático, no manual: si un ingeniero necesita recordar completar los campos de linaje en el registry, inevitablemente se omitirán en los momentos de mayor presión operativa.
