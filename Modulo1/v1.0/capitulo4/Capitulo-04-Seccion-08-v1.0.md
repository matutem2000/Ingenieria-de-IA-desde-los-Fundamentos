# Capítulo 4 --- Sección 08 de 10

# Observabilidad, Gobierno y Seguridad en Sistemas de Agentes

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"La diferencia entre un experimento y una plataforma empresarial no
> está en la calidad del modelo, sino en la capacidad de gobernar su
> comportamiento."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender la importancia de la observabilidad en arquitecturas
    basadas en agentes.
-   Identificar los principales mecanismos de gobierno y control.
-   Entender el papel del enfoque Human-in-the-Loop (HITL).
-   Diseñar sistemas auditables, seguros y preparados para producción.

------------------------------------------------------------------------

# Introducción

Construir un agente capaz de ejecutar tareas complejas representa un
desafío técnico importante.

Sin embargo, desplegar ese mismo agente dentro de una organización
incorpora nuevas exigencias.

La empresa necesita responder preguntas como:

-   ¿Qué decisión tomó el agente?
-   ¿Qué información utilizó?
-   ¿Qué herramientas ejecutó?
-   ¿Quién autorizó la operación?
-   ¿Cuál fue el costo?
-   ¿Cómo reconstruir una ejecución ocurrida hace seis meses?

Responder estas preguntas requiere mucho más que un buen modelo.

Requiere una arquitectura de gobierno.

------------------------------------------------------------------------

# Observabilidad

La observabilidad consiste en obtener información suficiente para
comprender el comportamiento interno del sistema.

En una arquitectura basada en agentes conviene registrar, al menos:

-   objetivo solicitado;
-   plan generado;
-   herramientas utilizadas;
-   parámetros enviados;
-   respuestas obtenidas;
-   duración de cada etapa;
-   cantidad de tokens consumidos;
-   costo estimado;
-   resultado final.

Estos registros permiten diagnosticar problemas y optimizar el sistema
de manera continua.

------------------------------------------------------------------------

# Auditoría

No toda la información registrada tiene únicamente fines técnicos.

En muchos sectores existen requisitos regulatorios.

Por ejemplo:

-   administración pública;
-   salud;
-   sistema financiero;
-   justicia;
-   infraestructura crítica.

En estos escenarios es indispensable reconstruir exactamente qué ocurrió
durante una ejecución.

La auditoría proporciona esa capacidad.

------------------------------------------------------------------------

# Gobierno

El gobierno establece las reglas bajo las cuales puede operar un agente.

Algunos ejemplos incluyen:

-   herramientas autorizadas;
-   operaciones prohibidas;
-   límites de gasto;
-   horarios permitidos;
-   clasificación de información;
-   políticas de retención;
-   segregación de funciones.

Estas reglas no deberían implementarse dentro del prompt.

Deben formar parte de la arquitectura.

------------------------------------------------------------------------

# Human-in-the-Loop

No todas las decisiones deben automatizarse completamente.

En operaciones críticas resulta habitual incorporar un mecanismo de
aprobación humana.

Este enfoque se conoce como **Human-in-the-Loop (HITL)**.

El agente puede preparar una propuesta, pero la ejecución definitiva
requiere validación por parte de una persona autorizada.

Algunos ejemplos son:

-   aprobar una transferencia bancaria;
-   eliminar información sensible;
-   otorgar permisos privilegiados;
-   firmar documentación legal;
-   publicar cambios en producción.

------------------------------------------------------------------------

# Gestión de riesgos

Toda arquitectura basada en agentes debe considerar riesgos como:

-   ejecución de acciones incorrectas;
-   acceso indebido a información;
-   uso excesivo de recursos;
-   errores de herramientas externas;
-   respuestas inconsistentes;
-   ataques mediante prompt injection;
-   fuga de información confidencial.

La mitigación de estos riesgos requiere controles en múltiples capas.

------------------------------------------------------------------------

# Arquitectura de control

``` mermaid
flowchart LR

U[Usuario]
U --> O[Orquestador]

O --> P[Políticas]
O --> A[Auditoría]
O --> L[Logs]
O --> H[Human-in-the-Loop]

P --> T[Herramientas]

T --> R[Resultado]

R --> O
```

Obsérvese que la seguridad no depende exclusivamente del modelo.

Está distribuida entre distintos componentes.

------------------------------------------------------------------------

# Caso de estudio

Una organización implementa un agente con capacidad para administrar
usuarios corporativos.

Durante una prueba, un empleado solicita:

> "Eliminá todas las cuentas inactivas."

El agente identifica correctamente la herramienta necesaria.

Sin embargo, las políticas establecen que cualquier eliminación masiva
requiere aprobación de un administrador.

El orquestador detiene la ejecución, genera una solicitud de aprobación
y registra toda la operación.

La seguridad no provino del modelo.

Provino de la arquitectura.

------------------------------------------------------------------------

# Buenas prácticas

-   Registrar todas las ejecuciones relevantes.
-   Aplicar políticas fuera del modelo.
-   Incorporar aprobación humana en operaciones críticas.
-   Medir costos y consumo de recursos.
-   Centralizar observabilidad.
-   Diseñar mecanismos de recuperación ante fallos.
-   Revisar periódicamente permisos y herramientas disponibles.

------------------------------------------------------------------------

# Ideas clave

-   Observabilidad, auditoría y gobierno son componentes esenciales de
    una plataforma de agentes.
-   Las políticas deben implementarse en la arquitectura y no depender
    del prompt.
-   Human-in-the-Loop reduce riesgos en operaciones sensibles.
-   Un sistema empresarial debe ser explicable, auditable y controlable.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos patrones de diseño para agentes
empresariales, analizando arquitecturas desacopladas, integración con
microservicios, resiliencia y escalabilidad.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
