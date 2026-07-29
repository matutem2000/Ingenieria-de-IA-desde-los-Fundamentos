# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 09 — Patrones y anti-patrones

La experiencia acumulada en el diseño de sistemas con herramientas ha identificado un conjunto de patrones recurrentes que funcionan, y un conjunto de anti-patrones recurrentes que producen sistemas frágiles, inseguros o difíciles de mantener. Esta sección los cataloga con el propósito de que el lector pueda reconocerlos en su propio trabajo.

### Patrones de diseño

**Patrón: herramienta de enrutamiento**

Cuando un sistema tiene muchas herramientas de dominios distintos (pedidos, clientes, inventario, facturación), en lugar de cargar todas en el contexto desde el inicio, se define una herramienta de enrutamiento que clasifica la intención del usuario y devuelve el subconjunto de herramientas relevantes. El loop carga esas herramientas en el siguiente turno.

```
Solicitud → Herramienta_enrutamiento("Necesito saber el estado de mi pedido")
           → {"dominio": "pedidos", "herramientas": ["consultar_estado_pedido", "rastrear_envio"]}
           → Cargar herramientas del dominio pedidos → Continuar
```

Beneficios: reduce el número de herramientas en el contexto (menos tokens, mejor selección), mejora la precisión de la elección y reduce la probabilidad de over-selection.

---

**Patrón: herramienta de verificación antes de acción**

Antes de ejecutar una herramienta de acción irreversible, se invoca una herramienta de verificación que devuelve un resumen del estado actual y confirma que la acción es válida en ese estado.

```
Usuario: "Cancela mi pedido más reciente."

1. listar_pedidos_cliente(cliente_id="CLI-789", limite=1)
   → {numero: "PED-2024-00501", estado: "en_proceso", fecha: "2024-12-18"}

2. verificar_cancelabilidad(numero_pedido="PED-2024-00501")
   → {cancelable: true, razon: "El pedido aún no fue enviado."}

3. [confirmación del usuario]

4. cancelar_pedido(numero_pedido="PED-2024-00501", motivo="cambio_de_opinion")
```

Beneficios: el modelo tiene el contexto completo antes de generar la acción, reduce errores, y el usuario recibe información relevante en la solicitud de confirmación.

---

**Patrón: respuesta estructurada via herramienta**

Cuando el sistema necesita que el modelo produzca una salida en un formato específico (un objeto JSON validado, un registro para insertar en una base de datos), se fuerza al modelo a invocar una herramienta cuya "ejecución" es simplemente capturar y validar los argumentos generados por el modelo.

```python
herramienta_extraer_datos_cliente = {
    "name": "registrar_solicitud",
    "description": "Registra los datos estructurados de la solicitud del cliente.",
    "input_schema": {
        "type": "object",
        "properties": {
            "tipo_solicitud": {"type": "string", "enum": ["reclamo", "consulta", "devolucion"]},
            "prioridad": {"type": "string", "enum": ["alta", "media", "baja"]},
            "descripcion_breve": {"type": "string", "maxLength": 200},
            "numero_pedido_afectado": {"type": "string", "description": "Si aplica."}
        },
        "required": ["tipo_solicitud", "prioridad", "descripcion_breve"]
    }
}

# La "ejecución" de esta herramienta captura los argumentos como datos estructurados
# No llama a ningún sistema externo: el valor está en los argumentos generados por el modelo
```

Beneficios: obtener salidas estructuradas validadas por JSON Schema, más confiable que parsear texto libre.

---

**Patrón: caché semántica de herramientas**

Cuando la misma herramienta es invocada con argumentos similares varias veces dentro de una interacción (o en interacciones frecuentes), los resultados se cachean asociados a la solicitud semántica, no solo al hash exacto de los argumentos.

```python
cache_semantico = {}

async def consultar_con_cache(nombre: str, argumentos: dict, ttl_segundos: int = 60) -> str:
    clave = f"{nombre}:{json.dumps(argumentos, sort_keys=True)}"
    if clave in cache_semantico:
        timestamp, resultado = cache_semantico[clave]
        if (datetime.now() - timestamp).seconds < ttl_segundos:
            return resultado
    resultado = await ejecutar_herramienta(nombre, argumentos)
    cache_semantico[clave] = (datetime.now(), resultado)
    return resultado
```

Beneficios: reduce llamadas repetidas a sistemas externos, disminuye latencia, reduce costos de API en sistemas con precio por llamada.

---

### Anti-patrones

