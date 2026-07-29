# Módulo 10 – Capítulo 06 – Sección 02

# Orquestadores de pipelines: Airflow, Prefect, Kubeflow y Metaflow

Los orquestadores de pipelines de MLOps tienen en común que gestionan la ejecución de flujos de trabajo como grafos acíclicos dirigidos (DAGs) con dependencias entre tareas, reintentos automáticos, y registro de ejecuciones, pero difieren significativamente en su modelo de programación, sus primitivas de ejecución y su integración con el ecosistema de ML. Apache Airflow es el orquestador más adoptado en la industria con el ecosistema de operadores más amplio (AWS, GCP, Databricks, dbt), pero su modelo de programación Python-based-DAG tiene curva de aprendizaje alta y el testing local es complejo; los ML pipelines en Airflow suelen delegar el cómputo pesado a Kubernetes via `KubernetesPodOperator` o a clusters de Spark via `SparkSubmitOperator`. Prefect adopta un modelo más cercano al código Python estándar usando decoradores (`@flow`, `@task`) que permiten testing local trivial con `if __name__ == "__main__": my_flow()`, y su modelo de ejecución distribuida usa un servidor central (Prefect Cloud o self-hosted) con workers que se despliegan donde el cómputo ocurre (Kubernetes, ECS, Lambda). Kubeflow Pipelines está diseñado específicamente para ML y se integra nativamente con Kubernetes: los componentes son contenedores Docker y el pipeline se define en Python con el SDK de KFP, generando un YAML de Argo Workflows; tiene integración nativa con el Kubeflow ecosystem (Training Operator para distributed training, Katib para hyperparameter tuning). Metaflow de Netflix se destaca por su modelo de branching para experimentos paralelos y su integración nativa con AWS (S3 para artefactos, Batch para cómputo) con un sistema de versionado de artefactos único por step.

## Comparación técnica de orquestadores

- Apache Airflow: ecosistema más amplio, operadores para decenas de servicios, scheduling basado en cron con backfill nativo; complejidad operativa alta, sensible a cambios de código de DAGs en producción
- Prefect: modelo de programación Python puro con decoradores, testing local trivial, UI moderna, deployment flexible (Kubernetes, Docker, Process); menor overhead operativo que Airflow
- Kubeflow Pipelines: integración nativa con Kubernetes y ecosistema Kubeflow, componentes reutilizables como contenedores, MLMD para tracking de artefactos; requiere cluster Kubernetes dedicado
- Metaflow: diseñado para data scientists (no DevOps), branching nativo para experimentos A/B de pipelines, versionado automático de artefactos por run; fuerte integración con AWS, menor soporte multi-cloud
- Criterio de selección: Airflow para organizaciones con múltiples tipos de pipelines de datos; Prefect para equipos que priorizan developer experience; Kubeflow para plataformas Kubernetes-first; Metaflow para equipos ML en AWS con foco en experimentación

## Principio rector

La elección del orquestador determina la cultura de desarrollo de pipelines: priorizar la experiencia del ML Engineer (Prefect, Metaflow) sobre la potencia del operador de datos (Airflow) resulta en mayor adopción y menos pipelines abandonados en favor de scripts ad-hoc.
