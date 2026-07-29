# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 06 — Orquestación y selección de herramientas

Cuando un sistema tiene más de unas pocas herramientas disponibles, la pregunta de diseño ya no es solo cómo ejecutar una herramienta, sino cómo el modelo selecciona la herramienta correcta entre varias opciones, en qué orden las invoca cuando necesita más de una, y cómo la aplicación que rodea al modelo gestiona esa secuencia dentro de una sola interacción.

Esta sección cubre la orquestación de herramientas en el contexto de una interacción: el modelo recibe una solicitud, determina qué herramientas necesita, las invoca en el orden que corresponde, y produce una respuesta. No cubre los ciclos de planificación multi-turno ni los sistemas en los que el modelo actúa de forma autónoma a lo largo del tiempo — esos temas se desarrollan en el capítulo 08 y el capítulo 10.

### Selección de herramientas: cómo decide el modelo

El modelo selecciona herramientas basándose en las descripciones que recibe. No tiene acceso al código, a la implementación ni a ningún otro metadato que no esté en la definición de la herramienta. Por eso, cuando hay varias herramientas disponibles, las descripciones deben ser suficientemente distintas para que el modelo pueda discriminar entre ellas.

Un conjunto de herramientas bien diseñado tiene descripciones que no se solapan. Si dos herramientas parecen hacer lo mismo según sus descripciones, el modelo elegirá arbitrariamente entre ellas — o usará ambas por si acaso.

**Señales de solapamiento problemático:**

- `buscar_cliente` y `encontrar_cliente` con descripciones similares (diferente nombre, mismo propósito percibido).
- `obtener_pedido` y `consultar_pedido` sin una distinción clara en la descripción.
- Herramientas con descripción tan genérica que aplican a casi cualquier situación.

**Estrategia:** cuando dos herramientas tienen propósitos relacionados, la descripción de cada una debe incluir una referencia explícita a cuándo preferirla frente a la otra.

### Secuenciación de herramientas

La secuenciación ocurre cuando el resultado de una herramienta determina qué herramienta invocar a continuación. El modelo gestiona esta lógica de forma natural: si la primera herramienta devuelve un identificador de cliente, el modelo puede usar ese identificador para invocar la segunda herramienta que requiere ese dato.

```
Usuario: "Cancela el pedido más reciente de la clienta Ana García."

Secuencia de invocaciones:
1. buscar_cliente(nombre="Ana García")
   → {cliente_id: "CLI-789", email: "ana@ejemplo.com"}

2. listar_pedidos_cliente(cliente_id="CLI-789", limite=1, orden="reciente")
   → {pedidos: [{numero: "PED-2024-00501", estado: "en_proceso", ...}]}

3. cancelar_pedido(numero_pedido="PED-2024-00501", motivo="cambio_de_opinion")
   → {exito: true, mensaje: "Pedido cancelado."}

Respuesta al usuario: "El pedido PED-2024-00501 de Ana García fue cancelado..."
```

En este ejemplo, el modelo realizó tres invocaciones en secuencia, cada una dependiente del resultado anterior. La aplicación no planificó esta secuencia: el modelo la determinó a partir del contenido de cada respuesta.

### Invocaciones paralelas

Cuando varias herramientas son independientes entre sí — ninguna depende del resultado de otra — el modelo puede generarlas en paralelo en un solo turno. Esto reduce la latencia total de la interacción.

```
Usuario: "¿Cuáles son los estados de los pedidos PED-001, PED-002 y PED-003?"

Turno 1 — El modelo genera tres invocaciones simultáneas:
  - obtener_estado_pedido(numero_pedido="PED-001")
  - obtener_estado_pedido(numero_pedido="PED-002")
  - obtener_estado_pedido(numero_pedido="PED-003")

La aplicación ejecuta las tres en paralelo (concurrent.futures o asyncio).

Turno 2 — El modelo recibe los tres resultados y genera la respuesta final.
```

La aplicación debe implementar ejecución concurrente para aprovechar esta capacidad. Si ejecuta las herramientas de forma secuencial aunque el modelo las generó en paralelo, la latencia real es la suma de cada herramienta en lugar de la máxima.

Implementación con asyncio:

