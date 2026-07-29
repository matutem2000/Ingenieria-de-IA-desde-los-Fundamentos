# Módulo 10 – Capítulo 08 – Sección 05

# Retención y eliminación: políticas de ciclo de vida para modelos y datos de entrenamiento

Las políticas de retención y eliminación para modelos y datos de entrenamiento son más complejas que para datos operacionales tradicionales porque introducen tensiones entre dos requisitos potencialmente contradictorios: el derecho al olvido del GDPR (que exige eliminar datos de un individuo cuando lo solicita) y la necesidad de reproducibilidad de experimentos (que exige conservar los datos de entrenamiento exactos mientras el modelo derivado esté en producción). Esta tensión se resuelve con diferentes estrategias según el tipo de dato: los logs de inferencia (prompts y respuestas de producción) tienen una retención corta (90 días) con eliminación automática; los datasets de entrenamiento se retienen mientras el modelo derivado esté en Production en el registry, con eliminación programada 30 días después de que el último modelo que los usó sea Archived; los pesos del modelo se retienen indefinidamente en el model registry con metadata de cuándo fue archivado y por qué. El "right to erasure" del GDPR cuando se aplica a datos de entrenamiento plantea el problema del "machine unlearning": si los datos de un usuario específico fueron usados en el entrenamiento, eliminar esos datos del dataset no modifica el modelo ya entrenado que puede haber memorizado esa información; la solución práctica es el reentrenamiento del modelo desde cero con el dataset que excluye al usuario afectado, lo cual es costoso y define un SLA de cumplimiento (ej. máximo 30 días para completar el proceso de unlearning).

## Políticas de ciclo de vida técnicas

- Clasificación de artefactos: logs de inferencia (retención corta: 30-90 días), datasets de entrenamiento (retención larga: mientras el modelo esté en Production + 30 días), pesos del modelo (retención indefinida en Archived), metadatos y linaje (retención indefinida)
- Automated lifecycle policies: S3 Lifecycle Rules o GCS Object Lifecycle Management que mueven objetos a storage classes más baratos (Glacier/Coldline) después de N días y los eliminan después de M días, configurados automáticamente cuando un modelo cambia a estado Archived
- Right to erasure workflow: proceso documentado para procesar solicitudes de eliminación de datos de entrenamiento; incluye identificar todos los datasets afectados, ejecutar el pipeline de datos con el dato eliminado, reentrenar el modelo afectado, y actualizar el registry con la nueva versión "cleaned"
- Model archiving: proceso de pasar un modelo de Production a Archived con registro de la justificación (sustituido por nueva versión, producto descontinuado, requisito legal), manteniendo los pesos disponibles pero el endpoint desactivado
- Audit de retención: reporte mensual automático de todos los artefactos (datasets, modelos) que están acercándose a su fecha de expiración de política, para que los data owners puedan decidir si extender o confirmar la eliminación

## Principio rector

La política de retención de artefactos de IA debe ser explícita desde el diseño del sistema, no decidida ad-hoc cuando se necesita espacio en almacenamiento: la eliminación no planificada de un dataset de entrenamiento puede hacer irresponsable a un modelo en producción que ya no puede ser auditado.
