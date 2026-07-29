# Informe Pedagógico — Módulo 12: Proyecto Final
**Revisado por:** Director Pedagógico / Claude  
**Fecha:** 2026-07-25  
**Archivos revisados:** muestra representativa de 42 secciones sobre 60 totales (secciones 01, 02, 03, 04, 05 y 06 de todos los capítulos, con cobertura completa de secciones 01, 03 y 06)

---

## 1. Fortalezas

### Secuencia del ciclo de ingeniería

Los 10 capítulos siguen el ciclo de vida completo de un sistema de producción con una lógica que el lector puede internalizar: diseño (Cap. 01) → decisiones documentadas (Cap. 02) → implementación del núcleo RAG (Cap. 03) → implementación agéntica (Cap. 04) → seguridad (Cap. 05) → despliegue y MLOps (Cap. 06) → evaluación (Cap. 07) → observabilidad (Cap. 08) → documentación técnica (Cap. 09) → cierre y evaluación del proyecto (Cap. 10). La secuencia es internamente coherente: cada capítulo asume el anterior como fundamento.

### Especificidad técnica consistente y cuantificada

El módulo evita la vaguedad habitual de los proyectos finales académicos. Los conceptos aparecen con parámetros concretos: chunking a 512 tokens con 64 de overlap, HNSW m=16 ef_construction=100, faithfulness >= 0.85, latencia P95 < 3 segundos, costo máximo 0.02 USD/petición, red teaming de 50 ataques con tasa de bypass objetivo < 5%. Esta especificidad es pedagógicamente valiosa porque el lector puede verificar cada criterio con un script de evaluación, no con juicio subjetivo.

### El capítulo de ADRs como eje de razonamiento arquitectónico

La decisión de dedicar el Capítulo 02 íntegramente a los ADRs es uno de los aciertos más importantes del módulo. No solo enseña el formato (Título, Estado, Contexto, Decisión, Consecuencias) sino que demuestra en cuatro ADRs concretos (modelo fundacional, estrategia RAG, diseño agéntico, seguridad) cómo se razona una decisión técnica con evidencia cuantitativa. El ADR-002 sobre chunking incluye comparaciones de 256/512/1024 tokens con RAGAS, el ADR-001 compara GPT-4o vs Claude 3.5 Sonnet vs Gemini 1.5 Pro con benchmark de dominio. Este nivel de concreción enseña el método, no solo el artefacto.

### Integración explícita con módulos anteriores

El cierre del Capítulo 01 (Sección 06) y el cierre del Capítulo 10 (Sección 05) mapean explícitamente cada componente del proyecto a los módulos que lo desarrollaron: RAG en Módulos 6-7, agentes en Módulo 8, seguridad en Módulo 10, MLOps en Módulo 9, observabilidad en Módulo 11. El lector que avanza secuencialmente por el libro puede reconocer qué capítulo anterior se aplica en cada componente del proyecto.

### Secciones de cierre como síntesis pedagógica

Cada capítulo termina con una sección 06 que no repite el contenido sino que articula el significado del capítulo en el contexto del módulo completo. El cierre del Capítulo 04 ("Un agente sin observabilidad y sin criterios de aceptación cuantitativos no es un sistema — es un experimento en producción") condensa el principio rector del capítulo en una frase que puede orientar decisiones de diseño futuras. Las frases "Para recordar" al final de cada sección cumplen la misma función a escala de sección.

### Evaluación como práctica continua, no como hito final

El Capítulo 07 integra la evaluación como un ciclo continuo (offline con golden dataset + online con muestreo del 5% del tráfico real) que comienza en el desarrollo y no termina con el despliegue. El pipeline CI/CD del Capítulo 06 ya incluye un gate de evaluación RAGAS antes del deploy. Esta coherencia entre capítulos refuerza el principio de que la evaluación es una práctica de ingeniería, no una verificación puntual.

### El cierre del módulo (Capítulo 10, Sección 05)

