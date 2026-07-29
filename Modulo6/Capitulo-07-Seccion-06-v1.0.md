# Módulo 6 – Capítulo 07 – Sección 06

# Cierre: operar RAG en producción requiere ingeniería de plataforma, no solo código

La distancia entre un prototipo de RAG que funciona en un notebook y un sistema RAG que opera en producción con SLOs de disponibilidad del 99.5%, latencia p99 <1 segundo y Recall@5 >0.80 es exactamente la distancia entre escribir código y construir un sistema de software. Los componentes de plataforma que separan ambos mundos son los mismos que en cualquier sistema distribuido crítico: observabilidad completa con tracing y alertas, pipelines de CI/CD que incluyen gates de calidad sobre el golden dataset, gestión de versiones del índice y del modelo, estrategias de escalado horizontal bajo carga, runbooks de recuperación ante fallos y ownership claro de cada componente. Los equipos que subestiman la complejidad operacional del RAG de producción tipicamente enfrentan los mismos problemas recurrentes: degradación silenciosa del índice sin detección, costos de API de embedding descontrolados, downtime durante actualizaciones del modelo de embedding, y ausencia de mecanismos de rollback cuando una actualización del pipeline produce regresiones. La ingeniería de plataforma para RAG no es un lujo para sistemas grandes sino un prerequisito para cualquier sistema que un usuario real depende para tomar decisiones; sin ella, el sistema tiene calidad impredecible y confiabilidad desconocida.

*"Operar un sistema de software en producción es diferente en especie, no en grado, de construirlo. Requiere disciplinas de ingeniería distintas: observabilidad, respuesta a incidentes, planificación de capacidad, y una cultura de fiabilidad."* — Niall Murphy y Betsy Beyer, Site Reliability Engineering (Google, O'Reilly)

## Principio rector

Tratar el sistema RAG de producción con los mismos estándares operacionales que cualquier servicio crítico: SLOs definidos, monitoring con alertas, runbooks de incidentes, planificación de capacidad y proceso de deployment con validación automática de calidad antes de cada release.
