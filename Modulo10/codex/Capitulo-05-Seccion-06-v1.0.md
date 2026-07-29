# Módulo 10 – Capítulo 05 – Sección 06

# Cierre: monitorear un modelo en producción es diferente a monitorear una aplicación tradicional

Una aplicación web tradicional tiene un estado correcto o incorrecto bien definido: o retorna un HTTP 200 con el contenido esperado o retorna un error. Un modelo de IA en producción puede retornar un HTTP 200 con latencia correcta y sin errores de infraestructura, pero estar produciendo predicciones degradadas que nadie detecta hasta que el impacto en el negocio es visible: la tasa de conversión cae, los usuarios empiezan a quejarse, o un auditor identifica que el modelo está discriminando de forma inadvertida. Esta diferencia fundamental requiere dos capas de monitoreo complementarias: la capa de infraestructura (latencia, throughput, error rate, GPU utilization) que sí se puede monitorear con las mismas herramientas que cualquier microservicio, y la capa de calidad del modelo (drift, métricas de calidad, bias metrics, business KPIs) que requiere instrumentación específica y, en muchos casos, acceso a ground truth o a evaluadores humanos. El monitoreo de modelos en producción también introduce el concepto de "silent failure": un modelo puede seguir respondiendo correctamente desde el punto de vista de la infraestructura mientras que su calidad se degrada gradualmente por concept drift, cambios en los datos de entrada o comportamientos emergentes no anticipados; solo el monitoreo activo de métricas de calidad puede detectar estos fallos antes de que sean evidentes para los usuarios.

## Principio rector

El monitoreo de un modelo en producción debe comenzar a diseñarse antes del despliegue: qué métricas de calidad se recolectan, cómo se obtiene el ground truth, y cuál es el proceso de respuesta cuando la calidad cae, son preguntas que deben responderse en el diseño del sistema, no después de un incidente.

---

*"In God we trust. All others must bring data."*
— W. Edwards Deming, estadístico cuya filosofía de gestión basada en datos y mejora continua es el fundamento de los sistemas de monitoreo modernos en ingeniería de software y IA.
