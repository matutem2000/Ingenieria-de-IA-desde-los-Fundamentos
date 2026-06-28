# Capítulo 2 --- Sección 02 de 10

# Los datos: la materia prima del aprendizaje

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un modelo nunca aprende directamente del mundo. Aprende de la
> representación del mundo contenida en los datos."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender por qué los datos determinan el límite superior de un
    modelo.
-   Diferenciar dato, característica (*feature*) y etiqueta (*label*).
-   Entender la relación entre calidad de datos y calidad del
    aprendizaje.
-   Identificar los principales problemas que aparecen antes del
    entrenamiento.

------------------------------------------------------------------------

# Introducción

Cuando hablamos de entrenamiento es fácil imaginar que un modelo
"absorbe conocimiento" de manera automática.

En realidad, el proceso depende completamente de los datos disponibles.

Un modelo no observa la realidad.

No comprende el contexto de una organización.

No conoce las intenciones de las personas.

Únicamente procesa ejemplos.

Por ello, la calidad del aprendizaje nunca puede superar la calidad de
los datos utilizados.

------------------------------------------------------------------------

# ¿Qué son los datos de entrenamiento?

Los datos de entrenamiento constituyen el conjunto de ejemplos que un
algoritmo utiliza para descubrir patrones.

Cada ejemplo representa una observación del problema que deseamos
resolver.

Si queremos clasificar correos electrónicos, necesitaremos miles o
millones de mensajes previamente clasificados.

Si queremos reconocer objetos en imágenes, necesitaremos imágenes
correctamente etiquetadas.

El objetivo no es memorizar ejemplos, sino aprender relaciones que
permitan generalizar a situaciones nuevas.

------------------------------------------------------------------------

# Features y labels

En aprendizaje supervisado aparecen dos conceptos fundamentales.

-   **Feature:** información utilizada para describir un ejemplo.
-   **Label:** resultado esperado para ese ejemplo.

Supongamos un sistema capaz de detectar correos no deseados.

Las palabras presentes en el mensaje, el remitente o la cantidad de
enlaces pueden formar parte de las *features*.

La clasificación "spam" o "no spam" constituye la *label*.

El entrenamiento consiste en aprender la relación entre ambas.

------------------------------------------------------------------------

# Calidad antes que cantidad

Existe la creencia de que disponer de más datos siempre produce mejores
modelos.

La realidad es más matizada.

Duplicados, errores, sesgos, información obsoleta o registros
inconsistentes pueden deteriorar significativamente el desempeño.

Por ese motivo, una parte importante del trabajo en proyectos reales
consiste en limpiar, validar y gobernar los datos antes del
entrenamiento.

------------------------------------------------------------------------

# Caso real

Una empresa desea predecir qué clientes abandonarán un servicio.

El equipo consigue millones de registros históricos.

Sin embargo, descubre que durante varios años el criterio utilizado para
registrar las bajas cambió en distintas sucursales.

Antes de entrenar cualquier modelo es necesario normalizar esa
información.

El desafío no es matemático.

Es ingenieril.

------------------------------------------------------------------------

# Ideas clave

-   Los modelos aprenden únicamente de los ejemplos disponibles.
-   La calidad de los datos condiciona la calidad del resultado.
-   Preparar datos suele consumir más esfuerzo que entrenar el modelo.
-   Un arquitecto debe considerar el gobierno de datos como parte de la
    arquitectura.

------------------------------------------------------------------------

## Próxima sección

Ahora que comprendemos el papel de los datos, estudiaremos cómo una
computadora transforma palabras, imágenes o números en representaciones
matemáticas capaces de ser procesadas por un modelo.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
