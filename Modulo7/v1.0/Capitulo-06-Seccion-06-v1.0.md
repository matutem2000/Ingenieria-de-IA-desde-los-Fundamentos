# Módulo 7 – Capítulo 06 – Sección 06

## Cierre: los sistemas multiagente amplifican tanto la capacidad como la complejidad

El capítulo sobre sistemas multiagente establece que la arquitectura multiagente es una decisión de ingeniería con consecuencias dobles: amplifica la capacidad del sistema para manejar tareas complejas mediante especialización y paralelismo, pero también amplifica la complejidad operativa, los puntos de fallo potenciales, el costo de tokens, y la dificultad de debugging. Un sistema de 5 agentes no es 5 veces más poderoso que un agente individual; es potencialmente más poderoso en el dominio del problema que resuelve, pero también significativamente más complejo en términos de observabilidad, testing, gestión de estado compartido, y reconciliación de resultados contradictorios.

Las tres motivaciones legítimas para adoptar la arquitectura multiagente —especialización de dominio, paralelismo de subtareas, reducción del contexto por agente— deben estar presentes como limitaciones concretas y medibles del agente individual antes de justificar el overhead de un sistema multiagente. Un equipo que adopta multiagente porque "suena más sofisticado" o porque "el agente único ya es complejo" está añadiendo complejidad sin beneficio proporcional: los mismos problemas que hacen complejo al agente individual se vuelven más difíciles de diagnosticar en un sistema de múltiples agentes donde los errores pueden originarse en cualquier nodo del grafo de coordinación.

La inversión que debe acompañar la adopción del multiagente es proporcional a su complejidad. Un sistema de 5 agentes requiere: testing de integración entre los agentes (no solo unit tests de cada agente individualmente), observabilidad que capture la traza completa de una tarea a través de todos los agentes (LangSmith o Langfuse con trazas anidadas), políticas de manejo de inconsistencias entre agentes, y procedimientos de respuesta a incidentes que identifiquen en qué agente específico se originó un fallo. Sin estas inversiones, el sistema multiagente produce un tipo de complejidad operativa que es más difícil de manejar que la complejidad de un agente único bien diseñado.

El capítulo siguiente —sobre testing de agentes— aplica estas consideraciones a la pregunta de cómo verificar que el comportamiento de estos sistemas, sean de un agente único o multiagente, cumple los criterios de calidad antes de desplegarse en producción. El testing de agentes es el puente entre el diseño y el despliegue seguro.

## Para recordar

El multiagente es la solución correcta cuando las limitaciones del agente individual son el cuello de botella medible de un sistema. Es la complejidad incorrecta cuando se adopta como aspiración arquitectónica antes de que esas limitaciones sean evidentes y cuantificadas. Medir primero, escalar después.

*"Simplicity is the ultimate sophistication."* — atribuido a Leonardo da Vinci; en el contexto de sistemas multiagente, la arquitectura más simple que resuelve el problema es siempre preferible a la más sofisticada que también lo resuelve. Cada agente adicional en un sistema debe justificarse con un beneficio medible que supere su costo en complejidad operativa.
