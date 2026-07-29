# Módulo 10 – Capítulo 03 – Sección 02

# MLflow: experiments, runs, modelos y serving integrado

MLflow es la plataforma de MLOps open source más adoptada en la industria, diseñada originalmente por Databricks y actualmente gestionada por la Linux Foundation, que unifica en un solo sistema el tracking de experimentos, el empaquetado de modelos, el model registry y el serving. El componente de Tracking Server registra cada ejecución de entrenamiento (run) con sus parámetros de entrada, métricas iteración por iteración (loss, accuracy, BLEU), artefactos generados (pesos, plots, confusion matrix) y el código fuente vía git commit SHA; cada run pertenece a un experiment y puede ser comparado visualmente en la UI o programáticamente vía la API REST. El componente de Model Registry añade el ciclo de vida sobre los modelos: desde un run exitoso se puede registrar el modelo (`mlflow.register_model(run_id, "my-model")`) creando automáticamente la versión 1, y luego gestionar su transición entre estados mediante `client.transition_model_version_stage("my-model", 1, "Production")`. El serving integrado permite desplegar cualquier modelo registrado como endpoint REST con `mlflow models serve -m "models:/my-model/Production" -p 5000`, soportando los flavors más comunes: sklearn, pytorch, tensorflow, transformers (HuggingFace) y pyfunc para modelos custom.

## Aspectos técnicos de MLflow

- MLflow Tracking: API Python (`mlflow.log_param`, `mlflow.log_metric`, `mlflow.log_artifact`) con autologging automático para sklearn, xgboost, lightgbm, pytorch-lightning y transformers
- MLflow Projects: especificación de entornos reproducibles vía `MLproject` YAML con conda environment o Docker container, permitiendo reproducir cualquier experimento con `mlflow run`
- MLflow Models: formato de empaquetado estándar con `MLmodel` YAML que define el flavor, las dependencias y la firma de la API (input/output schema validado con pydantic)
- MLflow Registry REST API: endpoints para crear modelos, versiones, transiciones de estado y búsqueda, completamente consumibles desde CI/CD pipelines vía `curl` o el SDK Python
- Databricks Managed MLflow: versión enterprise con RBAC integrado, Unity Catalog para linaje de datos y modelos, workspace isolation, y Feature Store nativo integrado con el Registry

## Buena práctica

Usar `mlflow.set_tracking_uri()` con el servidor centralizado de la plataforma desde el inicio de cada experimento garantiza que ningún run quede registrado solo localmente y se pierda al destruir el entorno de desarrollo.
