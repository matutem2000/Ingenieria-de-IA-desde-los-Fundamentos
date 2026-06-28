# Capítulo 4 --- Sección 04 de 10

# Tools y Function Calling: cómo un agente interactúa con el mundo

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"La diferencia entre un chatbot y un agente suele comenzar cuando el
> modelo deja de responder únicamente con texto y empieza a utilizar
> herramientas."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué es una *tool* dentro de una arquitectura de agentes.
-   Entender el concepto de *Function Calling*.
-   Diferenciar generación de texto de ejecución de acciones.
-   Diseñar interfaces seguras entre un agente y sistemas empresariales.

------------------------------------------------------------------------

# Introducción

Un Large Language Model posee una extraordinaria capacidad para
interpretar lenguaje natural y generar respuestas.

Sin embargo, no puede consultar una base de datos corporativa, enviar un
correo electrónico ni crear un usuario en un ERP por sí mismo.

Para realizar esas acciones necesita un mecanismo de integración.

Ese mecanismo se materializa mediante **tools** y **Function Calling**.

Lejos de ser una característica secundaria, constituyen uno de los
pilares de la Ingeniería de IA moderna.

------------------------------------------------------------------------

# ¿Qué es una tool?

Una *tool* es una capacidad externa que el agente puede invocar durante
la resolución de una tarea.

Puede representar prácticamente cualquier operación accesible mediante
una interfaz bien definida.

Algunos ejemplos son:

-   consultar una API REST;
-   ejecutar una consulta SQL;
-   buscar información en un sistema RAG;
-   enviar un correo electrónico;
-   crear un ticket;
-   generar un documento PDF;
-   ejecutar código controlado;
-   invocar otro agente.

Desde la perspectiva del modelo, todas estas operaciones se presentan
como funciones disponibles.

------------------------------------------------------------------------

# ¿Qué es Function Calling?

El *Function Calling* permite que el modelo indique **qué herramienta
desea utilizar y con qué parámetros**, en lugar de intentar ejecutar la
acción directamente.

Este cambio es fundamental.

El modelo no accede de manera autónoma a un sistema externo.

Genera una intención estructurada.

El orquestador interpreta esa intención, valida los parámetros y decide
si la operación puede ejecutarse.

De esta forma, el modelo propone acciones, mientras que la arquitectura
conserva el control.

------------------------------------------------------------------------

# Separación de responsabilidades

Una arquitectura madura distingue claramente tres responsabilidades.

**El modelo**

-   interpreta la solicitud;
-   decide qué herramienta necesita.

**El orquestador**

-   valida la solicitud;
-   aplica políticas de seguridad;
-   invoca la herramienta correspondiente.

**La herramienta**

-   ejecuta la operación;
-   devuelve un resultado estructurado.

Esta separación reduce el acoplamiento y facilita el reemplazo de
cualquiera de los componentes.

------------------------------------------------------------------------

# Flujo de ejecución

``` mermaid
flowchart LR

A[Usuario] --> B[LLM]

B --> C[Solicitud de Tool]

C --> D[Orquestador]

D --> E[API / ERP / SQL / Servicio]

E --> F[Resultado]

F --> D

D --> B

B --> G[Respuesta]
```

Obsérvese que el modelo nunca interactúa directamente con los sistemas
corporativos.

Siempre existe una capa de control.

------------------------------------------------------------------------

# Diseño de herramientas

Una herramienta bien diseñada debería cumplir varios principios.

## Responsabilidad única

Cada herramienta debe realizar una tarea claramente definida.

## Contratos explícitos

Los parámetros de entrada y salida deben estar completamente
especificados.

## Idempotencia cuando sea posible

Ejecutar la misma operación varias veces no debería producir efectos
inesperados.

## Manejo de errores

Toda herramienta debe devolver errores estructurados que el agente pueda
interpretar.

## Auditoría

Cada invocación debería quedar registrada para facilitar trazabilidad y
cumplimiento normativo.

------------------------------------------------------------------------

# Seguridad

Uno de los errores más peligrosos consiste en otorgar al modelo acceso
irrestricto a sistemas críticos.

La arquitectura debe incorporar mecanismos como:

-   autenticación;
-   autorización;
-   validación de parámetros;
-   listas de operaciones permitidas;
-   límites de ejecución;
-   confirmación humana para acciones críticas.

Un agente nunca debería ejecutar operaciones sensibles únicamente porque
un usuario las solicitó en lenguaje natural.

------------------------------------------------------------------------

# Caso de estudio

Un agente de soporte recibe la solicitud:

> "Deshabilitá el acceso VPN del usuario Juan Pérez."

El modelo identifica que debe utilizar la herramienta
**DeshabilitarVPN()**.

Sin embargo, antes de ejecutar la acción, el orquestador verifica:

-   que el usuario solicitante posee permisos;
-   que la operación requiere aprobación;
-   que el identificador corresponde a un usuario existente;
-   que la auditoría está habilitada.

Solo entonces la herramienta realiza la modificación.

La inteligencia del modelo no reemplaza las políticas de seguridad de la
organización.

Las complementa.

------------------------------------------------------------------------

# Buenas prácticas

-   Mantener herramientas pequeñas y especializadas.
-   Evitar exponer operaciones innecesarias al modelo.
-   Versionar las interfaces.
-   Registrar todas las ejecuciones.
-   Separar claramente razonamiento y ejecución.
-   Validar siempre los parámetros antes de invocar sistemas externos.

------------------------------------------------------------------------

# Ideas clave

-   Una *tool* amplía las capacidades del agente.
-   El *Function Calling* no ejecuta acciones; solicita su ejecución.
-   El orquestador mantiene el control sobre las operaciones.
-   Seguridad, auditoría y contratos son responsabilidades
    arquitectónicas.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos la memoria de los agentes,
analizando cómo administran contexto, conocimiento persistente y
experiencias previas para resolver tareas cada vez más complejas.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
