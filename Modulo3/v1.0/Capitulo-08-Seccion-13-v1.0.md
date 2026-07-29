# Módulo 3 — Context Engineering

# Capítulo 08 — Agentes de IA: Arquitectura y Orquestación

## Sección 13 — Resumen del capítulo

> *"Un capítulo sobre agentes vale lo que vale su definición de partida. Todo lo demás es consecuencia."*

---

## Propósito de esta sección

Esta sección consolida las ideas fundamentales del capítulo en un formato de referencia rápida. Está organizada por los núcleos conceptuales del capítulo, en el mismo orden en que fueron desarrollados.

---

## Qué es un agente de IA

Un agente de IA es un sistema que percibe un objetivo, planifica una secuencia de acciones para alcanzarlo, ejecuta esas acciones mediante herramientas, observa los resultados intermedios y adapta su plan en función de esas observaciones. La capacidad de adaptación iterativa es su característica definitoria.

La distinción entre un asistente y un agente no es de complejidad: es de estructura de control. El asistente opera en ciclo estímulo-respuesta. El agente opera en un bucle de planificación, acción y observación que puede extenderse durante múltiples iteraciones.

La autonomía de un agente es una variable de diseño, no un atributo fijo. El nivel correcto depende del riesgo de las acciones, la reversibilidad de los errores y el costo de la supervisión.

---

## Los componentes de un agente

Seis componentes componen cualquier arquitectura de agente:

1. **Núcleo de razonamiento (LLM):** Interpreta el objetivo, genera el plan, decide las acciones y formula la respuesta final. Es el motor de todo el sistema.
2. **Módulo de planificación:** Estructura cómo el agente aborda el objetivo, sea de forma implícita (dentro del razonamiento del LLM) o explícita (plan generado antes de la ejecución).
3. **Módulo de estado:** Registro efímero de la ejecución actual: objetivo, acciones, observaciones, paso en curso.
4. **Módulo de herramientas:** Los efectores del agente. Permiten actuar sobre sistemas externos. La decisión de qué herramienta usar en cada paso es parte del razonamiento del LLM.
5. **Módulo de memoria:** Continuidad entre ejecuciones. Contiene perfil del usuario, resultados de tareas anteriores, preferencias operativas.
6. **Capa de orquestación:** Coordina el ciclo completo: invoca al LLM, ejecuta herramientas, actualiza el estado, detecta las condiciones de terminación.

---

## Arquitecturas y ciclos

Los patrones de arquitectura más estables en producción son:

- **ReAct (Reason + Act):** Ciclo de tres elementos en cada iteración: Thought (razonamiento explícito), Action (herramienta a invocar) y Observation (resultado del sistema). Es el patrón más usado y el más transparente.
- **Plan-and-Execute:** Separa planificación y ejecución. Ventajoso para tareas con pasos predefinibles.
- **Reflection:** Añade autoevaluación después de cada acción. Útil cuando el resultado es verificable automáticamente.
- **Self-Ask:** Descompone preguntas complejas en sub-preguntas. Efectivo para consultas con múltiples pasos de razonamiento encadenado.

El contexto del agente crece con cada iteración. Para tareas largas, se requieren estrategias activas de compresión del historial o uso de estado estructurado separado.

---

## Estado, memoria y herramientas

El estado es efímero: específico a la ejecución actual. La memoria es persistente: proporciona continuidad entre sesiones. Confundir ambos produce diseños donde se guarda lo que debería descartarse o se descarta lo que debería recordarse.

Las herramientas y RAG tienen roles distintos: RAG recupera conocimiento semántico de un corpus no estructurado; las herramientas de búsqueda estructurada recuperan datos exactos de sistemas operacionales. En agentes empresariales maduros, ambos coexisten.

La calidad de las descripciones de las herramientas determina directamente la calidad de las decisiones del agente. Una descripción ambigua produce selecciones incorrectas; una descripción precisa guía al modelo hacia la herramienta correcta.

---

## Orquestación y control

Los puntos de control para acciones irreversibles son el mecanismo que hace confiables a los agentes en contextos de negocio. Deben aplicarse a: acciones irreversibles, acciones que afectan a terceros y situaciones con información insuficiente.

Las condiciones de terminación deben estar en la capa de orquestación, no delegadas exclusivamente al razonamiento del LLM. El límite de iteraciones, el timeout y la detección de bucles son salvaguardas obligatorias.

Un agente que falla debe terminar gracefully, reportando el estado del proceso y las opciones disponibles para el usuario o el operador.

---

## Patrones y anti-patrones

Los patrones que producen agentes robustos son: herramientas atómicas, verificación antes de acciones irreversibles, terminación explícita y fallback con información parcial.

Los anti-patrones más frecuentes son: el agente todo-en-uno (catálogo de herramientas sobredimensionado), la confianza ciega en el output de herramientas, la improvisación de herramientas fuera de su diseño, el contexto sin gestión y los efectos secundarios ocultos en herramientas declaradas como solo lectura.

La mayoría de los anti-patrones no aparecen en el prototipo inicial: aparecen cuando el sistema escala. El diseño debe anticiparlos.

---

## El agente en el contexto del módulo

El agente es la arquitectura que integra los bloques construidos en los capítulos anteriores:
- Las instrucciones del sistema (capítulo 05) definen la política y los límites del agente.
- La memoria (capítulo 04) proporciona continuidad entre sesiones.
- RAG (capítulo 06) incorpora conocimiento externo al ciclo de acción.
- Las herramientas (capítulo 07) son los efectores que permiten al agente actuar.

El agente individual de este capítulo escala al sistema multiagente del capítulo 09 cuando la tarea supera la capacidad de un único agente o requiere paralelismo y especialización.

---

## Ideas clave del capítulo

- Un agente es la síntesis de los bloques del módulo: memoria, instrucciones, RAG y herramientas integrados en un ciclo de control adaptativo.
- ReAct es el patrón de referencia para la mayoría de los agentes empresariales. Su transparencia (razonamiento explícito) es su principal ventaja operativa.
- La autonomía controlada —con puntos de control en acciones sensibles y condiciones de terminación robustas— es lo que distingue los agentes de producción de los agentes de demo.
- El diseño del catálogo de herramientas es tan importante como el diseño del propio agente. Las herramientas mal descritas producen agentes que fallan silenciosamente.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
