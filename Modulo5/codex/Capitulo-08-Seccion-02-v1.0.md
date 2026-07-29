# Módulo 5 – Capítulo 08 – Sección 02

# Trazas distribuidas: seguimiento de una petición a través de cadenas y agentes

Las trazas distribuidas en sistemas de IA siguen el mismo modelo que en microservicios —trace ID propagado a través de todos los componentes, con spans para cada operación— pero con spans específicos de IA que capturan información que no existe en trazas de software tradicional: el prompt enviado al modelo, la respuesta recibida, los tokens consumidos, el documento recuperado del vector store y el score de relevancia. El estándar OpenTelemetry (OTel) es el protocolo de instrumentación neutral al proveedor: define la API para crear traces, spans y attributes; exporta vía OTLP (gRPC o HTTP) a cualquier backend (Jaeger, Zipkin, Datadog, Honeycomb); y tiene auto-instrumentación para llamadas HTTP que captura automáticamente las llamadas al LLM API. Para pipelines LangChain, el `LangChainCallbackHandler` de Langfuse o el `LangSmithCallbackHandler` captura automáticamente cada nodo de la cadena como un span hijo de la traza principal, sin modificar el código de la cadena. En sistemas de agentes con múltiples llamadas al LLM por request, las trazas son indispensables para entender el árbol de razonamiento: qué herramientas decidió usar el agente, en qué orden, con qué inputs y qué outputs intermedios.

## Aspectos técnicos del distributed tracing para IA

- OpenTelemetry SDK en Python: `from opentelemetry import trace; tracer = trace.get_tracer(__name__)` y `with tracer.start_as_current_span("llm_call") as span: span.set_attribute("llm.model", model); span.set_attribute("llm.input_tokens", input_tokens)` para instrumentación manual con context propagation automática
- Semantic conventions para IA (OTel Gen AI): el working group de OTel define atributos estándar como `gen_ai.system` (openai/anthropic/google), `gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, estandarizando los atributos de las trazas de IA entre herramientas
- Langfuse tracing vía callback: `from langfuse.callback import CallbackHandler; handler = CallbackHandler(); chain.invoke(input, config={"callbacks": [handler]})` captura toda la cadena LangChain como traza jerárquica en Langfuse sin modificar el código de la cadena
- Sampling estratégico: tracear el 100% del tráfico es prohibitivo a escala; head-based sampling (decidir al inicio del request) o tail-based sampling (decidir al final, manteniendo siempre los requests lentos o erróneos) reducen el volumen de trazas sin perder visibilidad de los casos problemáticos
- Redaction de información sensible: los spans de IA pueden contener PII (nombres, emails, datos médicos) en los prompts y respuestas; implementar redaction automático en el exporter antes de enviar las trazas al backend cumple con GDPR y HIPAA

## Para recordar

Una traza completa de un agente con 5 llamadas al LLM, 3 consultas al vector store y 2 invocaciones de herramientas externas puede transformar un diagnóstico de 2 horas en 5 minutos; el ROI de instrumentar trazas desde el inicio supera siempre el costo de añadirlas después.
