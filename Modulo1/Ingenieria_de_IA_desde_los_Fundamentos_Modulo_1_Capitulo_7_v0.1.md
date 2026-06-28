# Ingeniería de IA desde los Fundamentos

# Módulo I --- Los Fundamentos de la Inteligencia Artificial

# Capítulo 7 --- Large Language Models (LLM)

**Versión:** 0.1 (Primer borrador editorial)

------------------------------------------------------------------------

# Objetivos del capítulo

Al finalizar este capítulo deberías poder:

-   Explicar qué es un Large Language Model.
-   Comprender cómo un LLM genera texto de manera conceptual.
-   Diferenciar un modelo de una aplicación que utiliza un modelo.
-   Entender por qué un LLM no "piensa" como una persona.
-   Identificar las fortalezas y limitaciones de estos modelos.

------------------------------------------------------------------------

# Introducción

Llegamos al punto donde confluyen muchos de los conceptos estudiados
hasta ahora.

Los modelos de lenguaje de gran tamaño, conocidos como **Large Language
Models (LLM)**, son la tecnología que hizo posible asistentes como
ChatGPT, Claude, Gemini o Copilot.

Sin embargo, existe una confusión muy frecuente.

Muchas personas creen que ChatGPT es un modelo.

No lo es.

ChatGPT es una aplicación que utiliza uno o varios modelos de lenguaje
desarrollados por OpenAI.

Del mismo modo, Claude es una aplicación construida sobre modelos
desarrollados por Anthropic.

Comprender esta diferencia evita muchos malentendidos.

------------------------------------------------------------------------

# ¿Qué es un LLM?

Un LLM es un modelo matemático entrenado con enormes cantidades de texto
para aprender relaciones estadísticas entre palabras, frases e ideas.

Su objetivo durante el entrenamiento no es memorizar respuestas.

Su objetivo principal consiste en aprender a predecir cuál es el
siguiente token más probable dadas las entradas anteriores.

Esa idea aparentemente sencilla produce resultados sorprendentemente
útiles.

------------------------------------------------------------------------

# ¿Cómo genera texto?

Cuando escribimos un prompt, el modelo no busca una respuesta
almacenada.

Tampoco consulta automáticamente Internet.

Conceptualmente realiza un proceso similar al siguiente:

1.  Recibe la secuencia de tokens.
2.  Analiza el contexto mediante la arquitectura Transformer.
3.  Calcula probabilidades para el siguiente token.
4.  Selecciona uno de ellos.
5.  Incorpora ese token al contexto.
6.  Repite el proceso hasta completar la respuesta.

Cada palabra se genera una después de la otra.

------------------------------------------------------------------------

# Predicción no significa comprensión

Aquí aparece uno de los conceptos más importantes del libro.

Un LLM produce texto extremadamente convincente.

Eso no implica necesariamente que comprenda el mundo como lo hace una
persona.

El modelo aprende patrones presentes en enormes cantidades de
información.

Es capaz de relacionar conceptos, resumir documentos, escribir código o
responder preguntas porque esas capacidades emergen del entrenamiento.

Sin embargo, no posee experiencias, conciencia ni intención propia.

------------------------------------------------------------------------

# ¿Por qué parecen tan inteligentes?

Existen varias razones.

-   Fueron entrenados con cantidades gigantescas de información.
-   La arquitectura Transformer aprovecha muy bien el contexto.
-   Los modelos modernos contienen miles de millones de parámetros.
-   El entrenamiento incluye enormes recursos computacionales.

El resultado es un sistema capaz de producir respuestas de gran calidad
en numerosos dominios.

------------------------------------------------------------------------

# Modelo, aplicación y agente

Es importante distinguir estos conceptos.

## Modelo

Es el LLM propiamente dicho.

## Aplicación

Es el software que permite interactuar con el modelo.

Por ejemplo:

-   ChatGPT.
-   Claude.
-   Gemini.
-   Interfaces propias.

## Agente

Es una aplicación que, además del modelo, incorpora herramientas,
memoria, planificación y capacidad para ejecutar acciones.

Esta diferencia será fundamental más adelante.

------------------------------------------------------------------------

# ¿Qué puede hacer un LLM?

-   Responder preguntas.
-   Resumir documentos.
-   Traducir idiomas.
-   Escribir código.
-   Explicar conceptos.
-   Analizar texto.
-   Generar ideas.
-   Clasificar información.

------------------------------------------------------------------------

# ¿Qué no puede garantizar?

-   Que toda respuesta sea correcta.
-   Que toda información esté actualizada.
-   Que comprenda el mundo físico.
-   Que razone exactamente igual que una persona.
-   Que no produzca alucinaciones.

Por eso el criterio humano continúa siendo indispensable.

------------------------------------------------------------------------

# Conversación con un arquitecto

**Usuario**

"El modelo dijo que esto es cierto."

**Arquitecto**

"Que el modelo lo afirme no significa que sea correcto. La confianza
nunca reemplaza la validación."

Este principio será especialmente importante cuando trabajemos con
aplicaciones críticas.

------------------------------------------------------------------------

# LLM no significa IA General

Los modelos actuales son extraordinariamente capaces.

Sin embargo, fueron diseñados para resolver determinadas clases de
problemas.

No poseen objetivos propios.

No tienen conciencia.

No desarrollan deseos.

No aprenden continuamente durante cada conversación.

Estas diferencias suelen perderse en el debate público.

------------------------------------------------------------------------

# Caso aplicado

Imaginemos un sistema de soporte técnico.

El LLM interpreta preguntas escritas en lenguaje natural.

Busca información relevante.

Genera una respuesta.

El verdadero valor del sistema no depende únicamente del modelo.

Depende de toda la arquitectura que lo rodea.

En capítulos posteriores estudiaremos cómo construir esas arquitecturas.

------------------------------------------------------------------------

# Ideas clave

-   Un LLM es un modelo, no una aplicación.
-   Su funcionamiento se basa en predicción de tokens.
-   El contexto es esencial para producir respuestas útiles.
-   La calidad del resultado depende del entrenamiento, los datos y la
    arquitectura.

------------------------------------------------------------------------

# Laboratorio

Compará tres asistentes distintos.

Para una misma pregunta analizá:

-   claridad;
-   precisión;
-   velocidad;
-   capacidad de explicación;
-   manejo del contexto.

No busques determinar cuál es "el mejor".

Intentá descubrir para qué tipo de tareas destaca cada uno.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Puede un sistema predecir texto sin comprender el mundo?
-   ¿Por qué algunas respuestas parecen extremadamente inteligentes?
-   ¿Qué papel continúa teniendo el profesional humano?

------------------------------------------------------------------------

# Resumen

Los Large Language Models representan una de las aplicaciones más
exitosas del Deep Learning y de la arquitectura Transformer.

Su capacidad para generar lenguaje natural cambió profundamente la
interacción entre las personas y el software.

Sin embargo, comprender qué hacen realmente y cuáles son sus límites
resulta esencial para utilizarlos de manera responsable y diseñar
soluciones sólidas.

------------------------------------------------------------------------

# Lo que un arquitecto debería recordar

-   Un modelo no es una aplicación.
-   Un LLM no sustituye el criterio profesional.
-   Las respuestas deben validarse.
-   El valor de una solución suele encontrarse en la arquitectura
    completa y no únicamente en el modelo utilizado.

------------------------------------------------------------------------

# Próximo capítulo

**Capítulo 8 --- Tokens**

Analizaremos el concepto de token, la unidad fundamental utilizada por
los modelos de lenguaje para representar y procesar información.

> "Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones."
