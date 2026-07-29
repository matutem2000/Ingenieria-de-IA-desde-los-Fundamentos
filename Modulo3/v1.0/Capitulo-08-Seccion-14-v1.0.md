# Módulo 3 — Context Engineering

# Capítulo 08 — Agentes de IA: Arquitectura y Orquestación

## Sección 14 — Autoevaluación

> *"La autoevaluación no mide cuánto se leyó. Mide cuánto se comprendió lo suficiente como para aplicarlo."*

---

## Propósito de la autoevaluación

Esta sección presenta preguntas para verificar la comprensión de los conceptos principales del capítulo. Las preguntas están organizadas en tres niveles: comprensión conceptual, análisis de casos y decisión de diseño. Las respuestas aparecen al final de la sección.

---

## Nivel 1 — Comprensión conceptual

**Pregunta 1.** ¿Cuál es la característica que distingue fundamentalmente a un agente de IA de un asistente conversacional que usa herramientas?

a) El agente usa modelos de lenguaje más grandes.
b) El agente puede adaptar su plan en función de los resultados intermedios de sus acciones.
c) El agente tiene acceso a más herramientas simultáneamente.
d) El agente no requiere intervención humana en ningún punto del proceso.

---

**Pregunta 2.** En el ciclo ReAct, ¿cuál de los tres elementos (Thought, Action, Observation) es generado por el sistema en lugar de por el LLM?

a) Thought.
b) Action.
c) Observation.
d) Los tres son generados por el LLM.

---

**Pregunta 3.** ¿Cuál es la diferencia principal entre el estado del agente y su memoria persistente?

a) El estado contiene información del usuario; la memoria contiene el historial de acciones.
b) El estado es efímero y específico a la ejecución actual; la memoria proporciona continuidad entre ejecuciones.
c) El estado se almacena en la base de datos; la memoria vive en el contexto del LLM.
d) El estado es gestionado por el LLM; la memoria es gestionada por la capa de orquestación.

---

**Pregunta 4.** ¿Por qué las condiciones de terminación de un agente deben estar implementadas en la capa de orquestación y no solo en el razonamiento del LLM?

a) Porque el LLM no puede generar texto de terminación.
b) Porque el LLM puede generar bucles o condiciones de fallo que no detecta por sí mismo.
c) Porque la capa de orquestación tiene acceso a las herramientas y el LLM no.
d) Porque las condiciones de terminación son costosas computacionalmente.

---

## Nivel 2 — Análisis de casos

**Pregunta 5.** Un equipo diseña un agente de análisis financiero con una herramienta llamada `generar_reporte(cliente_id, periodo)`. La herramienta genera el reporte, lo envía por email al cliente y registra la generación en el sistema de auditoría. ¿Qué anti-patrón describe mejor este diseño?

a) El agente todo-en-uno.
b) Herramienta con efectos secundarios ocultos (no atómica).
c) Confianza ciega en el output de herramientas.
d) Improvisación de herramientas.

---

**Pregunta 6.** Un agente ejecuta la misma acción `buscar_pedidos(cliente="CLT-0231", estado="pendiente")` en las iteraciones 4, 5 y 6 sin cambiar los parámetros. ¿Qué mecanismo de la capa de orquestación debería activarse?

a) Punto de control para confirmación humana.
b) Detección de bucle y terminación con reporte de estado.
c) Compresión del historial de contexto.
d) Escalada automática al siguiente nivel de soporte.

---

**Pregunta 7.** Un agente de soporte tiene que verificar si un cliente tiene contratos vencidos. Tiene disponibles dos herramientas: `buscar_contratos(cliente_id, estado)` y `buscar_en_documentacion(consulta)`. ¿Cuál debe usar y por qué?

a) `buscar_en_documentacion` porque la consulta es semántica.
b) `buscar_contratos` porque la consulta es estructurada y el ID del cliente está disponible.
c) Ambas en paralelo para aumentar el recall.
d) Ninguna: el agente debería razonar sobre los contratos usando su conocimiento interno.

---

## Nivel 3 — Decisión de diseño

**Pregunta 8.** Un agente empresarial debe enviar un email de oferta personalizada a un cliente como paso final de su ciclo. ¿Qué considera el AI Engineer al diseñar esta acción?

Responda desarrollando brevemente: (a) si esta acción requiere punto de control, (b) qué información debe presentarse al operador antes de la confirmación, y (c) qué debe hacer el agente si el operador rechaza la acción.

---

