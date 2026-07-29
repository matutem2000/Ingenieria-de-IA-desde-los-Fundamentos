# Módulo 3 — Context Engineering

# Capítulo 06 — RAG (Retrieval-Augmented Generation) como componente del Context Engineering

## Sección 14 — Autoevaluación

> *"La autoevaluación no es un examen. Es la herramienta para verificar si los conceptos se comprenden o solo se recuerdan."*

---

## Instrucciones

Las preguntas siguientes están organizadas en tres niveles. Las preguntas de nivel básico verifican la comprensión de los conceptos centrales. Las de nivel intermedio evalúan la capacidad de analizar situaciones concretas. Las de nivel avanzado demandan síntesis y criterio de diseño.

Para cada pregunta de opción múltiple, identificar la respuesta correcta y justificarla. Para las preguntas abiertas, formular una respuesta de no más de cinco oraciones.

---

## Nivel básico: comprensión conceptual

**1.** ¿Cuál de las siguientes afirmaciones describe mejor la relación entre RAG y el Context Engineering?

a) RAG es una técnica de entrenamiento que ajusta los parámetros del modelo para incluir conocimiento externo.
b) RAG es una estrategia del Context Engineering que incorpora conocimiento externo al contexto de cada inferencia.
c) RAG reemplaza a las instrucciones del sistema cuando el corpus es suficientemente grande.
d) RAG y el fine-tuning son enfoques equivalentes que producen los mismos resultados.

---

**2.** ¿Cuál es la función principal de los embeddings en un pipeline RAG?

a) Almacenar los documentos originales en un formato comprimido para ahorrar espacio.
b) Convertir texto en vectores numéricos donde textos con significados similares producen vectores cercanos.
c) Generar resúmenes automáticos de los fragmentos antes de indexarlos.
d) Comprimir los fragmentos para que quepan dentro de la ventana de contexto del modelo.

---

**3.** ¿Por qué el chunking es considerado la decisión más crítica de la fase de indexación?

a) Porque determina el costo computacional del embedding.
b) Porque la estrategia de segmentación define la granularidad y coherencia de los fragmentos que el retrieval puede recuperar.
c) Porque el tamaño del chunk determina la latencia del modelo de lenguaje.
d) Porque el chunking afecta únicamente a los documentos más largos del corpus.

---

**4.** ¿Qué problema resuelve la búsqueda híbrida (dense + sparse)?

a) Permite indexar documentos de cualquier idioma sin necesidad de un modelo multilingüe.
b) Elimina la necesidad de re-ranking al combinar dos estrategias de recuperación.
c) Mejora el recall para consultas que requieren tanto coincidencia semántica como coincidencia exacta de términos específicos.
d) Reduce el tamaño del índice vectorial combinando dos sistemas de almacenamiento.

---

## Nivel intermedio: análisis de situaciones

**5.** Un equipo desarrolla un asistente de soporte técnico que responde preguntas sobre la documentación de un producto de software. La documentación se actualiza con cada versión del producto, que se lanza cada seis semanas. El equipo considera usar fine-tuning para especializar el modelo en el vocabulario técnico del producto.

Analizar esta situación: ¿cuándo sería preferible RAG y cuándo fine-tuning? ¿Podría justificarse el uso de ambos en conjunto?

---

**6.** Un sistema RAG implementado hace seis meses comenzó a recibir reportes de usuarios que afirman que el sistema cita información desactualizada, específicamente referenciando versiones de procedimientos que fueron revisadas en los últimos tres meses. El corpus fuente sí fue actualizado: los documentos nuevos están disponibles en el repositorio.

¿Cuál es la causa más probable del problema? ¿Qué cambio en el diseño del pipeline habría prevenido esta situación?

---

**7.** Un AI Engineer propone mejorar la calidad del retrieval agregando un modelo de cross-encoder para re-ranking. El equipo de producto objeta que la latencia del sistema ya está cerca del límite aceptable (2 segundos de extremo a extremo) y que agregar el cross-encoder aumentaría la latencia en 300-400ms adicionales.

¿Cómo evaluarías esta situación? ¿Qué alternativas podrían considerarse para mejorar la calidad del retrieval sin aumentar la latencia de forma significativa?

---

**8.** El corpus de un sistema RAG tiene 60.000 fragmentos provenientes de 3.000 documentos, de los cuales el 40% son versiones antiguas de documentos que ya tienen una versión actualizada. Ambas versiones coexisten en el índice.

¿Cómo afecta esta situación a la calidad del retrieval? ¿Qué proceso de gestión del índice debería implementarse para resolver y prevenir este problema?

---

## Nivel avanzado: criterio de diseño

**9.** Diseñar en términos conceptuales un pipeline RAG para el siguiente escenario: una plataforma de e-learning con 500.000 estudiantes que necesita un asistente que responda preguntas sobre el material de sus cursos. Cada estudiante accede solo al material de los cursos en los que está inscripto. El catálogo de cursos tiene 2.000 cursos, cada uno con materiales de entre 10 y 200 páginas. El material de cada curso se actualiza aproximadamente una vez por semestre.

Describir: estrategia de chunking, metadatos clave, cómo se implementa el control de acceso, estrategia de retrieval y política de actualización.

---

**10.** En el capítulo se presentaron cinco anti-patrones de RAG. Elegir el anti-patrón que consideres más difícil de detectar en la práctica y explicar: por qué es difícil de detectar, qué señales indirectas podrían alertar al equipo sobre su presencia, y qué métricas o procesos permitirían confirmarlo.

---

## Respuestas de referencia (preguntas de opción múltiple)

**Pregunta 1:** La respuesta correcta es **b**. RAG es una estrategia del Context Engineering que enriquece el contexto enviado al modelo en cada inferencia; no modifica los parámetros del modelo ni reemplaza a las instrucciones del sistema.

**Pregunta 2:** La respuesta correcta es **b**. Los embeddings representan el significado del texto como posición en un espacio vectorial; la operación de retrieval busca posiciones cercanas en ese espacio.

**Pregunta 3:** La respuesta correcta es **b**. Si los fragmentos no son coherentes —rompen definiciones, separan condiciones de sus antecedentes, mezclan ideas de secciones distintas—, el retrieval recuperará fragmentos que el modelo no podrá usar eficientemente aunque la búsqueda vectorial sea técnicamente correcta.

**Pregunta 4:** La respuesta correcta es **c**. BM25 captura coincidencia exacta de términos (nombres propios, identificadores, siglas) que la búsqueda vectorial puede no recuperar si el embedding no representa esos términos con suficiente discriminación. La combinación mejora el recall global.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
