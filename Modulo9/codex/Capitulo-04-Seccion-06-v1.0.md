# Módulo 9 – Capítulo 04 – Sección 06

# Cierre: el red teaming es el único método que descubre vulnerabilidades antes que los atacantes

La diferencia entre un sistema de IA que fue atacado en producción y uno que no lo fue frecuentemente no es la ausencia de vulnerabilidades, sino la ausencia de un adversario que las buscó. El red teaming cierra esa brecha: pone a un equipo en el rol del adversario antes de que el adversario real llegue al sistema. Lo que hace al red teaming de IA especialmente valioso —y diferente del pentesting tradicional— es que no busca vulnerabilidades en el código sino en el comportamiento del modelo, que es fundamentalmente no determinista y no puede verificarse completamente mediante análisis estático. Los hallazgos de red teaming no solo mejoran la seguridad del sistema actual: acumulan en una base de conocimiento de técnicas de ataque que informa el diseño de futuros sistemas, el entrenamiento de nuevos modelos, y la construcción de guardrails más efectivos. La madurez de un equipo de AI Engineering se mide, entre otras métricas, por la sistematicidad con la que integra red teaming en su ciclo de desarrollo.

*"Only an attacker who has actually tried to break a system can know how robust it really is."* — Ross Anderson, profesor de seguridad de la Universidad de Cambridge y autor de "Security Engineering", sobre el principio fundamental que hace al red teaming insustituible.

## Conceptos clave del capítulo

- Red teaming de IA: evaluación adversarial estructurada que busca vulnerabilidades desde la perspectiva del atacante, no la del desarrollador; cubre seguridad, safety, privacidad y alineación
- Metodología: scoping del threat model + harm taxonomy + ejecución con criterios de éxito claros + reporte con hallazgos reproducibles + seguimiento de mitigaciones con SLA por severidad
- Red teaming manual: expertos interdisciplinarios (seguridad, psicología, dominio) para vulnerabilidades que requieren creatividad, conocimiento cultural y adaptabilidad en tiempo real
- Red teaming automatizado: PyRIT (Microsoft) para orquestación multi-turn, Garak (NVIDIA) para cobertura de probes conocidas, PAIR/TAP para generación iterativa con LLM-as-Attacker
- Integración en SDLC: red teaming ligero en CI/CD (Garak) + ejercicio completo pre-release + red teaming periódico en producción, activado por cambios de modelo, system prompt o herramientas

## Idea central

Un sistema de IA que no fue sometido a red teaming no sabe cuáles son sus vulnerabilidades: simplemente no ha tenido la suerte de encontrar a alguien que las buscara activamente, y en producción la suerte eventualmente se acaba.
