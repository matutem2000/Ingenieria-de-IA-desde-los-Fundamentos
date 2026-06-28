---
capitulo: 8
titulo: "Tokens: La Unidad de Medida de la Inteligencia Artificial"
version: 0.5
tipo: notas-revision
fecha: 2026-06-28
revisor: Editor técnico y pedagógico
estado: Borrador revisión conceptual
---

# Notas de Revisión — Capítulo 8: Tokens

**Versión revisada:** 0.5 (desde v0.1)
**Fecha:** 2026-06-28

---

## 1. Resumen de cambios respecto de la v0.1

La versión 0.1 presentaba los conceptos fundamentales de forma correcta pero esquemática. Cubría el qué (definición de token) y parte del por qué (costos, contexto, velocidad), pero carecía de la profundidad técnica y la estructura pedagógica necesaria para un lector que debe tomar decisiones de arquitectura. La v0.5 expande todos los ejes con contenido accionable.

| Dimensión | v0.1 | v0.5 |
|---|---|---|
| Longitud estimada | ~600 palabras | ~6.800 palabras |
| Secciones | 11 básicas | 17 completas según estructura obligatoria |
| Diagramas Mermaid | 0 | 2 (tokenización + entrada/salida con costos) |
| Explicación de BPE | Ausente | Sección dedicada con ejemplo paso a paso |
| Tabla diferencias por idioma | Ausente | 8 idiomas con factor y porcentaje de impacto |
| Tabla precios de API | Ausente | 4 modelos con precio entrada/salida y ratio |
| Código Python (tiktoken) | Ausente | 10+ líneas comentadas con análisis |
| Caso empresarial | 1 párrafo genérico | Caso RAG financiero con estimación corregida ×16 |
| Conversación con arquitecto | 2 intercambios | 5 intercambios con diagnóstico y estrategias |
| Errores frecuentes | Ausentes | 5 errores con heurística asociada |
| Buenas prácticas | 4 ítems en lista | 6 prácticas con justificación técnica |
| Laboratorio | 4 pasos simples | 5 pasos estructurados completos + 3 desafíos |
| Preguntas de reflexión | 3 | 7 con distintos niveles de análisis |
| Glosario | Ausente | 8 términos con definición precisa |
| Checklist | Ausente | 10 ítems verificables |

---

## 2. Decisiones editoriales tomadas

### 2.1 Título expandido

El título original "Tokens" fue expandido a "Tokens: La Unidad de Medida de la Inteligencia Artificial". La razón: el subtítulo establece desde el título la importancia del concepto en relación al sistema completo, no solo como detalle técnico. Un lector que ve solo "Tokens" puede subestimar el alcance del capítulo. Un lector que ve "La Unidad de Medida de la IA" entiende que se trata de un concepto que permea todo el sistema.

### 2.2 Explicación de BPE con ejemplo paso a paso

La v0.1 no explicaba el algoritmo de tokenización. Se consideró que BPE es el mecanismo central que explica por qué los tokens se comportan como se comportan —incluyendo la variación por idioma y la capacidad de representar palabras desconocidas. Un profesional que entiende BPE conceptualmente puede razonar sobre estas consecuencias. Uno que solo conoce la definición de token no puede.

El ejemplo usa un corpus mínimo de cuatro frases para hacer visible el algoritmo sin matemáticas. El criterio aplicado fue el mismo que en el Capítulo 5 (Deep Learning): explicar el mecanismo con suficiente precisión para permitir razonamiento, sin requerir que el lector implemente el algoritmo.

### 2.3 Tabla de diferencias por idioma

La inclusión de la tabla con 8 idiomas responde a un problema real y documentado en proyectos de IA: los presupuestos se calculan usando benchmarks en inglés y luego la realidad del idioma operativo genera costos inesperadamente mayores. La tabla no pretende ser una referencia exacta (los valores dependen del tokenizador y del texto específico), por eso incluye rangos y una nota aclaratoria.

Se incluyeron el chino y el japonés como contraejemplos: idiomas donde el texto es más compacto en tokens que en inglés, lo que demuestra que la penalización no es universal y depende de la estructura del idioma y del tokenizador.

### 2.4 Tabla de precios de API con cuatro modelos

La v0.1 mencionaba que "los proveedores cobran por token" sin dar cifras. Se decidió incluir precios de referencia reales con dos aclaraciones explícitas: que son aproximaciones al momento de redacción y que deben verificarse en la documentación oficial. El objetivo no es que el lector memorice precios sino que internalice tres conceptos: (1) los tokens de salida cuestan más que los de entrada, (2) el ratio es consistentemente de 4× a 5×, y (3) hay órdenes de magnitud de diferencia entre modelos.

### 2.5 Caso empresarial con la brecha ×16 en la estimación

El caso de la empresa financiera con contratos RAG fue diseñado para hacer visible el error más común y más costoso en proyectos de IA: presupuestar tokens mirando solo la pregunta visible del usuario. La brecha de 16× entre la estimación inicial ($400/mes) y la estimación corregida ajustada por idioma ($6.278/mes) no está exagerada. Es un valor representativo de lo que ocurre cuando se ignoran sistemáticamente el prompt del sistema, el historial, los documentos RAG y el factor de idioma.

