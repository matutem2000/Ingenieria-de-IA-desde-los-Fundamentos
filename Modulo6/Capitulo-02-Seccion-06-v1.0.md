# Módulo 6 – Capítulo 02 – Sección 06

# Cierre: elegir el modelo de embedding correcto para el dominio del problema

La elección del modelo de embedding es una de las decisiones más impactantes en la arquitectura de un sistema RAG porque determina el techo de calidad de toda la recuperación: ningún reranker, técnica de query expansion o prompt engineering puede compensar un embedding que no captura las relaciones semánticas relevantes del dominio. El proceso de selección debe ser empírico y sistemático: construir un conjunto de evaluación de 100–500 pares (query, chunk_relevante) representativos del uso real, ejecutar todos los candidatos (text-embedding-3, voyage-3, BGE-M3, nomic-embed) sobre ese dataset y comparar Recall@5 y NDCG@10; el modelo que mejora Recall@5 en 5–10 puntos porcentuales sobre la segunda opción justifica el costo adicional de API o el overhead de hosting. Considerar también el lock-in: los modelos de API (OpenAI, Voyage) requieren re-embedir todo el corpus si el proveedor depreca la versión o cambia el modelo, mientras que los modelos open source (BGE-M3, nomic-embed) bajo control propio eliminan ese riesgo pero requieren infraestructura de serving. En producción, el modelo de embedding debe tratarse como un componente versionado: el índice vectorial está acoplado a la versión específica del modelo, y cambiar el modelo implica reindexar todo el corpus.

*"En cualquier sistema de recuperación de información, la calidad de la representación es el límite superior de la calidad de la recuperación; ninguna mejora algorítmica posterior puede superar la información perdida en la proyección al espacio latente."* — Gerard Salton, pionero de la recuperación de información moderna

## Principio rector

Seleccionar el modelo de embedding mediante evaluación empírica sobre datos reales del dominio y tratarlo como una dependencia versionada del sistema; cualquier cambio de modelo requiere reindexado completo del corpus y re-ejecución del dataset de evaluación.
