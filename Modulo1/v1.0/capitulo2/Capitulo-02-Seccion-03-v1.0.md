# Capítulo 2 --- Sección 03 de 10

# De la información a los vectores

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Las computadoras no comprenden palabras, imágenes ni sonidos.
> Comprenden números."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender por qué toda la información debe representarse
    numéricamente.
-   Entender el concepto de vector como estructura fundamental en IA.
-   Relacionar la representación matemática con el aprendizaje
    automático.
-   Prepararte para comprender los embeddings en las próximas secciones.

------------------------------------------------------------------------

# Introducción

Los seres humanos interpretamos el mundo mediante conceptos.

Leemos una palabra y evocamos una idea.

Observamos una imagen y reconocemos personas, objetos y contextos.

Las computadoras no poseen esa capacidad.

Para un procesador, una palabra no tiene significado hasta que puede
transformarse en una representación numérica.

Por ello, antes de que un modelo pueda aprender, toda la información
debe convertirse en números.

------------------------------------------------------------------------

# ¿Por qué números?

Los algoritmos de aprendizaje automático operan sobre operaciones
matemáticas.

Suman, multiplican, comparan y optimizan valores.

No pueden trabajar directamente con una palabra como **arquitectura** o
**software**.

Primero es necesario convertir esos conceptos en una estructura
matemática.

Esa estructura recibe el nombre de **vector**.

------------------------------------------------------------------------

# ¿Qué es un vector?

En el contexto de la IA, un vector es una colección ordenada de valores
numéricos que representa alguna característica de un objeto.

Ese objeto puede ser:

-   una palabra;
-   una oración;
-   un documento;
-   una imagen;
-   un sonido;
-   un usuario;
-   un producto.

Dos objetos similares deberían terminar representados por vectores
cercanos entre sí.

Esta idea constituye uno de los principios fundamentales de la IA
moderna.

------------------------------------------------------------------------

# Pensar en un espacio

Imaginemos un mapa.

Cada ciudad ocupa una posición determinada.

La distancia entre dos ciudades permite estimar qué tan cerca se
encuentran.

Los espacios vectoriales funcionan de manera similar.

Cada elemento ocupa una posición matemática.

La distancia entre dos vectores expresa el grado de similitud entre los
objetos representados.

No significa que "comprendan" el concepto.

Significa que poseen representaciones matemáticas con propiedades
comparables.

------------------------------------------------------------------------

# ¿Por qué esto es importante?

Una vez que la información se encuentra representada mediante vectores,
los modelos pueden:

-   comparar similitudes;
-   identificar agrupamientos;
-   detectar patrones;
-   recuperar información relacionada;
-   generar nuevas representaciones.

Sin esta etapa, técnicas modernas como los embeddings, la búsqueda
semántica o los Large Language Models serían imposibles.

------------------------------------------------------------------------

# Caso real

Supongamos un buscador documental dentro de una empresa.

Un usuario consulta:

> "licencia por maternidad"

Otro usuario escribe:

> "permiso por nacimiento"

Aunque las palabras sean diferentes, ambas consultas deberían conducir a
documentos similares.

Esto solo resulta posible si el sistema trabaja sobre representaciones
matemáticas del significado y no únicamente sobre coincidencias exactas
de texto.

------------------------------------------------------------------------

# Ideas clave

-   Los modelos no procesan conceptos directamente; procesan números.
-   Los vectores permiten representar información compleja en forma
    matemática.
-   La cercanía entre vectores expresa similitud, no identidad.
-   Esta representación constituye la base de gran parte de la IA
    moderna.

------------------------------------------------------------------------

## Próxima sección

Ahora estudiaremos cómo esas representaciones evolucionaron hasta
convertirse en los **embeddings**, uno de los conceptos más importantes
para comprender los Large Language Models y los sistemas RAG.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
