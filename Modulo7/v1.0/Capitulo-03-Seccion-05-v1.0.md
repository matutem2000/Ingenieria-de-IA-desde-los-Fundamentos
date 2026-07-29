# Módulo 7 – Capítulo 03 – Sección 05

## Estándares de herramientas: MCP y la estandarización del tool use

Las secciones anteriores de este capítulo establecieron los principios del diseño de herramientas: nombre inequívoco, descripción precisa, schema JSON Schema bien documentado, y respuesta concisa. Estos principios son necesarios pero sufren de un problema de fragmentación: cada agente, cada framework y cada equipo implementa herramientas con su propia convención de nombres, estructura de parámetros y mecanismo de transporte. Una herramienta de búsqueda web desarrollada para un agente LangGraph no es directamente reutilizable por un agente AutoGen sin adaptación manual. El Model Context Protocol (MCP) es la respuesta de la industria a este problema de fragmentación: un estándar abierto que define cómo los LLMs se comunican con herramientas externas de forma portátil, reutilizable y componible.

**MCP (Model Context Protocol)**, publicado por Anthropic en noviembre de 2024 como especificación abierta, define un protocolo de comunicación entre un cliente LLM (el agente que invoca herramientas) y un servidor MCP (el servicio que implementa las herramientas). La arquitectura es cliente-servidor: el servidor MCP expone un conjunto de herramientas con sus schemas y descripciones a través de una interfaz estándar; el cliente LLM descubre las herramientas disponibles, las incluye en el contexto del modelo, y envía los argumentos de invocación al servidor cuando el LLM decide usar una herramienta. El transporte puede ser local (stdio, para servidores MCP que corren en el mismo proceso) o remoto (HTTP/SSE, para servidores MCP expuestos como servicios independientes).

La diferencia fundamental entre MCP y el function calling directo de OpenAI o Anthropic es el nivel de abstracción. Con function calling directo, las herramientas son funciones Python definidas en el mismo proceso del agente: el desarrollador escribe la función, genera el schema JSON, y pasa ambos al modelo en cada request. Con MCP, las herramientas son servicios independientes que el agente descubre dinámicamente: en lugar de hardcodear las herramientas en el código del agente, el agente se conecta a un servidor MCP y pregunta qué herramientas están disponibles. Esto tiene consecuencias prácticas importantes para la reutilización: una herramienta de búsqueda en GitHub implementada como servidor MCP puede ser usada por cualquier agente compatible con MCP —en cualquier framework, en cualquier lenguaje— sin duplicar el código de la implementación.

Implementar un servidor MCP básico en Python requiere el paquete `mcp` del repositorio oficial de Anthropic. La estructura mínima de un servidor MCP define herramientas mediante decoradores:

```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

server = Server("my-tools-server")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="search_documentation",
            description="Busca en la documentación interna del proyecto. Usa esto cuando el usuario pregunte sobre APIs, configuración o guías de uso.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Términos de búsqueda en lenguaje natural"},
                    "max_results": {"type": "integer", "description": "Número máximo de resultados (1-10)", "default": 5}
                },
                "required": ["query"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "search_documentation":
        results = await search_internal_docs(arguments["query"])
        return [TextContent(type="text", text=format_results(results))]
```

El servidor se conecta al cliente agente mediante `stdio_server()` para el caso local o mediante HTTP para el caso remoto. LangGraph, Claude Desktop y otros clientes compatibles con MCP pueden conectarse a este servidor y obtener automáticamente la lista de herramientas disponibles sin que el desarrollador del agente necesite conocer los detalles de implementación del servidor.

Los casos donde MCP añade valor sobre function calling directo son específicos y claros. Primero, cuando el mismo conjunto de herramientas debe ser reutilizable entre múltiples agentes o proyectos: en lugar de duplicar la implementación, todos los agentes apuntan al mismo servidor MCP. Segundo, cuando el ecosistema de herramientas es grande y dinámico: los servidores MCP pueden exponer docenas de herramientas que el agente descubre en tiempo de ejecución, en lugar de tener todas hardcodeadas en el sistema prompt. Tercero, cuando las herramientas deben ser mantenidas por equipos diferentes del equipo de agentes: el servidor MCP como servicio independiente tiene su propio ciclo de vida, tests y deployments.

La **gestión de errores en herramientas MCP** sigue los mismos principios que cualquier herramienta agéntica, pero con la particularidad de que los errores de comunicación con el servidor MCP son una categoría adicional: timeout de conexión, servidor no disponible, o respuesta mal formada. El cliente MCP debe implementar reintentos con backoff exponencial para fallos de conectividad transitorios, y comunicar al agente de forma informativa cuándo el servidor no está disponible para que pueda intentar herramientas alternativas. Los mensajes de error devueltos al LLM deben incluir el tipo de fallo (error de red, error de la herramienta, timeout) y una sugerencia de acción: "El servidor de herramientas de documentación no está disponible. Considera usar la herramienta de búsqueda web como alternativa o informar al usuario que la búsqueda en documentación interna no está disponible temporalmente."

## Conceptos clave

- **MCP (Model Context Protocol)**: estándar abierto publicado por Anthropic en 2024; define la comunicación entre clientes LLM y servidores de herramientas mediante un protocolo cliente-servidor portátil entre frameworks y proveedores
- **Servidor MCP**: servicio que expone herramientas con nombre, descripción y schema JSON; el agente descubre las herramientas dinámicamente en lugar de tenerlas hardcodeadas; el transporte puede ser stdio (local) o HTTP/SSE (remoto)
- **Cliente MCP**: el componente del agente que se conecta al servidor, descubre herramientas, y envía invocaciones; soportado nativamente en Claude Desktop, LangGraph y en la API de Anthropic con el parámetro `betas: ["computer-use-2024-10-22"]`
- **Reutilización entre agentes**: el principal beneficio de MCP sobre function calling directo; una implementación de herramienta en un servidor MCP es accesible por cualquier agente compatible sin duplicar código
- **Ecosistema de servidores MCP**: la comunidad ha publicado cientos de servidores MCP pre-construidos (GitHub, Notion, Slack, PostgreSQL, filesystem, web search) disponibles como paquetes npm y PyPI; reutilizar servidores pre-construidos antes de implementar desde cero
- **Retry y graceful degradation**: los fallos de comunicación con servidores MCP son una categoría adicional de error a manejar; implementar retry con backoff para errores transitorios y comunicar claramente al agente cuando un servidor no está disponible

> **Nota del Arquitecto**: MCP resuelve un problema real de fragmentación del ecosistema, pero no es la solución correcta para todos los proyectos. Para agentes con 3-5 herramientas simples que son específicas del proyecto, function calling directo con funciones Python es más simple, más rápido de implementar, y más fácil de depurar. MCP justifica su overhead de infraestructura cuando las herramientas necesitan ser reutilizables entre proyectos o cuando el equipo de herramientas y el equipo de agentes son distintos y necesitan ciclos de vida independientes.

## Para recordar

MCP estandariza la interfaz entre LLMs y herramientas de la misma forma en que REST estandarizó la interfaz entre servicios web: no elimina la necesidad de diseñar buenas herramientas (el nombre, la descripción y el schema siguen siendo igualmente críticos), pero sí elimina la necesidad de reimplementar esa interfaz para cada combinación de agente y herramienta.

La sección siguiente cierra el capítulo sobre herramientas, articulando el principio arquitectónico que conecta el diseño de herramientas individuales con la confiabilidad del sistema agéntico completo.
