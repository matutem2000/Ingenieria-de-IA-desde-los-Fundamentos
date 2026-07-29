# Módulo 7 – Capítulo 09 – Sección 06

# Cierre: un agente en producción es un servicio con requisitos operativos propios

El capítulo sobre despliegue establece que llevar un agente de un prototipo funcional a un sistema de producción confiable requiere el mismo rigor operativo que cualquier servicio de software crítico: SLOs de latencia y disponibilidad, mecanismos de checkpointing y recuperación ante fallos, observabilidad completa de cada paso de ejecución, escalabilidad horizontal para manejar variaciones de carga, y procedimientos de respuesta ante incidentes. La diferencia entre un agente de producción y un demo es precisamente la infraestructura que rodea al agente: el código del agente en sí puede ser idéntico, pero sin colas de trabajo, checkpointing, timeouts explícitos, observabilidad de trazas y auto-scaling, el comportamiento del sistema bajo carga real o ante fallos imprevistos será impredecible y no recuperable. Tratar el despliegue del agente como una afterthought —"primero lo hacemos funcionar, luego vemos la infraestructura"— es la causa más común de fallos de producción en sistemas agénticos.

## Para recordar

Un agente que funciona en el laptop del desarrollador pero no en producción no es un agente; es un prototipo. La diferencia la pone la infraestructura de despliegue, no el código del agente.

*"The ability to deploy software reliably, at any time, is fundamental to building products that people trust."* — Jez Humble y David Farley, "Continuous Delivery" (2010); en sistemas agénticos, "software" incluye el LLM, los prompts, las herramientas y el grafo de estado — cualquiera de los cuales puede cambiar en un deployment y debe poder desplegarse y revertirse con el mismo rigor que cualquier cambio de código.
