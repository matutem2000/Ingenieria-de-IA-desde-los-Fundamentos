# Módulo 5 – Capítulo 06 – Sección 01

# Diferencias entre CI/CD tradicional y CI/CD para sistemas de IA

El CI/CD tradicional valida que el código compila, los tests pasan y las métricas de performance de software (latencia, throughput, uso de memoria) están dentro de los límites; en sistemas de IA este conjunto necesario pero no suficiente se extiende con una dimensión nueva: la calidad de las respuestas del modelo, que no puede verificarse con tests deterministas. Un pipeline de CI para un servicio web convencional verifica si `def add(a, b): return a + b` es correcto; un pipeline de CI para un sistema de IA debe verificar si "el asistente responde correctamente a preguntas sobre el producto en el 95% de los casos del dataset de evaluación", lo que requiere llamadas reales al LLM, comparación con criterios de calidad, y decisiones estadísticas. Las consecuencias de este shift son concretas: el pipeline de CI de IA es más lento (segundos a minutos vs milisegundos), tiene costo variable (cada ejecución llama a APIs de pago), y su resultado puede ser probabilístico (el mismo pipeline puede pasar o fallar por variabilidad del modelo). Los gatekeepers del despliegue en CI/CD de IA son: los tests unitarios tradicionales, las métricas de evaluación de calidad sobre datasets curados, y las métricas de producción en despliegues canary antes del rollout completo.

## Aspectos técnicos del CI/CD para IA

- Separación de pipelines: el pipeline rápido de CI (linting, type checking, unit tests con mocks, <2 minutos) se ejecuta en cada commit; el pipeline de evaluación de calidad (llamadas reales al LLM, métricas RAGAS) solo se ejecuta cuando archivos de prompt o pipeline cambian, usando `paths` filters en GitHub Actions o GitLab CI
- Costos del pipeline de evaluación: calcular y registrar el costo de cada run de evaluación (`total_tokens * precio_por_token`), con alertas cuando el costo de un run supera un umbral; pipelines de evaluación sin control de costo pueden acumular facturas significativas en repositorios activos
- Artefactos de evaluación: guardar los resultados del run de evaluación (scores por caso de prueba, métricas agregadas, respuestas del LLM) como artefactos del pipeline para diagnóstico retrospectivo y comparación entre runs
- Gates de calidad configurables: definir umbrales en variables del pipeline (`MIN_FAITHFULNESS_SCORE=0.80`, `MIN_ANSWER_RELEVANCY=0.75`) en lugar de hardcodearlos, permitiendo ajustarlos sin modificar el código del pipeline
- Notificaciones de degradación: configurar notificaciones a Slack o email cuando el pipeline de evaluación falla o cuando las métricas caen por debajo del umbral, con el diff del run vs el baseline para facilitar el diagnóstico

## Para recordar

El CI/CD para sistemas de IA no reemplaza al CI/CD tradicional sino que lo extiende con una capa de evaluación de calidad; los sistemas que omiten esta capa son sistemas donde los cambios de calidad solo se detectan en producción.
