# Capítulo 15 — Proyecto Integrador

## Sección 04: Diseño del contexto y la memoria

Los capítulos 04 al 07 del módulo establecieron los fundamentos: cómo funciona la ventana de contexto, qué tipos de memoria existen, cómo se gestiona la información entre turnos. Esta sección aplica esos fundamentos al diseño concreto de TechCore.

### La estructura del contexto por turno

Cada vez que el usuario envía un mensaje, el orquestador construye el contexto que se enviará al LLM. Ese contexto tiene una estructura fija con cuatro zonas:

```
┌─────────────────────────────────────────────────────┐
│  ZONA 1 — INSTRUCCIÓN DEL SISTEMA                   │
│  (fija por sesión, varía por departamento y rol)    │
│  Aprox. 800–1200 tokens                             │
├─────────────────────────────────────────────────────┤
│  ZONA 2 — CONTEXTO DE MEMORIA PERSISTENTE           │
│  (recuperado al inicio de la sesión)                │
│  Aprox. 400–600 tokens                              │
├─────────────────────────────────────────────────────┤
│  ZONA 3 — FRAGMENTOS RAG                            │
│  (recuperados por consulta, turno a turno)          │
│  Aprox. 1500–2500 tokens                            │
├─────────────────────────────────────────────────────┤
│  ZONA 4 — HISTORIAL DE CONVERSACIÓN                 │
│  (ventana deslizante de los últimos N turnos)       │
│  Aprox. 1000–2000 tokens                            │
└─────────────────────────────────────────────────────┘
```

El presupuesto total de tokens por turno para TechCore v1.0 es de 6.000 tokens de entrada, reservando el espacio restante de la ventana del modelo (típicamente 128.000 tokens en modelos actuales) para futuras expansiones. Esta limitación autoimpuesta evita que el costo de la API escale sin control en las primeras semanas de operación.

### Diseño de las instrucciones del sistema por departamento

Cada perfil departamental tiene una instrucción del sistema que responde a cuatro preguntas: quién es el asistente en este contexto, qué puede hacer, qué no puede hacer, y cómo debe responder.

**Instrucción del sistema — Perfil TI (extracto):**

```
Eres el asistente interno de TI de TechCore. Tu función principal es 
ayudar a los ingenieros y analistas de soporte a resolver incidentes, 
localizar procedimientos en los runbooks de operaciones, y gestionar 
solicitudes en el sistema de tickets.

Puedes:
- Responder preguntas técnicas de procedimiento con base en la 
  documentación de TI disponible.
- Crear y consultar tickets en el sistema de gestión de incidentes.
- Proponer pasos de diagnóstico para incidentes de infraestructura.
- Escalar automáticamente incidentes P1 al equipo de guardia cuando 
  el usuario lo confirme.

No puedes:
- Acceder a información de otros departamentos (Legal, RRHH, Finanzas).
- Ejecutar comandos directamente en sistemas de producción.
- Proporcionar credenciales de acceso bajo ninguna circunstancia.

Nivel de detalle: técnico. Usa terminología de operaciones de TI. 
Cuando cites un runbook, incluye el nombre del documento y la sección.
```

**Instrucción del sistema — Perfil Legal (extracto):**

```
Eres el asistente interno de Legal de TechCore. Tu función principal es 
ayudar a los abogados internos y al equipo de cumplimiento a localizar 
cláusulas en contratos tipo, interpretar políticas internas con base 
en su texto, y gestionar solicitudes de revisión documental.

Puedes:
- Recuperar y citar cláusulas de los contratos tipo disponibles.
- Responder preguntas sobre políticas internas citando el documento fuente.
- Crear solicitudes de revisión de documentos.

No puedes:
- Proporcionar asesoría legal vinculante. Siempre indica que las 
  respuestas son orientativas y recomienda consultar al abogado 
  responsable para decisiones con efecto legal.
- Acceder a contratos activos en negociación sin nivel de autorización 
  elevado.

Nivel de detalle: preciso. Cita textualmente cuando sea posible. 
Indica siempre la versión y fecha del documento recuperado.
```

Los perfiles de RRHH y Finanzas siguen la misma estructura con restricciones específicas de sus dominios (datos salariales, información médica, datos de nómina).

### Gestión de la ventana deslizante

