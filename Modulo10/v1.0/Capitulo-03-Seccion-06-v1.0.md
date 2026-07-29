# Módulo 10 – Capítulo 03 – Sección 06

## Cierre: el model registry es el source of truth de todos los modelos de la organización

Sin un model registry centralizado, los modelos de una organización existen en un estado de entropía que se vuelve insostenible a medida que el número de modelos y equipos crece. Los síntomas de esta entropía son reconocibles: versiones del modelo nombradas con sufijos como `model_final_v3_REAL.pkl` dispersas en buckets de S3 sin estructura; endpoints de producción cuyo modelo subyacente nadie puede identificar sin investigación manual; equipos que descubren a través de un incidente de producción que el modelo que creían estar usando fue reemplazado silenciosamente hace tres semanas. Este estado no es el resultado de ingenieros descuidados: es el resultado esperado de operar sin la infraestructura correcta.

El model registry transforma este caos en un sistema gobernado donde cada modelo tiene una identidad única, un historial de versiones trazable, un estado explícito que refleja su posición en el ciclo de vida, y metadatos suficientes para que cualquier ingeniero —incluyendo alguien que no estuvo presente cuando el modelo fue creado— pueda entender qué hace el modelo, cómo fue creado, quién lo aprobó y quién es responsable de él. Esta transparencia no es solo una ventaja operacional: es un requisito regulatorio para categorías crecientes de sistemas de IA bajo el EU AI Act y las regulaciones sectoriales que lo complementan.

La implementación efectiva de un model registry requiere integración bidireccional con el pipeline de CI/CD. En la dirección de entrenamiento hacia el registry: los pipelines de entrenamiento registran modelos automáticamente en MLflow con todos los metadatos de linaje al completar exitosamente, sin que el ML Engineer tenga que ejecutar ningún paso adicional. En la dirección del registry hacia el sistema de despliegue: los cambios de estado en el registry disparan automáticamente los flujos de despliegue o notificación correspondientes via webhooks — cuando un modelo pasa a Production, ArgoCD actualiza la configuración del InferenceService de KServe sin intervención manual. Esta automatización bidireccional es lo que convierte el registry de un catálogo pasivo en un motor activo del pipeline de MLOps.

En organizaciones con decenas de modelos en producción, el model registry también actúa como **inventario estratégico** de la cartera de modelos. Permite identificar qué modelos están usando datasets que se van a deprecar (impacto cross-cutting que sin el registry requiere investigación manual en múltiples equipos), qué modelos tienen la mayor frecuencia de actualización y por tanto requieren mayor inversión en automatización de su pipeline de reentrenamiento, qué modelos llevan más de seis meses sin actualizarse y podrían estar acumulando concept drift, y qué modelos consumen los recursos de inferencia más caros y son por tanto los candidatos prioritarios de optimización para el equipo de FinOps. El registry como inventario estratégico convierte la información técnica sobre los modelos en insight de gestión para priorizar la inversión del equipo de plataforma.

## Principio rector

Un modelo sin registro es un artefacto sin identidad: no puede ser auditado, no puede ser reproducido, y no puede ser mantenido con confianza en producción. El model registry no es un añadido opcional al stack de MLOps: es la infraestructura base sobre la que el governance, el compliance y la reproducibilidad se construyen.

---

*"Without data, you're just another person with an opinion."*  
— W. Edwards Deming, estadístico y pionero de la gestión de calidad, cuya filosofía de mejora continua basada en datos es el fundamento del MLOps moderno.
