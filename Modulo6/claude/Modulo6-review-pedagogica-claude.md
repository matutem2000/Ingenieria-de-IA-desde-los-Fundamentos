# Informe Pedagógico — Módulo 6: Ingeniería de Sistemas RAG
**Revisado por:** Director Pedagógico / Claude  
**Fecha:** 2026-07-25  
**Muestra analizada:** Secciones 01, 02, 03, 04, 05 y 06 seleccionadas de los 10 capítulos (36 de 60 archivos leídos)

---

## 1. Fortalezas

### Progresión general de los capítulos

La secuencia de los diez capítulos tiene una lógica pedagógica sólida y reconocible: parte de lo conceptual (qué es RAG y por qué existe, Cap. 01), avanza hacia los componentes técnicos de forma bottom-up (embeddings Cap. 02, bases vectoriales Cap. 03, chunking Cap. 04, recuperación Cap. 05), luego construye las capas de ingeniería de calidad (evaluación Cap. 06, producción Cap. 07), y termina con la sofisticación incremental (extensiones Cap. 08, optimización Cap. 09, patrones avanzados Cap. 10). Este recorrido refleja la secuencia real de decisiones que toma un AI Engineer al construir un sistema RAG y es didácticamente correcto.

### Densidad técnica y especificidad

El nivel técnico es apropiado para el público objetivo (AI Engineers y Arquitectos de IA). Las secciones contienen parámetros concretos (chunk_size de 512 tokens con 10% overlap, M=16-64 y ef_construction=100-400 para HNSW, recall@10 de 95-99% para HNSW, latencia p99 <10ms en Qdrant para corpus de 1M vectores), referencias a papers específicos (Lewis et al. 2020 para RAG, Reimers y Gurevych 2019 para SBERT, Asai et al. 2023 para Self-RAG, Yan et al. 2024 para CRAG, Jiang et al. 2023 para FLARE), herramientas con nombres precisos y precios actuales (Cohere Rerank v3 a $2/millón de unidades, BGE Reranker v2-m3 de 568M parámetros). Esta especificidad distingue el contenido de un tutorial genérico y da al esqueleto suficiente substancia técnica para que el autor escriba el texto completo sin tener que investigar los valores fundamentales.

### Estructura interna de cada sección

La consistencia del formato (párrafo introductorio + bullets técnicos + cierre "Para recordar" o "Principio rector") facilita la lectura secuencial y crea un ritmo pedagógico predecible. Los cierres de capítulo (Sección 06) con una cita atribuida a una figura relevante del campo (Karen Spärck Jones, Ellen Voorhees, Martin Fowler, Niall Murphy/Betsy Beyer, Gerard Salton) añaden peso intelectual sin condescendencia y sitúan los principios del capítulo en la historia de la ingeniería de software, lo cual es adecuado para un público avanzado.

### Énfasis en evaluación empírica y métricas cuantitativas

El módulo establece de forma coherente y repetida que las decisiones de diseño deben basarse en métricas cuantitativas medidas sobre datos reales, no en intuición ni en los valores por defecto de los frameworks. Este principio aparece en el Capítulo 04 (Recall@5 para evaluar chunking), Capítulo 05 (Recall@K para optimizar el retriever), Capítulo 06 (RAGAS como framework de evaluación continua), Capítulo 07 (golden dataset como gate de CI/CD), y Capítulo 09 (diagnóstico basado en categorías de errores). La repetición temática aquí es una fortaleza, no una debilidad: construye el hábito mental correcto en el lector.

### Capítulos especialmente sólidos

- **Capítulo 04 (Chunking)**: Posiblemente el capítulo más completo. Establece el impacto pedagógico antes de las técnicas (Cap. 04-01: diferencias de 15-20 puntos en Recall@5 según estrategia), cubre seis estrategias de chunking con sus trade-offs reales (Cap. 04-02), analiza los parámetros de chunk_size y overlap con rangos justificados (Cap. 04-03), y el enriquecimiento de chunks (Cap. 04-04) incluye la técnica de contextual retrieval de Anthropic 2024 con datos de mejora concretos (+35-49% en Recall@20). Es el modelo de cómo debería escribirse un capítulo de este módulo.