```python
import asyncio
import json

async def ejecutar_herramienta_async(nombre: str, argumentos: dict) -> tuple:
    """Ejecuta una herramienta de forma asíncrona y devuelve (tool_use_id, resultado)."""
    # Aquí iría la lógica real de cada herramienta
    resultado = await herramienta_registry[nombre](**argumentos)
    return resultado

async def ejecutar_herramientas_en_paralelo(bloques_tool_use: list) -> list:
    """Ejecuta múltiples herramientas concurrentemente."""
    tareas = [
        ejecutar_herramienta_async(bloque.name, bloque.input)
        for bloque in bloques_tool_use
        if bloque.type == "tool_use"
    ]
    resultados = await asyncio.gather(*tareas, return_exceptions=True)

    respuestas = []
    for bloque, resultado in zip(bloques_tool_use, resultados):
        if isinstance(resultado, Exception):
            contenido = json.dumps({"exito": False, "error": str(resultado)})
        else:
            contenido = resultado
        respuestas.append({
            "type": "tool_result",
            "tool_use_id": bloque.id,
            "content": contenido
        })
    return respuestas
```

### El problema de la sobre-selección

Un error frecuente en sistemas con muchas herramientas disponibles es que el modelo invoca más herramientas de las necesarias. Si el sistema tiene treinta herramientas disponibles y el modelo percibe que varias podrían ser relevantes, puede invocar todas "por precaución".

Este comportamiento tiene dos causas principales: descripciones ambiguas que generan incertidumbre en el modelo, y demasiadas herramientas disponibles en el contexto de una sola interacción.

**Estrategia 1: cargar solo las herramientas relevantes para el contexto.** Si la interacción comienza con una consulta sobre pedidos, incluir solo las herramientas de pedidos en el contexto inicial. Las herramientas de facturación, inventario o soporte pueden cargarse si el modelo las solicita explícitamente o si la conversación deriva hacia esos temas.

**Estrategia 2: usar herramientas de enrutamiento.** Definir una herramienta inicial cuya función es clasificar la intención del usuario y devolver un conjunto reducido de herramientas relevantes. El loop de ejecución carga esas herramientas en el siguiente turno.

**Estrategia 3: instrucciones en el system prompt.** Instruir al modelo explícitamente sobre el principio de mínima invocación: "Invoca únicamente las herramientas necesarias para responder la solicitud. Si la información requerida está disponible en el contexto de la conversación, no invoques una herramienta para obtenerla de nuevo."

### Límites de iteración y condiciones de salida

El loop de ejecución debe tener un límite máximo de iteraciones para proteger el sistema ante comportamientos inesperados. Un modelo que entra en un ciclo de invocaciones repetidas — quizás porque el error de una herramienta lo lleva a intentar otra herramienta que también falla — sin un límite puede generar costos operativos significativos y dejar al usuario esperando indefinidamente.

```python
MAX_ITERACIONES = 15

def run_loop_con_limite(mensajes, herramientas, modelo):
    iteracion = 0
    while iteracion < MAX_ITERACIONES:
        respuesta = client.messages.create(...)
        iteracion += 1

        if respuesta.stop_reason == "end_turn":
            return extraer_texto(respuesta)

        if respuesta.stop_reason == "tool_use":
            # ejecutar herramientas y continuar
            ...

    # Si se alcanzó el límite, devolver una respuesta de fallback
    return "No pude completar la solicitud en el número de pasos disponibles. Por favor, reformula la pregunta."
```

El valor de MAX_ITERACIONES depende de la aplicación. Para asistentes de servicio al cliente con herramientas simples, 5 o 10 iteraciones son suficientes. Para flujos más complejos que implican encadenamiento de múltiples consultas, 15 a 20 puede ser apropiado. Valores más altos implican mayor costo y latencia potencial.

### Orquestación versus agentes: el límite del capítulo

Lo que se ha descrito en esta sección es orquestación dentro de una interacción: el modelo razona y selecciona herramientas en el marco de un único ciclo de conversación con un usuario. El loop tiene un principio claro (la solicitud del usuario) y un fin claro (la respuesta al usuario).

La orquestación de agentes — en la que múltiples modelos o ciclos de razonamiento se coordinan a lo largo del tiempo, con estado persistente entre sesiones, planificación multi-paso y control de flujo complejo — pertenece al capítulo 08. La distinción es el alcance temporal y el grado de autonomía del sistema.
