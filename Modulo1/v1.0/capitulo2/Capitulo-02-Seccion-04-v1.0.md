# Capítulo 2 --- Sección 04 de 10

# Embeddings: representando el significado mediante vectores

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Dos palabras pueden escribirse de forma diferente y, sin embargo,
> significar casi lo mismo. Los embeddings intentan capturar esa
> relación en un espacio matemático."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué es un embedding y por qué representa un avance
    respecto de las representaciones tradicionales.
-   Entender cómo un modelo transforma información en vectores con
    significado semántico.
-   Diferenciar similitud léxica de similitud semántica.
-   Comprender por qué los embeddings son la base de RAG, búsqueda
    semántica y sistemas modernos de recuperación de información.

------------------------------------------------------------------------

# Introducción

En la sección anterior vimos que una computadora necesita representar
toda la información mediante números.

Sin embargo, representar texto como simples valores numéricos no es
suficiente.

Consideremos las siguientes palabras:

-   automóvil
-   coche
-   vehículo

Para una persona resulta evidente que describen conceptos estrechamente
relacionados.

Para una computadora que únicamente compara caracteres, son tres
palabras completamente distintas.

Durante muchos años este fue uno de los principales obstáculos para
construir sistemas capaces de comprender lenguaje natural.

Los embeddings surgieron para reducir esa brecha.

------------------------------------------------------------------------

# El problema de las representaciones tradicionales

Las primeras técnicas de representación trataban cada palabra como un
símbolo independiente.

En ese enfoque:

-   "automóvil" no tenía relación matemática con "coche";
-   "doctor" era completamente diferente de "médico";
-   "programador" no compartía ninguna cercanía con "desarrollador".

El sistema solo podía reconocer coincidencias exactas.

Esto limitaba enormemente la capacidad de búsqueda y comprensión.

------------------------------------------------------------------------

# ¿Qué es un embedding?

Un embedding es una representación vectorial de un objeto que intenta
preservar su significado dentro de un espacio matemático.

Ese objeto puede ser:

-   una palabra;
-   una frase;
-   un documento;
-   una imagen;
-   un fragmento de código;
-   un audio.

La idea fundamental consiste en ubicar objetos con significados
similares en posiciones cercanas del espacio vectorial.

No importa únicamente cómo están escritos.

Importa lo que representan.

------------------------------------------------------------------------

# Una analogía

Imaginemos una biblioteca gigantesca.

En lugar de ordenar los libros por orden alfabético, decidimos ubicarlos
según su temática.

Los libros sobre bases de datos quedan próximos entre sí.

Los de arquitectura de software aparecen en otro sector.

Los relacionados con aprendizaje automático ocupan otra región.

Si un lector busca información sobre Docker, probablemente también
encuentre Kubernetes, contenedores y orquestación cerca de ese lugar.

Los embeddings funcionan de manera parecida.

La proximidad ya no depende de las palabras utilizadas.

Depende del significado aprendido por el modelo.

------------------------------------------------------------------------

# Espacios semánticos

Cuando millones de vectores se distribuyen en un espacio de alta
dimensión comienzan a aparecer agrupamientos naturales.

Conceptos relacionados terminan ocupando regiones cercanas.

Conceptos muy diferentes aparecen alejados.

Aunque un ser humano no pueda visualizar miles de dimensiones, los
algoritmos pueden calcular distancias entre esos vectores con enorme
precisión.

Estas distancias permiten responder preguntas como:

-   ¿Qué documento es más parecido a esta consulta?
-   ¿Qué productos presentan características similares?
-   ¿Qué respuesta previa se asemeja más a este problema?

------------------------------------------------------------------------

# ¿Cómo se generan?

Los embeddings no se construyen manualmente.

Se aprenden durante el entrenamiento del modelo.

Mientras el algoritmo intenta resolver tareas relacionadas con lenguaje,
imágenes o cualquier otro dominio, ajusta progresivamente las posiciones
de los vectores.

Con el tiempo, esas posiciones comienzan a reflejar relaciones
semánticas presentes en los datos.

Por ese motivo, dos modelos distintos pueden producir embeddings
diferentes para el mismo texto.

La calidad dependerá del entrenamiento, de los datos utilizados y del
objetivo para el cual fueron diseñados.

------------------------------------------------------------------------

# Caso real

Supongamos que una empresa posee cien mil documentos internos.

Un empleado realiza la siguiente consulta:

> "¿Cómo solicitar licencia por nacimiento?"

Ningún documento contiene exactamente esa frase.

Sin embargo, existen procedimientos titulados:

-   Licencia por maternidad.
-   Licencia por paternidad.
-   Permisos familiares.

Gracias a los embeddings, el sistema puede recuperar esos documentos
aunque las palabras utilizadas no coincidan exactamente con la consulta.

La búsqueda deja de ser textual y pasa a ser semántica.

------------------------------------------------------------------------

# Ideas clave

-   Un embedding es un vector que representa significado.
-   Objetos similares ocupan posiciones cercanas en el espacio
    vectorial.
-   La similitud deja de depender exclusivamente de coincidencias
    exactas de palabras.
-   Los embeddings constituyen uno de los pilares de la IA moderna.

------------------------------------------------------------------------

## Próxima sección

Ahora que comprendemos cómo representar significado mediante vectores,
estudiaremos cómo los modelos aprenden esas representaciones ajustando
millones de parámetros durante el entrenamiento.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
