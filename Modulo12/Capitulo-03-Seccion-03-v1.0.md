# Módulo 12 – Capítulo 03 – Sección 03

# Configuración de la base de datos vectorial: esquema, índices y filtros de metadatos

Qdrant se configura con una colección principal llamada `knowledge_base` que almacena vectores de 1536 dimensiones (dimensión de text-embedding-3-small) con distancia coseno. El índice HNSW se configura con m=16 y ef_construction=100, parámetros que ofrecen el balance óptimo entre velocidad de construcción del índice y recall en búsquedas con colecciones de hasta 500k vectores; para colecciones mayores, se incrementa m a 32. La cuantización escalar (Scalar Quantization) se habilita para reducir el uso de memoria en un 75% con una penalización de recall inferior al 2%, lo que es aceptable dado que el reranking posterior corrige errores de recuperación del índice aproximado. El payload de cada punto incluye los metadatos necesarios para los filtros de la aplicación: `document_type` (adr/runbook/api-spec/doc), `team`, `ingested_at` (timestamp) y `source_url`; estos campos se indexan con payload indexes de Qdrant para que los filtros no requieran un full scan de la colección.

## Configuración del esquema de Qdrant

- Colección: knowledge_base con vectores float32 de 1536 dims, distancia coseno, HNSW m=16 ef_construction=100
- Cuantización: Scalar Quantization para reducción de memoria 75% con penalización de recall < 2% validada en benchmark interno
- Payload indexes: índices en campos document_type, team, ingested_at para filtros eficientes sin full collection scan
- Sparse vectors: colección configurada con vectores sparse BM25 para soporte de búsqueda híbrida nativa
- Particionamiento: colecciones separadas por entorno (knowledge_base_dev, knowledge_base_staging, knowledge_base_prod)

## Para recordar

Los filtros de metadatos en Qdrant deben indexarse explícitamente con payload indexes — sin ellos, cada búsqueda filtrada ejecuta un full scan de la colección, degradando la latencia a escala.
