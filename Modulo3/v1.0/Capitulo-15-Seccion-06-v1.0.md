# Capítulo 15 — Proyecto Integrador

## Sección 06: Incorporación de agentes y planificación

Las secciones anteriores construyeron un asistente capaz de responder preguntas y ejecutar acciones simples con confirmación del usuario. Ese asistente es un sistema reactivo: responde a lo que el usuario pregunta. El agente de análisis de incidentes de TI introduce una capacidad cualitativamente distinta: el sistema puede razonar en múltiples pasos, consultar herramientas en secuencia y tomar decisiones intermedias sin input del usuario en cada paso.

### Cuándo un agente es la respuesta correcta

Antes de diseñar el agente, vale la pena enunciar explícitamente por qué RF-05 requiere un agente y no un flujo simple de herramienta.

Un incidente de TI no es una consulta con una respuesta directa. Es un proceso de investigación: se observa un síntoma, se formulan hipótesis, se recopila información para verificarlas, se descarta lo que no aplica, y se converge en un diagnóstico. Ese proceso tiene ramificaciones: la secuencia de pasos depende de lo que se encuentra en cada paso. Un flujo fijo de herramientas no puede manejar esa condicionalidad. Un agente, en cambio, puede razonar sobre lo que encontró y decidir qué herramienta invocar a continuación.

La heurística práctica: si la secuencia de herramientas que se necesita para resolver la tarea no puede definirse antes de ejecutarla, se necesita un agente.

### Arquitectura del agente de incidentes

El agente de incidentes opera bajo el ciclo ReAct (Reason-Act-Observe): razona sobre el estado actual, decide una acción, la ejecuta, observa el resultado, y vuelve a razonar con la nueva información. El orquestador implementa ese ciclo con un límite de iteraciones para evitar bucles infinitos.

```
CICLO REACT DEL AGENTE DE INCIDENTES

Entrada: descripción del incidente + contexto del usuario

Iteración 1:
  Razonamiento: "El usuario reporta que web-03 no responde. 
                 Necesito saber más: cuánto tiempo lleva caído,
                 si hay otros servicios afectados."
  Acción: verificar_solicitud(#4521) — recuperar historial del ticket
  Observación: "Ticket abierto hace 47 minutos. Severidad inicial: P2.
                Sin actualizaciones desde apertura."

Iteración 2:
  Razonamiento: "47 minutos sin resolución. Según política, P2 sin
                 resolución en 45 min debe escalarse a P1. Voy a buscar
                 el runbook de escalación para verificar."
  Acción: RAG("escalación incidentes P2 a P1 tiempo de resolución")
  Observación: Fragmento del Runbook-Incidentes-TI-v4.2, sección 4.1:
               "Si un incidente P2 no tiene resolución confirmada en 45
                minutos, debe reclasificarse a P1 y notificar al Gerente..."

Iteración 3:
  Razonamiento: "Confirmado por el runbook. Debo proponer la reclasificación.
                 Antes de hacerlo, verifico si hay incidentes similares 
                 recientes que puedan indicar la causa raíz."
  Acción: RAG("servidor web-03 incidentes previos disco lleno")
  Observación: Fragmento del historial de incidentes: "Ticket #4389 (2026-06-28):
               disco /var/log lleno en web-03, resuelto con limpieza de logs."

Iteración 4:
  Razonamiento: "Hay un antecedente de disco lleno en el mismo servidor.
                 Es la hipótesis más probable. Voy a formular el diagnóstico
                 y las acciones recomendadas."
  Acción: NINGUNA (síntesis final)

Salida al usuario:
  Diagnóstico probable: disco lleno en web-03 (antecedente el 28/06).
  Acciones recomendadas:
    1. Verificar uso de disco en web-03: df -h
    2. Si /var/log está al 90%+, ejecutar: journalctl --vacuum-size=500M
    3. Reclasificar ticket #4521 de P2 a P1 (47 min sin resolución).
  ¿Procedo con la reclasificación del ticket? [Sí / No]
```

El agente llegó a un diagnóstico específico usando cuatro pasos de razonamiento, dos consultas al motor RAG y una lectura del sistema de tickets, sin que el usuario tuviera que guiarlo paso a paso. Eso es lo que distingue al agente del asistente reactivo.

### Diseño de las herramientas del agente

El agente de incidentes tiene acceso a las mismas herramientas del asistente general más dos adicionales específicas para el análisis de incidentes:

**Herramienta 5: `buscar_incidentes_similares`**

