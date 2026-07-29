# Módulo 7 – Capítulo 05 – Sección 06

## Cierre: el framework no define la inteligencia del agente — solo su estructura

El capítulo sobre frameworks de agentes deja una conclusión que conviene articular con precisión: LangGraph, AutoGen, CrewAI y Pydantic AI son herramientas de ingeniería de software, no de inteligencia artificial. Determinan cómo se organiza el flujo de control, cómo se comunican los componentes, y qué garantías de tipo y persistencia se proveen; pero no determinan la calidad del razonamiento del agente, la precisión de sus herramientas, o la relevancia de su memoria. El framework es el andamiaje; la inteligencia está en el LLM, los prompts, las herramientas y la memoria —componentes que funcionan bien o mal independientemente del framework que los organiza.

Esta distinción tiene consecuencias prácticas directas. Un agente construido con LangGraph pero con prompts deficientes, herramientas mal descritas, y sin gestión de memoria producirá peores resultados que un agente simple construido con function calling directo pero con prompts cuidadosamente diseñados, herramientas bien documentadas y un sistema de memoria apropiado para el caso de uso. La tentación de esperar que el framework resuelva problemas de calidad que son inherentemente problemas de diseño de componentes es una de las causas más frecuentes de proyectos agénticos que no llegan a producción.

La elección del framework, por tanto, debe ser la última decisión de diseño, no la primera. El proceso correcto es: primero, definir con precisión el comportamiento requerido del agente —qué tareas debe completar, con qué criterios de éxito, con qué SLOs de latencia y costo—; luego, identificar los componentes necesarios —qué herramientas, qué tipo de memoria, qué estrategia de razonamiento—; finalmente, elegir el framework que mejor organiza esos componentes dadas las capacidades del equipo y los requisitos operativos del sistema. Este orden de decisiones produce sistemas coherentes donde el framework amplifica las capacidades del equipo en lugar de añadir complejidad sin propósito.

La transición al capítulo siguiente es natural: una vez que el agente tiene sus componentes diseñados y su framework elegido, la siguiente pregunta es cómo verificar que funciona correctamente antes de desplegarlo en producción. El Capítulo 07 sobre testing de agentes aborda exactamente ese desafío, con las particularidades que hacen el testing agéntico fundamentalmente diferente al testing de software convencional.

## Para recordar

El framework es el andamiaje; la inteligencia del agente está en el LLM, los prompts, las herramientas y la memoria —componentes que funcionan bien o mal independientemente del framework que los organiza. Elegir el framework antes de diseñar los componentes produce el orden incorrecto de decisiones.

*"A fool with a tool is still a fool."* — Grady Booch, pionero de la ingeniería de software orientada a objetos; en el contexto agéntico, ningún framework —por sofisticado que sea— compensa prompts ambiguos, herramientas mal descritas, o ausencia de estrategia de memoria en un sistema de agentes en producción.
