# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 10 — Caso de estudio: asistente de atención al cliente con herramientas

Este caso de estudio describe el diseño e implementación de un asistente de atención al cliente para una empresa de comercio electrónico mediana. El asistente reemplaza una parte del volumen de tickets que anteriormente requería atención humana: consultas de estado de pedidos, solicitudes de cambio de dirección de entrega, e iniciación de procesos de cancelación y devolución.

El propósito del caso es mostrar cómo los principios de las secciones anteriores se aplican en un sistema real, con las tensiones y concesiones que caracterizan a cualquier proyecto de ingeniería.

### El contexto del problema

La empresa maneja aproximadamente 3.000 tickets de soporte por día. El análisis histórico muestra que el 62% corresponde a tres categorías: consulta de estado de pedido (38%), cambio de dirección de entrega (14%) y solicitud de cancelación (10%). Estos tickets tienen tiempos de resolución promedio de entre 4 y 12 horas con el equipo humano actual, y la mayoría podría resolverse en segundos con acceso directo a los sistemas.

El objetivo del sistema es resolver automáticamente el 55% de los tickets entrantes, reducir el tiempo de resolución promedio y liberar al equipo humano para tickets complejos que requieren juicio discrecional.

### Los sistemas involucrados

El asistente necesita acceder a tres sistemas:

**Sistema de gestión de pedidos (OMS).** API REST interna con endpoints para consultar estado de pedido, listar pedidos por cliente, actualizar dirección de entrega (solo si el estado es "pendiente" o "en_proceso"), y cancelar pedidos (solo si el estado es "pendiente" o "en_proceso").

**Sistema de gestión de clientes (CRM).** Salesforce. Contiene datos del cliente: nombre, email, historial de contacto, preferencias de comunicación.

**Sistema de tickets (Helpdesk).** Zendesk. El ticket entrante se recibe desde este sistema. El asistente puede leerlo, agregar notas internas y, si resuelve el ticket, cerrarlo con una nota de resolución.

### Definición del conjunto de herramientas

El equipo define seis herramientas:

```python
HERRAMIENTAS = [
    {
        "name": "buscar_cliente_por_email",
        "description": (
            "Busca un cliente en el sistema por su dirección de correo electrónico. "
            "Devuelve el ID del cliente, nombre completo y estado de la cuenta. "
            "Usar cuando el ticket no incluya el ID del cliente pero sí el email."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Dirección de correo electrónico del cliente."}
            },
            "required": ["email"]
        }
    },
    {
        "name": "listar_pedidos_recientes",
        "description": (
            "Lista los pedidos más recientes de un cliente. "
            "Devuelve número de pedido, estado, fecha de creación y monto total. "
            "Usar para identificar el pedido al que se refiere el cliente cuando el número de pedido no está en el ticket."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "cliente_id": {"type": "string"},
                "limite": {"type": "integer", "default": 5, "description": "Máximo de pedidos a devolver. Por defecto 5."}
            },
            "required": ["cliente_id"]
        }
    },
    {
        "name": "consultar_estado_pedido",
        "description": (
            "Consulta el estado detallado de un pedido específico: estado actual, "
            "fecha estimada de entrega, número de seguimiento y transportista si fue enviado. "
            "Usar para responder preguntas sobre el progreso o ubicación de un pedido."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "numero_pedido": {"type": "string", "description": "Número de pedido en formato PED-YYYY-NNNNN."}
            },
            "required": ["numero_pedido"]
        }
    },
    {
        "name": "actualizar_direccion_entrega",
        "description": (
            "Actualiza la dirección de entrega de un pedido. "
            "Solo funciona si el pedido está en estado 'pendiente' o 'en_proceso'. "
            "Si el pedido ya fue enviado, esta herramienta devolverá un error. "
            "Verificar el estado del pedido antes de invocar."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "numero_pedido": {"type": "string"},
                "nueva_direccion": {
                    "type": "object",
                    "properties": {
                        "calle": {"type": "string"},
                        "numero": {"type": "string"},
                        "ciudad": {"type": "string"},
                        "codigo_postal": {"type": "string"},
                        "pais": {"type": "string", "default": "AR"}
                    },
                    "required": ["calle", "numero", "ciudad", "codigo_postal"]
                }
            },
            "required": ["numero_pedido", "nueva_direccion"]
        }
    },
    {
        "name": "iniciar_cancelacion_pedido",
        "description": (
            "Inicia el proceso de cancelación de un pedido. "
            "Solo disponible para pedidos en estado 'pendiente' o 'en_proceso'. "
            "Esta acción es irreversible y activa el reembolso si el pago fue procesado. "
            "Usar únicamente con confirmación explícita del cliente."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "numero_pedido": {"type": "string"},
                "motivo": {
                    "type": "string",
                    "enum": ["cambio_de_opinion", "error_en_pedido", "demora_excesiva", "otro"]
                }
            },
            "required": ["numero_pedido", "motivo"]
        }
    },
    {
        "name": "cerrar_ticket_resuelto",
        "description": (
            "Cierra el ticket de soporte marcándolo como resuelto. "
            "Usar solo cuando el problema del cliente haya sido completamente resuelto. "
            "Requiere una nota de resolución que se mostrará al cliente."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "ticket_id": {"type": "string"},
                "nota_resolucion": {"type": "string", "description": "Explicación de cómo se resolvió el problema. Máximo 500 caracteres."}
            },
            "required": ["ticket_id", "nota_resolucion"]
        }
    }
]
```

