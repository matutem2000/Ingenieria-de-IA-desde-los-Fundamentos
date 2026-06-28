# Capítulo 4 --- Sección 03 de 10

# El ciclo de razonamiento de un agente

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un agente no ejecuta acciones al azar. Observa, razona, planifica,
> actúa y aprende del resultado obtenido."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender el ciclo operativo de un agente moderno.
-   Diferenciar razonamiento de ejecución.
-   Entender cómo un agente adapta su comportamiento durante una tarea.
-   Identificar los puntos donde un arquitecto puede intervenir para
    mejorar el sistema.

------------------------------------------------------------------------

# Introducción

En los capítulos anteriores analizamos sistemas cuyo comportamiento
seguía un flujo relativamente lineal.

Un usuario realizaba una consulta.

El sistema recuperaba información.

El modelo generaba una respuesta.

En un agente, el comportamiento deja de ser lineal.

La ejecución se convierte en un proceso iterativo donde cada acción
modifica el contexto de la siguiente.

El agente no solo responde.

Evalúa continuamente si está avanzando hacia el objetivo.

------------------------------------------------------------------------

# Un ciclo continuo

Aunque existen distintas implementaciones, la mayoría de los agentes
sigue un patrón similar.

1.  Comprender el objetivo.
2.  Elaborar un plan.
3.  Seleccionar una acción.
4.  Ejecutar la acción.
5.  Observar el resultado.
6.  Evaluar si el objetivo fue alcanzado.
7.  Repetir el ciclo cuando sea necesario.

Este mecanismo permite resolver problemas cuya solución no puede
determinarse en una única inferencia.

------------------------------------------------------------------------

# Comprender antes de actuar

Toda ejecución comienza interpretando correctamente la solicitud.

Una misma instrucción puede admitir múltiples estrategias.

Por ejemplo:

> "Prepará un informe de ventas."

El agente deberá responder preguntas como:

-   ¿De qué período?
-   ¿Qué sistema contiene la información?
-   ¿Debe incluir gráficos?
-   ¿Quién recibirá el informe?
-   ¿Existe un formato corporativo?

Responder estas cuestiones forma parte del razonamiento inicial.

------------------------------------------------------------------------

# Planificación

Una vez comprendido el objetivo, el agente construye un plan.

El plan no tiene por qué ser definitivo.

Puede modificarse durante la ejecución.

Este comportamiento diferencia a un agente de un flujo rígido
preprogramado.

El sistema adapta sus decisiones según la información obtenida en cada
paso.

------------------------------------------------------------------------

# Acción

Cada acción implica utilizar una herramienta.

Algunos ejemplos incluyen:

-   ejecutar una consulta SQL;
-   llamar a una API REST;
-   consultar un ERP;
-   buscar documentos mediante RAG;
-   enviar un correo electrónico;
-   ejecutar un script.

El modelo no realiza directamente estas operaciones.

Las solicita al orquestador mediante interfaces previamente definidas.

------------------------------------------------------------------------

# Observación

Después de ejecutar una acción, el agente analiza el resultado.

Puede descubrir que:

-   obtuvo la información esperada;
-   la consulta produjo un error;
-   faltan datos;
-   es necesario consultar otra fuente;
-   el plan debe modificarse.

Esta retroalimentación convierte al agente en un sistema adaptativo.

------------------------------------------------------------------------

# Reflexión

Las arquitecturas más avanzadas incorporan una etapa adicional.

El agente evalúa la calidad de su propio trabajo antes de finalizar.

Puede verificar si:

-   respondió completamente;
-   utilizó información suficiente;
-   existen inconsistencias;
-   conviene ejecutar pasos adicionales.

Este proceso suele conocerse como *reflection* o *self-evaluation*.

No implica conciencia.

Representa un mecanismo de control diseñado para incrementar la calidad
del resultado.

------------------------------------------------------------------------

# Flujo completo

``` mermaid
flowchart LR

A[Objetivo]
A --> B[Razonar]
B --> C[Planificar]
C --> D[Actuar]
D --> E[Observar]
E --> F[Reflexionar]

F -->|Objetivo alcanzado| G[Finalizar]
F -->|Faltan acciones| B
```

Obsérvese que el ciclo puede repetirse múltiples veces.

------------------------------------------------------------------------

# Caso de estudio

Una empresa solicita a un agente:

> "Analizá las ventas del último semestre, identificá anomalías y
> prepará recomendaciones."

Durante la ejecución ocurre lo siguiente.

1.  Consulta el sistema comercial.
2.  Detecta datos incompletos.
3.  Consulta una segunda fuente.
4.  Recalcula los indicadores.
5.  Genera gráficos.
6.  Elabora conclusiones.
7.  Verifica consistencia.
8.  Produce el informe final.

El flujo no estaba completamente definido desde el principio.

Fue adaptándose según los resultados obtenidos.

------------------------------------------------------------------------

# Desafíos arquitectónicos

Implementar este ciclo implica resolver varios problemas.

-   Evitar bucles infinitos.
-   Limitar el número de acciones.
-   Administrar tiempos de espera.
-   Gestionar errores de herramientas.
-   Registrar todas las decisiones.
-   Controlar costos.
-   Mantener trazabilidad.

Estas responsabilidades pertenecen a la arquitectura y no al modelo.

------------------------------------------------------------------------

# Ideas clave

-   Un agente ejecuta un ciclo iterativo de razonamiento y acción.
-   Cada resultado modifica el contexto de la siguiente decisión.
-   La reflexión permite mejorar la calidad antes de finalizar.
-   El orquestador controla la ejecución y evita comportamientos no
    deseados.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos las herramientas (*Tools*) y el
mecanismo de *Function Calling*, comprendiendo cómo un agente interactúa
de forma segura con APIs, bases de datos y aplicaciones empresariales.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
