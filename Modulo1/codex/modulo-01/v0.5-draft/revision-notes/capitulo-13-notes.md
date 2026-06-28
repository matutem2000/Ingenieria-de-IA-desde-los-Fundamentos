---
documento: Notas de revisión — Capítulo 13 v0.5
capitulo: 13 — Laboratorios del Módulo I
version_origen: v0.1
version_destino: v0.5
fecha: 2026-06-28
tipo: Revisión editorial completa
---

# Notas de revisión — Capítulo 13

## Resumen ejecutivo

La versión v0.5 del Capítulo 13 constituye una reescritura completa respecto a v0.1. La estructura pasó de 8 secciones sin andamiaje pedagógico a 18 apartados organizados según la estructura obligatoria del proyecto. Se incorporó un noveno laboratorio (evaluación de alucinaciones), plantillas de registro de observaciones para todos los laboratorios, vinculación explícita de cada laboratorio a su capítulo teórico de referencia, y una autoevaluación de competencias expandida con escala 1-5 y descriptores de nivel.

---

## Diferencias respecto a v0.1

### Lo que se conservó de v0.1

- Los ocho laboratorios originales (Comparando modelos, Temperatura, Tokens, Contexto, Embeddings conceptual, ¿Necesita IA?, Arquitectura, Pensar como arquitecto).
- El desafío integrador final.
- El checklist del Módulo I (10 preguntas).
- La frase editorial de cierre.
- El enfoque de criterio profesional sobre memorización de respuestas.

### Lo que se amplió

| Elemento | v0.1 | v0.5 |
|---|---|---|
| Estructura | 8 secciones sin encabezado de metadata | 18 apartados con metadata YAML, sección de metodología, introducción narrativa y sección de próximo módulo |
| Laboratorio 1 | 6 dimensiones de comparación listadas, sin pasos estructurados | 5 pasos detallados con justificación, plantilla de registro de observaciones con 9 dimensiones calificadas |
| Laboratorio 2 | 4 preguntas sin pasos | 4 pasos detallados con dos prompts de prueba diferenciados, tabla de registro por temperatura y ejecución |
| Laboratorio 3 | 4 preguntas de comparación sin escenario | 5 pasos con escenario real, tabla comparativa y cálculo de ahorro proyectado |
| Laboratorio 4 | 3 estrategias mencionadas sin estructura | 4 pasos con escenario de onboarding, tabla de seguimiento de degradación por turno |
| Laboratorio 5 | Ejemplo de 5 variantes sin análisis de keyword | 5 pasos con tabla de análisis de coincidencia keyword vs. semántica y cierre con caso de negocio |
| Laboratorio 6 | 4 preguntas de evaluación sin framework | Framework estructurado de 4 preguntas con tabla de análisis y clasificación de casos |
| Laboratorio 7 | Lista de componentes posibles, sin pasos ni diagrama | 5 pasos con diagrama Mermaid de arquitectura, tabla de justificación de decisiones y análisis de riesgos |
| Laboratorio 8 | 4 casos sin estructura de análisis | Tabla de análisis para cada caso con 4 dimensiones: validez, error de razonamiento, pregunta de retorno, respuesta redactada |
| Laboratorio 9 | Ausente en v0.1 | Laboratorio completo: 5 pasos, 10 preguntas verificables, 3 preguntas trampa, tabla de evaluación y propuesta de mitigación |
| Checklist | 10 ítems en lista | 10 ítems con referencia explícita al capítulo de origen |
| Autoevaluación | Ausente en v0.1 | Escala 1-5 con 7 competencias, descriptores de nivel por competencia y tabla de interpretación de resultados |
| Vinculación teórica | Ausente | Cada laboratorio indica el capítulo teórico de referencia |
| Diagrama overview | Ausente | Diagrama Mermaid de flujo laboratorios → Módulo II |
| Próximo módulo | 2 líneas de texto | Sección completa con anticipación de contenido del Módulo II |

---

## Decisiones editoriales tomadas en v0.5

### 1. Incorporación del Laboratorio 9 — Evaluación de alucinaciones

**Decisión:** Agregar un noveno laboratorio dedicado específicamente a identificar alucinaciones y distinguir entre confianza aparente y corrección real.

**Justificación:** La v0.1 incluía alucinaciones en el checklist conceptual pero no las trabajaba en modo práctico. Las alucinaciones son uno de los problemas más críticos de los LLMs en producción y uno de los más difíciles de internalizar sin experimentación directa. El laboratorio está diseñado para producir una experiencia concreta de este fenómeno, no solo su comprensión abstracta.

**Posición en la secuencia:** El Lab 9 se coloca al final de los laboratorios porque requiere las competencias desarrolladas en los anteriores (capacidad de comparar modelos, criterio sobre confianza vs. corrección, pensamiento arquitectónico sobre validación).

---

### 2. Plantillas de registro de observaciones en todos los laboratorios

**Decisión:** Incluir una tabla de registro estructurada en cada laboratorio.

