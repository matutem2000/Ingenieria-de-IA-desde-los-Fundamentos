# Módulo 3 — Context Engineering

# Capítulo 08 — Agentes de IA: Arquitectura y Orquestación

## Sección 01 — ¿Qué es un agente de IA?

> *"Un asistente responde. Un agente percibe, planifica y actúa. La diferencia no es filosófica: es arquitectónica."*

---

## Objetivos de aprendizaje

- Establecer una definición operativa precisa de "agente de IA" que distinga el agente de un asistente conversacional y de una cadena simple de llamadas a herramientas.
- Comprender qué hace que un sistema sea agéntico y qué condiciones debe cumplir para merecer ese nombre.
- Ubicar el agente dentro de la arquitectura de Context Engineering construida a lo largo del módulo.
- Reconocer los límites conceptuales de este capítulo respecto a los capítulos adyacentes sobre herramientas (07) y sistemas multiagente (09).

---

## El problema de la definición

La industria usa la palabra "agente" de maneras distintas y a veces contradictorias. LangChain llama agente a cualquier cadena que usa herramientas. AutoGPT popularizó la imagen de un sistema que se ejecuta indefinidamente sin supervisión. Los papers académicos definen agentes en términos de percepción, estado y función de utilidad. El SDK de Claude describe agentes como sistemas que orquestan múltiples herramientas y ciclos de razonamiento.

Antes de estudiar cómo se construye un agente, es necesario acordar qué entendemos por uno. Una definición imprecisa produce diseños imprecisos.

---

## Definición operativa

Para este módulo, un agente de IA es un sistema que:

1. **Percibe un objetivo** definido por el usuario u otro sistema.
2. **Planifica una secuencia de acciones** para alcanzar ese objetivo.
3. **Ejecuta esas acciones** mediante herramientas externas, bases de conocimiento o llamadas a otros sistemas.
4. **Observa los resultados intermedios** de cada acción.
5. **Adapta su plan** en función de esos resultados hasta completar el objetivo o determinar que no puede completarlo.

Esta definición incluye cuatro elementos que lo distinguen de otros sistemas:

| Característica | Asistente conversacional | Cadena de herramientas | Agente |
|---|---|---|---|
| Responde a una consulta | Sí | Sí | Sí |
| Ejecuta herramientas | No / limitado | Sí (orden fijo) | Sí (orden dinámico) |
| Adapta el plan según resultados | No | No | Sí |
| Puede iterar múltiples ciclos | No | No | Sí |
| Decide cuándo terminó | No | No | Sí |

El punto central es la adaptación dinámica. Una cadena de herramientas ejecuta pasos en un orden predefinido. Un agente decide en cada paso qué hacer a continuación, basándose en lo que ya observó. Esa capacidad de decisión iterativa es lo que define la arquitectura agéntica.

---

## Lo que un agente no es

**Un agente no es un asistente que usa herramientas.** Si el sistema llama a una herramienta de búsqueda y entrega el resultado directamente, eso es un asistente con acceso a una herramienta. La estructura es estímulo-respuesta con un paso adicional. No hay planificación, no hay iteración, no hay adaptación.

**Un agente no es sinónimo de autonomía total.** El nivel de autonomía de un agente es una decisión de diseño. Algunos agentes consultan al usuario en cada paso crítico. Otros operan de manera completamente autónoma dentro de límites definidos. Ambos son agentes. La autonomía es una variable del diseño, no un atributo definitorio.

**Un agente no requiere un framework específico.** LangChain, LangGraph, AutoGen, CrewAI y el SDK de Claude implementan patrones de agentes, pero un agente puede implementarse directamente llamando a la API de un modelo de lenguaje en un bucle de control personalizado. El framework facilita la implementación; no constituye el agente.

---

## Por qué los agentes emergen en este punto del módulo

Los capítulos anteriores construyeron los bloques que un agente necesita:

