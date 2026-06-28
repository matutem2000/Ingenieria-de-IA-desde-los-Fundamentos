# Capitulo-15-Seccion-06-v1.0

# Capítulo 15 --- Evaluación Final y Proyecto Integrador

**Versión:** 1.0\
**Estado:** Aprobado

> *"Una arquitectura solo demuestra su valor cuando puede operar de
> forma confiable en producción."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Diseñar la arquitectura física del proyecto integrador.
-   Analizar alternativas de despliegue para soluciones empresariales de
    IA.
-   Incorporar criterios de disponibilidad, escalabilidad y resiliencia.
-   Relacionar la infraestructura con los requisitos del negocio.

------------------------------------------------------------------------

# Arquitectura física

La arquitectura lógica define responsabilidades.

La arquitectura física determina dónde y cómo se ejecutará cada
componente.

Esta decisión condiciona el rendimiento, la disponibilidad, los costos
operativos y la capacidad de evolución de la solución.

------------------------------------------------------------------------

# Topología propuesta

``` mermaid
flowchart LR
U[Usuarios] --> LB[Balanceador]
LB --> APP[Aplicaciones]
APP --> RAG[Motor RAG]
RAG --> VDB[Base Vectorial]
RAG --> LLM[Servidor LLM]
APP --> DB[Base de Datos]
APP --> OBS[Observabilidad]
```

------------------------------------------------------------------------

# Distribución de componentes

  Componente       Despliegue recomendado
  ---------------- --------------------------------------------
  Balanceador      Alta disponibilidad
  Aplicación       Múltiples instancias
  Motor RAG        Escalado independiente
  Base vectorial   Nodo dedicado o clúster
  LLM              Infraestructura con GPU cuando corresponda
  Observabilidad   Servicio independiente

------------------------------------------------------------------------

# Criterios arquitectónicos

La infraestructura debe contemplar:

-   escalabilidad horizontal;
-   tolerancia a fallos;
-   separación entre datos y procesamiento;
-   monitoreo continuo;
-   automatización del despliegue;
-   recuperación ante desastres.

La selección de la plataforma dependerá de las restricciones técnicas y
presupuestarias de la organización.

------------------------------------------------------------------------

# Riesgos operativos

  Riesgo                   Estrategia de mitigación
  ------------------------ -------------------------------
  Sobrecarga del modelo    Balanceo y autoescalado
  Falla de un nodo         Redundancia
  Crecimiento documental   Escalado del índice vectorial
  Incremento de usuarios   Escalabilidad horizontal
  Incidentes operativos    Observabilidad y alertas

------------------------------------------------------------------------

# Buenas prácticas

-   Separar servicios críticos.
-   Automatizar despliegues mediante CI/CD.
-   Implementar copias de seguridad periódicas.
-   Diseñar la capacidad antes del crecimiento esperado.
-   Validar la recuperación ante fallos.

------------------------------------------------------------------------

# Ideas clave

-   La arquitectura física transforma el diseño lógico en una solución
    operativa.
-   Disponibilidad y escalabilidad deben planificarse desde el inicio.
-   La infraestructura constituye un componente estratégico de la
    solución de IA.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección se desarrollará la estrategia de operación,
monitoreo y mejora continua necesaria para mantener el proyecto
integrador a lo largo del tiempo.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
