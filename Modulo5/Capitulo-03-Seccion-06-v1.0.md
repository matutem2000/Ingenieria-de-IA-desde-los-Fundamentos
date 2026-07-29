# Módulo 5 – Capítulo 03 – Sección 06

# Cierre: criterios para elegir entre orquestación directa y frameworks

La elección entre frameworks de orquestación e implementación directa no es ideológica sino pragmática: los frameworks brillan cuando el problema encaja en sus abstracciones y el equipo domina sus patrones, y estorban cuando imponen sus modelos mentales sobre problemas que tienen soluciones más simples. El criterio más útil en la práctica es el "test de la implementación directa": antes de adoptar un framework, intentar implementar el flujo con el SDK puro del proveedor, estimar cuántas líneas requiere y qué casos borde emergen; si el resultado es manejable (<200 líneas, pocos casos borde), la implementación directa es preferible. Si el flujo involucra RAG sobre múltiples fuentes, agentes con herramientas, memoria persistente y evaluación de calidad, los frameworks ahorran semanas de trabajo al proveer estas abstracciones probadas por la comunidad. La estrategia más sólida en producción es la composición cuidadosa: usar el SDK directamente para las llamadas al LLM, LlamaIndex solo para la capa de recuperación vectorial si el caso de uso es RAG intensivo, y LangGraph o LangChain solo cuando la complejidad de la orquestación justifica su adopción.

## Criterios de decisión sintetizados

- Complejidad del flujo: 1-2 pasos lineales favorecen implementación directa; 3+ pasos con ramificación, paralelismo o ciclos favorecen un framework
- Volumen de datos para recuperación: para RAG sobre >10.000 documentos con múltiples fuentes, LlamaIndex ahorra semanas de desarrollo de la capa de indexación y recuperación
- Velocidad de cambio del flujo: flujos que cambian frecuentemente se benefician de la modularidad del framework; flujos estables se benefician de la simplicidad de la implementación directa
- Observabilidad requerida: LangSmith (LangChain) y LlamaIndex Observability proveen trazas detalladas automáticamente; la implementación directa requiere instrumentación manual equivalente
- Madurez del equipo: equipos con experiencia en el framework específico obtienen productividad real; equipos que aprenden el framework en paralelo con el proyecto pagan un costo de learning curve que puede superar el beneficio

*"The best tool is the one you know how to use."* — Donald Knuth, adaptado al contexto de ingeniería de software. En AI Engineering, el framework que el equipo domina y que encaja con los requisitos del caso de uso siempre superará al framework más popular que el equipo no conoce bien.
