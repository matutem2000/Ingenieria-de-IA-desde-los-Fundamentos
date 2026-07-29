# Módulo 12 – Capítulo 02 – Sección 06

# Cierre: las ADRs son la memoria arquitectónica del sistema — documentan el porqué, no solo el qué

Los cuatro ADRs del proyecto final — elección de modelo, estrategia RAG, diseño agéntico y seguridad — forman la memoria arquitectónica del sistema. Sin ellos, cada nuevo integrante del equipo debe reconstruir el razonamiento detrás de cada decisión técnica preguntando a quienes las tomaron; con ellos, el equipo puede evaluar si las restricciones que motivaron una decisión siguen siendo válidas, y cambiar la decisión cuando han cambiado las circunstancias. En sistemas de IA, los ADRs tienen una dimensión adicional: los modelos fundacionales evolucionan, los precios cambian, los benchmarks se actualizan, y una decisión óptima en enero puede ser subóptima en junio. La práctica de mantener los ADRs como documentos vivos — con estado Superseded cuando son reemplazados — convierte la arquitectura en un artefacto auditable que puede evolucionar con evidencia, no con opiniones.

## Aspectos técnicos que integra este capítulo

- Formato ADR estándar con campos Título, Estado, Contexto, Decisión y Consecuencias aplicado a decisiones de IA
- ADR-001: modelo fundacional con evaluación cuantitativa sobre benchmark de dominio específico
- ADR-002: chunking + embedding + base vectorial con métricas RAGAS y análisis de costo-rendimiento
- ADR-003: framework agéntico con nivel de autonomía limitado y herramientas de solo lectura documentadas
- ADR-004: modelo de amenazas STRIDE con controles seleccionados y riesgos residuales aceptados explícitamente

## Para recordar

Las ADRs son el único mecanismo que convierte decisiones técnicas tácitas en conocimiento explícito y auditable — sin ellas, la arquitectura del sistema existe solo en la memoria de quienes la diseñaron.

*"Architecture represents the significant design decisions that shape a system, where significant is measured by cost of change." — Grady Booch*
