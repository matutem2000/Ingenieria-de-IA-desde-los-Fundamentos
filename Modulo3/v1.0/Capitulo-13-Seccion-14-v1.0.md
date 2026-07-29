# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 14: Autoevaluación

Las siguientes preguntas permiten verificar la comprensión de los conceptos centrales del capítulo. Para cada pregunta, intenta formular una respuesta antes de consultar la clave de respuestas.

---

**Pregunta 1**

Un sistema de IA en producción tiene 99.8% de disponibilidad, latencia p95 de 1.8 segundos y costo por solicitud dentro del presupuesto. El equipo de negocio reporta que la satisfacción de los usuarios cayó 12 puntos en el último mes. ¿Qué dimensión de observabilidad está faltando y qué técnica usarías para diagnosticar el problema?

---

**Pregunta 2**

¿Cuál es la diferencia entre monitoreo y observabilidad en el contexto de sistemas de IA? Da un ejemplo concreto de un problema que el monitoreo no detectaría pero la observabilidad sí.

---

**Pregunta 3**

Estás implementando un evaluador LLM-as-judge para medir la groundedness de las respuestas de un asistente de soporte técnico. Describe tres limitaciones conocidas de este enfoque y qué medidas tomarías para mitigar cada una.

---

**Pregunta 4**

Un sistema de RAG que lleva ocho meses en producción comienza a producir respuestas con información desactualizada sobre los productos de la empresa. El sistema técnico funciona correctamente: latencia normal, sin errores. ¿Qué tipo de degradación es este? ¿Cómo lo detectarías con las herramientas de observabilidad del capítulo?

---

**Pregunta 5**

¿Para qué sirve el golden set? ¿Por qué no es suficiente comparar las métricas del sistema solo con las del período anterior (semana a semana)?

---

**Pregunta 6**

Un agente en producción está ejecutando en promedio 18 pasos por solicitud cuando fue diseñado para operar en 4-8 pasos. ¿A qué nivel de alerta corresponde esta señal según el framework del capítulo? ¿Cuáles son las hipótesis de causa raíz más probables y cómo las investigarías?

---

**Pregunta 7**

¿Cuál es la diferencia entre la trazabilidad de contexto para sistemas de IA y el logging tradicional de software? ¿Por qué el logging de eventos no es suficiente para diagnosticar problemas de calidad en sistemas de IA?

---

**Pregunta 8**

Un equipo implementó un dashboard con 15 métricas, todas actualizándose en tiempo real. Hay 8 alertas activas la mayoría de los días. El equipo responde a las alertas más urgentes y el resto se ignoran. ¿Qué anti-patrón describe esta situación? ¿Cómo lo corregirías?

---

**Pregunta 9**

Explica el concepto de "deriva del modelo" (model drift). ¿Por qué es particularmente difícil de detectar? ¿Qué mecanismo del capítulo permite detectarlo de forma más fiable?

---

**Pregunta 10**

Una empresa quiere implementar A/B testing para comparar dos versiones de su sistema de recuperación RAG: la versión actual (sin re-ranking) y una nueva versión (con re-ranking semántico). La empresa tiene 500 solicitudes por día. ¿Cuáles son los desafíos específicos de este experimento y qué recomendaciones darías para que produzca resultados confiables?

---

### Clave de respuestas

**Respuesta 1**

La dimensión faltante es la observabilidad de la calidad: no se están midiendo métricas que indiquen si las respuestas son buenas. Las métricas operacionales (disponibilidad, latencia, costo) están en verde porque miden si el sistema responde, no si responde bien.

Para diagnosticar el problema: implementar un pipeline de evaluación LLM-as-judge para medir groundedness y relevancia sobre una muestra del tráfico reciente. Construir un golden set con el equipo de negocio y ejecutarlo para comparar con el comportamiento esperado. Revisar las trazas de contexto de las solicitudes de los últimos 30 días para detectar si los documentos recuperados tienen fechas de modificación antiguas (posible deriva del contexto).

