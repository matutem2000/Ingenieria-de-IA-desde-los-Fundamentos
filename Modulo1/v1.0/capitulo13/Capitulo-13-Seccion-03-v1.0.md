# Capitulo-13-Seccion-03-v1.0

# Capítulo 13 --- Laboratorios de Ingeniería de Inteligencia Artificial

**Versión:** 1.0\
**Estado:** Aprobado

> *"El objetivo de un laboratorio no es demostrar que una herramienta
> funciona, sino comprender por qué lo hace."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Construir el primer laboratorio del libro.
-   Ejecutar un Large Language Model (LLM) en un entorno controlado.
-   Comprender el flujo mínimo entre una aplicación y un modelo.
-   Validar el funcionamiento antes de incorporar componentes
    adicionales.

------------------------------------------------------------------------

# Laboratorio 1 --- Primer contacto con un LLM local

## Objetivo

Construir una aplicación mínima capaz de enviar un prompt a un modelo
ejecutándose localmente y visualizar la respuesta.

## Nivel

Inicial.

## Tiempo estimado

30 a 45 minutos.

## Prerrequisitos

-   Docker instalado.
-   Ollama operativo.
-   Un modelo descargado previamente.
-   Editor de código.

------------------------------------------------------------------------

# Escenario

Una organización desea evaluar el uso de modelos locales antes de
consumir servicios externos.

El objetivo consiste en validar la arquitectura mínima necesaria para
integrar un modelo dentro de una aplicación.

No interesa todavía optimizar rendimiento ni calidad de respuesta.

Lo importante es comprender el flujo completo.

``` mermaid
flowchart LR
A[Usuario] --> B[Aplicación]
B --> C[API de Ollama]
C --> D[LLM]
D --> C
C --> B
B --> A
```

------------------------------------------------------------------------

# Desarrollo

1.  Verificar que el servicio de Ollama se encuentre en ejecución.
2.  Confirmar que el modelo elegido esté disponible.
3.  Enviar un prompt sencillo desde una aplicación cliente.
4.  Registrar el tiempo de respuesta.
5.  Repetir la prueba modificando el prompt.
6.  Comparar los resultados obtenidos.

Durante esta actividad resulta conveniente registrar todas las
observaciones para utilizarlas en los siguientes laboratorios.

------------------------------------------------------------------------

# Validación

El laboratorio se considera exitoso cuando:

-   el modelo responde correctamente;
-   la aplicación recibe la respuesta sin errores;
-   el tiempo de inferencia queda registrado;
-   el comportamiento puede reproducirse en una nueva ejecución.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Qué parte del flujo presentó mayor complejidad?
-   ¿Qué ocurriría si el modelo no estuviera disponible?
-   ¿Qué componentes podrían reemplazarse sin modificar la aplicación?
-   ¿Cómo afectaría un modelo de mayor tamaño al tiempo de respuesta?

------------------------------------------------------------------------

# Desafíos opcionales

-   Probar distintos modelos locales.
-   Comparar tiempos de inferencia.
-   Registrar consumo de memoria y CPU.
-   Ejecutar el laboratorio desde otra máquina de la red.

------------------------------------------------------------------------

# Ideas clave

-   El laboratorio establece la base para todos los ejercicios
    posteriores.
-   Comprender el flujo de integración resulta más importante que la
    herramienta utilizada.
-   Las mediciones obtenidas servirán como línea base para futuras
    comparaciones.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección ampliaremos esta solución incorporando parámetros
de inferencia y analizando cómo pequeñas modificaciones producen
respuestas significativamente diferentes.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
