# Capitulo-12-Seccion-04-v1.0

# Capítulo 12 --- Mitos sobre la Inteligencia Artificial

**Versión:** 1.0\
**Estado:** Aprobado

> *"Las tecnologías transforman profesiones, pero rara vez eliminan la
> necesidad de comprender los problemas que intentan resolver."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Analizar el mito de que la IA reemplazará completamente a
    desarrolladores y arquitectos.
-   Comprender qué tareas son susceptibles de automatización y cuáles
    continúan requiriendo criterio humano.
-   Identificar el impacto real de la IA en el ciclo de vida del
    desarrollo de software.
-   Evaluar cómo evolucionan los roles técnicos en organizaciones que
    adoptan Inteligencia Artificial.

------------------------------------------------------------------------

# El mito: "La IA reemplazará a los desarrolladores"

Desde la popularización de los asistentes de programación comenzaron a
aparecer afirmaciones categóricas acerca del futuro de la profesión.

Algunas sostienen que el desarrollo de software desaparecerá.

Otras afirman que bastará con escribir un prompt para construir sistemas
empresariales completos.

Ambas posturas simplifican un problema considerablemente más complejo.

La generación automática de código constituye únicamente una parte del
proceso de ingeniería.

Diseñar una solución implica comprender el negocio, identificar
restricciones, evaluar riesgos, negociar prioridades, integrar múltiples
sistemas y garantizar atributos de calidad como seguridad,
mantenibilidad y escalabilidad.

Estas actividades requieren conocimiento contextual que trasciende la
simple generación de código.

------------------------------------------------------------------------

# Automatización versus sustitución

La historia de la informática demuestra que las herramientas exitosas
modifican la forma de trabajar antes que eliminar completamente una
profesión.

Los compiladores no reemplazaron a los programadores.

Los frameworks no eliminaron a los arquitectos.

Los servicios en la nube no hicieron desaparecer a los administradores
de infraestructura.

La Inteligencia Artificial sigue una tendencia similar.

Automatiza tareas repetitivas, acelera actividades de bajo valor
agregado y permite concentrar el esfuerzo humano en decisiones de mayor
impacto.

  Actividad                         Nivel de automatización
  --------------------------------- -------------------------
  Generación de código repetitivo   Alto
  Refactorizaciones simples         Alto
  Documentación inicial             Alto
  Diseño de arquitectura            Bajo
  Negociación con usuarios          Muy bajo
  Definición de requisitos          Muy bajo
  Toma de decisiones estratégicas   Muy bajo

------------------------------------------------------------------------

# Caso de estudio

Una empresa incorpora un asistente de programación para acelerar el
desarrollo de nuevos microservicios.

Durante los primeros meses la productividad aumenta de forma
considerable.

Sin embargo, aparecen inconsistencias arquitectónicas entre distintos
equipos debido a que cada desarrollador acepta automáticamente las
sugerencias generadas por el modelo.

La organización comprende entonces que la IA incrementa la velocidad de
implementación, pero no reemplaza la necesidad de estándares, revisiones
técnicas ni liderazgo arquitectónico.

La mejora sostenida surge cuando el asistente pasa a formar parte del
proceso de ingeniería, en lugar de sustituirlo.

``` mermaid
flowchart LR
A[Requisitos] --> B[Arquitecto]
B --> C[Diseño]
C --> D[Asistente IA]
D --> E[Implementación]
E --> F[Revisión humana]
F --> G[Producción]
```

------------------------------------------------------------------------

# Buenas prácticas

-   Utilizar asistentes de IA como herramientas de apoyo y no como
    fuente única de decisiones.
-   Mantener revisiones de código independientemente del origen de la
    implementación.
-   Definir estándares arquitectónicos antes de incorporar asistentes
    automáticos.
-   Capacitar a los equipos para evaluar críticamente las sugerencias
    del modelo.

------------------------------------------------------------------------

# Errores frecuentes

  -----------------------------------------------------------------------
  Error                     Consecuencia
  ------------------------- ---------------------------------------------
  Aceptar todo el código    Deuda técnica creciente
  generado                  

  Eliminar revisiones       Mayor probabilidad de defectos
  humanas                   

  Suponer que la            Soluciones inconsistentes
  arquitectura puede        
  automatizarse             
  completamente             

  Medir únicamente          Disminución de la calidad del software
  velocidad                 
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Ideas clave

-   La IA modifica la profesión del desarrollador, no la elimina.
-   Cuanto mayor es la complejidad del problema, mayor resulta la
    importancia del criterio humano.
-   La arquitectura continúa siendo una disciplina basada en decisiones,
    no en generación automática de código.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección analizaremos otro mito frecuente: la creencia de
que basta con utilizar el modelo más grande disponible para obtener la
mejor solución posible.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
