# Capítulo 10 — Planificación y Razonamiento

## Sección 08: Arquitecturas de planificación empresarial

Los patrones y técnicas de las secciones anteriores son piezas de construcción. Esta sección examina cómo esas piezas se ensamblan en arquitecturas completas que operan en entornos empresariales reales — con sus restricciones de latencia, costo, regulación y disponibilidad.

Un sistema de planificación empresarial no es solo un agente que razona bien. Es un sistema que razona bien dentro de los límites operacionales del negocio, produce outputs auditables, falla de forma predecible y escala bajo carga.

### Las cuatro dimensiones del diseño empresarial

**Dimensión 1: Calidad del razonamiento**

El sistema debe producir outputs de calidad suficiente para el caso de uso. "Suficiente" es la palabra clave: el nivel de sofisticación del razonamiento debe estar calibrado al nivel de precisión que el caso de uso requiere, no al nivel máximo que la técnica permite.

Un sistema de análisis de documentos legales requiere un nivel diferente de razonamiento que un sistema de clasificación de emails de marketing. La arquitectura de planificación debe reflejar esa diferencia: más iteraciones de reflexión, más capas de verificación, más llamadas al modelo donde la calidad es crítica; menos donde no lo es.

**Dimensión 2: Latencia**

En entornos empresariales, la latencia no es solo una métrica de experiencia de usuario. Es a menudo un requisito contractual (SLA) o una restricción funcional (el resultado del agente bloquea un proceso upstream).

La relación entre sofisticación del razonamiento y latencia es directa: más llamadas al modelo implica más latencia. El arquitecto debe conocer el presupuesto de latencia del caso de uso y diseñar la arquitectura de razonamiento dentro de ese presupuesto.

Estrategias para gestionar la latencia:
- Paralelizar llamadas al modelo cuando no tienen dependencias entre sí (por ejemplo, evaluar múltiples documentos simultáneamente).
- Usar modelos más pequeños y rápidos para los pasos de evaluación y reflexión donde la precisión completa no es necesaria.
- Cachear outputs de pasos que no cambian entre ejecuciones similares.
- Separar las fases de planificación (puede ser asíncrona) de las fases de acción (puede requerir latencia baja).

**Dimensión 3: Auditabilidad**

En sectores regulados — finanzas, salud, legal — el sistema debe poder responder a la pregunta: "¿Por qué el agente tomó esta decisión?". La respuesta no puede ser "el modelo lo generó". Debe ser un registro estructurado de los pasos de razonamiento, las herramientas usadas, los datos consultados y los criterios aplicados.

Los sistemas de planificación empresarial deben registrar:
- El input completo de cada llamada al modelo
- El output completo de cada llamada al modelo
- Las herramientas usadas y sus inputs/outputs
- El resultado de cada verificación
- La decisión tomada en cada punto de bifurcación del plan

Esta traza de ejecución no es solo para auditoría: es también la base para depurar el sistema cuando falla y para mejorar el diseño basándose en datos de producción.

**Dimensión 4: Escalada y control humano**

Ningún sistema de planificación autónoma es apropiado para todos los escenarios. El arquitecto debe definir explícitamente:

- Qué decisiones el agente puede tomar de forma autónoma
- Qué decisiones requieren confirmación humana antes de ejecutarse
- Qué situaciones desencadenan una escalada automática al operador humano
- Cómo se interrumpe el agente si es necesario

El patrón de escalada más robusto es el "human-in-the-loop" configurable: el sistema puede operar en modo completamente autónomo, en modo de confirmación (el humano aprueba cada acción antes de ejecutarse) o en modo de revisión (el agente actúa pero el humano puede revertir dentro de una ventana de tiempo). El nivel de supervisión se configura según el tipo de acción y el nivel de riesgo.

### Arquitectura de referencia

La siguiente arquitectura de referencia combina los cuatro patrones de planificación con las cuatro dimensiones empresariales. Es una estructura de tres capas:

```
CAPA 1 — PLANIFICACIÓN ESTRATÉGICA
  Input: tarea del usuario + contexto de negocio
  Proceso: llamada de planificación (CoT) → plan de alto nivel
  Output: plan estructurado con pasos, herramientas, criterios de éxito
  Latencia: puede ser asíncrona (el usuario espera el plan, no la ejecución)

CAPA 2 — EJECUCIÓN TÁCTICA (por cada paso del plan)
  Input: paso del plan + estado actual + memoria de trabajo
  Proceso: 
    a. Ejecutar acción (herramienta o llamada al modelo)
    b. Verificar output según tipo (código / factual / estructurado)
    c. Si verificación falla → reflexión + corrección (máx. N iteraciones)
    d. Si no converge → escalar a humano
  Output: resultado del paso + actualización de memoria de trabajo
  Latencia: sincrónica, debe cumplir SLA

CAPA 3 — SÍNTESIS Y ENTREGA
  Input: resultados de todos los pasos + tarea original
  Proceso: llamada de síntesis → respuesta final
  Output: respuesta al usuario / acción en sistema externo
  Auditabilidad: registro completo de capas 1 y 2 disponible
```

### Decisiones de diseño comunes

**¿Un modelo o múltiples modelos?**

En sistemas de producción, usar un modelo diferente para planificación (donde se necesita razonamiento profundo) y para ejecución de pasos de bajo riesgo (donde se necesita velocidad y bajo costo) es una decisión válida y frecuente. El modelo de planificación puede ser mayor y más preciso; el modelo de ejecución de pasos simples puede ser menor y más rápido.

**¿Planificación en tiempo real o planificación pre-computada?**

Para casos de uso con alta variabilidad de tareas (cada solicitud es diferente), la planificación debe ser en tiempo real. Para casos de uso donde las tareas son variantes de un conjunto limitado de flujos conocidos, los planes pueden pre-computarse y almacenarse, usando la llamada al modelo solo para adaptar el plan almacenado al contexto específico. Esto reduce significativamente la latencia.

**¿Cómo gestionar el contexto en sistemas de larga duración?**

Los sistemas de planificación que operan durante horas o días (por ejemplo, un agente que gestiona un proceso de semanas) deben gestionar el contexto de forma activa. La ventana de contexto del modelo tiene límites. El sistema debe mantener una memoria de trabajo que incluya solo la información relevante para el estado actual, y archivar el historial completo en almacenamiento externo (cubierto en el capítulo 09).

### Nota del arquitecto

El error más común en la transición de prototipo a producción es no planificar para el fallo. En el prototipo, el happy path funciona bien. En producción, el agente inevitablemente encuentra situaciones que no estaban en el conjunto de pruebas: herramientas que no responden, datos con formatos inesperados, tareas ambiguas que el plan no puede completar. El diseño debe incluir, desde el inicio, qué hace el sistema cuando falla — no como caso excepcional, sino como parte del diseño principal.

La siguiente sección examina los patrones que funcionan y los que fallan en producción, con el análisis de por qué.