**Respuesta 2**

El monitoreo recolecta métricas predefinidas sobre comportamientos conocidos. La observabilidad es la capacidad de inferir el estado interno del sistema a partir de sus salidas, incluyendo comportamientos no previstos en el diseño.

Ejemplo: el monitoreo puede detectar que el sistema devuelve HTTP 200 con latencia aceptable. No puede detectar que el sistema está respondiendo preguntas sobre precios con tarifas desactualizadas porque el documento de tarifas en la base vectorial tiene seis meses de antigüedad. La observabilidad —concretamente la trazabilidad de contexto con metadatos de fecha de los documentos recuperados— sí puede detectarlo.

**Respuesta 3**

Primera limitación: sesgo de autopreferencia. Si el evaluador y el sistema evaluado son del mismo modelo o familia de modelos, el evaluador tiende a calificar más alto las respuestas de ese estilo. Mitigación: usar un modelo evaluador diferente al modelo del sistema, o calibrar el evaluador contra evaluaciones humanas para detectar y corregir el sesgo.

Segunda limitación: incapacidad para detectar alucinaciones sobre conocimiento externo al contexto. El evaluador puede confirmar que la respuesta es consistente con el contexto recuperado sin detectar que el contexto recuperado contiene información desactualizada. Mitigación: complementar con verificación cruzada contra fuentes autorizadas para las categorías de afirmaciones de mayor riesgo.

Tercera limitación: sensibilidad al formato del prompt de evaluación. Cambios menores en el prompt del evaluador pueden producir scores significativamente diferentes. Mitigación: establecer un prompt de evaluación canónico, versionarlo junto con el sistema, y validar cualquier cambio al prompt contra la calibración humana de referencia antes de adoptarlo.

**Respuesta 4**

Es deriva del contexto (context drift): el conocimiento en la base vectorial se desactualizó porque los documentos de productos fueron actualizados en su fuente original pero no fueron reindexados en el sistema RAG.

Detección: la trazabilidad de contexto con metadatos de fecha de los documentos recuperados habría mostrado que los documentos con mayor frecuencia de recuperación tienen fechas de modificación de hace varios meses, cuando la empresa actualiza sus productos regularmente. El golden set ejecutado periódicamente habría mostrado una caída en el score de exactitud para las consultas sobre productos actualizados.

**Respuesta 5**

El golden set sirve para tener una referencia absoluta de calidad: un conjunto de casos con respuestas correctas conocidas que se ejecuta periódicamente y cuyos resultados se comparan siempre contra la línea base de lanzamiento, no solo contra el período anterior.

Si se comparan las métricas solo semana a semana, el sistema puede degradarse gradualmente sin que ninguna comparación individual muestre una diferencia significativa. Cada semana, el nuevo nivel (ligeramente peor) se convierte en la referencia para la siguiente comparación. Al cabo de seis meses, el sistema puede estar significativamente peor que en el lanzamiento sin que ninguna comparación semanal haya generado una alerta. El golden set, al comparar siempre contra la línea base absoluta, detecta esta degradación acumulada.

**Respuesta 6**

Corresponde a una alerta de Nivel 2 (revisión activa en 24-48 horas): el número de pasos es más del doble del diseñado, lo que indica un problema sistémico que requiere investigación activa pero no necesariamente acción inmediata si el sistema sigue produciendo respuestas y el costo es manejable. Si el costo proyectado o el tiempo de respuesta se vuelven inaceptables, escalaría a Nivel 3.

Hipótesis de causa raíz: (1) una herramienta del agente está fallando silenciosamente y devolviendo resultados vacíos o erróneos, lo que lleva al agente a repetir la llamada con parámetros ligeramente diferentes; (2) el criterio de terminación del ciclo agentivo no es suficientemente preciso para los tipos de consulta que el sistema está recibiendo actualmente; (3) hubo un cambio en el sistema de planificación que amplió el espacio de acciones exploradas.

