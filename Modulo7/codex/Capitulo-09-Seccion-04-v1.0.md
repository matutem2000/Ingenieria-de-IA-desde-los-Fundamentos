# Módulo 7 – Capítulo 09 – Sección 04

# Observabilidad agéntica: trazas, pasos, herramientas invocadas y latencia total

La observabilidad de sistemas agénticos requiere capturar no solo el input y el output final, sino cada paso del ciclo de ejecución: qué razonamiento generó el LLM en cada iteración, qué herramienta fue invocada y con qué argumentos, cuánto tiempo tardó la herramienta, qué observación retornó, y cómo ese resultado afectó el razonamiento siguiente. Sin esta granularidad de trazas, diagnosticar un fallo en producción —¿el agente tomó la decisión incorrecta? ¿la herramienta devolvió datos incorrectos? ¿el razonamiento se desvió en el paso 7 de 12?— requiere reproducir manualmente la ejecución completa, lo que puede ser imposible si el entorno ha cambiado. Las plataformas de observabilidad especializadas en LLMs —LangSmith (LangChain), Langfuse (open-source), Arize Phoenix, Helicone— capturan automáticamente trazas anidadas de cada llamada al LLM y cada invocación de herramienta, con metadata de tokens, latencia, costo estimado y errores, disponibles en dashboards con filtros y alertas configurables.

## Aspectos técnicos

- **Trazas anidadas (spans)**: cada ejecución del agente genera una traza raíz con spans hijos para cada llamada al LLM y cada invocación de herramienta; el formato OpenTelemetry (OTLP) está siendo adoptado como estándar para trazas de LLMs, con soporte en Langfuse, Arize y otras plataformas
- **Métricas por paso**: capturar para cada paso del agente: latencia del LLM (tiempo de respuesta de la API), latencia de la herramienta (tiempo de ejecución), tokens de input/output por paso, costo estimado por paso, y el nombre de la herramienta invocada
- **Alertas de anomalías**: configurar alertas cuando: la latencia total supera el percentil 95 histórico, el número de pasos supera max_steps * 0.8 (señal de inminente timeout), el costo de una sesión supera un umbral monetario configurado, o la tasa de fallos de herramientas supera un umbral
- **Session replay**: la capacidad de reproducir paso a paso la ejecución de un agente usando las trazas almacenadas; LangSmith y Langfuse proveen esta funcionalidad como parte de su UI de debugging; esencial para investigar incidentes reportados por usuarios
- **Sampling de trazas**: en producción de alto volumen, capturar el 100% de las trazas puede ser prohibitivo en costo y almacenamiento; implementar sampling adaptativo: 100% de las ejecuciones que fallan, 100% de las que superan umbrales de latencia/costo, y un % configurable (p.ej. 10%) de las exitosas

## Para recordar

La observabilidad agéntica no es logging de texto; es la captura estructurada de cada decisión del ciclo de razonamiento-acción, con la granularidad suficiente para diagnosticar por qué el agente tomó la decisión incorrecta en el paso 7 de una cadena de 15 pasos en producción.
