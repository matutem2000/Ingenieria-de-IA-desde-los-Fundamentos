# Módulo 6 – Capítulo 02 – Sección 03

# Embeddings de dominio específico vs embeddings generales

Los modelos de embedding generales como text-embedding-3-large son entrenados sobre corpus web masivos y tienen representaciones sólidas para lenguaje natural cotidiano, pero exhiben limitaciones significativas en dominios altamente especializados donde el vocabulario, las relaciones conceptuales y los patrones semánticos difieren sustancialmente del lenguaje general. Un modelo general puede representar deficientemente términos médicos como "troponina" o "QTc" porque aparecen con baja frecuencia relativa en el corpus de preentrenamiento comparado con un modelo como BioBERT o PubMedBERT entrenado sobre 18 millones de artículos de PubMed. La solución más común es el fine-tuning contrastivo de un modelo base usando triplas (query, chunk_positivo, chunk_negativo) generadas del corpus de dominio, técnica implementada fácilmente con la librería sentence-transformers mediante `MultipleNegativesRankingLoss`; alternativamente, Voyage AI ofrece modelos pre-especializados (voyage-law-2, voyage-finance-2, voyage-code-3) que evitan el overhead del fine-tuning propio.

## Aspectos técnicos del dominio específico

- Domain gap: distancia entre la distribución de texto del corpus de entrenamiento del modelo y la distribución del corpus de producción; se cuantifica comparando el ranking de los modelos en MTEB vs. en un benchmark interno con queries y documentos del dominio objetivo
- Fine-tuning contrastivo: proceso de ajuste de los pesos del modelo usando pares (query, documento_relevante) del dominio; requiere al menos 1000–10000 pares de calidad; implementado con sentence-transformers en pocas decenas de líneas de código
- Hard negative mining: técnica crítica en fine-tuning donde los negativos se seleccionan como chunks similares al positivo pero no relevantes, forzando al modelo a aprender distinciones semánticas finas del dominio en lugar de diferencias obvias
- Vocabulary coverage: verificar qué porcentaje del vocabulario técnico del corpus está tokenizado eficientemente por el tokenizador del modelo base; vocabulario OOV (out-of-vocabulary) fragmentado en múltiples subword tokens degrada la calidad del embedding
- Benchmark interno: dataset de evaluación con 100–500 pares (query, documentos_relevantes) anotados por expertos del dominio, necesario para medir el delta de calidad entre el modelo general y el fine-tuneado antes de decidir el esfuerzo de especialización
- Modelos de código: text-embedding-ada-002 y voyage-code-3 muestran que el código es un dominio semántico distinto donde identificadores de variables, nombres de funciones y comentarios determinan la similitud; los modelos generales fallan en recuperación de snippets de código equivalentes escritos con diferente nomenclatura

## Buena práctica

Antes de iniciar un fine-tuning costoso, evaluar siempre voyage-3 o BGE-M3 sobre el corpus de dominio; en la mayoría de los casos, un modelo general de alta calidad evaluado con las queries reales supera al modelo genérico promedio y puede evitar meses de trabajo de especialización.