**Justificación:** La v0.1 indicaba que el lector debía "registrar observaciones" pero no proporcionaba ningún andamiaje para hacerlo. Sin estructura de registro, la observación tiende a ser vaga y no acumulable. Las tablas cumplen dos funciones: guiar la atención hacia las dimensiones relevantes y producir un documento que el lector puede revisar después. Esto es consistente con la metodología del LAB_GUIDE: resultado verificable y preguntas de reflexión posteriores al registro.

---

### 3. Vinculación explícita de cada laboratorio a su capítulo teórico

**Decisión:** Cada laboratorio indica en su encabezado el capítulo o capítulos del libro de los que proviene.

**Justificación:** El Capítulo 13 es el capítulo de cierre práctico del Módulo I. Su utilidad depende de que el lector pueda volver a la teoría cuando una pregunta de reflexión no tiene respuesta. Sin la referencia al capítulo, esa navegación es lenta e ineficiente. La vinculación convierte el capítulo de laboratorios en un índice activo del módulo.

---

### 4. Autoevaluación expandida con descriptores de nivel

**Decisión:** Reemplazar la autoevaluación implícita del checklist por una matriz de competencias con escala 1-5 y descriptores específicos por nivel.

**Justificación:** El checklist de 10 preguntas de v0.1 es útil pero binario: el lector sabe o no sabe. La escala 1-5 permite distinguir entre comprensión conceptual, capacidad de aplicación y capacidad de síntesis. Esa distinción es crucial para un libro dirigido a profesionales: muchos pueden definir correctamente un token pero no pueden diseñar una estrategia de gestión de contexto para producción. Los descriptores de nivel hacen explícita esa diferencia.

---

### 5. Sección de metodología separada de recomendaciones generales

**Decisión:** Separar "Cómo sacar el máximo provecho" (metodología) de "Antes de comenzar" (recomendaciones generales) como dos secciones distintas.

**Justificación:** En v0.1 ambas ideas estaban mezcladas en un mismo bloque. La metodología responde a "cómo abordar el proceso" (registrar todo, no buscar respuesta correcta, trabajar con dos modelos). Las recomendaciones responden a "qué tener listo antes de empezar" (herramientas, documento de notas, actitud). Separarlas mejora la legibilidad y permite que el lector encuentre cada tipo de información sin leer el bloque completo.

---

### 6. Escenario profesional en cada laboratorio

**Decisión:** Cada laboratorio tiene un escenario que sitúa al lector en un rol y contexto específico.

**Justificación:** El LAB_GUIDE indica que el escenario debe presentar un problema concreto antes de la tecnología. En v0.1 los laboratorios comenzaban directamente con la actividad. Los escenarios en v0.5 cumplen tres funciones: establecen el "para qué" del ejercicio, conectan la práctica con situaciones reales y generan motivación intrínseca al hacer que el lector se identifique con el problema.

---

## Verificación de cumplimiento editorial

| Criterio | Estado |
|---|---|
| Estructura de 17 secciones obligatorias | Cumplido — 18 secciones (se agregó Lab 9 como sección adicional) |
| Encabezado de metadata YAML | Cumplido |
| Objetivos del capítulo con verbos medibles | Cumplido — 7 objetivos con verbos: aplicar, comparar, evaluar, diseñar, reconocer, desarrollar, identificar |
| Introducción narrativa con propósito de los laboratorios | Cumplido |
| Sección de metodología | Cumplido — con diagrama Mermaid de flujo |
| Recomendaciones generales | Cumplido — con diagrama Mermaid complementario |
| 9 laboratorios completos (8 + Lab 9 agregado) | Cumplido |
| Cada laboratorio con: Objetivo, Nivel, Tiempo, Herramientas, Escenario, Pasos (≥4), Validación, Reflexión, Desafíos | Cumplido en todos los laboratorios |
| Plantilla de registro en cada laboratorio | Cumplido |
| Vinculación de cada laboratorio a capítulo teórico | Cumplido |
| Diagramas Mermaid | Cumplido — 3 diagramas: overview de flujo, metodología de comparación, arquitectura de referencia en Lab 7 |
| Desafío integrador final con 6 preguntas | Cumplido |
| Checklist del Módulo I con referencia a capítulos | Cumplido — 10 ítems con capítulo de referencia |
| Autoevaluación de competencias con escala 1-5 | Cumplido — 7 competencias con descriptores y tabla de interpretación |
| Sección de próximo módulo | Cumplido |
| Terminología oficial con siglas en primera aparición | Cumplido — IA, LLM, ML, DL, RAG |
| Tono profesional-conversacional | Cumplido |
| Frase editorial de cierre | Cumplido |
| Sin terminología prohibida | Cumplido — revisado |

---

## Métricas de la revisión

