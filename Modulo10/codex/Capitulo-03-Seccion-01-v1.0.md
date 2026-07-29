# Módulo 10 – Capítulo 03 – Sección 01

# Model registry: catálogo centralizado de modelos, versiones y metadatos

Un model registry es el sistema de registro centralizado que actúa como source of truth para todos los modelos de una organización, almacenando no solo los artefactos binarios (pesos del modelo, tokenizer, configuración) sino también los metadatos que los hacen utilizables y auditables: versión semántica, framework y versión del framework, hash SHA256 del artefacto, métricas de evaluación offline, dataset de entrenamiento y su versión, hiperparámetros, estado del ciclo de vida (Staging/Production/Archived), y trazabilidad hacia el experimento de MLflow o el pipeline de entrenamiento que lo generó. A diferencia de un simple object storage con archivos nombrados, un model registry implementa el patrón de gestión de estados con transiciones controladas: un modelo no puede pasar de Staging a Production sin pasar por un gate de aprobación que puede ser automatizado (eval metrics sobre umbral) o manual (aprobación de un ML Engineer senior). Las implementaciones más adoptadas son MLflow Model Registry (open source, self-hosted o managed vía Databricks), SageMaker Model Registry (managed, integrado con AWS), Vertex AI Model Registry (managed, integrado con GCP), y Hugging Face Hub Enterprise para modelos de lenguaje. La elección entre estas soluciones depende del cloud provider principal, del volumen de artefactos y del grado de integración requerida con el pipeline de CI/CD.

## Conceptos clave del model registry

- Artefact storage: los pesos del modelo se almacenan en object storage (S3, GCS) con URIs inmutables por versión; el registry almacena el puntero y los metadatos, no el binario directamente
- Estado del ciclo de vida: transiciones explícitas entre None, Staging, Production y Archived con timestamps, responsable y justificación registrados en el audit log del registry
- Linaje de modelos: referencia trazable al experimento (run_id de MLflow), al dataset (URI + versión de DVC o LakeFS), y al código (commit SHA del repositorio de entrenamiento)
- Tags y metadatos personalizados: campos adicionales específicos de la organización como `compliance_reviewed`, `bias_evaluation`, `serving_latency_p99_ms` y `business_owner`
- Webhooks de estado: notificaciones automáticas a Slack, PagerDuty o sistemas de CI/CD cuando un modelo cambia de estado, permitiendo despliegues automáticos al pasar a Production

## Para recordar

El model registry no reemplaza el almacenamiento de artefactos: lo complementa añadiendo metadatos, gestión de estados y trazabilidad que hacen que un binario sea un modelo gestionado.
