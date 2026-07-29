# Módulo 12 – Capítulo 07 – Sección 03

# Evaluación de calidad: faithfulness, relevance, completeness y user satisfaction

La evaluación de calidad del sistema integrador combina métricas automáticas con RAGAS y evaluación humana mediante feedback implícito en producción. Faithfulness mide si cada afirmación de la respuesta tiene soporte en los documentos recuperados; se implementa en dos pasos: el LLM extrae las afirmaciones atómicas de la respuesta, y luego evalúa si cada afirmación está respaldada por algún chunk del contexto, reportando la proporción (score 0-1). Answer relevance mide si la respuesta aborda la pregunta formulada calculando el coseno entre el embedding de la pregunta y el embedding de la respuesta generada. Completeness es una métrica personalizada que evalúa si la respuesta incluye todos los puntos clave que el anotador del golden dataset identificó como necesarios; se implementa con un LLM evaluador que recibe la respuesta y la respuesta esperada y clasifica qué puntos clave están cubiertos. User satisfaction se mide con feedback implícito: tasa de seguimiento de conversación (el usuario continúa la sesión), tasa de reformulación (repite la misma pregunta) y rating explícito opcional de 1-5 estrellas.

## Métricas de evaluación de calidad

- Faithfulness RAGAS: proporción de afirmaciones atómicas de la respuesta respaldadas por el contexto recuperado
- Answer Relevance: coseno(embedding(query), embedding(respuesta)) con umbral de aceptación >= 0.80
- Completeness personalizada: LLM evaluador que clasifica cobertura de puntos clave del golden dataset (0%, 50%, 100%)
- Context Precision: proporción de chunks recuperados realmente relevantes sobre el total de chunks del contexto
- User Satisfaction: feedback implícito (session continuation rate, reformulation rate) + rating explícito opcional

## Para recordar

Las métricas automáticas de calidad como RAGAS son una aproximación al juicio humano — deben complementarse con evaluación humana periódica y con feedback implícito del comportamiento real del usuario en producción.
