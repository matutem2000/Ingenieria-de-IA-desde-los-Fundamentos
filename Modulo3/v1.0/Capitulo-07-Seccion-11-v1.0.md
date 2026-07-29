# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 11 — Laboratorio práctico

Este laboratorio pone en práctica los conceptos del capítulo en un ejercicio concreto. El objetivo es que el estudiante defina dos herramientas con propósitos distintos — una de consulta y una de acción — las integre en un loop de ejecución funcional, y observe cómo el modelo las invoca para responder una solicitud real. El ejercicio incluye el manejo deliberado de un error de herramienta para ejercitar la respuesta del modelo ante fallos.

### Objetivo del laboratorio

Al completar este laboratorio, el estudiante habrá:

1. Definido dos herramientas con JSON Schema completo y descripciones operativas efectivas.
2. Implementado el loop de ejecución con herramientas.
3. Observado la secuencia de invocaciones del modelo para una solicitud multi-paso.
4. Gestionado un error de herramienta y verificado el comportamiento del modelo ante él.

### Requisitos previos

- Python 3.10 o superior instalado.
- Cuenta activa en la API de Anthropic con acceso al modelo `claude-haiku-3-5` (el más económico para práctica).
- Variable de entorno `ANTHROPIC_API_KEY` configurada.
- Librería `anthropic` instalada: `pip install anthropic`.

### Descripción del escenario

Construirás un asistente de inventario básico para un almacén ficticio. El asistente puede:

1. Consultar el stock de un producto por su código SKU.
2. Actualizar la cantidad en stock de un producto (simulando una recepción de mercadería).

Los datos del inventario se almacenarán en un diccionario en memoria para simplificar el laboratorio. No se requiere una base de datos real.

### Paso 1: configurar el inventario de prueba

```python
# inventario_lab.py

import json
import anthropic

# Inventario en memoria (simula una base de datos)
INVENTARIO = {
    "SKU-001": {"nombre": "Teclado mecánico RGB", "cantidad": 42, "ubicacion": "A-3-2"},
    "SKU-002": {"nombre": "Monitor 27 pulgadas 4K", "cantidad": 15, "ubicacion": "B-1-1"},
    "SKU-003": {"nombre": "Auriculares inalámbricos", "cantidad": 0, "ubicacion": "A-5-4"},
    "SKU-004": {"nombre": "Webcam HD 1080p", "cantidad": 8, "ubicacion": "C-2-3"},
}
```

### Paso 2: implementar las herramientas

```python
def consultar_stock(sku: str) -> str:
    """
    Herramienta de consulta: devuelve el stock actual de un producto.
    Esta herramienta introduce un error deliberado para el SKU 'SKU-999'.
    """
    # Error deliberado: simular un SKU que causa un error interno
    if sku == "SKU-999":
        return json.dumps({
            "exito": False,
            "error": {
                "codigo": "SISTEMA_NO_DISPONIBLE",
                "mensaje": "El subsistema de inventario para productos descontinuados no está disponible en este momento.",
                "sugerencia": "Informar al usuario que este producto no puede consultarse actualmente y ofrecer consultar otro producto."
            }
        })

    producto = INVENTARIO.get(sku)
    if producto is None:
        return json.dumps({
            "exito": False,
            "error": {
                "codigo": "SKU_NO_ENCONTRADO",
                "mensaje": f"No existe ningún producto con el código '{sku}' en el sistema.",
                "sugerencia": "Verificar el código SKU con el usuario. Los SKU tienen el formato SKU-NNN."
            }
        })

    return json.dumps({
        "exito": True,
        "datos": {
            "sku": sku,
            "nombre": producto["nombre"],
            "cantidad_disponible": producto["cantidad"],
            "ubicacion": producto["ubicacion"],
            "estado": "disponible" if producto["cantidad"] > 0 else "sin_stock"
        }
    })


def actualizar_stock(sku: str, cantidad_nueva: int, motivo: str) -> str:
    """
    Herramienta de acción: actualiza la cantidad en stock de un producto.
    Registra el motivo del ajuste para trazabilidad.
    """
    if sku not in INVENTARIO:
        return json.dumps({
            "exito": False,
            "error": {
                "codigo": "SKU_NO_ENCONTRADO",
                "mensaje": f"No existe ningún producto con el código '{sku}'.",
                "sugerencia": "Verificar el SKU antes de intentar actualizar."
            }
        })

    if cantidad_nueva < 0:
        return json.dumps({
            "exito": False,
            "error": {
                "codigo": "CANTIDAD_INVALIDA",
                "mensaje": "La cantidad no puede ser negativa.",
                "sugerencia": "Usar 0 para registrar un producto sin stock."
            }
        })

    cantidad_anterior = INVENTARIO[sku]["cantidad"]
    INVENTARIO[sku]["cantidad"] = cantidad_nueva

    return json.dumps({
        "exito": True,
        "datos": {
            "sku": sku,
            "nombre": INVENTARIO[sku]["nombre"],
            "cantidad_anterior": cantidad_anterior,
            "cantidad_nueva": cantidad_nueva,
            "diferencia": cantidad_nueva - cantidad_anterior,
            "motivo": motivo
        }
    })
```

