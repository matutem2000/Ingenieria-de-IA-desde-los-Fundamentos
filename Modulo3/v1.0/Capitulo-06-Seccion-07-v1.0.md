# Módulo 3 — Context Engineering

# Capítulo 06 — RAG (Retrieval-Augmented Generation) como componente del Context Engineering

## Sección 07 — Re-ranking y selección de contexto

> *"El primer retrieval busca candidatos. El re-ranking elige cuáles merecen entrar al contexto del modelo."*

---

## Objetivos de aprendizaje

- Comprender por qué el retrieval inicial produce candidatos que requieren refinamiento antes de ser insertados en el contexto.
- Analizar las tres estrategias principales de re-ranking: semántico, temporal y por perfil de usuario.
- Diseñar una política de selección de contexto que maximice la utilidad dentro del presupuesto de tokens disponible.
- Identificar los trade-offs entre precisión del re-ranking y latencia de la respuesta.

---

## Por qué el retrieval inicial no es suficiente

La búsqueda por similitud vectorial es eficiente y escalable, pero evalúa la relevancia de cada fragmento de manera independiente, sin considerar el conjunto. Esta evaluación independiente introduce dos tipos de problemas.

**Problema de representación.** Los modelos de embedding producen representaciones de significado global del texto. Son menos sensibles a matices locales: si la consulta menciona una condición específica ("¿cuál es el plazo de entrega cuando el pedido supera 100 unidades?"), el fragmento más relevante puede no ser el que tiene mayor similitud coseno global, sino el que específicamente contiene esa condición. Los modelos de cross-encoding, que procesan consulta y fragmento juntos, capturan estos matices mejor que los modelos bi-encoder usados para el retrieval inicial.

**Problema de conjunto.** Si los k fragmentos recuperados provienen de la misma sección de un mismo documento, el contexto que el modelo recibirá será redundante. Un re-ranking que considera el conjunto, en lugar de cada fragmento individualmente, puede producir un contexto más rico con el mismo número de tokens.

El re-ranking es la etapa que aborda ambos problemas: toma los candidatos del retrieval inicial y los reordena o filtra aplicando criterios más sofisticados.

---

## Re-ranking por relevancia semántica: los cross-encoders

Un cross-encoder es un modelo que recibe la consulta y un fragmento concatenados, y produce una puntuación de relevancia. A diferencia del bi-encoder usado para producir embeddings (que procesa consulta y fragmento por separado), el cross-encoder procesa ambos textos juntos, lo que permite capturar interacciones entre términos de la consulta y del fragmento.

Esta capacidad de capturar interacciones mejora significativamente la precisión del ranking, especialmente para consultas con condiciones específicas o terminología técnica. El costo es mayor latencia y costo computacional: un cross-encoder se ejecuta una vez por cada par (consulta, fragmento), lo que hace que su costo escale linealmente con el número de candidatos.

El patrón típico es:
1. Retrieval inicial con bi-encoder: recuperar los top 20-50 candidatos en milisegundos.
2. Re-ranking con cross-encoder sobre esos 20-50 candidatos: proceso más lento pero sobre un conjunto ya reducido.
3. Seleccionar los top 3-5 mejor puntuados por el cross-encoder para insertar en el contexto.

Modelos de re-ranking de código abierto como los de la familia BGE Reranker o Cohere Rerank están disponibles para distintos idiomas y dominios.

---

## Re-ranking por actualidad temporal

En dominios donde la información cambia con frecuencia —normativas, precios, versiones de software, noticias de mercado—, un fragmento técnicamente relevante pero desactualizado puede ser más dañino que no tener ningún fragmento: el modelo lo presentará como verdadero aunque ya no lo sea.

El re-ranking temporal ajusta la puntuación de cada candidato según la distancia entre la fecha del documento y el momento de la consulta. Fragmentos de documentos recientes reciben una bonificación; fragmentos de documentos antiguos reciben una penalización.

La función de ajuste puede ser lineal (puntuación reducida N% por cada mes de antigüedad) o exponencial (puntuación reducida a la mitad cada semestre). La elección depende del ritmo de cambio del dominio: en normativa tributaria puede ser suficiente penalizar documentos de más de dos años; en precios de mercado puede ser necesario penalizar documentos de más de dos días.

```
Puntuación ajustada = Puntuación semántica × Factor_temporal

Factor_temporal:
  - Documento de hoy:       1.0
  - Documento de 6 meses:   0.85
  - Documento de 1 año:     0.70
  - Documento de 2 años:    0.50
  - Documento de 3+ años:   0.25
```

La implementación requiere que los metadatos del índice incluyan la fecha de creación o última modificación del documento. Los sistemas RAG que no almacenan este metadato no pueden aplicar re-ranking temporal.

---

## Re-ranking por perfil de usuario

