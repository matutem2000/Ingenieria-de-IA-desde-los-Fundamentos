---
documento: Notas de revisión — Capítulo 3 v0.5
capitulo: 3 — Historia de la Inteligencia Artificial
version_origen: v0.1
version_destino: v0.5
fecha: 2026-06-28
tipo: Revisión conceptual
---

# Notas de revisión — Capítulo 3

## Resumen ejecutivo

La versión v0.5 del Capítulo 3 constituye una reescritura completa con profundidad sustancialmente mayor respecto a v0.1. La estructura se expandió de 9 secciones a 17 apartados obligatorios, el contenido de cada etapa histórica pasó de ser descriptivo a ser analítico (patrón problema → solución → límite), y se incorporaron todos los componentes faltantes: laboratorio estructurado, diálogo extendido, glosario, checklist, errores frecuentes y buenas prácticas.

---

## Diferencias respecto a v0.1

### Lo que se conservó de v0.1

- El enfoque narrativo de la historia como sucesión de problemas (no como lista de fechas).
- Las etapas principales: pre-computación, Dartmouth 1956, ML, DL, Transformer, LLM.
- La idea central de los inviernos como períodos de retracción por expectativas desmedidas.
- La frase editorial de cierre.
- El concepto del diálogo con el arquitecto.

### Lo que se amplió

| Elemento | v0.1 | v0.5 |
|----------|------|------|
| Estructura | 9 secciones sin numeración formal | 17 apartados según estructura obligatoria |
| Etapas históricas | Descripción de 1-2 oraciones por etapa | Análisis completo: problema, solución, límite por etapa |
| Inviernos de la IA | Mencionados en un párrafo | Desarrollados como dos eventos separados con contexto, causas y lecciones |
| Diálogo arquitecto | 2 turnos, 3 oraciones totales | 5 turnos con argumentación técnica extendida |
| Laboratorio | Ejercicio de 4 líneas | Laboratorio completo con objetivo, nivel, tiempo, pasos, validación, reflexión y desafíos opcionales |
| Diagrama | Ausente | Diagrama Mermaid timeline con todas las etapas y ciclos |
| Errores frecuentes | Ausente | 5 errores con descripción y consecuencias prácticas |
| Buenas prácticas | Implícitas | 6 buenas prácticas accionables y numeradas |
| Analogía | Ausente | Analogía cohete Falcon 9 — explicita la estructura causal |
| Glosario | Ausente | 8 términos con definiciones técnicas precisas |
| Checklist | Ausente | 7 ítems verificables |
| Preguntas de reflexión | Ausente | 7 preguntas que desarrollan criterio |
| Motivación del problema | Ausente | Apartado completo justificando el estudio de la historia |

---

## Decisiones editoriales tomadas en v0.5

### 1. Subdivisión de los inviernos en dos eventos separados

**Decisión:** Separar el primer invierno (1974–1980) del segundo (1987–1993) como etapas distintas con sus propios ciclos problema → solución → límite.

**Justificación:** La v0.1 los agrupaba como un único período, lo que ocultaba que tuvieron causas distintas. El primer invierno fue consecuencia del Informe Lighthill y la reducción de DARPA. El segundo fue consecuencia del colapso del mercado de hardware Lisp y del fracaso de los sistemas expertos en producción. Separar los eventos permite extraer lecciones más específicas y aplicables.

### 2. Inclusión del período de sistemas expertos como etapa propia

**Decisión:** Dedicar un análisis específico a los sistemas expertos entre ambos inviernos.

**Justificación:** Los sistemas expertos representan una solución real a un problema real, no solo un período de transición. Su fracaso tiene causas técnicas precisas (costo de mantenimiento, falta de generalización) que son directamente análogas a limitaciones actuales de los LLMs en ciertos contextos. Incluirlos fortalece la lección histórica.

### 3. Analogía del cohete Falcon 9

**Decisión:** Usar el aterrizaje del Falcon 9 (2015) como analogía del momento LLM.

**Justificación:** La analogía cumple los criterios del STYLE_GUIDE: es breve, aclara sin simplificar en exceso, y no reemplaza la explicación técnica. Además es específica (tiene fecha, tiene nombre, tiene historia verificable), lo que la hace más efectiva pedagógicamente que una analogía genérica.

### 4. Diálogo extendido a 5 turnos

**Decisión:** Expandir el diálogo de 2 turnos a 5, con un Director de Tecnología como interlocutor.

**Justificación:** El diálogo original (v0.1) tenía un único intercambio que no desarrollaba argumentación. En v0.5 el diálogo muestra el razonamiento técnico del arquitecto en situaciones de presión organizacional, que es el contexto real en que este libro será aplicado. Los 5 intercambios permiten desplegar la lógica completa: por qué importa el problema, por qué los límites son relevantes, cuándo conviene avanzar y cuándo no.

