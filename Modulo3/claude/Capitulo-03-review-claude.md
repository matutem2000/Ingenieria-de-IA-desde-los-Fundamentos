# Informe Pedagógico — Capítulo 03: Ventanas de Contexto y Gestión de Tokens

**Revisado por:** Director Pedagógico / Claude
**Fecha:** 2026-07-25

---

## NOTA EDITORIAL PRIORITARIA

**El capítulo está en estado de desarrollo incompleto.** Las secciones 01 a 05 tienen contenido editorial desarrollado (equivalente en calidad a los capítulos 01 y 02). Las secciones 06, 07, 08, 09 y 10 son esqueletos mínimos: listas sin desarrollo, sin ejemplos, sin casos de uso, sin "notas del arquitecto" y sin transiciones entre secciones. El capítulo **no puede publicarse** en su estado actual.

---

## 1. Fortalezas

**Las secciones 01 a 05 están bien ejecutadas.** La sección 01 ("¿Qué es una ventana de contexto?") conecta correctamente con el capítulo anterior mediante la afirmación de que administrar la ventana es una de las competencias centrales del Context Engineering. La analogía del escritorio de trabajo es accesible e inmediatamente comprensible.

**Progresión temática lógica en las primeras cinco secciones:** ventana de contexto → token → tokenización → evolución histórica → límites y overflow. Es una secuencia de concreto a abstracto bien construida: primero se entiende el contenedor (ventana), luego la unidad de medida (token), luego el mecanismo (tokenización), luego la evolución y por último el problema de gestión.

**La distinción entre tokens de entrada y de salida (sección 02)** es un detalle técnico relevante que muchos textos omiten. Su inclusión es acertada para el público objetivo (AI Engineers) porque impacta directamente en el modelo de costos.

**El diagrama de flujo texto→token→ID→embedding→modelo (sección 03)** es claro y didáctico. Responde correctamente a la pregunta "¿por qué no simplemente palabras?" con una enumeración de casos reales (palabras compuestas, errores ortográficos, emojis).

**La sección 04 sobre evolución de ventanas de contexto** incluye el matiz clave: "¿más contexto siempre es mejor? No necesariamente." Este principio contraargumentativo es pedagógicamente valioso porque previene un error de novato que ya se anticipa como tentador.

**La sección 05 sobre overflow del contexto** es la más aplicada de las primeras cinco. El caso del asistente de soporte para un incidente multi-día y las cuatro estrategias de administración (descarte selectivo, resumido, recuperación bajo demanda, memoria persistente) dan al lector herramientas de decisión concretas.

---

## 2. Debilidades

**Las secciones 06 a 10 están incompletas al punto de ser inutilizables para el lector.** La sección 06 ("Técnicas de resumido y compresión") enumera cinco técnicas (resumen extractivo, abstractivo, jerárquico, incremental, compresión semántica) sin definir ninguna. La sección 07 ("Optimización de tokens") lista estrategias y métricas sin explicar cómo aplicarlas. La sección 08 ("Patrones de administración") nombra cuatro patrones (Sliding Window, Summary + Window, RAG First, Memoria + Historial + RAG) sin describir cuándo usar cada uno ni cuáles son sus compromisos. La sección 09 es una lista genérica de buenas prácticas. La sección 10 es un índice de lo ya visto con preguntas de autoevaluación sin respuestas de referencia.

**Ruptura cualitativa abrupta entre sección 05 y sección 06.** El lector pasa de secciones de 400-600 palabras con ejemplos, diagramas y notas del arquitecto a secciones de 80-100 palabras con solo bullets. Es uno de los problemas editoriales más graves del módulo.

**Los cuatro patrones de administración del contexto (sección 08)** son conceptos centrales del Context Engineering que merecen un capítulo completo o al menos una sección desarrollada. Nombrarlos sin explicarlos frustra al lector avanzado y no aporta nada al lector novato.

**La sección 10 no prepara al lector para el capítulo siguiente.** Solo menciona "el siguiente capítulo abordará la memoria de corto y largo plazo" sin establecer por qué ese es el paso natural después de haber estudiado la ventana de contexto. La transición es débil.

