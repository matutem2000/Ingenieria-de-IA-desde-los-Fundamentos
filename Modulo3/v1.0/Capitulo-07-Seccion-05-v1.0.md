# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 05 — Diseño de herramientas robustas

El comportamiento de un sistema con herramientas es tan bueno como el diseño de las herramientas que lo componen. Una herramienta mal diseñada no es un problema que el modelo pueda compensar: si la descripción es ambigua, el modelo la invocará en los momentos equivocados. Si el esquema de parámetros es permisivo, el modelo pasará valores que la herramienta no puede manejar. Si la herramienta falla sin devolver un error legible, el modelo no podrá razonar sobre el fallo.

El diseño de herramientas robustas combina principios de diseño de APIs con principios específicos de integración con modelos de lenguaje. Esta sección los desarrolla.

### Principio 1: una herramienta, una responsabilidad

Cada herramienta debe hacer exactamente una cosa. Una herramienta que "gestiona pedidos" — y dependiendo del parámetro `accion` consulta, modifica o cancela — es una herramienta que el modelo tendrá dificultades para usar correctamente. El modelo infiere la semántica de una herramienta a partir de su nombre y descripción. Una herramienta multipropósito con semántica ambigua produce invocaciones incorrectas.

**Mal diseño:**
```json
{
  "name": "gestionar_pedido",
  "description": "Gestiona un pedido: consulta estado, actualiza o cancela según el parámetro accion.",
  "input_schema": {
    "type": "object",
    "properties": {
      "numero_pedido": {"type": "string"},
      "accion": {"type": "string", "enum": ["consultar", "actualizar", "cancelar"]},
      "datos": {"type": "object", "description": "Datos adicionales según la acción."}
    },
    "required": ["numero_pedido", "accion"]
  }
}
```

**Buen diseño:**
```json
[
  {
    "name": "consultar_estado_pedido",
    "description": "Devuelve el estado actual de un pedido específico."
  },
  {
    "name": "actualizar_direccion_pedido",
    "description": "Cambia la dirección de entrega de un pedido que aún no fue enviado."
  },
  {
    "name": "cancelar_pedido",
    "description": "Cancela un pedido irreversiblemente. Usar solo con confirmación explícita del usuario."
  }
]
```

Tres herramientas separadas tienen nombres claros, descripciones precisas y esquemas de parámetros específicos para cada operación. El modelo puede elegir correctamente entre ellas.

### Principio 2: descripciones operativas, no documentales

La descripción de una herramienta es la instrucción operativa que el modelo lee para decidir cuándo y cómo invocarla. No es documentación para el desarrollador.

Una descripción efectiva contiene:

**El qué:** Qué hace la herramienta cuando se invoca. "Consulta el estado actual de un pedido en el sistema de gestión de órdenes."

**El cuándo:** En qué situaciones el modelo debe invocarla. "Usar cuando el usuario pregunte por el estado, la ubicación o la fecha estimada de entrega de un pedido específico."

**El qué no:** Si la herramienta tiene alcance limitado, especificarlo. "No usar para pedidos de más de 90 días: consultar el sistema de archivo histórico en su lugar."

**Los efectos secundarios:** Si la herramienta modifica datos o ejecuta acciones, indicarlo explícitamente. "Esta acción cancela el pedido de forma irreversible y activa el proceso de reembolso si el pago fue procesado."

**El formato del retorno:** Qué estructura tiene la respuesta para que el modelo pueda interpretarla. "Devuelve un objeto JSON con los campos: estado (string), fecha_estimada_entrega (ISO 8601), numero_seguimiento (string o null)."

### Principio 3: esquemas de parámetros precisos

El esquema JSON Schema de los parámetros cumple dos funciones: validar los argumentos que el modelo genera antes de pasarlos a la herramienta, y guiar al modelo sobre qué valores son válidos.

Usar tipos específicos en lugar de tipos genéricos:

```json
// Demasiado genérico
"fecha": {"type": "string", "description": "Fecha de inicio."}

// Preciso
"fecha_inicio": {
  "type": "string",
  "format": "date",
  "description": "Fecha de inicio del período a consultar, en formato ISO 8601 (YYYY-MM-DD). Ejemplo: '2024-03-15'."
}
```

Usar `enum` para parámetros con valores predefinidos:

```json
"estado_filtro": {
  "type": "string",
  "enum": ["pendiente", "en_proceso", "enviado", "entregado", "cancelado", "todos"],
  "description": "Estado de los pedidos a filtrar. Usar 'todos' para obtener pedidos en cualquier estado.",
  "default": "todos"
}
```

Marcar correctamente qué parámetros son obligatorios y cuáles son opcionales con defaults razonables:

```json
"input_schema": {
  "type": "object",
  "properties": {
    "numero_cliente": {"type": "string", "description": "Identificador único del cliente."},
    "limite": {"type": "integer", "description": "Número máximo de resultados. Por defecto: 10.", "default": 10},
    "estado_filtro": {"type": "string", "enum": ["activo", "inactivo", "todos"], "default": "activo"}
  },
  "required": ["numero_cliente"]
}
```

### Principio 4: contratos de respuesta predecibles

