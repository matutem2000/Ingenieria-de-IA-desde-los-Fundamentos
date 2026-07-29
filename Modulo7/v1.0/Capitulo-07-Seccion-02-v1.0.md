# Módulo 7 – Capítulo 07 – Sección 02

## Unit testing de herramientas individuales: mocks y comportamiento esperado

El primer nivel del testing de agentes —el más tractable, el más rápido de ejecutar, y el más frecuentemente omitido— es el unit testing de herramientas individuales. Las herramientas son funciones Python normales con una interfaz bien definida: dado un input específico, producen un output determinista. Esta propiedad hace que su testing sea completamente análogo al unit testing de software convencional, sin la complejidad del no-determinismo ni de los efectos secundarios del ciclo agéntico completo. Los bugs encontrados a este nivel son los más económicos de corregir: el stack trace indica exactamente qué línea falló, la reproductibilidad es perfecta, y la corrección no requiere re-ejecutar todo el pipeline agéntico.

El **testing de implementación de herramienta** verifica que la función Python que implementa la herramienta produce el output correcto ante diferentes inputs. Para la herramienta de búsqueda web `search_web(query: str, max_results: int) -> list[SearchResult]`, los tests mínimos deben cubrir: el happy path con una query típica que devuelve resultados válidos, el manejo de errores HTTP (4xx, 5xx) con retornos de error informativos, el comportamiento ante respuesta vacía de la API (sin resultados), la transformación correcta del formato raw de la API al formato `SearchResult` esperado por el agente, y el cumplimiento del límite `max_results` en el output. Estos tests usan `unittest.mock.patch` para sustituir las llamadas HTTP reales por respuestas predefinidas, lo que los hace rápidos (sin latencia de red) y repetibles.

```python
import pytest
from unittest.mock import patch, MagicMock
from myagent.tools import search_web, SearchResult

def test_search_web_happy_path():
    mock_response = {"results": [
        {"title": "Test Title", "url": "https://example.com", "content": "Test content"}
    ]}
    with patch("myagent.tools.tavily_client.search", return_value=mock_response):
        results = search_web(query="test query", max_results=5)
    assert len(results) == 1
    assert isinstance(results[0], SearchResult)
    assert results[0].url == "https://example.com"

def test_search_web_api_error():
    with patch("myagent.tools.tavily_client.search", side_effect=Exception("API timeout")):
        results = search_web(query="test query", max_results=5)
    assert results == []  # graceful degradation, no exception propagated

@pytest.mark.parametrize("max_results", [1, 3, 5])
def test_search_web_respects_max_results(max_results):
    mock_response = {"results": [{"title": f"Result {i}", "url": f"https://example.com/{i}", "content": ""} for i in range(10)]}
    with patch("myagent.tools.tavily_client.search", return_value=mock_response):
        results = search_web(query="test", max_results=max_results)
    assert len(results) <= max_results
```

El **testing de selección de herramientas** verifica que el agente invoca la herramienta correcta dado un input del usuario. Este test sí involucra el LLM pero mockea la capa de ejecución de herramientas para capturar la invocación sin ejecutarla. La herramienta mock registra el nombre de la herramienta invocada y los argumentos, permitiendo assertions del tipo: "dado que el usuario preguntó por información actual sobre una empresa, el agente debe invocar `search_web`, no `query_database`". Construir un dataset de 20-50 escenarios con el input del usuario y la herramienta esperada —y ejecutarlo regularmente en CI/CD— es la forma más efectiva de detectar regresiones en la selección de herramientas cuando el modelo base cambia de versión.

Los **contract tests** verifican que el schema de output de cada herramienta cumple el contrato esperado por el agente. Si el agente espera que `search_web` devuelva `list[SearchResult]` con campos `title`, `url`, y `content`, un contract test verifica que todos los outputs posibles de la herramienta cumplen ese schema. Usando `pydantic.TypeAdapter.validate_python()` o JSON Schema validation, estos tests detectan automáticamente cuando la implementación de la herramienta diverge del schema declarado —lo que ocurre frecuentemente cuando la API externa cambia su formato de respuesta sin notificación.

La **parametrización de tests** con `pytest.mark.parametrize` permite cubrir múltiples casos de una misma herramienta sin duplicar código de test. Para una herramienta de búsqueda, parametrizar con diferentes tipos de queries (queries en inglés, en español, con caracteres especiales, muy cortas, muy largas) verifica la robustez de la implementación sin escribir un test separado para cada caso. Los tests parametrizados también facilitan añadir nuevos casos de borde a medida que se descubren en producción.

## Aspectos técnicos

- **Testing de implementación**: tests pytest estándar sobre la función Python de la herramienta; cubrir happy path, error handling (HTTP 4xx/5xx, timeout, respuesta vacía), transformación de output, y cumplimiento de límites configurables
- **Mocking con unittest.mock**: `@patch` para sustituir dependencias externas (HTTP clients, DB connections) con mocks que devuelven respuestas predefinidas; tests rápidos sin latencia de red y repetibles
- **Dataset de selección de herramientas**: 20-50 escenarios (input_usuario, herramienta_esperada, argumentos_parciales); ejecutar en CI/CD ante cambios de prompt, descripción de herramienta, o modelo base; mide precisión de selección del agente
- **Contract tests**: validar que el schema de output de la herramienta cumple el contrato que el agente espera; `pydantic.TypeAdapter.validate_python()` o JSON Schema validation; detecta divergencias cuando la API externa cambia formato
- **Parametrización con pytest.mark.parametrize**: cubrir múltiples variaciones de input sin duplicar código de test; facilita añadir nuevos casos de borde descubiertos en producción

## Buena práctica

Mantener una suite de unit tests para cada herramienta del agente que se ejecute en el CI/CD pipeline antes de cualquier despliegue. Los fallos en herramientas individuales son los más fáciles de diagnosticar (stack trace directo, sin complejidad de ciclo agéntico) y los más importantes de detectar temprano, porque una herramienta rota produce fallos en cada tarea que la invoca.

La sección siguiente sube un nivel de abstracción: del testing de herramientas individuales al testing de las trayectorias completas que el agente toma para resolver una tarea.
