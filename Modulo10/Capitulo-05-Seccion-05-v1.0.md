# Módulo 10 – Capítulo 05 – Sección 05

# Herramientas: Evidently AI, Whylabs y Grafana + Prometheus para LLM

El ecosistema de herramientas de monitoreo para modelos en producción se divide en tres categorías: herramientas especializadas en calidad y drift de modelos (Evidently AI, WhyLabs, Arize AI), herramientas generalistas de observabilidad extendidas para IA (Grafana + Prometheus con exporters custom), y plataformas de observabilidad de LLMs específicamente (LangSmith, Phoenix de Arize, Helicone, Langfuse). Evidently AI es open source (con versión cloud Enterprise) y genera reportes HTML y dashboards de drift, data quality y calidad de modelo con una API Python simple: `Report(metrics=[DataDriftPreset(), ClassificationPreset()]).run(reference_data=ref_df, current_data=prod_df)` produce un reporte completo de drift por columna con visualizaciones y tests estadísticos; el modo de monitoreo continuo permite publicar snapshots periódicos a su backend y ver dashboards de evolución temporal. WhyLabs es una plataforma SaaS que recibe estadísticas de distribución (no datos crudos, preservando privacidad) mediante su librería `whylogs` embebida en el pipeline de inferencia: `logger.log(df)` calcula automáticamente perfiles estadísticos (quantiles, histogramas, frecuencias) y los envía al backend de WhyLabs donde se comparan con el perfil de referencia. Para LLMs específicamente, Langfuse es la herramienta open source más adoptada: traza cada llamada al LLM con su prompt, respuesta, latencia, tokens usados y costo, y permite añadir evaluaciones personalizadas (LLM-as-a-judge scores) asociadas a cada trace para monitorear calidad en producción.

## Comparación de herramientas de monitoreo

- Evidently AI: open source, especializado en drift y calidad de datos/modelos, reportes HTML y JSON exportables, integrable en pipelines de Airflow o Prefect como un step de validación automático
- WhyLabs: SaaS, ingesta de perfiles estadísticos (no datos crudos), UI de monitoreo temporal, alertas nativas; privacidad por diseño al no transmitir datos de producción al backend
- Grafana + Prometheus: stack generalista extendida para IA mediante exporters custom (Python prometheus_client) que exponen métricas de modelo; dashboards de latencia, throughput y métricas custom de calidad
- Langfuse: open source (self-hosteable) para observabilidad de LLMs; tracing de prompts y respuestas, evaluaciones, costos por modelo; integración nativa con LangChain, LlamaIndex y OpenAI SDK
- Arize AI (Phoenix): plataforma de observabilidad para LLMs y ML clásico; embeddings visualization para detectar clustering drift, tracing de llamadas LLM, evaluaciones de hallucination y relevance

## Para recordar

Ninguna herramienta de monitoreo resuelve el problema de calidad de datos: son instrumentos de detección, no de prevención; el monitoreo efectivo requiere también un proceso definido de respuesta cuando las alertas se disparan.