El modelo interpreta el resultado de una herramienta como texto en el contexto. Si ese texto tiene una estructura inconsistente — a veces un objeto JSON, a veces un string con un mensaje de error no estructurado, a veces un array — el modelo tendrá dificultades para extraer la información relevante.

Definir un contrato de respuesta fijo para cada herramienta:

```python
# Contrato de respuesta de consultar_estado_pedido
{
  "exito": True,
  "datos": {
    "numero_pedido": "PED-2024-00456",
    "estado": "enviado",
    "fecha_estimada_entrega": "2024-12-20",
    "numero_seguimiento": "TRACK-789-XYZ",
    "transportista": "DHL"
  }
}

# Contrato de error
{
  "exito": False,
  "error": {
    "codigo": "PEDIDO_NO_ENCONTRADO",
    "mensaje": "No se encontró un pedido con el número 'PED-2024-99999'.",
    "sugerencia": "Verificar que el número de pedido sea correcto."
  }
}
```

El campo `sugerencia` en los errores es especialmente valioso: le da al modelo información accionable para razonar sobre el siguiente paso. Esto se desarrolla en el siguiente principio.

### Principio 5: errores informativos para el modelo

Cuando una herramienta falla, el error que devuelve es parte del contexto del modelo. Si el error es opaco — un código de excepción del stack interno, un mensaje de HTTP 500 sin contexto — el modelo no puede razonar sobre él de manera útil.

Los errores de herramientas deben diseñarse para el modelo, no para el sistema de logs:

```python
def consultar_estado_pedido(numero_pedido: str) -> str:
    try:
        pedido = db.buscar_pedido(numero_pedido)
        if pedido is None:
            return json.dumps({
                "exito": False,
                "error": {
                    "codigo": "PEDIDO_NO_ENCONTRADO",
                    "mensaje": f"No existe un pedido con número '{numero_pedido}'.",
                    "sugerencia": "Verificar el número de pedido con el usuario o usar la herramienta buscar_pedidos_cliente para encontrar pedidos por nombre o correo electrónico."
                }
            })
        return json.dumps({"exito": True, "datos": pedido.to_dict()})
    except DatabaseTimeoutError:
        return json.dumps({
            "exito": False,
            "error": {
                "codigo": "TIMEOUT",
                "mensaje": "El sistema de pedidos no respondió en el tiempo esperado.",
                "sugerencia": "Informar al usuario que el sistema tiene demoras y ofrecer volver a intentar en unos minutos."
            }
        })
    except Exception as e:
        # Registrar el error real en los logs del sistema
        logger.error(f"Error inesperado en consultar_estado_pedido: {e}")
        return json.dumps({
            "exito": False,
            "error": {
                "codigo": "ERROR_INTERNO",
                "mensaje": "Ocurrió un error inesperado al consultar el pedido.",
                "sugerencia": "Disculparse con el usuario e informar que el problema será revisado."
            }
        })
```

Esta estructura mantiene el mensaje de error real en los logs del sistema (para el equipo de ingeniería) y entrega al modelo un error interpretable (para generar una respuesta útil al usuario).

### Principio 6: idempotencia y seguridad ante reintentos

Las herramientas de consulta son naturalmente idempotentes. Las herramientas de acción no lo son, a menos que se diseñen explícitamente para serlo.

En un sistema con herramientas, el loop de ejecución puede reintentar una herramienta si la respuesta es un timeout. Si la herramienta no es idempotente, un reintento puede producir efectos duplicados: dos correos enviados, dos registros creados, dos pagos procesados.

Para herramientas de acción, usar identificadores de idempotencia:

```python
def enviar_confirmacion_pedido(numero_pedido: str, email: str, idempotency_key: str) -> str:
    """
    Envía un correo de confirmación al cliente.
    El idempotency_key garantiza que el correo se envíe exactamente una vez
    aunque la herramienta sea invocada varias veces con la misma clave.
    """
    if redis.exists(f"email_sent:{idempotency_key}"):
        return json.dumps({"exito": True, "mensaje": "El correo ya fue enviado previamente.", "ya_enviado": True})

    resultado = email_service.send(email, pedido=numero_pedido)
    redis.set(f"email_sent:{idempotency_key}", "1", ex=86400)  # TTL de 24 horas
    return json.dumps({"exito": True, "mensaje": "Correo enviado correctamente.", "ya_enviado": False})
```

### Principio 7: timeouts y límites

Toda herramienta que realice una llamada externa debe tener un timeout explícito. Un timeout sin configurar deja el loop de ejecución bloqueado indefinidamente esperando una respuesta que puede no llegar.

El timeout debe ser coherente con el tiempo máximo de respuesta que el usuario puede esperar. Si la aplicación tiene un SLA de 5 segundos para una respuesta de chat, las herramientas que invoca deben tener timeouts significativamente menores — entre 1 y 3 segundos para herramientas críticas.

También es prudente limitar el tamaño de la respuesta de una herramienta. Un resultado de herramienta de 100.000 tokens consume espacio de contexto que perjudica el rendimiento general del sistema. Las herramientas de búsqueda y listado deben tener parámetros de paginación y devolver solo los N resultados más relevantes.
