# Módulo 7 – Capítulo 05 – Sección 05

# Criterios de selección de framework: complejidad, control y observabilidad

La selección del framework de agentes para un proyecto no debe basarse en popularidad o en el número de estrellas en GitHub, sino en la alineación entre las características del framework y los requisitos específicos del sistema agéntico a construir. Los tres ejes de evaluación más importantes son: complejidad del flujo de control requerido (¿el agente necesita ciclos, paralelismo, subgrafos o es un flujo lineal simple?), nivel de control y determinismo necesario (¿el comportamiento del agente debe ser reproducible y auditable o puede ser más flexible?) y capacidades de observabilidad del framework (¿qué trazas, métricas y logs expone nativamente?). Un error común es comenzar con el framework más poderoso disponible (LangGraph) para un caso de uso que sería más adecuado para Pydantic AI o incluso para function calling directo de la API sin framework; el overhead de abstracción reduce la velocidad de desarrollo y complica el debugging cuando el framework no es necesario.

## Conceptos clave

- **LangGraph**: elegir cuando el flujo de control es complejo (ciclos, paralelismo, subgrafos), cuando se requiere human-in-the-loop con checkpointing, o cuando la trazabilidad de cada transición de estado es crítica para auditoría; curva de aprendizaje alta
- **AutoGen**: elegir cuando el patrón central es generación-ejecución iterativa de código Python, cuando se necesita orchestración de múltiples LLMs conversando entre sí, o cuando la flexibilidad de la conversación entre agentes es más importante que el control del flujo
- **CrewAI**: elegir cuando la velocidad de desarrollo es la prioridad, el flujo es secuencial o jerárquico con roles bien definidos, y el equipo no tiene experiencia profunda en frameworks agénticos; API más simple a costa de menor control
- **Pydantic AI**: elegir cuando la validación de tipos de entrada/salida es crítica para la integridad del sistema, el equipo tiene experiencia en tipado estático Python, o se integra con código que consume la salida del agente directamente como objetos tipados
- **Sin framework (API directo)**: la opción más olvidada pero frecuentemente la correcta: para agentes simples con 1-3 herramientas y flujo lineal sin ciclos, usar function calling directo de la API del proveedor produce código más simple, más rápido y más fácil de mantener que cualquier framework

## Para recordar

El mejor framework de agentes para un proyecto es el mínimo necesario para resolver el problema: empezar con la API directa del proveedor y agregar el framework solo cuando el caso de uso supera las capacidades del approach más simple.
