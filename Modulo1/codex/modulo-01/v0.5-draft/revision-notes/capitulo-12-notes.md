---
capitulo: 12
titulo: "Mitos sobre la Inteligencia Artificial"
version: 0.5
tipo: notas-revision
fecha: 2026-06-28
revisor: Editor técnico y pedagógico
estado: Borrador revisión conceptual
---

# Notas de Revisión — Capítulo 12: Mitos sobre la Inteligencia Artificial

**Versión revisada:** 0.5 (desde v0.1)
**Fecha:** 2026-06-28

---

## 1. Resumen de cambios respecto de la v0.1

La versión 0.1 era un borrador funcional con cobertura conceptual correcta pero esquemática. Cubría siete mitos en una presentación lineal sin profundidad técnica, sin casos reales por mito, sin diagrama, sin glosario técnico y con un laboratorio de tres líneas. La v0.5 representa una expansión estructural y conceptual completa.

| Dimensión | v0.1 | v0.5 |
|---|---|---|
| Longitud estimada | ~600 palabras | ~7.500 palabras |
| Secciones | 10 básicas | 17 completas según estructura obligatoria |
| Cantidad de mitos | 7 | 10 |
| Diagramas Mermaid | 0 | 2 |
| Caso real por mito | 0 (ninguno) | 1 por cada mito (10 casos) |
| Análisis de alucinaciones | 1 párrafo | Sección dedicada: por qué ocurren, cómo detectarlas, estrategias de mitigación |
| Conversación con arquitecto | 2 intercambios (1 ronda) | 5 intercambios con profundidad técnica y de negocio |
| Errores frecuentes | Ausentes | 5 errores documentados |
| Buenas prácticas | 4 ítems en lista | 6 prácticas con justificación |
| Laboratorio | 3 líneas sin estructura | 4 pasos estructurados con objetivo, motivo, resultado esperado y validación |
| Glosario | Ausente | 9 términos con definición técnica precisa |
| Checklist | Ausente | 9 ítems verificables |

---

## 2. Decisiones editoriales tomadas

### 2.1 Ampliación de 7 a 10 mitos

La v0.1 cubría los siete mitos del brief original. La v0.5 incorpora los tres mitos adicionales solicitados en la especificación de expansión:

- **Mito 8 — "La IA es objetiva":** incorpora el concepto de sesgo (bias) desde los datos de entrenamiento, con el caso de Amazon (2014-2017) como evidencia documentada.
- **Mito 9 — "La IA puede razonar causalmente":** diferencia correlación estadística de razonamiento causal. El caso del algoritmo de salud publicado en *Science* (2019) ilustra las consecuencias de confundir ambos conceptos.
- **Mito 10 — "La IA tiene memoria entre sesiones por defecto":** explica la naturaleza stateless de los LLM y los mecanismos de ingeniería que implementan persistencia. El caso de la startup de RRHH ilustra las consecuencias de no diseñar la persistencia explícitamente.

### 2.2 Un caso real por mito (en lugar de uno general)

La v0.1 no tenía casos reales por mito. La especificación de expansión pedía "al menos un caso real donde creer en el mito causó un problema concreto". Se optó por incluir un caso por cada mito, con la misma estructura narrativa: contexto, lo que ocurrió, consecuencia. Esto hace el contenido más procesable y permite al lector relacionar cada mito con evidencia concreta.

Los casos seleccionados cubren dominios variados para reflejar la amplitud del problema:

| Mito | Caso | Dominio |
|---|---|---|
| 1 — Piensa como humano | Abogados NY / jurisprudencia inventada (2023) | Legal |
| 2 — Entiende todo | Telecomunicaciones / catálogo de productos | Telecomunicaciones |
| 3 — Aprende con conversaciones | Startup RRHH / asistente de entrevistas | Recursos Humanos |
| 4 — Más grande = mejor | Meta Llama 2 / 13B vs 70B (2023) | Investigación ML |
| 5 — Reemplaza todo el software | Aseguradora / pólizas no reproducibles | Seguros |
| 6 — Siempre conviene | E-commerce / LLM vs clasificador clásico | Comercio electrónico |
| 7 — Siempre dice verdad | Air Canada / chatbot y política de duelo (2024) | Aviación / Legal |
| 8 — Es objetiva | Amazon / sistema de contratación (2014-2017) | Tecnología / RRHH |
| 9 — Razona causalmente | Algoritmo de salud / *Science* (2019) | Salud |
| 10 — Tiene memoria | Startup / asistente de onboarding | Software |

### 2.3 Tratamiento en profundidad de la alucinación

La especificación pedía explicar el concepto en profundidad: por qué ocurre, cómo detectarla, estrategias de mitigación. Esto se implementó dentro del Mito 7 como subsecciones dedicadas:

