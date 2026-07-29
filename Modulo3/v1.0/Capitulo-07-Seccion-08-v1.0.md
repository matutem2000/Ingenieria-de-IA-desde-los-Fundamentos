# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 08 — Integración con sistemas empresariales

La mayoría de los sistemas de IA que se construyen en organizaciones no operan en aislamiento: necesitan interactuar con los sistemas que la empresa ya tiene. Un asistente de atención al cliente necesita leer el CRM. Un copiloto de ventas necesita consultar el ERP. Un sistema de soporte interno necesita acceder a la base de conocimiento, al sistema de tickets y al calendario de disponibilidad del equipo.

Esta sección cubre los patrones prácticos para integrar modelos con los sistemas empresariales más frecuentes, las consideraciones técnicas específicas de cada tipo de sistema, y las decisiones de diseño que determinan si la integración será mantenible en el tiempo.

### El panorama de sistemas empresariales

Las categorías de sistemas con los que más frecuentemente se integran los sistemas de IA en entornos corporativos son:

**CRM (Customer Relationship Management).** Salesforce, HubSpot, Microsoft Dynamics. Almacenan información de clientes, oportunidades de venta, historial de interacciones y comunicaciones. Las herramientas típicas son: buscar cliente, consultar historial de contacto, crear oportunidad, actualizar estado de lead.

**ERP (Enterprise Resource Planning).** SAP, Oracle, Microsoft Dynamics 365. Gestionan operaciones de negocio: inventario, pedidos, facturación, cadena de suministro. Son sistemas complejos con APIs frecuentemente diseñadas para integración máquina a máquina, no para consumo por modelos de lenguaje. Las herramientas típicas son: consultar stock, crear pedido, verificar factura, consultar estado de entrega.

**Bases de datos internas.** PostgreSQL, MySQL, SQL Server, MongoDB. Son el repositorio de datos propios de la empresa. La integración directa SQL es posible pero riesgosa (una herramienta que ejecuta SQL arbitrario es un vector de inyección SQL si no se valida correctamente). La práctica recomendada es exponer operaciones predefinidas en lugar de consultas arbitrarias.

**Sistemas de tickets y soporte.** Jira, ServiceNow, Zendesk. Gestionan solicitudes, incidencias, proyectos y flujos de trabajo. Las herramientas típicas son: crear ticket, actualizar estado, asignar a responsable, buscar tickets por cliente.

**Plataformas de comunicación.** Slack, Microsoft Teams, correo electrónico. Las herramientas de comunicación son de alto impacto: enviar un mensaje en nombre del usuario o enviar un correo puede tener consecuencias que el usuario no anticipó. Requieren controles de confirmación.

**Calendarios y agendas.** Google Calendar, Microsoft Outlook Calendar. Las herramientas típicas son: verificar disponibilidad, crear evento, modificar o cancelar cita.

**Plataformas en la nube.** AWS, Azure, GCP. Herramientas para gestionar recursos de infraestructura. Son de muy alto impacto: crear o eliminar recursos en la nube puede tener costos significativos y consecuencias difícilmente reversibles.

### Patrones de integración por tipo de sistema

**Integración via API REST.** La mayoría de los sistemas empresariales modernos exponen una API REST. La herramienta es un wrapper que llama a los endpoints correspondientes, maneja la autenticación y transforma la respuesta al formato esperado por el modelo.

```python
import httpx

async def buscar_cliente_crm(nombre: str = None, email: str = None) -> str:
    """
    Busca un cliente en el CRM por nombre o email.
    Devuelve los datos del cliente y su historial reciente de interacciones.
    """
    if not nombre and not email:
        return json.dumps({"exito": False, "error": "Se requiere nombre o email para buscar."})

    params = {}
    if nombre:
        params["q"] = nombre
    if email:
        params["email"] = email

    async with httpx.AsyncClient(timeout=3.0) as client:
        try:
            response = await client.get(
                f"{CRM_BASE_URL}/api/v2/contacts/search",
                params=params,
                headers={"Authorization": f"Bearer {CRM_API_TOKEN}"}
            )
            response.raise_for_status()
            datos = response.json()

            if not datos.get("contacts"):
                return json.dumps({"exito": False, "error": f"No se encontraron clientes con los criterios dados."})

            contacto = datos["contacts"][0]
            return json.dumps({
                "exito": True,
                "cliente": {
                    "id": contacto["id"],
                    "nombre": contacto["name"],
                    "email": contacto["email"],
                    "empresa": contacto.get("company", ""),
                    "telefono": contacto.get("phone", ""),
                    "ultimo_contacto": contacto.get("last_activity_date", ""),
                    "propietario": contacto.get("owner_name", "")
                }
            })
        except httpx.TimeoutException:
            return json.dumps({"exito": False, "error": "timeout", "sugerencia": "El CRM no respondió. Intentar en unos momentos."})
        except httpx.HTTPStatusError as e:
            return json.dumps({"exito": False, "error": f"Error del CRM: {e.response.status_code}"})
```

**Integración via SDK del proveedor.** Muchos sistemas tienen SDKs oficiales que simplifican la integración. La herramienta usa el SDK en lugar de llamadas HTTP directas. El SDK maneja reintentos, autenticación y serialización.

