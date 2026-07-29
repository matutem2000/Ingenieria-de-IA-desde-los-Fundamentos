# Capítulo 10 — Planificación y Razonamiento

## Sección 03: Patrones modernos de planificación

Dado que el razonamiento de un LLM depende del contexto, la pregunta del arquitecto es: ¿qué estructura de contexto induce el mejor razonamiento para cada tipo de tarea? La respuesta es una taxonomía de patrones de planificación. Cada patrón define cómo se estructura el flujo de llamadas al modelo, qué se incluye en el contexto de cada llamada y cómo se integran los outputs intermedios.

Esta taxonomía tiene cuatro patrones fundamentales. Son suficientemente estables como principios de diseño, aunque sus implementaciones específicas evolucionen con las herramientas y los modelos.

---

### Patrón 1: Llamada simple

**Descripción:** Una sola llamada al modelo produce la respuesta completa. El contexto contiene la tarea completa, y el modelo genera el output en un único paso.

**Estructura:**

```
[contexto: sistema + tarea] → [llamada al modelo] → [output final]
```

**Cuándo usarlo:** Tareas simples, bien delimitadas, donde el espacio de respuestas correctas es acotado. Clasificación de texto, extracción de entidades, transformación de formato, respuesta a preguntas con respuesta directa en el corpus de entrenamiento.

**Costo computacional:** Mínimo. Una llamada al modelo, latencia de una inferencia.

**Limitaciones:** Para problemas complejos, el modelo tiene a saltar pasos intermedios de razonamiento, lo que aumenta la tasa de error. No hay oportunidad de corrección intermedia. La calidad del output depende enteramente de que el modelo produzca la respuesta correcta en un solo intento.

**Ejemplo:** Un sistema de clasificación de tickets de soporte técnico que categoriza cada ticket en una de ocho categorías predefinidas. La tarea es suficientemente simple y el modelo suficientemente bien entrenado en el dominio como para que una sola llamada sea el diseño correcto.

---

### Patrón 2: Planificación secuencial (cadena de llamadas)

**Descripción:** La tarea se descompone en pasos, y cada paso es una llamada separada al modelo. El output de cada llamada se incorpora al contexto de la siguiente.

**Estructura:**

```
[tarea] → [llamada 1: descomposición] → [plan de pasos]
         → [llamada 2: paso 1] → [resultado parcial 1]
         → [llamada 3: paso 2, contexto incluye resultado 1] → [resultado parcial 2]
         → [llamada N: síntesis] → [output final]
```

**Cuándo usarlo:** Tareas que tienen estructura natural de pipeline: análisis seguido de síntesis, búsqueda seguida de respuesta, traducción de formato seguida de validación. También útil cuando la tarea supera la capacidad de razonamiento del modelo en una sola llamada.

**Costo computacional:** N veces la latencia de una llamada, donde N es el número de pasos. El contexto crece en cada llamada al incluir los resultados anteriores.

**Limitaciones:** Los errores en pasos tempranos se propagan a los pasos siguientes sin posibilidad de corrección automática. No hay ramificación: si el plan inicial es incorrecto, el sistema lo sigue hasta el final.

**Ejemplo:** Un sistema de análisis de contratos que primero extrae las cláusulas relevantes (llamada 1), luego identifica las obligaciones de cada parte en cada cláusula (llamada 2), luego evalúa el riesgo de cada obligación (llamada 3) y finalmente produce un resumen ejecutivo (llamada 4).

---

### Patrón 3: Planificación iterativa (con reflexión)

**Descripción:** El modelo genera una respuesta, luego la evalúa (en la misma llamada o en una llamada separada), identifica problemas y produce una versión mejorada. El ciclo se repite hasta que el output satisface un criterio de calidad o se alcanza un límite de iteraciones.

**Estructura:**

```
[tarea] → [llamada 1: borrador] → [respuesta inicial]
         → [llamada 2: evaluación] → [crítica + lista de problemas]
         → [llamada 3: revisión] → [respuesta mejorada]
         → [llamada 4: evaluación] → [¿satisfactorio? sí → fin / no → continuar]
```

