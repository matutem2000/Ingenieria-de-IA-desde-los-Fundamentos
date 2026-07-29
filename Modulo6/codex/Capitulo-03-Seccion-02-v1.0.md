# Módulo 6 – Capítulo 03 – Sección 02

# Principales bases vectoriales: Pinecone, Weaviate, Qdrant, Chroma, pgvector

El ecosistema de bases de datos vectoriales maduró rápidamente entre 2022 y 2025, pasando de proyectos experimentales a plataformas de producción con SLAs, gestión de índices, filtrado híbrido y SDKs en múltiples lenguajes. Pinecone es la opción managed más madura, con arquitectura serverless que desacopla el almacenamiento del cómputo de búsqueda, latencia p99 <100ms para colecciones de hasta 1B vectores, y soporte nativo para filtrado por metadatos con índice invertido acoplado al vectorial; su limitación es el lock-in al proveedor y el costo por unidad de almacenamiento. Qdrant es la alternativa open source que más aceleradamente ganó adopción en producción: implementado en Rust con arquitectura de sharding nativo, soporta payloads JSON sin límite de esquema, filtrado híbrido vectorial+payload en una sola operación de búsqueda, cuantización escalar e cuantización de productos en memoria, y tiene una API gRPC de baja latencia además de REST; puede desplegarse en Kubernetes o como servicio managed en cloud.qdrant.io. pgvector extiende PostgreSQL con tipos de datos vector y operadores de similitud, permitiendo combinar búsqueda vectorial con SQL completo; es la opción de menor fricción para equipos que ya tienen PostgreSQL en producción.

## Comparación técnica de bases vectoriales

- Pinecone: serverless managed; escalado automático de pods; ingesta asíncrona batch; filtrado de metadatos con índice acoplado; precio por RU (Read Units) y WU (Write Units); sin deployment propio; ideal para equipos sin experiencia en infraestructura
- Weaviate: open source (Go); módulos pluggables para embedding (text2vec-openai, text2vec-cohere); búsqueda híbrida nativa BM25+vectorial con parámetro alpha; soporte GraphQL y REST; cluster distribuido nativo; hosted en WCS (Weaviate Cloud Services)
- Qdrant: open source (Rust); la opción de mayor rendimiento en benchmarks de latencia y throughput (ann-benchmarks.com); HNSW + cuantización escalar/producto/binaria; filtrado de payload con tipos ricos (geo, datetime, enumerados); gRPC + REST; Kubernetes-native
- Chroma: open source (Python/Rust); diseñado para prototipado y uso embebido en aplicaciones Python; modo in-memory o persistido en disco SQLite; no recomendado para producción con corpus >1M vectores; integración nativa con LangChain y LlamaIndex
- pgvector: extensión de PostgreSQL; índice HNSW e IVFFlat; sintaxis SQL estándar para similitud coseno (<=>), L2 (<->) y producto punto (<#>); compatible con toda la infraestructura existente de PostgreSQL (replicación, backups, RBAC); rendimiento inferior a soluciones especializadas para corpus >10M vectores
- Redis Stack con VSS (Vector Similarity Search): alternativa para equipos con Redis existente; índice HNSW o FLAT; soporta hybrid search con filtros de metadatos; latencia muy baja para corpus en memoria (<1M vectores); no escala bien fuera de RAM disponible

## Principio rector

La base de datos vectorial correcta no es la que tiene el mejor rendimiento en benchmarks abstractos, sino la que se integra con menor fricción a la infraestructura existente del equipo y puede operar de forma autónoma en producción sin overhead de gestión desproporcionado.