La sección "El AI Engineer que fuiste y el AI Engineer que eres" es el punto culminante pedagógico de todo el libro. Traza explícitamente la distancia recorrida desde "hacer funcionar un LLM en un notebook" hasta "operar un sistema evaluable en producción" con métricas trazables. Esta articulación del crecimiento técnico del lector es infrecuente en libros de ingeniería y tiene un valor pedagógico elevado.

---

## 2. Debilidades

### Ausencia de puente explícito desde el Módulo 11

El Módulo 11 cierra con un roadmap de adopción de IA enterprise, niveles de madurez organizacional, checklists de escala y gestión de deuda técnica. El Módulo 12 arranca directamente con la definición del caso de uso sin ningún conector que explique la transición. Un lector que terminó el Módulo 11 leyendo sobre Change Advisory Boards, integración con SAP y cumplimiento GDPR/SOC 2 encuentra en el Capítulo 01 de Módulo 12 un sistema técnico concreto sin mediación entre los dos registros. Falta una sección introductoria que enmarque el proyecto final como la síntesis del libro completo, no solo del módulo anterior.

### Triplicación no diferenciada de la evaluación RAGAS

El concepto de evaluación RAGAS aparece con plena especificidad técnica en tres capítulos distintos sin que cada aparición indique claramente su rol diferencial:
- Capítulo 03, Sección 05: evaluación del pipeline RAG implementado con golden dataset de 200 pares y umbrales (faithfulness >= 0.85, answer relevance >= 0.80, context precision >= 0.75, context recall >= 0.70).
- Capítulo 06, Sección 02: gate de evaluación en CI/CD con 20 muestras del golden dataset y umbrales distintos (faithfulness < 0.80, answer_relevance < 0.75).
- Capítulo 07, Secciones 01 al 06: framework tri-capa de evaluación con sampling del 5% del tráfico real.

Los umbrales difieren entre capítulos (0.85 en Cap. 03 vs 0.80 en Cap. 06 para faithfulness) sin explicación. El lector no tiene herramientas para resolver esta inconsistencia: ¿son umbrales distintos para momentos distintos del ciclo? ¿el gate del CI/CD es más permisivo intencionalmente? Esta ambigüedad puede generar confusión en la implementación.

### Reaparición tardía de la memoria persistente del agente

El Capítulo 04 diseña el agente en detalle (nodos LangGraph, herramientas, ciclo ReAct, testing), pero la persistencia del estado del agente aparece por primera vez en el Capítulo 06, Sección 03 como un componente de infraestructura: "RDS PostgreSQL para el almacenamiento del estado del agente (LangGraph persistence)". La memoria y el estado persistente entre sesiones es una decisión arquitectónica de primer orden que debería estar en el diseño del agente (Capítulo 04), no descubrirse como un servicio de infraestructura en el capítulo de Terraform. El lector que implementa el agente en el Capítulo 04 no sabe si el agente mantiene estado entre sesiones o no.

### Seguridad presentada como bloque aislado

La seguridad se concentra en el Capítulo 05, pero la superficie de ataque del sistema se construye en los capítulos anteriores: el pipeline de ingesta del Capítulo 03 acepta documentos potencialmente maliciosos; el agente del Capítulo 04 ejecuta herramientas con parámetros generados por el LLM. La ausencia de referencias de seguridad dentro de los capítulos de implementación crea la impresión de que la seguridad se "agrega" al sistema existente, contradiciendo el principio que el propio módulo enuncia ("La seguridad de un sistema de IA en producción no se agrega al final"). El Capítulo 03 no menciona que los documentos ingestados pueden contener instrucciones maliciosas; el Capítulo 04 no menciona el riesgo de tool chaining no autorizado; ambos conceptos solo aparecen en el Capítulo 05.

### Posición del capítulo de documentación técnica

El Capítulo 09 (Documentación técnica: README, OpenAPI, runbook, guía de contribución) aparece después de la evaluación (Cap. 07) y la observabilidad (Cap. 08). El resultado es que el lector construye el sistema de monitoreo y alertas antes de tener el README que explica cómo ejecutar el sistema localmente. Pedagógicamente, la documentación técnica operativa (runbook en particular) está más estrechamente relacionada con la observabilidad y las alertas del Capítulo 08 que con el cierre del módulo. La posición actual del Capítulo 09 interrumpe el arco entre evaluación (07), observabilidad (08) y cierre (10).