- **Por qué ocurren:** explicación desde el mecanismo de generación de tokens. El modelo predice tokens estadísticamente probables, no factualmente correctos. No hay base de verdad externa durante la inferencia.
- **Cuándo son más frecuentes:** cuatro situaciones de alto riesgo (datos de entrenamiento insuficientes, hechos específicos, límite del corte de conocimiento, premisas incorrectas en el prompt).
- **Cómo detectarlas:** cinco señales prácticas (especificidad excesiva, inconsistencia interna, dominios de nicho, confianza sin fuentes).
- **Estrategias de mitigación:** cinco estrategias consolidadas (RAG, citación obligatoria, validación humana en el loop, evaluación automática, temperatura baja).

Esta profundidad es mayor que en cualquier otro mito porque la alucinación es el fenómeno técnico que más directamente diferencia a un LLM de una base de conocimiento confiable, y es el que más frecuentemente genera daño en aplicaciones profesionales.

### 2.4 Dos diagramas Mermaid con propósitos distintos

La especificación pedía un diagrama que mostrara la brecha entre percepción pública y realidad técnica. Se crearon dos:

- **Diagrama 1 (graph TB):** mapeo directo de los diez mitos a sus realidades técnicas correspondientes, con los subgraphs diferenciando visualmente percepción de realidad. Cumple el requisito de la especificación.
- **Diagrama 2 (sequenceDiagram):** anatomía del proceso de alucinación, mostrando la secuencia temporal de la inferencia y dónde en ese proceso se puede producir información incorrecta. Complementa la explicación técnica del Mito 7.

### 2.5 Laboratorio de "Auditoría de creencias"

La especificación pedía un laboratorio de "Auditoría de creencias" donde los lectores listan sus cinco creencias sobre IA y las evalúan con criterio técnico. El laboratorio de la v0.5 implementa eso en cuatro pasos:

- **Paso 1:** Inventario de creencias personales antes de cualquier evaluación (garantiza honestidad intelectual).
- **Paso 2:** Evaluación técnica estructurada con tabla de cinco dimensiones por creencia.
- **Paso 3:** Prueba práctica de alucinaciones con tres consultas diseñadas para producir resultados observables (alucinación, limitación factual, ausencia de memoria).
- **Paso 4:** Identificación de mitos en contexto organizacional (conexión con el entorno real del lector).

El diseño del Paso 3 es deliberado: las tres consultas no requieren ningún conocimiento técnico previo para ejecutarse, pero producen evidencia directa de tres propiedades distintas del LLM (alucinación, corte de conocimiento, stateless). Ver esos resultados es más efectivo pedagógicamente que leer una descripción.

### 2.6 Estructura de cada mito

Se estandarizó la estructura de cada mito en tres bloques: **El mito** (la afirmación y por qué se cree), **La realidad técnica** (explicación del mecanismo), **Consecuencia de creerlo** (impacto en decisiones de diseño), **Caso real** (evidencia concreta). Esta estructura permite al lector navegar el capítulo de forma no lineal: puede ir directamente al mito que le interesa y encontrar todo el análisis en un solo bloque.

---

## 3. Verificaciones de consistencia editorial

- [x] Terminología oficial: primera aparición de Inteligencia Artificial (IA), Large Language Model (LLM), Machine Learning (ML), Retrieval-Augmented Generation (RAG), fine-tuning, data drift, overfitting con nombre completo + sigla o nombre en español + término técnico.
- [x] Sin frases prohibidas: "La IA piensa", "La IA entiende", "La IA sabe" — no aparecen en el cuerpo del capítulo excepto dentro de las descripciones de los mitos (donde se usan para citar la creencia que se va a refutar).
- [x] Frase de cierre: presente al final del capítulo.
- [x] Continuidad con Capítulo 11: la introducción implica que el lector ya tiene conocimiento de los capítulos anteriores del módulo. La sección de Motivación asume familiaridad con los mecanismos de los LLM (predicción de tokens, entrenamiento).
- [x] Continuidad hacia Capítulo 13: la sección "Próximo capítulo" describe que el Capítulo 13 es integrador y hace referencia explícita a los conceptos del Módulo I en conjunto.
- [x] Diagramas en Mermaid: 2 diagramas (graph TB, sequenceDiagram).
- [x] Tono conversacional-técnico: sin lenguaje de marketing, sin frases vacías.
- [x] Casos reales con fuente identificable: todos los casos corresponden a eventos documentados públicamente o a escenarios hipotéticos con contexto suficiente para ser plausibles. Los que corresponden a eventos reales (Amazon, Air Canada, ProPublica/COMPAS, Meta Llama 2, Science 2019) tienen referencias implícitas que permiten su verificación.

---

## 4. Puntos abiertos para revisión técnica (v0.8)

Estos ítems no bloquean la v0.5 pero deben ser abordados en la siguiente revisión:

