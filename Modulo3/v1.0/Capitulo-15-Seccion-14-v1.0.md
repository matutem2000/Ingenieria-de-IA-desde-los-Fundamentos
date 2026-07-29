# Capítulo 15 — Proyecto Integrador

## Sección 14: Evaluación final

Esta evaluación está diseñada para que puedas aplicarla sin un instructor. No mide si recuerdas definiciones: mide si puedes aplicar los conceptos del módulo para resolver problemas nuevos. La escala de evaluación es simple: si puedes responder cada pregunta sin consultar el material, completaste el módulo. Si necesitas releer una sección para responder, esa sección merece una segunda lectura.

Dedica entre 60 y 90 minutos a esta evaluación. Responde en papel o en un documento separado antes de revisar las notas de contraste al final.

---

### Parte A — Preguntas de aplicación directa

Estas preguntas tienen respuestas verificables. No son preguntas de opinión.

**A1.** Un sistema de IA para atención al cliente recibe esta consulta de un usuario: "¿Cuánto tiempo tardan los envíos a las Islas Canarias?" El sistema tiene un índice RAG con el catálogo de productos y las políticas de envío. El motor RAG devuelve tres fragmentos: uno de la política de envíos peninsulares (no aplica), uno del FAQ de Canarias con los tiempos correctos, y uno de una actualización de precios de 2024 (no aplica). El LLM incluye información del fragmento de precios de 2024 en su respuesta porque encuentra una mención a "Canarias" en ese fragmento.

¿Qué falla en el sistema y en qué etapa? ¿Qué cambiarías en el diseño para evitar este tipo de error?

---

**A2.** Un agente de análisis de reclamos de seguros tiene acceso a cuatro herramientas: `consultar_poliza`, `verificar_historial_siniestros`, `calcular_indemnizacion`, y `aprobar_pago`. El agente procesa un reclamo y propone aprobar el pago automáticamente sin mostrar el cálculo al operador.

¿Qué principio de diseño de agentes viola este comportamiento? ¿Cómo modificarías la instrucción del sistema del agente para corregirlo?

---

**A3.** Un sistema de asistente médico interno para enfermeros tiene una instrucción del sistema que incluye: "Proporciona información clínica detallada sobre medicamentos, incluyendo dosis y contraindicaciones." Un enfermero con credenciales válidas pregunta sobre la dosis máxima de un medicamento controlado. El sistema responde correctamente. Un estudiante de enfermería que tiene acceso al sistema (para consultas de aprendizaje) hace la misma pregunta.

¿Qué mecanismo de diseño del módulo aplica directamente a este caso? ¿Qué cambios concretos implementarías?

---

**A4.** Un equipo construyó un sistema de IA con las siguientes características:
- El historial de conversación se conserva completo, sin límite.
- La instrucción del sistema ocupa 3.000 tokens.
- El sistema no usa RAG.
- El modelo tiene una ventana de 8.000 tokens.

Después de 15 turnos de conversación, el sistema empieza a "olvidar" instrucciones del sistema y su comportamiento se vuelve inconsistente.

Explica exactamente por qué ocurre esto y propón dos estrategias para resolverlo sin cambiar el modelo.

---

**A5.** Un sistema de asistente empresarial tiene un módulo de memoria persistente que almacena todo lo que el usuario menciona en sus conversaciones. Un usuario menciona, de pasada: "Esta semana estoy de mal humor porque mi jefe me llamó la atención." El sistema almacena ese fragmento como memoria.

Identifica al menos dos problemas que ese comportamiento puede causar y explica cómo el diseño correcto del módulo de memoria los evita.

---

### Parte B — Preguntas de diseño

Estas preguntas no tienen una única respuesta correcta. Se evalúan por la solidez del razonamiento.

**B1.** Una startup de legaltech quiere construir un asistente que ayude a abogados a revisar contratos. El asistente debe identificar cláusulas problemáticas según la ley argentina, comparar el contrato con plantillas estándar del estudio, y sugerir modificaciones. Los contratos son confidenciales y no deben mezclarse entre clientes.

Define la arquitectura en términos de los siete componentes del módulo. Para cada componente, explica su función específica en este caso. Identifica cuál es la decisión de diseño más crítica de esta arquitectura y justifica por qué.

---