| Métrica | v0.1 | v0.5 |
|---|---|---|
| Palabras aproximadas | ~900 | ~8.200 |
| Secciones | 8 | 18 |
| Laboratorios | 8 | 9 |
| Pasos promedio por laboratorio | Sin estructura | 4 a 5 pasos con justificación |
| Tablas de registro | 0 | 9 (una por laboratorio) |
| Diagramas Mermaid | 0 | 3 |
| Vinculación a capítulos teóricos | 0 | Todos los laboratorios |
| Ítems en autoevaluación | 0 | 7 competencias × 5 niveles = 35 descriptores |
| Desafíos opcionales | 0 | 3 por laboratorio = 27 desafíos opcionales |

---

## Observaciones para la revisión técnica (v0.8)

Las siguientes áreas deberán ser verificadas en la revisión técnica antes de avanzar a v0.8:

1. **Herramientas disponibles:** Verificar que todas las herramientas mencionadas (Ollama, Playground de OpenAI, tokenizer de OpenAI) sigan siendo accesibles y gratuitas o de costo razonable para el lector promedio. Las URLs y las disponibilidades pueden cambiar.

2. **Preguntas del Lab 9:** Las diez preguntas de evaluación de alucinaciones deben tener respuestas verificables y estables. Preguntas sobre conteo de parámetros de modelos específicos o características de versiones pueden quedar desactualizadas. Evaluar si conviene reemplazarlas por preguntas sobre hechos históricos más estables.

3. **Costos en Lab 3:** El cálculo de costo proyectado depende de precios de API que cambian frecuentemente. Evaluar si conviene expresar el cálculo como fórmula genérica (costo = N_tokens × precio_por_token × consultas_diarias × 30) en lugar de valores específicos.

4. **Coherencia con capítulos de referencia:** Verificar que los capítulos indicados como referencia (Cap. 2, 5, 6, 8, 9, 10, 11, 12) existan y cubran efectivamente el contenido al que se hace referencia. Si algún capítulo aún no está en v0.5, actualizar la referencia cuando esté disponible.

5. **Lab 7 — Diagrama Mermaid de arquitectura:** El diagrama incluido es genérico. Evaluar si conviene agregar diagramas específicos para cada una de las cuatro opciones de caso (Opción A a D) en v0.8.

6. **Autoevaluación — calibración de niveles:** Los descriptores de nivel de la autoevaluación deberían ser revisados por al menos un lector de perfil objetivo para verificar que la escala sea intuitiva y que los niveles estén correctamente diferenciados entre sí.

7. **Lab 9 — Preguntas trampa:** Las tres preguntas trampa incluyen referencias a eventos futuros o combinaciones erróneas de marca/producto. Verificar que sean suficientemente verosímiles para ser confundidas por el modelo pero verificablemente falsas para el lector.

---

## Alineación con otros capítulos del Módulo I

| Capítulo | Concepto trabajado en Cap. 13 | Laboratorio que lo ejercita |
|---|---|---|
| Cap. 2 — Qué es un LLM | Comparación de comportamiento entre modelos | Lab 1 |
| Cap. 3 — Transformers | Arquitectura subyacente a los modelos comparados | Lab 1 (contexto) |
| Cap. 4 — Machine Learning | Diferencia entre sistemas de reglas y ML | Lab 6 |
| Cap. 5 — Tokens y contexto | Gestión de tokens, ventana de contexto | Labs 3 y 4 |
| Cap. 6 — Alucinaciones | Identificación y mitigación de alucinaciones | Lab 9 |
| Cap. 7 — Modelos disponibles | Criterios de selección de modelo | Labs 1 y 7 |
| Cap. 8 — Temperatura y sampling | Efecto de la temperatura sobre la generación | Lab 2 |
| Cap. 9 — Memoria y contexto | Estrategias de gestión de contexto largo | Lab 4 |
| Cap. 10 — Embeddings | Búsqueda semántica vs. keyword | Lab 5 |
| Cap. 11 — Cuándo usar IA | Criterio de adopción y evaluación de casos | Labs 6 y 8 |
| Cap. 12 — Arquitecturas aplicadas | Diseño de arquitectura conceptual | Labs 7 y Desafío final |

---

## Estado del archivo

- Archivo principal: `/book/modulo-01/v0.5-draft/capitulo-13.md`
- Notas de revisión: `/Modulo1/code/v0.5-draft/revision-notes/capitulo-13-notes.md`
- Próxima revisión esperada: v0.8 (revisión técnica y calibración de autoevaluación)
- Pendiente: verificar coherencia con v0.5 de los capítulos 6, 9 y 11 cuando estén disponibles.

---

## Actualización complementaria — 2026-06-28

Se agregaron secciones explícitas para alinear el capítulo con la estructura editorial obligatoria del Módulo I:

- Analogía transversal.
- Conversación con un arquitecto.
- Errores frecuentes en los laboratorios.
- Buenas prácticas para ejecutar los laboratorios.
- Preguntas de reflexión.
- Resumen.
- Glosario breve.

El contenido agregado mantiene el enfoque del capítulo como instancia práctica y refuerza que los laboratorios buscan desarrollar criterio profesional, no solo completar ejercicios.