**Cuándo usarlo:** Tareas donde la calidad del output es crítica y los errores son costosos. Generación de código que debe funcionar. Análisis que debe ser exhaustivo. Respuestas que serán presentadas a clientes o tomadas de decisiones de negocio. Cualquier tarea donde el modelo comete errores identificables con un segundo intento.

**Costo computacional:** Variable. Típicamente 2x a 4x el costo de una llamada simple. En el peor caso, puede generar muchas iteraciones sin convergencia si el criterio de evaluación no está bien definido. Es necesario establecer un límite de iteraciones.

**Limitaciones:** El mismo modelo que generó el error es el que lo evalúa. Hay clases de errores que el modelo no puede detectar por sí mismo — en particular, errores factuales en dominios donde el modelo tiene conocimiento incorrecto. La reflexión mejora la coherencia y la completitud, pero no garantiza la corrección factual.

**Ejemplo:** Un sistema de generación de código que produce una función, luego evalúa si maneja todos los casos borde descritos en el enunciado, luego revisa el código para agregar los casos que faltaban, y finalmente verifica que la versión revisada es sintácticamente correcta y completa.

---

### Patrón 4: Planificación ramificada (Tree of Thoughts)

**Descripción:** El modelo genera múltiples ramas de razonamiento en paralelo, evalúa cada rama y selecciona la más prometedora para continuar. El proceso se repite hasta alcanzar una solución o un límite de profundidad.

**Estructura:**

```
[tarea]
  → [llamada 1a: enfoque A] → [razonamiento A]
  → [llamada 1b: enfoque B] → [razonamiento B]
  → [llamada 1c: enfoque C] → [razonamiento C]
  → [llamada 2: evaluación de A, B, C] → [selección: B es más prometedor]
  → [llamada 3a: continuación de B, rama B1]
  → [llamada 3b: continuación de B, rama B2]
  → [llamada 4: evaluación B1 vs B2] → [selección: B1]
  → [llamada 5: solución final desde B1] → [output final]
```

**Cuándo usarlo:** Problemas de optimización donde el espacio de soluciones es grande y la solución óptima no es evidente. Tareas creativas donde hay múltiples enfoques válidos y se busca el mejor. Problemas donde el primer enfoque intuitivo del modelo frecuentemente es subóptimo.

**Costo computacional:** Alto. El número de llamadas crece exponencialmente con la profundidad del árbol y el factor de ramificación. En práctica, se usan árboles poco profundos (2-3 niveles) con ramificación limitada (2-3 ramas). Para una configuración típica de 3 niveles con 3 ramas, se necesitan del orden de 40 llamadas al modelo.

**Limitaciones:** Latencia alta. Costo alto. Complejidad de implementación alta. Solo justificado cuando la calidad del output tiene un valor suficientemente alto como para justificar el costo. No escala bien para sistemas de alto throughput.

**Ejemplo:** Un sistema de generación de estrategias de negocio que genera tres enfoques estratégicos diferentes para un problema de mercado, evalúa cuál tiene mayor viabilidad dado el contexto de la empresa, desarrolla el enfoque seleccionado con detalle en dos variantes de implementación, evalúa cuál variante tiene menor riesgo y mayor impacto, y finalmente produce el plan detallado de la variante ganadora.

---

### Tabla de selección de patrones

| Criterio | Simple | Secuencial | Iterativo | Ramificado |
|---|---|---|---|---|
| Complejidad de la tarea | Baja | Media | Media-alta | Alta |
| Calidad requerida | Suficiente | Buena | Alta | Óptima |
| Latencia admisible | Mínima | Moderada | Alta | Muy alta |
| Costo admisible | Mínimo | Moderado | Alto | Muy alto |
| Errores propagables | No aplica | Riesgo | Controlado | Controlado |

### Nota del arquitecto

Los patrones no son mutuamente excluyentes. Un sistema de producción típico usa una combinación: planificación secuencial como estructura base, con reflexión iterativa en los pasos donde la calidad es crítica, y llamada simple para los pasos de bajo riesgo. La decisión de qué patrón usar en cada paso es una decisión de ingeniería que balancea calidad, latencia y costo — los tres ejes que definen el espacio de diseño de sistemas de razonamiento.

La siguiente sección examina en detalle las técnicas que implementan los patrones 2 y 4: Chain of Thought y Tree of Thoughts.
