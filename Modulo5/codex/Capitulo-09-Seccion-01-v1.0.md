# Módulo 5 – Capítulo 09 – Sección 01

# Anatomía del costo: tokens de entrada, salida, caché y llamadas a herramientas

El costo de una llamada a la API de un LLM se compone de múltiples componentes que deben entenderse individualmente para optimizar el gasto total: tokens de entrada (el prompt completo incluyendo system prompt, historial conversacional y contexto recuperado), tokens de salida (la respuesta generada, generalmente 3-5x más costosos por token que los de entrada), tokens de caché (tokens de entrada que fueron escritos al caché en una llamada anterior y se leen a costo reducido), y en algunos modelos el costo de las llamadas a herramientas (tool use) que se factura separadamente en ciertas configuraciones. Con Claude 3.5 Sonnet como ejemplo, el precio es $3/millón de tokens de entrada y $15/millón de tokens de salida; si un sistema de chat promedia 2.000 tokens de entrada y 400 tokens de salida por request, el costo por request es $(2000/1M)*$3 + (400/1M)*$15 = $0.006 + $0.006 = $0.012; a 100.000 requests/mes el costo mensual es $1.200. La variabilidad del costo entre requests es alta: un request con contexto de 500 tokens y respuesta de 100 tokens cuesta $0.003; un request con contexto de 50.000 tokens (documento largo) y respuesta de 2.000 tokens cuesta $0.18, 60x más caro.

## Componentes del costo de las APIs de LLM

- Tokens de entrada: el componente de mayor volumen de tokens pero menor precio por token; incluye system prompt, historial conversacional, documentos recuperados por RAG, ejemplos few-shot, y la query del usuario; crecer sin control si no se implementan límites de contexto
- Tokens de salida: menor volumen pero mayor precio por token (3-5x más que entrada en la mayoría de proveedores); su costo se controla limitando `max_tokens`, instruyendo al modelo a ser conciso, y usando formatos compactos (JSON vs XML verbose)
- Tokens cacheados de entrada (cache read): Anthropic cobra $0.30/M tokens cacheados leídos vs $3/M de tokens de entrada no cacheados (90% de descuento); Google Gemini cobra caching de contexto a precio diferencial con mínimo de 4.096 tokens para activar el cache
- Cache write tokens: el costo de escribir al caché en Anthropic es $3.75/M tokens (25% más caro que la lectura sin caché), pero se amortiza en pocas llamadas que reutilicen el mismo prefijo; el breakeven es 1.25 llamadas que usen el mismo prefijo cacheado
- Costos de herramientas y multimodalidad: las llamadas con imágenes se facturan por "tiles" de 512x512px en OpenAI (ej. imagen de 1024x1024 = 4 tiles); los tool results que vuelven como parte del contexto se cuentan como tokens de entrada adicionales en el siguiente turno

## Principio rector

El costo total de un sistema de IA es predecible si se instrumenta cada llamada con el conteo exacto de tokens de entrada, salida y caché; la variabilidad de costo sin instrumentación convierte el presupuesto en una sorpresa mensual en lugar de un métrica gestionada.