Para investigar: revisar las trazas de los flujos con más de 15 pasos, identificar qué herramientas se repiten, verificar los resultados de esas herramientas, comparar la distribución de tipos de consulta actual con la histórica para detectar si hay nuevos tipos de consulta que el agente no sabe resolver eficientemente.

**Respuesta 7**

El logging de eventos registra qué hizo el sistema: "el sistema llamó a la API del modelo y recibió una respuesta". La trazabilidad de contexto registra con qué información lo hizo: qué documentos tenía disponibles, qué versión del system prompt estaba activa, qué herramientas ejecutó el agente.

La diferencia es crítica para el diagnóstico de problemas de calidad. Si el sistema produce una respuesta incorrecta, el log de eventos dice que el sistema respondió; la traza de contexto dice qué tenía disponible para generar esa respuesta. El diagnóstico de calidad requiere la segunda información, no la primera. El logging solo no puede responder "¿por qué el modelo respondió eso?" porque no tiene la información sobre el contexto con el que el modelo tomó esa decisión.

**Respuesta 8**

Describe el anti-patrón de "dashboard sin umbral" combinado con el anti-patrón de "alertas sin dueño" y la consecuente "fatiga de alertas". Cuando hay demasiadas alertas activas y algunas se ignoran sistemáticamente, el sistema de alertas deja de funcionar: cuando aparece una alerta crítica, no recibe la atención que merece porque el equipo está acostumbrado a ignorar las alertas.

Corrección: reducir el número de alertas a las que el equipo puede atender en un día normal. Revisar cada alerta existente: ¿es Nivel 1 (logging), Nivel 2 (revisión activa) o Nivel 3 (acción inmediata)? Las de Nivel 1 deberían no generar notificaciones activas, sino solo aparecer en el dashboard operacional. Asignar un dueño explícito a cada tipo de alerta. Definir un proceso de resolución explícita: cada alerta se cierra cuando se investiga y se toma una decisión, no cuando la métrica mejora por sí sola.

**Respuesta 9**

La deriva del modelo ocurre cuando el comportamiento del modelo cambia sin que el sistema haya sido modificado por el equipo, típicamente porque el proveedor actualizó silenciosamente la versión del modelo de producción.

Es difícil de detectar porque no hay ningún evento en el sistema que la señale: el código no cambió, la base de conocimiento no cambió, la infraestructura no cambió. Los síntomas son cambios en el tono, la longitud, el nivel de precaución o la capacidad de seguir instrucciones complejas del model — cambios que solo son detectables al comparar el comportamiento actual con el histórico.

El mecanismo más fiable para detectarlo es el golden set ejecutado periódicamente y comparado contra la línea base. Si el mismo conjunto de casos que antes producía scores de 0.90 ahora produce consistentemente 0.82, hay evidencia de un cambio en el modelo que debe investigarse, incluyendo verificar con el proveedor si hubo una actualización.

**Respuesta 10**

Desafíos: con 500 solicitudes por día y un split 50/50, cada variante recibe 250 solicitudes por día. Para detectar una diferencia de 0.05 puntos en groundedness (un efecto size razonable) con 80% de potencia estadística y un nivel de significancia del 5%, se necesitan aproximadamente 1,000-1,500 solicitudes por variante, lo que requiere 4-6 semanas de experimento — un período durante el cual el sistema puede tener cambios externos (actualizaciones de la base vectorial, cambios en los patrones de consulta) que contaminan el experimento.

Recomendaciones: (1) definir antes del experimento el efecto mínimo detectable y el tamaño de muestra necesario, y comprometerse a no evaluar el experimento antes de alcanzarlo; (2) asignar usuarios, no solicitudes, a las variantes para evitar que el mismo usuario experimente los dos sistemas; (3) monitorear las métricas secundarias (latencia, costo) además de la métrica primaria (groundedness); (4) registrar cualquier evento externo durante el experimento que pueda contaminar los resultados; (5) no concluir el experimento antes del tamaño de muestra necesario aunque los resultados intermedios parezcan significativos.
