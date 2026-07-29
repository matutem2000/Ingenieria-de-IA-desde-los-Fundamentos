# Módulo 3 — Context Engineering

# Capítulo 08 — Agentes de IA: Arquitectura y Orquestación

## Sección 11 — Laboratorio práctico

> *"El diseño de un agente no se aprende leyendo sobre él. Se aprende trazando el ciclo paso a paso, con un objetivo real y herramientas concretas."*

---

## Objetivos del laboratorio

- Trazar el ciclo completo de un agente simple desde el objetivo hasta la respuesta final.
- Diseñar el catálogo de herramientas para una tarea específica, con descripciones precisas.
- Identificar los puntos de control y las condiciones de terminación correctas para el caso diseñado.
- Anticipar los fallos posibles y definir cómo el agente debe responder ante ellos.

---

## Estructura del laboratorio

Este laboratorio no requiere código. El objetivo es diseñar y trazar, con el nivel de detalle suficiente para que otro ingeniero pueda implementar lo que se describe.

El laboratorio tiene cuatro ejercicios progresivos. Cada uno puede realizarse de forma independiente o en secuencia como un diseño completo.

---

## Ejercicio 1 — Definir el agente

**Contexto:** Una empresa de logística quiere automatizar la primera etapa de gestión de reclamos de clientes por envíos retrasados. El agente debe: verificar si el envío está efectivamente retrasado, identificar la causa del retraso, y proponer al operador la acción apropiada (reembolso parcial, reembolso total, o escalada).

**Tarea:** Completar la ficha de definición del agente.

```
FICHA DE DEFINICIÓN DEL AGENTE
================================

Nombre del agente: ____________________

Objetivo principal:
[Describir en una oración qué debe lograr el agente al finalizar su ejecución]

Usuario/Sistema que activa el agente:
[¿Quién envía el objetivo inicial? ¿Es un humano o un sistema automatizado?]

Condiciones de éxito:
[¿Qué debe ser verdadero al finalizar para que el agente declare éxito?]

Condiciones de fallo:
[¿Cuándo debe el agente declarar que no puede completar el objetivo?]

Límite de iteraciones: ______ (justificar el valor elegido)

Nivel de autonomía: Supervisado / Semi-autónomo / Autónomo
[Indicar el nivel elegido y justificar por qué es apropiado para este caso]
```

---

## Ejercicio 2 — Diseñar el catálogo de herramientas

**Tarea:** Para el agente del ejercicio 1, diseñar entre 4 y 6 herramientas. Para cada herramienta, completar la ficha.

```
FICHA DE HERRAMIENTA
=====================

Nombre: ____________________
Tipo: [ ] Solo lectura  [ ] Escritura/Acción  [ ] Irreversible

Descripción para el agente:
[Esta descripción es la que verá el LLM. Debe indicar: qué hace la herramienta,
cuándo usarla, cuándo NO usarla, qué devuelve.]

Parámetros:
- nombre_param (tipo): descripción
- nombre_param (tipo): descripción

Output esperado:
[Describir la estructura del resultado en caso de éxito y en caso de error]

¿Requiere punto de control antes de ejecutar? [ ] Sí  [ ] No
Justificación: ____________________
```

---

## Ejercicio 3 — Trazar el ciclo

**Tarea:** Usando las herramientas diseñadas en el ejercicio 2, trazar el ciclo completo del agente para el siguiente escenario:

**Escenario:** El cliente CLT-0231 reporta que su envío ENV-20260718-4412, con fecha de entrega prometida para el 21 de julio, nunca llegó. Hoy es 25 de julio.

Usar el siguiente formato para cada iteración:

```
--- Iteración N ---
Thought: [El razonamiento del LLM en esta iteración]
Action: herramienta(parametros)
Observation: [El resultado que devuelve la herramienta]

[Si hay punto de control]
--- Punto de control N ---
Presentación al operador: [Descripción de la acción propuesta y su justificación]
Decisión del operador: Aprueba / Rechaza / Modifica
```

El ciclo debe incluir al menos 3 iteraciones y no más de 6.

---

## Ejercicio 4 — Anticipar fallos

