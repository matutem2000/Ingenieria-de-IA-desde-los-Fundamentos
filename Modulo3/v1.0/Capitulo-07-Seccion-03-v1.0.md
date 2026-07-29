# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 03 — Function Calling y Tool Calling

La terminología en torno a los mecanismos de invocación de herramientas en modelos de lenguaje es inconsistente entre proveedores. OpenAI introdujo el término *function calling* en 2023. Anthropic usa *tool use*. La industria más ampliamente adoptó *tool calling* como término genérico. El resultado es que los desarrolladores a menudo trabajan con tres términos que refieren a variantes del mismo mecanismo, con diferencias de implementación que importan cuando se integran sistemas o se migran entre proveedores.

Esta sección establece qué significa cada término, cómo funciona el mecanismo técnico en concreto y qué decisiones de diseño se derivan de las diferencias entre implementaciones.

### El mecanismo común

Independientemente del nombre que usa cada proveedor, el mecanismo tiene la misma estructura conceptual:

1. El desarrollador define las herramientas disponibles como un esquema estructurado (nombre, descripción, parámetros con tipos y validaciones).
2. El esquema se incluye en la solicitud al modelo junto con el mensaje del usuario.
3. El modelo, en lugar de (o además de) generar texto, puede generar una solicitud de invocación estructurada: un objeto JSON que indica qué herramienta invocar y con qué argumentos.
4. La aplicación intercepta esa solicitud, ejecuta la herramienta real, obtiene el resultado.
5. El resultado se devuelve al modelo como parte del contexto.
6. El modelo continúa generando a partir de ese resultado.

Lo que diferencia a los proveedores no es la lógica general, sino el formato exacto de los mensajes, el esquema de definición de herramientas y los modos de control disponibles.

### Definición de herramientas en JSON Schema

El formato para definir una herramienta sigue el estándar JSON Schema para los parámetros. La definición tiene tres campos esenciales: el nombre de la herramienta, una descripción en lenguaje natural, y el esquema de los parámetros de entrada.

El texto de la descripción es el campo más importante para el comportamiento del modelo. El modelo usa esa descripción para decidir si la herramienta es relevante y cuándo invocarla. Una descripción vaga produce invocaciones incorrectas.

A continuación se muestran dos ejemplos completos: una herramienta de consulta y una herramienta de acción.

**Ejemplo 1: herramienta de consulta (sin efectos secundarios)**

```json
{
  "name": "obtener_estado_pedido",
  "description": "Consulta el estado actual de un pedido de venta dado su número de pedido. Devuelve el estado (pendiente, en_proceso, enviado, entregado, cancelado), la fecha estimada de entrega y el número de seguimiento si el pedido ya fue enviado. Usar cuando el usuario pregunte por el estado o el progreso de un pedido específico.",
  "input_schema": {
    "type": "object",
    "properties": {
      "numero_pedido": {
        "type": "string",
        "description": "Número de pedido en formato alfanumérico, por ejemplo 'PED-2024-00123'."
      }
    },
    "required": ["numero_pedido"]
  }
}
```

Esta herramienta es idempotente: invocarla diez veces con el mismo número de pedido devuelve el mismo resultado (o el estado actualizado al momento de la consulta). No modifica ningún dato. Puede ejecutarse automáticamente sin requerir confirmación del usuario.

**Ejemplo 2: herramienta de acción (con efectos secundarios)**

```json
{
  "name": "cancelar_pedido",
  "description": "Cancela un pedido de venta que aún no haya sido enviado. Esta acción es irreversible: una vez cancelado, el pedido no puede reactivarse y se inicia automáticamente el proceso de reembolso si el pago ya fue procesado. Usar únicamente cuando el usuario solicite explícitamente cancelar un pedido específico y haya confirmado la acción.",
  "input_schema": {
    "type": "object",
    "properties": {
      "numero_pedido": {
        "type": "string",
        "description": "Número de pedido a cancelar, en formato 'PED-YYYY-NNNNN'."
      },
      "motivo": {
        "type": "string",
        "description": "Motivo de la cancelación para el registro interno. Valores válidos: 'cambio_de_opinion', 'error_en_pedido', 'demora_excesiva', 'otro'.",
        "enum": ["cambio_de_opinion", "error_en_pedido", "demora_excesiva", "otro"]
      }
    },
    "required": ["numero_pedido", "motivo"]
  }
}
```

Esta herramienta tiene efectos secundarios irreversibles. La descripción lo indica explícitamente para que el modelo tenga esa información al razonar sobre cuándo invocarla. La sección 07 desarrolla los controles de seguridad que deben acompañar a herramientas de este tipo.

### Diferencias entre proveedores

