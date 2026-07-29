# Informe Pedagógico — Módulo 5: AI Engineering para Desarrollo

**Revisado por:** Director Pedagógico / Claude
**Fecha:** 2026-07-25
**Muestra analizada:** Secciones 01, 02, 03, 04, 05 y 06 de todos los capítulos (60 archivos, cobertura total del módulo)

---

## 1. Fortalezas

### Progresión pedagógica del módulo

La secuencia de los 10 capítulos sigue una lógica de capas que es pedagógicamente correcta y coherente: el módulo parte del ecosistema abstracto (qué herramientas existen y por qué, cap. 01), desciende al protocolo concreto de comunicación con los modelos (cap. 02), asciende a los frameworks de orquestación (cap. 03), aborda los patrones de integración con sistemas existentes (cap. 04), y luego avanza secuencialmente hacia el ciclo de vida de producción: testing (cap. 05), CI/CD (cap. 06), evaluación de calidad (cap. 07), observabilidad (cap. 08), optimización de costos (cap. 09) y patrones de diseño avanzados (cap. 10). El lector que avanza linealmente construye primero el "qué" (herramientas), luego el "cómo" (integración), y finalmente el "para siempre" (operación y mantenimiento).

### Densidad técnica apropiada para el público objetivo

El nivel técnico es consistentemente alto y apropiado para un AI Engineer o Arquitecto de IA. Cada sección incluye nombres reales de clases y métodos (`client.messages.create()`, `VectorStoreIndex`, `AnswerRelevancyMetric`), valores concretos con justificación (`top_k=5`, `MAX_CONTEXT_TOKENS=8000`, `threshold=0.95`), cifras de referencia para decisiones de diseño (`breakeven = 1.25 llamadas para prompt caching`, `P95 TTFT < 1 segundo`), y precios reales con ejemplos de cálculo ($3/M tokens de entrada, cálculo de costo mensual a 100K requests). Este nivel de concreción convierte el esqueleto en un recurso de consulta técnica, no solo de lectura.

### Coherencia estructural interna de cada capítulo

El formato de seis secciones es consistente y eficaz: la sección 01 introduce el "por qué" del capítulo con el panorama conceptual, las secciones 02-05 profundizan en subtemas específicos con código y criterios, y la sección 06 cierra con una síntesis de principios accionables y una cita que ancla el capítulo. Esta estructura replica el patrón "hook — desarrollo — cierre" que facilita tanto la lectura lineal como la consulta puntual.

### Principios rectores como dispositivo pedagógico

Cada sección termina con un "Principio rector", "Buena práctica", "Idea central" o "Para recordar" que extrae el mensaje más importante en una sola oración. Este recurso es muy efectivo para el público técnico que puede leer el material rápidamente y necesita anclajes de alta densidad semántica. La variedad de nombres del cierre (no siempre "Principio rector") evita la monotonía formal.

### Cobertura temática del foco declarado

El módulo cubre con solidez los cuatro focos declarados: ecosistema de herramientas (cap. 01-03), patrones de integración y APIs (cap. 02, 04), testing y CI/CD (cap. 05-06), y evaluación y observabilidad (cap. 07-08). El capítulo de costos (cap. 09) es un añadido de alto valor que no siempre aparece en libros de AI Engineering y que está correctamente contextualizado como parte del ciclo de vida de producción.

### Semilla de conceptos para el Módulo 6 (Sistemas RAG)

El módulo siembra de forma efectiva los conceptos que el Módulo 6 profundizará: LlamaIndex y su flujo de ingesta-indexación-consulta (cap. 03, sec. 03), bases de datos vectoriales (pgvector, Qdrant, Chroma) en el contexto de integración de datos (cap. 04, sec. 03), métricas RAGAS específicas de RAG como faithfulness y context recall (cap. 07), y caché semántica (cap. 09, sec. 02). El lector que llega al Módulo 6 ya tiene el vocabulario y los patrones de integración fundamentales.

### Citas seleccionadas

Las citas de cierre de capítulo están bien seleccionadas y son funcionalmente pedagógicas, no decorativas: la de Dijkstra (cap. 01 sec. 06) ancla el principio del stack mínimo viable; la de Peter Drucker (cap. 07 sec. 06) refuerza la evaluación continua; la de Cindy Sridharan (cap. 08 sec. 06) establece observabilidad como requisito no negociable. El vínculo entre cita y principio del capítulo es explícito en todos los casos.

---

## 2. Debilidades

### 2.1 El capítulo 10 está fuera de su posición pedagógica óptima

