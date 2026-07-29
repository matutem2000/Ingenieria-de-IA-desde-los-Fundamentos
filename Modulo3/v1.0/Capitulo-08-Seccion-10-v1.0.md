# Módulo 3 — Context Engineering

# Capítulo 08 — Agentes de IA: Arquitectura y Orquestación

## Sección 10 — Caso de estudio: Agente de soporte técnico empresarial

> *"Un caso de estudio bien construido hace visible lo que los conceptos dejan implícito. Los detalles de implementación son donde vive la ingeniería real."*

---

## Objetivos de aprendizaje

- Integrar los conceptos del capítulo en un diseño de agente empresarial completo y coherente.
- Analizar las decisiones de diseño concretas que produce cada concepto cuando se aplica a un caso real.
- Identificar los compromisos entre capacidad, costo, latencia y seguridad en un sistema de producción.
- Utilizar este caso como plantilla mental para abordar diseños de agentes en contextos similares.

---

## Contexto del caso

Una empresa de software B2B ofrece soporte técnico a sus clientes a través de un sistema de tickets. El equipo de soporte recibe entre 200 y 400 tickets diarios. Aproximadamente el 60% de los tickets pueden resolverse con documentación existente; el 30% requiere consultar el historial técnico del cliente; el 10% requiere escalada a ingenieros.

El objetivo es construir un agente que maneje la primera atención de cada ticket: identifique la categoría del problema, recupere la información relevante, proponga una solución cuando sea posible, y escale cuando sea necesario. El agente opera en nombre de los agentes de soporte, no directamente con los clientes.

---

## Definición del objetivo del agente

El agente recibe un ticket con los siguientes campos:
- `ticket_id`: identificador único del ticket.
- `cliente_id`: identificador del cliente que reportó el problema.
- `descripcion`: texto libre con la descripción del problema.
- `prioridad`: baja, media, alta, crítica.
- `producto`: módulo o producto afectado.

El agente debe producir:
- Categorización del problema (tipo: configuración, error de datos, bug conocido, integración, otro).
- Historial relevante del cliente (tickets anteriores similares, soluciones aplicadas).
- Solución propuesta o, si no existe solución disponible, diagnóstico del problema.
- Recomendación de acción: resolver autónomamente, escalar al nivel 2, o escalar al equipo de ingeniería.

---

## Herramientas disponibles

```
obtener_ticket(ticket_id)
→ Devuelve todos los campos del ticket.

obtener_historial_cliente(cliente_id, limite, tipo_filtro)
→ Devuelve los últimos N tickets del cliente, con filtro opcional por tipo o producto.

buscar_en_documentacion(consulta)
→ RAG sobre la base de conocimiento técnico: manuales, guías de resolución, release notes.

buscar_bugs_conocidos(producto, descripcion)
→ Búsqueda en el registro de bugs conocidos con coincidencia por producto y descripción.

obtener_configuracion_cliente(cliente_id, producto)
→ Devuelve la configuración actual del cliente para un producto específico.

crear_resolucion(ticket_id, categoria, solucion, accion_recomendada)
→ Registra la resolución propuesta en el sistema de tickets. ACCIÓN IRREVERSIBLE.

escalar_ticket(ticket_id, nivel, justificacion)
→ Escala el ticket al nivel especificado (nivel_2 o ingenieria). ACCIÓN IRREVERSIBLE.
```

---

## Decisiones de diseño

**Arquitectura:** ReAct. El problema es exploratorio (los pasos dependen de la naturaleza del ticket) y el razonamiento transparente es valioso para los agentes de soporte que supervisan el sistema.

**Punto de control:** Las dos herramientas marcadas como irreversibles (`crear_resolucion` y `escalar_ticket`) siempre requieren un punto de control. El agente presenta la acción propuesta y espera confirmación del agente de soporte antes de ejecutarla.

**Límite de iteraciones:** 8 iteraciones máximo. Los tickets típicos se resuelven en 3-5 iteraciones. Si el agente necesita más de 8, el ticket es candidato a escalada.

**RAG vs. búsqueda estructurada:** `buscar_en_documentacion` usa RAG para recuperar guías y procedimientos por contenido semántico. `buscar_bugs_conocidos` y `obtener_historial_cliente` son búsquedas estructuradas sobre datos bien definidos.

---

## Traza del ciclo: ticket de ejemplo

**Ticket recibido:**
```
ticket_id: TKT-20260725-1847
cliente_id: CLI-0445 (Comercializadora del Norte S.A.)
prioridad: alta
producto: módulo de facturación
descripcion: "Desde ayer no podemos generar facturas electrónicas. El sistema muestra
              error CFDI-002 al intentar timbrar. Necesitamos resolverlo urgente."
```

---

**Iteración 1**

```
Thought: Ticket de prioridad alta sobre un error específico (CFDI-002) en el módulo de
facturación. Primero buscaré si este error es un bug conocido.
Action: buscar_bugs_conocidos(producto="facturacion", descripcion="CFDI-002")
Observation: {"bugs": [{"id": "BUG-1204", "codigo": "CFDI-002",
"descripcion": "Error de autenticación con el PAC cuando el certificado SAT
vence o fue renovado sin actualizar en el sistema", "solucion": "actualizar
el certificado en Configuración → Facturación → Certificados SAT",
"afecta_versiones": ["4.2", "4.3", "4.4"], "estado": "conocido_con_solucion"}]}
```

**Iteración 2**

