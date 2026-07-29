# Módulo 12 – Capítulo 01 – Sección 01

# Propósito del proyecto final: demostrar dominio integrado de AI Engineering aplicado

El proyecto final del libro no es un ejercicio académico aislado: es un sistema de IA completo, desplegado y evaluado, que integra cada capa técnica estudiada a lo largo de los módulos anteriores. A diferencia de los ejercicios parciales de cada capítulo, el proyecto final exige que el ingeniero tome decisiones arquitectónicas reales con restricciones reales: latencia máxima aceptable, costo por petición, controles de seguridad no negociables y métricas de calidad medibles. El sistema deberá incluir un pipeline RAG con evaluación RAGAS, un agente con herramientas instrumentadas, observabilidad con OpenTelemetry y despliegue automatizado mediante CI/CD. El propósito es demostrar que el ingeniero puede construir, evaluar y operar un sistema de IA en producción, no solo prototiparlo.

## Capacidades demostradas

- Integración de RAG + agente + API como sistema cohesivo con contratos de interfaz definidos
- Evaluación cuantitativa mediante RAGAS (faithfulness, answer relevance, context precision)
- Instrumentación con OpenTelemetry: trazas distribuidas y métricas de latencia P50/P95/P99
- Controles de seguridad activos: validación de inputs, output filtering y protección contra prompt injection
- Despliegue reproducible mediante Docker Compose o Kubernetes con configuración por entorno

## Para recordar

El proyecto final es la demostración de que se puede diseñar, construir, evaluar y operar un sistema de IA completo — no solo hacer funcionar un LLM en un notebook.
