# Módulo 12 – Capítulo 02 – Sección 02

# ADR 001: elección de modelo fundacional — criterios y justificación

La elección del modelo fundacional es la decisión de mayor impacto en el sistema integrador: afecta directamente la calidad de las respuestas, la latencia del pipeline, el costo por petición y los requisitos de seguridad. El ADR-001 documenta la evaluación entre GPT-4o (OpenAI), Claude 3.5 Sonnet (Anthropic) y Gemini 1.5 Pro (Google) usando un benchmark interno de 100 preguntas del dominio técnico objetivo, midiendo accuracy semántica evaluada por LLM-as-judge, latencia mediana y costo por 1000 tokens. Los criterios de eliminación temprana fueron: ausencia de JSON mode estructurado nativo, latencia P95 > 4 segundos, y precio superior a 15 USD por millón de tokens de output. La decisión final documenta que GPT-4o fue elegido por combinar el mejor score de accuracy (0.88 vs 0.86 de Claude 3.5 Sonnet) con soporte para function calling paralelo, que el agente ReAct necesita para ejecutar múltiples herramientas en un solo turno.

## Criterios de evaluación del modelo

- Benchmark de calidad: accuracy semántica evaluada por GPT-4o-as-judge sobre 100 preguntas del dominio objetivo
- Latencia: tiempo de first-token (TTFT) y latencia total medidos bajo carga de 10 peticiones simultáneas
- Costo: precio por millón de tokens de input y output, con proyección de costo mensual según volumen esperado
- Function calling: soporte para parallel tool use y JSON mode estructurado con schema validation integrado
- Disponibilidad de API: uptime histórico del proveedor, SLA documentado y presencia de circuit breakers

## Buena práctica

El ADR-001 del modelo no se escribe una sola vez — se revisa cuando el proveedor lanza una versión nueva, cuando el costo cambia significativamente, o cuando las métricas de calidad en producción caen por debajo del umbral acordado.
