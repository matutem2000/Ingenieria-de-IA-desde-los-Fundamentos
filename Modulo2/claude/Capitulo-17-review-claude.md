# Informe Editorial — Capítulo 17

**Capítulo:** 17 — Patrones de Prompt Engineering  
**Módulo:** 2 — Prompt Engineering Profesional  
**Versión revisada:** 0.1  
**Fecha de revisión:** 2026-07-01  
**Rol:** Director Pedagógico y Revisor Editorial

---

## 1. Fortalezas

**Estructura repetida como andamiaje didáctico (todas las secciones)**

El capítulo mantiene de forma consistente un esquema seccional uniforme: cita de apertura, objetivos, introducción, definición del patrón, cuándo utilizarlo, ventajas/limitaciones, caso de estudio, buenas prácticas, errores frecuentes, ideas clave y transición. Esta repetición no es un defecto sino un recurso pedagógico deliberado: el lector que avanza en el capítulo incorpora el marco mental del análisis antes de necesitar aplicarlo. Permite además leer cada sección de forma autónoma sin perder el hilo.

**Progresión lógica de complejidad bien calibrada (Secciones 01 a 09)**

El orden de presentación de patrones —Zero-Shot, One-Shot, Few-Shot, Chain of Thought, Self-Consistency, ReAct, Tree of Thoughts, marco comparativo— sigue un eje de complejidad creciente que resulta pedagógicamente apropiado. Cada patrón motiva el siguiente: las limitaciones expuestas en una sección justifican la aparición del patrón siguiente. Esto genera un hilo narrativo que mantiene la coherencia del capítulo.

**Transiciones explícitas entre secciones (todas las secciones)**

Cada sección cierra con un párrafo de transición que anuncia el siguiente patrón y anticipa el vínculo entre ambos. Este mecanismo reduce la sensación de discontinuidad y sostiene la lectura continua del capítulo como un todo. Es un recurso bien aplicado.

**Uso de casos de estudio situados en contextos empresariales reales (Secciones 02 a 09)**

Los casos de estudio —asistente para clasificar reclamos, resúmenes de informes ejecutivos, conversión de reportes técnicos, clasificación de siniestros, análisis de incidentes de ciberseguridad, operaciones financieras inusuales, asistente corporativo, arquitectura de plataforma— anclan los patrones en situaciones empresariales verosímiles. Esto facilita la transferencia del conocimiento y refuerza el perfil profesional del libro.

**Uso de diagramas Mermaid para representar la estructura de cada patrón (Secciones 02 a 09)**

Los diagramas de flujo ilustran visualmente la arquitectura de cada patrón antes de la explicación textual. Funcionan bien como ayuda cognitiva para lectores con preferencia visual y reducen la carga conceptual en el momento de la lectura.

**La sección final como cierre sintetizador (Sección 09)**

La Sección 09 cumple una función pedagógica importante: el diagrama de decisión, la tabla comparativa y el caso de estudio multi-patrón permiten al lector construir una visión integrada del capítulo. El principio de "comenzar con el patrón más simple" está bien articulado.

**Calidad de las citas de apertura (Secciones 01 y 05)**

Destacan especialmente la cita de Sección 01 ("Conocer un patrón no significa aplicarlo siempre. La ingeniería consiste en saber cuándo utilizarlo y cuándo descartarlo.") y la de Sección 05 ("Resolver un problema complejo rara vez consiste en encontrar la respuesta correcta de inmediato. Consiste en construir un razonamiento que conduzca a ella."). Ambas sintetizan la tesis del patrón con precisión y tono profesional.

---

## 2. Debilidades

**Ausencia de ejemplos concretos de prompts reales (Secciones 02, 03, 04, 05, 06)**

El capítulo explica cada patrón conceptualmente pero nunca muestra un prompt real. Para Zero-Shot, One-Shot y Few-Shot en particular, la ausencia de un bloque de código con un prompt completo —instrucción + ejemplo + consulta— constituye una laguna pedagógica importante. El lector termina la sección sin saber exactamente cómo luce un prompt de ese patrón escrito en texto. Esto es especialmente grave en Sección 03 (One-Shot) y Sección 04 (Few-Shot), donde el mecanismo de los ejemplos es precisamente el núcleo del patrón.

**El mecanismo de Self-Consistency no está suficientemente explicado (Sección 06)**

