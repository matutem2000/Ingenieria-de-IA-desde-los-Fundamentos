# Módulo 5 – Capítulo 05 – Sección 06

# Cierre: pirámide de testing adaptada a sistemas de IA

La pirámide de testing clásica (muchos unit tests, menos tests de integración, pocos end-to-end) se adapta en sistemas de IA para incorporar una capa nueva: la evaluación de calidad, que no existe en el testing de software tradicional. La pirámide adaptada tiene cuatro capas: en la base, unit tests con mocks del LLM que verifican la lógica de Python (constructores de prompts, parsers, validators) ejecutados en milisegundos en cada commit; encima, tests de integración con LLMs reales sobre datasets curados ejecutados en PRs relevantes; luego, evaluaciones de calidad automatizadas con RAGAS o DeepEval ejecutadas en CI y en producción; y en la cúspide, evaluación humana periódica (semanal o mensual) como ground truth de calibración. El costo de ejecutar la pirámide completa es real —los tests de integración y evaluación tienen costo de API—, por lo que el triggering condicional basado en los archivos modificados es fundamental: solo los tests que pueden haber sido afectados por el cambio se ejecutan en cada run. La deuda de testing en sistemas de IA se acumula más rápido que en software tradicional porque los cambios de modelo son externos e imprevistos; un sistema sin regression testing es un sistema que descubre sus regresiones por reportes de usuarios, no por métricas propias.

## Capas de la pirámide de testing adaptada a IA

- Base (unit tests, >100 tests): mocks del LLM, pytest, cobertura del 90%+ de la lógica Python; costo: $0, tiempo: <30 segundos; se ejecuta en cada commit y cada PR
- Segunda capa (tests de integración, 20-100 tests): LLM real de bajo costo, dataset curado, validación de propiedades y schema; costo: $0.01-$1 por run; se ejecuta en PRs que modifican prompts, modelos o pipeline
- Tercera capa (evaluación de calidad, 50-500 casos): RAGAS, DeepEval o LLM-as-judge, métricas de faithfulness/relevancy/coherence; costo: $1-$10 por run; se ejecuta en PRs relevantes y como scheduled job diario
- Cúspide (evaluación humana, 20-50 casos): anotadores humanos con rúbrica explícita, comparaciones A/B, inter-annotator agreement; costo: horas de trabajo humano; se ejecuta mensualmente o antes de releases mayores
- Feedback loop: las respuestas evaluadas negativamente por usuarios en producción (thumbs down, reportes) se añaden al dataset de evaluación para que future regresiones similares sean detectadas automáticamente

*"Testing leads to failure, and failure leads to understanding."* — Burt Rutan. En AI Engineering, las respuestas incorrectas del sistema que se capturan como casos de test son el activo más valioso para construir un sistema que mejora continuamente.
