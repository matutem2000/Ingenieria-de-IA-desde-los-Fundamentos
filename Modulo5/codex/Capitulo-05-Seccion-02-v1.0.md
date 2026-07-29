# Módulo 5 – Capítulo 05 – Sección 02

# Unit testing de componentes de IA: mocks, fixtures y boundaries

El unit testing de componentes de IA se basa en identificar los boundaries del sistema —los puntos donde el código propio interactúa con el LLM externo— y mockear esa interfaz con `pytest-mock` o `unittest.mock`, permitiendo testear toda la lógica de pre-procesamiento, construcción del prompt, post-procesamiento y manejo de errores sin hacer llamadas reales a la API. El boundary principal es la función o método que llama al SDK del proveedor: `client.messages.create()` en Anthropic o `client.chat.completions.create()` en OpenAI; mockeando este método con `mocker.patch.object(client, 'messages', ...)` o usando `respx` para mockear las llamadas HTTP a nivel de red, los tests son rápidos (<10ms), gratuitos y reproducibles. Los fixtures en pytest permiten definir datasets de ejemplos representativos: casos normales, casos límite (input vacío, input muy largo, caracteres especiales), y casos de error (el modelo devuelve JSON inválido, la API devuelve 429, timeout). La cobertura de tests en componentes de IA debe enfocarse en la lógica de Python, no en el comportamiento del modelo: el 100% de las ramas del código de parsing y validación deben tener tests, independientemente de si el LLM real produce esa salida frecuentemente.

## Conceptos clave del unit testing de IA

- Mocking del SDK: `MagicMock()` con `return_value` configurado para devolver una respuesta tipo Anthropic `Message` o OpenAI `ChatCompletion` con el texto fijo del fixture, verificando que el código de producción llama al SDK con los parámetros correctos
- Fixtures de respuestas del LLM: archivos JSON o strings en el directorio `tests/fixtures/` con respuestas representativas del modelo (JSON bien formado, JSON inválido, respuesta truncada, respuesta con caracteres especiales), cargados con `@pytest.fixture`
- Parametrize para casos múltiples: `@pytest.mark.parametrize("input,expected", [...])` permite ejecutar el mismo test con docenas de combinaciones de input/output esperado sin duplicar código de test
- Testing del manejo de errores: verificar que el código maneja correctamente `anthropic.RateLimitError`, `anthropic.APITimeoutError`, JSON inválido en la respuesta, y respuestas vacías; estos paths de error son críticos y raramente se ejercitan en tests de integración
- Test de la construcción del prompt: verificar que el prompt construido contiene las variables correctamente interpoladas, tiene la estructura de roles esperada, y no excede el límite de tokens configurado para el caso de uso

## Para recordar

El valor del unit testing en IA está en testear el código propio —constructores de prompts, parsers de respuestas, validadores de salida, lógica de retry— no el comportamiento del modelo, que es una caja negra externa fuera del control del test.
