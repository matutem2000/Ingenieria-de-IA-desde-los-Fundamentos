# Módulo 12 – Capítulo 03 – Sección 05

# Evaluación del RAG implementado: RAGAS y golden dataset de prueba

La evaluación del pipeline RAG usa el framework RAGAS con cuatro métricas principales sobre un golden dataset de 200 pares pregunta-respuesta-contexto anotados manualmente por ingenieros del dominio. Faithfulness mide si cada afirmación de la respuesta puede respaldarse en el contexto recuperado, usando un LLM evaluador para identificar afirmaciones que no tienen soporte en los chunks; el sistema debe alcanzar faithfulness >= 0.85 para considerarse aceptable en producción. Answer relevance mide si la respuesta aborda lo que la pregunta solicita, penalizando respuestas evasivas o que responden una pregunta diferente; el umbral es 0.80. Context precision mide qué proporción de los chunks recuperados son realmente relevantes para la pregunta, indicando la eficiencia del retrieval; context recall mide si toda la información necesaria para responder está presente en los chunks recuperados. El golden dataset se divide 80/20 entre evaluación continua y test set reservado para comparaciones entre versiones del pipeline.

## Métricas RAGAS implementadas

- Faithfulness: proporción de afirmaciones de la respuesta respaldadas por el contexto; umbral >= 0.85 en golden dataset
- Answer Relevance: coseno entre el embedding de la query y el embedding de la respuesta generada; umbral >= 0.80
- Context Precision: proporción de chunks recuperados relevantes sobre el total recuperado; umbral >= 0.75
- Context Recall: proporción de información necesaria presente en los chunks recuperados; umbral >= 0.70
- Evaluación continua: pipeline automatizado que corre RAGAS sobre 20 muestras aleatorias del golden dataset en cada deploy

## Para recordar

El golden dataset de evaluación RAGAS es un activo tan valioso como el código del sistema — su calidad determina la confianza en las métricas, y debe mantenerse actualizado cuando el dominio de conocimiento evoluciona.
