# Módulo 10 – Capítulo 04 – Sección 06

# Cierre: los datos son el input más importante del sistema — su calidad determina todo lo demás

Los feature stores, los pipelines de datos, el versionado con DVC o LakeFS, y los frameworks de validación como Great Expectations no son componentes opcionales de una plataforma de IA madura: son la garantía de que los modelos se entrenan con datos correctos, consistentes y reproducibles, y de que los sistemas de inferencia reciben en producción la misma calidad de datos que el modelo vio durante el entrenamiento. El training-serving skew —la diferencia entre los datos usados en entrenamiento y los disponibles en inferencia— es una de las causas más frecuentes y más difíciles de diagnosticar de degradación de modelos en producción, y solo se resuelve sistemáticamente con un feature store que garantice que la misma lógica de cálculo produce las mismas features en ambos contextos. Un pipeline de datos bien construido es también el primer nivel de defensa contra incidentes de IA: si los datos de entrada a un modelo cambian de forma inesperada (un campo que empieza a venir nulo, una distribución que cambia por un bug en el sistema de origen), el pipeline de validación debe detectarlo antes de que el modelo procese esos datos y produzca predicciones incorrectas que afecten a los usuarios.

## Principio rector

La inversión en calidad de datos es siempre rentable: cada hora dedicada a construir validaciones de datos robustas evita días de investigación de incidentes de producción causados por datos incorrectos.

---

*"Torture the data, and it will confess to anything."*
— Ronald Coase, Premio Nobel de Economía, advirtiendo sobre el riesgo de extraer conclusiones incorrectas de datos de baja calidad o mal procesados.
