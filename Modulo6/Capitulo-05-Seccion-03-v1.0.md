# Módulo 6 – Capítulo 05 – Sección 03

# Reranking: modelos cross-encoder, Cohere Rerank, BGE Reranker

El reranking es una etapa de post-procesamiento que re-ordena los top-K chunks recuperados por el retriever (ya sea vectorial, BM25 o híbrido) usando un modelo más preciso pero computacionalmente costoso, mejorando la Precision@K de los chunks presentados al LLM generador. Los modelos bi-encoder (como los usados en embedding) codifican la query y el documento por separado y comparan sus vectores; los modelos cross-encoder codifican la query y el documento juntos en una sola pasada del transformer, permitiendo atención cruzada entre los tokens de ambos textos y produciendo una puntuación de relevancia mucho más precisa a costa de O(K) inferencias adicionales. Cohere Rerank v3 es el modelo de reranking como servicio más utilizado: acepta la query y una lista de hasta 1000 documentos, devuelve scores de relevancia de 0 a 1 para cada documento en una sola llamada API con latencia de 200–500ms; su precio de $2/millón de documentos rankeados hace que sea práctico usarlo sobre los top-100 chunks recuperados. BGE Reranker (BAAI/bge-reranker-v2-m3) es la alternativa open source: modelo cross-encoder de 568M parámetros que puede hostearse localmente con ~2GB VRAM y ejecutar reranking sin costos de API, comparable en calidad a Cohere Rerank según benchmarks de BEIR.

## Componentes técnicos del reranking

- Arquitectura cross-encoder: el modelo recibe concatenación [CLS] query [SEP] documento [SEP] y produce un score escalar de relevancia; la atención entre tokens de query y documento permite capturar relaciones semánticas finas que los bi-encoders no pueden detectar al no ver ambos textos simultáneamente
- Latencia del reranking: ranquear 100 documentos con BGE Reranker en GPU V100 toma ~200ms; con Cohere Rerank API, la latencia es 200–500ms para hasta 100 documentos en paralelo; el overhead de reranking es siempre justificado cuando mejora la calidad de los chunks en los primeros 5 slots que el LLM realmente usa
- Pipeline two-stage retrieval: primera etapa: recuperar top-100 chunks con retriever rápido (vectorial o híbrido); segunda etapa: rerankear los 100 chunks con cross-encoder y usar solo los top-5 o top-10 para el contexto del LLM; la segunda etapa eleva Precision@5 sin penalizar Recall@100 de la primera etapa
- Cohere Rerank v3: soporta 100+ idiomas; acepta hasta 1000 documentos por llamada; devuelve scores normalizados de relevancia; latencia <500ms para 100 documentos; precio $2/millón de unidades de búsqueda; incluye un modelo lite ($0.10/millón) para casos con menor presupuesto
- BGE Reranker v2-m3: modelo open source (Apache 2.0); 568M parámetros; contexto de 8192 tokens; funciona tanto para reranking como para scoring de relevancia directa; disponible en Hugging Face y desplegable con sentence-transformers o TGI (Text Generation Inference)
- FlashRank: librería Python de reranking ultrarápido que implementa modelos cross-encoder pequeños (ms-marco-MiniLM, ms-marco-TinyBERT) en CPU con latencias de 5–20ms para 100 documentos; útil cuando la GPU no está disponible o el presupuesto de latencia es muy ajustado

## Para recordar

El reranking es la mejora de mayor ROI en sistemas RAG porque usa los chunks ya recuperados por el retriever y los reordena con mayor precisión sin incrementar el costo de embedding ni el número de llamadas a la base vectorial; la mejora de Precision@5 es consistente y medible.
