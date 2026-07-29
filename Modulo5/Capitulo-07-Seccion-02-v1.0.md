# Módulo 5 – Capítulo 07 – Sección 02

# Frameworks de evaluación: RAGAS, DeepEval, TruLens

Los frameworks de evaluación de IA automatizan el cálculo de métricas de calidad sobre datasets de prueba, proveen CLI y Python API para integración en pipelines de CI, y permiten comparar versiones de sistemas de forma sistemática. RAGAS (Retrieval Augmented Generation Assessment) es el estándar de facto para evaluar sistemas RAG: calcula faithfulness, answer relevancy, context recall y context precision usando LLMs como evaluadores internos, soporta OpenAI y Anthropic como modelos de evaluación, y expone un DataFrame con resultados por fila del dataset que facilita el análisis de qué casos fallan. DeepEval es un framework de evaluación más general (no específico de RAG) con una API de pytest-compatible: define `LLMTestCase` con `input`, `actual_output`, `expected_output` y `retrieval_context`, y ejecuta `assert_test()` con métricas como `AnswerRelevancyMetric`, `FaithfulnessMetric`, `HallucinationMetric`, `ToxicityMetric`; el output es compatible con JUnit XML para integración directa en GitHub Actions. TruLens (de TruEra) añade una UI de dashboard web para explorar las trazas de evaluación, comparar experimentos y analizar la distribución de scores, siendo particularmente útil para equipos que necesitan una interfaz visual en lugar de resultados en consola.

## Componentes principales de los frameworks de evaluación

- RAGAS `evaluate()`: recibe un `Dataset` de HuggingFace con columnas `question`, `answer`, `contexts`, `ground_truth` y devuelve un dict con el score medio de cada métrica; integración directa con LangChain y LlamaIndex via `from ragas.integrations.langchain import evaluate`
- DeepEval `@pytest.mark.deepeval`: decorador que ejecuta las métricas sobre el test case y genera un reporte en `deepeval_results/`; el threshold de cada métrica es configurable por test (ej. `AnswerRelevancyMetric(threshold=0.7)`)
- TruLens `TruChain` y `TruLlama`: wrappers de instrumentación para LangChain y LlamaIndex que capturan automáticamente la traza completa (retrieval + generation) y calculan los "RAG triad" scores (context relevance, groundedness, answer relevance) con visualización en `tru.get_leaderboard()`
- Selección del modelo evaluador: los tres frameworks usan un LLM como juez interno; elegir un modelo más capaz que el evaluado (ej. usar GPT-4o para evaluar un sistema basado en Haiku) mejora la confiabilidad de las métricas pero aumenta el costo de evaluación
- Costo de la evaluación automatizada: calcular el costo esperado del dataset de evaluación antes de ejecutarlo (`dataset_size * avg_tokens_per_case * evaluador_precio`); para datasets de 100-500 casos el costo es típicamente $1-$10 por run con modelos de evaluación eficientes

## Principio rector

La elección del framework de evaluación debe basarse en el tipo de sistema que se evalúa (RAG vs agente vs clasificador), la forma en que el equipo preferirá consumir los resultados (CLI en CI vs dashboard visual), y el modelo evaluador disponible para el presupuesto del proyecto.
