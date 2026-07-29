# Módulo 4 – Capítulo 06 – Sección 04

## Alertas y Respuesta

Recopilar métricas sin definir alertas es observabilidad sin consecuencias: los datos existen, pero el equipo no es notificado cuando algo sale mal hasta que el problema ya ha afectado a los usuarios. Las alertas son el mecanismo que convierte la observabilidad pasiva en gestión proactiva. Su diseño requiere tanto rigor técnico como disciplina organizacional: alertas demasiado sensibles producen fatiga de alertas (el equipo las ignora porque la mayoría son falsos positivos); alertas con umbrales demasiado permisivos detectan los problemas demasiado tarde.

El diseño de alertas para sistemas de IA debe abordar las siguientes categorías:

**Alertas de infraestructura (umbrales absolutos):** son las más simples y las más maduras del arsenal de alertas. La latencia P95 supera los 5 segundos, la tasa de error supera el 5%, la disponibilidad del servicio cae por debajo del 99%. Estas alertas se configuran con herramientas estándar (Grafana Alerting, Datadog Monitors, CloudWatch Alarms) y su respuesta es operativa: reiniciar un servicio, escalar recursos, activar el proveedor de LLM de respaldo.

**Alertas de costo (umbrales de gasto):** son específicas de sistemas de IA. Un pico anómalo en el consumo de tokens puede indicar un agente en bucle, una consulta maliciosa que genera contextos muy extensos, o un error en el pipeline que replica solicitudes. Alertas de gasto diario o por hora con umbrales definidos sobre la línea base histórica permiten detectar estos anomalías antes de que produzcan facturas inesperadas.

**Alertas de calidad (umbrales estadísticos):** son las más complejas y las más valiosas. Cuando las métricas RAGAS ejecutadas periódicamente muestran que el context recall ha caído por debajo de un umbral histórico, o cuando la tasa de reformulación de consultas supera el doble de su valor de referencia, una alerta debe notificar al equipo. Estas alertas requieren la ejecución periódica (diaria o semanal) del pipeline de evaluación sobre el conjunto de test fijo.

**Alertas de drift de modelo:** cuando el proveedor de LLM actualiza el modelo subyacente (algo que ocurre sin aviso en versiones no fijadas como `gpt-4o` vs. `gpt-4o-2024-11-20`), el comportamiento del sistema puede cambiar de forma que las métricas de infraestructura no detectan. Comparar el output del modelo ante un conjunto de prompts de referencia con sus outputs históricos esperados permite detectar cambios de comportamiento silenciosos.

Los **Service Level Objectives (SLO)** para sistemas de IA merecen una discusión específica porque son fundamentalmente distintos a los SLOs de sistemas determinísticos. Un sistema de software tradicional puede comprometerse a que el 99.9% de las solicitudes se completen en menos de 200ms, porque el output es determinístico. Un sistema de IA no puede comprometerse a que el 99.9% de las respuestas sean correctas — la calidad del output es probabilística. Los SLOs adecuados para sistemas de IA son los que miden calidad estadística a lo largo del tiempo: "el promedio de faithfulness medido semanalmente sobre el conjunto de evaluación no será inferior a 0.85", o "la tasa de escalada no superará el 15% en ningún período de 24 horas". Estos SLOs requieren el establecimiento previo de líneas base realistas sobre el comportamiento real del sistema.

El **runbook de respuesta a incidentes** de un sistema de IA debe incluir procedimientos específicos que van más allá del runbook estándar de operaciones:

- Cómo verificar si un cambio de calidad es causado por el LLM (problema del proveedor), el retriever (problema del índice vectorial), la base de conocimiento (documentos desactualizados) o el prompt (cambio accidental en el template).
- Cómo activar el modo de respaldo: un modelo alternativo, una versión fija del sistema anterior, o degradación controlada (responder solo las consultas simples y escalar las complejas).
- Cómo comunicar la degradación a los usuarios cuando el sistema está operando con calidad reducida.
- Los criterios de rollback: bajo qué condiciones el sistema revierte automáticamente a la versión anterior del pipeline.

> **Nota del Arquitecto:** La fatiga de alertas es el mayor enemigo de la observabilidad. En sistemas donde la latencia tiene alta varianza natural, una alerta configurada con un umbral demasiado bajo dispara varias veces al día sin indicar ningún problema real. El equipo aprende a ignorarla — y cuando la alerta correcta dispara, también la ignoran. Diseñe las alertas con la misma disciplina con que diseña el sistema: definición clara de qué mide, umbral justificado por datos históricos, y propietario responsable de la respuesta.

Un sistema con alertas bien diseñadas se comporta como un sistema autovigilado: el equipo sabe cuándo el sistema está saludable no porque estén mirando el dashboard constantemente, sino porque cuando algo sale de los parámetros esperados, el sistema se lo dice.