**Tarea:** Para el agente diseñado, identificar tres escenarios de fallo y definir cómo debe responder el agente en cada uno.

Usar el formato:

```
ESCENARIO DE FALLO
==================

Descripción del fallo:
[¿Qué ocurre? ¿Qué herramienta falla? ¿Qué información está ausente?]

¿En qué iteración puede ocurrir?: ____

Respuesta esperada del agente:
[¿Qué debe hacer el agente? ¿Cómo debe reportar el fallo? ¿Qué información parcial
puede proveer? ¿Qué opciones ofrece al operador?]

¿Cómo se detecta este fallo en el diseño?:
[¿Es un error explícito de la herramienta? ¿Es una observación vacía inesperada?
¿Es un timeout? ¿Cómo distingue el agente este fallo de un resultado válido?]
```

---

## Ejemplo de referencia: solución parcial del Ejercicio 3

Para orientar el trabajo, se incluye la traza de las primeras dos iteraciones del escenario propuesto.

```
--- Iteración 1 ---
Thought: El cliente reporta que el envío ENV-20260718-4412 con entrega prometida para
el 21/07 no llegó. Hoy es 25/07, hay 4 días de retraso. Primero verifico el estado
actual del envío para confirmar el retraso y ver si hay información de la causa.
Action: obtener_estado_envio(envio_id="ENV-20260718-4412")
Observation: {"envio_id": "ENV-20260718-4412", "estado": "en_transito",
"ultima_ubicacion": "Centro de distribución Córdoba",
"fecha_estimada_entrega_actualizada": "2026-07-28",
"motivo_demora": "condiciones_climaticas", "cliente_id": "CLT-0231",
"origen": "Buenos Aires", "destino": "Mendoza"}

--- Iteración 2 ---
Thought: El envío está efectivamente retrasado. La fecha original era 21/07, la nueva
estimación es 28/07 (7 días de retraso). La causa registrada es "condiciones_climáticas".
Necesito verificar si la política de reclamos establece qué corresponde en este caso.
Action: buscar_politica_reclamos(causa="condiciones_climaticas", dias_retraso=7)
Observation: {"politica": "fuerza_mayor", "reembolso_aplicable": "no",
"compensacion": "cupon_descuento_10_porcentaje_proximo_envio",
"comunicacion_recomendada": "disculpa con explicación de causa y fecha estimada revisada"}
```

---

## Criterios de evaluación

Un diseño correcto del agente debe satisfacer estos criterios:

- Las herramientas son atómicas: cada una hace una sola cosa claramente definida.
- Ninguna herramienta irreversible se ejecuta sin punto de control.
- El ciclo trazado es coherente: cada iteración usa información de las iteraciones anteriores.
- Los fallos anticipados son realistas y las respuestas son concretas y útiles para el operador.
- El límite de iteraciones está justificado para la complejidad típica del caso.

---

## Nota del Arquitecto

> El error más frecuente en este laboratorio es diseñar herramientas demasiado amplias que hacen varias cosas a la vez. La tentación es reducir el número de herramientas para simplificar el diseño. El resultado es el anti-patrón de herramientas no atómicas: más difícil de depurar, menos reutilizable y más frágil ante cambios en los sistemas externos. Si una herramienta devuelve más de un tipo de información, es una señal de que probablemente debería dividirse en dos.

---

## Ideas clave

- El diseño de un agente requiere definir explícitamente: objetivo, herramientas, condiciones de terminación y respuestas de fallo. La implementación es secundaria a estas decisiones.
- Trazar el ciclo manualmente para un caso concreto es el método más efectivo para identificar huecos en el diseño antes de implementar.
- Los puntos de control para acciones irreversibles deben estar presentes en el diseño desde el inicio, no añadirse como corrección posterior.
- Anticipar fallos no es pesimismo: es la práctica que distingue un prototipo de un sistema de producción.

---

## Transición hacia la siguiente sección

El laboratorio completa la parte práctica del capítulo. La siguiente sección proporciona una lista de verificación estructurada que el AI Engineer puede usar antes de desplegar cualquier agente en un entorno de producción.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