- **Capítulo 05 (Recuperación)**: La comparativa BM25 vs. búsqueda semántica en Cap. 05-01 es un ejemplo didáctico de libro: ejemplos concretos de queries que favorecen cada enfoque, con las limitaciones sistemáticas de cada uno descritas sin sesgos hacia una tecnología. El reranking en Cap. 05-03 tiene profundidad técnica real: arquitectura cross-encoder vs. bi-encoder, latencias por modelo en hardware específico, precio de Cohere Rerank v3 vs. alternativa open source BGE.

- **Capítulo 06 (Evaluación)**: La estructura del capítulo es correcta: primero el problema de evaluar RAG (múltiples componentes con métricas en conflicto, Cap. 06-01), luego las métricas concretas de RAGAS (Cap. 06-02), luego la evaluación separada del retriever como práctica (Cap. 06-03). El cierre del capítulo ("sin evaluación sistemática, la mejora de RAG es aleatoria") es el principio más importante del módulo y está bien posicionado.

- **Capítulo 10 (Patrones avanzados)**: Self-RAG, CRAG, FLARE y Agentic RAG están bien explicados con referencias a los papers originales, y cada sección distingue cuándo el patrón se justifica vs. cuándo es sobreingeniería. La sección 10-06 aplica este criterio al conjunto: "adoptar patrones avanzados únicamente cuando el análisis de métricas y errores identifica el problema que resuelven".

---

## 2. Debilidades

### Debilidad 1: Posición del Capítulo 08 (Extensiones) rompe el flujo pedagógico

La secuencia actual es: Producción (Cap. 07) → Extensiones (Cap. 08) → Optimización (Cap. 09) → Patrones avanzados (Cap. 10). Este orden interrumpe la progresión natural de "construir el sistema base con calidad → operarlo en producción → optimizarlo → sofisticarlo". Las extensiones (RAG multimodal, Text-to-SQL, GraphRAG) son variantes del sistema base, no pasos en la madurez operacional del sistema. El lector que termina de aprender a operar un sistema RAG en producción (Cap. 07) esperaría naturalmente aprender a optimizarlo (Cap. 09) antes de explorar extensiones del dominio (Cap. 08). La ruptura es especialmente notoria entre Cap. 08 (GraphRAG, Text-to-SQL) y Cap. 09 (diagnóstico de faithfulness baja y hallucinations): el nivel de sofisticación conceptual en Cap. 08-03 (comunidades del grafo, Leiden algorithm, query routing global vs. local) es mayor que el diagnóstico básico de fallos del Cap. 09-01.

### Debilidad 2: Articulación con el Módulo 5 ausente

El Capítulo 01 abre explicando qué son los LLMs y sus limitaciones como si el lector no tuviera contexto previo. En el flujo del libro, el lector del Módulo 6 acaba de completar el Módulo 5 (AI Engineering para Desarrollo), donde presumiblemente aprendió APIs de LLMs, prompting, chains en LangChain y aplicaciones básicas. La Cap. 01-01 sobre limitaciones de los LLM sin recuperación externa (knowledge cutoff, hallucination, opacidad de fuentes) es válida como motivación de RAG, pero debería anclar al lector con lo que ya conoce: "Las aplicaciones que construiste en el Módulo 5 usando prompting directo y chains tienen una limitación estructural...". Sin ese puente, el capítulo 01 se lee como el primer capítulo del libro completo, no como el sexto módulo de un itinerario secuencial.

### Debilidad 3: Articulación con el Módulo 7 (Ingeniería de Agentes) implícita pero no explícita

El Capítulo 10, especialmente la sección 10-05 sobre Agentic RAG, introduce ciclos ReAct, LangGraph, AutoGen y multi-agent RAG como extensión natural de RAG. Estos son exactamente los conceptos que el Módulo 7 de Ingeniería de Agentes debería profundizar. Sin embargo, la sección de cierre del Capítulo 10 (Cap. 10-06) no hace este puente explícito: concluye el módulo con el principio de adoptar patrones según métricas de error, sin señalar que el Agentic RAG es la transición hacia una disciplina más amplia. El lector podría terminar el Módulo 6 sin entender que Agentic RAG es una instancia del problema más general que abordará en el Módulo 7.