### Ausencia de scaffolding del repositorio

Ninguna sección describe la estructura de directorios del repositorio del proyecto. El lector sabe qué componentes implementar pero no cómo organizar el código: dónde van los ADRs (`docs/adr/`), cómo se estructura el proyecto Python, cómo se separan los tests unitarios de los de integración. Esta información práctica es especialmente importante en un proyecto integrador donde el lector está construyendo un sistema desde cero.

### La rúbrica de evaluación (Capítulo 10, Sección 01) llega demasiado tarde

La rúbrica de evaluación del proyecto aparece en el Capítulo 10, una vez que todos los componentes están implementados. Para que una rúbrica funcione pedagógicamente, debe estar disponible antes de la implementación, no después. El lector que construyó el pipeline RAG en el Capítulo 03 sin conocer que el criterio de aceptación es "búsqueda híbrida implementada" y "RAGAS faithfulness >= 0.82" pierde la orientación que la rúbrica podría haber proporcionado. La rúbrica debería introducirse en el Capítulo 01 o 02 como parte del diseño, no en el capítulo de cierre.

---

## 3. Conceptos a ampliar

### El puente entre Módulo 11 y Módulo 12

El Capítulo 01, Sección 01 necesita un párrafo introductorio que enmarque el proyecto final dentro del contexto enterprise del Módulo 11. ¿En qué tipo de organización se despliega este asistente técnico? ¿Cuáles de los desafíos enterprise (heterogeneidad de fuentes, cumplimiento regulatorio, sistemas legacy) están presentes o explícitamente excluidos del alcance? Sin este encuadre, el proyecto final parece desconectado del contexto organizacional que el Módulo 11 construyó.

### Estado persistente y memoria del agente

El Capítulo 04 debería incluir una sección sobre la persistencia del estado del agente: ¿el agente recuerda conversaciones anteriores del mismo usuario? ¿Cómo se almacena el checkpointing de LangGraph? ¿Cuál es la política de retención del historial de conversación? La presencia de "session_id" en el schema de la API (`QueryRequest` en Cap. 09, Sec. 02) implica que hay estado por sesión, pero este concepto nunca se desarrolla en el capítulo de diseño del agente.

### Construcción del golden dataset como práctica de ingeniería

El Capítulo 07, Sección 02 describe el proceso de construcción del golden dataset de forma concisa pero útil. Sin embargo, la construcción de un golden dataset de calidad es una de las tareas más subestimadas y con mayor impacto en la confiabilidad del sistema de evaluación. Merece más desarrollo: ¿cómo se detectan y resuelven las discrepancias entre anotadores? ¿Qué pasa cuando el dominio de conocimiento evoluciona y el golden dataset queda desactualizado? ¿Cuándo conviene expandir el golden dataset vs re-anotar el existente? El inter-annotator agreement no se menciona.

### Ingeniería de costos como disciplina operativa

El sistema tiene un constraint de 0.02 USD/petición y los ADRs incluyen análisis de costo por token, pero no hay una sección dedicada a cost engineering en producción. El Capítulo 06 o el Capítulo 08 deberían incluir: cómo se mide el costo real por petición (tokens de prompt + completion + embedding + reranking + Qdrant), cómo se atribuye el costo por usuario o equipo en un sistema multi-usuario, y cómo se configura una alerta de presupuesto que prevenga sorpresas en la factura de la API. La alerta de "costo por hora > 1.5x del promedio" en el Capítulo 08 apunta en la dirección correcta pero es insuficiente como tratamiento del tema.

### El prompt del sistema del agente como artefacto de ingeniería

