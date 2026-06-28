---
capitulo: 9
titulo: "Ventana de Contexto: El Escritorio del Modelo"
version: 0.5
tipo: notas-revision
fecha: 2026-06-28
revisor: Editor técnico y pedagógico
estado: Borrador revisión conceptual
---

# Notas de Revisión — Capítulo 9: Ventana de Contexto

**Versión revisada:** 0.5 (desde v0.1)
**Fecha:** 2026-06-28

---

## 1. Resumen de cambios respecto de la v0.1

La versión 0.1 era un borrador funcional pero muy esquemático: cubrió los conceptos esenciales en forma de lista de viñetas sin desarrollo pedagógico, sin diagramas, sin caso real expandido y sin estructura de laboratorio. La v0.5 representa una expansión significativa en todos los ejes.

| Dimensión | v0.1 | v0.5 |
|---|---|---|
| Longitud estimada | ~600 palabras | ~7.200 palabras |
| Secciones | 10 secciones breves sin jerarquía | 17 secciones completas según estructura obligatoria |
| Diagramas Mermaid | 0 | 2 (composición de Context Window + árbol de decisión de estrategias) |
| Tabla comparativa de modelos | Ausente | Tabla con 9 modelos principales y sus ventanas de contexto |
| Fenómeno "lost in the middle" | Ausente | Sección dedicada con implicaciones de diseño |
| Diferenciación contexto/memoria/conocimiento | 4 viñetas sin desarrollo | Subsección 4.1 con tratamiento conceptual completo |
| Estrategias de gestión de contexto | Lista de 5 ítems | Árbol de decisión en diagrama + 6 estrategias descritas con criterios de elección |
| Caso real | 1 párrafo (Data Warehouse sin desarrollo) | Caso expandido con arquitectura completa, cálculo de costo y lecciones aprendidas |
| Conversación con arquitecto | 2 intercambios | 5 intercambios cubriendo el caso "1M de tokens, mandemos todo" y el caso de memoria persistente |
| Errores frecuentes | Ausentes en v0.1 | 6 errores documentados con causa y consecuencia |
| Buenas prácticas | "Diseñar correctamente el contexto" sin desarrollo | 7 prácticas con justificación técnica |
| Laboratorio | 4 pasos sin estructura interna | 5 pasos estructurados con escenario, acción, motivo y resultado esperado |
| Glosario | Ausente | 10 términos con definición precisa |
| Checklist | Ausente | 9 ítems verificables |

---

## 2. Decisiones editoriales tomadas

### 2.1 Título expandido

El título original "Ventana de Contexto (Context Window)" fue expandido a "Ventana de Contexto: El Escritorio del Modelo". La razón: el subtítulo establece de inmediato la analogía central del capítulo, que es la más pedagógicamente efectiva para un lector sin experiencia previa con el concepto. La analogía del escritorio se introduce como subtítulo y luego se desarrolla en la sección 5.

### 2.2 Inclusión del fenómeno "lost in the middle"

Este fenómeno no aparecía en la v0.1 y fue una de las instrucciones explícitas para la v0.5. La decisión editorial fue tratarlo como una subsección del desarrollo conceptual (4.4), no como un error frecuente, porque cambia el modelo mental del lector: no es que el contexto sea un espacio homogéneo donde toda información es igualmente accesible. La posición importa. Ese cambio de modelo mental tiene implicaciones de diseño concretas que se repiten en las buenas prácticas y en el laboratorio.

### 2.3 Tabla comparativa de modelos

Incluida como subsección 4.3 dentro del desarrollo conceptual, no como apéndice. La razón: la tabla es información técnica de referencia que el arquitecto necesita al momento de tomar decisiones de selección de modelo. Colocarla en el desarrollo conceptual —inmediatamente después de explicar qué es el límite— le da contexto inmediato y relevancia. Se incluyó una advertencia explícita de que un contexto más grande no implica mejor calidad, para prevenir el error de diseño más frecuente asociado a este dato.

### 2.4 Árbol de decisión de estrategias en Diagrama 2

La v0.1 listaba estrategias sin criterio de elección. La v0.5 las presenta como un árbol de decisión porque la selección de estrategia depende de preguntas específicas: ¿qué tipo de información se está perdiendo? ¿Qué tipo de continuidad requiere la aplicación? El diagrama guía esa decisión sin prescribir una respuesta única.

### 2.5 Separación explícita de contexto, memoria y conocimiento

