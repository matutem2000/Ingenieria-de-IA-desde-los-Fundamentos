# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 02 — Model Context Protocol (MCP)

Cuando un equipo de ingeniería construye un asistente de IA con acceso a diez herramientas externas, el código que conecta el modelo con esas herramientas tiende a crecer en todas las direcciones. Hay lógica para formatear definiciones de herramientas, lógica para autenticar las llamadas a cada API, lógica para transformar los resultados al formato que el modelo espera, y lógica para manejar los errores de cada servicio. Cada herramienta nueva multiplica esa complejidad.

Model Context Protocol (MCP) es una respuesta a ese problema. Es un protocolo abierto, publicado por Anthropic en 2024, que define un estándar para que los modelos de lenguaje descubran y usen herramientas a través de servidores especializados. En lugar de integrar cada herramienta directamente en el código de la aplicación, el equipo construye o usa servidores MCP que exponen herramientas a través de una interfaz común. El cliente — la aplicación que usa el modelo — habla con cualquier servidor MCP usando el mismo protocolo.

### El problema que MCP resuelve

Para entender por qué MCP existe, conviene contrastar dos enfoques de integración.

**Integración directa.** La aplicación define las herramientas en su propio código, las registra en el cliente de la API del modelo, y gestiona toda la lógica de ejecución. Si el equipo quiere agregar acceso a Slack, escribe código que llama a la API de Slack, maneja la autenticación OAuth, transforma los mensajes al formato esperado y registra las herramientas en el cliente. Si quiere agregar acceso a GitHub, repite el proceso. Si un tercer sistema necesita acceder a las mismas herramientas, duplica el código o crea una capa compartida.

**Integración con MCP.** Existe un servidor MCP para Slack que cualquier cliente compatible puede descubrir y usar. El equipo configura el cliente para conectarse al servidor, y el servidor expone las herramientas disponibles (leer mensajes, enviar mensajes, buscar canales) a través del protocolo. Si el equipo quiere integrar GitHub, conecta el cliente al servidor MCP de GitHub. Si un tercer sistema necesita acceso a las mismas herramientas, apunta al mismo servidor.

La diferencia es el locus de la integración: con MCP, la lógica de cada herramienta vive en el servidor correspondiente, no en cada aplicación que la usa.

### Arquitectura del protocolo

MCP define tres componentes principales:

**Cliente MCP.** Es la aplicación que usa el modelo. Puede ser un IDE con asistente integrado, una aplicación de chat empresarial o un sistema de automatización. El cliente se conecta a uno o varios servidores MCP y, a través del protocolo, descubre qué herramientas están disponibles.

**Servidor MCP.** Es el componente que expone las herramientas. Puede ser un proceso local en la misma máquina o un servicio remoto. El servidor implementa el protocolo y expone las herramientas que gestiona (por ejemplo, leer y escribir archivos del sistema, consultar una base de datos, hacer llamadas a una API externa).

**Protocolo.** Define los mensajes que el cliente y el servidor intercambian: cómo el cliente solicita la lista de herramientas disponibles, cómo el servidor las describe, cómo el cliente solicita la ejecución de una herramienta y cómo el servidor devuelve el resultado. El transporte puede ser una conexión estándar de entrada/salida (para servidores locales) o HTTP con Server-Sent Events (para servidores remotos).

El flujo básico es:

1. El cliente establece conexión con el servidor.
2. El cliente solicita la lista de herramientas disponibles (`tools/list`).
3. El servidor devuelve las descripciones de las herramientas en formato JSON Schema.
4. El cliente incluye esas descripciones en el contexto enviado al modelo.
5. Cuando el modelo genera una invocación de herramienta, el cliente envía la solicitud al servidor (`tools/call`).
6. El servidor ejecuta la herramienta y devuelve el resultado.
7. El cliente incorpora el resultado al contexto y continúa la interacción.

### Estructura de un servidor MCP mínimo