```json
{
  "nombre": "buscar_incidentes_similares",
  "descripcion": "Busca en el historial de incidentes cerrados usando 
                  texto libre. Devuelve los 3 incidentes más similares.",
  "parametros": {
    "descripcion": "string",
    "servidor": "string | null",
    "dias_atras": "int (default: 90)"
  },
  "respuesta": {
    "incidentes": [
      {
        "id": "string",
        "titulo": "string",
        "causa_raiz": "string",
        "resolucion": "string",
        "fecha": "date"
      }
    ]
  },
  "permisos_requeridos": ["ti"],
  "requiere_confirmacion": false
}
```

**Herramienta 6: `escalar_incidente`**

```json
{
  "nombre": "escalar_incidente",
  "descripcion": "Reclasifica un incidente existente a mayor prioridad 
                  y notifica al equipo de guardia.",
  "parametros": {
    "ticket_id": "string",
    "nueva_prioridad": "P1",
    "justificacion": "string"
  },
  "respuesta": {
    "ticket_id": "string",
    "prioridad_anterior": "string",
    "prioridad_nueva": "P1",
    "notificados": ["string"]
  },
  "permisos_requeridos": ["ti"],
  "requiere_confirmacion": true
}
```

### Límites del agente y supervisión humana

El agente de incidentes tiene tres restricciones de diseño que limitan su autonomía:

**Restricción 1: máximo de iteraciones.** El ciclo ReAct tiene un límite de 8 iteraciones por ejecución. Si el agente no converge en un diagnóstico dentro de ese límite, presenta un resumen de lo que encontró y escala a un humano. Esto evita que el agente consuma tokens indefinidamente en casos de ambigüedad extrema.

**Restricción 2: confirmación antes de escalación.** El agente puede razonar, diagnosticar y proponer, pero la acción de escalar un incidente (que genera notificaciones al equipo de guardia) siempre requiere confirmación del usuario. El agente nunca escala sin aprobación humana.

**Restricción 3: sin ejecución de comandos en producción.** El agente puede proponer comandos de diagnóstico (como `df -h` o `journalctl`), pero no puede ejecutarlos directamente en servidores. La ejecución remota de comandos es una capacidad que está fuera del alcance de v1.0 por sus implicaciones de seguridad.

### Por qué un solo agente y no multiagente

La decisión de usar un solo agente fue establecida en la sección 03 y vale la pena desarrollarla aquí con el detalle que ese contexto no permitía.

Una arquitectura multiagente para el análisis de incidentes podría verse así: un agente coordinador que recibe el incidente y delega en agentes especializados (agente de diagnóstico, agente de búsqueda en runbooks, agente de escalación). Esa arquitectura tiene dos ventajas: mayor paralelismo (los agentes especializados pueden trabajar en simultáneo) y mayor modularidad (cada agente se puede mejorar independientemente).

Sin embargo, introduce dos costos que v1.0 no puede absorber: primero, la depuración se vuelve significativamente más difícil porque el estado del proceso está distribuido entre múltiples agentes; segundo, el costo de tokens se multiplica porque cada agente recibe su propio contexto completo.

Para TechCore v1.0, el agente único es la elección correcta porque los incidentes que el sistema debe manejar tienen una complejidad media: cuatro iteraciones de razonamiento son suficientes para la mayoría. Cuando el sistema madure y se identifiquen casos que requieren razonamiento más profundo, la migración a multiagente es el camino natural.

### La instrucción del sistema del agente

El agente de incidentes usa una instrucción del sistema diferente a la del asistente general de TI. Es más específica en cuanto al proceso que debe seguir:

```
Eres el agente de análisis de incidentes de TechCore TI. Cuando se te 
presenta un incidente, sigues este proceso:

1. RECOPILACIÓN: Obtén información básica del incidente (estado actual, 
   tiempo transcurrido, impacto).
2. DIAGNÓSTICO: Busca incidentes similares anteriores y runbooks aplicables.
3. HIPÓTESIS: Formula la causa raíz más probable con base en la evidencia.
4. PROPUESTA: Presenta diagnóstico, acciones recomendadas y, si aplica, 
   propuesta de escalación con justificación.

Reglas:
- Nunca ejecutes acciones en producción. Solo propone.
- Para escalar, siempre pide confirmación explícita.
- Si no tienes suficiente información después de 4 pasos, di qué 
  información adicional necesitas y quién puede proveerla.
- Cita siempre el runbook o el incidente previo que respalde tu análisis.
```

Esta instrucción transforma al LLM de un generador de texto en un agente con un proceso de trabajo explícito. El LLM sabe que debe seguir esos pasos en orden, y el operador que mantiene el sistema sabe exactamente qué comportamiento esperar.

---

Con el diseño de agentes completo, la siguiente sección incorpora las dos dimensiones operacionales que hacen que un sistema como este sea sostenible en producción: observabilidad y seguridad.