### Debilidad 4: Ausencia de Query Transformations como sección estructurada

El Capítulo 05 (Recuperación) cubre BM25 vs. semántica (Sec. 01), recuperación híbrida + RRF (Sec. 02) y reranking (Sec. 03), pero no tiene una sección dedicada a las técnicas de transformación de queries antes de la recuperación: HyDE (Hypothetical Document Embeddings), multi-query retrieval, query decomposition, step-back prompting. Estas técnicas actúan en la etapa de pre-retrieval y tienen impacto comparableal reranking en Recall@K. HyDE en particular tiene un impacto documentado de 5-15 puntos en Recall@5 para queries abstractas o ambiguas, y es una de las técnicas más discutidas en la literatura práctica de RAG. El Capítulo 04-04 menciona brevemente "hypothetical questions indexing" como técnica de enriquecimiento del índice, pero HyDE como técnica del lado del query no está cubierto.

### Debilidad 5: Seguridad y control de acceso ausentes del módulo

No hay capítulo ni sección dedicada a los aspectos de seguridad de un sistema RAG empresarial: filtrado por permisos de usuario antes de recuperar (row-level security en la base vectorial), aislamiento entre tenants en arquitecturas multi-tenant, prevención de data leakage entre usuarios del mismo sistema, protección contra prompt injection a través de documentos del corpus. Este gap es significativo para un libro dirigido a AI Engineers y Arquitectos de IA que construirán sistemas en entornos empresariales donde estos requisitos son no negociables. La revisión técnica de Codex ya identificó este punto ("Tratar permisos antes de recuperar, con pruebas explícitas contra filtraciones entre usuarios o clientes"), lo que confirma que es una laguna reconocida en el módulo.

### Debilidad 6: La decisión RAG vs. Fine-tuning vs. Long Context Window no está cubierta

El Capítulo 01-01 menciona que el fine-tuning continuo es costoso y que RAG lo evita, pero no hay sección que analice el árbol de decisión entre estas tres alternativas como decisión arquitectónica. Con la aparición de modelos con ventanas de contexto de 1M-2M tokens y técnicas de prompt caching (Anthropic, Google), la pregunta de cuándo RAG sigue siendo necesario vs. cuándo context caching con documentos completos es más apropiado es una decisión que un AI Engineer de 2025-2026 enfrenta con frecuencia. El módulo trata RAG como el destino final sin abordar cuándo no es la solución correcta.

### Debilidad 7: Gestión del RAG conversacional multi-turno superficial

El Capítulo 10-02 (Adaptive RAG) menciona que las queries conversacionales pueden no requerir retrieval si la información ya está en el historial, pero no hay desarrollo de cómo se gestiona el historial de conversación en un sistema RAG multi-turno: cómo reformular queries dependientes del contexto conversacional para que sean auto-contenidas antes de recuperar ("¿Y en el caso de usuarios con menos de 5 años de antigüedad?" requiere saber de qué política se estaba hablando), qué técnicas de condensación del historial evitan el context drift en conversaciones largas, o cómo el historial conversacional se combina con el contexto recuperado en el prompt del generador. Para aplicaciones empresariales (asistentes, bots de soporte, herramientas de investigación), el RAG conversacional es el caso de uso dominante, no el QA de turno único.

---

## 3. Conceptos a ampliar

### 3.1 Query Transformations como sección del Capítulo 05

El Capítulo 05 necesita una sección (Sec. 04 o Sec. 05, ajustando el índice actual) que cubra las técnicas de transformación de queries antes de la recuperación. Contenido mínimo necesario:

- **HyDE (Hypothetical Document Embeddings)**: usar el LLM para generar un documento hipotético que respondería la query, luego usar el embedding de ese documento como vector de búsqueda en lugar del embedding directo de la query. El documento hipotético está en el espacio semántico del corpus, no en el espacio semántico de las queries, mejorando el recall para queries abstractas.
- **Multi-query retrieval**: generar 3-5 variantes de la query original con un LLM (diferentes formulaciones del mismo intent), ejecutar la búsqueda para cada variante, fusionar los resultados con RRF, y eliminar duplicados. Mejora el recall para queries donde la formulación del usuario no coincide con el vocabulario del corpus.
- **Query decomposition**: descomponer queries complejas en sub-queries atómicas, recuperar para cada sub-query, y sintetizar los resultados. Fundamental para queries multi-hop que requieren información de múltiples partes del corpus.
- **Step-back prompting**: generar una pregunta más abstracta/general que la original para recuperar contexto de fondo antes de responder la pregunta específica. Mejora el razonamiento del generador cuando la respuesta requiere comprender el marco general del tema.

Estas técnicas actúan antes del retriever y son complementarias (no alternativas) al reranking que actúa después. Su ausencia es la laguna técnica más significativa del Capítulo 05.

### 3.2 Seguridad y control de acceso como sección del Capítulo 07

El Capítulo 07 (Producción) necesita una sección dedicada a seguridad en RAG empresarial. Conceptos que deben cubrirse:

- **Row-level filtering en la base vectorial**: cómo implementar filtrado por atributos de permiso (user_id, grupo, departamento, clasificación de confidencialidad) antes o durante la búsqueda ANN para garantizar que un usuario solo accede a los documentos para los que tiene permisos. Diferencia entre filtrado pre-ANN (mejor recall, soportado nativamente en Qdrant) y post-ANN (más fácil de implementar pero con recall degradado).
- **Namespace isolation en multi-tenant**: separación física (colecciones distintas por tenant en Qdrant/Weaviate) vs. separación lógica (namespaces con filtros en Pinecone); trade-offs de costo operacional vs. garantías de aislamiento.
- **Prompt injection desde el corpus**: un atacante que puede subir documentos al corpus puede intentar inyectar instrucciones en el contenido del documento que el LLM ejecutará al recibirlo como contexto. Técnicas de mitigación: sanitización del contenido durante la ingesta, instrucciones de groundedness en el system prompt, validación de la respuesta contra el corpus.
- **Auditoría de acceso**: registro de qué usuario recuperó qué documentos y generó qué respuesta, para trazabilidad en entornos regulados (medicina, legal, finanzas).

### 3.3 Ampliación de la sección de cierre del módulo (Cap. 10-06 o sección adicional)

La sección de cierre del Capítulo 10 debería ampliarse para actuar como puente explícito hacia el Módulo 7. Los conceptos de Agentic RAG (ciclos ReAct, LangGraph, multi-agent systems) no son el punto final del Módulo 6 sino la puerta de entrada a la Ingeniería de Agentes. El cierre del módulo debería hacer esta transición explícita: "Un agente de IA es, en esencia, un sistema que usa RAG y herramientas de forma autónoma para resolver problemas que exceden la capacidad de una única inferencia. En el Módulo 7 aprenderás a diseñar y operar estos sistemas."

### 3.4 Árbol de decisión RAG vs. Fine-tuning vs. Long Context (Cap. 01 o sección nueva)

El Capítulo 01 necesita una sección (posiblemente como Sección 05, antes del cierre) que establezca cuándo RAG es la respuesta correcta y cuándo no. El árbol de decisión debería cubrir:

- **Cuándo RAG es suficiente**: corpus actualizable con frecuencia, corpus de millones de documentos que no caben en ninguna ventana de contexto, necesidad de fuentes citables y auditables, costo prohibitivo de fine-tuning continuo.
- **Cuándo fine-tuning es la respuesta**: el modelo necesita aprender un estilo, formato o dominio de razonamiento nuevo (no solo acceder a nueva información), o cuando las queries requieren un conocimiento implícito del dominio que no puede articularse como documentos.
- **Cuándo long context window elimina la necesidad de RAG**: corpus de tamaño moderado (<200K tokens), latencia de procesamiento offline aceptable, documentos que deben analizarse completos sin perder coherencia al fragmentarlos.
- **Cuándo combinar RAG + fine-tuning**: sistemas que requieren tanto acceso a conocimiento actualizable como un perfil de respuesta especializado del dominio.