La ventana de conversación (Zona 4) usa una estrategia de ventana deslizante con resumen incremental. Las últimas cinco interacciones se conservan en texto completo. Las interacciones anteriores se comprimen en un resumen que el orquestador genera y almacena al momento de la compresión.

Esta elección tiene una consecuencia importante: el resumen es una interpretación, no una copia fiel. Si el usuario necesita recuperar un texto exacto de una conversación anterior, el sistema no puede garantizarlo. El diseño acepta ese límite a cambio de poder sostener conversaciones largas sin que el costo de tokens se vuelva prohibitivo.

El algoritmo de ventana deslizante para TechCore:

```python
def construir_historial(turnos: list[Turno], presupuesto_tokens: int) -> str:
    """
    Devuelve el historial de conversación que cabe en el presupuesto.
    Conserva los últimos 5 turnos completos.
    Comprime el resto en un resumen.
    """
    TURNOS_COMPLETOS = 5
    
    if len(turnos) <= TURNOS_COMPLETOS:
        return formatear_turnos(turnos)
    
    turnos_recientes = turnos[-TURNOS_COMPLETOS:]
    turnos_anteriores = turnos[:-TURNOS_COMPLETOS]
    
    resumen = recuperar_resumen_acumulado(turnos_anteriores)
    if resumen is None:
        resumen = generar_resumen(turnos_anteriores)
        almacenar_resumen(resumen)
    
    return f"[Resumen de conversación previa]\n{resumen}\n\n" + \
           formatear_turnos(turnos_recientes)
```

### Diseño del módulo de memoria persistente

La memoria persistente de TechCore almacena información que tiene valor más allá de una sesión. No todo lo que ocurre en una conversación merece ser memorizado: el criterio de selección es si la información cambiaría el comportamiento del asistente en la siguiente sesión.

**Qué se memoriza:**

| Tipo de información          | Ejemplo                                    | TTL               |
|------------------------------|---------------------------------------------|-------------------|
| Preferencias del usuario     | "Prefiero respuestas en viñetas"            | Sin expiración    |
| Rol dentro del departamento  | "Soy el responsable de turno nocturno de TI"| 90 días           |
| Solicitudes en curso         | "Tengo abierto el ticket #4521"             | Hasta resolución  |
| Incidentes recientes         | "El servidor web-03 estuvo caído el martes" | 30 días           |

**Qué no se memoriza:**

- El contenido literal de las respuestas del asistente.
- Datos personales sensibles (salud, situación financiera personal).
- Información que el usuario no proveyó explícitamente (inferencias especulativas).

**Estructura de entrada en el KV store:**

```json
{
  "user_id": "emp-0472",
  "department": "ti",
  "memories": [
    {
      "key": "preferencia_formato",
      "value": "viñetas cortas",
      "source": "explícita",
      "timestamp": "2026-06-15T09:23:00Z",
      "ttl_days": null
    },
    {
      "key": "tickets_activos",
      "value": ["#4521", "#4589"],
      "source": "inferida_de_conversación",
      "timestamp": "2026-07-20T14:15:00Z",
      "ttl_days": 30
    }
  ]
}
```

### El contexto de memoria en el prompt

Al inicio de cada sesión, el orquestador recupera la memoria persistente del usuario y la inyecta en la Zona 2 del contexto con un encabezado explícito:

```
[CONTEXTO DEL USUARIO - emp-0472]
Departamento: TI | Rol: Responsable de turno nocturno
Preferencias: respuestas en viñetas cortas, terminología técnica
Solicitudes activas: Ticket #4521 (disco lleno web-03, abierto hace 3 días)
Última sesión: 2026-07-22 — consultó runbook de escalación de incidentes P1
```

Este encabezado informa al LLM del estado actual del usuario sin que el usuario tenga que repetirlo. Si el usuario pregunta "¿cómo va lo del ticket?", el LLM ya sabe a qué ticket se refiere.

### Límites y compromisos de diseño

El diseño de memoria de TechCore asume que la memoria es un ayudante, no un archivo. Si el usuario quiere que el asistente olvide algo, puede solicitarlo explícitamente y el sistema debe honrarlo borrando la entrada del KV store. Este comportamiento no es solo una cortesía: en entornos regulados, el derecho al olvido puede ser un requisito legal.

La siguiente sección construye sobre esta base de contexto y memoria para integrar la recuperación de documentos y las herramientas externas.
