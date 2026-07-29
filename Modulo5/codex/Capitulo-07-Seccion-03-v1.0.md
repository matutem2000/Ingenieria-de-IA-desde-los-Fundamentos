# Módulo 5 – Capítulo 07 – Sección 03

# Evaluación con LLM-as-Judge: diseño de jueces y criterios

LLM-as-Judge es el patrón de evaluación donde se usa un LLM más capaz o del mismo nivel para evaluar la calidad de las respuestas de un sistema, reemplazando o complementando la evaluación humana en casos donde el volumen lo hace impracticable. La confiabilidad de un juez LLM depende críticamente del diseño del prompt de evaluación: un prompt genérico ("¿es esta respuesta buena?") produce evaluaciones inconsistentes y sesgadas; un prompt con rúbrica explícita, ejemplos de cada nivel de la escala, y separación clara entre criterios produce evaluaciones con alta correlación con el juicio humano (r > 0.8 en benchmarks como MT-bench y Chatbot Arena). Las dimensiones de evaluación que un juez bien diseñado debe abordar de forma independiente son: completitud (¿la respuesta aborda todos los aspectos de la pregunta?), precisión factual (¿las afirmaciones son correctas?), formato (¿cumple con el formato solicitado?), y seguridad (¿contiene contenido inapropiado?). Los sesgos conocidos del LLM-as-judge que deben mitigarse incluyen: position bias (el modelo favorece la primera o última opción en comparaciones A/B), verbosity bias (el modelo favorece respuestas más largas aunque no sean mejores), y self-enhancement bias (Claude evaluador puede favorecer respuestas de Claude vs otros modelos).

## Aspectos técnicos del diseño de jueces LLM

- Prompt de juez con rúbrica explícita: definir cada nivel de la escala con ejemplos concretos ("Nivel 1: la respuesta no aborda la pregunta. Ejemplo: [...]"), en lugar de descriptores abstractos ("malo", "regular", "bueno")
- Evaluación de múltiples criterios por separado: evitar el "halo effect" pidiendo al juez que evalúe primero completitud, luego precisión, luego formato; las evaluaciones por criterio separado correlacionan mejor con el juicio humano que las evaluaciones holísticas
- Mitigation del position bias: en comparaciones A/B (prompt A vs prompt B), ejecutar la evaluación dos veces con el orden invertido y promediar los resultados; si el juicio cambia al cambiar el orden, la diferencia de calidad no es estadísticamente significativa
- Chain-of-thought en el juez: pedir al juez que explique su razonamiento antes de dar el score (`"Primero analiza los criterios, luego asigna el score"`) mejora la consistencia y la trazabilidad; el razonamiento puede revisarse cuando el score parece incorrecto
- Calibración del juez con datos humanos: comparar los scores del juez LLM con una muestra de evaluaciones humanas (50-100 casos) usando Spearman correlation o Cohen's Kappa ponderado; un juez con correlación < 0.7 con el juicio humano necesita rediseño de su prompt

## Buena práctica

Documentar el prompt exacto del juez LLM junto con su versión del modelo evaluador como parte del sistema de evaluación versionado, ya que cambios en cualquiera de los dos pueden cambiar los scores históricos haciendo imposible la comparación temporal.
