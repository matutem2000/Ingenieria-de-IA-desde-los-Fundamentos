# Módulo 5 – Capítulo 01 – Sección 02

# APIs de modelos fundacionales: OpenAI, Anthropic, Google — estructura y autenticación

Las tres APIs dominantes del mercado —OpenAI (gpt-4o, o1), Anthropic (Claude 3.5 Sonnet/Haiku) y Google (Gemini 1.5 Pro vía Vertex AI o AI Studio)— exponen endpoints HTTP REST con autenticación mediante bearer tokens transmitidos en headers de cada request. La estructura de los mensajes varía entre proveedores: OpenAI usa un array `messages` con roles `system`, `user` y `assistant`; Anthropic separa `system` como campo de primer nivel y gestiona `messages` únicamente para el turno conversacional; Google Gemini utiliza la estructura `contents` con partes multimodales que permiten intercalar texto, imagen, audio y video en un mismo mensaje. El rate limiting se expresa en Tokens Per Minute (TPM) y Requests Per Minute (RPM) por tier de suscripción, y los errores 429 indican superación de alguno de estos límites, con el header `Retry-After` indicando el tiempo de espera. Comprender las diferencias estructurales entre APIs es crítico para construir abstracciones portables o para aprovechar las capacidades diferenciadoras de cada proveedor sin acoplamiento innecesario.

## Aspectos técnicos de las APIs principales

- OpenAI API: endpoint `https://api.openai.com/v1/chat/completions`, autenticación con header `Authorization: Bearer $OPENAI_API_KEY`, campo `model` como `gpt-4o` o `o1-preview`, tiers de rate limit desde Tier 1 (500 RPM) hasta Tier 5 (10.000 RPM) según gasto acumulado
- Anthropic API: endpoint `https://api.anthropic.com/v1/messages`, autenticación con `x-api-key: $ANTHROPIC_API_KEY` y header `anthropic-version: 2023-06-01` obligatorio en cada request, `system` como campo independiente del array `messages`
- Google Vertex AI: autenticación con OAuth2 via service account JSON o Application Default Credentials, endpoint dinámico `{region}-aiplatform.googleapis.com`, soporte nativo multimodal con `inline_data` y `file_data`
- Google AI Studio: autenticación simplificada con `x-goog-api-key` para desarrollo y pruebas, mismo modelo Gemini pero sin VPC ni controles enterprise de Vertex AI
- Códigos de error críticos: 400 (parámetros inválidos o contexto excedido), 401 (API key ausente o revocada), 422 (contenido que viola políticas de uso aceptable), 429 (rate limit), 529 (sobrecarga temporal, específico de Anthropic)

## Para recordar

Cada proveedor impone su propio contrato de autenticación y estructura de mensajes; abstraer estas diferencias en una capa de adaptador interna es más robusto que depender de wrappers de terceros para aplicaciones críticas de producción.
