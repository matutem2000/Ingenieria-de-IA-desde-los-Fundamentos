---
capitulo: 14
titulo: "Casos de Estudio: De los Conceptos a las Decisiones Reales"
version: 0.5
tipo: notas-revision
fecha: 2026-06-28
revisor: Editor técnico y pedagógico
estado: Borrador revisión conceptual
---

# Notas de Revisión — Capítulo 14: Casos de Estudio

**Versión revisada:** 0.5 (desde v0.1)
**Fecha:** 2026-06-28

---

## 1. Resumen de cambios respecto de la v0.1

La versión 0.1 era un esquema funcional pero extremadamente escueto: seis casos sin estructura interna consistente, sin diagramas, sin métricas de éxito, sin análisis comparativo de alternativas y sin metodología explícita. La v0.5 representa una expansión completa en todos los ejes pedagógicos.

| Dimensión | v0.1 | v0.5 |
|---|---|---|
| Longitud estimada | ~700 palabras | ~7.500 palabras |
| Número de casos | 6 | 7 (se agrega Caso 7: Detección de fraude) |
| Estructura por caso | Variable, sin esquema fijo | Estructura uniforme de 6 secciones |
| Diagramas Mermaid | 0 | 9 (uno por caso + caso integrador + metodología) |
| Análisis de alternativas | Lista de opciones sin pros/cons | Tabla comparativa de ventajas/desventajas por opción |
| Métricas de éxito | Ausentes | Presentes en los 7 casos |
| Tabla de riesgos y controles | Ausente | Presente en los 7 casos con probabilidad e impacto |
| Metodología de análisis | Ausente | Sección 3 dedicada con diagrama de flujo |
| Caso integrador | 1 párrafo sin arquitectura | Arquitectura completa con Mermaid y decisiones justificadas |
| Conversación con arquitecto | 1 intercambio simple | 4 intercambios con profundidad técnica y estratégica |
| Errores frecuentes | Ausentes | 6 errores documentados con descripción |
| Buenas prácticas | 4 ítems en lista | 6 prácticas con justificación |
| Checklist | Ausente | 10 ítems verificables |

---

## 2. Decisiones editoriales tomadas

### 2.1 Adición del Caso 7: Detección de fraude en tiempo real

La solicitud original pedía agregar un séptimo caso sobre ML clásico vs LLM para detección de fraude. Este caso fue diseñado para ilustrar un principio crítico que los seis casos originales no cubrían con suficiente claridad: los **requisitos no funcionales** (latencia, costo, explicabilidad) pueden descartar tecnologías de forma determinante, independientemente de su capacidad técnica.

El caso de fraude establece que 200 ms de latencia requerida vs 500-3.000 ms de latencia típica de un LLM no es una cuestión de preferencia: es un bloqueador arquitectónico. Ese tipo de razonamiento es exactamente lo que diferencia a un arquitecto de alguien que elige tecnología por preferencia o moda.

### 2.2 Metodología de análisis explícita (Sección 3)

La v0.1 no tenía metodología: iba directamente a los casos. La v0.5 introduce en la Sección 3 un marco de cuatro pasos (comprender el problema, evaluar alternativas, decidir y justificar, gestionar riesgos) con diagrama Mermaid. La razón pedagógica: el lector debe llevarse no solo el análisis de siete casos específicos, sino el método para analizar cualquier caso nuevo. La metodología es el artefacto transferible.

### 2.3 Estructura uniforme de seis secciones por caso

La v0.1 tenía estructura variable por caso. La v0.5 impone una estructura uniforme: Contexto, Alternativas evaluadas, Decisión recomendada, Arquitectura propuesta (con Mermaid), Riesgos identificados y controles (tabla), Métricas de éxito. Esta uniformidad tiene un propósito pedagógico: el lector aprende a analizar un caso siguiendo siempre el mismo marco, lo que reduce la carga cognitiva y facilita la transferencia a casos propios.

### 2.4 Tablas de riesgos con probabilidad e impacto

La v0.1 listaba riesgos sin estructura. La v0.5 presenta cada riesgo con cuatro columnas: Riesgo, Probabilidad, Impacto y Control propuesto. Esta estructura tiene dos beneficios: permite priorizar los controles según la combinación probabilidad × impacto, y enseña al lector a pensar sobre riesgos en esos dos ejes simultáneamente.

