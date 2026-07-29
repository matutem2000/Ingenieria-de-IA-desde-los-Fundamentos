# Módulo 11 – Capítulo 10 – Sección 05

# De piloto a producción enterprise: checklist técnico de madurez antes de escalar

El checklist de madurez técnica antes de escalar un sistema de IA de piloto a producción enterprise es el contrato técnico que el equipo de AI Engineering establece consigo mismo y con los stakeholders de negocio: cada item del checklist representa un control técnico que, si está ausente, introduce un riesgo específico y cuantificable cuando el sistema opera a escala con usuarios reales y datos de negocio reales. El checklist se organiza en seis dominios que corresponden a los pilares técnicos de los sistemas de IA enterprise: infraestructura y despliegue (el sistema puede desplegarse y revertirse de manera reproducible y controlada), evaluación y calidad (existe una manera objetiva de saber si el sistema está funcionando correctamente), seguridad y cumplimiento (el sistema cumple con los requisitos de acceso, cifrado, y normativa aplicables), observabilidad (el equipo puede diagnosticar problemas de producción en menos de 30 minutos), gestión de costos (el costo de operar el sistema en producción a escala es predecible y sostenible), y operaciones (existe documentación y procesos para que el sistema pueda operarse de manera sostenida sin depender de las personas que lo construyeron). Un item del checklist no se marca como completo hasta que existe evidencia verificable de su implementación: no "planeamos implementar logging", sino "el sistema produce logs estructurados en formato JSON con correlation IDs, verificado en staging con una petición de prueba en la fecha X".

## Checklist técnico de madurez por dominio

- Infraestructura y despliegue: Docker image versionada en registry, pipeline de CI/CD con tests como gate, entorno de staging con datos de prueba, plan de rollback probado en menos de 15 minutos, Infrastructure as Code en Git
- Evaluación y calidad: golden dataset con mínimo 100 casos curados, evaluación automática en el pipeline de CI/CD, métricas de calidad baseline documentadas, threshold de alerta configurado, proceso de actualización del golden set definido
- Seguridad y cumplimiento: autenticación y autorización implementadas, datos sensibles cifrados en reposo y en tránsito, secrets en KMS (no en código ni en variables de entorno en texto plano), audit logging activo, clasificación de datos del sistema documentada
- Observabilidad: traces de LLM en Langfuse o LangSmith, métricas de latencia y error rate en Grafana, alertas configuradas para anomalías de calidad y disponibilidad, runbook de respuesta a incidentes documentado
- Gestión de costos: costo por petición calculado en staging, proyección de costo mensual a escala enterprise aprobada por el budget owner, cost allocation por tenant o equipo configurado, alertas de gasto configuradas
- Operaciones: documentación de arquitectura actualizada, onboarding guide para nuevos miembros del equipo, proceso de on-call definido con responsables identificados, SLOs formalmente definidos y acordados con los usuarios

## Para recordar

Ningún sistema de IA debe declararse listo para producción enterprise hasta que el checklist está completo con evidencia — los items sin evidencia son riesgos abiertos, no "pendientes menores", y en producción enterprise los riesgos abiertos se materializan en incidentes.
