# Ingeniería de IA desde los Fundamentos

# Módulo I --- Los Fundamentos de la Inteligencia Artificial

# Capítulo 9 --- Ventana de Contexto (Context Window)

**Versión:** 0.1 (Primer borrador editorial)

------------------------------------------------------------------------

# Objetivos

Al finalizar este capítulo deberías poder:

-   Explicar qué es la ventana de contexto.
-   Comprender por qué los modelos "olvidan" información.
-   Diferenciar memoria de contexto.
-   Entender el impacto del contexto sobre costo, rendimiento y calidad.
-   Diseñar estrategias para administrar conversaciones largas.

------------------------------------------------------------------------

# Introducción

Una de las preguntas más frecuentes entre quienes comienzan a utilizar
un LLM es:

> "¿Por qué el modelo se olvidó de lo que hablamos hace un rato?"

La respuesta no suele estar relacionada con un error.

Está relacionada con un concepto fundamental: la **ventana de
contexto**.

Los modelos no tienen acceso ilimitado a toda la conversación.

Trabajan únicamente con una cantidad máxima de tokens disponible para
cada interacción.

------------------------------------------------------------------------

# ¿Qué es la ventana de contexto?

Podemos imaginar la ventana de contexto como el escritorio sobre el que
trabaja el modelo.

Todo lo que cabe sobre ese escritorio puede utilizarse para responder.

Lo que queda fuera deja de estar disponible para el proceso de
inferencia.

Mientras más grande sea el escritorio, más información puede considerar
simultáneamente.

------------------------------------------------------------------------

# Contexto no es memoria

Esta diferencia es muy importante.

El contexto contiene únicamente la información disponible durante la
conversación actual.

La memoria, en cambio, implica conservar información para reutilizarla
posteriormente.

Un LLM básico no recuerda automáticamente conversaciones anteriores.

Cada solicitud es procesada utilizando únicamente el contexto enviado.

Por eso las aplicaciones profesionales implementan mecanismos
adicionales cuando necesitan continuidad.

------------------------------------------------------------------------

# ¿Qué consume la ventana?

La ventana de contexto no contiene solamente la pregunta.

También incluye, por ejemplo:

-   instrucciones del sistema;
-   historial de conversación;
-   documentos recuperados por un RAG;
-   herramientas utilizadas;
-   respuesta parcial que el modelo está generando.

Todo ello consume tokens.

------------------------------------------------------------------------

# ¿Qué ocurre cuando se supera el límite?

Depende de la aplicación.

Entre las estrategias más comunes encontramos:

-   eliminar mensajes antiguos;
-   resumir conversaciones;
-   recuperar únicamente información relevante;
-   dividir documentos en fragmentos;
-   iniciar una nueva conversación.

No existe una única solución correcta.

Dependerá del problema que estemos resolviendo.

------------------------------------------------------------------------

# ¿Más contexto siempre es mejor?

No necesariamente.

Enviar información innecesaria puede:

-   aumentar el costo;
-   incrementar la latencia;
-   dificultar que el modelo identifique lo verdaderamente importante.

El objetivo no consiste en enviar "todo".

Consiste en enviar el contexto adecuado.

------------------------------------------------------------------------

# Ventana de contexto y RAG

En un sistema RAG suele recuperarse únicamente la información
relacionada con la consulta del usuario.

De esta manera se aprovecha mejor la ventana disponible.

Si se enviaran miles de documentos completos en cada consulta, el
sistema sería costoso e ineficiente.

La recuperación inteligente de contexto es uno de los pilares del diseño
moderno de aplicaciones con IA.

------------------------------------------------------------------------

# Conversación con un arquitecto

**Desarrollador**

"Nuestro modelo admite una ventana de un millón de tokens. Enviemos toda
la base documental."

**Arquitecto**

"¿Toda esa información aporta valor para responder esta consulta?"

El tamaño máximo disponible no elimina la necesidad de diseñar
correctamente el contexto.

------------------------------------------------------------------------

# Caso aplicado

Supongamos una aplicación para consultar un Data Warehouse.

El usuario pregunta:

> "Mostrame la evolución de ventas del último trimestre."

No resulta conveniente enviar el esquema completo de la base de datos.

Es preferible recuperar únicamente:

-   tablas relevantes;
-   relaciones necesarias;
-   definiciones útiles;
-   ejemplos similares.

La respuesta suele ser mejor y más económica.

------------------------------------------------------------------------

# Ideas clave

-   La ventana de contexto es limitada.
-   Contexto no significa memoria permanente.
-   Todo lo enviado consume tokens.
-   Diseñar correctamente el contexto es una tarea de arquitectura.

------------------------------------------------------------------------

# Laboratorio

1.  Escribí una conversación larga con un asistente.
2.  Observá cuándo comienza a perder referencias.
3.  Repetí la prueba resumiendo periódicamente la conversación.
4.  Compará los resultados.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Qué información es realmente imprescindible para responder una
    consulta?
-   ¿Cuándo conviene resumir y cuándo recuperar documentos?
-   ¿Cómo impacta el contexto sobre el costo de una solución?

------------------------------------------------------------------------

# Resumen

La ventana de contexto define la cantidad de información que un modelo
puede considerar simultáneamente durante la inferencia.

Comprender este concepto resulta esencial para diseñar aplicaciones
eficientes, controlar costos y obtener respuestas de mayor calidad.

En la práctica, administrar correctamente el contexto suele ser más
importante que elegir el modelo más grande disponible.

------------------------------------------------------------------------

# Lo que un arquitecto debería recordar

-   Diseñar el contexto es diseñar parte de la inteligencia del sistema.
-   Más información no implica mejores respuestas.
-   Contexto, memoria y conocimiento son conceptos diferentes.
-   La optimización del contexto reduce costos y mejora resultados.

------------------------------------------------------------------------

# Próximo capítulo

**Capítulo 10 --- Embeddings**

Estudiaremos cómo los modelos representan el significado de palabras,
frases y documentos y por qué este concepto es la base de RAG, búsqueda
semántica y recuperación inteligente de información.

> "Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones."