### 3.5 Observabilidad específica para pipelines RAG en el Capítulo 07

El Capítulo 07 tiene secciones sobre arquitectura desacoplada (Sec. 01), ingesta (Sec. 02), versionado de índices (Sec. 03), y caching semántico (Sec. 04). Sin embargo, la sección de observabilidad del pipeline RAG (si existe como Sec. 05) debería ampliar específicamente las herramientas de tracing para RAG: LangSmith (tracing nativo para LangChain), Langfuse (open source), Phoenix de Arize AI (especializado en LLM observability con soporte explícito de spans de embedding, retrieval y generación), y la estructura de spans anidados que permiten diagnosticar en qué etapa del pipeline ocurre la degradación. Este tema se menciona brevemente en Cap. 10-05 (Agentic RAG) pero merece más desarrollo en el contexto de producción del Capítulo 07.

---

## 4. Conceptos a resumir o eliminar

### 4.1 Redundancia controlada entre Capítulo 05 y Capítulo 09 en reranking

El reranking está cubierto en detalle en Cap. 05-03 (modelos cross-encoder, Cohere Rerank v3, BGE Reranker, FlashRank con latencias y precios específicos) y vuelve a aparecer en Cap. 09-02 (optimización del retriever), mencionando de nuevo los mismos modelos y rangos de mejora. La cobertura en Cap. 09-02 debería referenciar lo establecido en Cap. 05-03 sin repetir la descripción técnica de los modelos: "El reranking, cubierto en detalle en el Capítulo 05, es la optimización de mayor ROI..." seguido del análisis de cuándo subir a top-50 vs. top-100 chunks para el primer stage y cómo medir el delta de Precision@5. La redundancia actual es tolerable en un esqueleto pero el autor debe evitar duplicar la descripción técnica completa en el texto final.

### 4.2 Los "Principios rectores" de los capítulos de extensión (Cap. 08) podrían condensarse

Las secciones de cierre del Capítulo 08 (especialmente Cap. 08-06) tienen principios rectores de alto nivel sobre adopción incremental de extensiones que repiten el mismo mensaje del principio rector del Capítulo 10-06. El autor debería condensar uno de los dos o diferenciar más claramente el mensaje: Cap. 08 puede enfocarse en el criterio técnico de adopción de extensiones, y Cap. 10 en el criterio basado en análisis de métricas.

---

## 5. Recomendaciones editoriales

**1. Mover el Capítulo 08 (Extensiones) al final del módulo, después del Capítulo 10.**

La secuencia recomendada: 01 → 02 → 03 → 04 → 05 → 06 → 07 → 09 → 10 → 08 (Extensiones como capítulo final). Las razones: (a) los capítulos 07, 09 y 10 forman una unidad pedagógica coherente de "operar → optimizar → sofisticar el sistema base", que se interrumpe innecesariamente con las extensiones del dominio; (b) GraphRAG, RAG multimodal y Text-to-SQL son más fáciles de comprender como extensiones del sistema RAG estándar cuando el lector ya ha aprendido a optimizarlo y aplicar patrones avanzados; (c) el Capítulo 08 como capítulo final del módulo puede concluir con un párrafo de cierre del módulo que conecte hacia el Módulo 7.

**2. Añadir una sección introductoria explícita al Capítulo 01 que conecte con el Módulo 5.**

Proponer como Sección 00 (prefacio del módulo) o como apertura ampliada de la Sección 01. El texto de conexión debe referenciar lo aprendido en el Módulo 5 (APIs de LLMs, prompting, chains) y posicionar RAG como la extensión arquitectónica que transforma esas herramientas en sistemas con acceso a conocimiento verificable y actualizable. Longitud objetivo: 2-3 párrafos de introducción del módulo completo.

