# Capítulo 12 — Context Engineering Empresarial

## Sección 14: Autoevaluación

Las siguientes preguntas cubren los conceptos centrales del capítulo. Para cada pregunta se indica el nivel de dificultad y la sección de referencia donde se desarrolla el concepto.

---

### Preguntas de comprensión conceptual

**1.** ¿Cuál es la diferencia fundamental entre el Context Engineering para un proyecto individual y el Context Engineering empresarial? ¿Qué tipos de problemas aparecen en el segundo que no existen en el primero?
*(Nivel básico — Sección 01)*

**2.** Explica las tres dimensiones del conocimiento corporativo que son relevantes para el diseño del contexto: estructura, vigencia y autoridad. Para cada dimensión, describe un problema concreto que puede aparecer en un sistema de IA empresarial si esa dimensión no se gestiona correctamente.
*(Nivel básico — Sección 02)*

**3.** Describe la arquitectura de capas de contexto: qué contiene cada capa, quién la administra y cómo interactúan entre sí. ¿Por qué esta arquitectura resuelve el problema del silo de contexto sin sacrificar la especificidad de cada equipo?
*(Nivel intermedio — Sección 03)*

**4.** ¿Qué es el gobierno del conocimiento y por qué determina la calidad del contexto a largo plazo, más que la arquitectura técnica inicial? Describe las cuatro dimensiones del framework de gobierno del conocimiento presentado en el capítulo.
*(Nivel intermedio — Sección 04)*

**5.** Describe los cuatro patrones de integración entre el sistema de IA y los sistemas corporativos. Para cada uno, identifica un caso de uso donde es el patrón correcto y uno donde no lo es.
*(Nivel intermedio — Sección 05)*

---

### Preguntas de aplicación

**6.** Una organización tiene cinco sistemas de IA construidos independientemente por cinco equipos distintos. El equipo de ventas cambia su política de descuentos; el cambio se comunica al asistente de ventas pero no a los asistentes de soporte, recursos humanos, operaciones ni finanzas. Tres meses después, un cliente recibe información contradictoria de tres canales distintos.

   a) ¿Qué anti-patrón describe esta situación?
   b) ¿Qué elemento de arquitectura o proceso hubiera evitado el problema?
   c) ¿Cómo se diseña el mecanismo de propagación de actualizaciones para evitar que esto ocurra?
*(Nivel intermedio — Sección 06)*

**7.** El AI Engineer de una empresa detecta que el tiempo de respuesta del asistente de IA ha subido de 2 segundos a 8 segundos en tres meses, sin cambios en la infraestructura. Investigando, encuentra que el system prompt pasó de 800 tokens a 4.200 tokens por acumulación de instrucciones ad hoc. El tamaño del historial de conversación que el sistema incluye también creció porque nadie definió un límite.

   a) ¿Cuál es el diagnóstico técnico del problema?
   b) ¿Qué decisiones de diseño del contexto se tomaron incorrectamente?
   c) Proponer al menos dos medidas concretas para resolver el problema.
*(Nivel avanzado — Secciones 07 y 09)*

**8.** Un director de operaciones pregunta: "¿Cómo sé si nuestro sistema de IA está generando valor o solo consumiendo presupuesto?". El equipo de IA desplegó el sistema hace cuatro meses pero no estableció un baseline de métricas antes del despliegue.

   a) ¿Qué métricas de negocio son más relevantes para responder esta pregunta?
   b) Si no existe un baseline, ¿es posible establecer una estimación retrospectiva? ¿Cómo?
   c) ¿Qué proceso debe implementar el equipo ahora para que esta situación no se repita?
*(Nivel avanzado — Sección 08)*

---

### Preguntas de diseño

**9.** Una empresa farmacéutica con 600 empleados quiere implementar un sistema de IA para su equipo de asuntos regulatorios (30 personas), que trabaja con regulaciones de la FDA, EMA y otros organismos internacionales. El conocimiento regulatorio es altamente específico, cambia frecuentemente y tiene implicaciones legales si se usa información desactualizada.

   Diseña la arquitectura de contexto para este caso incluyendo:
   - Las fuentes de conocimiento a indexar y su clasificación en capas.
   - El proceso de actualización del conocimiento regulatorio.
   - Las métricas de calidad del contexto más relevantes para este caso específico.
   - Al menos un riesgo específico del dominio regulatorio que el diseño debe mitigar.

*(Nivel avanzado — Secciones 03, 04, 08)*

**10.** En el caso de estudio de TechServe, el incidente del silo de contexto en el mes nueve fue el catalizador para crear la plataforma corporativa. Considera un escenario alternativo: TechServe hubiera diseñado la plataforma corporativa desde el inicio, antes de desplegar el primer asistente. ¿Qué habría sido diferente en el diseño del primer asistente de soporte? ¿La plataforma corporativa desde el inicio habría acelerado o ralentizado el despliegue del primer asistente? Argumenta tu respuesta.

*(Nivel avanzado — Sección 10)*

---

### Respuestas de referencia (preguntas seleccionadas)

**Respuesta de referencia para la pregunta 6:**

a) El anti-patrón es el **silo de contexto por equipo**, donde cada sistema de IA gestiona su conocimiento de forma independiente sin mecanismos de coordinación horizontal. La consecuencia natural es que los cambios en el conocimiento corporativo no se propagan a todos los sistemas.

b) El elemento que hubiera evitado el problema es la **capa corporativa con mecanismo de propagación de actualizaciones**. Si la política de descuentos está en el núcleo corporativo compartido —no replicada en cinco bases de conocimiento independientes—, un cambio en la fuente autorizada se propaga automáticamente a todos los sistemas.

c) El mecanismo de propagación puede implementarse de dos formas complementarias. La primera es técnica: suscripción de las bases vectoriales departamentales a eventos de cambio en el núcleo corporativo, desencadenando reindexación automática cuando la fuente autorizada cambia. La segunda es de proceso: cuando cualquier responsable actualiza un documento de política, el sistema notifica automáticamente a todos los propietarios de capas departamentales que usan ese documento, solicitando confirmación de que sus capas fueron revisadas.

**Respuesta de referencia para la pregunta 8b:**

Si no existe un baseline previo, es posible construir una estimación retrospectiva aunque con menor precisión. Las opciones son: (1) solicitar al equipo de soporte una estimación del tiempo de resolución promedio antes del sistema de IA, basada en su experiencia y en registros históricos del sistema de tickets; (2) comparar el desempeño del sistema de IA con el desempeño de los agentes que no lo usan, si existen —si solo parte del equipo usa el sistema, la comparación entre el grupo que lo usa y el que no lo usa proporciona una estimación del impacto—; (3) usar benchmarks de la industria para organizaciones similares como referencia general. Ninguna de estas opciones reemplaza un baseline medido; solo proporcionan estimaciones con incertidumbre que deben comunicarse como tales.

---

### Reflexión final

El Context Engineering empresarial es el área donde la ingeniería de IA más se parece a la ingeniería de sistemas complejos en general: los problemas más difíciles no son los más técnicos sino los que emergen de la interacción entre el sistema técnico y la organización humana que lo usa y mantiene. El AI Engineer que comprende esa interacción y puede diseñar para ella —no solo para el caso técnico ideal— es el que genera valor sostenido en organizaciones reales.