- **Capítulo 04 (Memoria):** Un agente necesita recordar qué hizo en pasos anteriores y qué resultados obtuvo. Sin memoria, cada ciclo empieza desde cero.
- **Capítulo 05 (Instrucciones del sistema):** El agente opera bajo políticas definidas en el system prompt. Esas políticas determinan qué puede hacer y qué no, cómo debe comportarse ante resultados inesperados y cuándo debe escalar a un humano.
- **Capítulo 06 (RAG):** Un agente puede recuperar conocimiento externo como parte de su ciclo de acción. La decisión de cuándo recuperar y qué recuperar es parte de su planificación.
- **Capítulo 07 (Herramientas):** Las herramientas son los efectores del agente. Sin herramientas, el agente solo puede razonar y generar texto; no puede actuar sobre el mundo.

Un agente es la arquitectura que integra todos estos bloques en un ciclo de control coherente.

---

## Los límites de este capítulo

**Este capítulo cubre el agente individual.** La arquitectura de un único agente: cómo está compuesto, cómo opera su ciclo interno, cómo gestiona estado y memoria, cómo decide qué herramientas usar y cuándo terminar.

**El capítulo 09 cubre sistemas multiagente.** Qué ocurre cuando la tarea supera la capacidad de un único agente o requiere paralelismo y especialización. Cómo múltiples agentes se coordinan, se delegan trabajo entre sí y gestionan la coherencia colectiva.

**El capítulo 10 cubre planificación y razonamiento.** Los mecanismos cognitivos que el modelo de lenguaje usa para razonar. La distinción es importante: este capítulo se ocupa de cómo está construido el agente; el capítulo 10 se ocupa de cómo piensa.

---

## Qué contiene este capítulo

Las secciones siguen esta progresión:

1. **¿Qué es un agente de IA?** — Esta sección: definición, límites conceptuales.
2. **De asistentes a agentes autónomos** — El salto cualitativo entre responder y actuar.
3. **Componentes fundamentales** — Los bloques que componen cualquier agente.
4. **Arquitecturas de agentes modernas** — Los patrones de referencia estables: ReAct, Plan-and-Execute, Reflection.
5. **Ciclo de percepción, planificación y acción** — El ciclo ReAct en detalle con ejemplo completo.
6. **Gestión del estado y memoria** — Qué debe recordar el agente y cómo lo organiza.
7. **Uso coordinado de herramientas y RAG** — Cómo decide el agente qué herramienta usar y cuándo recuperar conocimiento.
8. **Orquestación y toma de decisiones** — Cuándo actuar autónomamente y cuándo escalar.
9. **Patrones y anti-patrones** — Lo que funciona y lo que rompe sistemas reales.
10. **Caso de estudio empresarial** — Una implementación completa de principio a fin.
11. **Laboratorio práctico** — Diseño y traza del ciclo de un agente simple.
12. **Checklist del AI Engineer** — Lo que debe verificarse antes de desplegar.
13. **Resumen** — Las ideas centrales del capítulo.
14. **Autoevaluación** — Preguntas para verificar la comprensión.
15. **Transición al Capítulo 9** — El paso del agente individual al sistema multiagente.

---

## Ideas clave

- Un agente de IA percibe un objetivo, planifica acciones, las ejecuta y adapta el plan según los resultados. Esa capacidad de adaptación iterativa es su característica definitoria.
- La diferencia entre un asistente con herramientas y un agente no es de complejidad: es de estructura de control. El agente decide dinámicamente qué hacer a continuación.
- La autonomía de un agente es una variable de diseño, no un atributo fijo. Los niveles de supervisión humana son decisiones de arquitectura.
- El agente es la síntesis de los bloques construidos en los capítulos anteriores: memoria, instrucciones del sistema, RAG y herramientas integradas en un ciclo de control.

---

## Transición hacia la siguiente sección

Definir qué es un agente exige entender de dónde viene. La distinción entre asistentes y agentes no surgió de una definición académica: emergió de la práctica, del intento de resolver tareas que los asistentes conversacionales no podían completar. La siguiente sección traza esa evolución y articula con precisión el salto cualitativo entre responder y actuar.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
