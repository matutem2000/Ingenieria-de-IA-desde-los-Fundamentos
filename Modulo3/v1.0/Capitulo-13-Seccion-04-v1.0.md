# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 04: Trazabilidad de prompts y contexto

Cuando un sistema de IA produce una respuesta incorrecta, la pregunta de diagnóstico inmediata es: ¿qué tenía el modelo disponible en ese momento? La respuesta a esa pregunta no es la consulta del usuario. Es el contexto completo que se ensambló y se envió al modelo: el system prompt en su versión específica de producción, los documentos recuperados por el sistema RAG con sus metadatos, el historial de conversación que se incluyó, los resultados de las herramientas que el agente ejecutó, y la consulta reformateada del usuario.

La trazabilidad de contexto es la capacidad de reconstruir ese contexto completo para cualquier solicitud de producción, en cualquier momento posterior. Es la segunda dimensión de observabilidad definida en la sección 01, y es la más diferenciadora: sin ella, el diagnóstico de respuestas incorrectas depende de conjeturas; con ella, el diagnóstico es reproducible y preciso.

### Por qué la trazabilidad de contexto es distinta al logging tradicional

En el software tradicional, el logging registra eventos: una función fue llamada con estos parámetros, una base de datos ejecutó esta consulta, un servicio respondió con este código HTTP. Los logs son registros de lo que hizo el sistema.

En sistemas de IA, lo que hizo el sistema —enviaron una consulta al modelo y recibieron una respuesta— no es suficiente para el diagnóstico. Lo que importa es con qué información exacta lo hizo. El mismo código de sistema puede producir respuestas completamente diferentes si la base vectorial tiene documentos actualizados o desactualizados, si el system prompt fue modificado la semana pasada, si la consulta del usuario activó un patrón de recuperación diferente.

La trazabilidad de contexto registra no la acción sino el estado del mundo en el momento de la acción: el contexto completo que el modelo recibió.

### Los componentes de una traza de contexto

Una traza completa de contexto tiene siete componentes que deben registrarse para que el diagnóstico sea posible.

**Identificador de traza.** Un ID único que vincula todos los registros de una solicitud específica a través del sistema. En pipelines multi-etapa —consulta del usuario → reformulación → recuperación RAG → generación → validación— el identificador de traza permite reconstruir el flujo completo aunque cada etapa esté en un servicio diferente.

**Versión del system prompt.** No el contenido del system prompt, sino el identificador de su versión en el sistema de control de versiones. Con la versión registrada, el equipo puede recuperar exactamente cuáles instrucciones estaban activas en el momento de la solicitud, incluso semanas después. Esto es crítico para diagnósticos retroactivos: si el sistema comenzó a fallar el martes pasado, la pregunta "¿cambió el system prompt ese día?" tiene respuesta objetiva.

**Consulta del usuario.** La consulta original, posiblemente reformulada o expandida por el sistema antes de usarla en la recuperación. Registrar ambas —la consulta original y la consulta procesada— permite detectar casos donde la reformulación introduce sesgos en la recuperación.

**Documentos recuperados.** Para sistemas RAG, la lista de documentos que el sistema recuperó, incluyendo: identificador del documento, nombre o URL de la fuente, fragmento exacto recuperado, score de relevancia asignado por el sistema de recuperación, y metadatos clave (fecha de creación, fecha de última modificación). Esta información permite responder: ¿era correcto el documento que el modelo usó? ¿el score de relevancia fue apropiado? ¿el fragmento recuperado contenía la información necesaria?

**Historial de conversación incluido.** Cuántos turnos de conversación anterior se incluyeron en el contexto, y cuáles. En conversaciones largas donde el historial se trunca por limitaciones de la ventana de contexto, registrar qué partes se incluyeron y cuáles se omitieron permite diagnosticar casos donde la respuesta incorrecta se debe a que el modelo no tenía acceso a información relevante de turnos anteriores.

**Herramientas ejecutadas.** Para sistemas agentivos, la secuencia de herramientas que el agente ejecutó: nombre de la herramienta, parámetros de entrada, resultado de la ejecución, y tiempo de ejecución. Si el agente ejecutó una búsqueda en internet, una consulta a una base de datos o una llamada a una API externa, el resultado de esas operaciones forma parte del contexto que el modelo procesó.

**Respuesta generada y metadatos de generación.** El texto completo de la respuesta del modelo, el número de tokens generados, el tiempo de generación, y el modelo específico que se usó (incluyendo la versión del modelo cuando el proveedor la expone).

### Implementación: distributed tracing para sistemas de IA

El concepto técnico más útil para implementar trazabilidad de contexto es el distributed tracing, que proviene de la ingeniería de sistemas distribuidos. En OpenTelemetry —el estándar abierto de observabilidad— una traza es un árbol de spans: cada etapa del procesamiento es un span con su duración, sus atributos y su relación con los spans padre e hijo.

Para un sistema de IA, el árbol de spans tiene una estructura que refleja el pipeline de procesamiento:

