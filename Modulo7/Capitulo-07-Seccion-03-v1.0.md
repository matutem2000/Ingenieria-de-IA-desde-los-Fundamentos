# Módulo 7 – Capítulo 07 – Sección 03

# Testing de trayectorias: verificar que el agente toma las decisiones correctas

El testing de trayectorias evalúa la secuencia de acciones que el agente toma para resolver una tarea, no solo el resultado final: ¿usó las herramientas correctas en el orden correcto? ¿evitó herramientas innecesarias? ¿aplicó la estrategia de razonamiento apropiada? Este nivel de testing es crucial porque un agente puede llegar al resultado correcto a través de una trayectoria subóptima (usando 8 herramientas cuando 3 eran suficientes) o incluso a través de una trayectoria incorrecta que solo funciona en el caso de prueba por coincidencia. En LangSmith y Langfuse, las trazas de ejecución de un agente incluyen cada paso del ciclo —tool call, arguments, observation, next reasoning step— que pueden compararse contra trayectorias de referencia (golden trajectories) anotadas manualmente para los casos de test. La evaluación de trayectorias puede ser programática (verificar que se invocó la herramienta X antes de la herramienta Y) o basada en LLM-judge (un modelo evalúa si la trayectoria completa fue razonable dado el objetivo).

## Aspectos técnicos

- **Golden trajectories**: conjunto de pares (task_input, expected_trajectory) anotados manualmente o generados por un agente de referencia; la expected_trajectory especifica las herramientas que deben invocarse, en qué orden y con qué argumentos (exactos o parciales)
- **Trajectory matching**: algoritmos para comparar trayectorias; matching exacto (mismo orden, mismas herramientas, mismos argumentos) es demasiado estricto; matching parcial (las herramientas críticas están presentes, aunque con argumentos ligeramente diferentes) es más tolerante y práctico
- **Métricas de eficiencia de trayectoria**: número de pasos para completar la tarea (menos es mejor), número de retries por fallo de herramienta, ratio de herramientas usadas vs herramientas disponibles; comparar estas métricas entre versiones del agente para detectar regresiones
- **LLM-as-trajectory-judge**: usar un LLM con un prompt de evaluación que recibe la tarea, la trayectoria ejecutada y un rubric de evaluación (criterios de buena decisión en cada paso) y genera un score + justificación; útil para trayectorias complejas donde el matching programático es insuficiente
- **Testing de invariantes**: en lugar de comparar contra una trayectoria específica, verificar propiedades que siempre deben cumplirse: "el agente nunca invoca `delete_file` sin antes invocar `confirm_action`", "el agente siempre verifica el resultado de la búsqueda antes de responder al usuario"

## Principio rector

El testing de trayectorias convierte el "llego al resultado correcto" en "llego al resultado correcto de la manera correcta": la segunda garantía es necesaria para que el comportamiento del agente sea predecible, auditahle y mejorable sistemáticamente.
