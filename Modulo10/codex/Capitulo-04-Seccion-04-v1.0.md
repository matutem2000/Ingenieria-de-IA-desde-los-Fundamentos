# Módulo 10 – Capítulo 04 – Sección 04

# Data versioning: DVC y LakeFS para reproducibilidad de experimentos

El versionado de datos es la capacidad de identificar de forma única y recuperar exactamente el conjunto de datos que se usó para entrenar cualquier versión de un modelo, y es tan crítico para la reproducibilidad como el versionado del código fuente: un mismo código de entrenamiento aplicado sobre datos distintos produce modelos distintos, y sin versionado de datos no es posible diagnosticar regresiones de calidad, reproducir experimentos ni cumplir con requisitos de auditoría que exigen saber exactamente qué datos de clientes fueron usados en cada modelo. DVC (Data Version Control) extiende Git para versionar datasets y modelos de gran tamaño almacenándolos en remote storage (S3, GCS, Azure Blob, SSH) mientras guarda en Git solo un archivo `.dvc` con el hash MD5 del contenido; `dvc repro` reconstruye automáticamente cualquier etapa del pipeline si los inputs (datos o código) han cambiado, y `dvc params diff` compara hiperparámetros entre versiones. LakeFS adopta un enfoque diferente: actúa como un sistema de control de versiones Git-like directamente sobre object storage (S3, GCS) sin necesitar copiar los datos, usando referencias (branches, commits, tags) que apuntan a los mismos objetos subyacentes con costo cero de branching; `lakectl commit` crea un snapshot atómico de todo el estado del data lake, y cualquier experimento puede ser reproducido haciendo `lakectl checkout <commit-id>` para recuperar exactamente los datos de ese momento.

## Aspectos técnicos del versionado de datos

- DVC tracking: `dvc add data/train.parquet` crea `data/train.parquet.dvc` con hash MD5, que se versiona en Git; `dvc push` sube al remote storage; `dvc pull` restaura la versión exacta del dataset
- DVC pipelines: `dvc.yaml` define el grafo de transformaciones con inputs, outputs y comandos; `dvc repro` ejecuta solo las etapas cuyos inputs cambiaron, similar al comportamiento de `make`
- LakeFS branching: cada experimento puede trabajar en su propio branch del data lake (`feature/experiment-42`) con aislamiento completo de las modificaciones de datos hasta hacer merge al branch principal
- LakeFS commits atómicos: una operación de `lakectl commit` captura el estado de millones de archivos en un snapshot instantáneo usando content-addressable storage, sin copiar datos físicamente
- Integración con el modelo de linaje: tanto DVC (`dvc.lock` con hashes exactos) como LakeFS (commit SHA del data lake) proveen los identificadores únicos que se registran en el model registry como parte del linaje del modelo

## Buena práctica

Registrar el hash del dataset (DVC) o el commit del data lake (LakeFS) junto con el run_id de MLflow en cada experimento crea automáticamente el linaje completo datos-experimento-modelo sin esfuerzo adicional.