### Paso 3: definir las herramientas en formato JSON Schema

```python
HERRAMIENTAS = [
    {
        "name": "consultar_stock",
        "description": (
            "Consulta el stock disponible de un producto en el almacén dado su código SKU. "
            "Devuelve la cantidad en unidades, la ubicación física y el estado (disponible o sin_stock). "
            "Usar cuando el usuario pregunte por la disponibilidad o cantidad de un producto específico."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "sku": {
                    "type": "string",
                    "description": "Código SKU del producto, en formato SKU-NNN. Ejemplo: 'SKU-001'."
                }
            },
            "required": ["sku"]
        }
    },
    {
        "name": "actualizar_stock",
        "description": (
            "Actualiza la cantidad en stock de un producto. "
            "Usar para registrar la recepción de mercadería nueva, ajustes de inventario o corrección de errores. "
            "Esta herramienta modifica los datos del inventario de forma permanente. "
            "Confirmar la acción con el usuario antes de invocar."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "sku": {
                    "type": "string",
                    "description": "Código SKU del producto a actualizar."
                },
                "cantidad_nueva": {
                    "type": "integer",
                    "description": "Nueva cantidad en stock (valor absoluto, no incremento). Mínimo 0.",
                    "minimum": 0
                },
                "motivo": {
                    "type": "string",
                    "description": "Motivo del ajuste de stock para el registro de auditoría.",
                    "enum": ["recepcion_mercaderia", "ajuste_inventario", "correccion_error", "devolucion_cliente"]
                }
            },
            "required": ["sku", "cantidad_nueva", "motivo"]
        }
    }
]
```

### Paso 4: implementar el loop de ejecución

