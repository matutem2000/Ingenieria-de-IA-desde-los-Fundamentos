# Módulo 11 – Capítulo 01 – Sección 03

# El AI Engineering enterprise stack: capas de aplicación, orquestación, plataforma y datos

El AI Engineering enterprise stack se organiza en cuatro capas jerárquicas que separan responsabilidades y permiten evolucionar cada capa de manera independiente sin romper los contratos entre ellas. La capa de aplicación contiene los agentes, chatbots, pipelines de RAG, y APIs de negocio que consumen capacidades de IA y son desarrollados por equipos de producto; estas aplicaciones deben ser agnósticas al proveedor de LLM subyacente, comunicándose con la capa inferior a través de interfaces abstractas. La capa de orquestación incluye los frameworks de coordinación de agentes y flujos complejos (LangGraph, CrewAI, Semantic Kernel), los sistemas de gestión de prompts versionados, los routers de modelos que seleccionan dinámicamente entre GPT-4o, Claude Sonnet, o modelos open-source según costo y complejidad, y los mecanismos de retry y circuit breaker para llamadas a APIs externas. La capa de plataforma provee las capacidades compartidas: servicio de embeddings, bases de datos vectoriales (Pinecone, Weaviate, pgvector), model serving con Triton Inference Server o vLLM, y el control plane de LLMOps (MLflow, Weights & Biases, LangSmith). La capa de datos es la fundación: feature stores, data catalogs (Apache Atlas, DataHub), pipelines de ingesta (Kafka, Flink), y el data lake empresarial donde residen los documentos que alimentan los sistemas RAG.

## Componentes principales por capa

- Capa de aplicación: APIs RESTful versionadas, interfaces de chat, pipelines de procesamiento de documentos, y dashboards de análisis con IA embebida
- Capa de orquestación: LLM routers, prompt registries, orchestration frameworks, guardrails de seguridad (LlamaGuard, NeMo Guardrails), y sistemas de caché semántico
- Capa de plataforma: model serving (vLLM, Triton), vector databases, embedding services, feature stores, y plataformas de evaluación y experimentación
- Capa de datos: data lake (S3/ADLS/GCS), data warehouse (Snowflake/BigQuery), streaming (Kafka/Kinesis), y herramientas de calidad de datos (Great Expectations, Soda)
- Plano de control transversal: observabilidad (OpenTelemetry + Grafana), seguridad (Vault, IAM), gestión de costos (FinOps dashboards), y gobierno de modelos

## Idea central

Definir contratos explícitos entre capas del stack — mediante interfaces, esquemas de API, y SLOs — es lo que permite que equipos distintos evolucionen su capa sin bloquear a los demás.