En aplicaciones donde distintos usuarios tienen roles, preferencias o contextos de trabajo diferentes, los fragmentos óptimos para la misma consulta pueden variar según quién pregunta.

Un director financiero y un analista junior pueden hacer la misma consulta sobre el presupuesto del trimestre, pero el director puede necesitar el resumen ejecutivo mientras el analista necesita el detalle por línea de partida. Un usuario habitual de la sede de Madrid puede necesitar la versión de los procedimientos aplicable a España, no la versión global.

El re-ranking por perfil combina la puntuación semántica con señales del perfil del usuario:

- **Rol en la organización:** ciertos tipos de documentos son más relevantes para ciertos roles.
- **Historial de consultas:** fragmentos de documentos que el usuario consultó frecuentemente en el pasado pueden recibir una bonificación.
- **Ubicación o división:** documentos específicos a la región o departamento del usuario tienen prioridad sobre documentos globales cuando ambos son igualmente relevantes.
- **Idioma preferido:** en corpus multilingüe, fragmentos en el idioma nativo del usuario pueden recibir preferencia cuando existen equivalentes en distintos idiomas.

El re-ranking por perfil requiere que el sistema mantenga información sobre el usuario y que esa información esté disponible durante la fase de recuperación. En aplicaciones con requerimientos de privacidad estrictos, el alcance del perfil de usuario puede estar limitado por regulación.

---

## Selección del contexto: el presupuesto de tokens

Una vez que el re-ranking produce una lista ordenada de fragmentos, el sistema debe decidir cuántos incluir en el contexto del modelo. Esta decisión está determinada por el presupuesto de tokens disponible en la ventana de contexto.

El presupuesto se calcula como:

```
Presupuesto de tokens para fragmentos =
    Capacidad total de la ventana
  - Tokens de las instrucciones del sistema
  - Tokens del historial conversacional relevante
  - Tokens de la consulta del usuario
  - Margen reservado para la respuesta esperada
```

La selección greedy toma los fragmentos ordenados por puntuación de re-ranking y los añade al contexto hasta agotar el presupuesto. Esta estrategia es simple y efectiva en la mayoría de los casos.

Una variante más sofisticada usa programación dinámica para seleccionar la combinación de fragmentos que maximiza la puntuación total dentro del presupuesto, en lugar de simplemente tomar los más puntuados en orden. Esta variante puede mejorar la calidad cuando hay fragmentos de puntuación moderada pero complementaria entre sí.

---

## El orden de los fragmentos en el contexto importa

La investigación en el comportamiento de los modelos de lenguaje ha documentado el fenómeno llamado "lost in the middle": los modelos tienden a prestar más atención al contenido al inicio y al final del contexto, y menos al contenido en el medio. Si el fragmento más relevante se inserta al final de una lista larga de fragmentos, el modelo puede "perderlo" al generar la respuesta.

La práctica recomendada es ordenar los fragmentos por relevancia decreciente y, si el modelo tiene esta tendencia conocida, colocar los más relevantes al principio del bloque de contexto. Algunos sistemas también añaden etiquetas explícitas ("Fragmento 1 (más relevante):", "Fragmento 2:", etc.) para guiar la atención del modelo.

---

## Nota del Arquitecto

> En muchos sistemas RAG que analicé en producción, el re-ranking estaba completamente ausente. El sistema recuperaba los top 5 por similitud vectorial y los insertaba directamente en el contexto, sin ningún criterio adicional. La mejora al agregar un cross-encoder de re-ranking era visible en las evaluaciones: precision@3 subía entre 15 y 30 puntos porcentuales dependiendo del corpus. El costo adicional —unos 100-200 ms por consulta— era completamente aceptable para las aplicaciones en cuestión. Si hay una sola optimización que recomendaría en un sistema RAG que ya funciona pero cuyas respuestas no son del todo precisas, es agregar un modelo de re-ranking.

---

## Ideas clave

- El re-ranking mejora la selección de candidatos usando criterios más sofisticados que la similitud vectorial global.
- Los cross-encoders capturan interacciones entre consulta y fragmento que los bi-encoders no pueden, a costo de mayor latencia.
- El re-ranking temporal es crítico en dominios donde la información cambia frecuentemente; requiere metadatos de fecha en el índice.
- El re-ranking por perfil personaliza el contexto según el rol, historial y contexto del usuario.
- El orden de los fragmentos en el contexto impacta sobre qué presta atención el modelo al generar la respuesta.

---

## Transición hacia la siguiente sección

Las secciones anteriores cubrieron los componentes técnicos individuales: embeddings, bases vectoriales, estrategias de recuperación y re-ranking. La siguiente sección los integra en una visión de conjunto: cómo se diseña y opera un pipeline RAG completo en un entorno empresarial real, con todas las consideraciones de producción que los tutoriales básicos omiten.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