```
Thought: El error CFDI-002 tiene una solución conocida: el certificado SAT venció o fue
renovado sin actualizar en el sistema. Necesito verificar la configuración actual del
cliente para confirmar que este es el caso.
Action: obtener_configuracion_cliente(cliente_id="CLI-0445", producto="facturacion")
Observation: {"certificado_sat": {"vigencia": "2026-07-20", "estado": "vencido"},
"version_modulo": "4.3", "pac": "Finkok"}
```

**Iteración 3**

```
Thought: Confirmado. El certificado SAT de Comercializadora del Norte venció el 20/07/2026
(hace 5 días), y están en la versión 4.3 que está afectada por BUG-1204. La solución
conocida aplica directamente. Debo consultar la documentación para dar instrucciones
precisas de cómo actualizar el certificado.
Action: buscar_en_documentacion(consulta="cómo actualizar certificado SAT módulo facturación renovación")
Observation: [fragmento: "Para actualizar el certificado SAT: 1) Ir a Configuración →
Facturación → Certificados SAT. 2) Hacer clic en 'Actualizar certificado'. 3) Subir
los archivos .cer y .key generados en el portal del SAT. 4) Ingresar la contraseña de
la clave privada. 5) Verificar el nuevo período de vigencia y guardar. 6) Emitir una
factura de prueba para confirmar la resolución."]
```

**Iteración 4 — Punto de control**

```
Thought: Tengo toda la información necesaria. El diagnóstico es claro (certificado vencido),
la solución es conocida y la documentación confirma los pasos exactos. Voy a proponer
la resolución. Esta acción requiere confirmación porque es irreversible.

Action: [PUNTO DE CONTROL — presentar al agente de soporte antes de ejecutar]

Propuesta de resolución para TKT-20260725-1847:
- Categoría: configuración
- Diagnóstico: Certificado SAT vencido el 20/07/2026. Error CFDI-002 es consecuencia directa.
- Solución: Instruir al cliente para que actualice el certificado en Configuración →
  Facturación → Certificados SAT (pasos detallados incluidos).
- Acción recomendada: resolver — nivel de soporte actual tiene toda la información necesaria.
- Referencia: BUG-1204, documentación sección 3.2.

¿Confirma la resolución?
```

**[Agente de soporte confirma]**

```
Action: crear_resolucion(ticket_id="TKT-20260725-1847", categoria="configuracion",
solucion="Certificado SAT vencido el 20/07. Instrucciones de actualización enviadas al cliente.
Referencia: BUG-1204.",
accion_recomendada="resolver")
Observation: {"estado": "resolucion_registrada", "timestamp": "2026-07-25T14:32:07"}
```

---

## Análisis de las decisiones de diseño en acción

Este ciclo ilustra varios principios del capítulo:

**Herramientas atómicas:** Cada herramienta hace una sola cosa. La verificación del bug, la verificación de la configuración del cliente y la búsqueda en documentación son operaciones separadas. Si alguna falla, el fallo está localizado.

**RAG vs. búsqueda estructurada:** `buscar_bugs_conocidos` y `obtener_configuracion_cliente` son búsquedas estructuradas con parámetros exactos. `buscar_en_documentacion` usa RAG porque el contenido es texto no estructurado y la consulta es semántica.

**Punto de control antes de acción irreversible:** El agente presenta la resolución propuesta antes de registrarla. El agente de soporte revisa y confirma. Esto evita registrar resoluciones incorrectas que podrían confundir al cliente.

**Terminación explícita:** La ejecución termina cuando la resolución es registrada, no cuando el agente deja de proponer acciones.

**Cuatro iteraciones:** El ticket se resolvió en 4 iteraciones (incluyendo el punto de control). El límite de 8 iteraciones no se alcanzó. Esto es indicativo de un diseño bien calibrado para el tipo de tarea.

---

## Nota del Arquitecto

> Este caso de estudio cubre el happy path: el ticket tiene un bug conocido con solución documentada y la configuración del cliente confirma el diagnóstico. En producción, el 40% de los tickets no siguen este camino. El diseño debe anticipar los casos donde el bug no está registrado, la documentación no tiene la respuesta, o la configuración del cliente es inconsistente. Para esos casos, el agente debe tener instrucciones explícitas en el system prompt sobre cuándo escalar y cómo reportar el estado parcial. El agente de soporte técnico del happy path es un buen primer paso; el agente que maneja bien los casos difíciles es el que produce valor en producción.

---

## Ideas clave

- El diseño de un agente empresarial requiere definir explícitamente: el objetivo, las herramientas disponibles, la política de puntos de control, el límite de iteraciones y la estrategia de fallback.
- Los puntos de control para acciones irreversibles no son una limitación de autonomía: son el mecanismo que hace confiable al agente en contextos de negocio.
- La elección entre RAG y búsqueda estructurada debe reflejar la naturaleza de los datos: semántica para documentación no estructurada, búsqueda exacta para datos operacionales bien definidos.
- Un ciclo de 4 iteraciones para un ticket de prioridad alta es un indicador de que el diseño está calibrado correctamente. Un ciclo de 8 iteraciones para el mismo tipo de ticket indicaría que algo en el diseño requiere revisión.

---

## Transición hacia la siguiente sección

El caso de estudio describió el proceso de diseño y ejecución de un agente. El laboratorio de la siguiente sección invita al lector a trazar su propio ciclo: diseñar el flujo de un agente simple, identificar sus herramientas, definir sus condiciones de terminación y anticipar sus fallos.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
