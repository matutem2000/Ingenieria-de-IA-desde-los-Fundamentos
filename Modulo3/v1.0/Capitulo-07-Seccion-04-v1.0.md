# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 04 — Arquitectura de integración con herramientas

Una herramienta bien definida es una condición necesaria pero no suficiente para un sistema funcional. El otro componente es la arquitectura que rodea al modelo: cómo se registran las herramientas, cómo se enruta la ejecución, cómo fluyen los resultados, y cómo se gestiona el estado entre invocaciones dentro de una interacción.

Esta sección describe los patrones arquitectónicos que sostienen los sistemas de IA con herramientas, desde la integración directa más simple hasta las arquitecturas multicapa apropiadas para entornos empresariales.

### El loop de ejecución

El componente central de cualquier sistema con herramientas es el loop de ejecución: el ciclo que itera entre el modelo y las herramientas hasta que el modelo produce una respuesta final. Este loop vive en la aplicación, no en el modelo.

```
┌─────────────────────────────────────────────────────────┐
│                    LOOP DE EJECUCIÓN                    │
│                                                         │
│  Contexto inicial ──► Modelo                            │
│                          │                              │
│                    ¿Herramienta?                        │
│                    /           \                        │
│                  Sí             No                      │
│                  │               │                      │
│            Ejecutar           Respuesta                 │
│            herramienta          final                   │
│                  │                                      │
│            Resultado al                                 │
│            contexto                                     │
│                  │                                      │
│            Modelo (loop)                                │
└─────────────────────────────────────────────────────────┘
```

La implementación mínima de este loop en Python:

```python
import anthropic
import json

client = anthropic.Anthropic()

def ejecutar_herramienta(nombre: str, argumentos: dict) -> str:
    """Enrutador de herramientas. Delega al manejador correspondiente."""
    if nombre == "obtener_estado_pedido":
        return obtener_estado_pedido(argumentos["numero_pedido"])
    elif nombre == "cancelar_pedido":
        return cancelar_pedido(argumentos["numero_pedido"], argumentos["motivo"])
    else:
        return json.dumps({"error": f"Herramienta desconocida: {nombre}"})

def run_loop(mensajes: list, herramientas: list, modelo: str = "claude-opus-4-5") -> str:
    """Loop de ejecución con herramientas."""
    while True:
        respuesta = client.messages.create(
            model=modelo,
            max_tokens=4096,
            tools=herramientas,
            messages=mensajes
        )

        # Si el modelo terminó sin invocar herramientas, devolver la respuesta
        if respuesta.stop_reason == "end_turn":
            texto = next(
                (b.text for b in respuesta.content if hasattr(b, "text")), ""
            )
            return texto

        # Si el modelo invocó herramientas, ejecutarlas y continuar
        if respuesta.stop_reason == "tool_use":
            # Agregar la respuesta del modelo al historial
            mensajes.append({"role": "assistant", "content": respuesta.content})

            # Ejecutar cada herramienta invocada y recopilar resultados
            resultados = []
            for bloque in respuesta.content:
                if bloque.type == "tool_use":
                    resultado = ejecutar_herramienta(bloque.name, bloque.input)
                    resultados.append({
                        "type": "tool_result",
                        "tool_use_id": bloque.id,
                        "content": resultado
                    })

            # Agregar los resultados al historial y continuar el loop
            mensajes.append({"role": "user", "content": resultados})
```

Este loop tiene una limitación intencionada: no tiene un máximo de iteraciones fijo en el código mostrado. En producción, siempre se añade un límite de seguridad para evitar ciclos infinitos ante comportamientos inesperados del modelo. El valor razonable depende de la aplicación, pero un límite de 10 a 20 iteraciones cubre la gran mayoría de los casos de uso prácticos.

### Patrón de integración directa

En la integración directa, la aplicación registra las herramientas en el cliente de la API, gestiona el loop de ejecución y contiene toda la lógica de las herramientas. Es el patrón más simple y el más apropiado cuando:

- El conjunto de herramientas es pequeño y estable (menos de diez herramientas).
- Una sola aplicación usa las herramientas.
- El equipo tiene control total sobre las herramientas y el cliente del modelo.