1. **Verificación de fechas en casos reales:** Las fechas del caso Amazon (2014-2017), el caso Air Canada (2024) y el estudio de *Science* (2019) deben verificarse contra fuentes primarias. Los datos incluidos en la v0.5 son consistentes con la documentación pública disponible al momento de la redacción, pero deben validarse editorialmente.

2. **Referencia explícita al paper de COMPAS (ProPublica):** El caso del sistema judicial (Mito 8 / caso real en sección 8) se basa en el análisis de ProPublica sobre el sistema COMPAS. En la v0.8 se recomienda incluir la referencia completa: Angwin, J. et al. (2016). "Machine Bias". ProPublica.

3. **Referencia al paper de Science (2019):** El estudio del algoritmo de salud (Mito 9) corresponde a: Obermeyer, Z. et al. (2019). "Dissecting racial bias in an algorithm used to manage the health of populations." *Science*, 366(6464), 447-453. Incluir en bibliografía de la v0.8.

4. **Caso del tribunal de Nueva York:** El caso de los abogados (Mito 1) corresponde al caso Mata v. Avianca (SDNY, 2023), juez P. Kevin Castel. Verificar y citar correctamente.

5. **Caso Air Canada:** Corresponde al fallo del Tribunal de Resolución Civil de la Columbia Británica (Canada). Verificar número de expediente y fecha exacta del fallo.

6. **Ampliación del glosario con AGI:** El término Inteligencia Artificial General (AGI) aparece en el glosario pero no tiene desarrollo en el cuerpo del capítulo. En la v0.8 se puede incluir una nota sobre por qué los sistemas actuales no califican como AGI, en el contexto del Mito 1.

7. **Diagrama 1 — validación de renderizado:** El diagrama de brecha percepción/realidad usa subgraphs con espacios en los nombres. Validar compatibilidad con el renderizador Mermaid del pipeline de publicación.

---

## 5. Evaluación contra criterios de calidad del EDITORIAL_GUIDE

| Criterio | Estado |
|---|---|
| ¿Responde al problema planteado? | Sí — cada mito está planteado como problema y refutado con argumento técnico |
| ¿Tiene ejemplos? | Sí — un caso real por mito, más los ejemplos del laboratorio |
| ¿Tiene un caso real? | Sí — sección 8 con caso integrador del sistema judicial (COMPAS) |
| ¿Tiene laboratorio completo? | Sí — 4 pasos estructurados con validación |
| ¿Tiene resumen? | Sí — sección 14 |
| ¿Existe continuidad con el capítulo anterior? | Sí — la introducción y motivación asumen el conocimiento del Módulo I |
| ¿Prepara correctamente el siguiente? | Sí — introduce que el Capítulo 13 es integrador de todo el módulo |
| ¿Forma mejores profesionales? | Sí — el foco está en criterio de decisión, no en memorización de mitos |
| ¿Desarrolla criterio? | Sí — errores frecuentes, buenas prácticas y laboratorio orientados a criterio |
| ¿Podría seguir siendo útil dentro de cinco años? | Sí — los mitos son estructurales al funcionamiento de los LLM, no a herramientas específicas |
| ¿Explica el problema antes de la solución? | Sí — cada mito comienza por la creencia y su origen antes de la refutación |

---

## 6. Notas para el editor jefe

- El capítulo tiene una longitud mayor que la mayoría de los capítulos del módulo. Esto es intencional: diez mitos con caso real cada uno, más el análisis en profundidad de la alucinación, requieren espacio. La alternativa de comprimirlos produciría exactamente el efecto contrario al objetivo del capítulo: afirmaciones vagas sin sustento técnico.

- Se decidió no incluir código fuente en este capítulo. El Capítulo 12 es conceptual por diseño: su objetivo es calibrar expectativas y desarrollar criterio técnico, no enseñar implementación. El laboratorio usa herramientas de LLM en modo conversacional, lo que es accesible para todo el público objetivo sin instalar nada.

- El Mito 9 (razonamiento causal) es el más técnico de los diez. El lector sin formación en estadística puede encontrarlo más denso. Se evaluará en la v0.8 si conviene agregar una nota explicativa sobre correlación vs. causalidad que lo haga más accesible sin perder precisión.

- La analogía del consultor (sección 5) fue elegida deliberadamente para reemplazar analogías que tienden a humanizar el sistema ("la IA como asistente inteligente"). La figura del consultor con capacidades específicas y limitaciones igualmente específicas captura mejor la utilidad real del LLM sin antropomorfizarlo.

- El laboratorio del Paso 3 (prueba práctica de alucinaciones) produce resultados observables que varían según el modelo y la sesión específica. La instrucción está diseñada para que los resultados sean informativos incluso si el modelo no alucina en la Consulta 2: si el modelo responde correctamente que no puede encontrar el informe, eso también es un resultado pedagógico (muestra que algunos modelos tienen mejores mecanismos de abstención). Se recomienda que el lector documente el nombre y versión del modelo que usó para facilitar la comparación.
