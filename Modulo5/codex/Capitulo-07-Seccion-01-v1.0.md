# Módulo 5 – Capítulo 07 – Sección 01

# Métricas de evaluación: exactitud, fidelidad, relevancia y coherencia

La evaluación de sistemas de IA requiere métricas que capturen dimensiones diferentes de la calidad de una respuesta: no existe una métrica única que lo capture todo, y la elección del conjunto de métricas debe alinearse con los requisitos del caso de uso específico. La fidelidad (faithfulness) mide si la respuesta está fundamentada exclusivamente en el contexto provisto, sin introducir información externa o inventada; es la métrica crítica en sistemas RAG donde las alucinaciones son el riesgo principal. La relevancia (answer relevancy) mide si la respuesta responde directamente a la pregunta formulada, penalizando respuestas que aunque sean verídicas resultan tangenciales o incompletas respecto a lo que el usuario preguntó. La coherencia (coherence) evalúa si la respuesta es internamente consistente, gramaticalmente correcta y fluye de forma lógica; es especialmente importante en respuestas largas donde el modelo puede contradecirse entre párrafos. La exactitud (accuracy o correctness) compara la respuesta con una ground truth conocida, aplicable cuando existe una respuesta correcta objetiva (preguntas factuales, clasificación, extracción de entidades con valores esperados definidos).

## Aspectos técnicos de las métricas de evaluación

- Faithfulness en RAGAS: descompone la respuesta en afirmaciones atómicas y verifica qué porcentaje de ellas puede inferirse del contexto recuperado usando el LLM como verificador; `faithfulness = afirmaciones_soportadas / total_afirmaciones`
- Answer relevancy en RAGAS: genera N preguntas a partir de la respuesta (reverse engineering) y mide la similitud coseno entre las preguntas generadas y la pregunta original; respuestas irrelevantes generan preguntas que divergen de la pregunta original
- Context recall: mide qué fracción de las declaraciones de la respuesta de referencia aparece en el contexto recuperado; detecta cuando el retriever no está trayendo los documentos correctos para responder la pregunta
- BERTScore F1: combina precision (qué tokens de la respuesta generada están en la referencia) y recall (qué tokens de la referencia están en la respuesta) a nivel de embeddings contextuales; más robusto que BLEU ante variación léxica y más interpretable que ROUGE-L
- Exactitud en clasificación: cuando el sistema clasifica categorías (intención del usuario, sentimiento, categoría de producto), accuracy, precision, recall y F1 por clase son las métricas estándar; el análisis de la matriz de confusión revela qué clases se confunden sistemáticamente

## Para recordar

Un sistema evaluado solo con faithfulness puede tener respuestas fieles pero no relevantes; solo con relevance puede tener respuestas relevantes pero alucinadas; la evaluación robusta requiere al menos tres métricas complementarias que cubran diferentes dimensiones de calidad.