**Integración via base de datos.** Para bases de datos internas, la práctica recomendada es definir herramientas que encapsulan consultas predefinidas en lugar de exponer acceso SQL genérico:

```python
async def obtener_metricas_ventas(periodo: str, zona: str = "todas") -> str:
    """
    Consulta las métricas de ventas para un período específico.
    Período: 'hoy', 'semana', 'mes', 'trimestre'. Zona: código de zona o 'todas'.
    """
    # Consulta parametrizada, no SQL dinámico
    query = """
        SELECT
            SUM(monto_total) as total_ventas,
            COUNT(*) as cantidad_pedidos,
            AVG(monto_total) as ticket_promedio
        FROM pedidos
        WHERE fecha_creacion >= %s
          AND (%s = 'todas' OR zona = %s)
          AND estado NOT IN ('cancelado')
    """
    fecha_inicio = calcular_fecha_inicio(periodo)
    async with db_pool.acquire() as conn:
        row = await conn.fetchrow(query, fecha_inicio, zona, zona)
        return json.dumps({
            "exito": True,
            "periodo": periodo,
            "zona": zona,
            "metricas": {
                "total_ventas": float(row["total_ventas"] or 0),
                "cantidad_pedidos": row["cantidad_pedidos"],
                "ticket_promedio": float(row["ticket_promedio"] or 0)
            }
        })
```

### Gestión de credenciales y autenticación

Las herramientas que acceden a sistemas externos necesitan credenciales. Esas credenciales no deben estar hardcodeadas en el código ni en las definiciones de herramientas. Las prácticas estándar:

- **Variables de entorno:** para configuraciones locales y de desarrollo.
- **Gestores de secretos:** AWS Secrets Manager, Azure Key Vault, HashiCorp Vault para entornos de producción.
- **Credenciales de corta duración:** usar tokens con expiración en lugar de claves de API permanentes cuando los sistemas lo soporten.
- **Rotación de credenciales:** las credenciales de larga duración deben rotarse periódicamente. El código de integración debe manejar el escenario de credencial expirada y renovarla sin interrumpir la interacción.

### La capa de abstracción de herramientas

Un antipatrón frecuente en integraciones empresariales es construir herramientas que replican exactamente la estructura de la API del sistema subyacente. Si la API del CRM tiene un endpoint `/api/v2/contacts/{id}/activities` con veinte parámetros de filtrado, no tiene sentido exponer al modelo una herramienta con esos mismos veinte parámetros.

Las herramientas deben abstraer la complejidad del sistema subyacente y exponer operaciones con semántica de negocio. En lugar de reflejar la API técnica, exponer acciones del negocio:

- No: `get_contact_activities(contact_id, activity_type, start_date, end_date, limit, offset, sort_field, sort_direction, include_deleted, ...)`
- Sí: `obtener_historial_cliente(cliente_id, periodo="ultimo_mes")` con un set de parámetros mínimo y defaults razonables.

La herramienta abstrae las decisiones técnicas de la API subyacente. El modelo trabaja con la semántica del negocio, no con los detalles de la API.

### Manejo de sistemas legados

Los sistemas legados son una realidad en la mayoría de las organizaciones. Un ERP instalado hace quince años puede no tener API REST, puede exponer solo servicios SOAP, o puede requerir integración a través de archivos de intercambio. Integrar un modelo con estos sistemas requiere una capa de adaptación que traduce entre la interfaz moderna que el modelo espera y el protocolo que el sistema legado entiende.

En muchos casos, la capa MCP descrita en la sección 02 es la solución correcta: un servidor MCP que encapsula la complejidad de la integración con el sistema legado y expone las herramientas a través del protocolo estándar.

Cuando el sistema legado no tiene ninguna forma de integración programática, la única alternativa es RPA (Robotic Process Automation): software que simula la interacción de un usuario humano con la interfaz del sistema. Esta es la opción de mayor fragilidad y menor recomendable, pero puede ser la única disponible para sistemas verdaderamente cerrados.

### Consideraciones de latencia y SLA

Cada llamada a un sistema externo agrega latencia a la interacción. Si un usuario espera una respuesta en menos de cinco segundos y la herramienta tarda tres segundos en obtener datos del ERP, el margen para el resto de la interacción es mínimo.

Las estrategias para gestionar la latencia en integraciones empresariales:

**Caché de datos frecuentes.** Los datos que cambian poco (listas de productos, configuraciones, datos maestros de clientes) pueden cachearse con un TTL apropiado para evitar llamadas repetidas a sistemas lentos.

**Invocación paralela.** Cuando una interacción necesita datos de múltiples sistemas, invocar las herramientas en paralelo en lugar de en secuencia.

**Degradación elegante.** Si un sistema externo no responde dentro del timeout, el modelo debe poder continuar con la información disponible y comunicar al usuario que algunos datos no están disponibles temporalmente, en lugar de fallar completamente.

**Monitoreo de SLA de herramientas.** Registrar el tiempo de respuesta de cada herramienta permite identificar cuáles están degradando la experiencia del usuario y priorizar mejoras.
