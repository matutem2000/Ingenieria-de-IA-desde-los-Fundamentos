# Capítulo 3 --- Sección 04 de 10

# Modelos de Embeddings: el motor silencioso de un sistema RAG

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"En un sistema RAG, la calidad de la recuperación depende mucho más
> de los embeddings de lo que la mayoría de los equipos imagina."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué hace un modelo de embeddings.
-   Diferenciar un modelo de embeddings de un LLM.
-   Conocer los principales criterios para seleccionar un modelo de
    embeddings.
-   Entender el impacto de esa elección sobre la precisión del sistema.

------------------------------------------------------------------------

# Introducción

Cuando se habla de Inteligencia Artificial generativa, casi toda la
atención se concentra en el Large Language Model.

Sin embargo, en una arquitectura RAG existe otro componente igualmente
importante: el modelo encargado de generar los embeddings.

Si los embeddings representan incorrectamente el significado de los
documentos, la búsqueda semántica devolverá resultados poco relevantes y
el LLM responderá utilizando un contexto deficiente.

En consecuencia, una mala recuperación rara vez puede compensarse con un
mejor modelo generativo.

------------------------------------------------------------------------

# ¿Qué hace un modelo de embeddings?

Su función consiste en transformar un contenido en un vector numérico
que preserve, en la mayor medida posible, su significado.

Ese contenido puede ser:

-   una palabra;
-   una oración;
-   un párrafo;
-   un documento completo;
-   código fuente;
-   imágenes o audio, dependiendo del modelo.

Una vez generado el vector, la comparación entre documentos deja de
depender de coincidencias textuales y pasa a basarse en cercanía
semántica.

------------------------------------------------------------------------

# Un modelo diferente al LLM

Aunque ambos trabajan con lenguaje, cumplen objetivos distintos.

  -----------------------------------------------------------------------
  Componente            Responsabilidad principal
  --------------------- -------------------------------------------------
  Modelo de Embeddings  Representar significado mediante vectores.

  Large Language Model  Comprender el contexto y generar una respuesta.
  -----------------------------------------------------------------------

En muchos proyectos ambos modelos son completamente diferentes.

Incluso pueden provenir de proveedores distintos.

Esta separación permite optimizar costos y rendimiento sin afectar toda
la arquitectura.

------------------------------------------------------------------------

# ¿Cómo elegir un modelo?

No existe un modelo universalmente mejor.

La elección depende del problema.

Algunos criterios habituales son:

-   idioma soportado;
-   dominio del conocimiento;
-   longitud máxima del texto;
-   precisión en búsqueda semántica;
-   velocidad de inferencia;
-   consumo de memoria;
-   costo de operación;
-   posibilidad de ejecutarlo localmente.

Un arquitecto evalúa estos factores antes de seleccionar una tecnología.

------------------------------------------------------------------------

# Reentrenar o reutilizar

En la mayoría de las implementaciones empresariales no resulta necesario
entrenar un modelo de embeddings desde cero.

Es mucho más habitual reutilizar modelos previamente entrenados y
concentrar el esfuerzo en la calidad de los documentos, el *chunking* y
la estrategia de recuperación.

Solo en dominios altamente especializados suele justificarse un
entrenamiento o ajuste adicional.

------------------------------------------------------------------------

# Caso de estudio

Una organización dispone de dos sistemas RAG.

Ambos utilizan exactamente el mismo LLM.

El primero genera embeddings con un modelo optimizado para inglés.

El segundo utiliza un modelo entrenado específicamente para español.

Las consultas realizadas en español muestran diferencias significativas
en la recuperación de documentos.

El cambio no estuvo en el modelo generativo.

Estuvo en la representación semántica utilizada para indexar el
conocimiento.

------------------------------------------------------------------------

# Buenas prácticas

-   Utilizar el mismo modelo de embeddings para indexación y búsqueda.
-   Evitar mezclar espacios vectoriales incompatibles.
-   Evaluar la calidad mediante conjuntos de consultas reales.
-   Medir precisión antes de reemplazar un modelo.
-   Versionar el proceso de indexación cuando cambie el modelo de
    embeddings.

------------------------------------------------------------------------

# Ideas clave

-   El modelo de embeddings determina la calidad de la recuperación.
-   Embeddings y LLM cumplen funciones diferentes.
-   Elegir correctamente el modelo de embeddings puede producir mejoras
    superiores a cambiar de LLM.
-   La evaluación debe realizarse con datos representativos del dominio.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos las bases de datos vectoriales,
cómo almacenan millones de embeddings y cómo realizan búsquedas
eficientes sobre espacios de alta dimensión.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
