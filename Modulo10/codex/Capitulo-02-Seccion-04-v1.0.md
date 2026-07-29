# Módulo 10 – Capítulo 02 – Sección 04

# Abstracciones de plataforma: APIs internas que ocultan complejidad de infraestructura

Las abstracciones de plataforma son los contratos de interfaz que definen cómo los equipos consumidores interactúan con la infraestructura sin necesitar conocer su implementación subyacente: un equipo de AI Engineering debe poder lanzar un training job especificando solo el número de GPUs, la imagen Docker y el script de entrada, sin configurar manualmente nodos de Kubernetes, seleccionar instance types, o gestionar tolerations y affinities de scheduling. Estas abstracciones se implementan típicamente como un SDK Python (similar a como Weights & Biases expone su SDK `wandb.init()` o como SageMaker expone `Estimator`), un CLI interno, y una API REST OpenAPI-documented que puede ser consumida por herramientas de CI/CD. El diseño de una buena abstracción sigue el principio de "progressive disclosure": la interfaz simple cubre el 80% de los casos, pero permite que los usuarios avanzados accedan a configuraciones más granulares vía parámetros opcionales sin romper la API estable. Una abstracción incorrecta es aquella que obliga a los equipos a escribir workarounds o a bypassear la plataforma, lo cual indica que la abstracción no resuelve el problema real.

## Conceptos clave de las abstracciones de plataforma

- Training Job API: abstrae la complejidad de Kubernetes Job/PyTorchJob/TFJob en una interfaz simple `platform.submit_training(config)` que selecciona automáticamente el runtime correcto
- Serving API: `platform.deploy_model(model_uri, resources)` que crea automáticamente el InferenceService de KServe, configura el ingress, registra el endpoint en el service catalog y habilita monitoring
- Data API: acceso a datasets y features mediante rutas semánticas (`platform.load_dataset("user_events/v3")`) que resuelven automáticamente a la ubicación en S3 con las credenciales correctas
- Experiment API: wrappers sobre MLflow o W&B que añaden automáticamente metadatos corporativos (team, project, cost_center) a cada run, y enforcement de convenciones de naming
- Versioning contract: toda abstracción expuesta tiene una versión semántica explícita y un período de deprecación anunciado de al menos 90 días antes de su eliminación

## Para recordar

Una abstracción de plataforma exitosa es aquella que un ML Engineer adopta porque le facilita el trabajo, no porque se lo exijan: si requiere coerción para su adopción, la abstracción está mal diseñada.
