# Módulo 11 – Capítulo 10 – Sección 04

# Gestión de deuda técnica en proyectos de IA: identificar y planificar la reducción gradual

La deuda técnica en proyectos de IA enterprise tiene características específicas que la hacen más costosa que la deuda técnica convencional: los prompts hardcodeados en el código fuente se vuelven críticos el día que necesitan actualizarse en producción sin despliegue de código; los notebooks usados como código de producción se vuelven inmanejables el día que hay que debuggear un problema en producción a las 2 de la madrugada; los pipelines de datos manuales se vuelven insostenibles el día que el volumen de documentos que alimentan el RAG se multiplica por 10. La deuda técnica de IA se clasifica en cuatro categorías con diferente urgencia de remediación: deuda de infraestructura (notebooks en producción, despliegues manuales, ausencia de CI/CD), deuda de datos (pipelines sin validación de calidad, sin versionado de datasets, sin linaje de datos), deuda de evaluación (ausencia de golden sets, evaluación solo manual, ausencia de métricas de producción), y deuda de observabilidad (logs no estructurados, ausencia de traces de LLM, monitoreo reactivo solo via alertas de usuarios). La estrategia de reducción gradual de deuda técnica de IA debe integrarse en el proceso de desarrollo normal como un porcentaje fijo del tiempo del equipo (típicamente 20-25% del sprint dedicado a deuda técnica, según el principio de "pagar la hipoteca mensualmente" en lugar de acumular hasta la crisis), con items de deuda técnica en el backlog junto con las features de negocio y priorizados por su impacto en la capacidad futura del equipo.

## Tipos de deuda técnica específica de IA y su remediación

- Deuda de evaluación (urgencia alta): construir el golden dataset con 100 casos curados es la primera prioridad de deuda técnica — sin él, el equipo opera sin capacidad de detectar regresiones, y cada cambio de prompt o modelo es un riesgo no cuantificado
- Deuda de prompts hardcodeados: migrar prompts del código fuente a un prompt registry versionado, con tests de regresión contra el golden set — inversión de 2-4 semanas que elimina el riesgo de cambios de prompts sin proceso de revisión
- Deuda de notebooks en producción: containerizar el código de inferencia con Docker y añadir un endpoint FastAPI o gRPC, migrando el notebook a un módulo Python estructurado con tests unitarios — inversión de 1-3 semanas por servicio
- Deuda de pipelines de datos manuales: automatizar los pipelines de ingesta y actualización del índice RAG con Airflow o Prefect, añadiendo validaciones de calidad con Great Expectations — inversión de 3-6 semanas para pipelines de complejidad media
- Deuda de observabilidad: instrumentar el servicio de orquestación con OpenTelemetry y desplegar Langfuse o LangSmith para traces de LLM — inversión de 1-2 semanas que produce visibilidad inmediata sobre el comportamiento del sistema en producción

## Buena práctica

Mantener un registro visible de la deuda técnica de IA (en Jira, Linear, o GitHub Issues) con estimación de costo de no remediación (el tiempo que costaría manejar un incidente sin el control técnico faltante) hace que la priorización sea objetiva en lugar de subjetiva.
