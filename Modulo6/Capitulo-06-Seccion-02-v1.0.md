# Módulo 6 – Capítulo 06 – Sección 02

# RAGAS: faithfulness, answer relevancy, context precision, context recall

RAGAS (Retrieval-Augmented Generation Assessment), publicado por Es et al. en 2023 y disponible como librería Python open source (github.com/explodinggradients/ragas), es el framework de evaluación de sistemas RAG más adoptado en la industria, definiendo cuatro métricas core que cubren las dimensiones críticas del sistema: dos métricas de calidad de la generación (faithfulness, answer relevancy) y dos métricas de calidad de la recuperación (context precision, context recall). La arquitectura de RAGAS usa un LLM como juez para evaluar cada dimensión, generando internamente preguntas o clasificaciones de relevancia; la calidad de los scores de RAGAS depende de la calidad del LLM evaluador, por lo que se recomienda usar GPT-4o o Claude 3 Sonnet como evaluador, con un costo de $0.01–0.05 por muestra de evaluación. RAGAS Score es la media armónica de las cuatro métricas, proporcionando un número único para comparar configuraciones; pero en la práctica los equipos de ingeniería monitorean cada métrica por separado porque degradaciones específicas indican problemas en componentes específicos: faithfulness baja indica hallucination del generador; context recall baja indica retriever deficiente.

## Las cuatro métricas core de RAGAS

- Faithfulness: mide qué fracción de las afirmaciones en la respuesta generada están soportadas por el contexto recuperado; RAGAS descompone la respuesta en declaraciones individuales y verifica cada una contra los chunks del contexto usando un LLM evaluador; rango [0,1]; <0.7 indica hallucinations sistemáticas del generador
- Answer Relevancy: mide qué tan directamente responde la respuesta generada a la pregunta del usuario; RAGAS genera variantes de preguntas que la respuesta podría responder y calcula la similitud coseno con la pregunta original; penaliza respuestas evasivas o que incluyen información irrelevante; rango [0,1]
- Context Precision: mide qué fracción de los chunks en el contexto recuperado son relevantes para responder la query; chunks irrelevantes en el contexto reducen la precision y pueden confundir al LLM generador; calculado como la fracción de chunks marcados como relevantes por el LLM evaluador; rango [0,1]
- Context Recall: mide qué fracción de la información necesaria para responder la query está presente en el contexto recuperado; requiere una respuesta ground truth para comparar; RAGAS descompone la respuesta ground truth en declaraciones y verifica cuáles están en el contexto; rango [0,1]
- Métricas adicionales de RAGAS: answer correctness (comparación semántica de la respuesta generada con la ground truth usando LLM + embedding similarity), answer similarity (similitud coseno entre respuesta generada y esperada), noise sensitivity (robustez ante chunks irrelevantes inyectados)
- Configuración práctica de RAGAS: instalar con `pip install ragas`; configurar LLM evaluador (`from ragas.llms import LangchainLLMWrapper`); preparar dataset con columnas question, answer, contexts[], ground_truth; ejecutar `evaluate(dataset, metrics=[faithfulness, answer_relevancy, context_precision, context_recall])`

## Para recordar

RAGAS proporciona un framework de evaluación automatizado que puede ejecutarse en CI/CD para detectar regresiones en cualquier métrica al hacer cambios en el pipeline; usarlo como gate de calidad antes de desplegar cambios a producción.
