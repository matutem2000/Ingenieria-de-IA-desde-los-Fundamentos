# Módulo 7 – Capítulo 05 – Sección 04

## Pydantic AI: agentes tipados con validación de entrada/salida

Los tres frameworks anteriores —LangGraph, AutoGen, CrewAI— abordan el problema de la coordinación y el flujo de control. Pydantic AI aborda un problema diferente y complementario: la confiabilidad de los tipos en la interfaz entre el agente y el código que lo consume. En sistemas de producción donde el output del agente alimenta directamente otros componentes del sistema —una API que espera un JSON específico, un pipeline de datos que procesa la respuesta, un formulario que se pre-llena con los resultados—, la garantía de que el output tiene el formato correcto es tan crítica como la garantía de que el contenido es correcto. Pydantic AI hace de esta garantía de tipos el principio de diseño central, no una característica adicional.

Pydantic AI es un framework de agentes desarrollado por el equipo de Pydantic que aplica la filosofía de tipado estático de Python —ya establecida en el ecosistema con modelos Pydantic para validación de datos— al dominio de los agentes. La primitiva central es el `Agent[ResultType]` donde `ResultType` es un modelo Pydantic con campos tipados: el LLM es instruido para generar output JSON que valide contra ese modelo, y si la respuesta no es válida, Pydantic AI construye automáticamente un mensaje de error descriptivo y reintenta la generación hasta `max_retries` veces antes de lanzar una excepción. Esta garantía de estructura hace que la salida del agente sea directamente deserializable a un objeto Python tipado sin transformación manual adicional.

Considerar el caso concreto de un agente de extracción de información de CVs. Con function calling directo, el desarrollador recibe una string JSON que debe parsear, validar y manejar con try/except para errores de formato. Con Pydantic AI, define:

```python
from pydantic import BaseModel
from pydantic_ai import Agent

class CandidateProfile(BaseModel):
    name: str
    years_experience: int
    skills: list[str]
    education_level: str
    current_role: str | None = None

agent = Agent(
    model="anthropic:claude-3-5-sonnet-20241022",
    result_type=CandidateProfile,
    system_prompt="Extract candidate information from the provided CV text."
)

result = await agent.run(cv_text)
profile = result.data  # tipo garantizado: CandidateProfile
```

El resultado `result.data` es una instancia `CandidateProfile` con validación automática de tipos: `years_experience` es garantizadamente un entero (no "five years" como string), `skills` es garantizadamente una lista (no un string separado por comas), y `education_level` está dentro de los valores permitidos si se define como `Literal["bachelor", "master", "phd"]`. Si el LLM genera output que no cumple el schema, Pydantic AI reintenta con un mensaje de error que incluye exactamente qué campos fallaron y por qué: "The field 'years_experience' must be an integer, but received '10+'. Please provide only the numeric value."

Las **herramientas tipadas** en Pydantic AI eliminan la necesidad de escribir JSON Schema manualmente. Las herramientas se definen como funciones Python con anotaciones de tipo estándar; Pydantic AI genera automáticamente el JSON Schema correspondiente y lo incluye en el contexto del LLM. Una herramienta de búsqueda se define como `async def search(query: str, max_results: int = 5) -> list[SearchResult]` y el framework genera el schema `{"type": "object", "properties": {"query": {"type": "string"}, "max_results": {"type": "integer", "default": 5}}, "required": ["query"]}` automáticamente. Esto elimina una fuente frecuente de bugs donde el schema documentado y la implementación de la función divergen gradualmente.

El **`RunContext` con dependency injection** es el mecanismo por el cual las herramientas y el agente acceden a servicios externos de forma type-safe. En lugar de variables globales o closures que capturan dependencias externas, el `RunContext[Dependencies]` inyecta un objeto de dependencias tipado en cada tool call: `ctx.deps.db_connection`, `ctx.deps.http_client`, `ctx.deps.config`. Este patrón hace que las herramientas sean directamente testeables pasando dependencias mock: `agent.run(input, deps=MockDependencies(db=FakeDatabase()))`.

Pydantic AI soporta los modelos principales de la industria con una interfaz unificada: `"openai:gpt-4o"`, `"anthropic:claude-3-5-sonnet-20241022"`, `"google-gla:gemini-1.5-pro"`, `"groq:llama-3.1-70b-versatile"`, y modelos locales vía `"ollama:llama3"`. El **streaming tipado** con `agent.run_stream()` devuelve eventos intermedios como objetos tipados, no texto libre: `TextPartEvent` para texto generado, `ToolCallEvent` para invocaciones de herramientas, `ToolReturnEvent` para resultados, lo que facilita construir UIs reactivas que muestran el progreso del agente con información estructurada.

## Aspectos técnicos

- **Output model typing**: `Agent[ResultType]` donde `ResultType` es un modelo Pydantic; el LLM genera output JSON que se valida y deserializa automáticamente; reintentos automáticos con mensajes de error descriptivos ante fallos de validación
- **Tool typing automático**: las herramientas se definen como funciones Python con anotaciones de tipo estándar; el JSON Schema se genera automáticamente de las anotaciones, eliminando divergencia entre schema y implementación
- **RunContext y dependency injection**: `RunContext[Dependencies]` provee acceso type-safe a servicios externos (DB, HTTP client, config); hace las herramientas directamente testeables con dependencias mock
- **Structured validation retries**: cuando el LLM genera output inválido, Pydantic AI construye un mensaje de error que especifica exactamente qué campos fallaron y por qué, y reintenta hasta `max_retries` veces antes de lanzar excepción
- **Multi-provider con interfaz unificada**: soporta OpenAI, Anthropic, Google, Groq y modelos locales (Ollama) con la misma API; cambiar de proveedor requiere modificar solo el parámetro `model`, no el código del agente

## Principio rector

Pydantic AI aplica el principio de "fail fast" a la integración agéntica: en lugar de descubrir en producción que la salida del agente no tiene el formato esperado cuando el código consumidor lanza un KeyError, la validación en tiempo de ejecución garantiza que el output es correcto antes de que llegue al código consumidor. El costo de los reintentos de validación es menor que el costo de los bugs de integración en producción.

La sección siguiente examina los criterios para elegir entre los cuatro frameworks —LangGraph, AutoGen, CrewAI, Pydantic AI— y cuándo la opción correcta es no usar ningún framework.