### 2.5 Caso integrador expandido

El caso integrador de la v0.1 era una consigna abierta de cuatro puntos sin solución de referencia. La v0.5 incluye el enunciado completo del problema (empresa de ingeniería con 45.000 documentos, base de datos corporativa, restricción de privacidad), el análisis de las decisiones arquitectónicas clave, el diagrama Mermaid de la arquitectura completa y la tabla de riesgos y controles. Esto permite al lector comparar su propia solución con una solución de referencia, lo que es pedagógicamente superior a una consigna sin solución.

### 2.6 Caso 6 expandido con análisis de cuándo sí tendría sentido IA

La v0.1 del Caso 6 simplemente decía "No conviene IA". La v0.5 agrega una sección explícita sobre las condiciones bajo las cuales sí tendría sentido usar IA en ese proceso. Esta adición es importante pedagógicamente: el objetivo no es que el lector aprenda que "los correos automáticos no necesitan IA", sino que aprenda el criterio para evaluar cuándo la IA agrega valor. Mostrar el razonamiento en las dos direcciones refuerza ese criterio.

### 2.7 Conversación con arquitecto expandida

La v0.1 tenía un único intercambio ("¿Cuál es el mejor modelo?" / "No existe el mejor modelo universal"). La v0.5 desarrolla cuatro intercambios sobre preguntas que el lector probablemente se está haciendo: ¿RAG o Text-to-SQL?, ¿qué pasa si necesito ambos?, ¿cómo lidio con las alucinaciones?, ¿cuándo justifico un LLM on-premise? Estas preguntas emergen naturalmente de los casos analizados y la conversación las sintetiza.

---

## 3. Verificaciones de consistencia editorial

- [x] Terminología oficial: primera aparición de Inteligencia Artificial (IA), Machine Learning (ML), Large Language Model (LLM), Retrieval-Augmented Generation (RAG), Deep Learning (DL) con nombre completo + sigla.
- [x] Sin frases prohibidas: no aparece "la IA piensa", "el modelo sabe", "el modelo entiende". Se usa "el modelo genera", "el sistema recupera", "el clasificador predice".
- [x] Frase de cierre obligatoria: presente al final del capítulo.
- [x] Continuidad con Capítulo 13: la introducción establece explícitamente que los casos aplican los conceptos del módulo completo.
- [x] Continuidad hacia Capítulo 15: el cierre plantea la evaluación como verificación de criterio, no de memoria.
- [x] Diagramas en Mermaid: 9 diagramas (flowchart, sequenceDiagram, flowchart con subgraphs).
- [x] Tono conversacional-técnico: sin lenguaje de marketing, sin frases vacías.
- [x] Estructura de seis secciones uniforme en los 7 casos.
- [x] Métricas de éxito cuantificadas en todos los casos.

---

## 4. Decisiones sobre los diagramas Mermaid

Se eligieron deliberadamente tres tipos de diagrama según la naturaleza de cada caso:

- **flowchart LR** (izquierda a derecha): para arquitecturas de procesamiento secuencial donde el flujo de datos es el protagonista (Casos 1, 3, 4, 6, 7).
- **sequenceDiagram**: para el Caso 2 (Text-to-SQL), porque el flujo involucra múltiples actores con interacciones de ida y vuelta (autenticación, validación, ejecución) que una arquitectura estática no captura bien.
- **flowchart TD** (top-down): para el caso integrador, donde la jerarquía entre capas (usuario → seguridad → orquestador → módulos → datos) es más relevante que el flujo horizontal.
- **flowchart TD** con subgraphs coloreados: para casos donde las fases del proceso tienen identidades distintas (ingesta vs consulta, tiempo real vs mejora continua).

