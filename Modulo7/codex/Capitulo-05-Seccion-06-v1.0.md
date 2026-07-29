# Módulo 7 – Capítulo 05 – Sección 06

# Cierre: el framework no define la inteligencia del agente — solo su estructura

El capítulo sobre frameworks de agentes deja una conclusión clara: LangGraph, AutoGen, CrewAI y Pydantic AI son herramientas de ingeniería de software, no de inteligencia artificial. Determinan cómo se organiza el flujo de control, cómo se comunican los componentes y qué garantías de tipo y persistencia se proveen; pero no determinan la calidad del razonamiento del agente, la precisión de sus herramientas o la relevancia de sus memorias. Un agente construido con LangGraph pero con prompts deficientes, herramientas mal descritas y sin gestión de memoria producirá peores resultados que un agente simple construido con function calling directo pero con prompts cuidadosamente diseñados y herramientas bien documentadas. La elección del framework debe ser la última decisión de diseño, no la primera: primero definir el comportamiento requerido del agente, luego los componentes necesarios para implementarlo, y finalmente el framework que organiza mejor esos componentes dadas las capacidades del equipo y los requisitos operativos del sistema.

## Para recordar

El framework es el andamiaje; la inteligencia del agente está en el LLM, los prompts, las herramientas y la memoria —componentes que funcionan bien o mal independientemente del framework que los organiza.

*"A fool with a tool is still a fool."* — Grady Booch, pionero de la ingeniería de software orientada a objetos; en el contexto agéntico, ningún framework compensa prompts ambiguos, herramientas mal descritas o ausencia de estrategia de memoria en un sistema de agentes en producción.