La Sección 06 explica que el sistema "genera varias cadenas de razonamiento y selecciona la más consistente", pero nunca aclara quién hace esa selección, ni cómo se implementa en la práctica. ¿El propio LLM compara sus respuestas? ¿Lo hace código externo? ¿Se usa votación por mayoría? Esta ambigüedad deja al lector con una comprensión incompleta del patrón. La sección presenta el qué pero omite el cómo en un nivel mínimo aceptable para un libro de ingeniería.

**Tree of Thoughts carece de explicación del mecanismo de evaluación y poda (Sección 08)**

El texto menciona que el modelo "evalúa cada rama" y "continúa desarrollando únicamente las más prometedoras", pero no ofrece ningún detalle sobre cómo funciona esa evaluación. En un patrón cuyo valor central es precisamente la exploración y el descarte de alternativas, la omisión del mecanismo de evaluación debilita la comprensión del patrón. El lector no puede distinguir entre una aplicación correcta y una incorrecta de ToT.

**El orden en la Sección 01 no coincide con el orden de desarrollo del capítulo (Sección 01)**

La tabla de clasificación inicial presenta los patrones en este orden: Zero-Shot, One-Shot, Few-Shot, Chain of Thought, ReAct, Tree of Thoughts, Self-Consistency. Sin embargo, el capítulo los desarrolla en orden diferente: Zero-Shot (S02), One-Shot (S03), Few-Shot (S04), Chain of Thought (S05), Self-Consistency (S06), ReAct (S07), Tree of Thoughts (S08). Self-Consistency aparece como último en la tabla introductoria pero se desarrolla antes de ReAct. Esta inconsistencia puede generar confusión en el lector que consulta la tabla como referencia.

**La cita de cierre es idéntica en todas las secciones (Secciones 02 a 09)**

La frase "Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones." cierra todas y cada una de las ocho secciones con exactamente el mismo texto. La repetición literal diluye el impacto de la frase y genera una sensación de plantilla mecánica. En la Sección 01 funciona como conclusión central del capítulo; en todas las demás pierde resonancia.

**Ausencia de criterios cuantitativos para la toma de decisiones (Secciones 04, 05, 06, 08)**

Las secciones mencionan repetidamente que el costo debe equilibrarse con el beneficio, pero nunca ofrecen ningún criterio orientador: ¿a partir de cuántos ejemplos se pasa de One-Shot a Few-Shot? ¿Cuántas cadenas de razonamiento son típicas en Self-Consistency? ¿En qué orden de magnitud varía el consumo de tokens entre patrones? El lector queda sin referencias prácticas mínimas.

**Redundancia conceptual en la tabla comparativa final (Sección 09)**

La tabla de comparación general de la Sección 09 agrega la columna "Complejidad" que repite información ya transmitida a lo largo del capítulo, sin aportar un criterio de decisión nuevo. La columna "Costo" es orientativa pero usa categorías poco precisas ("Bajo", "Medio", "Variable", "Alto") que no añaden valor sin un contexto de referencia.

---

## 3. Conceptos que conviene ampliar

**Prompts reales como ejemplos del patrón (Secciones 02, 03, 04, 05)**

La laguna más crítica del capítulo es la ausencia total de prompts escritos. Se recomienda incorporar al menos un bloque de código con un prompt completo para cada patrón principal. En particular:
- Sección 02: un prompt Zero-Shot para clasificación simple o resumen.
- Sección 03: un prompt One-Shot mostrando instrucción + ejemplo completo (entrada y salida) + consulta.
- Sección 04: un prompt Few-Shot con al menos tres ejemplos que demuestren diversidad representativa.
- Sección 05: un prompt que incluya la instrucción "razona paso a paso antes de responder" o equivalente.

Sin estos ejemplos concretos, el capítulo enseña el "qué" de los patrones pero no el "cómo" a nivel operativo.

**Mecanismo de implementación de Self-Consistency (Sección 06)**

Esta sección necesita al menos un párrafo que explique las dos estrategias de implementación más comunes: (a) múltiples llamadas independientes al modelo con temperatura elevada y selección por mayoría de votos, y (b) una única llamada solicitando explícitamente al modelo que razone por múltiples caminos. Sin esta distinción, el lector no puede implementar el patrón.

