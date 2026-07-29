# Módulo 12 – Capítulo 04 – Sección 05

# Observabilidad agéntica: trazas de razonamiento y métricas de completitud de tareas

La observabilidad del agente va más allá de las métricas estándar de latencia y error rate — requiere capturar las trazas de razonamiento completas para entender por qué el agente tomó cada decisión. Cada ejecución del agente emite un span OpenTelemetry de nivel raíz con `agent.trace_id`, que contiene spans hijo por cada paso del ciclo ReAct: `agent.thought` (razonamiento del LLM), `agent.tool_call` (herramienta llamada con argumentos y resultado), y `agent.final_answer` (respuesta generada). Las métricas de completitud de tareas se calculan en dos dimensiones: task completion rate (porcentaje de queries donde el agente entregó una respuesta con al menos un documento citado) y task accuracy rate (porcentaje donde la respuesta fue evaluada como correcta por LLM-as-judge). LangSmith se usa para almacenar las trazas completas de razonamiento, permitiendo debug visual de ejecuciones fallidas y análisis de patrones de uso de herramientas.

## Métricas de observabilidad agéntica

- Trazas de razonamiento: spans OpenTelemetry por cada paso ReAct con duración, herramienta usada y tokens consumidos
- Tool usage rate: distribución de llamadas por herramienta para detectar sobreuso o infrauso de capacidades disponibles
- Iterations per task: distribución del número de iteraciones por query para detectar casos de complejidad anómala
- Task completion rate: porcentaje de queries con respuesta completa (vs declinadas o con error) por ventana de tiempo
- LangSmith tracing: almacenamiento de trazas completas para debugging visual de ejecuciones fallidas o inesperadas

## Para recordar

Sin trazas de razonamiento, el comportamiento del agente es una caja negra — cuando el agente falla o produce una respuesta incorrecta, los spans de cada paso del ciclo ReAct son el único mecanismo para entender el porqué.
