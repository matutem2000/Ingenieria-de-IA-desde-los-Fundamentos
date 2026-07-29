# Módulo 6 – Capítulo 07 – Sección 01

# Arquitectura de producción: desacoplamiento de ingesta, índice y serving

Un sistema RAG de producción madura inevitablemente hacia una arquitectura de tres planos desacoplados: el plano de ingesta (ingest plane) que procesa documentos y actualiza el índice, el plano de índice (index plane) que almacena y sirve los vectores, y el plano de serving (query plane) que procesa las consultas de los usuarios en tiempo real. Este desacoplamiento es un prerequisito para escalar cada plano de forma independiente según su carga: la ingesta puede ser intensiva en CPU y GPU durante ventanas de procesamiento batch, mientras el serving requiere baja latencia y alta concurrencia constante; unirlos en un solo proceso obliga a sobre-aprovisionar recursos para el peor caso de ambas cargas simultáneamente. En producción, el plano de ingesta implementado como un pipeline de datos (Apache Airflow, Prefect, AWS Step Functions) con workers escalables horizontalmente puede procesar decenas de miles de documentos por hora, notificando al índice cuando los vectores están listos; el plano de serving implementado como una API REST/gRPC con instancias de GPU para el modelo de reranking y CPU para la consulta vectorial puede atender miles de requests por segundo con latencia p99 <500ms. La interfaz entre los tres planos debe ser asíncrona y basada en eventos o colas (Kafka, SQS, Redis Streams) para garantizar que el procesamiento de ingesta no bloquee la disponibilidad del serving.

## Componentes de la arquitectura desacoplada

- Ingest plane: workers de procesamiento de documentos (parsing, cleaning, chunking, embedding) escalables horizontalmente con Kubernetes o AWS ECS; orquestados por Apache Airflow, Prefect o AWS Step Functions; throughput típico de 500–5000 documentos/hora dependiendo del volumen y la complejidad del enriquecimiento
- Index plane: base de datos vectorial (Qdrant, Pinecone, Weaviate) con réplicas de lectura para alta disponibilidad del serving; instancias separadas para escritura (actualizaciones del ingest plane) y lectura (queries del query plane) para evitar contención de recursos
- Query plane: API de serving (FastAPI, gRPC) que recibe la query del usuario, ejecuta la búsqueda vectorial y léxica, aplica reranking y construye el contexto para el LLM; escalado horizontal con load balancer; circuit breakers hacia la base vectorial y el LLM para resiliencia
- Message queue entre planos: Apache Kafka o AWS SQS como cola de eventos entre el ingest plane y el index plane; garantiza que los vectores generados se persistan de forma ordenada y con retry automático en caso de fallos transitorios del index plane
- Configuration management: gestión centralizada de parámetros del pipeline (modelo de embedding, chunk_size, K del retriever, umbral de reranking) mediante un servicio de configuración como HashiCorp Consul o AWS Parameter Store; permite cambiar parámetros sin redespliegue
- Feature flags para el pipeline RAG: implementar feature flags que permitan activar/desactivar módulos del pipeline (reranking, HyDE, búsqueda híbrida) por porcentaje de tráfico; crítico para A/B testing de configuraciones en producción sin afectar a todos los usuarios simultáneamente

## Principio rector

El desacoplamiento de ingesta, índice y serving no es una optimización prematura sino un prerequisito arquitectónico para operar un sistema RAG a escala sin comprometer ni la velocidad de actualización del corpus ni la disponibilidad y latencia del serving.
