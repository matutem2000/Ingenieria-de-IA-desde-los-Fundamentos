# Capitulo-13-Seccion-04-v1.0

# Capítulo 13 --- Laboratorios de Ingeniería de Inteligencia Artificial

**Versión:** 1.0\
**Estado:** Aprobado

> *"Una hipótesis sin mediciones es solamente una opinión."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Comprender el impacto de los parámetros de inferencia.
-   Experimentar con temperatura, Top-K y Top-P.
-   Analizar la relación entre creatividad, estabilidad y
    reproducibilidad.
-   Registrar resultados para fundamentar decisiones de arquitectura.

------------------------------------------------------------------------

# Laboratorio 2 --- Influencia de los parámetros de inferencia

## Objetivo

Observar cómo pequeñas modificaciones en la configuración del modelo
producen respuestas significativamente distintas ante el mismo prompt.

## Nivel

Inicial -- Intermedio.

## Tiempo estimado

45 minutos.

## Prerrequisitos

-   Laboratorio anterior completado.
-   Modelo local operativo.
-   Aplicación cliente funcional.

------------------------------------------------------------------------

# Escenario

Un equipo de desarrollo debe construir un asistente corporativo.

Antes de definir la configuración definitiva necesita comprender cómo
afectan los parámetros de inferencia al comportamiento del modelo.

No se busca encontrar una configuración universal, sino desarrollar
criterio.

``` mermaid
flowchart LR
A[Prompt único] --> B[Temperatura]
A --> C[Top-K]
A --> D[Top-P]
B --> E[Respuesta]
C --> E
D --> E
```

------------------------------------------------------------------------

# Desarrollo

1.  Seleccionar un único prompt.
2.  Ejecutarlo con temperatura baja.
3.  Repetir con temperatura media.
4.  Repetir con temperatura alta.
5.  Mantener constantes los demás parámetros.
6.  Registrar diferencias de estilo, precisión y variabilidad.
7.  Repetir el procedimiento modificando Top-K y posteriormente Top-P.

------------------------------------------------------------------------

# Validación

El laboratorio será satisfactorio cuando el lector pueda identificar
diferencias objetivas entre las respuestas y explicar qué parámetro
produjo cada cambio.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Qué configuración ofrece mayor estabilidad?
-   ¿Cuál resulta más apropiada para tareas creativas?
-   ¿Qué riesgos aparecen con temperaturas elevadas?
-   ¿Cómo influye la reproducibilidad en un sistema empresarial?

------------------------------------------------------------------------

# Desafíos opcionales

-   Comparar dos modelos utilizando la misma configuración.
-   Medir tiempos de respuesta para cada prueba.
-   Documentar una configuración recomendada para un asistente
    corporativo.

------------------------------------------------------------------------

# Ideas clave

-   Los parámetros modifican el comportamiento del modelo sin alterar su
    entrenamiento.
-   No existe una configuración óptima para todos los escenarios.
-   La experimentación controlada constituye una herramienta fundamental
    para el arquitecto.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección incorporaremos documentos externos para comprobar
cómo cambia el comportamiento del modelo cuando dispone de contexto
adicional.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
