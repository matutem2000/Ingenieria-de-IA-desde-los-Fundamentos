# Módulo 11 – Capítulo 01 – Sección 03

## El AI Engineering enterprise stack: capas de aplicación, orquestación, plataforma y datos

Una de las decisiones de diseño más importantes que toma un equipo de AI Engineering enterprise es la organización conceptual de su stack. Sin una arquitectura en capas explícita, los sistemas de IA tienden a crecer como monolitos donde la lógica de negocio, la coordinación de llamadas a LLMs, el acceso a datos, y la infraestructura de observabilidad están entrelazados en el mismo servicio o incluso en el mismo archivo. Este acoplamiento hace que cualquier cambio — actualizar el modelo, cambiar el proveedor de embeddings, agregar un segundo caso de uso — requiera tocar el sistema completo con el riesgo de introducir regresiones no anticipadas.

El AI Engineering enterprise stack se organiza en cuatro capas jerárquicas que separan responsabilidades y permiten evolucionar cada capa de manera independiente sin romper los contratos entre ellas. Esta separación no es solo una preferencia estética: es lo que hace posible que equipos distintos operen partes distintas del sistema sin acoplamiento operacional. El equipo de datos puede actualizar el pipeline de ingesta sin coordinar con el equipo de producto; el equipo de plataforma puede actualizar el motor de embeddings sin que los equipos de aplicación noten el cambio, siempre que el tiempo de respuesta y el esquema de vectores se mantengan estables.

La **capa de aplicación** contiene los agentes, chatbots, pipelines de RAG, y APIs de negocio que consumen capacidades de IA y son desarrollados por equipos de producto. Estas aplicaciones deben ser agnósticas al proveedor de LLM subyacente, comunicándose con la capa inferior a través de interfaces abstractas que encapsulan la selección del modelo y el manejo de errores. Cuando OpenAI cambia los precios o introduce rate limits más estrictos, las aplicaciones no deben necesitar modificaciones.

La **capa de orquestación** es el cerebro coordinador del sistema: incluye los frameworks de coordinación de agentes y flujos complejos (LangGraph, CrewAI, Semantic Kernel), los sistemas de gestión de prompts versionados, los routers de modelos que seleccionan dinámicamente entre GPT-4o, Claude Sonnet, o modelos open-source según costo y complejidad, y los mecanismos de retry y circuit breaker para llamadas a APIs externas. Es en esta capa donde se implementan los guardrails de seguridad (LlamaGuard, NeMo Guardrails) y el semantic caching que evita llamadas redundantes al LLM.

La **capa de plataforma** provee las capacidades compartidas que todos los casos de uso consumen: el servicio de embeddings, las bases de datos vectoriales (Pinecone, Weaviate, pgvector), el model serving con Triton Inference Server o vLLM para modelos self-hosted, y el control plane de LLMOps donde viven MLflow, Weights & Biases, y LangSmith. Esta capa es operada por el equipo de AI Platform Engineering y expone sus capacidades mediante APIs internas con SLOs definidos.

La **capa de datos** es la fundación: feature stores, data catalogs (Apache Atlas, DataHub), pipelines de ingesta (Kafka, Flink), y el data lake empresarial donde residen los documentos que alimentan los sistemas RAG. La calidad de toda la cadena de valor de la IA depende de la calidad de esta capa. Un embedding generado a partir de un documento corrupto o desactualizado produce retrieval de baja calidad que ninguna mejora en la capa de orquestación puede compensar.

> **Nota del Arquitecto:** El plano de control transversal — observabilidad (OpenTelemetry + Grafana), seguridad (Vault, IAM), gestión de costos (FinOps dashboards), y gobierno de modelos — no es una quinta capa sino una responsabilidad horizontal que cruza todas las capas. En la práctica, implementar este plano de control transversal es lo que permite al equipo de operaciones monitorear el sistema completo desde un único punto, independientemente de en qué capa se origina un problema.

## Componentes principales por capa

- **Capa de aplicación:** APIs RESTful versionadas, interfaces de chat, pipelines de procesamiento de documentos, y dashboards de análisis con IA embebida; desarrolladas con contratos de interfaz hacia la capa de orquestación que se mantienen estables aunque el modelo subyacente cambie.
- **Capa de orquestación:** LLM routers, prompt registries, orchestration frameworks, guardrails de seguridad (LlamaGuard, NeMo Guardrails), y sistemas de caché semántico; es el componente más frecuentemente desarrollado a medida por el equipo de AI Engineering.
- **Capa de plataforma:** model serving (vLLM, Triton), vector databases, embedding services, feature stores, y plataformas de evaluación y experimentación; operada como servicio interno con SLOs y documentación para los equipos consumidores.
- **Capa de datos:** data lake (S3/ADLS/GCS), data warehouse (Snowflake/BigQuery), streaming (Kafka/Kinesis), y herramientas de calidad de datos (Great Expectations, Soda); la fundación que determina el techo de calidad del sistema completo.
- **Plano de control transversal:** observabilidad (OpenTelemetry + Grafana), seguridad (Vault, IAM), gestión de costos (FinOps dashboards), y gobierno de modelos; cruza todas las capas y permite operar el sistema completo como una unidad coherente.

---

**Idea central:** Definir contratos explícitos entre capas del stack — mediante interfaces, esquemas de API, y SLOs — es lo que permite que equipos distintos evolucionen su capa sin bloquear a los demás. Sin esos contratos, la coordinación entre equipos se convierte en el cuello de botella del desarrollo.

Con la arquitectura de capas como marco conceptual, la sección siguiente introduce el modelo de madurez que permite diagnosticar en qué estado de implementación de este stack se encuentra actualmente la organización, y qué acciones técnicas concretas son necesarias para avanzar al siguiente nivel.
