# Módulo 10 – Capítulo 03 – Sección 06

# Cierre: el model registry es el source of truth de todos los modelos de la organización

Sin un model registry centralizado, los modelos de una organización existen en un estado de entropía: versiones nombradas `model_final_v3_REAL.pkl` en buckets de S3 sin estructura, endpoints de producción cuyo modelo subyacente nadie recuerda cómo fue entrenado, y equipos que descubren a través de un incidente que el modelo que están usando en producción fue reemplazado por error hace dos semanas. El model registry transforma este caos en un sistema gobernado donde cada modelo tiene una identidad única, un historial de versiones trazable, un estado explícito que refleja su posición en el ciclo de vida, y metadatos suficientes para que cualquier ingeniero pueda entender qué hace el modelo, cómo fue creado y quién es responsable de él. La implementación efectiva de un model registry requiere integración bidireccional con el pipeline de CI/CD: los pipelines de entrenamiento registran modelos automáticamente con todos los metadatos de linaje, y los cambios de estado en el registry disparan automáticamente los flujos de despliegue o notificación correspondientes. En organizaciones con decenas de modelos en producción, el model registry también actúa como inventario estratégico: permite identificar qué modelos están usando datos que se van a deprecar, qué modelos tienen deuda técnica acumulada, y qué modelos tienen la mayor frecuencia de actualización y por tanto requieren mayor inversión en automatización de su pipeline.

## Principio rector

Un modelo sin registro es un artefacto sin identidad: no puede ser auditado, no puede ser reproducido, y no puede ser mantenido con confianza en producción.

---

*"Without data, you're just another person with an opinion."*
— W. Edwards Deming, estadístico y pionero de la gestión de calidad, cuya filosofía de mejora continua basada en datos es el fundamento de MLOps moderno.
