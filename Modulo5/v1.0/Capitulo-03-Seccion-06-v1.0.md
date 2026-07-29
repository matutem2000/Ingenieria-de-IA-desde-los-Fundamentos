# Módulo 5 – Capítulo 03 – Sección 06

## Cierre: criterios para elegir entre orquestación directa y frameworks

La elección entre frameworks de orquestación e implementación directa no es ideológica sino pragmática, y el equipo que la toma con criterios claros evita dos errores simétricos igualmente costosos: adoptar prematuramente todo el stack posible por aspiración a la sofisticación técnica, o rechazar los frameworks por dogma de "código propio es mejor" cuando la complejidad del flujo justifica la abstracción. Ambos errores tienen el mismo resultado: sistemas más difíciles de mantener de lo necesario, por razones opuestas.

El criterio más útil en la práctica es el "test de la implementación directa": antes de comprometerse con un framework, implementar el flujo completo con el SDK puro del proveedor, incluyendo el manejo de errores, el logging, la gestión del historial y los casos borde que emergen del análisis de requisitos. Si el resultado cabe en menos de 150 líneas de código claro y el equipo puede entenderlo de un vistazo, la implementación directa es preferible y el framework añadiría complejidad sin justificación. Si la implementación directa crece hacia 500 o más líneas con lógica de estado compleja, múltiples fuentes de datos que necesitan indexación, o ciclos de agente con herramientas, el framework está ganando su costo.

La estrategia más sólida en proyectos de IA maduros es la composición cuidadosa de capas: el SDK directamente para las llamadas al LLM simples donde el control granular importa, LlamaIndex solo para la capa de recuperación vectorial cuando el caso de uso es RAG intensivo con múltiples fuentes, LangGraph cuando la lógica del agente necesita ciclos y estado persistente, y DSPy cuando el sistema de evaluación tiene los datasets necesarios para guiar la optimización automática de prompts. Esta composición evita el "todo o nada" de comprometerse con un único framework para toda la aplicación, manteniendo el control donde importa y usando la abstracción donde ahorra trabajo real.

El mantenimiento a largo plazo es el criterio que los análisis de adopción inicial más frecuentemente subestiman. Los frameworks de orquestación tienen velocidad de cambio de API alta: LangChain realizó breaking changes significativos entre v0.1, v0.2 y v0.3, y cada actualización requirió refactorización del código que usaba las interfaces modificadas. Los sistemas construidos sobre implementación directa con el SDK del proveedor no se ven afectados por estos cambios de framework; el proveedor de LLM tiene contratos de estabilidad de API más sólidos que los frameworks de la comunidad open source. Este trade-off —velocidad de desarrollo vs estabilidad a largo plazo— es una dimensión de la decisión que debe incorporarse explícitamente.

## Criterios de decisión sintetizados

- **Complejidad del flujo:** 1-2 pasos lineales favorecen la implementación directa; 3 o más pasos con ramificación, paralelismo o ciclos favorecen un framework con el modelo correcto para ese patrón.
- **Volumen de datos para recuperación:** para RAG sobre más de 10.000 documentos con múltiples fuentes heterogéneas, LlamaIndex elimina semanas de desarrollo de ingesta, chunking e indexación.
- **Velocidad de cambio del flujo:** flujos que evolucionan rápidamente se benefician de la modularidad del framework para cambiar componentes; flujos estables se benefician de la predictibilidad de la implementación directa.
- **Disponibilidad de datos de entrenamiento:** si existen más de 50 ejemplos etiquetados y una función de evaluación definida, DSPy es viable; sin ellos, la implementación manual de prompts es la única opción.
- **Madurez del equipo en el framework específico:** equipos con experiencia previa en LangChain o LlamaIndex obtienen productividad real desde el primer sprint; equipos que aprenden el framework en paralelo con el proyecto pagan un costo de learning curve que puede superar el beneficio durante los primeros meses.

> **Nota del Arquitecto:** La estrategia más efectiva que he visto en equipos productivos es: comenzar con el SDK puro para los primeros sprints de validación del caso de uso, adoptar LlamaIndex cuando el volumen de documentos hace que la indexación manual sea costosa, y adoptar LangGraph cuando la lógica del agente requiere ciclos que el LCEL lineal no puede expresar. Este orden de adopción —guiado por evidencia de necesidad real, no por plan previo— resulta en sistemas que tienen el mínimo de dependencias necesarias y el máximo de control sobre lo que importa.

La elección correcta entre frameworks es la que el equipo puede mantener, que encaja con los requisitos del caso de uso, y que fue evaluada empíricamente antes de comprometerse con ella. Los capítulos siguientes asumen que esta elección ha sido tomada y se centran en las capas de ingeniería que aplican independientemente del framework: los patrones de integración con sistemas existentes, el testing, el CI/CD, la evaluación de calidad y la observabilidad.

---

*"The best tool is the one you know how to use."* — Adaptado de Donald Knuth. En AI Engineering, el framework que el equipo domina y que encaja con los requisitos del caso de uso siempre superará en productividad al framework más popular que el equipo no conoce bien o que resuelve un problema que el proyecto no tiene.
