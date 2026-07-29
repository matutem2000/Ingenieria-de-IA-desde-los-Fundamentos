# Módulo 12 – Capítulo 01 – Sección 05

# Criterios de éxito técnico: métricas de calidad, rendimiento y seguridad del sistema

Los criterios de éxito del proyecto final son métricas verificables, no aspiraciones. El sistema debe alcanzar en producción un RAGAS faithfulness >= 0.85 y un answer relevance >= 0.80 medidos sobre un golden dataset de 200 preguntas anotadas manualmente. En términos de rendimiento, la latencia P95 del pipeline completo debe ser inferior a 3 segundos bajo carga de 50 usuarios concurrentes, con un costo medio por petición inferior a 0.015 USD. La seguridad requiere que el sistema supere un red teaming de 50 ataques de prompt injection documentados con tasa de bypass inferior al 5%, y que todos los inputs sean validados mediante Pydantic con rechazo de payloads malformados antes de alcanzar el modelo. El sistema debe pasar un checklist de producción de 30 puntos que incluye health checks, graceful shutdown, rotación de secrets y alertas configuradas.

## Métricas de éxito por dimensión

- Calidad RAG: RAGAS faithfulness >= 0.85, answer relevance >= 0.80, context precision >= 0.75 sobre golden dataset de 200 casos
- Rendimiento: latencia P50 < 1.5s, P95 < 3s, P99 < 5s bajo carga de 50 usuarios concurrentes con ramp-up de 10s
- Costo: costo medio por petición < 0.015 USD, costo máximo < 0.03 USD para queries de alta complejidad con contexto extenso
- Seguridad: tasa de bypass de prompt injection < 5% en red teaming de 50 ataques documentados con variantes de jailbreak
- Operabilidad: tiempo de recovery ante fallo de pod < 30s, zero downtime en despliegue canary con rollback automático disponible

## Idea central

Los criterios de éxito técnico deben definirse antes de comenzar la implementación — una métrica que no puede medirse durante el desarrollo no puede garantizarse en producción.
