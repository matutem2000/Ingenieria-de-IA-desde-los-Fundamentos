# Capítulo 15 — Proyecto Integrador

## Sección 10: Caso completo de implementación

Esta sección presenta el caso TechCore como una unidad completa: el ciclo de vida de una interacción real, desde que el usuario escribe su mensaje hasta que recibe la respuesta, con todos los componentes del sistema en operación. No es un resumen de las secciones anteriores: es el escenario de integración que verifica que el diseño produce el comportamiento esperado.

### El escenario

**Usuario:** Marcos Velarde, analista de soporte TI, departamento TI, nivel de autorización estándar.
**Horario:** Martes 08:42, turno matutino.
**Memoria persistente disponible:** Preferencia por respuestas en viñetas. Ticket #4521 activo (servidor web-03 caído, abierto hace 3 días).

**Mensaje del usuario:**
> "Buenos días. Necesito ayuda con el web-03. Sigue sin responder y el ticket lleva 3 días abierto. ¿Esto ya debería haberse escalado?"

### Paso 1: El orquestador recibe la entrada

El orquestador registra la entrada del usuario con timestamp y genera el trace_id de la interacción:

```
trace_id: trc-20260725-0842-emp0472
user_id: emp-0472 (Marcos Velarde)
department: ti
timestamp: 2026-07-25T08:42:17Z
input: "Buenos días. Necesito ayuda con el web-03..."
```

### Paso 2: Recuperación del perfil y la instrucción del sistema

El orquestador consulta el módulo de instrucciones para el perfil TI. Recupera la instrucción del sistema v1.0. El tamaño de la instrucción es de 987 tokens.

### Paso 3: Recuperación de memoria persistente

El orquestador consulta el KV store con la clave `emp-0472`. Recupera:

```json
{
  "preferencia_formato": "viñetas cortas",
  "rol": "analista de soporte, turno matutino",
  "tickets_activos": ["#4521"],
  "ultima_sesion": {
    "fecha": "2026-07-22",
    "tema": "runbook de escalación de incidentes P1"
  }
}
```

El módulo de memoria formatea esta información en 412 tokens para la Zona 2 del contexto.

### Paso 4: Recuperación RAG

El orquestador detecta que el mensaje contiene referencias a escalación y a un incidente activo. Ejecuta una búsqueda RAG con la consulta: "escalación incidente servidor web tiempo de resolución política".

El motor RAG devuelve 5 fragmentos candidatos. El filtro de control de acceso verifica que todos pertenecen al departamento TI (el usuario tiene acceso). Los 5 fragmentos pasan el filtro. Se incluyen 4 de los 5 (el quinto es redundante con el primero) en 1.843 tokens para la Zona 3.

Los fragmentos recuperados provienen de:
- `Runbook-Incidentes-TI-v4.2.pdf`, sección 3.2 (escalación a soporte nivel 2)
- `Política-Gestión-Incidentes-v2.1.pdf`, sección 5 (tiempos de escalación)
- `Runbook-Incidentes-TI-v4.2.pdf`, sección 4.1 (clasificación P1)
- `Acuerdo-Nivel-Servicio-TechCore-v3.0.pdf`, sección 2 (SLA para servidores web)

### Paso 5: Construcción del contexto completo

El orquestador ensambla el contexto de 4.344 tokens:

```
[ZONA 1 — INSTRUCCIÓN DEL SISTEMA — 987 tokens]
Eres el asistente interno de TI de TechCore...

[ZONA 2 — CONTEXTO DEL USUARIO — 412 tokens]
[CONTEXTO DEL USUARIO - emp-0472]
Departamento: TI | Rol: Analista de soporte, turno matutino
Preferencias: viñetas cortas
Solicitudes activas: Ticket #4521 (web-03 caído, abierto hace 3 días)
Última sesión (22/07): consultó runbook de escalación P1

[ZONA 3 — DOCUMENTACIÓN RECUPERADA — 1843 tokens]
[DOCUMENTACIÓN INTERNA RECUPERADA]
Fuente 1: Runbook-Incidentes-TI-v4.2.pdf — Sección 3.2...
Fuente 2: Política-Gestión-Incidentes-v2.1.pdf — Sección 5...
...

[ZONA 4 — HISTORIAL DE CONVERSACIÓN — 1102 tokens]
(turno actual: mensaje de Marcos)
```

