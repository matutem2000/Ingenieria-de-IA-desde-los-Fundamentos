# Módulo 5 – Capítulo 09 – Sección 03

# Prompt caching: Anthropic, OpenAI y su impacto en costos repetitivos

El prompt caching es una funcionalidad del proveedor que almacena en memoria del servidor los tokens de prefix de un prompt para reutilizarlos en llamadas subsiguientes sin re-procesarlos, con un descuento significativo en el precio de los tokens cacheados. Anthropic implementa prompt caching con `cache_control: {"type": "ephemeral"}` marcado en los bloques de contenido del system prompt o los primeros mensajes: los tokens del prefijo marcado se cachean por 5 minutos (con renovación al ser usados), el costo de cache write es $3.75/M tokens (25% más que la lectura normal) y el costo de cache read es $0.30/M tokens (90% de descuento); el breakeven se alcanza con solo 2 llamadas que usen el mismo prefijo. OpenAI lanzó Prompt Caching en 2024 de forma automática: prefijos de 1.024+ tokens se cachean sin configuración explícita y se cobran a 50% del precio de entrada; el caching es automático para conversaciones multi-turno donde el historial acumulado es el prefix. La condición para que el caching sea efectivo es que el prefijo cacheado sea textualmente idéntico entre llamadas y que el token count del prefijo supere el mínimo (1.024 tokens en OpenAI, 1.024 en Anthropic); estructurar el prompt con las instrucciones estáticas al inicio y la parte variable al final maximiza el cache hit rate.

## Aspectos técnicos del prompt caching

- Estructura de prompt optimizada para caching: `[system prompt estático - 2.000 tokens][documentos de referencia fijos - 5.000 tokens]` marcados con `cache_control` en Anthropic, seguidos de `[query variable del usuario]`; el prefijo de 7.000 tokens se cachea y la query de 50 tokens es lo único que varía entre llamadas
- Cache hit rate y su monitoreo: en la respuesta del API de Anthropic, el campo `usage.cache_read_input_tokens` indica cuántos tokens vinieron del caché; monitorear este campo como métrica operativa con alerta cuando la tasa de cache hits cae por debajo del expected
- Casos de uso de mayor ahorro: asistentes con system prompt largo (instrucciones de empresa, reglas de negocio, ejemplos few-shot), sistemas RAG donde el documento de referencia es fijo por sesión, y sistemas de análisis de documentos donde el documento se envía múltiples veces en la misma sesión
- TTL del caché y renovación: en Anthropic, el caché dura 5 minutos desde el último uso; para sesiones largas, estructurar el sistema para garantizar llamadas regulares al mismo endpoint dentro de la ventana de 5 minutos renueva el TTL automáticamente
- Google Gemini context caching: API separada `CachedContent.create()` que almacena el contenido en la nube con un mínimo de 4.096 tokens y un TTL configurable; el costo de almacenamiento es $1/millón de tokens por hora, con precio de generación reducido que varía por modelo

## Para recordar

El prompt caching es la optimización de costo de mayor impacto para sistemas con system prompts o contextos documentales largos y repetitivos; habilitarlo puede reducir el costo de las llamadas en un 40-80% sin ningún cambio en la calidad de las respuestas.
