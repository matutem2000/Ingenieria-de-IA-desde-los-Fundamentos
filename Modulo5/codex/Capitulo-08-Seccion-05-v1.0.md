# Módulo 5 – Capítulo 08 – Sección 05

# Herramientas: LangSmith, Langfuse, Weights & Biases, OpenTelemetry

El ecosistema de observabilidad para sistemas de IA ha madurado rápidamente, con herramientas especializadas que van más allá de las plataformas de observabilidad general para capturar las dimensiones específicas de IA: trazas de cadenas, evaluación de calidad, gestión de datasets y comparación de experimentos. LangSmith (de LangChain) es la plataforma de observabilidad nativa para aplicaciones LangChain: auto-integración con `LANGCHAIN_TRACING_V2=true`, captura de todas las llamadas al LLM con latencia y tokens, playground para re-ejecutar trazas con diferentes prompts, y Dataset & Evaluation para crear datasets a partir de trazas de producción y ejecutar suites de evaluación. Langfuse es la alternativa open source y self-hosteable (Docker Compose o Kubernetes) con SDK para Python, TypeScript y cualquier lenguaje vía REST API: captura prompts, respuestas, tokens, latencia y scores de evaluación; incluye prompt management con versionado, A/B testing de prompts, y exportación de datasets; siendo open source, el costo de operación es el de la infraestructura propia. Weights & Biases (W&B) Weave extiende la plataforma de MLOps de W&B hacia LLM Engineering: tracing de llamadas, evaluación de modelos, y comparación de runs de fine-tuning con métricas de calidad.

## Herramientas de observabilidad para sistemas de IA

- LangSmith: integración vía `LangSmithCallbackHandler` o variables de entorno `LANGCHAIN_API_KEY` + `LANGCHAIN_PROJECT`; UI con árbol de trazas, comparación de runs, playground interactivo y anotación humana de respuestas; pricing por proyecto y volumen de trazas
- Langfuse: SDK Python `from langfuse import Langfuse; lf = Langfuse(); trace = lf.trace(name="chat"); span = trace.span(name="llm_call"); span.end(output=response, usage=usage_object)`; self-hosteable con Postgres, Redis y S3; incluye gestión de prompts versionados accesibles desde el código
- OpenTelemetry (OTel): estándar neutral al proveedor con `opentelemetry-sdk` y exportadores a Jaeger, Zipkin, Datadog, Honeycomb o Grafana Tempo; las semantic conventions `gen_ai.*` estandarizan los atributos de spans de IA; ideal para equipos que ya tienen observabilidad OTel y quieren unificar el stack
- Weights & Biases Weave: `import weave; weave.init("my-project"); @weave.op()` decorador que captura inputs, outputs y metadata de funciones Python que llaman a LLMs; integrado con el ecosistema de experimentos de W&B para comparar modelos fine-tuned vs base
- Arize AI Phoenix: plataforma de observabilidad de IA con foco en detección de drift de datos y degradación de calidad; integración con LangChain, LlamaIndex y OpenAI; soporta tanto trazas como evaluación de calidad con métricas como evals scores

## Buena práctica

Elegir la herramienta de observabilidad antes de escribir la primera línea de código de producción y usarla desde el inicio, no añadirla después; el costo de instrumentar retroactivamente un sistema en producción —especialmente uno con código de terceros como LangChain— es desproporcionado al costo de configurarla desde el día uno.
