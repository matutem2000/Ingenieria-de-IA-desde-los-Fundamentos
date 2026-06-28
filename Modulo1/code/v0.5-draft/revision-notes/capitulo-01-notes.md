# Notas de Revisión — Capítulo 1 v0.5
## ¿Qué entendemos por inteligencia?

**Módulo:** I — Los Fundamentos de la Inteligencia Artificial  
**Capítulo:** 1  
**Versión revisada:** 0.5  
**Versión anterior:** 0.1  
**Editor:** Claude (asistente editorial técnico)  
**Fecha:** 2026-06-28

---

## 1. Resumen ejecutivo de la revisión

La v0.1 era un esqueleto funcional con las ideas centrales correctas pero sin el desarrollo necesario para cumplir los objetivos pedagógicos del libro. La v0.5 expande el capítulo de aproximadamente 600 palabras a más de 3.500 palabras, incorpora todos los apartados de la estructura obligatoria y eleva el nivel pedagógico de forma sustancial.

---

## 2. Qué se conservó de la v0.1

- La pregunta central del capítulo: "¿Qué significa realmente ser inteligente?"
- La estructura narrativa de apertura con la imagen de la caja.
- La afirmación de que la IA no nació con ChatGPT.
- La afirmación de que la inteligencia no es una habilidad única sino un conjunto de capacidades.
- La analogía de la empresa con departamentos.
- El primer principio del libro (preguntar por el problema antes que por la solución).
- La reflexión del arquitecto sobre cuándo no usar IA.
- La frase de cierre obligatoria.

---

## 3. Qué se expandió

### Introducción (v0.1 → v0.5)
- En v0.1: 3 párrafos breves que establecen el tono.
- En v0.5: 3 párrafos con referencias históricas explícitas (Platón, Descartes, Turing) que contextualizan por qué la pregunta sobre inteligencia es previa a la tecnología. Se añadió una advertencia explícita sobre por qué este capítulo no es "filosófico opcional" sino fundacional para la práctica.

### Motivación del problema (nuevo apartado)
- No existía en v0.1.
- En v0.5: apartado completo que explica el problema concreto que resuelve este capítulo (la confusión conceptual sobre "IA" que genera fracasos de implementación), y por qué esa confusión existe (la IA llegó como producto antes que como concepto al mainstream).

### Desarrollo conceptual (v0.1 → v0.5)
- En v0.1: 2 párrafos que afirman que la inteligencia es múltiple sin detallar cuáles son esas dimensiones.
- En v0.5: 8 dimensiones cognitivas definidas y explicadas individualmente (razonamiento lógico, memoria, aprendizaje, abstracción, planificación, lenguaje, percepción, metacognición). Para cada dimensión se añade su relevancia en sistemas de IA actuales.
- Se añadió un apartado específico sobre cómo distintos sistemas de IA cubren distintas dimensiones, con ejemplos concretos de LLM, ML clásico y sistemas expertos.
- Se añadió un apartado sobre la historia de la IA que contextualiza la Prueba de Turing y los ciclos de la disciplina.

### Analogía (v0.1 → v0.5)
- En v0.1: la analogía de la empresa con departamentos estaba presente en 4 líneas.
- En v0.5: se mantuvo la misma analogía y se desarrolló con mayor detalle. Se añadió el cierre de la analogía hacia el diseño de sistemas de IA ("no existe un modelo único que resuelva todo").

---

## 4. Qué se agregó nuevo

### Diagrama Mermaid
- Diagrama de tipo mindmap con las 8 dimensiones cognitivas como ramas del nodo "Inteligencia".
- Cada rama incluye los tipos de sistemas de IA más asociados a esa dimensión.
- Nota editorial bajo el diagrama que aclara que ningún sistema cubre el árbol completo.
- Elección del tipo mindmap: permite visualizar la naturaleza distribuida y multidimensional de la inteligencia, que es la idea central del capítulo.

### Ejemplo empresarial (TerraLogix)
- Empresa ficticia con nombre realista: TerraLogix (consultoría de infraestructura).
- Personajes con nombres y roles concretos: Valentina Soria (directora comercial), Rodrigo Méndez (CTO).
- El escenario ilustra directamente la idea central: "un problema de IA" es en realidad múltiples subproblemas con soluciones distintas.
- Los tres subproblemas identificados (priorización de leads, generación de mensajes, análisis de tendencias) mapean a tres tipos distintos de sistemas de IA.

### Conversación con un arquitecto
- Personajes: Martina (desarrolladora senior incorporada a un equipo de IA) y Diego (arquitecto del proyecto).
- 4 intercambios que cubren: por qué empieza el libro con filosofía, la diferencia entre desarrollador y arquitecto, un caso real donde la solución correcta fue "no usar IA", y la síntesis conceptual del capítulo.
- El diálogo está escrito en registro conversacional pero técnicamente preciso, coherente con el tono del libro.

### Errores frecuentes
1. Tratar "IA" como concepto unitario (con consecuencia práctica: selección por popularidad).
2. Confundir competencia en una dimensión con inteligencia general (con referencia explícita al fenómeno de alucinación en LLMs).
3. Ignorar la dimensión de la metacognición (con consecuencia práctica: decisiones basadas en outputs incorrectos presentados con alta confianza).