**Ausencia de laboratorio práctico.** El capítulo cubre conceptos que se prestan naturalmente para ejercicios: estimar tokens de un contexto dado, calcular el costo de una conversación con distintas estrategias, comparar dos arquitecturas de ventana. Ninguno de estos ejercicios aparece.

**El capítulo no menciona herramientas concretas para medir tokens.** Se recomienda reiteradamente "medir el consumo de tokens" pero no se proporciona ninguna referencia a cómo hacerlo (tiktoken de OpenAI, la API de Anthropic, etc.). Para un AI Engineer, esta omisión es significativa.

---

## 3. Conceptos a ampliar

**Sección 06: Técnicas de resumido y compresión.** Cada una de las cinco técnicas mencionadas necesita: (a) una definición de dos líneas, (b) un caso de uso donde sea preferible sobre las otras, y (c) sus limitaciones. Sin esto, la sección es solo un glosario de etiquetas.

**Sección 08: Patrones de administración.** Los cuatro patrones (Sliding Window, Summary + Window, RAG First, Memoria + Historial + RAG) son los patrones arquitectónicos más importantes que el lector encontrará en producción. Cada uno merece: descripción, diagrama, cuándo usarlo, ventajas, compromisos y un ejemplo.

**Lost in the middle:** La sección 04 menciona que ventanas más grandes no garantizan mejores resultados, pero no explica el fenómeno conocido como "lost in the middle" (los modelos tienden a prestar menos atención a información ubicada en el medio del contexto). Esta es una limitación concreta que el AI Engineer debe conocer para diseñar correctamente el orden del contexto.

**Caching de contexto:** Los principales proveedores (Anthropic, OpenAI, Google) ofrecen caching de prefijos de contexto que reduce costos significativamente. Este tema está ausente del capítulo y es de alta relevancia práctica.

---

## 4. Conceptos a resumir o eliminar

**La sección 01 ("Introducción a las ventanas de contexto")** puede integrarse con la sección 02 ("Tokens") dado que ambas secciones introductorias se complementan directamente. Fusionarlas reduciría el capítulo sin pérdida de contenido.

**La lista de "objetivos del capítulo" en sección 01** repite exactamente lo que las secciones posteriores desarrollarán. Si se mantiene, debería ubicarse en la apertura del capítulo, no al final de la sección 01.

**La sección 09 ("Buenas prácticas para aplicaciones empresariales")** en su estado actual es una lista genérica que no agrega nada que no haya aparecido en las secciones anteriores. En su estado actual, debería integrarse a la sección 10 de cierre.

---

## 5. Recomendaciones editoriales

1. **Prioridad editorial urgente:** Desarrollar las secciones 06, 07, 08 y 09 al mismo nivel editorial que las secciones 01-05. El capítulo no puede publicarse en su estado actual. Las secciones de conclusión y cierre (secciones 09 y 10) solo pueden ser definitivas una vez que el contenido que cierran exista.

2. **Desarrollar los cuatro patrones de administración del contexto** (sección 08) con descripción, diagrama, criterio de elección, ventajas y compromisos. Este es el contenido técnico más importante del capítulo y actualmente está ausente.

3. **Expandir la sección 06** con definiciones operativas de cada técnica de resumido y un criterio de selección ("cuándo usar resumen extractivo vs. abstractivo vs. incremental").

4. **Agregar la sección "Herramientas para medir tokens"** con referencias a las APIs de conteo de tokens de los principales proveedores y cómo integrarlo en el flujo de desarrollo.

5. **Agregar un laboratorio práctico** (puede ser la sección 09 reformulada) con dos o tres ejercicios: estimar el costo de una conversación, seleccionar el patrón de administración para un caso dado, calcular qué porcentaje de la ventana ocupa cada capa del contexto.

6. **Incorporar el concepto "lost in the middle"** en sección 04 o 05 como una limitación concreta del aumento de contexto.

7. **Fortalecer el cierre (sección 10)** con una transición más articulada hacia el capítulo 04: explicar que habiendo comprendido los límites y la gestión de la ventana, el paso natural es profundizar en uno de sus componentes más complejos: el diseño de la memoria.

8. **Las secciones 01-05 están listas** para revisión final con ajustes menores de redundancia. Las secciones 06-10 requieren desarrollo completo antes de cualquier otra revisión.
