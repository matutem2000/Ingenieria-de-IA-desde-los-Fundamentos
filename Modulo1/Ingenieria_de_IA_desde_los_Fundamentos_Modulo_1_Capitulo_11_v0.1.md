# Ingeniería de IA desde los Fundamentos

# Módulo I --- Los Fundamentos de la Inteligencia Artificial

# Capítulo 11 --- Temperatura, Top‑K, Top‑P y Sampling

**Versión:** 0.1 (Primer borrador editorial)

------------------------------------------------------------------------

# Objetivos

Al finalizar este capítulo deberías poder:

-   Comprender por qué un mismo modelo puede generar respuestas
    distintas.
-   Explicar el concepto de temperatura.
-   Entender intuitivamente qué son Top‑K, Top‑P y Sampling.
-   Elegir configuraciones adecuadas según el tipo de aplicación.
-   Relacionar estos parámetros con calidad, creatividad y consistencia.

------------------------------------------------------------------------

# Introducción

Una de las preguntas más frecuentes cuando se trabaja con modelos de
lenguaje es:

> "¿Por qué el mismo prompt produce respuestas diferentes?"

La respuesta no suele deberse a un error.

Está relacionada con la forma en que el modelo selecciona el siguiente
token.

Hasta ahora vimos que un LLM calcula probabilidades para muchos tokens
posibles.

La pregunta es:

> ¿Cómo decide finalmente cuál elegir?

------------------------------------------------------------------------

# Una analogía

Imaginemos que completamos la frase:

> "Hoy está haciendo mucho..."

Las palabras más probables podrían ser:

-   calor
-   frío
-   viento

Si siempre eligiéramos la palabra más probable, todas las respuestas
serían prácticamente iguales.

En cambio, si ocasionalmente permitimos elegir alternativas menos
probables, obtenemos respuestas más variadas.

Los parámetros que veremos en este capítulo controlan precisamente ese
comportamiento.

------------------------------------------------------------------------

# Temperatura

La temperatura regula el grado de aleatoriedad durante la generación.

## Temperatura baja

-   respuestas más predecibles;
-   mayor consistencia;
-   menor creatividad.

Suele utilizarse en:

-   generación de código;
-   consultas técnicas;
-   documentos legales;
-   respuestas donde la precisión es prioritaria.

## Temperatura alta

-   mayor variedad;
-   respuestas más creativas;
-   mayor riesgo de errores o alucinaciones.

Puede resultar útil para:

-   lluvia de ideas;
-   escritura creativa;
-   generación de historias;
-   propuestas de marketing.

La temperatura no vuelve más inteligente al modelo.

Simplemente modifica la forma en que selecciona los tokens.

------------------------------------------------------------------------

# Sampling

Sampling significa que el modelo no siempre elige el token más probable.

En su lugar, selecciona uno teniendo en cuenta una distribución de
probabilidades.

Esto evita respuestas excesivamente repetitivas y hace que la
conversación resulte más natural.

------------------------------------------------------------------------

# Top‑K

Top‑K limita la elección a los K tokens más probables.

Ejemplo:

Si Top‑K = 5

El modelo solo podrá seleccionar entre los cinco candidatos con mayor
probabilidad.

Esto reduce respuestas extremadamente improbables.

------------------------------------------------------------------------

# Top‑P

Top‑P utiliza otra estrategia.

En lugar de elegir una cantidad fija de tokens, considera únicamente
aquellos cuya probabilidad acumulada alcanza un determinado porcentaje.

Por ejemplo:

Top‑P = 0.9

El modelo analiza los candidatos más probables hasta alcanzar
aproximadamente el 90 % de la probabilidad total.

Luego selecciona uno dentro de ese conjunto.

Este enfoque suele adaptarse mejor a distintos contextos.

------------------------------------------------------------------------

# ¿Cuál es mejor?

No existe un único valor correcto.

Depende del objetivo.

Un arquitecto debe comprender qué comportamiento necesita la aplicación.

------------------------------------------------------------------------

# Casos prácticos

## Asistente de programación

-   temperatura baja;
-   alta consistencia;
-   mínima creatividad.

## Generador de ideas

-   temperatura media o alta;
-   mayor diversidad de respuestas.

## Chat empresarial

-   equilibrio entre creatividad y precisión.

La configuración forma parte del diseño de la solución.

------------------------------------------------------------------------

# Conversación con un arquitecto

**Desarrollador**

"El modelo respondió distinto."

**Arquitecto**

"¿Qué configuración de temperatura y sampling utilizaste?"

Muchas veces la diferencia no está en el modelo.

Está en la configuración.

------------------------------------------------------------------------

# Ideas clave

-   Los modelos trabajan con probabilidades.
-   Temperatura controla el nivel de aleatoriedad.
-   Top‑K limita la cantidad de candidatos.
-   Top‑P limita la probabilidad acumulada considerada.
-   Sampling evita respuestas completamente determinísticas.

------------------------------------------------------------------------

# Laboratorio

Elegí un mismo prompt.

Ejecutalo con distintas configuraciones de temperatura.

Compará:

-   creatividad;
-   precisión;
-   repetición;
-   claridad.

Intentá identificar cuál resulta más adecuada para cada tipo de tarea.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Siempre queremos la respuesta más creativa?
-   ¿Cuándo la consistencia es más importante que la originalidad?
-   ¿Qué riesgos aparecen si aumentamos demasiado la temperatura?

------------------------------------------------------------------------

# Resumen

La generación de texto no consiste únicamente en calcular
probabilidades.

También implica decidir cómo utilizar esas probabilidades para
seleccionar el siguiente token.

Temperatura, Top‑K, Top‑P y Sampling permiten controlar ese
comportamiento y adaptar el modelo a distintos escenarios.

Comprender estos parámetros ayuda a diseñar aplicaciones más previsibles
y acordes con las necesidades del negocio.

------------------------------------------------------------------------

# Lo que un arquitecto debería recordar

-   No existe una configuración universal.
-   La creatividad tiene un costo en consistencia.
-   La precisión suele requerir menor aleatoriedad.
-   Elegir correctamente estos parámetros forma parte del diseño de la
    solución.

------------------------------------------------------------------------

# Próximo capítulo

**Capítulo 12 --- Mitos sobre la Inteligencia Artificial**

Analizaremos las ideas equivocadas más frecuentes sobre los modelos
modernos y aprenderemos a distinguir entre capacidades reales, marketing
y expectativas infundadas.

> "Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones."