El Capítulo 04 menciona "system prompt del agente con instrucciones de grounding, formato de citación obligatoria y criterios de parada explícitos" sin desarrollar el diseño del prompt. Dado que el Módulo 3 del libro cubre ingeniería de prompts sistemática, el Módulo 12 debería mostrar cómo se aplica esa metodología al caso específico del prompt de un agente ReAct: cómo se especifican las herramientas disponibles, cómo se instruye la citación, cómo se diseñan los criterios de parada en lenguaje natural para el LLM. Este es un punto de conexión directa entre el Módulo 3 y el Módulo 12 que actualmente no se desarrolla.

### Estrategia de migración de embeddings

El ADR-002 selecciona text-embedding-3-small sobre text-embedding-3-large. El Capítulo 10, Sección 04 menciona el fine-tuning del modelo de embedding como extensión posible. Ningún capítulo aborda qué sucede cuando se necesita cambiar el modelo de embedding en producción: la re-indexación completa de la colección, el rollback si el nuevo embedding empeora las métricas, el período de transición con dos colecciones paralelas. La estrategia blue-green para cambios en Qdrant se menciona en el Capítulo 06, Sección 04, pero solo como una línea. Dado que esta es una de las operaciones de mayor riesgo en sistemas RAG productivos, merece una sección de procedimiento.

---

## 4. Conceptos a resumir o eliminar

### Repetición de la descripción de RAGAS

Las cuatro métricas RAGAS (faithfulness, answer relevance, context precision, context recall) se describen con definición completa en el Capítulo 03 (Sección 05) y se definen nuevamente en el Capítulo 07 (Sección 03). La segunda definición es casi idéntica a la primera. La solución no es eliminar una sino diferenciarlas por perspectiva: la primera como guía de implementación del evaluador, la segunda como framework de interpretación operativa. En el estado actual ambas funcionan como exposiciones independientes del mismo concepto.

### Redundancia en los cierres de capítulo

Varios cierres de capítulo (Sección 06) reproducen el listado de la Sección 01 casi sin variación. Por ejemplo, el cierre del Capítulo 03 lista los mismos componentes del pipeline que la Sección 01 de apertura. Las secciones de cierre son más efectivas cuando articulan la relevancia del capítulo en el conjunto del módulo o anticipan el capítulo siguiente, no cuando resumen lo que el lector acaba de leer.

### El threat model STRIDE en dos capítulos

El ADR-004 del Capítulo 02 documenta el threat model STRIDE con sus controles. El Capítulo 05, Sección 01 redescribe el mismo threat model STRIDE con las mismas categorías. La diferencia es de escala, no de perspectiva: el ADR-004 es el documento de toma de decisión, el Capítulo 05 es la implementación de esos controles. Esta distinción debería ser explícita al inicio del Capítulo 05: "Este capítulo implementa los controles definidos en el ADR-004; no repite el análisis de amenazas sino que detalla cómo cada control se traduce en código."

---

## 5. Recomendaciones editoriales

**1. Introducir la rúbrica de evaluación en el Capítulo 01.**  
La rúbrica del Capítulo 10, Sección 01 debe aparecer —al menos en versión resumida— en el Capítulo 01, Sección 01 o en el Capítulo 02. El lector necesita conocer los criterios de éxito antes de diseñar el sistema, no después de implementarlo. La rúbrica completa puede permanecer en el Capítulo 10 como instrumento de evaluación final, pero una versión de los criterios clave (faithfulness >= 0.82, task completion >= 75%, bypass < 5%) debe anclar el diseño desde el Capítulo 01.

**2. Añadir un párrafo de puente al inicio del Capítulo 01, Sección 01.**  
Antes de la descripción del sistema, incluir un párrafo que enmarque el proyecto final en relación con el Módulo 11: qué aspectos del contexto enterprise están presentes en este proyecto (el asistente técnico como caso de uso enterprise real), cuáles están simplificados o excluidos del alcance por razones pedagógicas, y cómo el proyecto integra los once módulos anteriores. Este párrafo convierte el inicio del módulo en una transición, no en un corte.

