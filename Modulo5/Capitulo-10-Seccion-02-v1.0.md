# Módulo 5 – Capítulo 10 – Sección 02

# Patrones de salida: parsing estructurado, reintentos y fallbacks

El post-procesamiento de la salida del LLM transforma la respuesta textual en un formato utilizable por la aplicación: parsear JSON, validar contra un schema, extraer entidades específicas, o detectar y manejar respuestas de baja calidad antes de exponerlas al usuario. El parsing de salida estructurada con Pydantic es el patrón dominante en Python: el prompt instruye al modelo a responder en JSON con un schema específico, la respuesta se parsea con `model = MySchema.model_validate_json(response_text)`, y si el parseo falla se dispara un reintento con un prompt de corrección que incluye el error de validación: `"Tu respuesta anterior produjo este error de parseo: {error}. Corrige el JSON para que cumpla el schema."` Los modelos modernos como gpt-4o y Claude 3.5 Sonnet soportan "structured outputs" o "tool use" que garantizan JSON válido según el schema provisto, eliminando los errores de parseo sin necesidad de reintentos; usarlos cuando el proveedor lo soporta es la práctica recomendada. Los fallbacks manejan el caso donde la respuesta del LLM no puede ser parseada o no cumple los criterios de calidad después de N reintentos: devolver un valor por defecto, escalar al humano, o activar un flujo alternativo más conservador (respuesta genérica pre-definida, búsqueda en FAQ, o transferencia a agente humano).

## Componentes principales del procesamiento de salida

- Structured outputs de OpenAI: `client.beta.chat.completions.parse(response_format=MyPydanticModel, ...)` garantiza JSON válido según el schema Pydantic; usa la gramática del modelo para forzar JSON conforme al schema sin necesidad de reintento
- Tool use para extracción estructurada en Anthropic: definir un tool con el schema JSON de la respuesta esperada y el modelo responderá siempre con un `tool_use` block parseable directamente; patrón más robusto que pedir JSON libre en el content
- Retry con OutputFixingParser: si el modelo devuelve JSON inválido (común en respuestas largas o con modelos más pequeños), `OutputFixingParser.from_llm(parser=parser, llm=llm)` de LangChain reintenta automáticamente con el error de parseo incluido en el prompt de corrección
- Post-procesamiento de markdown: cuando el modelo devuelve markdown y se necesita HTML, usar `markdown.markdown(response_text)` o una librería similar en lugar de intentar parsear markdown a mano; cuando se necesita texto plano, `BeautifulSoup(html, 'html.parser').get_text()` limpia el HTML resultante
- Fallback jerárquico: definir una cadena de fallbacks ordenada por calidad y costo: (1) respuesta del modelo principal parseada correctamente, (2) reintento con modelo principal tras error de parseo, (3) respuesta del modelo de fallback (más pequeño o diferente proveedor), (4) respuesta genérica pre-definida para el tipo de query

## Para recordar

El parseo robusto de salida con reintentos y fallbacks es lo que separa un prototipo de un sistema de producción: los prototipos asumen que el LLM siempre devuelve el formato esperado; los sistemas de producción manejan explícitamente todos los casos donde eso no ocurre.
