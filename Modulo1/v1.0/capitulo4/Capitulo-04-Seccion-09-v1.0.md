# Capítulo 4 --- Sección 09 de 10

# Patrones arquitectónicos para agentes empresariales

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un agente útil resuelve una tarea. Una arquitectura de agentes bien
> diseñada permite que cientos de ellos evolucionen sin perder control,
> seguridad ni mantenibilidad."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender los principales patrones arquitectónicos para agentes
    empresariales.
-   Diseñar soluciones desacopladas y escalables.
-   Integrar agentes con microservicios, eventos y sistemas existentes.
-   Identificar decisiones arquitectónicas que favorecen la resiliencia
    y el mantenimiento.

------------------------------------------------------------------------

# Introducción

Los primeros prototipos de agentes suelen concentrar toda la lógica en
un único proceso.

El mismo componente recibe la solicitud, razona, invoca herramientas,
almacena memoria y devuelve una respuesta.

Este enfoque resulta adecuado para validar una idea.

Sin embargo, cuando la solución comienza a crecer aparecen problemas de
escalabilidad, mantenimiento y gobierno.

La arquitectura debe evolucionar.

------------------------------------------------------------------------

# Desacoplamiento

Una plataforma empresarial debería separar claramente sus
responsabilidades.

Una arquitectura habitual incluye:

-   interfaz de usuario;
-   API de entrada;
-   orquestador de agentes;
-   servicio de memoria;
-   servicio RAG;
-   catálogo de herramientas;
-   observabilidad;
-   auditoría.

Cada componente puede evolucionar independientemente.

Esta separación reduce el impacto de los cambios y facilita las pruebas.

------------------------------------------------------------------------

# Integración con microservicios

En muchas organizaciones los sistemas ya existen.

ERP, CRM, RR. HH., autenticación, facturación y otros servicios forman
parte de la plataforma tecnológica.

El agente no debería reemplazarlos.

Debe integrarse con ellos mediante contratos estables.

En este contexto, los agentes se comportan como consumidores de
capacidades ya disponibles.

La lógica de negocio permanece donde corresponde.

------------------------------------------------------------------------

# Arquitecturas orientadas a eventos

No todas las interacciones requieren una respuesta inmediata.

Algunas tareas pueden ejecutarse de forma asincrónica.

Por ejemplo:

-   generar informes extensos;
-   procesar grandes volúmenes documentales;
-   ejecutar migraciones;
-   enviar notificaciones masivas.

En estos escenarios resulta conveniente utilizar eventos y colas de
mensajes.

El agente inicia el proceso y continúa con otras tareas mientras la
operación se ejecuta en segundo plano.

------------------------------------------------------------------------

# Resiliencia

Toda arquitectura debe asumir que los errores ocurrirán.

Una API puede dejar de responder.

Una herramienta puede exceder el tiempo máximo permitido.

Una base vectorial puede encontrarse temporalmente fuera de servicio.

Por ello conviene incorporar mecanismos como:

-   reintentos controlados;
-   tiempos de espera (*timeouts*);
-   circuit breakers;
-   degradación controlada;
-   colas de recuperación;
-   compensación de operaciones.

La resiliencia no elimina los errores.

Reduce su impacto.

------------------------------------------------------------------------

# Escalabilidad

Los distintos componentes presentan necesidades diferentes.

El servicio RAG puede requerir más memoria.

El LLM puede necesitar GPU.

El catálogo de herramientas puede crecer sin afectar al resto del
sistema.

Diseñar servicios independientes permite escalar únicamente los
componentes que realmente lo necesitan.

------------------------------------------------------------------------

# Arquitectura de referencia

``` mermaid
flowchart LR

U[Cliente]

U --> API[API Gateway]

API --> ORQ[Orquestador]

ORQ --> RAG[Servicio RAG]
ORQ --> MEM[Servicio de Memoria]
ORQ --> TOOLS[Catálogo de Tools]
ORQ --> OBS[Observabilidad]

TOOLS --> ERP[ERP]
TOOLS --> CRM[CRM]
TOOLS --> MAIL[Correo]

RAG --> VDB[Base Vectorial]

OBS --> LOGS[Logs]
```

Este diseño favorece el desacoplamiento y permite evolucionar cada
servicio de forma independiente.

------------------------------------------------------------------------

# Caso de estudio

Una empresa comienza con un único agente encargado de atención interna.

Con el tiempo incorpora automatizaciones para recursos humanos,
finanzas, infraestructura y compras.

En lugar de ampliar indefinidamente el agente original, adopta una
arquitectura modular.

Cada dominio dispone de sus propias herramientas y reglas de negocio.

El orquestador decide qué agente o servicio debe intervenir en cada
solicitud.

El resultado es un sistema más mantenible y preparado para crecer.

------------------------------------------------------------------------

# Buenas prácticas

-   Mantener responsabilidades claramente separadas.
-   Reutilizar servicios existentes antes de duplicar lógica.
-   Diseñar contratos estables entre componentes.
-   Incorporar resiliencia desde el inicio.
-   Escalar servicios de forma independiente.
-   Centralizar monitoreo, métricas y auditoría.

------------------------------------------------------------------------

# Ideas clave

-   Una arquitectura empresarial debe evolucionar más allá del prototipo
    inicial.
-   Los agentes deben integrarse con la plataforma existente, no
    reemplazarla.
-   Eventos, microservicios y desacoplamiento facilitan la evolución del
    sistema.
-   Escalabilidad y resiliencia forman parte del diseño arquitectónico.

------------------------------------------------------------------------

## Próxima sección

En la última sección del capítulo integraremos todos los conceptos
estudiados sobre agentes de IA y construiremos una arquitectura de
referencia completa, preparando el camino para los capítulos dedicados a
plataformas de IA y MLOps.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
