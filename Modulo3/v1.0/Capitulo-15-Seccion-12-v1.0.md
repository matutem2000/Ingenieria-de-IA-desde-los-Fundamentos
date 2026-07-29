# Capítulo 15 — Proyecto Integrador

## Sección 12: Checklist final del AI Engineer

Este checklist es el instrumento de revisión definitivo del módulo. Sintetiza los criterios de calidad de todas las dimensiones del Context Engineering en un único documento aplicable a cualquier proyecto propio. No es un resumen de los checklists parciales de capítulos anteriores: cubre exclusivamente los criterios que aplican a un sistema integrado completo.

Usa este checklist antes de pasar cualquier sistema de IA basado en Context Engineering a un entorno de producción. Las preguntas que no puedas responder con "sí" son los aspectos del diseño que necesitan trabajo adicional.

---

### BLOQUE 1 — Instrucciones del sistema y comportamiento base (5 ítems)

- [ ] **1.1** La instrucción del sistema define explícitamente qué puede hacer el asistente, qué no puede hacer, y cómo debe responder en los casos borde más frecuentes.

- [ ] **1.2** Si el sistema tiene múltiples perfiles de usuario (por departamento, rol o tipo de acceso), cada perfil tiene su propia instrucción del sistema con diferencias justificadas por los requisitos del caso de uso, no por preferencias arbitrarias.

- [ ] **1.3** Las instrucciones del sistema se gestionan como datos (fuera del código fuente), pueden actualizarse sin re-desplegar el servicio, y tienen un historial de versiones con fecha y responsable de cada cambio.

- [ ] **1.4** El sistema tiene un proceso de prueba para nuevas versiones de instrucciones del sistema antes de activarlas para todos los usuarios (prueba A/B, canario, o equivalente).

- [ ] **1.5** La instrucción del sistema declara explícitamente la jerarquía de precedencia entre las reglas institucionales y las preferencias del usuario, para los aspectos en que puedan entrar en conflicto.

---

### BLOQUE 2 — Gestión del contexto y la ventana (4 ítems)

- [ ] **2.1** El presupuesto de tokens por turno está definido explícitamente y distribuido entre las zonas del contexto (instrucción del sistema, memoria, RAG, historial de conversación). El sistema no envía contextos que superan el presupuesto definido.

- [ ] **2.2** La estrategia de gestión del historial de conversación (ventana deslizante, resumen incremental, u otra) está documentada. El sistema degrada correctamente cuando el historial supera la capacidad de la ventana: no trunca silenciosamente sin informar al LLM del límite.

- [ ] **2.3** El sistema puede manejar correctamente el caso borde en que la combinación de instrucción del sistema + memoria + RAG + historial supera el presupuesto de tokens: sabe qué zona priorizar y qué zona comprimir cuando el presupuesto se agota.

- [ ] **2.4** El costo estimado de tokens por interacción (promedio y P95) ha sido calculado con datos reales o estimaciones basadas en el tipo de consulta esperada, y es sostenible dentro del presupuesto de la API.

---

### BLOQUE 3 — Memoria persistente (4 ítems)

- [ ] **3.1** El sistema distingue claramente entre qué información merece ser memorizada entre sesiones y qué no. El criterio de selección está documentado y se aplica consistentemente, no discrecionalmente.

- [ ] **3.2** La memoria persistente tiene TTL (tiempo de expiración) configurado para cada tipo de información, y el sistema elimina automáticamente las entradas caducadas.

- [ ] **3.3** El usuario puede solicitar la eliminación de su memoria persistente y el sistema lo honra efectivamente: borra las entradas del almacén y no las recupera en sesiones posteriores.

- [ ] **3.4** La memoria persistente pasa por el mismo filtro de control de acceso que el motor RAG: las entradas que hacen referencia a información a la que el usuario ya no tiene acceso se omiten al construir el contexto.

---

### BLOQUE 4 — Recuperación aumentada (RAG) (6 ítems)

- [ ] **4.1** El tamaño de los chunks y el solapamiento entre chunks han sido calibrados para el tipo de documentos que se indexan. El tamaño por defecto (400 tokens con solapamiento de 80) es un punto de partida, no un valor definitivo para todos los casos.

- [ ] **4.2** Cada fragmento del índice vectorial tiene metadatos de origen completos: nombre del documento, sección, fecha de última modificación, propietario y nivel de clasificación.

- [ ] **4.3** El proceso de actualización del índice cuando un documento cambia está automatizado y verificado: el sistema elimina los fragmentos de la versión anterior antes de indexar la versión nueva, y verifica que la eliminación fue exitosa.

- [ ] **4.4** El control de acceso se aplica en el nivel del recuperador (antes de que los fragmentos lleguen al contexto del LLM), no solo en el nivel de la salida del LLM.

- [ ] **4.5** El sistema puede responder correctamente cuando no encuentra información relevante en el índice: no inventa respuestas, indica explícitamente que no encontró documentación aplicable y sugiere una alternativa (persona de contacto, sistema alternativo).

- [ ] **4.6** Las respuestas del sistema que usan información de documentos incluyen siempre la referencia al documento fuente (nombre, sección, fecha). El usuario puede verificar la fuente sin esfuerzo adicional.

---

### BLOQUE 5 — Herramientas y MCP (4 ítems)

- [ ] **5.1** Cada herramienta expuesta al LLM tiene una especificación completa: nombre, descripción, parámetros con tipos, respuesta esperada, permisos requeridos y comportamiento ante fallo.

