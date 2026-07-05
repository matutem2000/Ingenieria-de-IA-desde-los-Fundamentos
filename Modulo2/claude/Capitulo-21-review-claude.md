# Informe Editorial — Capítulo 21

**Capítulo:** 21 — Laboratorios de Prompt Engineering  
**Módulo:** 2 — Prompt Engineering Profesional  
**Versión revisada:** 0.1  
**Fecha de revisión:** 2026-07-01  
**Rol:** Director Pedagógico y Revisor Editorial

---

## 1. Fortalezas

### Estructura repetible y reconocible como andamiaje

Cada sección del capítulo sigue la misma estructura interna: epígrafe, objetivos, introducción, problema, diagrama de flujo, casos de prueba, criterios de evaluación, caso de estudio, buenas prácticas, errores frecuentes, ideas clave y transición. Esta regularidad es una fortaleza pedagógica genuina: el lector sabe qué esperar en cada sección, lo que reduce la carga cognitiva y facilita la navegación.

### Progresión temática bien concebida (Secciones 01 a 06)

La secuencia de laboratorios —clasificación, extracción estructurada, generación controlada, ingeniería conversacional, integración— responde a una lógica acumulativa sólida. Cada laboratorio agrega complejidad sobre el anterior, culminando en el laboratorio integrador de la Sección 06. La Sección 01 funciona como marco metodológico previo, y la Sección 07 como cierre reflexivo. El arco general del capítulo está bien diseñado.

### El diagrama de flujo metodológico como herramienta recurrente (Secciones 01 al 07)

Los diagramas Mermaid aparecen en todas las secciones con propósitos distintos: el ciclo iterativo de mejora, la arquitectura técnica de cada laboratorio, el ciclo de madurez de la solución. Son concisos, no sobrecargan el texto y refuerzan la idea central de que el Prompt Engineering es un proceso sistematizado, no una actividad intuitiva.

### Las tablas de casos de prueba como herramienta concreta (Secciones 02, 03, 04, 05, 06)

La presentación de los conjuntos de prueba en tablas bicolumna es un acierto metodológico. Permite al lector visualizar la variedad de escenarios que debe contemplar (directo, ambiguo, múltiple, incompleto, fuera de alcance) y conecta la teoría con la práctica de forma inmediata.

### El caso de estudio como ancla narrativa (Secciones 02 al 07)

Cada sección incluye un "Caso de estudio" breve que narra una situación concreta de mejora. Estos pasajes son pedagógicamente valiosos porque muestran el error, la intervención y el resultado. El caso de la Sección 07 —dos equipos con enfoques distintos— es especialmente eficaz para ilustrar la diferencia entre experimentación y disciplina de ingeniería.

### Los apartados "Errores frecuentes" y "Buenas prácticas" como recurso de refuerzo

Estos dos bloques, presentes en todas las secciones, funcionan como consolidación del aprendizaje. La redacción es directa, sin tecnicismos, y los contrastes implícitos entre ambos bloques refuerzan los conceptos sin necesidad de reiterarlos en el cuerpo principal.

### Tono y estilo consistente

El texto mantiene un registro técnico pero accesible a lo largo de todo el capítulo. No cae en informalidad ni en abstracción excesiva. La voz es clara y las oraciones son mayoritariamente cortas, lo que favorece la lectura en un texto técnico.

---

## 2. Debilidades

### Ausencia total de código o prompts reales (Secciones 02 al 06)

El mayor déficit del capítulo es estructural: se llama "Laboratorios de Prompt Engineering" pero no contiene ningún prompt real. Los casos de estudio describen lo que "el equipo" hace o ajusta, pero nunca muestran el prompt antes y el prompt después. El lector lee sobre un proceso de diseño sin ver el artefacto que se diseña. Esto genera una discontinuidad importante entre el título del capítulo y su contenido efectivo.

### Los casos de estudio son genéricos y no ofrecen aprendizaje transferible (Secciones 02 al 06)

Los casos de estudio describen situaciones verosímiles, pero con un nivel de abstracción tan alto que no permiten al lector aprender de los detalles. En la Sección 02 se dice que "se incorpora una regla para detectar múltiples intenciones", pero no se muestra esa regla. En la Sección 03 se menciona que el modelo "utiliza distintos nombres para un mismo campo", pero no se ve el prompt corregido. El patrón se repite en las Secciones 04, 05 y 06. La narrativa es de proceso, no de contenido.

### La Sección 01 es una introducción metodológica, no un laboratorio (Sección 01)

