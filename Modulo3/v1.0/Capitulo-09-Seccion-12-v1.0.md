# Capítulo 09 — Arquitecturas Multiagente

## Sección 12 — Checklist del AI Engineer

Esta checklist consolida los criterios y verificaciones de diseño del capítulo en un formato accionable. Está organizada en tres momentos del proceso: antes de diseñar el sistema (decisión de arquitectura), durante el diseño (calidad del diseño), y antes de pasar a producción (verificación operacional).

No es una lista de control mecánica. Cada ítem es una pregunta que requiere una respuesta genuina, no una casilla para marcar. Si no puedes responder una pregunta con precisión, esa es la señal de que esa dimensión del sistema necesita más trabajo antes de avanzar.

---

### Bloque 1: Decisión de arquitectura

Completa este bloque antes de comprometerte con una arquitectura multiagente. Si ninguno de los primeros cuatro ítems produce una respuesta afirmativa, considera si un agente único bien diseñado resuelve el problema de forma más simple.

- [ ] **Paralelismo justificado.** La tarea tiene subtareas independientes que se benefician de ejecución simultánea. Puedo nombrar cuáles son y demostrar que son genuinamente independientes.

- [ ] **Especialización justificada.** Las distintas dimensiones de la tarea requieren conocimiento, herramientas o instrucciones de sistema fundamentalmente distintos. Puedo describir en qué difieren los dominios de trabajo de cada agente previsto.

- [ ] **Verificación independiente justificada.** La criticidad del output justifica que un segundo agente evalúe el trabajo del primero antes de que sea aceptado. Puedo articular qué consecuencias tiene un error en el output.

- [ ] **Distribución de contexto justificada.** El volumen de información que la tarea requiere procesar excede lo que puede mantenerse en una sola ventana de contexto con calidad aceptable.

- [ ] **Agente único descartado explícitamente.** Intenté resolver el problema con un agente único y encontré límites específicos. Puedo describir cuáles son esos límites.

---

### Bloque 2: Diseño de los agentes

Completa este bloque para cada agente del sistema antes de implementarlo.

- [ ] **Rol limitado.** El agente tiene una función específica y delimitada. Puedo describirla en una oración sin usar "y también".

- [ ] **Instrucción de sistema coherente con el rol.** La instrucción de sistema expresa el rol con precisión: incluye el objetivo, las restricciones y el formato de output esperado. No incluye capacidades que el agente no necesita para su función.

- [ ] **Herramientas mínimas necesarias.** El agente tiene acceso solo a las herramientas que su función específicamente requiere. Puedo justificar por qué cada herramienta incluida es necesaria.

- [ ] **Formato de output definido.** El output que este agente produce tiene un esquema definido, conocido por el agente que lo consumirá. No hay ambigüedad sobre qué estructura tendrá el resultado.

- [ ] **Sin estado interno entre tareas.** El agente opera sobre el input que recibe y el estado compartido al que tiene acceso. No acumula estado interno que dependa de interacciones anteriores. Si necesita información de contexto anterior, está disponible en el estado compartido.

---

### Bloque 3: Diseño del sistema

Completa este bloque para el sistema en su conjunto.

- [ ] **Topología documentada.** Existe un diagrama del sistema que muestra todos los agentes, sus conexiones, la dirección del flujo de información y el orden de ejecución (paralelo o secuencial para cada parte del sistema).

- [ ] **Dependencias explícitas.** Las dependencias entre agentes (el agente B requiere el output del agente A) están explicitadas en el diagrama y en la estructura del plan de ejecución.

- [ ] **Protocolos de mensajes definidos.** Para cada conexión entre agentes existe un esquema definido para el mensaje. Los tipos de mensaje (tarea, resultado, error) están especificados.

- [ ] **Supervisión diseñada.** El sistema tiene un mecanismo para detectar cuando un agente produce un output de calidad inaceptable. Ese mecanismo puede ser automático (agente supervisor) o manual (revisión humana), pero está diseñado explícitamente, no asumido implícitamente.

- [ ] **Sin roles solapados.** No hay dos agentes que hacen el mismo trabajo ni vacíos donde ningún agente es responsable de una parte necesaria de la tarea.

---

### Bloque 4: Memoria compartida y estado

- [ ] **Almacén de estado diseñado.** Existe una definición del almacén de estado compartido: qué campos contiene, quién puede leer cada campo, quién puede escribir cada campo.

- [ ] **Conflictos de escritura resueltos.** Si dos agentes pueden escribir en el mismo campo simultáneamente, hay un mecanismo para resolver ese conflicto (serialización, versionamiento con control optimista, o separación de escrituras por diseño).

- [ ] **Contexto mínimo por agente.** Cada agente recibe el contexto mínimo necesario para su subtarea, no el estado completo del sistema. El orquestador construye ese contexto mínimo como parte del mensaje de tarea.

- [ ] **Privacidad y aislamiento.** Cada agente tiene acceso de lectura y escritura solo a las partes del estado que su función requiere. No hay acceso generalizado a todo el estado para todos los agentes.

---

### Bloque 5: Resiliencia operacional

- [ ] **Fallos de agentes individuales manejados.** Cada agente tiene una estrategia de manejo de error: reintentos con backoff, agente de respaldo, o comportamiento degradado definido. El fallo de un agente no colapsa el sistema completo.

- [ ] **Timeouts definidos.** Cada espera del sistema tiene un tiempo máximo. No hay esperas indefinidas.

- [ ] **Idempotencia en entregas duplicadas.** Si un mensaje es entregado dos veces, el procesamiento produce el mismo resultado en ambas entregas. El sistema verifica identificadores de mensaje antes de procesar.

- [ ] **Observabilidad implementada.** El sistema registra, como mínimo: cada mensaje enviado y recibido entre agentes (con marca temporal), el estado de cada subtarea (iniciada, completada, con error) y el costo de tokens por agente y por tarea.

- [ ] **Límites de reintentos definidos.** Hay un número máximo de reintentos para cada agente. Cuando se alcanza ese límite, el sistema reporta el fallo en lugar de continuar reintentando indefinidamente.

---

### Bloque 6: Costo y viabilidad

- [ ] **Estimación de costo por tarea.** Existe una estimación del número de llamadas al modelo de lenguaje que realiza el sistema por tarea, y del costo total de tokens esperado.

- [ ] **Estimación de latencia.** Existe una estimación de la latencia total esperada por tarea, considerando el paralelismo y los tiempos de cada agente.

- [ ] **Costo justificado por valor.** El costo adicional de la arquitectura multiagente (versus un agente único) está justificado por el valor que añade: menor latencia, mayor calidad, mayor cobertura. Ese análisis se hizo explícitamente.

- [ ] **Plan de monitoreo de costo en producción.** Hay un mecanismo para detectar cuando el costo real en producción se desvía significativamente de la estimación. Las desviaciones grandes activan una revisión del diseño.

---

*La sección 13 resume los conceptos centrales del capítulo en una visión integrada. Un buen resumen no es una lista de lo que se cubrió: es la articulación del marco mental que el lector debe llevarse.*
