# Capítulo 09 — Arquitecturas Multiagente

## Sección 10 — Caso de estudio empresarial

La teoría de los sistemas multiagente adquiere claridad cuando se aplica a un caso concreto. Esta sección desarrolla el diseño completo de un sistema multiagente para un problema empresarial real: un sistema de análisis de propuestas de proveedores para el departamento de compras de una empresa de manufactura mediana.

El caso no es trivial ni es artificialmente complejo. Fue elegido porque tiene características que justifican genuinamente una arquitectura multiagente, y porque las decisiones de diseño que requiere son las mismas que aparecen en la mayoría de los sistemas empresariales de esta clase.

### El problema

La empresa recibe entre veinte y cincuenta propuestas de proveedores por mes para distintas categorías de compra: materiales, equipamiento, servicios de logística, tecnología. Cada propuesta incluye documentación técnica, condiciones comerciales, referencias de clientes y, en algunos casos, muestras o demos.

El equipo de compras actualmente revisa estas propuestas manualmente. El proceso toma entre dos y cinco días hábiles por propuesta, dependiendo de la complejidad. El resultado es un informe de evaluación que compara al proveedor contra los criterios de la empresa en cada dimensión relevante y produce una recomendación: aprobar, rechazar o solicitar información adicional.

El equipo de compras quiere un sistema que produzca borradores de evaluación de alta calidad en horas, no en días. Un analista humano revisará cada borrador antes de que sea comunicado externamente, por lo que el sistema no necesita operar sin supervisión humana. Pero la calidad del borrador debe ser suficientemente alta como para que la revisión humana sea un proceso de verificación, no una reescritura.

### Análisis de la arquitectura

**¿Justifica este problema una arquitectura multiagente?** Aplicando las cuatro preguntas de la sección 02:

- ¿Subtareas independientes paralelizables? Sí. El análisis técnico, el análisis comercial, la verificación de referencias y la búsqueda de información pública sobre el proveedor son independientes entre sí. Un agente puede analizar las condiciones comerciales mientras otro verifica las referencias simultáneamente.
- ¿Especialización fundamentalmente distinta por dominio? Sí. El análisis técnico requiere conocimiento del dominio de manufactura y los criterios técnicos de la empresa. El análisis comercial requiere conocimiento de condiciones contractuales estándar y parámetros financieros. Son dominios suficientemente distintos para justificar agentes especializados.
- ¿Criticidad que justifica verificación independiente? Sí. Una evaluación incorrecta puede llevar a la empresa a contratar un proveedor inadecuado, con impacto en costos, calidad de producción o continuidad operacional. La calidad del output justifica supervisión.
- ¿Volumen que excede la ventana de contexto? Depende de la propuesta. Propuestas complejas con documentación extensa pueden exceder la ventana de un agente único. La arquitectura multiagente resuelve también este problema.

La respuesta es sí en todas las dimensiones relevantes. La arquitectura multiagente está justificada.

### Diseño del sistema

**Agentes del sistema:**

El sistema tiene cinco agentes con roles claramente delimitados:

*Agente orquestador:* recibe la propuesta, extrae los metadatos básicos (proveedor, categoría de compra, fecha), lanza el plan de análisis en paralelo y coordina la síntesis final. No produce análisis propio.

*Agente de análisis técnico:* recibe la documentación técnica de la propuesta y los criterios técnicos de la empresa para esa categoría de compra. Evalúa si las especificaciones del proveedor cumplen los requisitos técnicos mínimos y los diferenciadores positivos. Produce un informe estructurado con evaluación por dimensión técnica.

*Agente de análisis comercial:* recibe las condiciones comerciales de la propuesta: precios, plazos de pago, penalidades, cláusulas de ajuste, garantías. Las evalúa contra los parámetros comerciales estándar de la empresa. Produce un informe con el análisis de riesgo comercial y las condiciones que requieren negociación.

*Agente de investigación de proveedor:* realiza búsquedas sobre la reputación pública del proveedor: cobertura mediática, litigios conocidos, certificaciones verificadas, presencia en mercados relevantes. Produce un resumen de hallazgos con fuentes.

*Agente redactor:* recibe los tres informes de los agentes especializados y el resumen de investigación. Redacta el borrador de evaluación en el formato estándar de la empresa, integrando los hallazgos de cada dimensión con coherencia y sin contradicciones. Produce el documento final para revisión humana.

**Topología:** jerárquica. El orquestador coordina el proceso. Los tres agentes especializados trabajan en paralelo. El redactor espera a tener todos los informes antes de comenzar.

**Mecanismo de comunicación:** mensajes estructurados en JSON. El orquestador envía a cada agente especializado un mensaje con el tipo de análisis requerido y los documentos relevantes como payload. Los agentes especializados responden con informes estructurados en JSON. El redactor recibe los tres informes y produce el texto final.

**Estado compartido:** el sistema mantiene un estado de progreso por propuesta que incluye: estado de cada análisis (pendiente, en curso, completado, con error), los informes producidos por cada agente y el borrador final cuando esté disponible. El orquestador actualiza este estado a medida que cada agente reporta.

**Supervisión:** el sistema no incluye un agente supervisor automático porque la revisión humana actúa como supervisor final. Lo que el sistema sí incluye es validación de esquema en cada informe: si un agente produce un informe que no cumple el esquema esperado, el sistema lo rechaza y reintenta la tarea antes de continuar.

### Decisiones de diseño y alternativas descartadas

**¿Por qué no hay un agente supervisor automático?** Porque el costo adicional y la latencia de un ciclo de supervisión automático no están justificados cuando hay un revisor humano como paso final obligatorio. Si la empresa quisiera que el sistema operara sin revisión humana —lo que en este contexto no es el caso— añadir supervisión automática sería la decisión correcta.

**¿Por qué el redactor es un agente separado y no el orquestador?** Porque la redacción de un documento de evaluación es una tarea especializada: requiere un prompt de sistema orientado a la síntesis, el formato estándar de la empresa y el tono apropiado para comunicación interna de compras. El orquestador tiene un rol de coordinación, no de redacción. Mezclar ambos roles en un único agente degradaría la calidad de ambas funciones.

**¿Por qué el análisis técnico y el análisis comercial son agentes separados?** Porque sus instrucciones de sistema, sus herramientas y sus criterios de evaluación son fundamentalmente distintos. Un analista técnico que evalúa especificaciones de materiales no tiene el mismo marco de referencia que un analista comercial que evalúa condiciones contractuales. Separar los roles permite optimizar cada agente para su función específica.

### Estimación de costo y latencia

Para una propuesta de complejidad media, el sistema estima:

- Análisis paralelo (técnico + comercial + investigación): 45 a 90 segundos en paralelo.
- Redacción del borrador: 20 a 40 segundos.
- Tiempo total por propuesta: 65 a 130 segundos.
- Costo de tokens estimado por propuesta: equivalente a tres o cuatro llamadas a un modelo de alta capacidad (dado el contexto de cada agente).

Este costo es significativamente menor que el costo del tiempo humano de dos a cinco días de análisis. La calidad del borrador producido, según validación con el equipo de compras, reduce el tiempo de revisión humana de dos a cinco días a una o dos horas de verificación y ajustes.

---

*La sección 11 convierte este caso en un ejercicio práctico. El lector tomará un escenario diferente y diseñará el sistema multiagente desde cero, aplicando los criterios, patrones y decisiones de diseño desarrollados a lo largo del capítulo.*
