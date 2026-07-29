# Módulo 12 – Capítulo 04 – Sección 04

# Testing del agente: casos de prueba, escenarios de fallo y criterios de aceptación

El testing del agente combina pruebas unitarias de cada herramienta con mocks del pipeline RAG, pruebas de integración con el pipeline real sobre un conjunto reducido de documentos, y pruebas de evaluación de comportamiento sobre el golden dataset. Las pruebas unitarias validan que cada herramienta maneja correctamente sus errores: timeout, respuesta vacía del retrieval, argumentos inválidos y filtros que no coinciden con ningún documento. Las pruebas de integración validan los flujos completos más importantes: pregunta simple (1 llamada a herramienta), pregunta compuesta (2-3 llamadas), pregunta fuera del dominio (agente declina correctamente) y pregunta con prompt injection (agente ignora las instrucciones maliciosas). Los criterios de aceptación para el agente incluyen: tasa de task completion >= 80% en el golden dataset, tasa de hallucination <= 10% medida con faithfulness RAGAS, y tasa de bypass de inyección <= 5% en el red teaming de 50 casos.

## Tipos de pruebas del agente

- Unit tests de herramientas: pytest con unittest.mock para aislar cada herramienta del pipeline RAG subyacente
- Integration tests: flujos end-to-end sobre Qdrant de test con colección de 50 documentos representativos del dominio
- Behavior tests: golden dataset de 200 queries evaluadas por LLM-as-judge con criterios de task completion y faithfulness
- Failure scenarios: timeout de herramienta, retrieval vacío, LLM sin respuesta, loop detection (max_iterations alcanzado)
- Adversarial tests: 50 casos de prompt injection directa e indirecta para validar la robustez del system prompt

## Buena práctica

Los escenarios de fallo del agente deben testearse tan sistemáticamente como los flujos felices — el comportamiento del agente ante errores (timeout, retrieval vacío, injection) define la experiencia del usuario en producción.