**3. Unificar y diferenciar los umbrales de RAGAS entre capítulos.**  
Resolver la inconsistencia entre faithfulness >= 0.85 (Cap. 03) y faithfulness >= 0.80 como gate del CI/CD (Cap. 06). Si los umbrales son intencionalmente distintos (umbral de producción más exigente que el gate del CI/CD continuo), explicarlo explícitamente. Si es un error de consistencia, unificar los valores. El mismo alineamiento aplica para answer relevance (0.80 en Cap. 03 vs 0.75 en el gate del CI/CD del Cap. 06).

**4. Ampliar el diseño del agente (Capítulo 04) con la gestión de estado.**  
Agregar en el Capítulo 04 una sección (o expandir la Sección 01) que cubra: si el agente mantiene estado entre sesiones, cómo se implementa el checkpointing de LangGraph, qué información persiste (historial de conversación, herramientas usadas, documentos recuperados) y cuál es la política de retención. Esto cierra la brecha con el `session_id` del schema de API y la referencia a RDS PostgreSQL del Capítulo 06.

**5. Enhebrar señales de seguridad dentro de los capítulos de implementación.**  
En el Capítulo 03, Sección 01 (pipeline de ingesta) añadir una nota que advierta sobre el riesgo de prompt injection indirecta en los documentos y señale el Capítulo 05 para el tratamiento completo. En el Capítulo 04, Sección 02 (implementación de herramientas) añadir una nota sobre el riesgo de tool chaining no autorizado y el control de max_iterations como primera línea de defensa. Este enhebrado convierte la seguridad de un bloque aislado a un hilo que recorre el módulo.

**6. Reubicar el Capítulo 09 (Documentación técnica) o integrarlo con el Capítulo 08.**  
Considerar tres opciones: (a) mover el Capítulo 09 al final del Capítulo 06 como parte del MLOps (el runbook es la documentación operativa del despliegue), (b) dividirlo en dos: la documentación de API y el README como parte del despliegue (Cap. 06), y el runbook como parte de la observabilidad (Cap. 08), o (c) mantener su posición actual pero añadir al inicio una nota que lo enmarque como el artefacto que convierte la observabilidad en operación mantenida por el equipo. La opción (c) es la menos disruptiva.

**7. Agregar una sección de estructura del repositorio en el Capítulo 01 o Capítulo 02.**  
Incluir el árbol de directorios del proyecto (estructura de carpetas para la API, los tests, los ADRs, los scripts de evaluación, la infraestructura Terraform, el pipeline CI/CD) como artefacto de diseño previo a la implementación. Este árbol actúa como mapa del sistema para el lector que construye el proyecto de forma progresiva capítulo por capítulo.

**8. Añadir una sección de ingeniería de costos en el Capítulo 06 o Capítulo 08.**  
Desarrollar el monitoring de costos como práctica operativa: cómo se desagrega el costo real por petición (embedding + LLM + reranking + infraestructura), cómo se configura una alerta de presupuesto en AWS Budgets o en Grafana, y cómo se atribuye el costo por usuario o equipo en sistemas multi-tenant. El constraint de 0.02 USD/petición del Capítulo 01 merece un cierre operativo en el módulo de MLOps u observabilidad.

**9. Reescribir los cierres de capítulo (Sección 06) que duplican la apertura.**  
Para cada Sección 06 que lista los mismos componentes que la Sección 01 del mismo capítulo, reorientar el cierre hacia: (a) la relación de este capítulo con el siguiente, (b) los trade-offs que el lector ha resuelto en este capítulo y que tendrán consecuencias en los capítulos posteriores, o (c) las señales de alerta que indican cuándo una decisión tomada en este capítulo debe revisarse. Esta reorientación convierte los cierres de capítulo en puentes, no en resúmenes.

