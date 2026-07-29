# Módulo 10 – Capítulo 07 – Sección 01

# LLM Gateway: capa de proxy centralizada para gestionar todo el tráfico hacia modelos

Un LLM Gateway es un servicio de proxy inverso especializado que se interpone entre las aplicaciones clientes y los proveedores de modelos (OpenAI, Anthropic, Azure OpenAI, modelos self-hosted en vLLM o TGI), proveyendo un punto de control centralizado para todo el tráfico de inferencia de la organización. Al igual que un API Gateway tradicional (Kong, AWS API Gateway, Apigee) gestiona el tráfico HTTP hacia microservicios, el LLM Gateway gestiona las llamadas a modelos de lenguaje añadiendo funcionalidades específicas de IA: routing inteligente entre modelos según criterios de costo/latencia/calidad, caching semántico de respuestas similares, rate limiting por equipo o proyecto, auditoría completa de prompts y respuestas, y transformación de la API para presentar una interfaz unificada independientemente del proveedor backend. Implementaciones open source como LiteLLM Proxy, PortKey, y OpenRouter implementan este patrón, mientras que empresas como Netflix, Uber y Stripe han documentado sus implementaciones propietarias. La ventaja principal del LLM Gateway es operacional: en lugar de que cada aplicación gestione sus propias API keys, retry logic, fallback a modelos alternativos y logging de llamadas, toda esa lógica se centraliza en el gateway y los equipos de desarrollo solo consumen un endpoint interno unificado.

## Componentes principales del LLM Gateway

- Proxy layer: recibe requests en formato OpenAI API-compatible (`/v1/chat/completions`), los transforma al formato del proveedor backend seleccionado, y normaliza la respuesta a un formato unificado
- Authentication y authorization: valida tokens JWT o API keys internas, mapea cada cliente al equipo/proyecto correspondiente para atribución de costos y aplicación de políticas de rate limiting
- Router: selecciona el modelo y proveedor backend según la política configurada (menor latencia, menor costo, mayor calidad, modelo específico requerido por el cliente)
- Audit logger: registra inmutablemente cada request con timestamp, cliente, modelo usado, tokens de input/output, latencia, costo estimado, y un hash del prompt (o el prompt completo si la política de retención lo permite)
- Fallback handler: en caso de error del proveedor primario (rate limit, timeout, error 5xx), reintenta automáticamente con el proveedor secundario configurado, transparentemente para el cliente

## Para recordar

Sin un LLM Gateway centralizado, cada equipo gestiona su propia lógica de retry, fallback y logging de llamadas a modelos, resultando en comportamientos inconsistentes, dificultad de auditoría y imposibilidad de optimizar el costo de inferencia a nivel de organización.
