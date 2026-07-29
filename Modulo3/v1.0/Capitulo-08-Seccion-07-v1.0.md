# Módulo 3 — Context Engineering

# Capítulo 08 — Agentes de IA: Arquitectura y Orquestación

## Sección 07 — Uso coordinado de herramientas y RAG

> *"Un agente que tiene diez herramientas y no sabe cuándo usar cada una no es más capaz que uno que tiene dos y las usa correctamente."*

---

## Objetivos de aprendizaje

- Comprender cómo un agente decide qué herramienta usar en cada paso del ciclo.
- Distinguir cuándo el agente debe invocar una herramienta de acción versus cuándo debe recuperar conocimiento mediante RAG.
- Analizar los desafíos de coordinación cuando herramientas y RAG coexisten en el mismo ciclo.
- Diseñar una política de uso de herramientas que sea eficiente, predecible y segura.

---

## Herramientas y RAG: dos mecanismos con roles distintos

El capítulo 07 estudió las herramientas como el mecanismo por el cual el agente actúa sobre sistemas externos. El capítulo 06 estudió RAG como el mecanismo por el cual el agente incorpora conocimiento externo al contexto. En el ciclo del agente, ambos coexisten, pero tienen roles distintos:

| Mecanismo | Función principal | Produce |
|---|---|---|
| Herramienta de acción | Ejecuta algo en el mundo externo | Efecto y resultado (éxito/error/datos) |
| Herramienta de búsqueda | Recupera datos específicos de un sistema | Datos estructurados |
| RAG | Recupera conocimiento semántico de un corpus | Fragmentos de texto con contexto |

La distinción no es absoluta. Una búsqueda en una base de datos es técnicamente una herramienta que recupera datos, pero su lógica es diferente a la de un sistema RAG que recupera fragmentos por similitud semántica. Ambos pueden coexistir en el mismo agente y el LLM debe decidir cuándo usar cada uno.

---

## Cómo el LLM decide qué herramienta usar

La decisión de qué herramienta invocar emerge del razonamiento del LLM, no de una lógica de enrutamiento explícita. Esto es lo que distingue al agente de una cadena de herramientas: el agente decide dinámicamente en función del estado actual.

El mecanismo es simple en su formulación: el LLM recibe las descripciones de todas las herramientas disponibles y, como parte de su razonamiento, selecciona la que mejor responde a la necesidad del paso actual.

```
Herramientas disponibles:
- buscar_contratos(cliente_id, fecha_inicio, fecha_fin): Busca contratos de un cliente.
- leer_documento(doc_id): Recupera el contenido completo de un documento.
- buscar_conocimiento(consulta): Busca en la base de conocimiento por similitud semántica.
- enviar_email(destinatario, asunto, cuerpo): Envía un correo electrónico.
- crear_tarea(descripcion, responsable, fecha_limite): Crea una tarea en el sistema de gestión.

Objetivo: "El cliente CLI-0892 pregunta sobre las condiciones de renovación del contrato
CONT-2024-087. Revisa el contrato, consulta nuestra política de renovaciones y prepara
una respuesta para el cliente."

--- Iteración 1 ---
Thought: Primero necesito leer el contrato específico. Tengo su ID en el objetivo.
Action: leer_documento(doc_id="CONT-2024-087")
Observation: [contenido completo del contrato — cláusulas, fechas, condiciones]

--- Iteración 2 ---
Thought: Tengo el contrato. Ahora necesito conocer nuestra política de renovaciones.
Eso es conocimiento interno que está en nuestra base de documentación. Usaré
buscar_conocimiento porque no sé el ID exacto del documento de política.
Action: buscar_conocimiento(consulta="política de renovación de contratos condiciones plazos")
Observation: [tres fragmentos de la política de renovaciones con los términos relevantes]

--- Iteración 3 ---
Thought: Tengo el contrato y la política. El contrato vence el 31/10/2026, tiene
cláusula de renovación automática con 90 días de preaviso para cancelar, y la política
establece que clientes Premium tienen descuento del 5% en renovaciones. CLI-0892 es
Premium. Puedo redactar la respuesta.
Action: [ninguna — genera respuesta final]
```

En este ejemplo, el agente usa `leer_documento` cuando conoce el ID exacto del recurso, y `buscar_conocimiento` (RAG) cuando necesita recuperar información por contenido sin saber exactamente qué documento contiene lo que busca. La decisión es parte del razonamiento del LLM.

---

## La calidad de las descripciones de herramientas

La decisión del LLM sobre qué herramienta usar depende directamente de la calidad de las descripciones de las herramientas disponibles. Una descripción ambigua produce selecciones incorrectas. Una descripción precisa guía al modelo hacia la herramienta correcta.

Principios para describir herramientas en el contexto de un agente:

**Describir el cuándo, no solo el qué.** No basta con decir qué hace la herramienta. La descripción debe indicar en qué situaciones es la elección correcta y, cuando aplica, en qué situaciones no lo es.

