# Capítulo 3 --- Sección 07 de 10

# Reranking: mejorando la calidad antes de generar la respuesta

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Recuperar documentos relevantes es importante. Ordenarlos
> correctamente suele ser aún más importante."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué es el reranking y qué problema resuelve.
-   Diferenciar recuperación inicial de reordenamiento.
-   Conocer el papel de los modelos *cross-encoder*.
-   Incorporar criterios para decidir cuándo el reranking aporta valor.

------------------------------------------------------------------------

# Introducción

En las secciones anteriores vimos que una consulta se transforma en un
embedding y se utiliza para recuperar los documentos más cercanos dentro
de una base vectorial.

Sin embargo, la similitud vectorial no siempre produce el orden ideal.

Es frecuente recuperar veinte documentos potencialmente relevantes donde
solo tres contienen exactamente la información necesaria.

Enviar todos esos documentos al LLM aumenta el consumo de tokens,
incrementa la latencia y puede introducir ruido.

Aquí aparece el reranking.

------------------------------------------------------------------------

# Dos etapas diferentes

Conviene separar claramente ambos procesos.

**Recuperación inicial**

Su objetivo es encontrar rápidamente un conjunto reducido de candidatos.

Debe ser veloz incluso sobre millones de documentos.

**Reranking**

Su objetivo es analizar con mayor profundidad esos candidatos y
ordenarlos según su verdadera relevancia para la consulta.

Al trabajar únicamente sobre unas pocas decenas de documentos puede
utilizar modelos más costosos y precisos.

------------------------------------------------------------------------

# ¿Cómo funciona?

El flujo general puede resumirse así:

1.  El usuario realiza una consulta.
2.  Se recuperan los *k* documentos más cercanos mediante búsqueda
    vectorial o híbrida.
3.  Un modelo de reranking compara la consulta con cada documento.
4.  Se calcula una nueva puntuación de relevancia.
5.  Solo los mejores documentos se envían al LLM.

``` mermaid
flowchart LR
A[Consulta] --> B[Recuperación inicial]
B --> C[Top K documentos]
C --> D[Modelo de Reranking]
D --> E[Ranking refinado]
E --> F[LLM]
```

------------------------------------------------------------------------

# ¿Por qué utilizar otro modelo?

Los modelos de embeddings buscan representar significado de forma
eficiente.

Los modelos de reranking persiguen un objetivo distinto.

Analizan simultáneamente la consulta y cada documento para estimar con
mayor precisión si realmente responden a la necesidad del usuario.

En muchos casos se implementan mediante arquitecturas conocidas como
**cross-encoders**, capaces de evaluar relaciones más profundas que una
simple distancia entre vectores.

El costo computacional es mayor.

La precisión también.

------------------------------------------------------------------------

# ¿Siempre es necesario?

No.

El reranking incorpora complejidad adicional.

En repositorios pequeños o consultas muy específicas puede aportar poco
valor.

Sin embargo, cuando existen miles o millones de documentos con
contenidos similares suele producir mejoras significativas.

Como en cualquier decisión arquitectónica, la respuesta depende del
contexto.

------------------------------------------------------------------------

# Caso de estudio

Una compañía mantiene un repositorio con miles de procedimientos de
recursos humanos.

Una búsqueda semántica recupera diez documentos relacionados con
licencias.

Solo dos describen la licencia por adopción solicitada por el usuario.

El modelo de reranking reordena esos resultados considerando el
contenido completo de cada documento y coloca esos dos procedimientos en
las primeras posiciones.

El LLM recibe un contexto mucho más preciso y genera una respuesta
correctamente fundamentada.

------------------------------------------------------------------------

# Costos y beneficios

Incorporar un paso de reranking implica:

-   una llamada adicional a un modelo;
-   mayor tiempo de procesamiento;
-   consumo extra de recursos.

A cambio puede ofrecer:

-   mayor precisión;
-   menor cantidad de contexto enviado al LLM;
-   reducción del ruido documental;
-   mejor aprovechamiento de la ventana de contexto.

El balance debe evaluarse mediante métricas objetivas y pruebas
representativas.

------------------------------------------------------------------------

# Ideas clave

-   Recuperación y reranking son procesos distintos.
-   El reranking optimiza la calidad del contexto, no la generación.
-   Los modelos de reranking priorizan precisión sobre velocidad.
-   La decisión de incorporarlo debe justificarse con datos y
    necesidades del negocio.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección analizaremos cómo evaluar objetivamente un
sistema RAG, qué métricas utilizar y cómo medir la calidad de la
recuperación y de las respuestas generadas.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