**Pregunta 9.** Un equipo observa que su agente funciona correctamente en staging (100 tickets de prueba) pero en producción, después de una semana, presenta un 15% de tickets con más de 10 iteraciones. El límite configurado es 15 iteraciones. ¿Qué tres causas probables investigaría el AI Engineer y cómo?

---

**Pregunta 10.** Un agente debe procesar solicitudes de crédito. El objetivo es: verificar el historial crediticio del solicitante, consultar la política de aprobación vigente, y emitir una recomendación (aprobar, rechazar, revisar manualmente). Diseñar brevemente: el nivel de autonomía apropiado, los puntos de control necesarios y el sistema de fallback si la herramienta de historial crediticio no responde.

---

## Respuestas

**Respuesta 1:** (b). La capacidad de adaptar el plan en función de los resultados intermedios es la característica definitoria del agente. El tamaño del modelo, el número de herramientas y el nivel de autonomía son variables de diseño, no atributos definitorios.

**Respuesta 2:** (c). La Observation es el resultado generado por el sistema al ejecutar la herramienta indicada en la Action. El LLM genera el Thought y la Action; el sistema genera la Observation.

**Respuesta 3:** (b). El estado es efímero y registra lo que está ocurriendo en la ejecución actual. La memoria persiste entre ejecuciones y proporciona continuidad. Son conceptos distintos con roles distintos en la arquitectura.

**Respuesta 4:** (b). El LLM puede entrar en bucles de razonamiento donde no detecta que está bloqueado, o puede malinterpretar el estado del proceso y no generar la señal de terminación correcta. La capa de orquestación implementa salvaguardas externas al razonamiento del modelo.

**Respuesta 5:** (b). La herramienta hace tres cosas: genera el reporte, lo envía por email y registra en auditoría. No es atómica. Además, el envío del email es un efecto secundario con consecuencias en el mundo externo que el agente puede no anticipar si invoca la herramienta para "solo generar" el reporte.

**Respuesta 6:** (b). La repetición de la misma acción con los mismos parámetros en iteraciones consecutivas es un indicador de bucle. La capa de orquestación debe detectar este patrón y terminar el ciclo con un reporte del estado en que quedó el proceso.

**Respuesta 7:** (b). La consulta tiene un parámetro exacto (cliente_id) y busca datos estructurados (contratos con un estado específico). `buscar_contratos` es la herramienta apropiada. `buscar_en_documentacion` (RAG) es la elección correcta para recuperar políticas o procedimientos por contenido semántico, no para recuperar datos operacionales de un cliente específico.

**Respuesta 8:** (a) Sí requiere punto de control, porque el envío de un email a un cliente es irreversible y afecta a un tercero. (b) El operador debe ver: el destinatario del email, el asunto, el cuerpo completo del mensaje, la información del cliente en que se basa la personalización, y el contexto del ciclo que llevó a esta acción. (c) Si el operador rechaza, el agente no debe reintentar automáticamente. Debe registrar el rechazo, reportar al operador qué quedó pendiente (la oferta no fue enviada) y ofrecer opciones: reformular el mensaje, cancelar la tarea o escalar.

**Respuesta 9:** Tres causas probables: (1) Aparición de tickets de tipos no cubiertos en los casos de prueba, lo que hace que el agente explore más iteraciones buscando herramientas o información no disponible. Diagnóstico: analizar el razonamiento de los tickets con más de 10 iteraciones para identificar patrones comunes. (2) Una herramienta que en staging respondía rápido en producción devuelve resultados incompletos o parciales, haciendo que el agente reintente. Diagnóstico: verificar las tasas de error y tiempo de respuesta de cada herramienta en producción. (3) Tickets con ambigüedad en el objetivo: el agente no puede determinar cuándo ha completado el objetivo y sigue iterando. Diagnóstico: revisar el system prompt y agregar criterios de terminación más explícitos para los casos problemáticos.

**Respuesta 10:** Nivel de autonomía semi-autónomo: el agente puede consultar herramientas y analizar autónomamente, pero la recomendación final (aprobar o rechazar) requiere punto de control antes de ser registrada. Puntos de control necesarios: (1) antes de emitir una recomendación de aprobación o rechazo (acción con consecuencias financieras y legales), (2) si el historial crediticio indica condiciones que la política no cubre explícitamente. Fallback si la herramienta de historial no responde: el agente no debe emitir una recomendación basada en información incompleta. Debe reportar: "No se pudo completar el análisis porque el sistema de historial crediticio no respondió después de [N] intentos. La solicitud de crédito de [cliente] queda pendiente de análisis manual. Información disponible: [datos que sí se obtuvieron]."

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
