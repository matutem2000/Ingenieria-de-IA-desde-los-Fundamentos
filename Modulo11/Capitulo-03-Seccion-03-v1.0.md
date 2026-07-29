# Módulo 11 – Capítulo 03 – Sección 03

# ETL vs ELT para datos empresariales que alimentan sistemas de IA

La elección entre ETL (Extract-Transform-Load) y ELT (Extract-Load-Transform) para los pipelines de datos que alimentan sistemas de IA enterprise no es solo una decisión técnica sino una decisión de arquitectura que afecta la latencia de disponibilidad de los datos, la capacidad de retroalimentación iterativa del pipeline, y los costos operacionales a escala. En el modelo ETL clásico, la transformación ocurre antes de cargar los datos en el destino: esto implica que los datos crudos del sistema legacy son procesados en un servidor de transformación intermedio (Informatica PowerCenter, IBM DataStage, Talend) antes de aterrizar en el data warehouse, lo que garantiza que solo datos limpios y conformados llegan al destino pero limita la capacidad de explorar los datos crudos para identificar patrones no anticipados durante el diseño del pipeline. En el modelo ELT que adoptaron los data warehouses cloud modernos (Snowflake, BigQuery, Redshift), los datos crudos se cargan primero en el data lake en su formato original y las transformaciones ocurren mediante SQL en el destino usando herramientas como dbt, lo que reduce el tiempo hasta disponer de los datos para análisis y permite que los AI Engineers accedan a los datos crudos para construir features no anticipadas por el pipeline original. Para sistemas de IA que alimentan RAG, el pipeline debe además incluir una etapa de chunking y embedding posterior a la transformación, con reindexación incremental en la base de datos vectorial cuando los documentos fuente cambian.

## Componentes críticos de la decisión ETL vs ELT

- Latencia de datos: ETL introduce latencia adicional por el paso de transformación intermedio; ELT permite que los datos crudos estén disponibles en minutos mientras las transformaciones se procesan en background
- Capacidad de exploración: ELT permite a los AI Engineers explorar datos crudos en el data lake para identificar features nuevas sin modificar el pipeline de transformación existente
- Herramientas ELT modernas: dbt (data build tool) para transformaciones SQL versionadas en Git, con tests de calidad de datos integrados (not_null, unique, accepted_values, relationships)
- Orquestación de pipelines: Apache Airflow para pipelines batch complejos con DAGs, Prefect para flujos más simples con Python nativo, o Dagster para pipelines con fuerte énfasis en observabilidad de datos
- Calidad de datos antes de IA: Great Expectations o Soda Core para validar contratos de datos en cada etapa del pipeline, fallando el job antes de que datos corruptos contaminen los índices vectoriales o los features del modelo

## Buena práctica

Para sistemas de RAG enterprise, el pipeline ELT debe incluir detección de cambios en documentos fuente (hashing MD5/SHA-256 del contenido) para reindexar solo los documentos modificados y no reconstruir el índice vectorial completo en cada actualización.