### El system prompt

```
Eres el asistente de atención al cliente de una empresa de comercio electrónico.
Tu función es resolver tickets de soporte de forma eficiente y empática.

Tienes acceso a herramientas para consultar el estado de pedidos, actualizar
direcciones de entrega e iniciar cancelaciones. Úsalas para obtener información
real antes de responder.

Reglas de operación:
- Verifica el estado del pedido antes de cualquier acción.
- Para cancelaciones e iniciar devoluciones, confirma explícitamente con el cliente
  antes de proceder.
- Si el problema requiere intervención humana (disputas complejas, problemas de pago,
  casos de fraude), escala el ticket al equipo humano sin intentar resolverlo.
- Cierra el ticket solo cuando el problema esté completamente resuelto.
- Responde en el mismo idioma en que el cliente escribió su solicitud.
```

### Una interacción completa

**Ticket entrante:**
> "Hola, necesito cancelar mi último pedido. Pedí algo pero ya no lo necesito. Mi email es cliente@ejemplo.com"

**Secuencia de ejecución:**

1. El modelo invoca `buscar_cliente_por_email(email="cliente@ejemplo.com")`
   → `{cliente_id: "CLI-4521", nombre: "Mariana Torres"}`

2. El modelo invoca `listar_pedidos_recientes(cliente_id="CLI-4521", limite=1)`
   → `{pedidos: [{numero: "PED-2024-00834", estado: "en_proceso", fecha: "2024-12-17", monto: 8750}]}`

3. El modelo genera la respuesta al cliente:

   > "Hola Mariana, encontré tu pedido más reciente: PED-2024-00834 por $8.750, actualmente en proceso de preparación.
   >
   > ¿Confirmas que deseas cancelar este pedido? Una vez cancelado, se procesará el reembolso completo a tu método de pago original en un plazo de 5 a 10 días hábiles. Esta acción no puede deshacerse."

4. El cliente responde: "Sí, cancela ese pedido por favor."

5. El modelo invoca `iniciar_cancelacion_pedido(numero_pedido="PED-2024-00834", motivo="cambio_de_opinion")`
   → `{exito: true, reembolso_iniciado: true, plazo_reembolso: "5-10 dias habiles"}`

6. El modelo invoca `cerrar_ticket_resuelto(ticket_id="ZD-98234", nota_resolucion="Cancelación del pedido PED-2024-00834 procesada por solicitud del cliente. Reembolso iniciado.")`

7. El modelo genera la respuesta final:

   > "Tu pedido PED-2024-00834 ha sido cancelado. El reembolso de $8.750 se acreditará en tu método de pago original en un plazo de 5 a 10 días hábiles. Recibirás un correo de confirmación. ¿Hay algo más en lo que pueda ayudarte?"

### Métricas del sistema en producción

Después de tres meses de operación, el sistema muestra:

- **Tasa de resolución automática:** 58% de los tickets que entran en el alcance definido (supera el objetivo de 55%).
- **Tiempo de resolución promedio:** 45 segundos (frente a 7 horas en el proceso anterior).
- **Herramienta más invocada:** `consultar_estado_pedido` (71% de las interacciones).
- **Tasa de escalación a humanos:** 12% de los tickets procesados por el sistema (casos complejos o fuera del alcance definido).
- **Satisfacción del cliente (CSAT):** 4.2/5 en tickets resueltos automáticamente, frente a 4.0/5 en tickets resueltos por humanos para los mismos tipos de solicitud.

### Lecciones del proyecto

**La confirmación antes de cancelar fue esencial.** En las primeras iteraciones de prueba sin confirmación explícita, el modelo canceló pedidos en casos donde la solicitud del cliente era ambigua (preguntar sobre la posibilidad de cancelar, no confirmar que quería cancelar). La confirmación explícita eliminó esos falsos positivos.

**Las descripciones de herramientas requirieron varias revisiones.** La descripción inicial de `listar_pedidos_recientes` y `consultar_estado_pedido` era lo suficientemente similar como para que el modelo invocara ambas en situaciones donde solo una era necesaria. Agregar en la descripción de `listar_pedidos_recientes` "Usar para identificar el pedido cuando el número no está en el ticket" y en `consultar_estado_pedido` "Usar cuando el número de pedido ya está identificado" eliminó el solapamiento.

**El sistema de logs de herramientas fue fundamental para el diagnóstico.** Cada vez que el sistema escaló un ticket cuando podría haberlo resuelto, el log de invocaciones de herramientas mostró exactamente en qué punto el modelo no tuvo la información necesaria para proceder.
