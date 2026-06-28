# Capítulo 3 --- Sección 06 de 10

# Búsqueda híbrida: combinando significado y coincidencia textual

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Los mejores sistemas RAG no eligen entre búsqueda semántica o
> búsqueda léxica. Aprovechan las fortalezas de ambas."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender la diferencia entre búsqueda léxica y búsqueda semántica.
-   Entender el funcionamiento general de BM25.
-   Conocer el concepto de búsqueda híbrida (*Hybrid Search*).
-   Identificar cuándo conviene utilizar cada estrategia dentro de una
    arquitectura RAG.

------------------------------------------------------------------------

# Introducción

Durante muchos años los motores de búsqueda empresariales se basaron en
coincidencias de palabras.

Si un documento contenía exactamente los términos solicitados por el
usuario, tenía mayores probabilidades de aparecer entre los primeros
resultados.

Este enfoque continúa siendo extremadamente útil.

Sin embargo, presenta limitaciones cuando distintas palabras expresan
una misma idea.

La búsqueda semántica resolvió parte de este problema, pero tampoco es
perfecta.

La búsqueda híbrida surge para combinar ambos enfoques.

------------------------------------------------------------------------

# Búsqueda léxica

La búsqueda léxica trabaja sobre el texto.

Analiza palabras, frecuencia de aparición y otros indicadores
estadísticos.

Uno de los algoritmos más utilizados es **BM25**.

De forma simplificada, BM25 intenta responder una pregunta:

> ¿Qué documentos contienen con mayor relevancia los términos utilizados
> por el usuario?

Este enfoque resulta especialmente eficaz cuando existen nombres
propios, códigos, números de expediente, identificadores o terminología
exacta.

------------------------------------------------------------------------

# Búsqueda semántica

La búsqueda semántica trabaja sobre embeddings.

En lugar de comparar palabras, compara significado.

Esto permite recuperar documentos relacionados aunque utilicen
vocabularios diferentes.

Por ejemplo, una consulta sobre "licencia por nacimiento" puede
recuperar documentación titulada "licencia por paternidad" aunque
ninguna palabra coincida exactamente.

------------------------------------------------------------------------

# ¿Por qué combinar ambas?

Cada enfoque resuelve problemas distintos.

La búsqueda léxica destaca cuando los términos exactos son importantes.

La búsqueda semántica sobresale cuando el significado resulta más
relevante que la coincidencia textual.

Al combinar ambas se obtiene un sistema más robusto.

``` mermaid
flowchart LR
A[Consulta] --> B[BM25]
A --> C[Embeddings]
B --> D[Fusión de resultados]
C --> D
D --> E[Ranking final]
E --> F[LLM]
```

------------------------------------------------------------------------

# Estrategias de fusión

Existen distintas formas de combinar resultados.

Algunas arquitecturas asignan una puntuación independiente a cada método
y luego calculan un ranking conjunto.

Otras aplican primero filtros léxicos y posteriormente una búsqueda
semántica sobre el subconjunto resultante.

La estrategia adecuada depende del dominio, del volumen documental y de
los objetivos del negocio.

------------------------------------------------------------------------

# Caso de estudio

Un organismo público dispone de millones de expedientes.

Un usuario consulta un número de resolución específico.

En este escenario, la búsqueda léxica obtiene mejores resultados porque
el identificador debe coincidir exactamente.

Otro usuario pregunta:

> "¿Cómo solicitar una prórroga por maternidad?"

Aquí la búsqueda semántica resulta superior porque puede recuperar
documentos relacionados aunque la redacción sea diferente.

La búsqueda híbrida permite responder correctamente en ambos escenarios
utilizando una única arquitectura.

------------------------------------------------------------------------

# Buenas prácticas

-   Evaluar ambos enfoques con consultas reales.
-   No asumir que un único método resolverá todos los casos.
-   Ajustar el peso relativo entre búsqueda léxica y semántica según el
    dominio.
-   Medir precisión, cobertura y latencia antes de modificar la
    estrategia.

------------------------------------------------------------------------

# Ideas clave

-   BM25 y los embeddings resuelven problemas diferentes.
-   La búsqueda híbrida aprovecha las fortalezas de ambos enfoques.
-   El ranking final depende de una estrategia de combinación
    cuidadosamente diseñada.
-   La evaluación debe realizarse sobre datos representativos del
    negocio.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección analizaremos el **reranking**, una técnica
utilizada para volver a ordenar los documentos recuperados y mejorar aún
más la calidad del contexto enviado al modelo de lenguaje.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
