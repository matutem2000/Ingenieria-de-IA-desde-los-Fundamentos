# Ingeniería de IA desde los Fundamentos

# Módulo I --- Los Fundamentos de la Inteligencia Artificial

# Capítulo 6 --- Transformers

**Versión:** 0.1 (Primer borrador editorial)

------------------------------------------------------------------------

# Objetivos

Al finalizar este capítulo deberías poder:

-   Comprender por qué nació la arquitectura Transformer.
-   Explicar qué problema resolvía respecto a arquitecturas anteriores.
-   Entender conceptualmente qué es la atención (*Attention*).
-   Relacionar Transformers con los LLM modernos.
-   Explicar por qué este avance cambió la historia de la IA.

------------------------------------------------------------------------

# Introducción

Si tuviéramos que elegir un único avance responsable de la explosión de
la IA generativa, probablemente sería la arquitectura **Transformer**.

Modelos como ChatGPT, Claude, Gemini, Llama, Qwen o Gemma tienen
diferencias importantes, pero todos comparten una misma idea
fundamental: procesar el lenguaje utilizando mecanismos de atención.

Para comprender por qué esto fue revolucionario primero debemos entender
el problema.

------------------------------------------------------------------------

# El problema del lenguaje

Las personas no interpretamos una oración palabra por palabra de forma
aislada.

Comprendemos una palabra gracias al contexto.

En la frase:

> "El banco cerró temprano."

¿Se refiere a una entidad financiera o a un banco de plaza?

La respuesta depende del resto de la oración.

Las arquitecturas anteriores tenían dificultades para mantener ese
contexto cuando el texto era largo.

------------------------------------------------------------------------

# Antes de Transformers

Durante muchos años se utilizaron redes recurrentes (RNN) y
posteriormente LSTM y GRU.

Funcionaban razonablemente bien para secuencias cortas.

Sin embargo presentaban varios inconvenientes:

-   procesamiento secuencial;
-   dificultad para recordar información lejana;
-   entrenamiento lento;
-   escasa paralelización.

La industria necesitaba una arquitectura diferente.

------------------------------------------------------------------------

# La idea que cambió todo

En 2017 un grupo de investigadores publicó el trabajo:

> **Attention Is All You Need**

La propuesta era sorprendente.

En lugar de recorrer una oración palabra por palabra, el modelo podía
observar simultáneamente todas las palabras y calcular cuáles eran
relevantes para interpretar cada una de ellas.

A este mecanismo se lo conoce como **Attention**.

------------------------------------------------------------------------

# ¿Qué es Attention?

Imaginemos que leemos la siguiente oración:

> "El perro persiguió al gato porque estaba asustado."

Cuando llegamos a "estaba", automáticamente buscamos en la oración qué
elemento tiene sentido relacionar con ese estado.

Nuestro cerebro presta más atención a determinadas palabras que a otras.

Transformer intenta hacer algo conceptualmente parecido.

No todas las palabras tienen la misma importancia para interpretar una
determinada posición.

El mecanismo de atención asigna distintos pesos a cada relación.

------------------------------------------------------------------------

# Una analogía

Imaginá una reunión con diez personas.

Si querés entender lo que dice una de ellas, no escuchás con la misma
intensidad a todos.

Prestás más atención a quienes aportan información relevante.

Transformer hace algo similar con las palabras de un texto.

------------------------------------------------------------------------

# ¿Por qué fue revolucionario?

Gracias a este enfoque se obtuvieron varias ventajas:

-   procesamiento paralelo;
-   mejor aprovechamiento del hardware;
-   comprensión de relaciones lejanas;
-   entrenamiento sobre cantidades enormes de texto;
-   mejor escalabilidad.

Estas características permitieron entrenar modelos cada vez más grandes.

------------------------------------------------------------------------

# ¿Dónde aparecen los Transformers?

Actualmente se utilizan en:

-   modelos de lenguaje;
-   generación de imágenes;
-   reconocimiento de voz;
-   visión por computadora;
-   biología computacional;
-   robótica.

Aunque nacieron para lenguaje natural, su impacto alcanzó numerosos
dominios.

------------------------------------------------------------------------

# Relación con los LLM

Un Large Language Model puede entenderse, de forma simplificada, como:

``` text
Grandes cantidades de texto
            +
Arquitectura Transformer
            +
Entrenamiento masivo
            =
Modelo de Lenguaje
```

Transformer no es el modelo completo.

Es la arquitectura sobre la cual se construye.

------------------------------------------------------------------------

# Conversación con un arquitecto

**Desarrollador**

"¿ChatGPT y Claude funcionan completamente distinto?"

**Arquitecto**

"No necesariamente. Muchos modelos comparten fundamentos arquitectónicos
similares. Lo que cambia son el entrenamiento, los datos, el tamaño, el
ajuste fino y las decisiones de ingeniería."

Comprender esto evita pensar que cada modelo pertenece a un universo
completamente diferente.

------------------------------------------------------------------------

# Ideas clave

-   Transformer resolvió limitaciones importantes de arquitecturas
    anteriores.
-   El mecanismo de atención permite utilizar mejor el contexto.
-   La paralelización posibilitó entrenar modelos mucho más grandes.
-   Los LLM modernos se apoyan en esta arquitectura.

------------------------------------------------------------------------

# Laboratorio

1.  Elegí un párrafo largo.
2.  Marcá las palabras indispensables para comprender cada oración.
3.  Reflexioná por qué algunas palabras aportan mucho contexto y otras
    muy poco.
4.  Relacioná esa idea con el concepto de atención.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Comprender contexto implica comprender significado?
-   ¿Puede un mecanismo estadístico producir respuestas
    sorprendentemente útiles?
-   ¿Qué limitaciones siguen existiendo incluso con Transformers?

------------------------------------------------------------------------

# Resumen

Transformer cambió el rumbo de la Inteligencia Artificial al introducir
una forma mucho más eficiente de procesar secuencias.

Su mecanismo de atención permitió aprovechar mejor el contexto, escalar
el entrenamiento y sentar las bases de los modelos de lenguaje actuales.

Sin Transformer difícilmente existirían los asistentes de IA que hoy
utilizamos.

------------------------------------------------------------------------

# Lo que un arquitecto debería recordar

-   Transformer es una arquitectura, no un producto.
-   Attention explica gran parte de la capacidad de comprender contexto.
-   El éxito de los LLM modernos depende tanto de la arquitectura como
    del entrenamiento y los datos.
-   Comprender los fundamentos evita caer en explicaciones simplistas
    sobre "magia" o "inteligencia".

------------------------------------------------------------------------

# Próximo capítulo

**Capítulo 7 --- Large Language Models**

Analizaremos cómo funcionan conceptualmente los LLM, qué hacen realmente
cuando generan texto y cuáles son sus fortalezas y limitaciones.

> "Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones."