**10. Posicionar "El AI Engineer que fuiste y el AI Engineer que eres" como la sección de cierre absoluta del módulo.**  
La Sección 10-05 es la más resonante pedagógicamente. Actualmente está entre las extensiones posibles (10-04) y el cierre formal (10-06). Considerar reordenar: Rúbrica (10-01) → Checklist de producción (10-02) → Lecciones aprendidas (10-03) → Extensiones (10-04) → Cierre formal del sistema (10-06 actual) → Síntesis del recorrido del ingeniero (10-05, ahora como cierre). El último párrafo que lee el lector del libro debería ser la síntesis de su crecimiento, no un listado técnico de verificaciones de producción.

---

## Evaluación de las seis preguntas del encargo

**1. ¿La secuencia de los 10 capítulos tiene progresión pedagógica correcta?**  
En términos generales, sí. La progresión diseño → implementación → seguridad → despliegue → evaluación → observabilidad → documentación → cierre sigue una lógica de ingeniería de sistemas reconocible. Los dos desplazamientos que afectan la progresión son: la rúbrica de evaluación al final (debería estar al inicio) y la documentación técnica (Capítulo 09) interpuesta entre la observabilidad y el cierre.

**2. ¿Los capítulos están bien conectados entre sí dentro del módulo?**  
La conexión técnica es fuerte (los capítulos referencian los artefactos de los anteriores: el golden dataset aparece en Cap. 03 y Cap. 07, el pipeline RAG del Cap. 03 se encapsula como herramienta en Cap. 04, el CI/CD del Cap. 06 usa la evaluación del Cap. 07). La conexión pedagógica explícita entre capítulos (frases de anticipación al capítulo siguiente) está prácticamente ausente. Los cierres de capítulo miran hacia atrás, no hacia adelante.

**3. ¿El módulo aterriza bien desde el módulo anterior y prepara bien al lector para el siguiente?**  
El aterrizaje desde el Módulo 11 es abrupto: no hay mediación entre el contexto enterprise del Módulo 11 y el proyecto técnico del Módulo 12. La preparación para el "siguiente" no aplica en sentido estricto porque el Módulo 12 es el último del libro, pero el Capítulo 10, Sección 05 cumple la función de preparar al lector para seguir aprendiendo en producción, que es el único "siguiente" posible. Esa sección lo hace con efectividad.

**4. ¿Qué capítulos o secciones necesitan más desarrollo técnico?**  
Capítulo 04 (estado persistente del agente, prompt de sistema como artefacto de ingeniería), Capítulo 06 (ingeniería de costos como práctica operativa, procedimiento de migración de embeddings), Capítulo 07 (construcción del golden dataset: inter-annotator agreement, mantenimiento del dataset en el tiempo). El Capítulo 05 tiene cobertura técnica sólida; el riesgo es que la lista negra de 200 patrones y los delimitadores XML puedan dar una falsa sensación de completitud frente a la superficie de ataque real de los ataques adversariales sofisticados — el clasificador de intent como tercera capa de defensa merece más prominencia.

**5. ¿Hay lagunas conceptuales importantes en el temario?**  
Tres lagunas relevantes para el perfil del lector objetivo (AI Engineer / Arquitecto de IA):  
(a) Estructura del repositorio y organización del código: cómo scaffoldear el proyecto antes de implementar.  
(b) Gestión del ciclo de vida del golden dataset: cuándo y cómo actualizarlo, qué hacer cuando el dominio evoluciona.  
(c) Operaciones de alto riesgo en producción: migración de modelo de embedding, re-indexación de la colección Qdrant, rollback de changes en el pipeline RAG. Estas operaciones son mencionadas pero no procedimentalizadas.

**6. ¿Qué temas están bien cubiertos y cuáles son superficiales?**  
Bien cubiertos: ADRs con metodología y ejemplos concretos, pipeline RAG con parámetros verificables, agent ReAct con contratos tipados y testing sistemático, threat model STRIDE con controles específicos de sistemas agénticos, CI/CD con gate de evaluación como diferenciador MLOps, observabilidad con stack completo (OTel + Tempo + Prometheus + Loki) y alertas con runbooks.  
Superficiales: persistencia del estado del agente, ingeniería de costos operativa, migración de componentes del pipeline en producción, estructura del repositorio, prompt engineering del sistema del agente como aplicación del Módulo 3.
