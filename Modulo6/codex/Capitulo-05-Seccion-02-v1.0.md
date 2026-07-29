# Módulo 6 – Capítulo 05 – Sección 02

# Recuperación híbrida: combinar dense y sparse retrieval con RRF y puntuaciones ponderadas

La recuperación híbrida combina los resultados de un retriever denso (vectorial) y un retriever disperso (BM25 o SPLADE) en una lista unificada de resultados ordenados por relevancia combinada, aprovechando las fortalezas complementarias de ambos enfoques. Reciprocal Rank Fusion (RRF), propuesto por Cormack et al. (2009), es el algoritmo de fusión más utilizado en producción: asigna a cada documento un score igual a la suma de 1/(k + rank_i) donde rank_i es la posición del documento en cada lista y k=60 es un hiperparámetro de suavizado que reduce la influencia de las posiciones más altas; no requiere normalizar los scores de los retrievers (que tienen escalas incompatibles) y es robusto ante outliers. La alternativa de fusión por puntuaciones ponderadas (weighted score fusion) normaliza los scores de ambos retrievers a [0,1] y combina linealmente con coeficientes alpha y (1-alpha): `score_final = alpha * score_vectorial + (1-alpha) * score_BM25`; permite ajustar la contribución relativa de cada retriever según el dominio pero requiere calibración del parámetro alpha mediante evaluación. Weaviate implementa búsqueda híbrida nativa con el parámetro `alpha` en su API; Qdrant combina internamente dense y sparse con su soporte de vectores esparsos SPLADE.

## Aspectos técnicos de la recuperación híbrida

- Reciprocal Rank Fusion (RRF): formula RRF(d) = sum_i(1/(k+r_i)); k=60 es el valor recomendado por el paper original; no requiere normalización de scores; robusto y efectivo como baseline; fácil de implementar con cualquier par de retrievers independientes
- Weighted score fusion: normalizar scores a [0,1] con min-max scaling y combinar linealmente; alpha=0.5 da igual peso a ambos retrievers; alpha>0.5 favorece el retriever vectorial; requiere calibración de alpha mediante búsqueda en grid sobre el dataset de evaluación
- SPLADE (SParse Lexical AnD Expansion): modelo de embedding disperso que produce vectores con miles de dimensiones mayoritariamente cero, donde cada dimensión corresponde a un término del vocabulario; combina la eficiencia de los índices invertidos con la capacidad de expansión de vocabulario de los modelos de lenguaje; disponible en naver-splade-v3
- Ensemble retriever en LangChain: clase `EnsembleRetriever` que combina múltiples retrievers con pesos configurables usando RRF; acepta cualquier objeto que implemente la interfaz retriever, incluyendo BM25Retriever y VectorStoreRetriever
- Búsqueda híbrida nativa en Weaviate: parámetro `alpha` en la query controla el balance entre vectorial (alpha=1) y BM25 (alpha=0); el motor ejecuta ambas búsquedas internamente y aplica fusion; latencia ligeramente mayor que búsqueda individual por el overhead del merge
- Costos adicionales de la hibridación: la búsqueda híbrida requiere mantener tanto el índice vectorial (en RAM o GPU) como el índice invertido BM25 (en disco con I/O eficiente); Elasticsearch + pgvector o Weaviate son las opciones que mejor integran ambos índices en un solo sistema operacional

## Principio rector

Implementar recuperación híbrida como configuración estándar en sistemas de producción; el costo incremental de mantener un índice BM25 junto al vectorial es mínimo comparado con la ganancia sistemática de Recall@K en queries léxicamente específicas.
