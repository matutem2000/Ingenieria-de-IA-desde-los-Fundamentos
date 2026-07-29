# Módulo 9 – Capítulo 10 – Sección 06

# Cierre: un sistema de IA seguro no es el que nunca es atacado, sino el que sobrevive al ataque

El objetivo de AI Security Engineering no es construir un sistema impenetrable — esa meta es inalcanzable — sino construir un sistema que sea suficientemente costoso de atacar para disuadir a la mayoría de los adversarios, suficientemente resiliente para continuar operando cuando es atacado, y suficientemente observable para detectar, contener y aprender de los ataques que ocurren. Un sistema diseñado con security by design desde la arquitectura, con mínimo privilegio aplicado a cada componente, con defensa en profundidad en cuatro capas independientes, con threat modeling continuo que evoluciona con las capacidades del sistema, y con un pipeline de security testing que verifica continuamente los controles, es un sistema que "sobrevive al ataque": puede ser comprometido parcialmente pero contiene el blast radius, detecta el compromiso rápidamente, lo mitiga con controles de segunda línea, y aprende del incidente para mejorar. La seguridad en IA no es un estado que se alcanza sino un proceso continuo de mejora ante adversarios que también mejoran continuamente.

*"The question is not whether you will be attacked, but whether you will notice and respond appropriately when you are."* — Adam Shostack, experto en threat modeling y autor de "Threat Modeling: Designing for Security" (Microsoft Press), sobre el paradigma de resiliencia que debe guiar el diseño de sistemas seguros en la era moderna.

## Conceptos clave del capítulo

- Security by design: las decisiones arquitectónicas de trust zones, sandboxing, cifrado y separación de privilegios deben tomarse antes de escribir código, no después del primer incidente; GDPR Art. 25 y EU AI Act Art. 9 lo formalizan como requisito legal
- Mínimo privilegio: el modelo solo recibe el contexto mínimo necesario; el agente solo tiene acceso a las herramientas necesarias; cada herramienta tiene el IAM role más restrictivo posible; privilege elevation temporal con logging para operaciones excepcionales
- Defense in depth: capa de prompt + capa de API (LlamaGuard, rate limiting) + capa de red (WAF + TLS) + capa de datos (cifrado + RBAC + logs inmutables) — cuatro capas independientes donde el fallo de una no compromete el sistema
- Threat modeling continuo: actualización obligatoria ante cada nueva capacidad, nueva herramienta o cambio de modelo base; mantenido como código en git con versioning explícito; validado mediante red teaming enfocado en las nuevas amenazas identificadas
- Security testing pipeline: SAST (Semgrep/Bandit) + DAST (ZAP/Burp) + fuzzing de prompts + evaluación de clasificadores + red teaming automatizado (Garak) integrados en CI/CD con gates de calidad que bloquean deploys con hallazgos críticos

## Idea central

Un sistema de IA con diseño seguro por construcción —mínimo privilegio, defensa en profundidad, threat modeling continuo y testing automatizado— no es uno que nunca es atacado: es uno que cuando es atacado, contiene el daño, lo detecta rápidamente, lo mitiga con las capas de control restantes, y sale más resistente del incidente.