**Anthropic (tool use).** Las herramientas se definen en el campo `tools` del request. El campo de descripción del parámetro es `description` dentro de cada propiedad del schema. Cuando el modelo decide invocar una herramienta, el mensaje de respuesta tiene `stop_reason: "tool_use"` y el contenido incluye un bloque de tipo `tool_use` con el nombre de la herramienta y los argumentos. El resultado de la herramienta se devuelve como un bloque de tipo `tool_result` en el turno siguiente.

```python
import anthropic

client = anthropic.Anthropic()

herramientas = [
    {
        "name": "obtener_estado_pedido",
        "description": "Consulta el estado actual de un pedido dado su número.",
        "input_schema": {
            "type": "object",
            "properties": {
                "numero_pedido": {
                    "type": "string",
                    "description": "Número de pedido en formato 'PED-YYYY-NNNNN'."
                }
            },
            "required": ["numero_pedido"]
        }
    }
]

respuesta = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    tools=herramientas,
    messages=[
        {"role": "user", "content": "¿En qué estado está mi pedido PED-2024-00456?"}
    ]
)

# Si el modelo invocó una herramienta:
if respuesta.stop_reason == "tool_use":
    for bloque in respuesta.content:
        if bloque.type == "tool_use":
            nombre = bloque.name          # "obtener_estado_pedido"
            argumentos = bloque.input     # {"numero_pedido": "PED-2024-00456"}
            id_uso = bloque.id            # identificador único de esta invocación
```

**OpenAI (function calling / tool calling).** Las herramientas se definen en el campo `tools` con un objeto `function` anidado. El campo de la función tiene `name`, `description` y `parameters` (que contiene el JSON Schema). Cuando el modelo invoca una herramienta, el campo `finish_reason` del mensaje de respuesta es `"tool_calls"` y el campo `tool_calls` contiene la lista de invocaciones. El resultado se devuelve con un mensaje de rol `"tool"`.

La diferencia principal desde el punto de vista del desarrollador no es conceptual sino de formato: los campos tienen nombres diferentes, el esquema de anidamiento es diferente, y el protocolo de devolución de resultados usa distintos roles de mensaje.

### Modos de control de la invocación

La mayoría de los proveedores ofrece un parámetro para controlar si el modelo puede invocar herramientas, debe invocar herramientas, o está obligado a elegir una específica:

- **Automático (por defecto).** El modelo decide si invoca una herramienta o genera texto directamente.
- **Forzado a usar herramientas.** El modelo debe invocar al menos una herramienta antes de responder. Útil cuando la respuesta siempre requiere datos frescos.
- **Herramienta específica.** El modelo debe invocar exactamente una herramienta determinada. Útil para estructurar la salida del modelo como un objeto validado.
- **Sin herramientas.** El modelo no puede invocar herramientas en este turno, aunque estén definidas.

En Anthropic, este control se maneja con el parámetro `tool_choice`:

```python
# Forzar al modelo a usar herramientas
tool_choice={"type": "any"}

# Forzar al modelo a usar una herramienta específica
tool_choice={"type": "tool", "name": "obtener_estado_pedido"}

# Desactivar herramientas para este turno
tool_choice={"type": "none"}
```

### Invocaciones en paralelo

Cuando una solicitud del usuario requiere información de varias herramientas independientes, los modelos más capaces pueden generar múltiples invocaciones de herramientas en un solo turno. Esto reduce la latencia total comparado con el ciclo secuencial.

Por ejemplo, si el usuario pregunta "¿cuál es el estado de mis pedidos PED-2024-001 y PED-2024-002?", el modelo puede generar dos invocaciones de `obtener_estado_pedido` en paralelo. La aplicación las ejecuta concurrentemente y devuelve ambos resultados en el turno siguiente.

La aplicación debe estar preparada para manejar múltiples bloques de invocación en un mismo turno y para devolver los resultados emparejados con sus identificadores de invocación (`tool_use_id`).

### La descripción como parte del contrato técnico

Un error frecuente en la implementación de herramientas es tratar la descripción como documentación para el desarrollador en lugar de como instrucción operativa para el modelo. El modelo lee la descripción en tiempo de ejecución. Los errores en la descripción producen errores en el comportamiento.

Principios para escribir descripciones efectivas:

- **Especificar el alcance.** Qué casos cubre la herramienta y, cuando sea relevante, qué casos no cubre.
- **Indicar cuándo invocarla.** El modelo necesita criterios para decidir entre herramientas similares.
- **Señalar efectos secundarios.** Si la herramienta modifica datos, la descripción debe decirlo.
- **Describir el formato de retorno.** Qué estructura tendrán los datos que devuelve la herramienta, para que el modelo pueda interpretar el resultado correctamente.

La sección 05 desarrolla estos principios con mayor profundidad en el contexto del diseño de herramientas robustas.
