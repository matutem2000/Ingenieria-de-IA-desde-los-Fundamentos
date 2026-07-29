# Módulo 4 – Capítulo 07 – Sección 06

## Resumen

Este capítulo desarrolló la seguridad en sistemas de IA como una disciplina que extiende la ciberseguridad convencional con controles específicos para las amenazas que los modelos de lenguaje y las arquitecturas de IA introducen. Los sistemas de IA no solo pueden ser atacados a través de sus componentes de infraestructura — como cualquier sistema de software — sino también a través de su propio mecanismo de razonamiento: manipulando el prompt, contaminando el contexto que el modelo procesa, o explotando la capacidad del modelo para seguir instrucciones embebidas en el contenido que recupera.

El OWASP LLM Top 10 es el marco de referencia más completo para evaluar el perfil de amenazas de un sistema de IA basado en modelos de lenguaje. La protección de prompts — contra injection directa e indirecta, exfiltración y manipulación de comportamiento — requiere una combinación de diseño defensivo del prompt, validación de input en la capa de aplicación, herramientas de guardrails (Guardrails AI, NVIDIA NeMo Guardrails, Azure AI Content Safety) y monitoreo continuo del output.

La seguridad de datos en sistemas de IA combina los controles estándar — cifrado en reposo y en tránsito, control de acceso, auditoría — con consideraciones específicas: la clasificación de datos antes de la indexación para habilitar el control de acceso a nivel de vector, la gestión de datos personales en sistemas RAG bajo GDPR y CCPA, y la detección de patrones de exfiltración sistemática. La distribución entre capas de control técnico (a nivel de la base vectorial y las herramientas) versus instrucciones al modelo (en el prompt de sistema) es una decisión arquitectónica crítica: los controles técnicos son más robustos porque no pueden ser evadidos por un prompt diseñado con habilidad.

El control de acceso debe extenderse a todas las superficies del sistema — API de LLM, base vectorial, herramientas de agentes, sistema de administración — con gestión centralizada de identidades, principio de mínimo privilegio en cada componente, y propagación controlada de la identidad del usuario a través del sistema completo.

El cumplimiento de seguridad distingue entre el cumplimiento técnico de las obligaciones de protección de datos — tratado en este capítulo — y el cumplimiento regulatorio organizacional más amplio — que el Capítulo 09 desarrolla en el contexto del gobierno de plataformas de IA. El arquitecto debe diseñar para ambos niveles desde el inicio, porque retrofitar controles de seguridad después del despliegue es significativamente más costoso que incorporarlos en el diseño.

El Capítulo 08 aborda la tercera disciplina operativa: la escalabilidad. Un sistema seguro y observable que no puede crecer con la demanda producirá una experiencia degradada precisamente en los momentos de mayor valor para el negocio. La escalabilidad bien diseñada es la que permite que el sistema crezca de manera controlada, sostenible y económicamente viable.

---

*"Incorporar seguridad desde la arquitectura resulta considerablemente menos costoso que corregir vulnerabilidades una vez que el sistema está en producción."*
— Principio de Security by Design aplicado a sistemas de IA