### 5. Laboratorio sin código

**Decisión:** Diseñar el laboratorio como un ejercicio de análisis y escritura, sin código.

**Justificación:** El Capítulo 3 es histórico y conceptual. Introducir código en este punto sería incongruente con el contenido y desalinearía con la progresión pedagógica del libro (el código aparece en capítulos posteriores). El laboratorio analítico cumple los criterios del LAB_GUIDE: tiene objetivo, nivel, pasos estructurados, validación y reflexión.

---

## Verificación de cumplimiento editorial

| Criterio | Estado |
|----------|--------|
| Enseña desde primeros principios | Cumplido — cada etapa parte del problema antes de la solución |
| Explica el "por qué" antes del "cómo" | Cumplido |
| Tono profesional conversacional | Cumplido |
| Terminología oficial con siglas en primera aparición | Cumplido — IA, ML, DL, LLM, RNN |
| Sin frases prohibidas ("la IA piensa", etc.) | Cumplido — revisado |
| Diagrama Mermaid | Cumplido — timeline con todas las etapas |
| Analogía breve que aclara sin simplificar | Cumplido — analogía Falcon 9 |
| Ejemplo real con lección aplicable | Cumplido — vehículos autónomos y la brecha de expectativas |
| Diálogo con al menos 4 intercambios | Cumplido — 5 intercambios |
| Al menos 3 errores frecuentes | Cumplido — 5 errores |
| Al menos 4 buenas prácticas accionables | Cumplido — 6 buenas prácticas |
| Laboratorio completo con todos los componentes | Cumplido |
| 5-7 preguntas de reflexión | Cumplido — 7 preguntas |
| Resumen narrativo integrador | Cumplido |
| Checklist del capítulo | Cumplido — 7 ítems |
| Glosario 5-8 términos | Cumplido — 8 términos |
| Próximos pasos / próximo capítulo | Cumplido |
| Frase editorial de cierre | Cumplido |

---

## Observaciones para la revisión técnica (v0.8)

Las siguientes áreas deberán ser verificadas en la revisión técnica antes de avanzar a v0.8:

1. **Fechas:** Verificar la precisión de las fechas del Informe Lighthill (1973), AlexNet (2012), la publicación de *Attention Is All You Need* (2017) y los hitos de GPT (GPT-2 2019, GPT-3 2020, InstructGPT/ChatGPT 2022).

2. **Afirmaciones sobre predicciones de vehículos autónomos:** Verificar las citas específicas atribuidas a Tesla/Elon Musk y Waymo para el Ejemplo Real. Si no pueden verificarse con precisión, reformular de forma más general.

3. **Descripción de backpropagation:** La descripción en la sección 4.7 es correcta pero simplificada. Evaluar si en v0.8 conviene agregar una nota aclaratoria sobre la distinción entre backpropagation como algoritmo de cálculo de gradientes y el descenso por gradiente como algoritmo de optimización.

4. **RLHF:** El acrónimo *Reinforcement Learning from Human Feedback* aparece en la sección 4.10 sin ser desarrollado. Evaluar si en este capítulo es suficiente mencionarlo como dato histórico (postura actual) o si requiere una explicación mínima.

5. **Coherencia con capítulos adyacentes:** Verificar que el Capítulo 2 v0.5 prepare correctamente los conceptos introducidos aquí, y que el Capítulo 4 v0.5 tome los conceptos dejados como "próximo paso" al final de este capítulo.

---

## Métricas de la revisión

| Métrica | v0.1 | v0.5 |
|---------|------|------|
| Palabras aproximadas | ~800 | ~5.800 |
| Secciones | 9 | 17 |
| Etapas históricas desarrolladas | 8 (superficialmente) | 10 (con ciclo completo) |
| Intercambios en el diálogo | 2 | 5 |
| Ítems en el laboratorio | 3 (no estructurado) | 4 pasos + validación + reflexión + 3 desafíos |
| Errores frecuentes | 0 | 5 |
| Buenas prácticas | 0 (implícitas en resumen) | 6 |
| Términos en glosario | 0 | 8 |

---

## Estado del archivo

- Archivo principal: `/book/modulo-01/v0.5-draft/capitulo-03.md`
- Notas de revisión: `/Modulo1/code/v0.5-draft/revision-notes/capitulo-03-notes.md`
- Próxima revisión esperada: v0.8 (revisión técnica)
- Pendiente: alineación con Capítulo 2 v0.5 y Capítulo 4 v0.5 cuando estén disponibles.
