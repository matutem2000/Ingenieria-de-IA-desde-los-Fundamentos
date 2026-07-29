# Módulo 10 – Capítulo 04 – Sección 05

# Data quality: validación y monitoreo de calidad de los datos que alimentan el sistema

La calidad de datos en un sistema de IA no es un problema que se resuelve una vez durante el desarrollo del pipeline: es un proceso de monitoreo continuo que detecta degradaciones en las propiedades estadísticas de los datos de entrada (esquema, distribución, completitud, consistencia) antes de que impacten la calidad de los modelos. El framework estándar de la industria para validación de datos es Great Expectations, que permite definir "expectations" (afirmaciones sobre propiedades esperadas de los datos) en Python: `expect_column_values_to_be_between("age", 0, 120)`, `expect_column_proportion_of_unique_values_to_be_between("user_id", 0.95, 1.0)`, `expect_column_distribution_to_match_other("feature_x", reference_dataset)`. Estas expectations se ejecutan automáticamente en cada run del pipeline de datos, y si alguna falla, el pipeline puede detenerse antes de usar datos inválidos para entrenamiento o inferencia. Para el monitoreo continuo en producción, las distribuciones estadísticas de las features de entrada se comparan periódicamente contra una distribución de referencia (el dataset de entrenamiento) usando tests estadísticos como Kolmogorov-Smirnov (para variables continuas), Chi-squared (para variables categóricas) y Population Stability Index (PSI), con alertas cuando el p-value cae por debajo de 0.05 o el PSI supera 0.2.

## Dimensiones de calidad de datos para sistemas de IA

- Completitud: porcentaje de valores nulos por columna; alertar si supera el umbral definido (ej. >5% para features críticas, >20% para features secundarias)
- Frescura: tiempo desde la última actualización de las features en el online store; latencia de materialización medida y alertada cuando supera el SLO
- Distribución: drift estadístico medido con KS-test (variables continuas) o Chi-squared (variables categóricas), ejecutado periódicamente comparando datos de producción contra distribución de referencia
- Esquema: validación automática de que el schema (columnas, tipos, cardinalidades) coincide con el contrato definido; cambios de schema detectados inmediatamente antes de que rompan el pipeline
- Consistencia referencial: validación de que los identificadores (user_id, item_id) en los datos de features existen en los sistemas fuente y no hay data corruption por JOINs incorrectos

## Para recordar

La validación de datos debe ejecutarse en cada etapa del pipeline, no solo al inicio: datos que entran correctos pueden corromperse en transformaciones intermedias, y la detección tardía convierte un problema de datos en un incidente de producción.