```
┌────────────────────────────────────────────────────┐
│                    APLICACIÓN                      │
│  ┌─────────────┐    ┌─────────────────────────┐   │
│  │   Cliente   │◄──►│    Herramientas         │   │
│  │  del modelo │    │  - obtener_estado_pedido│   │
│  │             │    │  - cancelar_pedido      │   │
│  └─────────────┘    │  - buscar_cliente       │   │
│                     └─────────────────────────┘   │
└────────────────────────────────────────────────────┘
                           │
                      APIs externas
                     (CRM, ERP, BD)
```

### Patrón de capa de herramientas

Cuando varias aplicaciones necesitan acceder a las mismas herramientas, o cuando la complejidad de la integración justifica encapsularla, se introduce una capa de herramientas independiente: un servicio que expone las herramientas como una API interna, y que cada aplicación invoca sin conocer los detalles de integración con los sistemas externos.

```
┌──────────────┐    ┌──────────────┐
│  Aplicación  │    │  Aplicación  │
│     Chat     │    │  Automatizac.│
└──────┬───────┘    └──────┬───────┘
       │                   │
       └─────────┬─────────┘
                 │
        ┌────────▼────────┐
        │   CAPA DE       │
        │  HERRAMIENTAS   │
        │  (servicio)     │
        └────────┬────────┘
                 │
       ┌─────────┼─────────┐
       │         │         │
      CRM       ERP       BD
```

Este patrón simplifica el mantenimiento: los cambios en la integración con el CRM se hacen en un solo lugar, no en cada aplicación.

### Patrón de herramientas como microservicios

Para organizaciones que operan ecosistemas complejos con múltiples equipos, cada familia de herramientas puede vivir como un microservicio independiente con su propio ciclo de despliegue, su propio SLA y su propio equipo responsable. El cliente del modelo agrega las herramientas disponibles consultando un registro o directorio de servicios.

Este patrón tiene la mayor complejidad operativa y se justifica cuando la escala y la separación de responsabilidades lo requieren. MCP, descrito en la sección 02, provee un protocolo estándar para este escenario.

### Gestión del contexto entre iteraciones

Cada vez que el loop devuelve un resultado de herramienta al modelo, ese resultado se convierte en parte del contexto. En interacciones largas con muchas invocaciones de herramientas, el contexto puede crecer considerablemente.

El AI Engineer debe anticipar ese crecimiento y tomar decisiones sobre qué información mantener en el contexto y qué información puede truncarse o resumirse. Los principios del capítulo 03 sobre gestión de contexto aplican directamente aquí: los resultados de herramientas recientes son más relevantes que los resultados de iteraciones tempranas, y los resultados detallados pueden reemplazarse por resúmenes cuando el espacio de contexto es limitado.

Un antipatrón frecuente es acumular todos los resultados de herramientas en el contexto sin revisión. En un sistema con múltiples herramientas de consulta, el contexto puede saturarse con datos que el modelo ya procesó y que no necesita en su forma original para generar la respuesta final.

### Registro y observabilidad

Cualquier arquitectura de producción con herramientas debe incluir registro de cada invocación: qué herramienta fue invocada, con qué argumentos, qué resultado devolvió, cuánto tiempo tardó en ejecutarse. Este registro tiene dos propósitos: diagnóstico de fallos y auditoría de comportamiento.

El diagnóstico de fallos sin registro es ciego. Cuando el sistema produce una respuesta incorrecta, la cadena de invocaciones de herramientas es la primera fuente de evidencia. Sin ese registro, el diagnóstico se reduce a suposiciones.

La auditoría es igualmente importante en entornos empresariales. Saber exactamente qué hizo el sistema con los datos del usuario, qué herramientas invocó y qué información accedió es un requisito de cumplimiento en muchas industrias reguladas.

La estructura mínima de un registro de invocación incluye: marca de tiempo, identificador de sesión, nombre de la herramienta, argumentos de entrada, resultado de salida, duración en milisegundos y, si aplica, el error que ocurrió.