**3. Añadir una sección de Query Transformations al Capítulo 05.**

Incorporar como Sección 04 del Capítulo 05 (y renumerar las secciones actuales 04 y 05 como 05 y 06). Cubrir HyDE, multi-query retrieval, query decomposition y step-back prompting con el mismo nivel de detalle técnico que tienen las demás secciones del capítulo: nombres de implementaciones específicas en LangChain/LlamaIndex, latencias, impacto en Recall@K medido, y cuándo justificar el overhead. Esta es la laguna técnica más importante del módulo dado el impacto de estas técnicas en la práctica.

**4. Añadir una sección de Seguridad y Control de Acceso al Capítulo 07.**

Incorporar como Sección 05 del Capítulo 07 (antes del cierre actual en Sección 06). Cubrir: filtrado por permisos pre-ANN en bases vectoriales, namespace isolation multi-tenant con análisis de garantías de aislamiento (física vs. lógica), mitigación de prompt injection desde el corpus, y auditoría de acceso para entornos regulados. Esta sección es prerequisito para que el módulo sea aplicable en contextos empresariales reales.

**5. Añadir una sección "RAG vs. Fine-tuning vs. Long Context Window" al Capítulo 01.**

Incorporar como Sección 05 del Capítulo 01 (antes del cierre actual). Establecer el árbol de decisión arquitectónica con criterios cuantitativos cuando sea posible (tamaño del corpus, frecuencia de actualización, necesidad de citabilidad, costo de re-entrenamiento por cambio de corpus). Incluir en la discusión el prompt caching (Anthropic, Google) como alternativa moderna a RAG para corpus de tamaño moderado. El lector debe terminar este capítulo sabiendo cuándo RAG es la respuesta y cuándo no.

**6. Ampliar el cierre del Capítulo 10 (o agregar sección de cierre del módulo) para crear el puente hacia el Módulo 7.**

La Sección 06 del Capítulo 10 actualmente concluye con un principio de adopción basado en métricas. Ampliar con un párrafo de cierre del módulo completo que establezca la conexión: Agentic RAG es la intersección entre los sistemas RAG que este módulo enseñó y la Ingeniería de Agentes que el Módulo 7 desarrollará. Señalar explícitamente qué conceptos del Módulo 6 son prerrequisito para el Módulo 7: retrieval como herramienta del agente, evaluación de ciclos multi-step, observabilidad de trazas anidadas.

**7. Revisar el Capítulo 09 para incorporar el RAG conversacional multi-turno.**

En la Sección 09-04 (compresión de contexto) o como sección adicional, añadir el caso del RAG conversacional: cómo reformular queries dependientes del contexto de la conversación para hacerlas auto-contenidas antes de recuperar (técnica de query rewriting con historial), qué porción del historial incluir en el prompt de reformulación, y cómo condensar el historial de conversaciones largas para evitar degradación del retrieval. Para la mayoría de las aplicaciones empresariales, el caso multi-turno es el caso de uso dominante.

**8. Incorporar tablas comparativas entre opciones en los capítulos 02, 03 y 05 cuando el autor escriba el texto completo.**

Los capítulos 02 (embeddings), 03 (bases vectoriales) y 05 (recuperación) tienen comparativas entre múltiples opciones (text-embedding-3 vs. voyage-3 vs. BGE-M3; Qdrant vs. Pinecone vs. pgvector vs. Weaviate; RRF vs. weighted score fusion). Estas comparativas son ideales para tablas de doble entrada con criterios de decisión cuantificados (dimensión, precio por millón de tokens, latencia p99 para escala X, tipo de filtrado soportado). Las tablas serían la adición de mayor valor informacional en el texto final dado que los lectores frecuentemente consultan estos capítulos como referencia, no solo como lectura secuencial.

---

## 6. Evaluación de las seis preguntas del mandato

**P1: ¿La secuencia de los 10 capítulos tiene progresión pedagógica correcta?**

