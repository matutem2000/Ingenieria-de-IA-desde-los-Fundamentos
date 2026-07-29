# Módulo 4 – Capítulo 04 – Sección 06

## Resumen

Este capítulo desarrolló las arquitecturas de agentes como sistemas con diseño interno propio: componentes específicos con responsabilidades bien definidas, patrones de ejecución que estructuran el razonamiento, y criterios claros de aplicabilidad que distinguen los casos de uso donde los agentes producen valor de los casos donde añaden complejidad innecesaria.

Un agente productivo no es un LLM con acceso a herramientas. Es un sistema compuesto por un modelo de razonamiento, una arquitectura de memoria en dos niveles (episódica y semántica), un registro de herramientas con descripciones precisas, y un bucle de observación-acción con controles explícitos de timeout, límite de iteraciones y política de fallos. Cada uno de esos componentes requiere decisiones de diseño específicas que determinan la calidad, el costo y la seguridad del sistema resultante.

La gestión del estado es la dimensión más frecuentemente subestimada en los proyectos de agentes. Un agente sin gestión robusta de estado es impredecible en tareas que se extienden en el tiempo, incapaz de reanudar trabajo interrumpido, y potencialmente peligroso si mezcla contexto de diferentes usuarios o sesiones. El diseño explícito de las tres capas de estado — sesión, entidad y memoria semántica — con sus políticas de persistencia, retención y control de acceso, es un requisito de arquitectura, no un detalle de implementación.

Los patrones de diseño — ReAct para tareas exploratorias, Planner-Executor para tareas estructuradas paralelizables, Supervisor-Workers para tareas con componentes independientes, Reflection para tareas con alta exigencia de calidad — no son mutuamente excluyentes. Los sistemas de producción frecuentemente combinan patrones: un supervisor que planifica y delega a workers que usan ReAct para sus subtareas, o un ejecutor que aplica reflection sobre el output de cada paso antes de continuar.

Los casos de uso más productivos para agentes empresariales — investigación y análisis, soporte técnico, asistencia al desarrollo, procesamiento documental, gestión de workflows complejos — comparten una característica: el valor de la automatización supera con claridad el costo y la complejidad del agente. Donde esa condición no se cumple, un pipeline determinístico o un sistema RAG simple es la elección correcta.

El Capítulo 05 extiende estos conceptos al siguiente nivel de complejidad: los sistemas donde múltiples agentes colaboran entre sí. La frontera entre el agente individual de este capítulo y los sistemas multiagente del siguiente es precisa: un agente individual coordina herramientas. Un sistema multiagente coordina agentes. Esa distinción determina los patrones de coordinación, los protocolos de comunicación y los riesgos de gobierno que exploraremos a continuación.

---

*"El verdadero valor de los agentes no reside únicamente en el modelo de lenguaje, sino en la capacidad de integrar razonamiento, herramientas y procesos para resolver problemas reales."*
— Principio de diseño de sistemas agénticos