```
# Descripción débil:
buscar_contratos — busca contratos en el sistema

# Descripción precisa:
buscar_contratos(cliente_id, fecha_inicio, fecha_fin) — Usa esta herramienta cuando
necesites encontrar contratos asociados a un cliente específico, filtrando por período.
Requiere el ID del cliente. No uses esta herramienta para recuperar el contenido de
un contrato: usa leer_documento(doc_id) con el ID del contrato que devuelve esta búsqueda.
```

**Especificar el formato de los parámetros.** El LLM generará los parámetros de la herramienta como parte de su acción. Si el formato esperado es ambiguo, los parámetros generados pueden ser incorrectos.

**Indicar qué devuelve la herramienta.** El LLM razona sobre el resultado esperado para decidir si es la herramienta correcta. Si sabe que `buscar_contratos` devuelve IDs de contratos y no su contenido completo, entenderá que necesita un paso adicional con `leer_documento`.

---

## Cuándo elegir RAG versus herramientas de búsqueda estructurada

Una de las decisiones de diseño más frecuentes en agentes empresariales es cuándo usar RAG y cuándo usar una herramienta de búsqueda estructurada.

| Situación | RAG | Búsqueda estructurada |
|---|---|---|
| La consulta es semántica ("documentos sobre renovaciones") | Apropiado | No aplica |
| La consulta es por clave exacta ("contrato ID=CONT-2024-087") | No es la opción principal | Apropiado |
| El contenido está en documentos no estructurados | Apropiado | Limitado |
| El contenido está en una base de datos relacional | No aplica | Apropiado |
| Se necesita diversidad de perspectivas sobre un tema | Apropiado | Limitado |
| Se necesita un valor exacto o un conjunto acotado | No es la opción principal | Apropiado |

La regla práctica es que RAG es la elección cuando el agente necesita encontrar conocimiento por su contenido y la búsqueda exacta no es posible. La búsqueda estructurada es la elección cuando el agente conoce los criterios exactos de búsqueda y opera sobre datos estructurados.

En agentes empresariales maduros, ambos mecanismos coexisten: la búsqueda estructurada cubre los datos de los sistemas operacionales, y RAG cubre el conocimiento interno de la organización (políticas, procedimientos, documentación técnica).

---

## El riesgo de la sobreutilización de herramientas

Un agente con acceso a muchas herramientas puede volverse impredecible. El LLM puede invocar herramientas innecesarias (por ejemplo, buscar información que ya está en el contexto), puede encadenar llamadas redundantes o puede generar parámetros incorrectos para herramientas que no necesitaba usar.

Las estrategias para mitigar este riesgo:

**Proveer solo las herramientas necesarias para cada tarea.** Un agente no necesita tener acceso a todas las herramientas del sistema todo el tiempo. En diseños modulares, el conjunto de herramientas disponibles puede variar según el tipo de tarea o el paso del plan en ejecución.

**Incluir en el system prompt una guía de uso.** Una sección del system prompt del agente que explique la política de uso de herramientas (cuándo preferir RAG, cuándo usar búsqueda directa, en qué situaciones no se deben invocar herramientas) reduce las decisiones incorrectas.

**Validar las llamadas antes de ejecutarlas.** La capa de orquestación puede incluir una etapa de validación que verifica que los parámetros generados por el LLM son coherentes con la firma de la herramienta antes de ejecutarla.

---

## Nota del Arquitecto

> El diseño del catálogo de herramientas de un agente es tan importante como el diseño del propio agente. Un catálogo bien diseñado hace que el agente tome decisiones correctas naturalmente. Un catálogo mal diseñado produce errores difíciles de depurar porque el agente "racionalmente" elige la herramienta equivocada dada la información que tiene. Si un agente toma decisiones de herramientas incorrectas repetidamente, el primer lugar donde buscar el problema no es el prompt del agente: es la descripción de las herramientas.

---

## Ideas clave

- Las herramientas de acción y RAG tienen roles distintos en el ciclo del agente. Las herramientas actúan sobre sistemas externos o recuperan datos estructurados. RAG recupera conocimiento por similitud semántica de un corpus no estructurado.
- La decisión de qué herramienta usar emerge del razonamiento del LLM, que se basa en las descripciones de las herramientas disponibles. La calidad de esas descripciones determina directamente la calidad de las decisiones.
- En agentes empresariales maduros, búsqueda estructurada y RAG coexisten, cada uno cubriendo un tipo diferente de información.
- Un catálogo de herramientas sobredimensionado aumenta la incertidumbre del agente. Proveer solo las herramientas necesarias para cada contexto mejora la precisión y la predictibilidad.

---

## Transición hacia la siguiente sección

Las herramientas y RAG son los recursos que el agente usa en su ciclo. La siguiente sección estudia cómo el agente orquesta internamente el uso de esos recursos: cómo decide la secuencia de acciones, cuándo actuar autónomamente y cuándo detener la ejecución para solicitar intervención humana.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
