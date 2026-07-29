# Módulo 10 – Capítulo 04 – Sección 06

## Cierre: los datos son el input más importante del sistema — su calidad determina todo lo demás

Los feature stores, los pipelines de datos para LLMs, el versionado con DVC o LakeFS, y los frameworks de validación como Great Expectations no son componentes opcionales de una plataforma de IA madura: son la garantía de que los modelos se entrenan con datos correctos, consistentes y reproducibles, y de que los sistemas de inferencia reciben en producción la misma calidad de datos que el modelo vio durante el entrenamiento. Este conjunto de garantías es la diferencia entre un sistema de IA cuyo comportamiento se puede explicar y auditar, y uno cuyo comportamiento es opaco incluso para los equipos que lo construyeron.

El training-serving skew —la divergencia entre los datos de entrenamiento y los datos de inferencia— es una de las causas más frecuentes y más difíciles de diagnosticar de degradación de modelos en producción, precisamente porque no produce errores de sistema: el endpoint responde correctamente desde el punto de vista de la infraestructura mientras el modelo produce predicciones silenciosamente peores. El feature store es la solución estructural a este problema porque garantiza que la misma lógica de cálculo produce las mismas features en ambos contextos; sin él, las organizaciones dependen de la disciplina de los equipos individuales para mantener la consistencia, y esa disciplina falla inevitablemente bajo presión operativa.

Un pipeline de datos bien construido es también el primer nivel de defensa contra incidentes de IA: cuando los datos de entrada a un modelo cambian de forma inesperada —un campo que empieza a llegar nulo, una distribución que cambia por un bug en el sistema de origen, un cambio de schema no comunicado por un equipo upstream— el pipeline de validación debe detectar ese cambio antes de que el modelo procese esos datos y produzca predicciones incorrectas. Esta detección temprana convierte lo que podría ser un incidente de producción silencioso en una alerta de pipeline que el equipo puede investigar y resolver en horas, sin impacto visible para los usuarios.

El valor de la infraestructura de datos se hace visible en retrospectiva: las organizaciones que invirtieron en feature stores, versionado de datos y validación automática durante los primeros años de sus sistemas de IA son las que pueden responder rápidamente a preguntas de auditoría, reproducir experimentos de hace años, e investigar incidentes de producción con trazabilidad completa. Las organizaciones que no lo hicieron están, años después, tratando de reconstruir retroactivamente qué datos usaron en qué modelos, con la urgencia de auditorías regulatorias o de incidentes de producción que exigen respuestas que el sistema no puede proveer.

## Principio rector

La inversión en calidad de datos es siempre rentable cuando se mide correctamente: cada hora dedicada a construir validaciones de datos robustas evita días de investigación de incidentes de producción causados por datos incorrectos. El primer nivel de gobierno de un sistema de IA no está en el modelo ni en el serving layer —está en la calidad y la trazabilidad de los datos que alimentan el pipeline.

---

*"Torture the data, and it will confess to anything."*  
— Ronald Coase, Premio Nobel de Economía, advirtiendo sobre el riesgo de extraer conclusiones incorrectas de datos de baja calidad o mal procesados.