### Buenas prácticas (6 prácticas accionables)
1. Definir qué capacidad cognitiva necesita el problema antes de evaluar soluciones.
2. Preguntar si IA es necesaria o si un sistema determinista resuelve mejor.
3. Separar problemas compuestos en subproblemas atómicos.
4. Mantener escepticismo calibrado ante demostraciones.
5. Documentar suposiciones implícitas sobre inteligencia en las decisiones de diseño.
6. Preguntar "¿qué pasa cuando falla?" antes de "¿cómo lo construimos?".

### Laboratorio completo
- Empresa ficticia: FreightCore (logística).
- Personaje: Ana Burgos (gerente de operaciones).
- 4 pasos estructurados que llevan al lector a descomponer un problema compuesto, mapear dimensiones cognitivas, evaluar si requiere IA, y sintetizar en un cuadro.
- Tabla de trabajo incluida como plantilla.
- Criterios de validación explícitos (incluyendo un indicador de alerta: si todos los subproblemas marcaron "sí, requiere IA", revisar el análisis).
- 3 preguntas de reflexión del laboratorio.
- 3 desafíos opcionales con niveles de dificultad progresivos.

### Preguntas de reflexión (7 preguntas)
- Las 5 preguntas originales de v0.1 fueron reemplazadas por 7 preguntas de mayor profundidad que desarrollan criterio profesional, no solo comprensión conceptual.
- Las preguntas cubren: epistemología de la inteligencia, evaluación de sistemas, implicancias éticas, presiones organizacionales y autodiagnóstico profesional.

### Resumen narrativo
- Párrafo integrador que sintetiza los conceptos del capítulo y enmarca el método de análisis como hilo conductor del libro.

### Checklist del capítulo
- 7 ítems verificables que el lector puede usar para autoevaluar su comprensión antes de continuar.

### Glosario breve
- 8 términos definidos en una línea: IA, ML, LLM, metacognición, Prueba de Turing, alucinación, primeros principios, inferencia.
- Todos los términos siguen la convención de TERMINOLOGY.md (nombre completo en primera aparición con sigla entre paréntesis).

### Conexión al Capítulo 2
- La sección "Próximos pasos" ahora explica con mayor precisión qué responderá el capítulo siguiente y crea un puente narrativo explícito.

---

## 5. Analogías usadas

| Analogía | Concepto que ilustra | Evaluación |
|---|---|---|
| Caja con "inteligencia" | La inteligencia como algo que se evalúa por comportamiento, no por afirmación | Mantenida de v0.1. Clara y efectiva para enganche inicial. |
| Empresa con departamentos | La inteligencia como sistema de capacidades integradas, no como capacidad única | Mantenida y expandida. Se añade el cierre hacia diseño de sistemas. |

---

## 6. Diagrama creado

**Tipo:** Mermaid mindmap  
**Concepto ilustrado:** Las dimensiones de la inteligencia y su cobertura en sistemas de IA actuales  
**Nodo raíz:** Inteligencia  
**Ramas (8):** Razonamiento lógico, Memoria y recuperación, Aprendizaje, Abstracción y categorización, Planificación y anticipación, Lenguaje y comunicación, Percepción y reconocimiento, Metacognición  
**Subramas:** Ejemplos de sistemas de IA correspondientes a cada dimensión  

**Decisión de diseño:** Se eligió mindmap sobre flowchart porque el objetivo es mostrar naturaleza multidimensional y paralela, no secuencial. El árbol comunica visualmente que no hay jerarquía ni orden entre dimensiones.

**Limitación conocida:** El diagrama no muestra la interacción entre dimensiones, solo su existencia separada. Una versión futura podría usar un diagrama de red (grafo) para mostrar interdependencias.

---

## 7. Observaciones editoriales

### Tono y estilo
- El capítulo mantiene el registro conversacional del libro sin sacrificar rigor técnico.
- Los personajes del ejemplo y del diálogo tienen nombres hispanos y roles concretos, lo que aumenta la identificación del lector latinoamericano.
- Se evitaron en todo el texto las frases prohibidas por TERMINOLOGY.md ("La IA piensa", "El modelo sabe", etc.).

### Coherencia con el libro
- El capítulo establece el método de primeros principios que se usará en todo el libro.
- El glosario introduce los términos que serán usados en capítulos posteriores (LLM, ML, RAG referenciado en el diagrama).
- La conexión al Capítulo 2 está escrita para crear tensión narrativa, no solo como anuncio de contenido.

### Puntos a revisar en v0.8 (revisión técnica)
- Verificar que las referencias a capacidades cognitivas (especialmente metacognición) sean coherentes con los marcos teóricos que se usen en capítulos posteriores sobre agentes de IA.
- Evaluar si el diagrama Mermaid mindmap se renderiza correctamente en todos los entornos de publicación previstos.
- Revisar si la mención a "ciclos de invierno de la IA" requiere una nota a pie de página o un apartado más desarrollado (actualmente se menciona sin definición formal).
- La tabla del laboratorio puede requerir ajuste de formato según el sistema de publicación final.

### Posibles extensiones para v0.8
- Añadir referencias bibliográficas (Turing 1950, Gardner sobre inteligencias múltiples, Minsky sobre "La Sociedad de la Mente").
- Evaluar si agregar un segundo diagrama que muestre la relación entre tipos de sistemas de IA y las dimensiones cognitivas (matriz en lugar de mindmap).
- Considerar un apartado de "Lo que un arquitecto debería recordar" como síntesis ejecutiva al final (mencionado en STYLE_GUIDE.md como ítem 13 de la estructura).
