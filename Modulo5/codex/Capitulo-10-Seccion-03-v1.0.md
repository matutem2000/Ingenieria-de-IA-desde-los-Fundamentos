# Módulo 5 – Capítulo 10 – Sección 03

# Patrón Gateway: punto único de entrada para llamadas a modelos

El patrón Gateway centraliza todas las llamadas a los LLMs a través de un único componente o servicio que actúa como proxy inteligente: autentica las llamadas, aplica rate limiting interno, añade observabilidad, implementa routing por modelo, gestiona fallbacks entre proveedores, y aplica políticas de seguridad —todo ello sin que el código de aplicación necesite conocer estos detalles. En arquitecturas de microservicios, el AI Gateway puede ser un servicio independiente (ej. litellm proxy, Kong AI Gateway) que expone una API compatible con la interfaz de OpenAI y por detrás enruta las llamadas al proveedor configurado; los servicios de la organización hablan siempre con el gateway en lugar de hacerlo directamente con los proveedores, lo que centraliza la rotación de credenciales, el monitoreo de costos y las políticas de uso en un único punto de control. En arquitecturas más simples sin microservicios, el patrón Gateway se implementa como una clase Python `LLMGateway` con métodos `complete()`, `stream()` y `embed()` que envuelven los SDKs de los proveedores, aplican retry con backoff, loggean cada llamada, y exponen métricas vía Prometheus; todos los módulos de la aplicación usan esta clase en lugar de los SDKs directamente.

## Componentes del patrón Gateway para LLMs

- LiteLLM Proxy: servidor FastAPI open source que expone la interfaz de OpenAI y enruta a 100+ modelos de distintos proveedores; configura modelos en YAML, soporta load balancing, fallback entre proveedores, rate limiting por API key, y logging a Langfuse o LangSmith
- Gateway como clase Python: `class LLMGateway: def __init__(self, provider, model, ...); def complete(self, messages, **kwargs) -> LLMResponse: # retry, logging, metrics`, inyectada vía dependency injection en los servicios que la usan
- Routing por costo y capacidad: el gateway implementa lógica de routing (`if task_complexity == "simple": model = "haiku"; elif task_complexity == "complex": model = "sonnet"`) de forma centralizada, evitando que esta lógica esté dispersa en cada punto de uso
- Fallback entre proveedores: si Anthropic devuelve 529 (sobrecarga) o 429 (rate limit agotado), el gateway reintenta automáticamente con OpenAI usando el modelo equivalente configurado; el caller nunca ve el fallo del proveedor primario
- Auditoría centralizada: cada llamada que pasa por el gateway se registra con `caller_id`, `model`, `tokens`, `latency`, `cost`, `request_id`, proporcionando un registro centralizado de toda la actividad de IA de la organización sin depender de que cada servicio implemente su propio logging

## Idea central

El patrón Gateway convierte un conjunto disperso de llamadas a APIs de múltiples proveedores en un sistema gestionado con políticas centralizadas; el costo de implementarlo una sola vez se recupera rápidamente en términos de operación simplificada, rotación de credenciales sin tocar el código de aplicación, y visibilidad unificada del gasto.