Parcialmente. La secuencia 01-07 es correcta (fundamentos → componentes → evaluación → producción). La inserción de Extensiones (Cap. 08) entre Producción (Cap. 07) y Optimización (Cap. 09) rompe la coherencia del arco de madurez operacional del sistema. Recomendación: mover Cap. 08 al final (ver Recomendación 1).

**P2: ¿Los capítulos están bien conectados entre sí dentro del módulo?**

Sí dentro de las subsecuencias 01-07 y 09-10. Débil entre Cap. 07 y Cap. 08, y entre Cap. 08 y Cap. 09. Las transiciones entre capítulos dentro del texto final deberán incluir párrafos de conexión explícita que el esqueleto naturalmente no tiene. El autor debe ser consciente de que el lector que termina Cap. 07 y abre Cap. 08 necesita un puente de orientación.

**P3: ¿El módulo aterriza bien desde el Módulo 5 y prepara al lector para el Módulo 7?**

El aterrizaje desde el Módulo 5 es débil (no hay conexión explícita). La preparación hacia el Módulo 7 es implícita pero no aprovechada. Ambos aspectos son resolubles con las adiciones recomendadas en los puntos 2 y 6 de las Recomendaciones editoriales.

**P4: ¿Qué capítulos o secciones necesitan más desarrollo técnico?**

El Capítulo 05 necesita una sección de Query Transformations (gap técnico más significativo). El Capítulo 07 necesita la sección de Seguridad. El Capítulo 01 necesita la sección de decisión arquitectónica RAG vs. alternativas. Los capítulos 02, 03 y 05 se beneficiarán de tablas comparativas en el texto final. El resto del contenido tiene densidad técnica suficiente para el formato de esqueleto.

**P5: ¿Hay lagunas conceptuales importantes en el temario?**

Sí, tres lagunas significativas: (a) Query Transformations pre-retrieval (HyDE, multi-query, decomposition), (b) Seguridad y control de acceso en RAG empresarial, (c) Árbol de decisión RAG vs. alternativas (fine-tuning, long context). Una laguna menor: RAG conversacional multi-turno con gestión de historial.

**P6: ¿Qué temas están bien cubiertos y cuáles son superficiales?**

Bien cubiertos: embeddings y modelos de embedding (Cap. 02), chunking y enriquecimiento (Cap. 04), recuperación híbrida y reranking (Cap. 05), RAGAS y evaluación separada retriever/generador (Cap. 06), arquitectura desacoplada y versionado de índices (Cap. 07), patrones Self-RAG/CRAG/FLARE/Agentic RAG (Cap. 10), diagnóstico de problemas por categoría (Cap. 09).

Superficiales o ausentes: query transformations pre-retrieval (ausente), seguridad y control de acceso (ausente), decisión RAG vs. alternativas (ausente), RAG conversacional multi-turno (superficial), observabilidad específica de herramientas RAG (parcial).

---

## Dictamen pedagógico global

El Módulo 6 tiene una estructura pedagógica sólida y un nivel técnico apropiado para el público objetivo. Los 10 capítulos establecen una base completa de Ingeniería de Sistemas RAG que un AI Engineer puede aplicar directamente en producción. Las fortalezas del módulo son la especificidad técnica, el énfasis consistente en evaluación empírica con métricas cuantitativas, y la cobertura del estado del arte (contextual retrieval de Anthropic 2024, CRAG, FLARE, Agentic RAG con LangGraph).

Las intervenciones prioritarias antes de la escritura del texto completo son, en orden de importancia:
1. Añadir la sección de Query Transformations al Capítulo 05.
2. Añadir la sección de Seguridad y Control de Acceso al Capítulo 07.
3. Mover el Capítulo 08 al final del módulo.
4. Añadir los puentes explícitos hacia el Módulo 5 (inicio del módulo) y el Módulo 7 (final del módulo).
5. Añadir la sección de árbol de decisión RAG vs. alternativas al Capítulo 01.

Las intervenciones de segunda prioridad (importantes pero no bloqueantes para el texto completo) son el RAG conversacional multi-turno y las tablas comparativas en los capítulos de comparativa de opciones.
