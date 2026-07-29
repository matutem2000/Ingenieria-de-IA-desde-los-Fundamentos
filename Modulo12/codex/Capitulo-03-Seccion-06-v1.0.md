# Módulo 12 – Capítulo 03 – Sección 06

# Cierre: el pipeline RAG es el núcleo de conocimiento del sistema integrador

El pipeline RAG implementado en el proyecto final no es solo un componente técnico — es el mecanismo que convierte documentación dispersa en conocimiento accesible con precisión y trazabilidad. Cada decisión técnica del pipeline (chunking a 512 tokens, búsqueda híbrida RRF, reranking con Cohere, compresión de contexto) tiene consecuencias medibles en las métricas RAGAS y en el costo operativo del sistema. La evaluación con golden dataset cierra el loop: permite saber con precisión qué tan bien recupera el sistema, qué preguntas falla y dónde está el límite de la base de conocimiento. El pipeline de ingesta asíncrona y tolerante a fallos garantiza que la base de conocimiento se mantenga actualizada sin intervención manual. La arquitectura modular del pipeline — cada etapa intercambiable por otra implementación con la misma interfaz — permite iterar sobre cada componente de forma independiente, reemplazando el modelo de embedding o el reranker sin afectar el resto del sistema.

## Aspectos técnicos que integra este capítulo

- Pipeline de ingesta: parsers por tipo de fuente, deduplicación por hash SHA-256, cola asíncrona Celery + Redis
- Chunking híbrido: RecursiveCharacterTextSplitter a 512 tokens con CodeTextSplitter para bloques de código
- Qdrant: índice HNSW con cuantización escalar, payload indexes, sparse vectors para búsqueda híbrida
- Recuperación: RRF sobre BM25 + embeddings densos, reranking Cohere, compresión LLMChainExtractor
- Evaluación: RAGAS con faithfulness, answer relevance, context precision y context recall sobre golden dataset de 200 casos

## Para recordar

Un pipeline RAG bien diseñado y evaluado es la diferencia entre un sistema que responde y un sistema que responde correctamente.

*"Data quality is not a technical problem — it's an engineering discipline. The same applies to the knowledge that feeds your retrieval system." — Chip Huyen, Designing Machine Learning Systems*
