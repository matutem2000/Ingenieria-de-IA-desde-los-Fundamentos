# Módulo 7 – Capítulo 01 – Sección 03

# Taxonomía de agentes: simples, reactivos, deliberativos y multi-agente

La clasificación de agentes en la literatura de IA —codificada originalmente por Russell y Norvig en "Artificial Intelligence: A Modern Approach"— distingue tipos arquitectónicos que corresponden a capacidades operativas concretas en sistemas basados en LLMs. Los agentes simples o de reflejo (simple reflex agents) mapean directamente percepción a acción sin estado interno; los agentes reactivos mantienen un modelo del estado del mundo pero actúan sin planificación anticipada; los agentes deliberativos construyen un plan antes de actuar, evaluando múltiples cursos de acción posibles mediante cadenas de razonamiento como Chain-of-Thought o Tree of Thoughts. Los sistemas multi-agente extienden esta taxonomía al coordinar múltiples instancias especializadas con roles distintos, patrón implementado en frameworks como AutoGen y CrewAI. Elegir el tipo correcto de agente para cada caso de uso impacta directamente en la latencia, el costo por tarea y la confiabilidad del sistema.

## Conceptos clave

- **Agente de reflejo simple**: mapea directamente input → output sin historial ni planificación; útil para clasificaciones y ruteo rápido donde la latencia es crítica (p.ej. clasificador de intenciones en <50ms)
- **Agente reactivo con estado**: mantiene un modelo del entorno (scratchpad o AgentState) y actúa en base a él sin lookahead; adecuado para tareas secuenciales predecibles
- **Agente deliberativo**: genera un plan explícito antes de actuar usando técnicas como ReAct, MRKL o planificación jerárquica; necesario para tareas que requieren estrategia multi-paso
- **Agente BDI (Beliefs-Desires-Intentions)**: arquitectura formal donde el agente mantiene un conjunto de creencias sobre el mundo, deseos (objetivos) e intenciones (planes comprometidos); base de sistemas como JADE
- **Sistema multi-agente**: múltiples agentes con roles especializados que se comunican mediante mensajes estructurados, handoffs o pizarra compartida; amplifica capacidad pero añade complejidad de coordinación

## Principio rector

La complejidad del agente debe ser proporcional a la complejidad de la tarea: elegir un agente deliberativo para clasificaciones simples desperdicia tokens y latencia, mientras que un agente de reflejo falla ante tareas que requieren planificación.