El capítulo 10 ("Patrones de entrada, salida, Gateway, Circuit Breaker, composición y diseño mantenible") agrupa patrones de diseño de código que son prerrequisitos lógicos para entender el testing, el CI/CD y la observabilidad de capítulos anteriores. El lector que lee testing (cap. 05) aún no conoce el patrón Gateway ni el Circuit Breaker; cuando lee sobre "encapsular el SDK en un wrapper con observabilidad" (cap. 02, sec. 06), no ha visto aún la clase `LLMGateway` descrita en cap. 10, sec. 03. Esta inversión de dependencias cognitivas es el problema estructural más importante del módulo.

Específicamente: el Adapter Pattern para el LLM (cap. 10, sec. 06) debería leerse antes que el mockeo del SDK en unit tests (cap. 05, sec. 02); el patrón Gateway (cap. 10, sec. 03) antes que la observabilidad centralizada (cap. 08); y el Circuit Breaker (cap. 10, sec. 04) antes que las buenas prácticas de consumo de APIs (cap. 02, sec. 06).

### 2.2 DSPy mencionado pero no desarrollado

DSPy aparece en la sección 01 del capítulo 01 como uno de los tres frameworks principales de orquestación (junto a LangChain y LlamaIndex) y en la sección 01 del capítulo 03 como "optimización declarativa de prompts". Sin embargo, no recibe una sección propia en el capítulo 03, que sí dedica secciones completas a LangChain (sec. 02) y LlamaIndex (sec. 03). DSPy representa un paradigma radicalmente diferente al de las cadenas imperativas —optimiza automáticamente los prompts en lugar de escribirlos manualmente— y su ausencia de desarrollo deja una asimetría notoria en el capítulo de frameworks.

### 2.3 Seguridad de aplicaciones de IA tratada de forma fragmentaria

La seguridad en sistemas de IA está dispersa en menciones puntuales sin integración sistemática: gestión de credenciales (cap. 01, sec. 04), detección de prompt injection (cap. 10, sec. 01), redaction de PII en trazas (cap. 08, sec. 02 y sec. 05), logs de seguridad separados (cap. 08, sec. 03). Ningún capítulo trata de forma integrada los vectores de ataque específicos de sistemas LLM: jailbreaking, indirect prompt injection, exfiltración de datos via prompt, output safety y moderación de contenido. Para un módulo de AI Engineering para desarrollo, la ausencia de un tratamiento articulado de seguridad es una laguna conceptual significativa.

### 2.4 Ausencia de puente explícito con el Módulo 4 (Arquitecturas Modernas)

El capítulo 01 comienza directamente con el panorama del ecosistema de herramientas sin establecer el vínculo con los patrones arquitectónicos que el lector ya conoce del Módulo 4 (RAG, agentes, pipelines multi-modal, sistemas multi-agente). El lector que viene de aprender arquitecturas no tiene una guía de "estas son las herramientas con las que se implementan los patrones que aprendiste". Esta desconexión hace que el Módulo 5 parezca iniciar desde cero en lugar de construir sobre el Módulo 4.

### 2.5 Fine-tuning ausente del módulo

La decisión de cuándo hacer fine-tuning versus prompting extenso es una de las decisiones más importantes en AI Engineering, y el módulo no la aborda. En el capítulo 01 sec. 05 se mencionan los modelos disponibles, y en el capítulo 09 sec. 04 se aborda la selección de modelos por costo-beneficio, pero en ningún punto se discute la decisión de "¿cuándo tiene sentido invertir en fine-tuning sobre el modelo base?". Esta es una laguna conceptual especialmente notable en un módulo orientado a desarrollo.

### 2.6 La evaluación humana carece de tratamiento operacional

La evaluación humana aparece como "Layer 4" en la pirámide de testing (cap. 05, sec. 06) y como etapa periódica en el sistema de evaluación continua (cap. 07, sec. 06), pero nunca se describe el proceso operacional: cómo seleccionar anotadores, cómo diseñar rúbricas de anotación, cómo medir y manejar el inter-annotator agreement, y qué herramientas facilitan el proceso (Label Studio, Argilla, Scale AI). El concepto aparece pero sus aspectos operacionales concretos están ausentes.

### 2.7 LangGraph sin sección propia

LangGraph se menciona en cap. 03, sec. 02 y sec. 01 como extensión de LangChain para flujos cíclicos y agentes con estado. Dado que LangGraph es el mecanismo principal para implementar agentes con memoria persistente —concepto central del Módulo 4— y que tiene una API sustancialmente diferente al LCEL estándar, su cobertura como mención subordinada dentro de la sección de LangChain es insuficiente.

