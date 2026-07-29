# Módulo 7 – Capítulo 07 – Sección 04

# Evaluación de completitud de tareas: criterios de éxito y métricas de tarea

La evaluación de completitud determina si el agente logró el objetivo de la tarea de forma satisfactoria, independientemente de la trayectoria que tomó para llegar ahí. Definir criterios de éxito claros y medibles es uno de los ejercicios más importantes en el diseño de sistemas agénticos: sin criterios explícitos, la evaluación de si el agente "funciona" queda relegada a la inspección visual subjetiva de los outputs, lo que no escala y no detecta regresiones. Los criterios de éxito deben especificarse en dos niveles: verificación programática (el output cumple propiedades verificables sin intervención humana: el JSON es válido, el código compila, la URL devuelve HTTP 200, el email contiene los campos requeridos) y evaluación semántica (el contenido del output es correcto según el objetivo: la respuesta responde la pregunta, el código implementa la funcionalidad solicitada, el análisis es factualmente correcto). La combinación de ambos niveles produce una función de evaluación robusta que puede ejecutarse automáticamente en pipelines de evaluación continua.

## Aspectos técnicos

- **Criterios programáticos de completitud**: verificaciones automáticas sin LLM; ejemplos: el output JSON valida contra el schema esperado, el archivo generado tiene más de N bytes, la query SQL es sintácticamente correcta, la URL extraída devuelve HTTP 200 con un timeout de 5 segundos
- **LLM-as-judge para completitud semántica**: un prompt de evaluación que recibe el input del usuario, el output del agente y un rubric (criterios de evaluación en lenguaje natural) y devuelve un score (0-1 o 1-5) con justificación; usar modelos fuertes como GPT-4o o Claude 3.5 Sonnet como judges incluso si el agente evaluado usa modelos menores
- **Task success rate**: porcentaje de tareas de un test set que el agente completa satisfactoriamente; la métrica principal de comparación entre versiones del agente; calcular con intervalos de confianza estadísticos dado el tamaño del test set
- **Partial credit scoring**: para tareas complejas con múltiples sub-objetivos, asignar puntuación parcial por cada sub-objetivo completado; más informativo que éxito binario para diagnosticar dónde falla el agente
- **Evaluación end-to-end vs subtarea**: complementar la evaluación end-to-end (¿completó la tarea completa?) con evaluación por subtarea (¿cuál de los N pasos falló?); permite identificar el punto exacto de fallo en tareas complejas

## Buena práctica

Definir los criterios de éxito de la tarea antes de comenzar la implementación del agente: si no sabes exactamente qué significa que el agente "completó" la tarea, no podrás medir ni mejorar su desempeño de forma sistemática.
