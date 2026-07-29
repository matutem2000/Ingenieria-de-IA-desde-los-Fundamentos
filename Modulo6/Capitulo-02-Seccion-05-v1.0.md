# Módulo 6 – Capítulo 02 – Sección 05

# Evaluación de modelos de embedding: MTEB benchmark y métricas de recuperación

El Massive Text Embedding Benchmark (MTEB), publicado por Hugging Face y mantenido como leaderboard público en hf.co/spaces/mteb/leaderboard, es el estándar de la industria para evaluar modelos de embedding en 56 datasets y 8 categorías de tareas: retrieval, classification, clustering, pair classification, reranking, summarization, bitext mining y STS. Un modelo que lidera el ranking global de MTEB no necesariamente es el mejor para el caso de uso específico; por ejemplo, el subcategory "Retrieval" del MTEB usa 15 datasets de BEIR (BioASQ, HotpotQA, FiQA, etc.) que miden específicamente la capacidad de recuperar documentos relevantes, que es la tarea central en RAG. Las métricas de evaluación de retriever en RAG se miden sobre datasets con relevance judgments anotados (qrels): Recall@K mide qué fracción de los documentos relevantes están entre los top-K recuperados; MRR (Mean Reciprocal Rank) pondera inversamente la posición del primer documento relevante; NDCG@K (Normalized Discounted Cumulative Gain) pondera la posición logarítmicamente y soporta relevance gradada (0, 1, 2).

## Métricas de recuperación y su interpretación

- Recall@K: métrica principal para RAG; mide el porcentaje de documentos relevantes recuperados entre los top-K resultados; Recall@5 entre 0.7 y 0.85 es el umbral práctico para sistemas de producción de calidad
- Precision@K: fracción de los K documentos recuperados que son relevantes; trade-off inverso con Recall@K; útil cuando el contexto del LLM es limitado y cada slot de chunk tiene alto costo en tokens
- MRR (Mean Reciprocal Rank): promedio de 1/posición del primer resultado relevante; sensible a la posición del primer hit; más relevante que Recall cuando el usuario o el LLM solo lee el primer resultado
- NDCG@K (Normalized Discounted Cumulative Gain): métrica que maneja relevance gradada (escala de 0 a 3) y pondera logarítmicamente la posición; estándar en el benchmark TREC y en los datasets de BEIR
- MTEB Retrieval subcategory: los datasets clave son NFCorpus (dominio médico), FiQA (finanzas), TREC-COVID (biomédico), ArguAna (argumentación) y SciFact (ciencia); rendimiento en estos datasets es predictivo del comportamiento en dominios similares
- Evaluación end-to-end con RAGAS: framework de evaluación que combina métricas del retriever (context recall, context precision) con métricas del generador (faithfulness, answer relevancy) en una sola pipeline ejecutable sobre datasets de Q&A con respuestas ground truth

## Para recordar

Nunca seleccionar un modelo de embedding basándose solo en el ranking global de MTEB; ejecutar siempre una evaluación sobre un subconjunto representativo del corpus y las queries de producción antes de tomar la decisión final.
