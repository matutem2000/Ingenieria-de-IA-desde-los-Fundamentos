# Módulo 12 – Capítulo 07 – Sección 05

# Evaluación de seguridad: resultados del red teaming y controles implementados

La evaluación de seguridad del sistema integrador se basa en los resultados documentados del red teaming de 50 ataques y en métricas de efectividad de los controles implementados. Los resultados del red teaming se presentan como una matriz que cruza categoría de ataque con resultado (mitigado/bypass parcial/bypass exitoso) y el control responsable de la mitigación. Para los ataques de prompt injection directa, la tasa de mitigación fue del 96% (1 bypass parcial en 15 ataques), donde el bypass parcial fue una variante de injection en árabe que la lista negra no cubría; el control se mejoró con un clasificador de intent multilingüe que redujo la tasa de bypass a 0% en la iteración siguiente. Los ataques de injection indirecta mediante documentos tuvieron una tasa de mitigación del 87% (2 bypasses exitosos en 15 ataques), donde los documentos con instrucciones embebidas en código Python no fueron detectados por el sanitizador de documentos; el control se ajustó para incluir extracción y análisis de strings en bloques de código.

## Resultados del red teaming por categoría

- Prompt injection directa: 14/15 mitigados (93.3%); 1 bypass parcial en variante en árabe, corregido con clasificador multilingüe
- Prompt injection indirecta: 13/15 mitigados (86.7%); 2 bypasses en instrucciones dentro de bloques de código, corregidos
- Evasión de autorización: 10/10 mitigados (100%); filtros de allowed_document_types en Qdrant bloquearon todos los casos
- DoS agéntico: 8/10 mitigados (80%); 2 casos de queries que maximizan iteraciones, corregidos con clasificador de complejidad
- Tasa global de bypass: 3/50 ataques (6%), objetivo era < 5%; controles ajustados redujeron a 1/50 (2%) en iteración siguiente

## Para recordar

Los resultados del red teaming no son un informe de éxito o fracaso — son el mecanismo de mejora continua de la seguridad, donde cada bypass detectado en la sesión de evaluación es un control que debe mejorarse antes del deploy a producción.
