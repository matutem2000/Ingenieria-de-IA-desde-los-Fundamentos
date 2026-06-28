# Ingeniería de IA desde los Fundamentos

# Módulo I --- Los Fundamentos de la Inteligencia Artificial

# Capítulo 8 --- Tokens

**Versión:** 0.1 (Primer borrador editorial)

------------------------------------------------------------------------

# Objetivos

Al finalizar este capítulo deberías poder:

-   Explicar qué es un token.
-   Comprender por qué los LLM trabajan con tokens y no con palabras.
-   Entender cómo los tokens afectan el costo, la velocidad y el
    contexto.
-   Saber estimar el impacto de los tokens al diseñar una solución con
    IA.

------------------------------------------------------------------------

# Introducción

Cuando utilizamos un asistente como ChatGPT o Claude solemos pensar que
el modelo procesa palabras.

En realidad, los modelos trabajan con una unidad más pequeña llamada
**token**.

Comprender este concepto resulta fundamental porque prácticamente todo
en un LLM depende de él:

-   el costo;
-   la velocidad;
-   la memoria utilizada;
-   la ventana de contexto;
-   la longitud máxima de las respuestas.

------------------------------------------------------------------------

# ¿Qué es un token?

Un token es la unidad mínima con la que el modelo representa el texto.

No siempre coincide con una palabra.

Según el idioma y el algoritmo de tokenización, un token puede
representar:

-   una palabra completa;
-   parte de una palabra;
-   un signo de puntuación;
-   un número;
-   un espacio;
-   incluso varios caracteres juntos.

El modelo no "ve" letras ni palabras como nosotros.

Ve secuencias de tokens.

------------------------------------------------------------------------

# ¿Por qué no usar palabras?

Porque distintos idiomas tienen estructuras diferentes.

Si el modelo trabajara únicamente con palabras completas, el vocabulario
sería inmenso y poco flexible.

La tokenización permite representar millones de textos utilizando un
conjunto mucho más manejable de unidades.

También facilita procesar palabras desconocidas dividiéndolas en partes
conocidas.

------------------------------------------------------------------------

# Un ejemplo conceptual

Supongamos la frase:

> "La inteligencia artificial está cambiando el mundo."

El modelo podría dividirla conceptualmente en varios tokens.

No importa memorizar exactamente cómo lo hace cada proveedor.

Lo importante es comprender que la longitud que nosotros percibimos no
coincide necesariamente con la cantidad de tokens.

------------------------------------------------------------------------

# ¿Por qué los tokens importan?

## Contexto

Los modelos tienen un límite máximo de tokens que pueden procesar
simultáneamente.

Cuando ese límite se supera, parte del contexto debe descartarse.

## Costo

La mayoría de las APIs comerciales cobran por cantidad de tokens
procesados.

Más tokens significan mayor costo.

## Rendimiento

Procesar una conversación extensa requiere más memoria y mayor tiempo de
cálculo.

------------------------------------------------------------------------

# Tokens de entrada y salida

Conviene distinguir dos conceptos.

## Tokens de entrada

Son los que enviamos al modelo.

Incluyen:

-   prompt;
-   instrucciones;
-   historial de conversación;
-   documentos incorporados al contexto.

## Tokens de salida

Son los que genera el modelo como respuesta.

En muchos proveedores ambos tipos de tokens tienen costos diferentes.

------------------------------------------------------------------------

# Conversación con un arquitecto

**Desarrollador**

"El modelo es muy caro."

**Arquitecto**

"¿Cuántos tokens estás enviando en cada solicitud?"

En muchos proyectos el problema no es el modelo elegido.

Es el tamaño innecesario del contexto.

Optimizar prompts y contexto suele reducir costos significativamente.

------------------------------------------------------------------------

# Tokens y arquitectura

Supongamos un sistema RAG.

Cada consulta incorpora:

-   prompt del sistema;
-   historial;
-   documentos recuperados;
-   pregunta del usuario.

Todo eso consume tokens.

Diseñar correctamente un sistema implica decidir qué información
realmente necesita el modelo.

Más contexto no siempre significa mejores respuestas.

------------------------------------------------------------------------

# Ideas clave

-   Los modelos trabajan con tokens y no con palabras.
-   Los tokens determinan costos, velocidad y capacidad de contexto.
-   Optimizar el uso de tokens forma parte del trabajo del arquitecto.
-   Comprender la tokenización ayuda a diseñar soluciones más
    eficientes.

------------------------------------------------------------------------

# Laboratorio

1.  Elegí tres prompts de distinta longitud.
2.  Estimá cuál consumirá más tokens.
3.  Eliminá información redundante.
4.  Compará la calidad de la respuesta antes y después.

Reflexioná si toda la información enviada era realmente necesaria.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Más contexto siempre mejora la respuesta?
-   ¿Qué impacto económico tiene una mala gestión de tokens?
-   ¿Qué estrategias podrían reducir el consumo sin perder calidad?

------------------------------------------------------------------------

# Resumen

Los tokens son la unidad fundamental con la que trabajan los modelos de
lenguaje.

Aunque el usuario interactúe mediante texto natural, internamente todo
se representa como secuencias de tokens.

Comprender este concepto permite explicar fenómenos como los límites de
contexto, el costo de las APIs y la velocidad de inferencia.

------------------------------------------------------------------------

# Lo que un arquitecto debería recordar

-   Pensar siempre en tokens, no solamente en palabras.
-   Diseñar prompts eficientes.
-   Evitar enviar contexto innecesario.
-   Considerar el costo de entrada y salida al estimar una solución.

------------------------------------------------------------------------

# Próximo capítulo

**Capítulo 9 --- Ventana de Contexto**

Estudiaremos cómo los modelos utilizan los tokens disponibles y qué
ocurre cuando el contexto supera el límite permitido.

> "Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones."
