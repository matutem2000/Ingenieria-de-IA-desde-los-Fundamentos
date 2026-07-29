# Módulo 5 – Capítulo 01 – Sección 01

# Panorama general: herramientas, APIs, SDKs y frameworks para construir aplicaciones de IA

El ecosistema de desarrollo de IA se puede analizar en cuatro capas tecnológicas: modelos fundacionales accesibles vía API REST (OpenAI, Anthropic, Google Vertex AI), SDKs oficiales en Python y TypeScript que encapsulan la autenticación y serialización, frameworks de orquestación como LangChain y LlamaIndex que abstraen patrones de composición, y herramientas de observabilidad como LangSmith y Langfuse que instrumentan el comportamiento en producción. Cada capa resuelve un problema diferente: las APIs proveen capacidad de inferencia, los SDKs normalizan el acceso, los frameworks reducen código repetitivo en flujos complejos, y las herramientas de observabilidad cierran el ciclo de retroalimentación. La elección de qué capa usar depende directamente del perfil de la tarea: llamadas simples no justifican la sobrecarga de un framework de orquestación. Un ingenieros de IA profesional entiende con precisión qué abstracción aporta cada herramienta y cuándo añade complejidad accidental en lugar de valor real.

## Componentes principales del ecosistema

- APIs de modelos fundacionales: endpoints HTTP REST o gRPC que exponen inferencia bajo esquemas de autenticación basada en API keys con límites de rate y cuotas de tokens por minuto (TPM) y requests por minuto (RPM)
- SDKs oficiales: bibliotecas de cliente como `openai` (Python/Node), `anthropic` (Python/TypeScript) y `google-cloud-aiplatform` que gestionan retry automático, streaming SSE y tipado estricto de parámetros
- Frameworks de orquestación: LangChain (cadenas, agentes, runnables), LlamaIndex (índices, query engines, data connectors) y DSPy (optimización declarativa de prompts) reducen boilerplate en flujos de múltiples pasos
- Herramientas de evaluación: RAGAS, DeepEval y TruLens miden calidad de respuestas con métricas como faithfulness, answer relevancy y context recall de forma automatizada
- Herramientas de observabilidad: LangSmith, Langfuse y OpenTelemetry con OTLP exporters proveen trazas distribuidas, logs estructurados y métricas de latencia y costo por petición

## Principio rector

El ecosistema de IA es una pila de abstracciones donde cada capa tiene un costo; la maestría del ingenieros de IA reside en elegir el nivel mínimo necesario para resolver el problema sin introducir dependencias innecesarias.
