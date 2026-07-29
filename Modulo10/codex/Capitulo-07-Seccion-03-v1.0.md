# Módulo 10 – Capítulo 07 – Sección 03

# Routing inteligente: redirigir peticiones al modelo correcto según latencia, costo y calidad

El routing inteligente en un LLM Gateway implementa la lógica de decisión para seleccionar, request a request, cuál modelo y cuál proveedor sirve mejor cada petición según múltiples criterios simultáneos, en lugar de enrutar todo el tráfico al mismo modelo de forma estática. El router puede operar en tres modos: routing basado en reglas explícitas (si el contexto supera 16k tokens, usar Claude; si la latencia requerida es <200ms, usar GPT-3.5; si el proyecto tiene flag de `use_cheaper_model`, usar Gemini Flash), routing basado en el estado del sistema (si el proveedor primario está experimentando latencia elevada > threshold medido en los últimos 60 segundos, redirigir al proveedor secundario), y routing por contenido (clasificar el request en categorías y asignar el modelo óptimo para cada categoría: código → CodeLlama o GPT-4 con system prompt especializado, resumen → Claude Haiku, razonamiento complejo → o3 o Claude Opus). La implementación de routing basado en latencia requiere circuit breakers por proveedor: si el proveedor A tiene una tasa de error > 5% en los últimos 60 segundos, el circuit breaker lo marca como "open" y el router evita enviarle tráfico hasta que pase el período de recuperación; este patrón, implementado con librerías como `pybreaker` o directamente en la lógica del gateway, protege al sistema de la latencia de cascade cuando un proveedor se degrada.

## Estrategias de routing inteligente

- Rule-based routing: tabla de reglas configurables en YAML/JSON que mapean condiciones del request (modelo solicitado, tamaño del contexto, project_id, required_latency_sla) a modelos/proveedores específicos
- Latency-aware routing: medir la latencia media de cada proveedor en una ventana deslizante de 60 segundos y dirigir el tráfico al más rápido, con pesos de round-robin ajustados dinámicamente
- Cost-optimized routing: estimar el costo del request (input tokens × precio/token + output tokens estimados × precio/token) y seleccionar el modelo más barato que cumpla el SLA de calidad mínima requerida
- Fallback chains: secuencia ordenada de modelos a intentar si el primero falla: `[gpt-4o, claude-3-5-sonnet, gpt-4o-mini]`; el gateway intenta el siguiente en la cadena ante error HTTP 429, 503, o timeout
- A/B routing para evaluación: enviar un porcentaje configurable del tráfico (ej. 5%) a un modelo experimental y comparar las métricas de calidad y satisfacción de usuario contra el modelo de producción

## Para recordar

El routing inteligente convierte la complejidad de gestionar múltiples proveedores y modelos en una ventaja: la organización puede optimizar simultáneamente costo, latencia y calidad sin que los equipos de desarrollo cambien una línea de código.