```
TRAZA — Solicitud de soporte al cliente (ID: trace-8f2a91)

SPAN RAÍZ: handle_user_request (total: 1,847ms)
│
├── SPAN: preprocess_query (12ms)
│     atributos: {query_original, query_expanded}
│
├── SPAN: retrieve_context (340ms)
│     │
│     ├── SPAN: embed_query (45ms)
│     │     atributos: {tokens, modelo_embedding}
│     │
│     └── SPAN: vector_search (295ms)
│           atributos: {k=5, scores=[0.91, 0.87, 0.82, 0.78, 0.71],
│                       doc_ids=[...], fragmentos=[...]}
│
├── SPAN: assemble_context (8ms)
│     atributos: {tokens_sistema: 1200, tokens_recuperados: 2100,
│                 tokens_historial: 450, tokens_usuario: 85,
│                 tokens_total: 3835, system_prompt_version: "v2.3.1"}
│
├── SPAN: call_model (1,420ms)
│     atributos: {modelo: "gpt-4o-mini", tokens_input: 3835,
│                 tokens_output: 312, ttft_ms: 890}
│
└── SPAN: postprocess_response (67ms)
      atributos: {groundedness_score: 0.89, response_id: "resp-7c4d"}
```

Este árbol de spans permite responder en segundos preguntas que sin trazabilidad requerirían horas de análisis: ¿cuánto tardó la recuperación? ¿qué documentos se usaron? ¿cuántos tokens consumió el historial? ¿qué versión del system prompt estaba activa?

### Qué registrar y qué no registrar

La trazabilidad completa tiene un costo: almacenamiento y procesamiento de datos. En un sistema que maneja millones de solicitudes, registrar el contexto completo de cada una puede ser prohibitivo en costo de almacenamiento. Hay estrategias para gestionarlo.

**Muestreo de trazas.** Registrar la traza completa de una fracción del tráfico —tipicamente el 10-20% para sistemas de volumen moderado, menor para sistemas de muy alto volumen— con muestreo determinístico que asegura que los casos con errores técnicos o scores de calidad bajos siempre se registran. El muestreo inteligente captura los casos normales con menor densidad y los casos anómalos con mayor densidad.

**Retención diferenciada.** Las trazas de solicitudes normales pueden retenerse por 30 días; las trazas de solicitudes con errores, scores de calidad bajos o respuestas que el usuario marcó explícitamente como incorrectas deben retenerse por períodos más largos (90 días o más) para permitir análisis retrospectivos.

**Compresión del contenido.** Almacenar hashes de los documentos recuperados en lugar del contenido completo, con la capacidad de recuperar el contenido desde el sistema fuente cuando sea necesario para diagnóstico. Esto reduce el volumen de almacenamiento sin perder la capacidad de reconstruir el contexto.

**Consideraciones de privacidad.** Los datos del usuario —consultas, fragmentos de conversación— son datos personales en la mayoría de las jurisdicciones. La trazabilidad debe diseñarse desde el inicio con las restricciones de privacidad aplicables: quién puede acceder a las trazas, durante cuánto tiempo se retienen, cómo se anonimiza la información del usuario para análisis agregados.

### El valor diagnóstico de la trazabilidad: un ejemplo

Supóngase que el equipo de soporte reporta que el asistente de IA dio una respuesta incorrecta sobre el proceso de devolución de un producto. Sin trazabilidad, el ingeniero debe adivinar qué ocurrió: ¿el sistema prompt era incorrecto? ¿el RAG recuperó el documento equivocado? ¿el modelo alucinó?

Con la traza de esa solicitud específica, el diagnóstico es directo:

- Se recupera el identificador de la solicitud del log de conversación.
- Se busca la traza correspondiente en el sistema de observabilidad.
- Se verifica la versión del system prompt: v2.3.1, actualizada hace tres semanas. No coincide con el problema reportado.
- Se revisan los documentos recuperados: el sistema recuperó un fragmento de la política de devoluciones con fecha de modificación de hace seis meses, que menciona un plazo de 30 días. La política actual, actualizada hace dos semanas, establece un plazo de 15 días.
- El documento desactualizado no fue reindexado después de la actualización de la política.

El diagnóstico tomó tres minutos. La solución —reindexar el documento actualizado y verificar si hay otros documentos con el mismo problema— tomó una hora. Sin trazabilidad, el mismo diagnóstico habría requerido revisar manualmente múltiples fuentes posibles de error, y podría haber llegado a la conclusión incorrecta de que el problem era el model prompt.

### Nota del arquitecto

La trazabilidad de contexto es el componente de observabilidad más diferenciador y, paradójicamente, el más frecuentemente omitido en los primeros diseños de sistemas de IA. La razón es que su valor no es visible cuando el sistema funciona bien; solo se vuelve evidente cuando hay un problema que diagnosticar. La tentación es omitirla para reducir la complejidad inicial y agregarla después "si es necesario".

El problema es que agregar trazabilidad retroactivamente requiere modificar el sistema, lo que puede ser costoso y disruptivo. Un sistema de IA sin trazabilidad diseñada desde el inicio es un sistema que opera en modo opaco: puede funcionar bien, puede funcionar mal, y en ambos casos el equipo tiene poca capacidad de saberlo con certeza.

Diseñar la trazabilidad desde el primer sprint es inversión, no gasto. El retorno aparece la primera vez que hay que diagnosticar un problema de producción.

La siguiente sección extiende la observabilidad desde las llamadas individuales al modelo hacia los flujos completos de agentes multi-etapa: cómo monitorear ciclos agentivos, detectar bucles y medir la latencia por etapa de un pipeline complejo.
