# Módulo 7 – Capítulo 03 – Sección 02

# Function calling en APIs: OpenAI, Anthropic (tool_use) y Google

Las tres principales plataformas de LLMs para producción —OpenAI, Anthropic y Google— implementan function calling con diferencias en nomenclatura, estructura de respuesta y comportamiento de control de flujo que el desarrollador debe conocer para construir agentes portables. OpenAI (GPT-4o, GPT-4 Turbo) usa el campo `tools` con objetos `function` y devuelve `tool_calls` en el mensaje del asistente; Anthropic (Claude 3.5 Sonnet, Claude 3 Opus) usa el campo `tools` con bloques `tool_use` y `tool_result` en el flujo de mensajes; Google (Gemini 1.5 Pro) usa `function_declarations` dentro de `tools` y `functionCall`/`functionResponse` en los contenidos. Las tres plataformas soportan llamadas paralelas a múltiples herramientas en una sola inferencia (parallel tool use), pero con diferencias en cómo se especifica y se manejan las respuestas múltiples. Frameworks como LangChain abstraen estas diferencias mediante la clase `BaseTool` y adaptadores específicos por proveedor.

## Aspectos técnicos

- **OpenAI tool_calls**: el modelo devuelve un array `tool_calls` con id, nombre y argumentos como string JSON; el desarrollador ejecuta las funciones y devuelve resultados como mensajes con role `tool` referenciando el id
- **Anthropic tool_use**: el modelo devuelve bloques `content` de tipo `tool_use` con id, nombre e input como objeto JSON; los resultados se devuelven como bloques `tool_result` en el siguiente mensaje de usuario
- **Google functionCall**: el modelo devuelve un `Part` de tipo `functionCall` con nombre y args como struct; la respuesta se envía como `Part` de tipo `functionResponse` en el siguiente turno de usuario
- **tool_choice / forced calling**: las tres APIs permiten forzar que el modelo use una herramienta específica (`tool_choice: {type: "tool", name: "..."}` en Anthropic) o que no use ninguna (`none`); útil para garantizar formato estructurado de salida
- **Parallel tool use**: GPT-4o y Claude 3.5 Sonnet pueden invocar múltiples herramientas en una sola respuesta; reducir el número de pasos de razonamiento hasta en un 50% para tareas donde múltiples acciones son independientes entre sí

## Para recordar

La portabilidad entre proveedores de function calling no es automática: las diferencias en estructura de respuesta, manejo de herramientas paralelas y control de tool_choice requieren una capa de abstracción explícita o el uso de un framework que la proporcione.
