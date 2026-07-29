# Módulo 10 – Capítulo 04 – Sección 02

# Feast, Hopsworks y Tecton: comparación de soluciones de feature store

Las tres plataformas de feature store más adoptadas en la industria tienen distintos posicionamientos que determinan su idoneidad para diferentes contextos: Feast es open source (mantenido por la Linux Foundation con contribuciones de Google, Twitter y Gojek), Hopsworks es open source con una versión Enterprise managed, y Tecton es una solución SaaS propietaria orientada a enterprise con foco en rapidez de time-to-value. Feast es la opción más flexible y con menor costo de licencia: define features en Python (`FeatureView`, `Entity`, `FeatureService`), soporta múltiples backends de almacenamiento (Redis, BigQuery, Snowflake, DynamoDB) y múltiples fuentes de datos (Parquet, Kafka, Kinesis), pero requiere mayor esfuerzo de operación ya que el equipo de plataforma debe gestionar la infraestructura subyacente. Hopsworks añade sobre el modelo de Feast un motor de ingesta streaming integrado (Flink), una UI para el feature store con estadísticas automáticas, versioning nativo de feature groups, y un modelo de entrenamiento de modelos integrado; la versión managed (Hopsworks AI) elimina la carga operativa pero con costo de licencia. Tecton es la opción con mayor abstracción operativa y las funciones más avanzadas (real-time transformations con baja latencia, backfilling automático, monitoring de feature drift nativo), pero a un costo significativamente mayor que las alternativas open source.

## Comparación técnica

- Feast: open source, deployment self-managed en Kubernetes, soporte para batch y streaming features vía Kafka, bajo costo de licencia pero mayor esfuerzo operativo del equipo de plataforma
- Hopsworks: open source con Enterprise tier, motor de streaming Flink integrado, feature versioning nativo con `FeatureGroup.insert()`, estadísticas automáticas de distribución en cada escritura
- Tecton: SaaS propietario, real-time feature computation con SLA de sub-100ms, automatic backfilling de features históricas, feature monitoring nativo; mayor costo pero menor esfuerzo operativo
- Criterio de selección por tamaño: Feast para equipos que ya operan Kubernetes y quieren control total; Hopsworks para equipos con necesidades de streaming y versioning avanzado; Tecton para organizaciones que priorizan velocidad de adopción sobre costo
- Integración con el model registry: los tres soportan integración con MLflow para registrar automáticamente las features usadas en cada training run como parte de los metadatos de linaje

## Buena práctica

Antes de elegir un feature store, validar con un proof of concept si la arquitectura online/offline soluciona el training-serving skew específico del caso de uso es más valioso que comparar features en papel.