**B2.** Un sistema de asistente de soporte técnico fue desplegado hace seis meses. En las últimas dos semanas, el equipo nota que las respuestas sobre un producto específico son incorrectas: el producto tuvo una actualización importante y el asistente sigue respondiendo sobre la versión anterior.

Describe paso a paso cómo diagnosticarías este problema usando las herramientas de observabilidad del módulo. ¿Qué trazas buscarías? ¿Qué indicadores mirarías? ¿Cuál es la causa raíz más probable y cómo la resolverías?

---

**B3.** Un equipo propone la siguiente arquitectura para un asistente de recursos humanos: el LLM tiene acceso a una herramienta que consulta directamente la base de datos de RRHH sin filtros de acceso, y el sistema filtra la salida para no mostrar salarios u otros datos sensibles en la respuesta.

Evalúa críticamente esta arquitectura desde el punto de vista de seguridad. ¿Qué riesgo específico introduce? ¿Qué arquitectura alternativa sería más robusta y por qué?

---

### Notas de contraste

Estas notas no son las respuestas "correctas". Son los aspectos más importantes que una respuesta de calidad debería incluir. Úsalas para evaluar la completitud de tus propias respuestas.

**A1:** La falla es en el motor RAG o en el proceso de construcción del contexto: el fragmento de precios de 2024 no debería haber pasado al contexto porque no es relevante para la consulta de envíos a Canarias. El problema puede estar en el chunking (el fragmento mezcla información de precios con menciones geográficas) o en el k de la recuperación (se recuperan demasiados fragmentos sin suficiente filtro de relevancia). La solución más robusta incluye re-ranking de fragmentos por relevancia directa y la instrucción al LLM de citar solo los fragmentos que responden directamente la pregunta.

**A2:** El agente viola el principio de supervisión humana: las acciones con efectos financieros irreversibles (aprobación de un pago) siempre requieren confirmación humana antes de ejecutarse. La instrucción del sistema debe declarar explícitamente: "Nunca ejecutes `aprobar_pago` sin presentar el cálculo completo al operador y recibir confirmación explícita."

**A3:** El control de acceso diferenciado por rol aplica directamente. La instrucción del sistema debe variar según el rol del usuario: el perfil "enfermero certificado" tiene acceso a información clínica completa; el perfil "estudiante de enfermería" tiene acceso a información clínica de aprendizaje con limitaciones sobre medicamentos controlados. El motor RAG debe filtrar el índice de documentos clínicos por el nivel de autorización del perfil activo.

**A4:** La ventana de 8.000 tokens se llena con 3.000 de instrucción del sistema más el historial acumulado. Después de ~15 turnos, el historial compite con la instrucción del sistema por el espacio disponible. Cuando el historial excede el espacio restante, el LLM recibe un contexto truncado que puede excluir partes de la instrucción del sistema. Estrategia 1: implementar ventana deslizante con resumen incremental para el historial, limitando a 5 turnos completos + resumen comprimido. Estrategia 2: reducir el tamaño de la instrucción del sistema a lo estrictamente necesario y separar el conocimiento estático en RAG.

**A5:** Problema 1: violación de privacidad implícita (el usuario no consintió que ese comentario fuera memorizado como dato persistente). Problema 2: el estado emocional momentáneo de una persona no es información útil para sesiones futuras y puede generar sesgos en las respuestas. El diseño correcto del módulo de memoria aplica el criterio de relevancia futura: solo se memoriza información que cambia el comportamiento del sistema de manera que el usuario considera valiosa. Un comentario emocional casual no cumple ese criterio.

**B1-B3:** Estas preguntas evalúan la capacidad de razonamiento de diseño. No hay respuesta única. Los criterios de calidad son: especificidad (las respuestas se refieren a este caso, no a casos genéricos), consistencia (las decisiones de diseño son coherentes entre sí), y completitud (se cubren los aspectos de seguridad, observabilidad y operación, no solo la funcionalidad).

---

Si completaste las cinco preguntas de la Parte A con respuestas que cubren los puntos de las notas de contraste, y al menos dos de las tres preguntas de la Parte B con razonamiento específico y coherente, completaste el módulo con solidez suficiente para abordar el Módulo 4.

Si identificaste preguntas que no pudiste responder bien, eso no es un fracaso: es precisamente la información que necesitas. Las preguntas que no pudiste responder señalan los capítulos que vale la pena releer antes de continuar.