**Mecanismo de evaluación y poda en Tree of Thoughts (Sección 08)**

La Sección 08 requiere expandirse para explicar quién evalúa las ramas (¿el mismo LLM como juez?, ¿una función externa?), cuál es el criterio de poda, y cómo se implementa el ciclo de expansión-evaluación-descarte en la práctica. El caso de estudio de la arquitectura empresarial es bueno, pero el diagrama muestra solo que "Idea B" se selecciona sin explicar por qué o mediante qué proceso.

**Relación entre ReAct y la arquitectura de agentes (Sección 07)**

La Sección 07 menciona al cierre que ReAct "constituye uno de los fundamentos conceptuales de los agentes modernos", pero no desarrolla esa conexión. Para un libro de Ingeniería de IA, este es un puente importante que debería anticipar el Capítulo 18 o los capítulos de agentes con mayor profundidad. Al menos un párrafo breve sobre cómo ReAct se implementa en frameworks reales (LangChain, LlamaIndex, etc.) o en llamadas a herramientas daría más densidad a la sección.

**Criterios prácticos para la cantidad de ejemplos en Few-Shot (Sección 04)**

La sección afirma que "la cantidad de ejemplos no constituye una regla fija" pero no ofrece ninguna orientación práctica sobre rangos típicos, ni sobre cómo medir si agregar un ejemplo adicional mejora los resultados. Se recomienda incorporar alguna referencia orientativa (por ejemplo: rangos habituales de 3 a 10 ejemplos, o cómo construir un experimento de ablación básico para medir el impacto de cada ejemplo adicional).

**Criterios de comparación entre razonamientos en Self-Consistency (Sección 06)**

La sección menciona que se debe "comparar razonamientos mediante criterios objetivos" (buenas prácticas), pero nunca define cuáles son esos criterios. Este punto requiere al menos un párrafo concreto.

---

## 4. Conceptos que pueden resumirse

**Las listas de "Buenas prácticas" y "Errores frecuentes" son casi intercambiables entre secciones (Secciones 02 a 08)**

Cada sección repite variaciones de las mismas cuatro o cinco buenas prácticas: comenzar por lo simple, medir resultados, no aplicar el patrón en exceso, mantener los componentes actualizados. Lo mismo ocurre con los errores frecuentes: aplicarlo indiscriminadamente, confundir cantidad con calidad, no validar. En secciones como la 06 (Self-Consistency) y la 08 (Tree of Thoughts), estas listas no aportan nada específico al patrón en cuestión y podrían reducirse a uno o dos ítems genuinamente distintivos de ese patrón.

**Las introducciones de sección repiten el cierre de la transición anterior (Secciones 03 a 08)**

Cada sección abre con un párrafo que recapitula lo visto en la sección anterior antes de presentar el nuevo patrón. Si el lector lee el capítulo de corrido, esta información es redundante. Si el lector llega directamente a una sección, el párrafo introductorio tampoco le es suficiente para comprender el patrón anterior. Se podría condensar ese vínculo en una oración o en una referencia cruzada ("ver Sección 02"), en lugar de un párrafo completo.

**La Sección 09 repite la tabla de la Sección 01 con información adicional mínima**

La Sección 01 presenta una tabla de clasificación con siete patrones y su objetivo principal. La Sección 09 presenta una tabla comparativa con los mismos siete patrones, añadiendo solo "complejidad", "costo" y "caso de uso típico". Dado que la Sección 09 es el cierre del capítulo y tiene la función de integrar, la tabla podría ser más densa (incluir, por ejemplo, el criterio de decisión para elegir ese patrón) o bien la tabla de la Sección 01 podría eliminarse y remitir al lector al cierre.

**El diagrama de flujo de la Sección 09 no incluye Self-Consistency de forma clara**

En el diagrama de decisión de la Sección 09, Self-Consistency aparece como caso residual ("si no hay herramientas externas y no hay múltiples alternativas, entonces Self-Consistency"). Esto no refleja con precisión cuándo usar ese patrón y en la práctica genera confusión. El nodo podría simplificarse o el diagrama reorganizarse para que Self-Consistency aparezca como una capa aplicable sobre CoT cuando la criticidad lo justifique.

---

## 5. Recomendaciones editoriales

**R1 — Incorporar al menos un bloque de prompt real por patrón (Secciones 02, 03, 04, 05)**

