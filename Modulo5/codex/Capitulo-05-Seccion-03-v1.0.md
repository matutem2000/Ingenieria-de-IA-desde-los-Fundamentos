# Módulo 5 – Capítulo 05 – Sección 03

# Testing de integración: validación de cadenas y flujos completos

Los tests de integración en sistemas de IA validan que los componentes funcionan correctamente en conjunto: que el retriever recupera documentos relevantes del índice vectorial, que el prompt se construye con el contexto correcto, que el LLM genera una respuesta dentro de los criterios de calidad, y que el parser extrae la estructura esperada de esa respuesta. A diferencia de los unit tests con mocks, los tests de integración hacen llamadas reales al LLM o a un LLM de bajo costo como `claude-3-haiku-20240307` o `gpt-4o-mini` reservado para el entorno de test, incurriendo en costo real pero obteniendo validación end-to-end del flujo completo. La suite de integración debe ejecutarse de forma selectiva: localmente bajo demanda, automáticamente en el pipeline de CI en PRs que modifiquen prompts o la lógica de procesamiento, y en un scheduled job diario o nocturno para detectar degradaciones del comportamiento del modelo. El dataset de tests de integración debe incluir casos de prueba representativos del dominio real con criterios de evaluación explícitos: respuestas de referencia, propiedades que deben cumplirse, o un LLM-as-judge configurado para evaluar la calidad.

## Aspectos técnicos del testing de integración

- Dataset de evaluación curado: conjunto de 50-200 pares (input, criterio de calidad) representativos del dominio real, incluyendo casos difíciles y casos límite, versionado en el repositorio junto al código como `tests/eval/dataset.json`
- Tests de cadena RAG: verificar que para una pregunta del dataset, el retriever devuelve al menos un fragmento relevante (score de similitud > threshold), el prompt se construye con ese fragmento, y la respuesta del LLM menciona información del documento recuperado
- Comparación de prompts A/B: ejecutar el mismo dataset con dos versiones de prompt y comparar las métricas de calidad; el test "pasa" si la nueva versión no degrada la puntuación media en más de un 5%
- Validación de schema de salida estructurada: para endpoints que deben devolver JSON, verificar que el 100% de las respuestas del dataset son JSON válido parseado correctamente por el schema Pydantic objetivo
- Costos acotados en tests: usar `max_tokens=256` o `max_tokens=512` en los LLMs de test para limitar el costo de la suite, configurado vía variable de entorno `TEST_MAX_TOKENS` independiente del config de producción

## Principio rector

Los tests de integración son el único mecanismo que detecta la interacción entre componentes reales: el retriever que devuelve los documentos equivocados, el prompt que pierde variables al escalar el contexto, o el parser que falla ante un formato de respuesta que el modelo real produce pero el mock no simula.
