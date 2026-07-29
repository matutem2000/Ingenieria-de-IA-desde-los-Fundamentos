# Módulo 5 – Capítulo 07 – Sección 06

# Cierre: construir un sistema de evaluación continua

Un sistema de evaluación continua no es una herramienta que se ejecuta puntualmente antes de un despliegue, sino un componente permanente del sistema de IA que opera en paralelo con el servicio de producción: evalúa el tráfico real, detecta degradaciones, alimenta el dataset offline con nuevos casos, y produce métricas visibles para el equipo en tiempo real. La construcción incremental de este sistema sigue el mismo principio que el sistema de IA que evalúa: comenzar con lo mínimo viable —un script que ejecuta RAGAS sobre un dataset de 50 casos en un job de CI— y añadir complejidad (evaluación online, LLM-as-judge, feedback loop automático) conforme la evidencia demuestra que el incremento de cobertura de evaluación detecta problemas reales que el sistema actual no detecta. El return on investment de un sistema de evaluación continua es alto: el costo de detectar y corregir una degradación antes del despliegue es entre 10x y 100x menor que el costo de detectarla en producción, considerando el costo de comunicación con usuarios afectados, el daño reputacional y el time-to-fix en un incidente activo. El equipo que construye el sistema de evaluación también construye el entendimiento profundo del comportamiento del sistema de IA, que es un activo de conocimiento que va más allá de las métricas numéricas.

## Componentes de un sistema de evaluación continua maduro

- Evaluación en CI (Layer 1): suite de 50-500 casos offline ejecutada en PRs relevantes con RAGAS o DeepEval, con gate de calidad que bloquea merges que degradan las métricas por encima del umbral definido
- Evaluación online por muestreo (Layer 2): job asíncrono que evalúa el 1-5% del tráfico de producción con LLM-as-judge, publicando métricas a un dashboard de monitoreo con alertas configuradas
- Feedback loop (Layer 3): pipeline que mueve casos con evaluación negativa (baja puntuación, feedback negativo del usuario) al dataset offline, haciendo crecer el dataset con los fallos reales del sistema
- Evaluación humana periódica (Layer 4): revisión mensual de 50-100 casos por anotadores humanos para calibrar la correlación entre la evaluación automática y el juicio humano, y actualizar las rúbricas del LLM-as-judge si la correlación baja
- Leaderboard de versiones: tabla histórica que compara las métricas de calidad de todas las versiones del sistema desplegadas, con fecha, modelo, versión de prompt y scores, permitiendo ver la evolución de la calidad a lo largo del tiempo

*"What gets measured gets managed."* — Peter Drucker. En AI Engineering, el sistema que mide su propia calidad de forma continua y sistemática es el sistema que puede mejorar de forma deliberada y demostrable, en lugar de mejorar por intuición y sorprenderse cuando la calidad se degrada.
