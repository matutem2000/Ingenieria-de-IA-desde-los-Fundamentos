# Capítulo 10 — Planificación y Razonamiento

## Sección 05: Planificación iterativa y ejecución

Los patrones de planificación de la sección anterior son estructuras estáticas: el arquitecto define la secuencia de llamadas de antemano. La planificación iterativa es diferente: el agente decide en tiempo de ejecución qué paso dar a continuación, basándose en el resultado del paso anterior. Esta capacidad — planificar dinámicamente a medida que avanza — es lo que distingue a un agente con razonamiento real de un pipeline fijo.

### El ciclo de planificación dinámica

Un agente con planificación iterativa opera en un ciclo que se repite hasta que la tarea está completa o se alcanza un límite:

```
ESTADO INICIAL
  Tarea: [descripción de la tarea]
  Herramientas disponibles: [lista de herramientas]
  Contexto: [información disponible]

ITERACIÓN N
  1. RAZONAMIENTO: "Dado el estado actual, ¿cuál es el próximo paso necesario?"
  2. SELECCIÓN DE ACCIÓN: elegir entre:
     - Usar una herramienta
     - Consultar al usuario
     - Generar un output intermedio
     - Declarar la tarea completa
  3. EJECUCIÓN: realizar la acción seleccionada
  4. OBSERVACIÓN: incorporar el resultado al contexto
  5. EVALUACIÓN: ¿la tarea está completa? → si sí, terminar / si no, continuar

ESTADO FINAL
  Output: [resultado de la tarea]
  Traza: [historia de pasos, acciones y observaciones]
```

Este ciclo es la implementación concreta del patrón ReAct (Reasoning + Acting) mencionado en la sección anterior. La característica clave es que cada iteración produce información nueva que modifica el plan para la siguiente iteración.

### Por qué la planificación iterativa falla sin control

La planificación iterativa es poderosa pero introduce un riesgo que el arquitecto debe gestionar explícitamente: el ciclo puede no terminar.

**El problema del loop infinito de planificación** ocurre cuando el agente:

- Genera pasos que no avanzan hacia la solución (da vueltas alrededor del mismo problema)
- Alcanza un estado donde no puede avanzar porque una herramienta falla y no tiene alternativa
- Malinterpreta el criterio de completitud y sigue generando pasos innecesarios después de que la tarea está resuelta
- Genera un plan que requiere herramientas no disponibles y queda atrapado intentando diferentes variantes

Los mecanismos de control que el sistema debe implementar:

**1. Límite de iteraciones:** El número máximo de ciclos que el agente puede ejecutar antes de reportar un error o escalar al humano. Un valor típico es entre 10 y 30 iteraciones para tareas de complejidad media.

**2. Detección de estancamiento:** Si el agente ejecuta la misma acción (o acciones muy similares) más de N veces sin avanzar, el sistema debe interrumpir el ciclo y escalar.

**3. Criterio de completitud explícito:** El prompt del agente debe incluir una descripción precisa de cuándo la tarea está completa. Sin esta descripción, el modelo puede continuar generando pasos adicionales que degradan el output en lugar de mejorarlo.

**4. Timeout:** Un límite de tiempo absoluto, independiente del número de iteraciones, que garantiza que el sistema no bloquea indefinidamente.

### Plan-and-Execute: separar pensar de actuar

Una variante más controlable de la planificación iterativa es el patrón Plan-and-Execute. En lugar de decidir el próximo paso en cada iteración, el agente genera primero un plan completo y luego lo ejecuta paso a paso.

**Estructura:**