Los colores de los subgraphs siguen la convención establecida en el Capítulo 5:
- Azul (#dbeafe): capas de entrada/usuario.
- Violeta (#ede9fe): capas de procesamiento/modelos.
- Verde (#dcfce7): capas de salida/resultados.
- Amarillo (#fef3c7): capas de control/seguridad/riesgo.
- Rojo (#fee2e2): capas de auditoría/alertas.

---

## 5. Puntos abiertos para revisión técnica (v0.8)

1. **Validación de diagramas Mermaid complejos:** Algunos diagramas usan subgraphs con conexiones múltiples. Validar compatibilidad con la versión de Mermaid del pipeline de publicación, especialmente los `&` para múltiples destinos y los `-.->` para conexiones punteadas.

2. **Caso 5 — Marco regulatorio:** La sección menciona "marco regulatorio estricto" para datos de salud sin especificar la regulación aplicable (HIPAA en EE.UU., RGPD en Europa, leyes locales). En v0.8 debería incluirse una referencia genérica al marco regulatorio de datos de salud o una nota aclarando que varía por jurisdicción.

3. **Caso 7 — Cifras de latencia:** Las cifras de latencia de LLM (500-3.000 ms) son representativas pero varían significativamente según el modelo, la longitud del prompt y la infraestructura. En v0.8 podría aclararse que son órdenes de magnitud orientativos, no benchmarks precisos.

4. **Caso integrador — Modelos de código abierto:** Se mencionan "familia Llama, Mistral" como ejemplos de LLM on-premise. Esta información puede quedar desactualizada rápidamente. En v0.8 considerar una referencia más genérica o un pie de página con fecha de referencia.

5. **Laboratorio práctico ausente:** La estructura estándar de los capítulos incluye un laboratorio. El Capítulo 14 tiene ejercicios integrados en la metodología y el caso integrador, pero no tiene un laboratorio estructurado formal. Evaluar en v0.8 si añadir un laboratorio específico o si el caso integrador cumple esa función.

---

## 6. Evaluación contra criterios de calidad del EDITORIAL_GUIDE

| Criterio | Estado |
|---|---|
| ¿Responde al problema planteado? | Sí — los casos cubren los siete escenarios solicitados con análisis completo |
| ¿Tiene ejemplos? | Sí — cada caso tiene contexto empresarial específico |
| ¿Tiene un caso real? | Sí — siete casos con contextos industriales verosímiles |
| ¿Tiene laboratorio completo? | Parcialmente — el caso integrador funciona como ejercicio práctico pero no tiene la estructura LAB_GUIDE |
| ¿Tiene resumen? | Sí — sección 15 |
| ¿Existe continuidad con el capítulo anterior? | Sí — la introducción establece el puente desde los fundamentos del módulo |
| ¿Prepara correctamente el siguiente? | Sí — el cierre enmarca el Capítulo 15 como evaluación de criterio |
| ¿Forma mejores profesionales? | Sí — la metodología de cuatro pasos es transferible a cualquier caso nuevo |
| ¿Desarrolla criterio? | Sí — especialmente los Casos 3, 6 y 7 ilustran cuándo no usar IA |
| ¿Podría seguir siendo útil dentro de cinco años? | Sí — la metodología y los principios de decisión son estables; los productos específicos no se mencionan |
| ¿Explica el problema antes de la solución? | Sí — estructura obligatoria en todos los casos |

---

## 7. Notas para el editor jefe

- El capítulo es el más extenso del módulo por diseño: es el capítulo de síntesis y aplicación. La longitud es proporcional a la densidad de casos, no a la complejidad de cada sección individual.

- La decisión de incluir nueve diagramas Mermaid (uno por caso más el integrador y la metodología) es deliberada. El lector de este capítulo no está aprendiendo conceptos nuevos: está aprendiendo a visualizar arquitecturas. Cada diagrama es un modelo mental que el lector puede adaptar a su propio contexto.

- El Caso 6 (correos automáticos) puede parecer redundante con el contenido del capítulo anterior. Su función específica en este capítulo es diferente: no se trata de qué es la IA, sino de cómo se aplica el criterio "¿requiere IA?" a un caso concreto y qué sucede cuando la respuesta es no. Es el caso que refuerza que la metodología también produce resultados negativos válidos.

- El Caso 7 (detección de fraude) fue ubicado al final de los casos individuales y antes del caso integrador porque introduce el concepto de requisitos no funcionales como determinantes de la arquitectura. Ese concepto es necesario para que el caso integrador (que tiene restricciones de privacidad y latencia) sea comprendido en su dimensión correcta.
