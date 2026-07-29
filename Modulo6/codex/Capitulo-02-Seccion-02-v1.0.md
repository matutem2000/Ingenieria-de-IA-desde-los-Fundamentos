# Módulo 6 – Capítulo 02 – Sección 02

# Modelos de embedding: text-embedding-3, voyage-3, BGE, nomic-embed

El mercado de modelos de embedding en 2024–2025 ofrece opciones con trade-offs distintos en términos de rendimiento en benchmarks, costo por millón de tokens, latencia, tamaño de contexto y disponibilidad de hosting. OpenAI text-embedding-3-small y text-embedding-3-large introducen soporte nativo para reducción de dimensionalidad (Matryoshka Representation Learning) que permite comprimir los vectores de 1536 a 256 dimensiones con degradación mínima de rendimiento, reduciendo costos de almacenamiento hasta 6x. Voyage AI voyage-3 y voyage-3-lite lideran en benchmarks de recuperación para dominios legales, financieros y de código, con ventanas de contexto de hasta 32K tokens que permiten embedir documentos completos sin chunking; su costo de $0.006 por millón de tokens los hace competitivos con OpenAI. Los modelos open source como BGE-M3 (BAAI) y nomic-embed-text-v1.5 ofrecen rendimiento competitivo con los modelos de API, pueden hostearse en infraestructura propia (eliminando dependencias de terceros y latencias de red) y soportan fine-tuning sobre datos de dominio específico.

## Comparación técnica de modelos principales

- text-embedding-3-small (OpenAI): 1536 dimensiones nativas con MRL para reducción a 256–512; $0.02/millón de tokens; rendimiento MTEB promedio de 62.3; máximo 8191 tokens de contexto; opción más accesible para prototipado
- text-embedding-3-large (OpenAI): 3072 dimensiones nativas; $0.13/millón de tokens; MTEB promedio 64.6; superior en tareas de clasificación y clustering pero cost-prohibitive para corpus grandes
- voyage-3 (Voyage AI): 1024 dimensiones; 32K tokens de contexto; MTEB 68.32 en tareas de recuperación; especialización en dominios legales, financieros y científicos con modelos voyage-law-2, voyage-finance-2
- BGE-M3 (BAAI): modelo multilingüe de 500M parámetros; soporta dense, sparse y colbert retrieval desde un único modelo; hosting local en GPU con ~4GB VRAM; MTEB promedio 64.0; sin costo de API
- nomic-embed-text-v1.5 (Nomic AI): modelo open source con arquitectura modificada de BERT; 137M parámetros; soporte MRL; contexto de 8192 tokens; disponible vía Ollama para inferencia local sin GPU de alta gama
- bge-reranker-v2-m3 (BAAI): aunque técnicamente un reranker cross-encoder, se menciona en el mismo contexto porque complementa BGE-M3 en pipelines de recuperación de dos etapas

## Idea central

La elección del modelo de embedding no debe basarse en rankings globales de MTEB sino en evaluación sobre el corpus y las queries reales del caso de uso específico, donde los modelos de dominio especializado superan sistemáticamente a los modelos generales.
