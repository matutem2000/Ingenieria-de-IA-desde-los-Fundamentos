# Módulo 7 – Capítulo 07 – Sección 06

# Cierre: testear agentes requiere pensar en comportamiento, no solo en salidas

El capítulo sobre testing de agentes establece que la transición del testing tradicional al testing agéntico es fundamentalmente un cambio de perspectiva: de "¿produce el output correcto?" a "¿se comporta correctamente dado el contexto?". Esta distinción es crucial porque un agente puede producir el output correcto de múltiples maneras —algunas correctas, otras frágiles y coincidentes— y solo el análisis de la trayectoria completa puede distinguirlas. La suite de tests de un agente en producción debe cubrir cuatro niveles: unit tests de herramientas individuales (deterministas, rápidos, sin LLM), tests de selección de herramientas (el agente elige la herramienta correcta), tests de completitud de tareas (el agente logra el objetivo) y pruebas de estrés (el agente se comporta adecuadamente ante adversidad). Esta suite debe ejecutarse en el pipeline de CI/CD ante cualquier cambio en el agente, el prompt, las herramientas o el modelo base; los cambios de modelo (p.ej. upgrade de GPT-4o a GPT-4o-mini) deben tratarse como cambios de código que requieren validación completa.

## Para recordar

El testing de agentes no es un lujo de proyectos con recursos abundantes; es la única forma de saber si un cambio en el prompt, las herramientas o el modelo base mejoró o degradó el comportamiento del sistema.

*"Testing shows the presence, not the absence of bugs."* — Edsger W. Dijkstra; en sistemas agénticos, esta afirmación tiene especial peso: dado el no-determinismo y el espacio exponencial de trayectorias posibles, los tests no pueden garantizar ausencia de fallos, pero sí garantizan que los fallos más conocidos y críticos no están presentes.
