# Módulo 7 – Capítulo 06 – Sección 06

# Cierre: los sistemas multiagente amplifican tanto la capacidad como la complejidad

El capítulo sobre sistemas multiagente establece que la arquitectura multiagente es una decisión de ingeniería con consecuencias dobles: amplifica la capacidad del sistema para manejar tareas complejas mediante especialización y paralelismo, pero también amplifica la complejidad operativa, los puntos de fallo potenciales, el costo de tokens y la dificultad de debugging. Un sistema de 5 agentes no es 5 veces más poderoso que un agente individual; es potencialmente más poderoso en el dominio del problema que resuelve, pero también 5 veces más complejo en términos de observabilidad, testing, gestión de estado compartido y reconciliación de resultados. La decisión de pasar de un agente individual a un sistema multiagente debe estar motivada por limitaciones concretas —no por la aspiración de mayor sofisticación— y debe ir acompañada de inversiones proporcionales en infraestructura de observabilidad, testing de integración y políticas de manejo de inconsistencias.

## Para recordar

El multiagente es la solución correcta cuando las limitaciones del agente individual son el cuello de botella medible de un sistema; es la complejidad incorrecta cuando se adopta como aspiración arquitectónica antes de que esas limitaciones sean evidentes.

*"Simplicity is the ultimate sophistication. The architecture of a system should be as simple as possible, and no simpler."* — paráfrasis de Leonardo da Vinci y Albert Einstein aplicada a la arquitectura de sistemas multiagente: cada agente adicional en un sistema debe justificarse con un beneficio medible que supere su costo en complejidad.