### 2.8 Redundancia entre cierres de capítulos consecutivos

Varios cierres de capítulos repiten el mismo principio de "instrumentar desde el primer sprint": cap. 06 sec. 06, cap. 07 sec. 06, cap. 08 sec. 06 y cap. 09 sec. 06 todos incluyen variaciones del mensaje "hacerlo desde el principio tiene un ROI muy superior a hacerlo retroactivamente". El principio es correcto pero su repetición en cuatro cierres consecutivos diluye su impacto y puede producir sensación de relleno en el lector secuencial.

---

## 3. Conceptos a ampliar

### 3.1 DSPy: optimización declarativa de prompts (Capítulo 03)

El paradigma de DSPy —definir el programa como una firma de entrada/salida y dejar que el optimizador encuentre los prompts y few-shot examples óptimos mediante evaluación automática— merece una sección completa en el capítulo de frameworks. Sus componentes fundamentales (`dspy.Signature`, `dspy.ChainOfThought`, `dspy.teleprompt.BootstrapFewShot`) representan una abstracción radicalmente diferente a LangChain y LlamaIndex, y su relación con el sistema de evaluación (cap. 07) es pedagógicamente relevante: DSPy cierra el ciclo entre evaluación y mejora automática de prompts.

### 3.2 Seguridad de aplicaciones LLM: un capítulo o conjunto de secciones integradas

Los siguientes temas deberían tratarse de forma articulada y no dispersa:
- Prompt injection directo e indirecto (especialmente en sistemas RAG donde los documentos recuperados pueden contener instrucciones maliciosas)
- Jailbreaking y estrategias de defensa en el system prompt
- Output safety: moderación de contenido y clasificadores de seguridad pre-deployment
- PII en prompts: detección, redaction y políticas de retención
- Threat modeling específico de sistemas LLM (OWASP Top 10 for LLMs)

### 3.3 Fine-tuning vs prompting: cuándo y cómo (nuevo capítulo o sección en cap. 09)

El módulo necesita un tratamiento de la decisión de fine-tuning que incluya: señales que indican que el prompting ha alcanzado su límite (latencia, costo, capacidad del modelo base), tipos de fine-tuning disponibles (SFT, RLHF, LoRA/QLoRA), casos de uso donde el fine-tuning tiene ROI claro (dominios muy especializados, formato de output muy específico, consistencia de persona/estilo), y el pipeline de fine-tuning en los proveedores principales (OpenAI fine-tuning API, Vertex AI, Anthropic fine-tuning vía enterprise). Este concepto es prerrequisito implícito para entender el sistema de evaluación (cap. 07) en su dimensión de "cuándo la calidad no mejora con más prompting".

### 3.4 LangGraph como sección propia en el capítulo 03

LangGraph merece entre media y una sección completa que cubra: el modelo de nodos-aristas-estado vs el modelo de cadenas lineales de LCEL, cuándo un grafo de estado es la abstracción correcta (agentes con ciclos de reflexión, workflows con ramificación condicional compleja), el `StateGraph` con `add_node()` y `add_edge()`, el `MemorySaver` para persistencia de estado, y los límites conocidos (debugging de grafos con muchos nodos es más complejo que debugging de cadenas).

### 3.5 Evaluación humana: proceso operacional

La sección existente (cap. 07, sec. 06) menciona la evaluación humana como "Layer 4" con anotadores y rúbricas. Ampliar con: proceso de selección y briefing de anotadores, diseño de rúbricas con ejemplos ancla para cada nivel de la escala, medición de inter-annotator agreement (Cohen's Kappa, Krippendorff's Alpha), herramientas de anotación (Label Studio, Argilla), y cómo mantener la coherencia del juicio humano a lo largo del tiempo cuando el sistema evoluciona.

### 3.6 Modelos locales y self-hosting (cap. 01 sec. 05 y cap. 09)

El módulo menciona Ollama y vLLM como opciones para privacidad y soberanía de datos (cap. 01, sec. 05) pero no profundiza en los trade-offs operacionales: costo de GPU vs costo de API, throughput alcanzable con modelos locales, latencia vs API externa, complejidad operacional de mantener el modelo actualizado, y casos de uso donde self-hosting tiene ROI claro. Esto es especialmente relevante en el capítulo de optimización de costos (cap. 09) donde la opción de auto-alojar un modelo open-source tiene un breakeven calculable.