Es la recomendación más urgente del capítulo. Para Zero-Shot, One-Shot y Few-Shot, el texto puede permanecer exactamente como está; basta añadir un bloque de código formateado (usando triple backtick) que muestre un prompt completo y representativo. Para Chain of Thought, mostrar la instrucción que activa el razonamiento paso a paso. Sin este material, el capítulo es teórico en exceso para un libro de ingeniería.

**R2 — Corregir el orden de la tabla introductoria para que coincida con el orden de desarrollo del capítulo (Sección 01)**

La tabla de la Sección 01 presenta Self-Consistency al final y ReAct antes de Tree of Thoughts. El capítulo desarrolla Self-Consistency en la Sección 06 (antes de ReAct en la 07). Reordenar la tabla para que coincida con el orden de aparición real evitará confusión al lector que use la tabla como índice.

**R3 — Variar o eliminar la cita de cierre repetida (Secciones 02 a 09)**

La frase de cierre "Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones." es efectiva como epílogo del capítulo completo (Sección 01), pero su repetición literal en cada sección la vacía de significado. Se sugiere utilizarla solo en la Sección 01 y en la Sección 09 como cierre del capítulo, o reemplazarla en las secciones intermedias por una frase distinta que conecte con el patrón específico de cada sección.

**R4 — Añadir un párrafo técnico mínimo sobre la implementación de Self-Consistency (Sección 06)**

Sin reescribir el estilo existente, basta agregar un párrafo que describa la estrategia de múltiples llamadas con temperatura elevada y selección por mayoría de votos, junto con una referencia al costo implicado. Este párrafo puede integrarse después del diagrama, antes de la sección "¿Cuándo utilizarlo?".

**R5 — Ampliar el mecanismo de evaluación de ramas en Tree of Thoughts (Sección 08)**

Añadir un párrafo breve entre el diagrama y la sección "¿Cuándo utilizar Tree of Thoughts?" que explique cómo el modelo (o un evaluador externo) determina qué ramas continuar. Incluso una referencia al concepto de "self-evaluation" o "LLM-as-judge" aplicado a este contexto daría al lector las herramientas mínimas para entender el mecanismo.

**R6 — Reducir las listas de "Buenas prácticas" y "Errores frecuentes" a ítems específicos del patrón (Secciones 04 a 08)**

Para cada sección, conservar solo los ítems que son genuinamente específicos del patrón en cuestión y eliminar o consolidar los ítems genéricos (medir resultados, no sobredimensionar, actualizar cuando cambie el negocio) en una sola nota al pie o en la Sección 01 como principios generales de uso de patrones. Esto reducirá la sensación de repetición sin perder información útil.

**R7 — Integrar la conexión entre ReAct y arquitectura de agentes (Sección 07)**

Añadir un párrafo corto al final de la Sección 07, antes de las "Ideas clave", que anticipe cómo ReAct se relaciona con los sistemas agénticos que el libro presumiblemente aborda en capítulos posteriores. Esto refuerza la continuidad narrativa del módulo y justifica la importancia estratégica del patrón más allá del uso inmediato.

**R8 — Añadir un ejemplo de prompt incorrecto para ilustrar errores frecuentes (Secciones 03, 04)**

La sección "Errores frecuentes" menciona errores como "utilizar ejemplos que no representan el problema real" o "contradecir las instrucciones mediante el ejemplo", pero el lector no puede visualizar a qué se refiere exactamente. Un contraejemplo concreto —un prompt mal diseñado seguido de una breve indicación de por qué falla— daría a estas listas una utilidad pedagógica que hoy no tienen.

**R9 — Considerar si la Sección 09 cubre todos los patrones presentados en el capítulo**

El caso de estudio de la Sección 09 (tres asistentes: resúmenes, contratos, coordinación) solo ejemplifica Zero-Shot, Chain of Thought y ReAct. Self-Consistency y Tree of Thoughts quedan fuera del caso integrador. Se sugiere ampliar el caso con una cuarta o quinta situación que justifique esos patrones, o bien aclarar explícitamente por qué el caso de estudio es representativo sin necesitar cubrir todos los patrones.

---

*Informe producido en rol de Director Pedagógico y Revisor Editorial. No incluye reescritura de contenidos. Todas las observaciones son de carácter analítico y orientativo.*
