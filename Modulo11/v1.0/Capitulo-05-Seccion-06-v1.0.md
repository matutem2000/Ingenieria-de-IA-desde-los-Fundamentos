# Módulo 11 – Capítulo 05 – Sección 06

## Cierre: LLMOps es MLOps adaptado a la naturaleza no determinista de los modelos de lenguaje

LLMOps no reinventa MLOps sino que lo extiende para acomodar las propiedades únicas de los modelos de lenguaje que invalidan algunas de las suposiciones centrales del MLOps clásico. El no determinismo de las respuestas, la imposibilidad de evaluar la calidad con métricas simples, el costo elevado de inferencia que convierte la optimización en una responsabilidad de primer nivel, la dependencia de proveedores externos que pueden actualizar o deprecar modelos sin previo aviso suficiente, y el prompt como artefacto de ingeniería con su propio ciclo de vida — ninguna de estas propiedades tiene un equivalente directo en el MLOps de modelos supervisados clásicos.

Los componentes de LLMOps cubiertos en este capítulo — la evaluación continua con LLM-as-a-judge y golden datasets, el prompt registry versionado con canary deployments, el A/B testing con asignación consistente por sesión y análisis estadístico apropiado, y las estrategias de rollback con blue-green deployments y feature flags — constituyen la infraestructura mínima para operar sistemas de LLM en producción enterprise con confianza. No son opcionales: un equipo que opera sin esta infraestructura puede funcionar adecuadamente durante los primeros meses gracias a la calidad del modelo subyacente, pero cuando el proveedor actualiza el modelo, cuando el caso de uso evoluciona, o cuando el volumen de usuarios aumenta sustancialmente, la ausencia de LLMOps se convierte en la causa principal de incidentes de calidad que dañan la reputación del sistema y la confianza de los stakeholders internos.

La inversión en LLMOps también es la que habilita la mejora continua del sistema: sin evaluación automatizada, no hay manera de medir el impacto de cada cambio; sin A/B testing, las mejoras se deciden por intuición en lugar de por evidencia; sin prompt registry, los cambios de prompts no tienen historia; sin rollback planificado, cada mejora es un riesgo. La infraestructura de LLMOps transforma el ciclo de mejora del sistema de IA de un proceso episódico y arriesgado en un proceso continuo y controlado.

El siguiente capítulo aplica los principios de LLMOps al caso de uso más frecuente en enterprise: los sistemas de RAG que conectan los LLMs con el conocimiento corporativo. La evaluación de sistemas RAG introduce métricas específicas del dominio (faithfulness, context precision, answer relevancy), y el ciclo de vida del knowledge management añade una dimensión de frescura del índice vectorial que no existe en los sistemas de LLM sin recuperación.

---

*"La diferencia entre investigación y producción en machine learning es que en investigación se maximiza el rendimiento del modelo, mientras que en producción se maximiza la confiabilidad del sistema que lo rodea."* — Chip Huyen, autora de "Designing Machine Learning Systems" y "AI Engineering"
