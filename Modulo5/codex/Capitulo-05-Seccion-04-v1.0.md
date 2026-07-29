# Módulo 5 – Capítulo 05 – Sección 04

# Evaluación de calidad de respuestas: métricas automáticas y humanas

La evaluación de la calidad de las respuestas de un sistema de IA requiere métricas que capturen dimensiones que los tests de igualdad de string no pueden verificar: coherencia, relevancia, fidelidad al contexto, completitud y ausencia de alucinaciones. Las métricas automáticas se dividen en basadas en referencia (BLEU, ROUGE, BERTScore para comparar con una respuesta de referencia), sin referencia (usar un LLM-as-judge para evaluar la respuesta sin necesitar una respuesta golden), y específicas de RAG (faithfulness, answer relevancy, context recall de RAGAS). RAGAS es el framework de evaluación de RAG más adoptado: dado un dataset de preguntas, contextos recuperados y respuestas generadas, calcula `faithfulness` (¿la respuesta está fundamentada en el contexto?), `answer_relevancy` (¿la respuesta responde la pregunta?), y `context_recall` (¿el contexto recuperado contiene la información necesaria?). La evaluación humana sigue siendo el gold standard para calidad final: workflows de anotación donde evaluadores humanos puntúan respuestas en escala Likert (1-5) o realizan comparaciones pares (A/B preference) son necesarios para calibrar y validar las métricas automáticas.

## Métricas automáticas y humanas de calidad

- RAGAS `faithfulness`: mide si cada afirmación de la respuesta puede inferirse del contexto recuperado; score de 0 a 1, donde 1 significa que la respuesta no contiene información que no esté en el contexto (sin alucinaciones)
- RAGAS `answer_relevancy`: embeddings de la respuesta vs la pregunta para medir relevancia semántica; penaliza respuestas genéricas o que desvían el tema sin responder directamente la consulta del usuario
- BERTScore: compara la respuesta generada con una respuesta de referencia usando embeddings de BERT layer-wise; más robusta que BLEU/ROUGE ante variación léxica porque captura similitud semántica
- LLM-as-judge con escala: prompt al modelo evaluador con la pregunta, la respuesta, y una rúbrica de evaluación explícita (`[1=totalmente incorrecto, 5=perfectamente correcto]`); correlaciona bien con juicio humano cuando la rúbrica es específica
- Human evaluation con inter-annotator agreement: calcular Cohen's Kappa o Krippendorff's Alpha entre anotadores para medir la consistencia de la evaluación humana; un kappa < 0.6 indica que la tarea de evaluación es ambigua y la rúbrica necesita refinamiento

## Para recordar

Ninguna métrica automática captura toda la dimensionalidad de la calidad humana; la evaluación robusta de un sistema de IA requiere al menos una métrica automática para escala y evaluación humana periódica como ground truth para calibrar esa métrica.