La v0.1 distinguía "contexto" de "memoria" en cuatro viñetas. La v0.5 añade un tercer término —conocimiento— y los desarrolla en una subsección completa (4.1). La razón: los errores de diseño más frecuentes en aplicaciones de producción provienen de confundir estos tres conceptos. Un lector que los distingue con precisión tomará mejores decisiones sobre qué incluir en el contexto y qué no.

### 2.6 Caso real con cálculo de costos

El caso del Data Warehouse en la v0.1 era una descripción de 6 líneas. En la v0.5 se desarrolla con: contexto de la empresa, el error de diseño inicial (enviar el esquema completo), la arquitectura correcta (RAG de esquema semántico con 4 pasos), el cálculo aproximado del ahorro en tokens (factor >50) y la lección aprendida. El cálculo de costos es deliberado: es el argumento más efectivo para convencer a equipos que resisten el aumento de complejidad que implica un sistema RAG.

### 2.7 Conversación con arquitecto ampliada a 5 intercambios

La conversación de la v0.1 tenía un único par pregunta-respuesta. La v0.5 la expande a 5 intercambios cubriendo tres dimensiones: el caso "enviar todo" con ventana grande (el argumento más frecuente en equipos con acceso a Gemini 1.5), el cálculo de costo que lo refuta, y el caso de memoria persistente que diferencia Context Window de memory layer. Este último intercambio es importante porque el concepto de memory layer fue una adición de la v0.5 y requería aparición en la conversación para anclar su comprensión.

### 2.8 Laboratorio con experimento de "lost in the middle"

La instrucción explícita pedía un experimento práctico de "lost in the middle". El laboratorio fue diseñado en 5 pasos progresivos:
- Pasos 1-3: experimento con dato en posición central vs. inicial, verificando el efecto de posicionamiento.
- Pasos 4-5: experimento de pérdida de historial y simulación de summarization, que conecta el problema del contexto con la solución práctica más común.

Las herramientas elegidas son interfaces web gratuitas de los modelos principales, sin requerir programación. Esto mantiene el laboratorio accesible para el público objetivo (profesionales de tecnología sin experiencia previa en ML).

---

## 3. Verificaciones de consistencia editorial

- [x] Terminología oficial: primera aparición de Context Window, Token, Large Language Model (LLM), Retrieval-Augmented Generation (RAG) con nombre completo + sigla.
- [x] Sin frases prohibidas: "La IA piensa", "El modelo sabe" — no aparecen. Se usa "el modelo produce", "el modelo genera", "el sistema recupera", "el modelo tiende a".
- [x] Frase de cierre: presente al final del capítulo.
- [x] Continuidad con Capítulo 8 (Prompts): la introducción y el laboratorio hacen referencia a la construcción del contexto como extensión del diseño de prompts.
- [x] Continuidad hacia Capítulo 10 (Embeddings): el cierre y la sección "Próximo capítulo" plantean el problema de cómo un sistema RAG compara semánticamente la consulta con los fragmentos, introduciendo la necesidad de embeddings.
- [x] Diagramas en Mermaid: 2 diagramas (graph TD para composición de Context Window, flowchart TD para árbol de decisión de estrategias).
- [x] Tabla comparativa de modelos: incluida con 9 modelos y advertencia de que el tamaño no implica calidad.
- [x] Tono conversacional-técnico: sin lenguaje de marketing, sin frases vacías.
- [x] Analogía del escritorio: presente en sección 5 con desarrollo y limitaciones explícitas de la analogía.

---

## 4. Puntos abiertos para revisión técnica (v0.8)

Estos ítems no bloquean la v0.5 pero deben ser abordados en la siguiente revisión:

1. **Actualización de la tabla de modelos:** Las ventanas de contexto de los LLMs evolucionan frecuentemente. La tabla deberá revisarse antes de publicación final para reflejar los valores vigentes. Considerar agregar una nota de "fecha de relevamiento" a la tabla para que el lector identifique cuándo fue verificada.

2. **Referencia al paper "Lost in the Middle":** La sección 4.4 menciona el fenómeno documentado por investigadores de Stanford pero no incluye la cita formal. En la v0.8 se debe agregar la referencia: Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" (2023). Verificar si la política editorial del libro incluye referencias bibliográficas en el cuerpo o como apéndice.

3. **Validación del experimento de laboratorio:** El experimento de "lost in the middle" en el laboratorio fue diseñado conceptualmente. Antes de la v0.8, debe ejecutarse en al menos tres modelos (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro) para verificar que los "resultados esperados" descritos son reproducibles y no dependen de versiones específicas de los modelos.

