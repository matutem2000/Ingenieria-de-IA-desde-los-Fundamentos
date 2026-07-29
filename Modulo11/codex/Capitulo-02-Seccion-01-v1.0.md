# Módulo 11 – Capítulo 02 – Sección 01

# Enterprise AI reference architecture: capas, componentes y flujos de datos

Una arquitectura de referencia enterprise para IA no es un diagrama aspiracional sino un conjunto de decisiones de diseño documentadas que responden a restricciones reales: latencia máxima aceptable por caso de uso, requisitos de disponibilidad (SLA del 99.9% implica menos de 9 horas de downtime al año), modelo de seguridad de red (VPC, Private Link, Network Policies en Kubernetes), y estrategia de multi-cloud o cloud híbrido. La arquitectura de referencia define cinco flujos de datos primarios que coexisten en el sistema: el flujo de inferencia en tiempo real (petición de usuario → API Gateway → servicio de orquestación → LLM → respuesta), el flujo de recuperación en RAG (query → embedding service → vector database → reranker → contexto enriquecido), el flujo de ingesta de datos (fuentes enterprise → ETL/ELT → feature store/data lake), el flujo de evaluación (respuestas del modelo → evaluadores automatizados → métricas en MLflow/LangSmith), y el flujo de retroalimentación (feedback de usuario → dataset de mejora → ciclo de reentrenamiento o prompt optimization). Cada componente de la arquitectura debe documentarse con sus dependencias, SLOs, propietarios, y contratos de interfaz, permitiendo que diferentes equipos operen partes distintas del sistema sin acoplamiento innecesario.

## Componentes principales de la arquitectura

- API Gateway y autenticación: Kong, AWS API Gateway, o Azure APIM con OAuth 2.0/OIDC, rate limiting por cliente, y logging de todas las peticiones para auditoría
- Capa de orquestación de IA: servicio stateless que implementa la lógica de negocio, gestiona el contexto conversacional en Redis, y coordina las llamadas a LLMs, tools, y bases de datos vectoriales
- Servicio de embeddings compartido: instancia de text-embedding-3-large (OpenAI) o multilingual-e5-large desplegada centralmente para evitar duplicación de costos entre equipos
- Base de datos vectorial enterprise: Pinecone, Weaviate con RBAC, o pgvector sobre PostgreSQL con índices HNSW para búsqueda aproximada de vecinos cercanos a escala
- Plataforma de observabilidad: stack de OpenTelemetry para traces distribuidos, Prometheus para métricas de infraestructura, y LangSmith o Langfuse para trazas específicas de LLM

## Idea central

Una arquitectura de referencia enterprise reduce el tiempo de decisión de cada equipo al establecer las elecciones de componentes ya tomadas y dejar espacio solo para las decisiones genuinamente específicas de cada caso de uso.
