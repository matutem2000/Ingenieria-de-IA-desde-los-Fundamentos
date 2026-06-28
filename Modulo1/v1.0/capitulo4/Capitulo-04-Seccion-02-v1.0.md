# Capítulo 4 --- Sección 02 de 10

# Anatomía de un agente de IA

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"La inteligencia de un agente no depende únicamente del modelo que
> utiliza, sino de cómo coordina todos sus componentes."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender los componentes internos de un agente moderno.
-   Entender el flujo de planificación y ejecución.
-   Diferenciar razonamiento, memoria, herramientas y orquestación.
-   Identificar las responsabilidades arquitectónicas de cada
    componente.

------------------------------------------------------------------------

# Introducción

En la sección anterior definimos un agente como un sistema orientado a
objetivos.

Ahora analizaremos su estructura interna.

Aunque distintas plataformas implementan agentes de formas diferentes,
la mayoría comparte un conjunto de componentes fundamentales.

Comprender estas responsabilidades resulta mucho más importante que
aprender una biblioteca específica.

Las herramientas evolucionan.

Los principios arquitectónicos permanecen.

------------------------------------------------------------------------

# El modelo de lenguaje

El Large Language Model continúa siendo el núcleo del razonamiento.

Su función consiste en:

-   interpretar instrucciones;
-   comprender el contexto;
-   analizar información;
-   generar planes;
-   decidir qué acción realizar a continuación.

Sin embargo, el modelo no ejecuta directamente esas acciones.

Necesita colaborar con otros componentes.

------------------------------------------------------------------------

# El planificador

Una característica distintiva de los agentes es la capacidad de dividir
un objetivo complejo en una secuencia de tareas.

Por ejemplo, ante la solicitud:

> "Generá un informe de ventas del último trimestre y enviáselo al
> director comercial."

El planificador podría producir una secuencia como:

1.  Consultar el ERP.
2.  Obtener las ventas.
3.  Consolidar los datos.
4.  Generar gráficos.
5.  Redactar el informe.
6.  Enviar el correo.
7.  Registrar la auditoría.

Esta planificación permite abordar problemas que no pueden resolverse
con una única llamada al modelo.

------------------------------------------------------------------------

# La memoria

Un agente necesita recordar información mientras trabaja.

Dependiendo de la arquitectura, la memoria puede dividirse en diferentes
niveles.

**Memoria de corto plazo**

Mantiene el contexto de la tarea actual.

**Memoria de largo plazo**

Conserva información útil entre distintas sesiones, como preferencias
del usuario, configuraciones o resultados previamente validados.

No toda la información debe almacenarse en el contexto del LLM.

Una gestión adecuada de la memoria mejora el rendimiento y reduce
costos.

------------------------------------------------------------------------

# Las herramientas

Los agentes amplían sus capacidades mediante herramientas externas.

Algunos ejemplos incluyen:

-   consultar una base de datos;
-   invocar una API;
-   ejecutar código;
-   acceder a un sistema ERP;
-   enviar correos electrónicos;
-   generar documentos;
-   realizar búsquedas en Internet;
-   interactuar con otros agentes.

Cada herramienta posee una interfaz bien definida.

El agente decide cuándo utilizarla y cómo interpretar sus resultados.

------------------------------------------------------------------------

# El orquestador

El orquestador coordina el funcionamiento completo del sistema.

Entre sus responsabilidades se encuentran:

-   iniciar la ejecución;
-   administrar el estado;
-   invocar herramientas;
-   controlar errores;
-   registrar auditoría;
-   aplicar políticas de seguridad;
-   finalizar la tarea.

En sistemas empresariales, el orquestador suele contener una parte
importante de la lógica de negocio.

------------------------------------------------------------------------

# Flujo general

``` mermaid
flowchart LR

A[Objetivo del usuario]
A --> B[Planificador]

B --> C[LLM]
C --> D[Selección de herramienta]
D --> E[Ejecución]
E --> F[Resultado]
F --> G[Memoria]
G --> H[Respuesta final]
```

Este flujo puede repetirse múltiples veces hasta completar el objetivo.

------------------------------------------------------------------------

# Caso de estudio

Una empresa desarrolla un agente para asistir al área de compras.

El usuario solicita:

> "Compará los precios de los tres últimos proveedores y recomendá la
> mejor alternativa."

El agente no puede responder únicamente con el conocimiento del modelo.

Debe:

-   consultar el sistema de compras;
-   recuperar órdenes anteriores;
-   comparar valores;
-   aplicar criterios definidos por la organización;
-   justificar la recomendación;
-   registrar la decisión.

El modelo aporta razonamiento.

La arquitectura aporta capacidad operativa.

------------------------------------------------------------------------

# Ideas clave

-   Un agente está compuesto por múltiples componentes especializados.
-   El LLM representa solo una parte del sistema.
-   Planificación, memoria, herramientas y orquestación trabajan de
    forma coordinada.
-   La calidad del agente depende tanto de la arquitectura como del
    modelo utilizado.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos el ciclo de razonamiento de un
agente, analizando cómo planifica, ejecuta, observa resultados y adapta
sus acciones hasta alcanzar el objetivo solicitado.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