```python
def enrutar_herramienta(nombre: str, argumentos: dict) -> str:
    """Enruta la invocación a la función correspondiente."""
    if nombre == "consultar_stock":
        return consultar_stock(**argumentos)
    elif nombre == "actualizar_stock":
        return actualizar_stock(**argumentos)
    else:
        return json.dumps({"exito": False, "error": f"Herramienta no reconocida: {nombre}"})


def ejecutar_asistente(consulta_usuario: str, max_iteraciones: int = 10) -> str:
    """Loop de ejecución principal."""
    client = anthropic.Anthropic()

    mensajes = [{"role": "user", "content": consulta_usuario}]
    system_prompt = (
        "Eres el asistente de inventario de un almacén. "
        "Tienes acceso a herramientas para consultar y actualizar el stock de productos. "
        "Usa las herramientas para obtener información real antes de responder. "
        "Si una herramienta falla, comunica el problema al usuario de forma clara y sugiere alternativas."
    )

    for iteracion in range(max_iteraciones):
        respuesta = client.messages.create(
            model="claude-haiku-3-5",
            max_tokens=1024,
            system=system_prompt,
            tools=HERRAMIENTAS,
            messages=mensajes
        )

        print(f"\n[Iteración {iteracion + 1}] stop_reason: {respuesta.stop_reason}")

        if respuesta.stop_reason == "end_turn":
            texto = next((b.text for b in respuesta.content if hasattr(b, "text")), "")
            return texto

        if respuesta.stop_reason == "tool_use":
            mensajes.append({"role": "assistant", "content": respuesta.content})
            resultados = []
            for bloque in respuesta.content:
                if bloque.type == "tool_use":
                    print(f"  Herramienta invocada: {bloque.name}({bloque.input})")
                    resultado = enrutar_herramienta(bloque.name, bloque.input)
                    print(f"  Resultado: {resultado[:100]}...")
                    resultados.append({
                        "type": "tool_result",
                        "tool_use_id": bloque.id,
                        "content": resultado
                    })
            mensajes.append({"role": "user", "content": resultados})

    return "No se pudo completar la consulta en el número de pasos disponibles."
```

### Paso 5: ejecutar los escenarios de prueba

```python
if __name__ == "__main__":
    print("=" * 60)
    print("ESCENARIO 1: Consulta de stock normal")
    print("=" * 60)
    resultado = ejecutar_asistente("¿Cuántos teclados mecánicos tenemos en stock? El SKU es SKU-001.")
    print(f"\nRespuesta final:\n{resultado}")

    print("\n" + "=" * 60)
    print("ESCENARIO 2: Producto sin stock")
    print("=" * 60)
    resultado = ejecutar_asistente("Necesito saber si hay auriculares disponibles. SKU: SKU-003.")
    print(f"\nRespuesta final:\n{resultado}")

    print("\n" + "=" * 60)
    print("ESCENARIO 3: Error deliberado de herramienta")
    print("=" * 60)
    resultado = ejecutar_asistente("Consulta el stock del producto SKU-999.")
    print(f"\nRespuesta final:\n{resultado}")

    print("\n" + "=" * 60)
    print("ESCENARIO 4: Actualización de stock (acción con efectos)")
    print("=" * 60)
    resultado = ejecutar_asistente(
        "Recibimos 30 unidades de la webcam HD (SKU-004). "
        "Actualiza el inventario sumando esas 30 unidades a las que ya hay."
    )
    print(f"\nRespuesta final:\n{resultado}")
```

### Preguntas de reflexión

Después de ejecutar los escenarios, analiza los siguientes puntos:

1. En el escenario 3 (error deliberado), ¿cómo procesó el modelo el mensaje de error de la herramienta? ¿La "sugerencia" del error influyó en la respuesta generada al usuario?

2. En el escenario 4 (actualización de stock), el modelo debía calcular la nueva cantidad total (8 existentes + 30 nuevas = 38). ¿Invocó primero `consultar_stock` para verificar la cantidad actual antes de invocar `actualizar_stock`? Si no lo hizo, ¿qué cambio en el system prompt o en la descripción de la herramienta podría inducir ese comportamiento?

3. Si modificas la descripción de `actualizar_stock` para eliminar la frase "Esta herramienta modifica los datos del inventario de forma permanente", ¿cambia el comportamiento del modelo ante solicitudes ambiguas? Pruébalo.

4. Agrega una tercera herramienta: `listar_productos_sin_stock` que devuelva todos los SKU con cantidad igual a cero. Escribe su descripción de forma que el modelo no la confunda con `consultar_stock`. ¿Qué elementos de la descripción son clave para mantener la distinción?

### Extensión opcional

Para los estudiantes que quieran ir más allá: implementa un mecanismo de confirmación para la herramienta `actualizar_stock`. Antes de ejecutar la actualización, el loop debe interrumpirse e imprimir un mensaje de confirmación en la consola. Solo si el usuario ingresa "s" o "sí" se procede con la ejecución. Observa cómo el flujo del loop cambia con este control.
