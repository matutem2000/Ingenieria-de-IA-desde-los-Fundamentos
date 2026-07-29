# Módulo 7 – Capítulo 07 – Sección 02

# Unit testing de herramientas individuales: mocks y comportamiento esperado

El primer nivel del testing de agentes —y el más tractable— es el unit testing de herramientas individuales: verificar que cada herramienta produce el output correcto dado un input específico, independientemente del agente que la invoca. Este nivel de testing es completamente determinista porque las herramientas son funciones Python normales sin LLM involucrado: dado `search_web(query="Python async generators")`, el test puede verificar que la función llama a la API correcta, maneja correctamente los errores HTTP, limita el número de resultados y retorna el formato esperado. El segundo aspecto del unit testing de herramientas es verificar que el agente las selecciona correctamente: dado un input de usuario, ¿el agente invoca la herramienta correcta con los parámetros correctos? Este test sí involucra el LLM y requiere mocking de las capas de ejecución para capturar la invocación sin ejecutarla realmente.

## Aspectos técnicos

- **Testing de implementación de herramienta**: tests pytest estándar sobre la función Python que implementa la herramienta; verificar happy path, error handling (HTTP 4xx/5xx, timeout, respuesta vacía), transformación del output al formato esperado por el agente, y límites de longitud de respuesta
- **Mocking de herramientas con `unittest.mock`**: usar `@patch` o `MagicMock` para reemplazar la implementación real de la herramienta durante el test del agente; capturar las llamadas a la herramienta mock y verificar que se invocó con los argumentos correctos
- **LangSmith dataset para selección de herramientas**: crear un dataset de (user_input, expected_tool, expected_args) y ejecutarlo contra el agente con herramientas mockeadas; mide la precision de selección de herramientas sin ejecutar efectos secundarios
- **Parametrización de tests**: usar `pytest.mark.parametrize` para cubrir múltiples casos de una misma herramienta (diferentes formatos de query, distintos idiomas, inputs con caracteres especiales) sin duplicar código de test
- **Contract tests**: verificar que el schema de output de la herramienta cumple el contrato esperado por el agente; usar `pydantic.TypeAdapter.validate_python()` o JSON Schema validation para verificar automáticamente el formato del output

## Buena práctica

Mantener una suite de unit tests para cada herramienta del agente que se ejecute en el CI/CD pipeline antes de cualquier despliegue; los fallos en herramientas individuales son los más fáciles de diagnosticar y los más importantes de detectar temprano.