### 3.7 Retry y backoff exponencial con tratamiento propio

El retry con backoff exponencial se menciona en múltiples capítulos (cap. 01 sec. 03, cap. 02 sec. 06, cap. 10 sec. 04) como buena práctica, pero nunca se desarrolla en detalle: la fórmula del backoff con jitter, el manejo diferenciado de errores retryables (429, 529, timeout) vs no retryables (400, 401, 422), la implementación con `tenacity` en Python, y la integración con el Circuit Breaker. Dado que la resiliencia ante fallos del proveedor es un requisito fundamental de producción, este tema merece una sección específica (probablemente en cap. 02 o cap. 10).

---

## 4. Conceptos a resumir o eliminar

### 4.1 Redundancia en mensajes de "instrumentar desde el inicio"

Los cierres de los capítulos 06, 07, 08 y 09 incluyen todos una variación del argumento "el costo de implementar X desde el inicio es mucho menor que el costo de añadirlo retroactivamente". El argumento es correcto, pero presentarlo cuatro veces consecutivas en cuatro capítulos distintos lo convierte en ruido. Recomendación: mantenerlo con plena fuerza en el capítulo donde tiene mayor impacto conceptual (cap. 08, observabilidad, donde la cita de Cindy Sridharan lo articula perfectamente) y reducirlo a una referencia cruzada breve en los demás.

### 4.2 Mención prematura del Circuit Breaker en cap. 02 sec. 06

El capítulo 02 sección 06 ("buenas prácticas para consumir APIs de LLM") menciona el circuit breaker como una de las cuatro disciplinas, sin desarrollo técnico. El lector aún no conoce el patrón. El capítulo 10 sección 04 lo desarrolla completamente. La mención en cap. 02 sec. 06 puede eliminarse o reemplazarse por una referencia: "ver patrones de resiliencia en cap. 10", evitando introducir un término técnico sin definición en un capítulo que no lo va a explicar.

### 4.3 Solapamiento entre cap. 04 sec. 06 y cap. 10 sec. 06 sobre integración incremental

Ambas secciones de cierre abordan el principio de "añadir IA sin reescribir el sistema existente" y mencionan el strangler fig pattern. El cap. 04 sec. 06 lo desarrolla mejor (con el ejemplo del CRM y los antipatrones). El cap. 10 sec. 06 lo reitera desde el ángulo del diseño mantenible. La superposición puede reducirse limitando cap. 10 sec. 06 al ángulo específico de "diseño para cambio de modelo" (que es donde sí aporta perspectiva nueva: la evolucionabilidad medida por cuántos archivos hay que tocar para cambiar el modelo).

### 4.4 Repetición del criterio "implementación directa vs framework"

El criterio de decisión entre implementación directa y uso de framework aparece en: cap. 01 sec. 06 (stack mínimo viable), cap. 03 sec. 01 (principio rector), cap. 03 sec. 04 (comparación), cap. 03 sec. 05 (cuándo no usar un framework), y cap. 03 sec. 06 (cierre). Dentro del capítulo 03, la repetición del mismo argumento en cuatro de las seis secciones es excesiva. El criterio de "test de la implementación directa" (sec. 06) y la tabla de criterios (sec. 04) son los más potentes y podrían consolidarse, dejando las otras menciones como referencias cruzadas.

---

## 5. Recomendaciones editoriales

**1. Reubicar el capítulo 10 como capítulo 5 en la secuencia del módulo.**
El orden recomendado es: 01 (ecosistema), 02 (APIs), 03 (frameworks), 04 (integración con sistemas), 05 (patrones de diseño: Gateway, Circuit Breaker, composición, validación), 06 (testing), 07 (CI/CD), 08 (evaluación), 09 (observabilidad), 10 (costos y optimización). Este orden hace que los patrones de diseño sean un prerrequisito conocido cuando el lector aborde testing, CI/CD y observabilidad. El mockeo del SDK tiene sentido cuando el lector ya vio la clase `LLMGateway`; el logging centralizado tiene sentido cuando el lector ya vio el Adapter Pattern.

**2. Añadir una sección 00 o un párrafo introductorio en el capítulo 01 que explicite el puente con el Módulo 4.**
El texto debe responder: "En el Módulo 4 aprendiste las arquitecturas de sistemas de IA (RAG, agentes, pipelines multi-agente). En este módulo aprenderás el ecosistema de herramientas con el que esas arquitecturas se implementan en producción." Un mapeo breve de arquitectura → herramienta (RAG → LlamaIndex + vector DB, agentes → LangGraph + tool use, observabilidad de arquitectura → LangSmith/Langfuse) daría al lector la orientación que le falta.

