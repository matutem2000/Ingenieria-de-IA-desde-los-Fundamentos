# Módulo 12 – Capítulo 10 – Sección 01

# Rúbrica del proyecto final: criterios técnicos de evaluación por componente

La rúbrica del proyecto final evalúa el sistema integrador en seis dimensiones técnicas con criterios cuantitativos y cualitativos verificables. Cada dimensión se evalúa en tres niveles: Completo (cumple todos los criterios), Parcial (cumple los criterios mínimos con deficiencias documentadas) y Incompleto (no cumple los criterios mínimos). La dimensión de pipeline RAG evalúa: RAGAS faithfulness >= 0.82 en el golden dataset, búsqueda híbrida implementada (no solo embeddings densos), reranking activo y pipeline de ingesta con deduplicación. La dimensión agéntica evalúa: agente ReAct con LangGraph, al menos tres herramientas con contratos Pydantic, max_iterations configurado y task completion rate >= 75% en el golden dataset. La dimensión de seguridad evalúa: ADR-004 con threat model documentado, al menos tres controles implementados y red teaming de mínimo 20 ataques documentados con resultados. La dimensión MLOps evalúa: Dockerfile funcional, pipeline CI/CD con al menos build + test + deploy, y despliegue en Kubernetes o Docker Compose con configuración de producción.

## Criterios de evaluación por dimensión

- Pipeline RAG: faithfulness >= 0.82, búsqueda híbrida, reranking, ingesta con deduplicación y pipeline de chunking validado
- Sistema agéntico: ReAct con LangGraph, >= 3 herramientas tipadas, max_iterations, task completion >= 75% en golden dataset
- Seguridad: ADR-004 con STRIDE, >= 3 controles implementados, red teaming documentado >= 20 ataques con resultados
- MLOps: Dockerfile multi-stage, CI/CD con gate de evaluación, despliegue reproducible, gestión de secrets
- Observabilidad: OpenTelemetry con trazas por etapa, dashboard con >= 4 paneles, al menos 3 alertas configuradas
- Documentación: README con setup funcional, API documentada con OpenAPI, runbook con >= 3 incidentes, guía de contribución

## Para recordar

Una rúbrica con criterios cuantitativos verificables es la diferencia entre una evaluación objetiva y una opinión — los criterios de faithfulness >= 0.82 y task completion >= 75% pueden verificarse con un script de evaluación, no con juicio subjetivo.