- [ ] **5.2** Las herramientas que producen efectos en sistemas externos (creación, modificación, eliminación, notificación) requieren confirmación explícita del usuario antes de ejecutarse, excepto cuando el caso de uso justifica la ejecución automática y esa decisión está documentada.

- [ ] **5.3** El sistema tiene comportamiento de degradación controlada para cada herramienta: cuando una herramienta falla, el usuario recibe una respuesta útil (no un error técnico) y una alternativa de acción.

- [ ] **5.4** El acceso a herramientas está controlado por el perfil del usuario: las herramientas que requieren permisos específicos no aparecen como disponibles para usuarios sin esos permisos (no solo fallan cuando se intentan usar).

---

### BLOQUE 6 — Agentes (4 ítems, solo si el sistema incluye agentes)

- [ ] **6.1** La decisión de usar un agente en lugar de un flujo fijo de herramientas está justificada: el caso de uso requiere condicionalidad en la secuencia de pasos que no puede definirse antes de ejecutar.

- [ ] **6.2** El agente tiene un límite máximo de iteraciones configurado. Cuando alcanza ese límite sin converger en una respuesta, presenta un resumen de lo que encontró y escala a un humano, en lugar de fallar con un error técnico.

- [ ] **6.3** La instrucción del sistema del agente define explícitamente el proceso de trabajo que debe seguir (pasos, criterios de decisión, condiciones de parada), no solo las capacidades que tiene.

- [ ] **6.4** Las herramientas del agente tienen mecanismos de detección de fallos recurrentes: si una herramienta falla dos veces consecutivas, el agente la marca como no disponible y continúa el análisis sin ella o informa que no puede completar la tarea sin esa información.

---

### BLOQUE 7 — Observabilidad (5 ítems)

- [ ] **7.1** Cada interacción genera una traza completa: entrada del usuario, contexto enviado al LLM (con tokens por zona), respuesta del LLM, herramientas invocadas, fuentes RAG recuperadas, y latencias por etapa.

- [ ] **7.2** Las trazas son inmutables y tienen un período de retención definido que cumple los requisitos de auditoría del caso de uso.

- [ ] **7.3** El sistema monitorea latencia (P50 y P95 por etapa), tasa de error por componente, y costo de tokens por usuario/departamento, con umbrales de alerta configurados.

- [ ] **7.4** El equipo de operaciones puede diagnosticar un incidente del sistema a partir de las trazas almacenadas, sin necesidad de reproducir la interacción problemática.

- [ ] **7.5** Los cambios en instrucciones del sistema, en el índice RAG y en la configuración de herramientas quedan registrados en un log de administración separado de las trazas de interacción.

---

### BLOQUE 8 — Seguridad (5 ítems)

- [ ] **8.1** El control de acceso opera en el nivel de recuperación: los documentos a los que el usuario no tiene acceso nunca llegan al contexto del LLM, no solo son filtrados en la salida.

- [ ] **8.2** El sistema tiene un mecanismo de detección de prompt injection sobre la entrada del usuario, con respuesta de bloqueo y registro del intento ante detección positiva.

- [ ] **8.3** El filtro de salida verifica que las respuestas del LLM no contienen: datos personales sensibles fuera del alcance del usuario, referencias a documentos no recuperados en ese turno, ni instrucciones que sugieran manipulación exitosa del sistema.

- [ ] **8.4** El equipo tiene un proceso documentado de respuesta ante un incidente de seguridad del sistema de IA (acceso no autorizado a documentos, exposición de datos, prompt injection exitosa).

- [ ] **8.5** Los documentos de alta clasificación (restringido) generan alertas de auditoría en tiempo real al responsable de cumplimiento cuando son accedidos, además de quedar en la traza general.

---

### BLOQUE 9 — Operación y evolución (3 ítems)

- [ ] **9.1** La estrategia de despliegue es incremental: el sistema fue validado con un subconjunto de usuarios antes de operar con toda la organización.

- [ ] **9.2** El proceso de actualización de la base documental RAG está automatizado o tiene un calendario explícito de revisión manual, y el responsable de mantenerla actualizada está identificado por departamento.

- [ ] **9.3** El equipo tiene un proceso de revisión periódica de las instrucciones del sistema por parte del responsable de negocio de cada departamento, con una frecuencia adecuada al ritmo de cambio de las políticas del caso de uso.

---

### Cómo usar este checklist en producción

Este checklist tiene 40 ítems. No todos son bloqueantes para el lanzamiento inicial: algunos son críticos (control de acceso, trazas de auditoría, comportamiento ante herramientas fallidas) y otros son mejoras que pueden incorporarse después del lanzamiento (TTL de memoria, pruebas A/B de instrucciones).

Antes de llevar cualquier sistema de IA a producción, clasifica los ítems no cumplidos en dos categorías:

**Bloqueantes:** ítems sin los cuales el sistema expone datos de forma incorrecta, no puede auditarse, o tiene comportamientos impredecibles ante fallos. Los bloqueantes deben cumplirse antes del lanzamiento.

**Post-lanzamiento:** ítems que mejoran la calidad, la operabilidad o la experiencia del usuario pero cuya ausencia no compromete la seguridad ni la confiabilidad básica del sistema. Estos pueden incorporarse en las primeras semanas de operación.

El criterio de clasificación es tuyo, no de este libro. Conoces tu caso de uso, tu organización y tus usuarios. Lo que es post-lanzamiento para un chatbot interno de bajo riesgo puede ser bloqueante para un sistema que maneja datos regulados.

---

Con el checklist completo, las dos secciones finales del capítulo cierran el módulo.