Cada uno de estos cuatro factores fue documentado como "problema" numerado para que el lector pueda identificarlos en sus propios proyectos.

### 2.6 Cinco intercambios en la conversación con el arquitecto

El intercambio de la v0.1 era de 2 fragmentos y se limitaba a plantear la pregunta de "¿cuántos tokens enviás?". La v0.5 desarrolla la conversación hasta incluir el diagnóstico del prompt del sistema (2.400 tokens), la causa del crecimiento orgánico, y las tres estrategias para gestionar el historial. Esta extensión permite que el lector vea no solo el diagnóstico sino también el razonamiento que conduce a las soluciones.

### 2.7 Error frecuente sobre "lost in the middle"

Se incluyó el fenómeno "lost in the middle" como error frecuente porque combina dos conceptos del capítulo (cantidad de tokens en el contexto y calidad de la respuesta) de una forma que no es obvia. Muchos equipos asumen que más contexto = mejor respuesta de forma lineal. El fenómeno demuestra que la relación es no monótona y que la posición de la información en el contexto importa, no solo su presencia.

### 2.8 Código Python con análisis de tokenización en español

El código incluye deliberadamente la tokenización de "La tokenización es fundamental" para mostrar cómo el término "tokenización" se divide en subtokens en el tokenizador cl100k_base. Este ejemplo hace visible, en código ejecutable, la razón por la que el español consume más tokens que el inglés: las palabras largas con morfología compleja generan múltiples subtokens.

### 2.9 Laboratorio con brecha de estimación como escenario central

El escenario del laboratorio (prompt del sistema que creció orgánicamente durante 6 meses) refleja una situación real que la mayoría de los equipos reconocerá. El Paso 5 (cálculo del impacto económico) cierra el laboratorio con un output concreto y cuantificable. El objetivo es que el lector salga del laboratorio con un número: cuánto está ahorrando (o desperdiciando) con su prompt actual.

---

## 3. Verificaciones de consistencia editorial

- [x] Terminología oficial: primera aparición de Token, Large Language Model (LLM), Byte-Pair Encoding (BPE), Retrieval-Augmented Generation (RAG), Inteligencia Artificial (IA) con nombre completo + sigla.
- [x] Sin frases prohibidas: "La IA piensa", "La IA entiende", "El modelo sabe" — no aparecen. Se usa "el modelo produce", "el modelo procesa", "el sistema recupera", "el modelo genera".
- [x] Frase de cierre obligatoria: presente al final del capítulo antes del "Próximo capítulo".
- [x] Continuidad con Capítulo 7 (Embeddings): la introducción no rompe la continuidad aunque no hace referencia explícita a embeddings (capítulo anterior). Se recomienda en v0.8 agregar una oración de transición desde embeddings hacia tokens.
- [x] Continuidad hacia Capítulo 9 (Ventana de Contexto): la sección "Próximo capítulo" establece claramente que la ventana de contexto es el límite que gobernierna los tokens, creando tensión narrativa hacia el siguiente capítulo.
- [x] Diagramas en Mermaid: 2 diagramas (flowchart del proceso de tokenización + flowchart de tokens entrada/salida con costos).
- [x] Tono conversacional-técnico: sin lenguaje de marketing, sin frases vacías, sin "increíble", "revolucionario" o equivalentes.
- [x] Tablas con notas aclaratorias: las tablas de precios y diferencias por idioma incluyen notas que aclaran que los valores son aproximados y pueden cambiar.
- [x] Código Python comentado: cada línea o bloque de líneas tiene un comentario que explica el propósito.
- [x] Heurísticas en errores frecuentes: cada uno de los 5 errores incluye una heurística concreta para reconocerlo y evitarlo.

---

## 4. Puntos abiertos para revisión técnica (v0.8)

Estos ítems no bloquean la v0.5 pero deben ser abordados en la siguiente revisión:

1. **Transición explícita desde Capítulo 7 (Embeddings):** La v0.5 no menciona embeddings en la introducción. En v0.8 se debería agregar una oración que conecte: "Los embeddings, que estudiamos en el capítulo anterior, operan sobre representaciones vectoriales de tokens. Antes de profundizar en embeddings, necesitamos tener claro qué son exactamente los tokens."

2. **Validación de valores en la tabla de diferencias por idioma:** Los rangos de la tabla (por ejemplo, árabe +70% a +110%) son consistentes con experiencia práctica pero no están respaldados por una fuente publicada citada. En v0.8 se debería o bien citar una fuente (paper de benchmark, documentación de proveedor) o bien agregar una nota que indique explícitamente que son estimaciones basadas en experiencia y que varían según el tipo de texto.

3. **Actualización de precios de API:** Los precios en la tabla de la Sección 4.4 corresponden a junio 2026 y cambiarán. Se recomienda agregar en el proceso de publicación un mecanismo de verificación de precios (al menos trimestral) o transformar la tabla en una referencia a las páginas de pricing oficiales de cada proveedor, manteniendo solo los ratios como información estable.