La Sección 01 describe la metodología, presenta buenas prácticas y errores frecuentes, pero no propone un laboratorio propio. El primer caso de estudio que aparece —clasificación de correos— es exactamente el mismo que desarrolla la Sección 02. Esto crea redundancia conceptual y el riesgo de que el lector sienta que avanzó de capítulo sin recibir contenido nuevo.

### Repetición exacta del epígrafe de cierre en todas las secciones (Secciones 01 al 07)

Las siete secciones terminan con la misma cita: "Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones." La primera vez es impactante. A partir de la segunda, pierde toda fuerza y puede generar una impresión de descuido editorial.

### Los criterios de evaluación son listas sin jerarquía ni orientación operativa (Secciones 02 al 06)

Las listas de criterios de evaluación son válidas como inventario, pero no indican cuáles son prioritarios, cómo se miden concretamente ni qué umbrales señalan un resultado aceptable. Por ejemplo, en la Sección 02 se menciona "consistencia entre ejecuciones" sin aclarar qué porcentaje de consistencia sería esperado o cómo detectarlo.

### La Sección 07 introduce el concepto de "deuda técnica de prompts" sin andamiaje previo (Sección 07)

En la sección de "Errores frecuentes" de la Sección 07 aparece el concepto "deuda técnica generada por los prompts", que no fue introducido en ningún lugar anterior del capítulo ni, aparentemente, del módulo. Es un concepto relevante que merece tratamiento, pero su aparición puntual como un ítem de lista lo hace pasar desapercibido.

### El laboratorio de Ingeniería Conversacional (Sección 05) no desarrolla el diseño del sistema de estado

La Sección 05 menciona un "Gestor del estado" y un "Constructor de contexto" en el diagrama, pero no explica cómo se diseñan ni qué técnicas concretas de Prompt Engineering se aplican para implementarlos. El lector que no revisó capítulos anteriores del módulo no tendría herramientas para abordar el laboratorio.

---

## 3. Conceptos que conviene ampliar

### Prompts reales como ejemplos centrales (Secciones 02, 03, 04, 05)

El capítulo necesita, al menos en las primeras secciones (o en la sección introductoria), uno o dos prompts reales que ilustren antes/después de una iteración. No es necesario hacerlo en todos los laboratorios, pero la ausencia total es un vacío pedagógico para un capítulo de aplicación práctica.

### Cómo medir consistencia entre ejecuciones (Sección 02 y Sección 04)

Los criterios de evaluación mencionan "consistencia" como indicador clave en múltiples secciones, pero no se explica cómo medirla en la práctica. ¿Se comparan salidas con diferente temperatura? ¿Se usan pruebas automatizadas? ¿Se define una rúbrica manual? Esta laguna metodológica debilita el valor práctico del capítulo.

### El concepto de "deuda técnica de prompts" (Sección 07)

Este concepto merece al menos un párrafo de desarrollo en la Sección 07 o, preferiblemente, una mención anticipatoria en la Sección 01. Si se introduce solo como ítem de lista en la sección de cierre, su potencial pedagógico se desperdicia.

### La distinción entre estado, contexto e historial (Sección 05)

La Sección 05 menciona explícitamente en los "Errores frecuentes" que se debe evitar "mezclar estado, memoria y contexto", pero en ningún momento del capítulo se define con precisión la diferencia entre estos tres conceptos. El lector que llega a la Sección 05 esperaría una definición o al menos una referencia a la sección del módulo donde se desarrollaron.

### RAG aparece mencionado sin contexto en la lista de casos de prueba (Sección 06)

En la Sección 06, los casos de prueba incluyen "recuperación mediante RAG" sin que este concepto haya sido explicado en el capítulo. Si fue cubierto en capítulos anteriores, conviene al menos una referencia cruzada. Si no fue cubierto, su aparición aquí es abrupta.

### La tabla de síntesis de la Sección 07 podría expandirse

La tabla "Síntesis de los laboratorios" de la Sección 07 resume cada laboratorio en una sola columna de competencia. Podría enriquecerse con una columna adicional que indique el tipo de arquitectura utilizada o la técnica clave aplicada, para reforzar la integración conceptual antes del Proyecto Integrador.

---

## 4. Conceptos que pueden resumirse

### La Sección 01 puede consolidarse con la introducción del capítulo

La Sección 01 duplica en gran parte la función de una introducción de capítulo. La metodología (tabla de etapas), las buenas prácticas, los errores frecuentes y el caso de estudio inicial ya están cubiertos en el material de apertura. Una solución es fundir la Sección 01 con la presentación del capítulo y comenzar directamente con el Laboratorio 1 (Sección 02) como primera sección numerada.

### Los bloques "Buenas prácticas" y "Errores frecuentes" se vuelven repetitivos entre secciones