**3. Añadir una sección sobre DSPy en el capítulo 03 (entre sec. 03 LlamaIndex y sec. 04 comparación).**
Contenido mínimo: qué problema resuelve DSPy que LangChain y LlamaIndex no resuelven (optimización automática de prompts y few-shot examples), sus primitivas principales (`dspy.Signature`, `dspy.ChainOfThought`, los teleprompters de optimización), el caso de uso donde brilla (sistemas donde el prompt ideal no es obvio y la evaluación automática puede guiar la búsqueda), y sus limitaciones actuales (overhead de runtime, reproducibilidad de la optimización, compatibilidad con modelos open-source).

**4. Añadir una sección de seguridad de aplicaciones LLM al módulo, preferiblemente en el capítulo de patrones de diseño (actual cap. 10, reordenado a cap. 05).**
La sección debe cubrir con código y ejemplos concretos: detección y mitigación de prompt injection directa e indirecta, moderación de outputs antes de exponerlos al usuario, redaction de PII en prompts y logs, y referencia al OWASP Top 10 for LLMs como marco de evaluación de riesgos. Alternativamente, si el equipo editorial decide no crear una sección nueva, las menciones dispersas actuales deben consolidarse en al menos dos de las secciones ya existentes (cap. 02 sec. 06 sobre buenas prácticas, y cap. 08 sec. 03 sobre logging estructurado).

**5. Añadir en el capítulo 09 (actual) una sección sobre fine-tuning como decisión de ingeniería.**
Contenido: señales que indican que el prompting ha alcanzado su techo de calidad para la tarea, comparación de costos total de fine-tuning vs prompting a largo plazo (incluyendo costo de datos de entrenamiento, costo del proceso de fine-tuning, y el diferencial de costo en inferencia con un modelo más pequeño y especializado), y los casos de uso con ROI probado. Esta sección puede ser el puente hacia módulos más avanzados del libro que traten modelos especializados.

**6. Añadir una sección sobre LangGraph en el capítulo 03, entre sec. 02 (LangChain) y sec. 03 (LlamaIndex).**
Contenido: en qué casos un grafo de estado es la abstracción correcta en lugar de una cadena lineal, primitivas básicas (`StateGraph`, `add_node`, `add_conditional_edges`, `MemorySaver`), el modelo de "nodo = función Python con acceso al estado compartido", y cómo conectar LangGraph con LangSmith para observabilidad de grafos. Esto cierra la brecha entre "LangChain para cadenas" y "LangGraph para agentes con estado", conexión que el Módulo 4 (Arquitecturas) habrá establecido conceptualmente.

**7. Consolidar los mensajes repetidos sobre "instrumentar desde el primer sprint" en el capítulo de observabilidad (cap. 08 en el orden actual) y reemplazar las demás instancias por referencias cruzadas breves.**
Esto no es eliminar el mensaje sino concentrar su fuerza en el capítulo donde tiene mayor densidad conceptual, evitando la sensación de repetición en los capítulos 06, 07 y 09.

**8. Añadir en el cierre del módulo (última sección de cap. 10 reordenado, o sec. 06 del último capítulo) una prospectiva explícita hacia el Módulo 6 (Sistemas RAG).**
El texto debe identificar los 3-5 conceptos del Módulo 5 que son prerrequisitos directos del Módulo 6: el flujo de indexación con LlamaIndex, las métricas RAGAS de faithfulness y context recall, la integración con pgvector y bases de datos vectoriales, y el pipeline de evaluación automatizada que el Módulo 6 aplicará específicamente al ciclo de RAG. Esta prospectiva da al lector propósito para lo que sigue y refuerza la coherencia del libro como sistema.

**9. Añadir al capítulo 03 un criterio cuantitativo de decisión más preciso para la elección entre frameworks.**
La sección 04 menciona el criterio de "200 líneas de código". Este criterio puede complementarse con una tabla de decisión que cruce: número de pasos en el pipeline × variabilidad del flujo × volumen de datos para recuperación × tamaño del equipo → recomendación. Una tabla de 3×3 con los casos más comunes daría al lector un artefacto de decisión reutilizable.

