# Módulo 3 — Context Engineering

# Capítulo 08 — Agentes de IA: Arquitectura y Orquestación

## Sección 05 — Ciclo de percepción, planificación y acción

> *"El ciclo no es una metáfora. Es el mecanismo concreto por el que un agente convierte un objetivo en resultado."*

---

## Objetivos de aprendizaje

- Comprender en detalle el ciclo de percepción, planificación y acción en el patrón ReAct.
- Trazar un ciclo completo de tres iteraciones con todos sus elementos: pensamiento, acción y observación.
- Entender cómo el contexto del agente crece con cada iteración y qué implica para el diseño.
- Identificar las condiciones que determinan cuándo el ciclo debe terminar.

---

## El ciclo como unidad de análisis

El ciclo de percepción, planificación y acción es la unidad operativa del agente. Cada iteración del ciclo produce una acción que acerca al agente al objetivo o genera información que refina la comprensión del problema. La suma de esas iteraciones es la ejecución completa de la tarea.

Entender el ciclo en detalle no es un ejercicio académico. Es el conocimiento que permite al AI Engineer diseñar el prompt del agente, dimensionar el presupuesto de tokens, definir las condiciones de terminación y depurar comportamientos inesperados.

---

## Los tres elementos del ciclo ReAct

Cada iteración del ciclo ReAct tiene tres elementos:

**Thought (pensamiento).** El LLM razona sobre el estado actual antes de decidir una acción. Este pensamiento es texto explícito generado por el modelo como parte de su respuesta. No es un paso interno invisible: es una parte del output que puede ser leída, auditada y usada para diagnóstico.

**Action (acción).** El LLM especifica qué herramienta invocar y con qué parámetros. La acción es la consecuencia directa del pensamiento. En la mayoría de las implementaciones, la acción se genera en un formato estructurado (JSON o similar) que la capa de orquestación puede parsear y ejecutar.

**Observation (observación).** El resultado que devuelve la herramienta después de ser ejecutada. La observación es generada por el sistema, no por el LLM, y se añade al contexto del agente antes del siguiente ciclo. El LLM no puede predecir la observación: solo puede razonar sobre ella una vez que la recibe.

---

## Un ciclo completo: ejemplo en tres iteraciones

Tarea asignada al agente: "Identifica al cliente con mayor volumen de compras en el último mes y redacta un correo de fidelización personalizado."

El agente tiene acceso a dos herramientas:
- `consultar_ventas(periodo, orden, limite)` — devuelve clientes ordenados por volumen de compras.
- `obtener_perfil_cliente(cliente_id)` — devuelve el perfil completo del cliente.

---

**Iteración 1**

```
[Estado del contexto]
Objetivo: "Identifica al cliente con mayor volumen de compras en el último mes
y redacta un correo de fidelización personalizado."

[Respuesta del LLM]
Thought: Necesito identificar al cliente con mayor volumen de compras en el último mes.
Tengo acceso a la herramienta consultar_ventas. La usaré con el período del mes actual,
ordenada por volumen descendente, tomando solo el primero.

Action: consultar_ventas(periodo="2026-07", orden="volumen_desc", limite=1)

[Sistema ejecuta la herramienta]
Observation: {"cliente_id": "CLI-0892", "nombre": "Distribuidora Meridional S.A.",
"volumen_compras": 847500, "moneda": "ARS", "cantidad_pedidos": 23}
```

---

**Iteración 2**

```
[Estado del contexto]
Objetivo: [mismo]
Iteración 1 — Thought: [anterior]
Iteración 1 — Action: consultar_ventas(...)
Iteración 1 — Observation: {"cliente_id": "CLI-0892", ...}

[Respuesta del LLM]
Thought: Ya identifiqué al cliente: Distribuidora Meridional S.A. (CLI-0892), con
$847.500 en 23 pedidos este mes. Para redactar un correo personalizado, necesito
más información sobre el cliente: su contacto, el tipo de productos que compra y
si tiene algún segmento especial asignado. Usaré obtener_perfil_cliente.

Action: obtener_perfil_cliente(cliente_id="CLI-0892")

[Sistema ejecuta la herramienta]
Observation: {"cliente_id": "CLI-0892", "nombre": "Distribuidora Meridional S.A.",
"contacto": "Lic. Patricia Moreno", "email": "p.moreno@meridional.com.ar",
"segmento": "Premium", "productos_principales": ["ferretería industrial", "EPP"],
"cliente_desde": "2019-03-15", "ciudad": "Rosario"}
```

---

**Iteración 3**

