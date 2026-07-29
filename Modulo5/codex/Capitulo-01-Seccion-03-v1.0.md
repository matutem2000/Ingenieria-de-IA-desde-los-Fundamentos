# Módulo 5 – Capítulo 01 – Sección 03

# SDKs oficiales: instalación, configuración y primeras llamadas

Los SDKs oficiales de cada proveedor encapsulan la complejidad de la autenticación HTTP, la serialización JSON, el manejo de streaming Server-Sent Events (SSE) y la lógica de retry automático, reduciendo el código necesario para una primera llamada a menos de 10 líneas en Python o TypeScript. El SDK de OpenAI se instala con `pip install openai` e instancia con `client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])`, exponiendo métodos síncronos y asíncronos bajo `client.chat.completions.create(...)`. El SDK de Anthropic (`pip install anthropic`) sigue una estructura similar con `client = anthropic.Anthropic()` y `client.messages.create(...)`, con tipado estricto vía Pydantic que detecta errores de parámetros en tiempo de desarrollo. Google ofrece tanto `pip install google-generativeai` (AI Studio) como `pip install google-cloud-aiplatform` (Vertex AI), con la diferencia de que el segundo requiere autenticación con service accounts y configuración de proyecto y región antes de cualquier llamada.

## Componentes principales de los SDKs

- Gestión de autenticación: los SDKs leen la API key desde variable de entorno por convención (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`) sin requerir configuración explícita al instanciar el cliente, evitando hardcodear credenciales
- Tipado estricto y autocompletado: los SDKs modernos usan tipos generados desde OpenAPI specs, proporcionando autocompletado en VS Code o PyCharm y detectando parámetros inválidos antes de ejecutar la llamada
- Retry automático con backoff exponencial: el SDK de OpenAI reintenta hasta 2 veces por defecto con jitter; Anthropic SDK reintenta hasta `max_retries` configurables (default 2) ante errores 429 y 529
- Soporte de streaming nativo: `stream=True` en OpenAI y `stream=True` o uso de context manager `with client.messages.stream(...) as stream:` en Anthropic devuelven iteradores de eventos delta
- Configuración de timeout y base_url: ambos SDKs permiten configurar `timeout` (default 600s en OpenAI) y `base_url` para apuntar a proxies o compatibles como Azure OpenAI Service con `api_version`

## Principio rector

Usar el SDK oficial en lugar de llamadas HTTP directas reduce errores de implementación y reduce el esfuerzo necesario para adaptarse a actualizaciones compatibles del proveedor sin modificar el código de la aplicación.
