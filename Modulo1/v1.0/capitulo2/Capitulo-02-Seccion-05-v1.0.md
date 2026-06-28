# Capítulo 2 --- Sección 05 de 10

# Parámetros, pesos y el proceso de entrenamiento

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un modelo no almacena conocimiento como un libro. Lo distribuye
> entre millones o miles de millones de parámetros."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué son los parámetros de un modelo.
-   Diferenciar arquitectura, parámetros y datos de entrenamiento.
-   Entender cómo un modelo ajusta sus pesos durante el entrenamiento.
-   Comprender por qué entrenar e inferir son procesos diferentes.

------------------------------------------------------------------------

# Introducción

Cuando se afirma que un modelo posee 7.000 millones o 70.000 millones de
parámetros, suele interpretarse como una medida directa de inteligencia.

La realidad es más compleja.

La cantidad de parámetros representa la capacidad del modelo para
almacenar relaciones aprendidas, pero no garantiza mejores resultados
por sí sola.

Para comprender esta afirmación debemos analizar qué son realmente esos
parámetros.

------------------------------------------------------------------------

# ¿Qué es un parámetro?

Un parámetro es un valor numérico interno que participa en los cálculos
realizados por el modelo.

Durante el entrenamiento esos valores cambian millones de veces.

Cada modificación intenta reducir el error cometido al resolver una
tarea.

Al finalizar el entrenamiento, el conjunto completo de parámetros
constituye el conocimiento matemático del modelo.

No almacena frases completas.

No guarda respuestas preparadas.

Almacena relaciones estadísticas distribuidas entre todos sus
parámetros.

------------------------------------------------------------------------

# Arquitectura y parámetros

Es importante no confundir estos conceptos.

La **arquitectura** define cómo está construido el modelo.

Los **parámetros** representan los valores aprendidos por esa
arquitectura.

Una analogía útil consiste en pensar en un edificio.

Los planos indican la estructura del edificio.

Los parámetros serían la configuración concreta de cada uno de sus
componentes una vez terminada la construcción.

Dos modelos pueden compartir exactamente la misma arquitectura y
producir resultados muy distintos si fueron entrenados con datos
diferentes.

------------------------------------------------------------------------

# ¿Cómo aprende un modelo?

El entrenamiento puede resumirse en un ciclo repetitivo:

1.  Recibir un conjunto de ejemplos.
2.  Generar una predicción.
3.  Compararla con el resultado esperado.
4.  Calcular el error.
5.  Ajustar los parámetros para reducir ese error.
6.  Repetir el proceso millones de veces.

Cada iteración produce cambios muy pequeños.

Sin embargo, la acumulación de esos ajustes permite que el modelo
aprenda patrones extremadamente complejos.

``` mermaid
flowchart LR
A[Datos] --> B[Predicción]
B --> C[Cálculo del error]
C --> D[Ajuste de parámetros]
D --> A
```

------------------------------------------------------------------------

# Entrenamiento e inferencia

Conviene distinguir claramente dos etapas.

**Entrenamiento**

-   Requiere enormes volúmenes de datos.
-   Consume gran capacidad de procesamiento.
-   Modifica los parámetros.

**Inferencia**

-   Utiliza un modelo ya entrenado.
-   No altera sus parámetros.
-   Produce respuestas para nuevos datos de entrada.

La mayoría de los usuarios interactúa únicamente con la etapa de
inferencia.

------------------------------------------------------------------------

# Caso real

Una empresa utiliza un modelo fundacional para responder consultas
internas.

No lo entrena desde cero.

En cambio, reutiliza un modelo previamente entrenado y lo complementa
con documentación corporativa mediante RAG.

Esta decisión reduce costos y tiempos de implementación sin renunciar a
un alto nivel de calidad.

Comprender la diferencia entre entrenar e inferir permite justificar
arquitecturas mucho más eficientes.

------------------------------------------------------------------------

# Ideas clave

-   Los parámetros representan el conocimiento aprendido por el modelo.
-   Más parámetros implican mayor capacidad, no necesariamente mejores
    resultados.
-   Entrenar modifica parámetros; inferir utiliza esos parámetros.
-   La arquitectura y los datos son tan importantes como el tamaño del
    modelo.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos cómo surgieron las redes neuronales
modernas y por qué el mecanismo de atención (*Attention*) transformó por
completo la evolución de los modelos de lenguaje.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