Un servidor MCP implementa, como mínimo, dos endpoints del protocolo: `tools/list` para exponer la lista de herramientas disponibles, y `tools/call` para ejecutarlas. A continuación se muestra la estructura de un servidor MCP básico en Python usando el SDK oficial:

```python
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

app = Server("servidor-inventario")

@app.list_tools()
async def listar_herramientas():
    return [
        Tool(
            name="consultar_stock",
            description=(
                "Consulta el stock disponible de un producto en el almacén. "
                "Devuelve la cantidad en unidades y la ubicación en el almacén."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "sku": {
                        "type": "string",
                        "description": "Identificador único del producto (SKU)."
                    }
                },
                "required": ["sku"]
            }
        )
    ]

@app.call_tool()
async def ejecutar_herramienta(name: str, arguments: dict):
    if name == "consultar_stock":
        sku = arguments["sku"]
        # Aquí iría la llamada real a la base de datos del inventario
        resultado = {"sku": sku, "cantidad": 142, "ubicacion": "Pasillo B, Estante 3"}
        return [TextContent(type="text", text=str(resultado))]
    raise ValueError(f"Herramienta desconocida: {name}")

async def main():
    async with stdio_server() as streams:
        await app.run(*streams)

if __name__ == "__main__":
    asyncio.run(main())
```

Este servidor puede ejecutarse como un proceso local y conectarse a cualquier cliente compatible con MCP. El cliente descubre la herramienta `consultar_stock`, la incluye en el contexto del modelo, y el modelo puede invocarla cuando el usuario pregunta por disponibilidad de un producto.

### Capacidades adicionales del protocolo

Además de herramientas, MCP define dos capacidades que los servidores pueden exponer:

**Recursos.** Contenido que el servidor puede proveer para incorporar al contexto: documentos, configuraciones, código fuente, datos de referencia. A diferencia de las herramientas, los recursos son lectura directa de contenido, no invocaciones con parámetros.

**Prompts.** Plantillas de instrucción que el servidor puede proveer al cliente para estructurar interacciones comunes. Un servidor de base de datos puede exponer una plantilla de prompt para consultas analíticas; un servidor de código puede exponer una para revisión de código.

En la práctica, la mayoría de los servidores MCP implementa herramientas. Los recursos y prompts son capacidades opcionales del protocolo.

### Ecosistema actual

Al momento de escribir este capítulo, existe un ecosistema creciente de servidores MCP mantenidos por la comunidad y por proveedores: servidores para sistemas de archivos, Git, bases de datos (SQLite, PostgreSQL), servicios de productividad (Google Drive, Slack, GitHub), y plataformas en la nube. El cliente más usado es Claude Desktop, aunque el protocolo es agnóstico al modelo.

Desde el lado de los modelos, la compatibilidad con MCP depende del cliente que envuelve al modelo, no del modelo en sí. El modelo recibe las descripciones de herramientas en el formato estándar de la API del proveedor y genera invocaciones de la misma manera que lo haría con herramientas definidas directamente en la aplicación.

### Nota del arquitecto

MCP no elimina la complejidad de la integración: la desplaza del código de la aplicación al servidor. Construir un servidor MCP para un sistema legado con una API inconsistente puede ser tan complejo como integrarlo directamente. La diferencia es que esa complejidad queda encapsulada en un lugar, puede compartirse entre múltiples clientes y puede mantenerse de forma independiente.

MCP justifica su adopción cuando:
- Múltiples aplicaciones necesitan acceder a las mismas herramientas.
- El equipo quiere usar servidores MCP de terceros sin reescribir código de integración.
- La organización quiere establecer un estándar uniforme para la exposición de herramientas.

MCP no justifica su complejidad adicional cuando:
- Una sola aplicación necesita tres o cuatro herramientas simples.
- El equipo tiene control total sobre el código de integración y no necesita compartirlo.
- Los tiempos de latencia del transporte de red son un factor crítico.

Como cualquier capa de abstracción, MCP tiene un costo. Evaluarlo honestamente antes de adoptarlo es parte del trabajo del AI Engineer.
