# Ingeniería de IA desde los Fundamentos

# Módulo I --- Los Fundamentos de la Inteligencia Artificial

# Capítulo 10 --- Embeddings

**Versión:** 0.1 (Primer borrador editorial)

------------------------------------------------------------------------

# Objetivos

Al finalizar este capítulo deberías poder:

-   Explicar qué es un embedding sin recurrir a fórmulas matemáticas.
-   Comprender cómo un modelo representa el significado de un texto.
-   Entender por qué los embeddings son la base de la búsqueda semántica
    y de los sistemas RAG.
-   Diferenciar búsqueda por palabras clave de búsqueda por significado.
-   Identificar cuándo conviene utilizar embeddings en una arquitectura.

------------------------------------------------------------------------

# Introducción

Hasta ahora vimos que los modelos trabajan con tokens y utilizan una
ventana de contexto para generar respuestas.

Sin embargo, todavía queda una pregunta fundamental.

> ¿Cómo "sabe" un modelo que dos textos hablan de lo mismo aunque
> utilicen palabras diferentes?

La respuesta comienza con un concepto llamado **embedding**.

Los embeddings constituyen uno de los pilares de la IA moderna y
permiten construir aplicaciones capaces de recuperar información por
significado y no solamente por coincidencia de palabras.

------------------------------------------------------------------------

# El problema

Imaginemos dos preguntas:

-   "¿Cómo reinicio mi contraseña?"
-   "Olvidé mi clave de acceso."

Las palabras son diferentes.

Sin embargo, para una persona ambas expresan prácticamente la misma
intención.

Un buscador tradicional basado únicamente en palabras clave podría no
relacionarlas correctamente.

Necesitamos una forma distinta de representar el significado.

------------------------------------------------------------------------

# ¿Qué es un embedding?

Un embedding es una representación numérica de un texto, una palabra,
una imagen o cualquier otro objeto, diseñada para capturar su
significado.

No es un resumen.

No es una traducción.

Es una forma de ubicar conceptos dentro de un espacio matemático donde
los elementos con significado parecido quedan próximos entre sí.

Podemos imaginarlo como un mapa.

En ese mapa, ideas similares ocupan posiciones cercanas.

Ideas diferentes aparecen alejadas.

------------------------------------------------------------------------

# Una analogía

Pensá en una ciudad.

Dos casas pueden tener colores distintos y tamaños diferentes.

Sin embargo, si están en el mismo barrio, probablemente compartan muchas
características.

Los embeddings hacen algo parecido.

No comparan únicamente las palabras.

Comparan la "ubicación semántica" de los conceptos.

------------------------------------------------------------------------

# ¿Cómo se utilizan?

El flujo simplificado suele ser el siguiente:

``` text
Documento
      ↓
Modelo de embeddings
      ↓
Vector numérico
      ↓
Base vectorial
      ↓
Búsqueda por similitud
```

Cuando el usuario realiza una consulta:

``` text
Pregunta
      ↓
Embedding
      ↓
Comparación con los vectores almacenados
      ↓
Documentos más similares
```

El modelo ya no busca coincidencias exactas.

Busca cercanía semántica.

------------------------------------------------------------------------

# Búsqueda tradicional vs búsqueda semántica

## Búsqueda tradicional

-   Coincidencia de palabras.
-   Muy rápida.
-   Puede perder documentos relevantes si utilizan vocabulario
    diferente.

## Búsqueda semántica

-   Busca significado.
-   Tolera sinónimos y distintas formas de expresar una idea.
-   Es la base de muchos asistentes modernos.

Ambos enfoques pueden combinarse.

De hecho, muchas arquitecturas utilizan estrategias híbridas.

------------------------------------------------------------------------

# Embeddings y RAG

Cuando estudiemos Retrieval-Augmented Generation (RAG), veremos que los
embeddings cumplen un papel central.

Un sistema RAG normalmente:

1.  Convierte documentos en embeddings.
2.  Los almacena en una base vectorial.
3.  Convierte la consulta del usuario en otro embedding.
4.  Recupera los documentos más similares.
5.  Envía únicamente esos documentos al LLM.

Este diseño permite responder utilizando información propia de la
organización sin volver a entrenar el modelo.

------------------------------------------------------------------------

# Conversación con un arquitecto

**Usuario**

"Quiero que el modelo consulte toda la documentación."

**Arquitecto**

"No hace falta enviar todos los documentos. Recuperemos únicamente los
más relevantes mediante embeddings."

Esta decisión reduce costos, mejora tiempos de respuesta y disminuye el
riesgo de introducir contexto innecesario.

------------------------------------------------------------------------

# Caso aplicado

Supongamos el proyecto del Data Warehouse de Finnegans.

Un usuario escribe:

> "¿Cuánto facturamos el último trimestre?"

La aplicación puede:

-   interpretar la intención;
-   recuperar documentación relevante sobre tablas y métricas mediante
    embeddings;
-   generar la consulta adecuada;
-   responder utilizando únicamente el contexto necesario.

El embedding no responde la pregunta.

Ayuda a encontrar la información correcta.

------------------------------------------------------------------------

# Ideas clave

-   Un embedding representa significado, no texto literal.
-   Dos frases diferentes pueden producir embeddings cercanos si
    expresan la misma idea.
-   Los embeddings permiten construir buscadores semánticos.
-   Constituyen uno de los pilares de RAG.

------------------------------------------------------------------------

# Laboratorio

1.  Pensá cinco formas distintas de preguntar exactamente lo mismo.
2.  Reflexioná por qué un buscador basado en palabras podría fallar.
3.  Explicá por qué una búsqueda semántica tendría mayores
    probabilidades de éxito.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Puede un embedding reemplazar un LLM?
-   ¿Puede existir un RAG sin embeddings?
-   ¿Qué ventajas aporta una base vectorial respecto de una base
    relacional para este tipo de búsquedas?

------------------------------------------------------------------------

# Resumen

Los embeddings transforman información compleja en representaciones
numéricas capaces de preservar relaciones de significado.

Gracias a ellos es posible recuperar documentos relacionados aunque
utilicen vocabulario diferente.

Este concepto permitió el desarrollo de sistemas RAG, buscadores
semánticos y numerosas aplicaciones empresariales basadas en IA.

------------------------------------------------------------------------

# Lo que un arquitecto debería recordar

-   Un embedding representa significado.
-   Los embeddings no generan respuestas; recuperan contexto relevante.
-   La calidad de un RAG depende en gran medida de sus embeddings y de
    su estrategia de recuperación.
-   No todo problema requiere una base vectorial, pero cuando la
    búsqueda por significado es importante, los embeddings suelen ser la
    herramienta adecuada.

------------------------------------------------------------------------

# Próximo capítulo

**Capítulo 11 --- Temperatura, Top‑K, Top‑P y Sampling**

Analizaremos por qué un mismo modelo puede producir respuestas
diferentes frente al mismo prompt y cómo controlar ese comportamiento.

> "Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones."