**10. Uniformizar el tratamiento de herramientas de evaluación a lo largo del módulo.**
RAGAS y DeepEval se introducen en cap. 01 sec. 01, se desarrollan en cap. 07 sec. 02, se usan en cap. 05 sec. 06 (pirámide) y cap. 06 sec. 01 y 02 (CI/CD). TruLens aparece en cap. 07 sec. 02 sin referencia posterior. Arize Phoenix aparece en cap. 08 sec. 05 como adición de última hora. Recomendación: construir en el capítulo 01 o en el capítulo 07 un mapa explícito de herramientas de evaluación que el lector pueda usar como referencia constante, evitando la sensación de que las herramientas se introducen en capítulos diferentes sin un tratamiento integrador.

---

## Evaluación por criterio solicitado

### ¿La secuencia de los 10 capítulos tiene progresión pedagógica correcta?

**Mayoritariamente sí, con una excepción importante.** Los capítulos 01 a 09 tienen una progresión correcta de concreto a abstracto, de herramienta a proceso, de construcción a operación. El capítulo 10 rompe la progresión al colocar patrones de diseño de código (Gateway, Circuit Breaker, composición tipada) después de capítulos que los presuponen (testing en cap. 05, CI/CD en cap. 06, observabilidad en cap. 08). La reubicación del capítulo 10 como capítulo 5 resolvería el único problema estructural significativo del módulo.

### ¿Los capítulos están bien conectados entre sí?

**Sí, con oportunidades de mejora.** Hay referencias cruzadas implícitas (cap. 07 sobre evaluación remite conceptualmente a cap. 05 sobre testing; cap. 09 sobre costos remite a cap. 07 sobre elección de modelo), pero raramente explícitas mediante texto como "como vimos en el capítulo anterior". Las citas explícitas entre capítulos mejorarían la cohesión y reducirían la sensación de que cada capítulo es un documento independiente.

### ¿El módulo aterriza bien desde el módulo anterior y prepara bien al lector para el siguiente?

**La preparación para el Módulo 6 es buena; el aterrizaje desde el Módulo 4 es débil.** El Módulo 6 sobre sistemas RAG encontrará al lector con LlamaIndex, vector stores, RAGAS y pipelines de evaluación ya vistos. Sin embargo, el Módulo 4 sobre Arquitecturas Modernas no tiene un puente explícito con el Módulo 5: el capítulo 01 no menciona que las herramientas que describe son las que implementan los patrones arquitectónicos del módulo anterior.

### ¿Qué capítulos o secciones necesitan más desarrollo técnico?

En orden de prioridad: (1) Capítulo 03 sec. 02 para LangGraph —actualmente una mención subordinada—, (2) Capítulo 03 para DSPy —ausente como sección propia—, (3) toda la dimensión de seguridad de aplicaciones LLM, actualmente fragmentada, (4) Capítulo 09 para añadir la dimensión de fine-tuning como alternativa a la optimización de costos vía prompting.

### ¿Hay lagunas conceptuales importantes en el temario?

Tres lagunas de relevancia alta: (1) **Seguridad de aplicaciones LLM** — prompt injection, output safety, PII; (2) **Fine-tuning como decisión de ingeniería** — cuándo, cómo, ROI; (3) **LangGraph como herramienta de implementación de agentes** — que conecta directamente con el Módulo 4. Una laguna de relevancia media: el proceso operacional de evaluación humana (herramientas, rúbricas, inter-annotator agreement).

### ¿Qué temas están bien cubiertos y cuáles son superficiales?

**Bien cubiertos:** APIs y SDKs (cap. 01-02), LangChain y LlamaIndex (cap. 03), patrones de integración (cap. 04), unit e integration testing (cap. 05), pipelines de CI/CD (cap. 06), métricas de evaluación y LLM-as-judge (cap. 07), observabilidad con los tres pilares (cap. 08), prompt caching y optimización de costos (cap. 09), patrones Gateway y Circuit Breaker (cap. 10), parsing robusto de salida (cap. 10).

**Superficiales o ausentes:** DSPy (mencionado, no desarrollado), LangGraph (mencionado en subordinación), seguridad de aplicaciones LLM (fragmentada), fine-tuning como alternativa de ingeniería (ausente), evaluación humana operacional (conceptual sin proceso), modelos self-hosted/locales (mencionados sin desarrollo), retry/backoff como patrón técnico completo (disperso).

---

*Nota sobre el formato esqueleto: el material está en estado de esquema estructural denso. La profundidad técnica del esquema es alta y el autor tiene una base sólida para expandir cada sección a texto completo. Las recomendaciones de este informe se refieren a la arquitectura pedagógica del módulo, no a la extensión del texto actual.*
