# Módulo 6 – Capítulo 01 – Sección 06

# Cierre: RAG como disciplina de ingeniería, no solo integración de APIs

Construir un sistema RAG de producción exige aplicar los mismos principios de ingeniería de software que cualquier sistema distribuido crítico: diseño de interfaces claras entre componentes, observabilidad completa del pipeline, gestión de fallos en cada etapa, versionado de índices y modelos, y evaluación continua con métricas cuantitativas. La proliferación de frameworks como LangChain, LlamaIndex y Haystack democratizó el acceso a los componentes de RAG, pero también generó la ilusión de que integrar APIs es suficiente; en producción, la diferencia entre un prototipo funcional y un sistema confiable radica en las decisiones de ingeniería que los frameworks no toman por el desarrollador: qué chunking strategy usar, cómo manejar documentos que se actualizan, cómo detectar degradación del índice, cómo correlacionar trazas entre el retriever y el generador. Los sistemas RAG de mayor impacto en producción, como el de Notion AI o el sistema de asistencia de GitHub Copilot, son el resultado de meses de iteración sobre pipelines de evaluación, no de semanas de integración de APIs. Tratar RAG como una disciplina de ingeniería implica establecer desde el inicio datasets de evaluación golden, pipelines de CI/CD para el índice, SLOs para latencia y faithfulness, y procesos de revisión de degradaciones.

*"La diferencia entre un programador y un ingeniero de software es que el ingeniero sabe que el sistema seguirá ejecutándose mucho después de que él haya terminado de escribir el código."* — Dave Parnas, pionero de la ingeniería de software modular

## Principio rector

RAG no es una integración sino una arquitectura: cada decisión de diseño en el pipeline de ingesta, indexación, recuperación y generación tiene impacto directo y medible en la calidad de las respuestas que los usuarios experimentan.