Varios ítems de "Buenas prácticas" y "Errores frecuentes" se repiten casi textualmente entre secciones. Por ejemplo:
- "Cambiar una variable por vez" aparece en Sección 01 y Sección 02.
- "Optimizar sin medir" aparece en Sección 01 y Sección 02 (como "Optimizar sin métricas").
- "Evaluar únicamente ejemplos favorables" aparece en Sección 01 y Sección 02.

Una estrategia posible es consolidar las prácticas transversales en la Sección 01 y dejar solo las prácticas específicas de cada laboratorio en las secciones posteriores.

### Las transiciones entre secciones son excesivamente uniformes

Todas las transiciones siguen el mismo patrón: "En la próxima sección desarrollaremos un laboratorio...". Aunque la función de transición es válida, la uniformidad hace que cada cierre suene idéntico al anterior. Podrían reducirse a una frase más breve o diferenciarse por contenido.

### El diagrama de flujo metodológico se repite casi idéntico en Secciones 01 y 02

El diagrama de la Sección 01 (Problema → Diseño → Pruebas → Evaluación → Mejora → Versión final) es prácticamente idéntico al de la Sección 02 (Analizar → Diseñar → Ejecutar → Evaluar → Refinar → Nueva versión). Si ambas secciones coexisten, uno de los dos diagramas es redundante.

---

## 5. Recomendaciones editoriales

### R1. Incluir al menos un prompt real en el capítulo

El capítulo se llama "Laboratorios de Prompt Engineering". La ausencia de prompts concretos es el problema más urgente a resolver. Se sugiere que la Sección 01 o la Sección 02 incluya al menos un prompt de ejemplo en versión inicial y una versión refinada, para anclar el proceso iterativo en un artefacto tangible. No es necesario hacerlo en todas las secciones, pero la ausencia total rompe la promesa pedagógica del título.

### R2. Variar el epígrafe de cierre en cada sección

La cita "Un arquitecto no memoriza respuestas..." es poderosa una vez. Se recomienda reemplazarla en las Secciones 02 a 07 por citas distintas que reflejen el tema específico de cada laboratorio, o eliminar el epígrafe de cierre en las secciones intermedias y reservarlo solo para la Sección 01 y la Sección 07 (apertura y cierre del capítulo).

### R3. Consolidar las buenas prácticas y errores frecuentes transversales en la Sección 01

Identificar cuáles ítems de "Buenas prácticas" y "Errores frecuentes" son comunes a todos los laboratorios y agruparlos únicamente en la Sección 01. En las secciones siguientes, mantener solo los ítems específicos del tipo de laboratorio que corresponde. Esto reduciría la repetición sin perder contenido.

### R4. Dar andamiaje previo a los conceptos de estado, contexto y memoria antes de la Sección 05

Si el Módulo 2 tiene capítulos previos donde se definieron estos conceptos, conviene agregar una referencia cruzada explícita al inicio de la Sección 05 ("Como se desarrolló en el Capítulo X..."). Si no fueron cubiertos, la Sección 05 necesita un párrafo definitorio antes de presentar el problema del laboratorio.

### R5. Añadir referencia cruzada para RAG en la Sección 06

El término "RAG" aparece en la lista de casos de prueba de la Sección 06 sin contexto. Agregar entre paréntesis una referencia al capítulo donde se desarrolló el concepto ("recuperación mediante RAG —ver Capítulo X—") es suficiente para no interrumpir el ritmo del texto.

### R6. Desarrollar mínimamente el concepto de "deuda técnica de prompts" en la Sección 07

Este concepto tiene valor pedagógico real en el cierre del capítulo. Se recomienda elevarlo de un ítem de lista a al menos un párrafo breve que defina qué se entiende por deuda técnica aplicada a prompts y por qué es relevante en contextos de producción.

### R7. Considerar fusionar la Sección 01 con la introducción del capítulo o redefinir su rol

Si la Sección 01 se mantiene como sección independiente, se sugiere diferenciar claramente su función: que no sea solo un marco metodológico sino que también anticipe los cinco laboratorios con una descripción de una línea por laboratorio y la competencia que desarrollará cada uno. Esto serviría como mapa conceptual previo al recorrido.

### R8. Enriquecer la tabla de síntesis de la Sección 07

La tabla de cierre de la Sección 07 es un recurso valioso que podría potenciarse con una tercera columna: por ejemplo, "Técnica clave" o "Patrón de diseño utilizado". Esto reforzaría la conexión entre los laboratorios y los contenidos teóricos del módulo, y prepararía mejor al lector para el Proyecto Integrador.

---

*Informe generado en función del manuscrito v0.1. Las observaciones corresponden exclusivamente al Capítulo 21 y no implican juicio sobre el módulo completo.*
