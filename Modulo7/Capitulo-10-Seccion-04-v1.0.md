# Módulo 7 – Capítulo 10 – Sección 04

# Evaluación humana: validación de trayectorias y resultados finales

La evaluación humana sigue siendo el estándar de oro para la evaluación de agentes en dominios donde los criterios de calidad son subjetivos, contextuales o difíciles de formalizar: la corrección de una respuesta legal, la calidad de un análisis de negocio, o si el agente tomó el camino más eficiente para resolver un problema complejo requieren juicio humano que los evaluadores automáticos no pueden replicar con suficiente fiabilidad. La evaluación humana de agentes tiene dos niveles: evaluación del resultado final (¿la respuesta del agente es correcta, completa y útil?) y evaluación de la trayectoria (¿la secuencia de pasos del agente fue razonable y eficiente?). La segunda dimensión es especialmente valiosa para diagnóstico: un evaluador humano que revisa la trayectoria completa puede identificar exactamente en qué paso el agente tomó la decisión incorrecta y articular por qué fue incorrecta, información que alimenta directamente las iteraciones de mejora del sistema.

## Aspectos técnicos

- **Annotation guidelines**: documentar los criterios de evaluación para que distintos anotadores humanos sean consistentes entre sí; incluir ejemplos de respuestas con score 1, 2, 3, 4 y 5 (rubric con ejemplos concretos) para anclar el juicio subjetivo a referencias objetivas
- **Inter-annotator agreement (IAA)**: medir el acuerdo entre anotadores con Cohen's Kappa o Krippendorff's Alpha; un IAA < 0.6 indica que los criterios de evaluación son demasiado ambiguos y deben refinarse antes de continuar la evaluación
- **Evaluación de trayectoria paso a paso**: proporcionar al anotador el objetivo de la tarea, el historial completo de reasoning + tool calls + observations, y pedir que evalúe cada paso como: correcto, aceptable, incorrecto; el análisis de los pasos frecuentemente evaluados como incorrectos revela los puntos de fallo sistemáticos
- **Sampling estratificado**: en lugar de evaluar todos los outputs del agente, usar sampling estratificado: evaluar el 100% de los casos donde los evaluadores automáticos dan scores extremos (muy bajo o muy alto) y un sample aleatorio del resto; maximiza el valor de la evaluación humana por unidad de tiempo
- **Human-AI evaluation pipeline**: combinar evaluación automática (rápida, escalable, objetiva en criterios formalizables) con evaluación humana (para casos de baja confianza del evaluador automático o para calibración del evaluador automático contra el juicio humano)

## Buena práctica

Implementar un pipeline de feedback loop donde los resultados de la evaluación humana se alimentan directamente como datos de entrenamiento para el LLM-judge automático: los casos donde el juicio humano difiere del juicio automático son los más valiosos para mejorar la calibración del evaluador.