4. **Sliding window como estrategia:** La estrategia de sliding window está mencionada en el diagrama y en el glosario. En la v0.8 podría merecer una subsección propia dentro de "Estrategias avanzadas" si el editor decide expandir esa sección, dado que es la estrategia más implementada en producción para asistentes conversacionales de largo aliento.

5. **Memory layer — profundidad técnica:** El concepto de memory layer se introduce en este capítulo y se desarrollará con mayor profundidad en el capítulo dedicado a arquitecturas de agentes. Verificar con el editor si corresponde añadir una nota de forward reference explícita en la sección 4.1 o si el "Próximo capítulo" al final es suficiente transición.

6. **Diagrama 1 — validación en renderizadores Mermaid:** El diagrama de composición de Context Window usa subgraphs implícitos mediante nodos con texto multilínea. Validar compatibilidad con la versión de Mermaid del pipeline de publicación, especialmente el manejo de saltos de línea dentro de los nodos de tipo `["..."]`.

---

## 5. Evaluación contra criterios de calidad del EDITORIAL_GUIDE

| Criterio | Estado |
|---|---|
| ¿Responde al problema planteado? | Sí — la pregunta "¿por qué olvidó?" está respondida desde la introducción y la motivación |
| ¿Tiene ejemplos? | Sí — caso Data Warehouse, experimentos del laboratorio, tabla de modelos |
| ¿Tiene un caso real? | Sí — asistente de consulta para Data Warehouse (sección 8) con arquitectura completa |
| ¿Tiene laboratorio completo? | Sí — 5 pasos estructurados con escenario, acción, motivo, resultado esperado, validación y reflexión |
| ¿Tiene resumen? | Sí — sección 14, resumen narrativo de 4 párrafos |
| ¿Existe continuidad con el capítulo anterior? | Sí — retoma el concepto de prompt y lo extiende al problema del contexto |
| ¿Prepara correctamente el siguiente? | Sí — plantea el problema de comparación semántica que justifica los embeddings |
| ¿Forma mejores profesionales? | Sí — desarrolla criterio de decisión sobre estrategias de gestión, no memorización |
| ¿Desarrolla criterio? | Sí — secciones de errores frecuentes, buenas prácticas, árbol de decisión y preguntas de reflexión |
| ¿Podría seguir siendo útil dentro de cinco años? | Sí — los principios de gestión de contexto son independientes de los valores específicos de los modelos |
| ¿Explica el problema antes de la solución? | Sí — secciones 3 y 4.1 antes de las estrategias de gestión |

---

## 6. Notas para el editor jefe

- **Extensión:** El capítulo supera la extensión habitual de la v0.5 en aproximadamente un 30%. Esto es intencional: la combinación de la tabla de modelos, el fenómeno "lost in the middle" y las 7 estrategias de gestión requirió espacio adicional para ser tratada con el nivel de rigor necesario para un capítulo de referencia.

- **Laboratorio dividible:** El laboratorio puede ejecutarse en dos sesiones si el lector no dispone de 75 minutos continuos: Pasos 1-3 en una sesión (experimento "lost in the middle", 30 min) y Pasos 4-5 en otra (historial y summarization, 45 min).

- **Dependencia de herramientas externas:** Los pasos del laboratorio dependen de la disponibilidad de las interfaces web de ChatGPT, Claude o Gemini. A diferencia de herramientas como TensorFlow Playground (que es puramente estática), estas interfaces pueden cambiar su comportamiento por actualizaciones de los modelos. Incluir una nota en el laboratorio sugiriendo al lector que los resultados pueden variar entre versiones y que eso es en sí mismo parte del aprendizaje.

- **Fenómeno "lost in the middle" — nivel de certeza:** La sección 4.4 lo presenta como un fenómeno "documentado empíricamente". Es importante mantener ese nivel de cautela: el fenómeno es real pero su intensidad varía entre modelos y versiones. Los modelos más recientes (Gemini 1.5, Claude 3.5) han mostrado mejoras específicas en el manejo del contexto central. La sección no afirma que todos los modelos fallen siempre, sino que el patrón existe y debe ser considerado en el diseño.

- **Glosario ampliado a 10 términos:** La instrucción original pedía 7 términos. Se añadieron "Token" y "Lost in the middle" porque son conceptos introducidos en este capítulo con definición explícita. Se añadió "Sliding Window" porque aparece en el diagrama sin definición en el cuerpo. Si el formato editorial estándar establece un máximo, los tres agregados son los candidatos a mover a un glosario general del módulo.
