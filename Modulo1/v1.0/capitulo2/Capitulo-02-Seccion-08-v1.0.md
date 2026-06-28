# Capítulo 2 --- Sección 08 de 10

# Tokenización: cómo leen los modelos de lenguaje

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un modelo de lenguaje no procesa palabras ni caracteres. Procesa
> tokens."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué es un token y por qué es la unidad básica de
    procesamiento de un LLM.
-   Diferenciar caracteres, palabras y tokens.
-   Entender la relación entre tokenización, ventana de contexto y
    costo.
-   Identificar el impacto arquitectónico de la cantidad de tokens.

------------------------------------------------------------------------

# Introducción

Cuando un usuario escribe una consulta en un chatbot, suele pensar que
el modelo lee exactamente las mismas palabras que aparecen en pantalla.

No ocurre así.

Antes de que el modelo pueda procesar un texto, este debe transformarse
en una secuencia de unidades llamadas **tokens**.

La tokenización constituye el primer paso de prácticamente todos los
modelos modernos de lenguaje.

------------------------------------------------------------------------

# ¿Qué es un token?

Un token es una unidad de información utilizada por el modelo durante el
procesamiento.

Dependiendo del algoritmo de tokenización, un token puede representar:

-   una palabra completa;
-   parte de una palabra;
-   un signo de puntuación;
-   un número;
-   un espacio;
-   un carácter especial.

Por ejemplo, la palabra **internacionalización** podría dividirse en
varios tokens, mientras que palabras muy frecuentes podrían corresponder
a un único token.

Por este motivo no existe una equivalencia fija entre palabras y tokens.

------------------------------------------------------------------------

# ¿Por qué no utilizar palabras?

Si cada idioma tuviera un vocabulario limitado y estable, trabajar con
palabras sería suficiente.

Sin embargo, el lenguaje natural presenta desafíos importantes:

-   aparecen palabras nuevas constantemente;
-   existen nombres propios y términos técnicos;
-   distintos idiomas comparten fragmentos comunes;
-   una misma raíz puede generar muchas variantes.

Dividir el texto en fragmentos reutilizables permite representar de
manera más eficiente un vocabulario prácticamente ilimitado.

------------------------------------------------------------------------

# Del texto a los números

Una vez tokenizado el texto, cada token recibe un identificador
numérico.

Posteriormente esos identificadores se transforman en embeddings y
continúan recorriendo las distintas capas del modelo.

El proceso puede resumirse así:

``` mermaid
flowchart LR
A[Texto] --> B[Tokenización]
B --> C[Identificadores]
C --> D[Embeddings]
D --> E[Transformer]
E --> F[Respuesta]
```

Aunque para el usuario todo sucede en una fracción de segundo,
internamente el modelo nunca trabaja directamente con palabras.

------------------------------------------------------------------------

# Tokens y ventana de contexto

La tokenización también determina cuánto contenido puede procesar un
modelo simultáneamente.

La **ventana de contexto** define el número máximo de tokens que el
modelo puede considerar durante una interacción.

Dentro de ese límite se incluyen:

-   el mensaje del usuario;
-   las instrucciones del sistema;
-   el historial de la conversación;
-   documentos adicionales;
-   la respuesta que generará el modelo.

Cuando el límite se alcanza, parte del contexto debe descartarse o
resumirse.

------------------------------------------------------------------------

# Impacto en costos y rendimiento

En la mayoría de los servicios comerciales el consumo se mide en tokens.

Esto tiene consecuencias directas para la arquitectura.

Un sistema que envía documentos completos en cada consulta consumirá
muchos más recursos que otro que recupera únicamente los fragmentos
relevantes.

Por esta razón, comprender la tokenización resulta esencial para diseñar
soluciones eficientes, especialmente cuando se utilizan técnicas como
RAG.

------------------------------------------------------------------------

# Caso real

Una organización incorpora un asistente documental.

En la primera versión, cada consulta envía manuales completos de cientos
de páginas al modelo.

Los costos aumentan rápidamente y la latencia se vuelve inaceptable.

Al reemplazar esa estrategia por una búsqueda semántica que recupera
únicamente los fragmentos relevantes, la cantidad de tokens disminuye de
forma significativa, mejorando tanto el rendimiento como el costo
operativo.

El cambio no consistió en utilizar un modelo diferente.

Consistió en diseñar mejor la arquitectura.

------------------------------------------------------------------------

# Ideas clave

-   Los modelos procesan tokens, no palabras.
-   La cantidad de tokens determina el tamaño del contexto disponible.
-   El consumo de tokens influye directamente en costos y rendimiento.
-   Comprender la tokenización permite tomar mejores decisiones
    arquitectónicas.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos la **ventana de contexto**, sus
limitaciones y por qué este concepto impulsó el desarrollo de
arquitecturas como Retrieval-Augmented Generation (RAG).

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
