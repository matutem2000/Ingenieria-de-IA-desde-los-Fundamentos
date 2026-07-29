# Módulo 10 – Capítulo 04 – Sección 03

# Pipelines de datos para LLM: ingestión, limpieza y preparación de datos de entrenamiento

Los pipelines de datos para LLM difieren significativamente de los pipelines de ML clásico en escala y en complejidad de las transformaciones: mientras un dataset de ML tradicional puede procesarse en horas con Spark, un corpus de preentrenamiento de un LLM de tamaño medio (100B tokens) requiere pipelines distribuidos que corren durante días sobre cientos de nodos, con etapas de limpieza específicas para texto como deduplicación fuzzy (MinHash LSH), language identification (fastText), calidad de contenido (clasificadores de perplexidad con KenLM), y filtrado de contenido dañino. El pipeline de datos para fine-tuning de LLMs es más manejable en escala pero requiere mayor precisión en la calidad: el dataset de instruction tuning (pares prompt/completion) necesita pasar por validaciones de formato, filtrado de respuestas de baja calidad, deduplicación exacta (hash SHA256 de la muestra normalizada) y, opcionalmente, verificación de calidad con un modelo juez (LLM-as-a-judge via GPT-4 o Claude). Herramientas especializadas para este dominio incluyen: EleutherAI's `lm_datasets` para procesamiento de Common Crawl, `datatrove` de Hugging Face para pipelines de limpieza de texto a escala, `datasets` de Hugging Face para gestión de datasets con caching inteligente, y Apache Beam sobre Dataflow o Spark sobre EMR para el procesamiento distribuido.

## Etapas técnicas del pipeline de datos para LLM

- Ingestión: descarga y normalización de fuentes heterogéneas (Common Crawl WARC, GitHub, arXiv, Wikipedia dumps) con conversión a formato estándar (JSONL con campos text, source, timestamp, url)
- Limpieza de texto: eliminación de HTML/boilerplate (Trafilatura, Resiliparse), normalización Unicode, detección de idioma (fastText lid.176.bin), y filtros de calidad heurísticos (longitud mínima, ratio de caracteres especiales)
- Deduplicación: deduplicación exacta por hash del texto normalizado, y deduplicación fuzzy con MinHash + LSH (similitud de Jaccard > 0.8 entre documentos eliminando el duplicado más reciente)
- Filtrado de calidad: perplexity scoring con KenLM entrenado sobre texto de alta calidad (Wikipedia), clasificadores de calidad entrenados sobre curated vs web data, y listas de bloqueo de dominios de baja calidad
- Tokenización y empaquetado: tokenización con el tokenizer del modelo objetivo, empaquetado en secuencias de longitud fija (2048 o 4096 tokens) con document boundaries marcados, y almacenamiento en formato MosaicML MDS o Hugging Face datasets para carga eficiente durante el entrenamiento

## Para recordar

La calidad del corpus de entrenamiento determina más el comportamiento del LLM que la arquitectura: una hora invertida en mejorar los filtros de calidad del pipeline tiene mayor impacto que una hora ajustando hiperparámetros de entrenamiento.