**Anti-patrón: herramienta omnipotente**

Definir una sola herramienta que acepta SQL o código arbitrario para ejecutar en los sistemas de la empresa.

```json
// NUNCA hacer esto
{
  "name": "ejecutar_consulta",
  "description": "Ejecuta cualquier consulta SQL en la base de datos de la empresa.",
  "input_schema": {
    "properties": {
      "sql": {"type": "string", "description": "Consulta SQL a ejecutar."}
    }
  }
}
```

Por qué falla: expone el sistema completo a inyección SQL, permite al modelo (o a un atacante que manipula el modelo) acceder a cualquier dato o ejecutar cualquier operación sin restricciones de autorización. Una herramienta de este tipo invalida toda la arquitectura de seguridad.

---

**Anti-patrón: descripción duplicada**

Tener varias herramientas con nombres y descripciones que suenan idénticos o muy similares desde la perspectiva del modelo.

```json
// Problemático
{"name": "buscar_cliente", "description": "Busca un cliente en el sistema."}
{"name": "encontrar_cliente", "description": "Encuentra un cliente en la base de datos."}
{"name": "obtener_cliente", "description": "Obtiene los datos de un cliente."}
```

Por qué falla: el modelo no puede discriminar entre herramientas con descripciones semánticamente equivalentes. Invocará la que aparezca primero, o las invocará todas.

---

**Anti-patrón: ignorar los errores de herramientas**

Diseñar el sistema asumiendo que las herramientas siempre funcionan correctamente y no definir comportamiento para los errores.

```python
# Antipatrón: sin manejo de errores
async def ejecutar_herramienta(nombre, argumentos):
    resultado = await llamar_api_externa(nombre, argumentos)
    return resultado  # Si falla, la excepción rompe el loop completo
```

Por qué falla: los sistemas externos fallan. Un timeout no manejado puede interrumpir abruptamente la interacción. Sin un error informativo en el contexto, el modelo no puede adaptar su respuesta al usuario.

---

**Anti-patrón: herramientas con efectos secundarios ocultos**

Definir una herramienta de "consulta" que en realidad modifica datos como efecto secundario no documentado.

Ejemplo: una herramienta `obtener_siguiente_numero_pedido` que internamente incrementa un contador en la base de datos para reservar el número. Si el modelo la invoca varias veces durante el proceso de razonamiento, se reservan múltiples números que nunca se usan.

Por qué falla: viola el contrato de la herramienta tal como el modelo lo percibe. El modelo espera que las herramientas de consulta sean idempotentes. Si tienen efectos ocultos, el comportamiento del sistema es impredecible.

---

**Anti-patrón: exponer el stack técnico en los errores**

Devolver excepciones internas del sistema como resultado de una herramienta.

```python
# Antipatrón
except Exception as e:
    return str(e)  # "sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server..."
```

Por qué falla: el modelo recibe información técnica interna que no puede usar para razonar útilmente, y que puede filtrar información sensible sobre la arquitectura del sistema. El error correcto para el modelo es el descripto en la sección 05: informativo, accionable, sin detalles de implementación.

---

**Anti-patrón: no limitar el tamaño de la respuesta**

Herramientas que devuelven todos los resultados de una consulta sin paginación.

```python
# Antipatrón
resultado = db.query("SELECT * FROM pedidos WHERE cliente_id = %s", cliente_id)
return json.dumps({"pedidos": [p.to_dict() for p in resultado]})  # Puede ser 10,000 registros
```

Por qué falla: un resultado de herramienta de 50,000 tokens consume una porción enorme del contexto disponible, degrada el rendimiento del modelo, y en muchos casos contiene información que el modelo no necesita. La herramienta debe paginar y devolver solo los N resultados más relevantes para la solicitud.

---

### Tabla de referencia rápida

| Situación | Patrón recomendado | Anti-patrón a evitar |
|---|---|---|
| Muchas herramientas disponibles | Herramienta de enrutamiento | Cargar todas en el contexto siempre |
| Acción irreversible | Verificación + confirmación humana | Ejecución automática |
| Salida estructurada necesaria | Herramienta como esquema de salida | Parsear texto libre del modelo |
| Misma consulta repetida | Caché con TTL | Re-invocar la herramienta cada vez |
| Acceso a base de datos | Operaciones predefinidas | SQL arbitrario |
| Error de herramienta | Error informativo y accionable | Stack trace o excepción cruda |
| Resultados grandes | Paginación + limite configurable | Devolver todos los registros |