### Paso 6: Inferencia del LLM

El contexto se envía al LLM. El LLM razona sobre el mensaje considerando:
- El contexto de memoria (Marcos tiene el ticket #4521 activo hace 3 días)
- La política de escalación recuperada (P2 sin resolución en 45 min → P1; en este caso, 72 horas es claramente un caso que debió escalarse)
- El SLA para servidores web (el Acuerdo de Nivel de Servicio establece que un servidor web en producción tiene SLA de resolución de 4 horas para incidentes P2)

El LLM no solicita ninguna herramienta en este turno: puede responder completamente con la información del contexto. Genera una respuesta de 287 tokens.

### Paso 7: Filtrado de salida

La respuesta del LLM pasa por el filtro de salida. El filtro verifica:
- No contiene datos personales sensibles: ninguno detectado.
- Las citas de documentos están en los fragmentos recuperados: verificado.
- No hay señales de inyección de prompt en la salida: ninguna detectada.

La respuesta pasa el filtro.

### Paso 8: Respuesta al usuario

El sistema entrega la respuesta a Marcos a las 08:42:22 (5 segundos desde la entrada):

---

**Asistente:**

Buenas, Marcos. Sí, ese ticket debió escalarse hace tiempo.

**¿Por qué debió escalarse?**
- La Política de Gestión de Incidentes (sección 5) establece que un incidente P2 sin resolución en 45 minutos debe reclasificarse a P1.
- El ticket #4521 lleva 72 horas abierto sin resolución: excede ampliamente ese umbral.
- El SLA para servidores web de producción establece resolución de incidentes P2 en máximo 4 horas.

**Lo que recomiendo ahora:**
- Reclasificar el ticket #4521 de P2 a P1 inmediatamente.
- Notificar al Gerente de TI (según política, en los 15 minutos siguientes a la reclasificación).
- Verificar si hay logs de error recientes en web-03 — el 28 de junio tuviste un incidente similar de disco lleno resuelto con limpieza de logs.

¿Quieres que cree la actualización del ticket con la reclasificación a P1?

---

### Paso 9: Actualización de memoria

El orquestador actualiza la memoria persistente de Marcos con la nueva información relevante de la sesión:

```json
{
  "key": "ultima_sesion",
  "value": {
    "fecha": "2026-07-25",
    "tema": "escalación ticket #4521 a P1, servidor web-03"
  }
}
```

### Paso 10: Registro completo de la traza

El sistema registra la traza completa de la interacción con todos los campos definidos en la sección 07. El registro es inmutable.

### Lo que este escenario demuestra

Esta interacción de cinco segundos integró seis de los siete componentes de la arquitectura:

| Componente               | Contribución                                                    |
|--------------------------|-----------------------------------------------------------------|
| Instrucción del sistema  | Definió el rol y las restricciones del asistente para TI        |
| Memoria persistente      | Proveyó el contexto del ticket activo y las preferencias        |
| Motor RAG                | Recuperó la política de escalación y el SLA aplicable           |
| Orquestador              | Coordinó todos los componentes y construyó el contexto          |
| LLM                      | Razonó sobre el contexto y generó la respuesta                  |
| Observabilidad           | Registró la traza completa con latencias por etapa              |

El único componente que no se activó en este turno fue el módulo de herramientas, que hubiera entrado en el siguiente turno si Marcos hubiera respondido "Sí" a la propuesta de reclasificar el ticket.

Esta interacción es representativa del 80 % de las consultas que TechCore recibirá: preguntas de procedimiento que combinan recuperación de documentos con contexto de memoria. El 20 % restante activará el módulo de herramientas o el agente de incidentes para casos más complejos.

---

Con el caso completo de implementación como referencia, la siguiente sección propone el laboratorio integrador en tres niveles de profundidad.
