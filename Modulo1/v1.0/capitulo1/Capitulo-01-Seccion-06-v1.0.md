# Capítulo 1 --- Sección 06 de 10

# Pensar en probabilidades: un cambio de paradigma

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"El software tradicional busca respuestas correctas. La Inteligencia
> Artificial busca respuestas suficientemente buenas con un nivel de
> confianza conocido."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender la diferencia entre sistemas determinísticos y
    probabilísticos.
-   Entender por qué un modelo de IA nunca garantiza respuestas
    perfectas.
-   Incorporar el concepto de incertidumbre como parte del diseño de
    soluciones.
-   Comprender por qué evaluar un sistema de IA requiere métricas
    diferentes a las del software clásico.

------------------------------------------------------------------------

# Introducción

La mayor parte del software que desarrollamos durante décadas fue
determinístico.

Con los mismos datos de entrada siempre obteníamos exactamente el mismo
resultado.

Si una función calcula el IVA de una factura, esperamos que el resultado
sea idéntico cada vez que se ejecuta.

Ese comportamiento resulta ideal para procesos donde las reglas son
completamente conocidas.

La Inteligencia Artificial introduce un paradigma diferente.

En muchos problemas no existe una única respuesta correcta.

Existen respuestas con distintos grados de probabilidad.

------------------------------------------------------------------------

# Software tradicional versus IA

En un sistema clásico podemos escribir reglas como:

-   Si el usuario ingresó una contraseña válida, permitir el acceso.
-   Si el saldo es menor que cero, rechazar la operación.

Estas reglas producen resultados previsibles.

En cambio, responder preguntas en lenguaje natural, resumir documentos o
clasificar imágenes requiere interpretar información ambigua.

No siempre existe una única solución correcta.

El modelo estima cuál es la respuesta más probable según el conocimiento
adquirido durante el entrenamiento.

------------------------------------------------------------------------

# ¿Qué significa "probabilidad"?

Cuando un modelo genera una respuesta, no recupera una frase almacenada
en una base de datos.

Evalúa millones o miles de millones de parámetros aprendidos durante el
entrenamiento para estimar cuál debería ser el siguiente elemento de la
secuencia.

Ese proceso es estadístico.

Por ese motivo pueden existir varias respuestas razonables para una
misma pregunta.

La calidad del sistema depende de qué tan cerca se encuentre la
respuesta generada de la solución esperada para el problema.

------------------------------------------------------------------------

# Implicancias para un arquitecto

Este cambio tiene consecuencias importantes.

No alcanza con preguntar si el sistema funciona.

También debemos preguntarnos:

-   ¿Con qué frecuencia se equivoca?
-   ¿Qué impacto tiene un error?
-   ¿Cómo detectaremos respuestas incorrectas?
-   ¿Debe existir supervisión humana?
-   ¿Cómo mediremos la calidad del sistema en producción?

Estas preguntas forman parte del diseño arquitectónico y no pueden
resolverse únicamente ajustando un modelo.

------------------------------------------------------------------------

# Caso real

Un asistente jurídico resume expedientes para acelerar el trabajo de un
equipo legal.

Aunque el modelo acierta en la mayoría de los casos, ocasionalmente
omite información relevante.

La solución no consiste únicamente en cambiar de modelo.

El sistema debe incorporar validaciones, trazabilidad de las fuentes y
revisión humana cuando el riesgo lo justifique.

La arquitectura completa es la que determina la confiabilidad del
producto.

------------------------------------------------------------------------

# Resumen

Comprender que la IA trabaja sobre probabilidades modifica la manera de
diseñar software.

El objetivo deja de ser eliminar completamente los errores y pasa a ser
gestionarlos mediante una arquitectura adecuada, métricas de calidad y
procesos de validación.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
