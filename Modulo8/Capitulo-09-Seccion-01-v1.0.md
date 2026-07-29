# Módulo 8 – Capítulo 09 – Sección 01

# Model registry local: Hugging Face Hub, MLflow y soluciones self-hosted

Un model registry es el componente de infraestructura que centraliza el almacenamiento, versionado, metadata y control de acceso de los modelos de ML a lo largo de su ciclo de vida, análogamente a como un container registry (Docker Hub, ECR) gestiona las imágenes de contenedor. Hugging Face Hub es el registry de facto para modelos open weights: su API de upload (`huggingface_hub.HfApi.upload_folder()`), el protocolo Git-LFS para versionado de archivos grandes y el sistema de model cards estandarizados permiten publicar modelos con metadata estructurada, historial de commits y soporte para download eficiente con reanudación automática via `hf_transfer`. Para organizaciones con requisitos de privacidad o compliance que impiden usar Hugging Face Hub público, las alternativas self-hosted incluyen Hugging Face Hub Enterprise (instancia privada), Gitea con soporte LFS para versionado básico, y MinIO como object storage con una capa de API custom para metadata de modelos. MLflow Model Registry es la opción más integrada para organizaciones que ya usan MLflow para tracking de experimentos: almacena modelos con stages (Staging, Production, Archived), permite transiciones de stage con aprobación manual o automática via CI/CD, y expone una API Python (`mlflow.register_model()`, `mlflow.pyfunc.load_model()`) que abstrae el almacenamiento subyacente (S3, Azure Blob, GCS o NFS local).

## Componentes de un model registry

- Almacenamiento de artefactos: los pesos del modelo (archivos SafeTensors, GGUF, PyTorch .bin) se almacenan en object storage (S3, GCS, MinIO) o filesystem compartido (NFS, EFS); el registry gestiona la metadata y los punteros a los artefactos, no necesariamente el almacenamiento directo
- Versionado semántico: cada versión del modelo se identifica con un número de versión, un commit SHA del código de entrenamiento, el SHA del dataset de entrenamiento y los hiperparámetros usados; esta información permite reproducir el entrenamiento y auditar los cambios entre versiones
- Model card: documento estructurado (README.md en Hugging Face o YAML metadata en MLflow) que describe el modelo: arquitectura base, tarea, dataset de entrenamiento, métricas de evaluación, limitaciones conocidas, instrucciones de uso y consideraciones éticas; es el contrato de API humano del modelo
- Control de acceso: modelos privados en Hugging Face Hub requieren token de autenticación para descarga; MLflow usa los permisos del object storage subyacente; para modelos propietarios o con datos sensibles en el fine-tuning, el control de acceso granular es un requisito de compliance
- Búsqueda y descubrimiento: el registry debe permitir buscar modelos por tarea, arquitectura, idioma, fecha y métricas de evaluación; Hugging Face Hub lo implementa con filtros en la interfaz web y via `list_models()` en la API Python; MLflow permite búsqueda por tags y métricas registradas

## Para recordar

El model registry no es un lujo sino la infraestructura mínima para gestionar múltiples versiones de modelos en producción: sin él, los equipos pierden trazabilidad de qué modelo está corriendo en producción y no pueden ejecutar rollbacks controlados.