```
FASE 1 — PLANIFICACIÓN (una llamada al modelo)
Prompt: "Dada la tarea [descripción], genera un plan paso a paso para completarla.
Para cada paso, especifica: (a) la acción a realizar, (b) la herramienta necesaria,
(c) el output esperado, (d) cómo saber si el paso fue exitoso."

Output del modelo:
Paso 1: Buscar los últimos 3 informes anuales de la empresa.
  Herramienta: búsqueda web / base de datos documental.
  Output esperado: 3 documentos PDF o URLs.
  Criterio de éxito: documentos con fechas correspondientes a los últimos 3 años.

Paso 2: Extraer los indicadores financieros clave de cada informe.
  Herramienta: extractor de documentos.
  Output esperado: tabla con indicadores por año.
  Criterio de éxito: tabla completa para los 3 periodos.

[...]

FASE 2 — EJECUCIÓN (una llamada por paso)
Para cada paso del plan:
  - Ejecutar la acción con la herramienta indicada
  - Verificar el criterio de éxito
  - Si el paso falla, intentar alternativa o escalar
  - Registrar el output en la memoria de trabajo
```

**Ventajas del Plan-and-Execute:**

- El plan completo es inspeccionable antes de ejecutarse. Un humano puede revisarlo y modificarlo.
- Los errores de planificación (elegir la herramienta equivocada, olvidar un paso) se detectan antes de incurrir en el costo de ejecución.
- El progreso de ejecución es medible: "completados 3 de 7 pasos".
- Si la ejecución falla en un paso, el sistema sabe exactamente dónde está y puede replanificar desde ese punto.

**Limitaciones del Plan-and-Execute:**

- El plan se genera con información limitada (solo la información disponible al inicio). Si la ejecución de un paso revela información que cambiaría el plan, el sistema puede necesitar una fase de replanificación.
- El plan puede ser demasiado rígido para tareas donde los pasos dependen fuertemente de resultados intermedios que no se pueden predecir.

### Replanificación dinámica

Para tareas donde el entorno es suficientemente incierto como para que el plan inicial frecuentemente requiera ajustes, se puede combinar Plan-and-Execute con un mecanismo de replanificación:

```
[Plan inicial]
  → [Ejecutar paso 1] → [Resultado]
  → [Evaluar: ¿el resultado permite continuar con el plan?]
     → Sí: continuar con el paso 2
     → No: replanificar desde el paso 2 con la información nueva
```

La replanificación es una llamada adicional al modelo que recibe: el plan original, el resultado del paso fallido (o el resultado inesperado), y la tarea original, y produce un plan revisado para los pasos restantes.

### Ejemplo empresarial: análisis de proveedores

Un agente de análisis de proveedores recibe la tarea: "Evaluar si el proveedor X es un candidato adecuado para el contrato de suministro de componentes electrónicos para el próximo año."

**Plan generado en la fase de planificación:**

1. Buscar información pública sobre el proveedor (web, bases de datos de empresas).
2. Verificar su historial de cumplimiento en contratos similares (base de datos interna de contratos).
3. Consultar el perfil de riesgo financiero del proveedor (sistema de riesgo de crédito).
4. Verificar si el proveedor tiene certificaciones requeridas (ISO, CE, etc.).
5. Consolidar la evaluación: puntaje en cada dimensión, recomendación final.

**Ejecución:**

En el paso 3, el sistema de riesgo de crédito reporta que el proveedor tiene calificación "insuficiente" porque es una empresa nueva sin historial financiero previo. El plan original no contemplaba esta situación.

**Replanificación:** El agente replanifica a partir del paso 3: en lugar de descartar al proveedor, añade pasos adicionales para obtener referencias de clientes actuales del proveedor y verificar el respaldo financiero de su empresa matriz. La evaluación final incorpora esta información adicional.

### Nota del arquitecto

La tensión entre planificación rígida y planificación dinámica es real en producción. Los sistemas con planificación completamente dinámica son difíciles de depurar porque cada ejecución puede seguir un camino diferente. Los sistemas con planificación rígida fallan cuando el entorno no coincide con los supuestos del plan. El balance práctico es Plan-and-Execute con replanificación limitada: un plan inicial revisable, con capacidad de replanificar en pasos específicos predefinidos donde el entorno es más incierto.

La siguiente sección examina el mecanismo que hace posible que el agente detecte sus propios errores y los corrija: la reflexión y autoevaluación.
