# Módulo 5 – Capítulo 06 – Sección 02

# Pipelines de evaluación automatizada en el ciclo de integración

Un pipeline de evaluación automatizada en CI ejecuta un conjunto curado de casos de prueba contra el sistema de IA en el estado actual del código, compara las métricas resultantes contra un baseline registrado, y decide si el cambio puede avanzar al siguiente stage del despliegue o debe ser bloqueado. La implementación con GitHub Actions es representativa: un job que se dispara cuando se modifican archivos en `prompts/`, `pipelines/` o `config/models.yaml`, instala las dependencias, ejecuta el script de evaluación con DeepEval o RAGAS sobre un dataset en `tests/eval/`, compara las métricas con los umbrales definidos en `eval_config.yaml`, y falla el job si alguna métrica cae por debajo del umbral, bloqueando el merge del PR. La gestión del dataset de evaluación es un primer-class citizen en este pipeline: el dataset se versiona en Git junto al código, cada PR que añade nuevos casos edge al dataset se considera una mejora de calidad, y el dataset crece orgánicamente con los casos de fallo observados en producción. Herramientas como LangSmith Datasets permiten mantener el dataset en la nube con versionado y ejecutar evaluaciones contra él desde el pipeline de CI via su Python SDK.

## Componentes principales del pipeline de evaluación

- Script de evaluación centralizado: `evaluate.py --dataset tests/eval/dataset.json --model claude-3-5-sonnet-20241022 --output results.json` que corre todos los casos del dataset, calcula métricas y genera un reporte JSON estructurado con score por caso y métricas agregadas
- Comparación de métricas con baseline: el baseline se almacena como `baseline_metrics.json` en el repositorio; el script de CI compara el resultado actual contra el baseline y falla si alguna métrica degrada más del umbral configurado (`delta_threshold: 0.03`)
- Informe de evaluación como comentario de PR: usando la API de GitHub, el pipeline publica automáticamente las métricas de evaluación como un comentario en el PR con una tabla de comparación baseline vs actual, permitiendo revisión rápida sin salir de GitHub
- Dataset versionado con DVC: para datasets grandes (>500 MB con embeddings pre-computados), usar DVC (Data Version Control) para versionar el dataset en S3 o GCS y referenciar la versión exacta desde el pipeline de CI
- Paralelización de la evaluación: dividir el dataset en N chunks y ejecutar N jobs en paralelo (GitHub Actions matrix) para reducir el tiempo total del pipeline de evaluación de minutos a segundos cuando el dataset tiene >100 casos

## Buena práctica

El dataset de evaluación es el activo más valioso del pipeline de CI de IA; invertir en su crecimiento continuo —añadiendo casos de los fallos en producción— es más impactante que sofisticar las métricas de evaluación sobre un dataset estático.
