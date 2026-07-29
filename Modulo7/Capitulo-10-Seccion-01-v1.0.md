# Módulo 7 – Capítulo 10 – Sección 01

# Métricas de tarea: tasa de completitud, precisión de pasos y eficiencia de herramientas

Las métricas de tarea son los indicadores cuantitativos que miden si el agente logra sus objetivos operativos en producción, y son la base sobre la que se toman decisiones de mejora, regresión de versiones y comparación entre modelos. La tasa de completitud de tareas (Task Completion Rate, TCR) es la fracción de tareas del conjunto de evaluación que el agente completa exitosamente según los criterios predefinidos; un TCR del 85% en el test set y del 70% en producción indica un gap de distribución que requiere análisis de los casos de fallo en producción. La precisión de pasos (Step Accuracy) mide qué fracción de los pasos individuales en la trayectoria del agente son correctos (herramienta correcta, argumentos correctos, interpretación correcta de la observación); un agente con alta precisión de pasos pero baja TCR probablemente falla en un paso específico de la cadena. La eficiencia de herramientas (Tool Efficiency) mide cuántas llamadas a herramientas requiere el agente para completar la tarea, comparado con el mínimo teórico; alta ineficiencia indica sobre-uso de herramientas o bucles de corrección evitables.

## Métricas clave

- **Task Completion Rate (TCR)**: porcentaje de tareas completadas exitosamente según criterios programáticos o LLM-judge; calcular separadamente para diferentes categorías de tarea (simple, media, compleja) para identificar dónde falla el agente
- **Step Accuracy**: porcentaje de pasos individuales en la trayectoria que son correctos; requiere golden trajectories anotadas o evaluación por LLM-judge de cada paso; permite identificar el paso específico donde el agente más frecuentemente se desvía
- **Tool Call Efficiency**: ratio de llamadas necesarias sobre llamadas realizadas (ideal = 1.0, mayor que 1 indica ineficiencia); detecta agentes que realizan búsquedas redundantes, reintentan innecesariamente o verifican información que ya está en el contexto
- **Token Efficiency**: tokens totales consumidos por tarea (input + output + tool results) dividido por la complejidad de la tarea; permite comparar la eficiencia entre versiones del agente y estimar el costo esperado por tarea
- **Mean Time to Complete (MTTC)**: latencia media end-to-end por tarea, desde el primer mensaje del usuario hasta la respuesta final del agente; monitorear su distribución (P50, P95, P99) para detectar outliers y degradaciones de performance

## Principio rector

Las métricas de tarea solo son útiles si se miden sobre distribuciones representativas de casos de uso reales: un TCR del 95% en un test set fácil y curado proporciona falsa confianza si el 50% de las tareas de producción son más complejas que las del test set.