```
[Estado del contexto]
Objetivo: [mismo]
Iteración 1 — [completa]
Iteración 2 — [completa]

[Respuesta del LLM]
Thought: Tengo toda la información que necesito. El cliente es Distribuidora Meridional
S.A., contacto Lic. Patricia Moreno, segmento Premium, cliente desde 2019. Sus compras
principales son en ferretería industrial y EPP. Puedo redactar un correo que reconozca
su actividad de este mes, mencione su antigüedad y ofrezca algo relevante para su
categoría de productos.

Action: [ninguna — el agente genera la respuesta final directamente]

Respuesta final:
---
Asunto: Gracias por otro mes excepcional, Distribuidora Meridional

Estimada Lic. Moreno:

A lo largo de este mes, Distribuidora Meridional S.A. ha sido una vez más nuestro
cliente con mayor actividad: 23 pedidos y $847.500 en compras de ferretería
industrial y EPP. Llevan más de siete años eligiéndonos, y cada mes lo confirman.

Como cliente Premium, queremos reconocer ese compromiso con acceso anticipado a
nuestra nueva línea de EPP certificada que estará disponible a partir de agosto.
Si desea coordinar una presentación personalizada para su equipo en Rosario,
quedo a disposición.

Muchas gracias por su confianza sostenida.
---
```

---

## Cómo crece el contexto en cada iteración

Uno de los aspectos más importantes del ciclo ReAct es que el contexto del agente crece con cada iteración. El prompt que el LLM recibe en la iteración 3 contiene el objetivo original más todos los pensamientos, acciones y observaciones de las iteraciones anteriores.

```
Iteración 1: Objetivo → ~150 tokens
Iteración 2: Objetivo + Iter1 completa → ~400 tokens
Iteración 3: Objetivo + Iter1 + Iter2 completas → ~700 tokens
```

Este crecimiento es predecible y debe tenerse en cuenta en el diseño. Para tareas que requieren muchas iteraciones o que devuelven observaciones muy extensas, el contexto puede aproximarse al límite de la ventana del modelo. Las estrategias de gestión de contexto del capítulo 04 se aplican aquí directamente: resumir observaciones largas, truncar resultados de herramientas o descartar pensamientos anteriores cuando ya no son relevantes.

---

## Condiciones de terminación

El ciclo debe terminar. Un agente sin condiciones de terminación robustas puede entrar en bucles infinitos, agotar el presupuesto de tokens o acumular errores sin resolución. Las condiciones de terminación son:

**Éxito:** El LLM determina que el objetivo está cumplido y genera la respuesta final sin invocar ninguna herramienta adicional.

**Máximo de iteraciones:** La capa de orquestación interrumpe el ciclo al alcanzar un límite predefinido. Típicamente entre 5 y 20 iteraciones según la complejidad esperada de las tareas.

**Error irrecuperable:** Una herramienta falla repetidamente, los resultados son inconsistentes o el agente detecta que no puede alcanzar el objetivo con los recursos disponibles.

**Solicitud de intervención humana:** El agente determina que la situación requiere una decisión humana y detiene la ejecución para escalar.

Estas condiciones deben estar codificadas en la capa de orquestación, no delegadas exclusivamente al razonamiento del LLM. Confiar en que el LLM siempre detectará cuándo debe detenerse es una fuente frecuente de fallos en sistemas de agentes.

---

## Nota del Arquitecto

> El crecimiento del contexto en cada iteración no es solo un problema de tokens: es un problema de calidad del razonamiento. Los LLMs grandes tienen ventanas de contexto extensas, pero su capacidad de atención a fragmentos distantes del contexto disminuye a medida que el contexto crece. Una observación de la iteración 1 puede recibir menos atención en la iteración 15 que en la iteración 2. Para tareas con muchas iteraciones, la estrategia de incluir un resumen del estado actual al inicio de cada prompt (en lugar del historial completo) puede mejorar tanto la calidad del razonamiento como el uso de tokens.

---

## Ideas clave

- El ciclo ReAct tiene tres elementos en cada iteración: Thought (razonamiento explícito del LLM), Action (herramienta a invocar con parámetros) y Observation (resultado generado por el sistema).
- El contexto del agente crece con cada iteración porque incluye el historial completo de pensamientos, acciones y observaciones. Este crecimiento debe gestionarse activamente.
- Las condiciones de terminación deben estar codificadas en la capa de orquestación. El límite de iteraciones, la detección de errores irrecuperables y los puntos de escalada son decisiones de diseño, no comportamientos emergentes.
- El pensamiento explícito del agente es su principal herramienta de diagnóstico. Leer la secuencia de pensamientos de un agente que falló casi siempre revela en qué punto del razonamiento ocurrió el error.

---

## Transición hacia la siguiente sección

El ciclo de acción del agente describe cómo opera en una sola ejecución. Pero los agentes que operan en entornos reales deben mantener coherencia entre múltiples ejecuciones, recordar el contexto del usuario y gestionar el estado interno de tareas largas. La siguiente sección estudia la gestión del estado y la memoria del agente.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