4. **Diagrama Mermaid 2 — validación de subgraphs anidados:** El diagrama de tokens entrada/salida usa subgraphs con direction TB y flowchart TB. Validar compatibilidad con la versión de Mermaid usada en el pipeline de publicación antes de promover a v0.8.

5. **Compatibilidad del código tiktoken con modelos Anthropic y Google:** La Sección 12 menciona `anthropic.count_tokens` y `google-generativeai` como equivalentes para otros proveedores. Verificar que la API exacta de estos métodos no haya cambiado en versiones recientes de las librerías.

6. **Laboratorio — disponibilidad de acceso a API:** El laboratorio requiere acceso activo a al menos una API de modelo de lenguaje. Para lectores sin acceso, se debería considerar una alternativa usando solo tiktoken localmente para el conteo (sin generación de respuestas). Esto podría documentarse como "Variante sin API" en v0.8.

7. **Fenómeno "lost in the middle" — añadir referencia:** El fenómeno se menciona en el Error 5 sin citar el paper original (Liu et al., 2023, "Lost in the Middle: How Language Models Use Long Contexts"). En v0.8 se recomienda agregar la referencia al pie o en una sección de bibliografía del capítulo.

---

## 5. Evaluación contra criterios de calidad del EDITORIAL_GUIDE

| Criterio | Estado |
|---|---|
| ¿Responde al problema planteado? | Sí — explica qué son los tokens, por qué importan y cómo gestionarlos en proyectos reales |
| ¿Tiene ejemplos? | Sí — BPE con corpus mínimo, tokenización de "La tokenización es fundamental", código Python |
| ¿Tiene un caso real? | Sí — empresa de servicios financieros con sistema RAG, estimación corregida ×16 |
| ¿Tiene laboratorio completo? | Sí — 5 pasos estructurados con objetivo, nivel, tiempo, prerrequisitos, herramientas, validación, reflexión y desafíos |
| ¿Tiene resumen? | Sí — sección 15 con resumen narrativo |
| ¿Existe continuidad con el capítulo anterior? | Parcial — no hay referencia explícita a Embeddings (pendiente para v0.8) |
| ¿Prepara correctamente el siguiente? | Sí — la sección "Próximo capítulo" presenta la ventana de contexto como el límite que rige a los tokens |
| ¿Forma mejores profesionales? | Sí — desarrolla criterio de estimación de costos, no memorización de precios |
| ¿Desarrolla criterio? | Sí — errores frecuentes, buenas prácticas, conversación con arquitecto y Paso 5 del laboratorio |
| ¿Podría seguir siendo útil dentro de cinco años? | Mayormente sí — BPE, diferencias por idioma y estructura de costos son conceptos estables; precios de API no lo son |
| ¿Explica el problema antes de la solución? | Sí — sección 3 ("por qué tokens y no palabras") antes de la sección 4 (desarrollo conceptual) |

---

## 6. Notas para el editor jefe

- **Extensión:** El capítulo supera la extensión habitual de la v0.5 (objetivo era ~4.000-5.000 palabras, resultado ~6.800 palabras). La extensión adicional está justificada: el caso empresarial con la comparación de estimaciones y el laboratorio de 5 pasos son los componentes que más espacio demandan, y también los de mayor valor práctico para el lector objetivo.

- **El laboratorio puede hacerse sin acceso a API:** Los Pasos 1, 2 y 5 son completamente locales (solo requieren tiktoken). El Paso 4 requiere API. Si el lector no tiene acceso a una API, puede completar los primeros tres pasos y el quinto y obtener el valor central del laboratorio (la auditoría de tokens y el cálculo del impacto económico).

- **La analogía del ancho de banda (Sección 5):** Se eligió esta analogía porque el público objetivo es profesional de tecnología, familiar con conceptos de redes. La analogía establece tres correspondencias exactas (ventana de contexto = buffer, prompt del sistema = overhead de protocolo, optimizar prompt = comprimir datos) que resultan inmediatamente intuitivas para ese perfil. Se evitó intencionalmente la analogía de "dinero/presupuesto" porque refuerza la noción de que los tokens son solo un problema de costos, cuando también son un límite de capacidad.

- **La conversación del arquitecto:** Los 5 intercambios están estructurados en escalada de diagnóstico: de síntoma (el modelo es caro) → causa superficial (prompts no medidos) → causa raíz (crecimiento orgánico del prompt) → problema adicional (historial sin gestión) → estrategias concretas. Este arco narrativo permite que el lector siga el proceso de razonamiento del arquitecto, no solo sus conclusiones.

- **Tabla de precios:** Se incluyó con la decisión editorial consciente de que puede quedar desactualizada. La alternativa (no incluir precios) hubiera hecho el capítulo menos accionable. La nota aclaratoria de "verificar documentación oficial" y el énfasis en los ratios (que son más estables que los precios absolutos) son los mecanismos para mitigar el riesgo de desactualización.
