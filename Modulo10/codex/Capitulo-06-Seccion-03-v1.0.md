# Módulo 10 – Capítulo 06 – Sección 03

# Continuous training: reentrenar automáticamente cuando la calidad cae por debajo del umbral

El continuous training (CT) es la práctica de reentrenar automáticamente un modelo cuando se detecta que su calidad en producción ha caído por debajo de un umbral predefinido, sin requerir intervención manual para iniciar el proceso, completando el ciclo de MLOps desde el monitoreo hasta la actualización del modelo en producción. La implementación del CT requiere tres componentes integrados: un sistema de monitoreo que emita una señal cuando la calidad degradada se detecta (drift score > umbral, accuracy rolling 7-day < threshold, o llegada de suficientes nuevos datos etiquetados), un sistema de triggers que convierta esa señal en el inicio de un pipeline de reentrenamiento (webhook de Evidently, cron-based con evaluación de condición, o event-driven con SQS/Pub-Sub), y un pipeline de reentrenamiento completamente automatizado que produce y despliega un nuevo modelo sin intervención humana si pasa los gates de calidad. El nivel de automatización del CT puede variar: CT Level 1 (reentrenamiento automático, despliegue manual aprobado por humano), CT Level 2 (reentrenamiento automático, despliegue automático con gates de calidad automáticos y rollback automático si las métricas de producción se degradan). Las consideraciones de seguridad del CT son críticas: un loop de reentrenamiento automático puede amplificar bias si los datos de producción reflejan sesgos del modelo anterior, y requiere mecanismos de data quality validation antes del reentrenamiento y diversidad del training set garantizada.

## Aspectos técnicos del continuous training

- Triggers de reentrenamiento: basados en tiempo (reentrenar cada N días independientemente de la calidad), en datos (cuando se acumulan N nuevas muestras etiquetadas), en calidad (cuando el drift score o las métricas de producción superan el umbral definido)
- Data collection para reentrenamiento: pipeline automático que combina el dataset histórico con las nuevas muestras de producción (con sus labels reales o sintéticos), balanceando la distribución para evitar catastrophic forgetting
- Gates de aprobación automáticos: el pipeline de CT solo despliega el nuevo modelo si accuracy_new > accuracy_champion * 0.99 Y las métricas de producción en canary (primeras N requests) no muestran degradación significativa
- Rollback automático: si las métricas de producción se degradan dentro de las primeras 1-6 horas después del despliegue automático, el sistema revierte al modelo anterior sin intervención humana
- Monitoreo de loops de reentrenamiento: alertas cuando el pipeline de CT se ejecuta con frecuencia inusualmente alta (posible señal de concept drift severo o problema en los datos de producción)

## Buena práctica

El continuous training sin validación robusta del dataset de reentrenamiento es más peligroso que no tenerlo: los datos de producción contienen feedback loops (el modelo anterior influye en los datos que ve el siguiente) que pueden crear espirales de degradación si no se gestionan explícitamente.
