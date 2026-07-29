# Módulo 3 — Context Engineering

# Capítulo 06 — RAG (Retrieval-Augmented Generation) como componente del Context Engineering

## Sección 13 — Resumen del capítulo

---

## Lo que aprendimos en este capítulo

Este capítulo presentó RAG como una estrategia del Context Engineering para incorporar conocimiento externo al contexto que el modelo recibe en cada inferencia. El recorrido siguió una progresión deliberada: del problema, a los componentes técnicos, a la arquitectura completa, a los criterios de decisión.

---

## El problema que RAG resuelve

El conocimiento interno de un modelo de lenguaje queda congelado en la fecha de corte del entrenamiento. Hay tres clases de conocimiento que el modelo no puede tener en su estado base: conocimiento temporal (posterior al corte), conocimiento privado (documentos internos de la organización) y conocimiento de nicho (dominio especializado subrepresentado en el preentrenamiento).

Actualizar el conocimiento vía reentrenamiento o fine-tuning es costoso, lento y no produce trazabilidad. RAG desacopla el conocimiento del sistema del conocimiento del modelo, permitiendo actualizar el primero sin modificar el segundo.

---

## La arquitectura en dos fases

RAG tiene dos fases bien diferenciadas:

**Fase offline (indexación):** los documentos se ingresan, se segmentan en fragmentos (chunking), cada fragmento se convierte en un vector (embedding) y se almacena en una base vectorial con sus metadatos asociados. Los errores en esta fase afectan a todas las consultas futuras.

**Fase online (recuperación e inferencia):** la consulta del usuario se convierte en un vector, el sistema busca los fragmentos más similares, los reordena mediante re-ranking, ensambla el contexto y lo entrega al modelo para que genere la respuesta.

---

## Los componentes técnicos

**Embeddings:** representaciones vectoriales del texto donde fragmentos con significados similares producen vectores cercanos en el espacio semántico. La elección del modelo de embedding debe considerar idioma, dominio y restricciones de privacidad.

**Bases vectoriales:** sistemas de almacenamiento y búsqueda diseñados para comparar vectores por similitud. Los algoritmos de búsqueda aproximada (HNSW, IVF) permiten escalar el retrieval a millones de fragmentos con latencias bajas. El filtrado por metadatos permite implementar control de acceso y relevancia temporal.

---

## Las decisiones que determinan la calidad

**Chunking:** la estrategia de segmentación es la decisión de mayor impacto sobre la calidad del retrieval. Fragmentos que parten ideas incompletas producen recuperaciones irrelevantes aunque el algoritmo de búsqueda sea correcto.

**Estrategia de recuperación:** el retrieval naive (top-k por similitud vectorial) puede complementarse con expansión de consulta, HyDE, MMR o búsqueda híbrida (dense + BM25) según el tipo de consulta y el corpus.

**Re-ranking:** los cross-encoders mejoran la precisión del ranking sobre los candidatos iniciales. El re-ranking temporal es crítico en dominios con información dinámica. El re-ranking por perfil personaliza el contexto según el usuario.

---

## Las decisiones que determinan la robustez

**Política de actualización del índice:** un índice estático se convierte en un pasivo de información. La actualización incremental es un requisito operativo, no una mejora futura.

**Control de acceso a nivel de fragmento:** el filtrado por nivel de acceso debe aplicarse durante el retrieval, no solo en la interfaz de usuario.

**Trazabilidad de fuentes:** en dominios regulados, cada respuesta debe incluir referencia a los documentos que la respaldaron.

**Monitoreo de calidad:** precision@k, recall@k y MRR deben medirse sobre consultas representativas, de forma continua en producción.

---

## RAG dentro del Context Engineering

RAG es una de las cuatro estrategias del Context Engineering cubiertas en este módulo:

| Estrategia | Función |
|---|---|
| Instrucciones del sistema | Define comportamiento, rol y restricciones |
| Memoria conversacional | Mantiene continuidad entre turnos y sesiones |
| Resumen y compresión | Gestiona el contexto cuando supera la ventana |
| RAG | Incorpora conocimiento externo relevante por consulta |

En aplicaciones empresariales completas, estas cuatro estrategias coexisten y se coordinan dentro de la misma arquitectura.

---

## La decisión RAG vs. fine-tuning

RAG es preferible cuando el conocimiento cambia frecuentemente o cuando se requiere trazabilidad. El fine-tuning es preferible cuando el objetivo es ajustar el comportamiento del modelo (tono, formato, estilo de razonamiento) de forma consistente. En sistemas de producción maduros, ambas técnicas suelen coexistir: fine-tuning para el comportamiento base y RAG para el conocimiento actualizable.

---

## Los anti-patrones que más frecuentemente falla un proyecto RAG

1. Usar RAG como sustituto de fine-tuning para ajustar el comportamiento del modelo.
2. Construir el índice una vez y no actualizarlo.
3. Chunking descuidado que rompe la coherencia de los fragmentos.
4. No implementar control de acceso a nivel de fragmento.
5. No medir la calidad del retrieval independientemente de la calidad de la respuesta final.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
