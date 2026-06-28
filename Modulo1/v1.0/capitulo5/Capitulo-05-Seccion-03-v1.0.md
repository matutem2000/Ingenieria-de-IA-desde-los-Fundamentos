# Capítulo 5 --- Sección 03 de 10

# Gestión del ciclo de vida de los modelos

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Elegir un modelo es una decisión técnica. Administrar cientos de
> versiones de modelos es una disciplina de ingeniería."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender el ciclo de vida de un modelo dentro de una plataforma de
    IA.
-   Entender por qué el versionado va más allá del código fuente.
-   Conocer estrategias de despliegue y reemplazo de modelos.
-   Incorporar criterios para operar múltiples modelos en producción.

------------------------------------------------------------------------

# Introducción

En una aplicación tradicional, actualizar una dependencia suele implicar
recompilar y desplegar una nueva versión del software.

En una plataforma de IA el problema es más complejo.

El comportamiento del sistema puede cambiar simplemente por reemplazar
el modelo fundacional, modificar su configuración o utilizar una versión
diferente del mismo proveedor.

Por esta razón, los modelos deben administrarse como activos de la
plataforma.

------------------------------------------------------------------------

# El ciclo de vida de un modelo

Un modelo atraviesa normalmente las siguientes etapas:

1.  Evaluación inicial.
2.  Incorporación al catálogo.
3.  Validación técnica.
4.  Despliegue controlado.
5.  Operación y monitoreo.
6.  Reemplazo o retiro.

Cada etapa requiere criterios objetivos y evidencia medible.

------------------------------------------------------------------------

# Versionado

Versionar un modelo implica registrar mucho más que su nombre.

Conviene conservar información como:

-   proveedor;
-   versión exacta;
-   fecha de incorporación;
-   parámetros de configuración;
-   ventana de contexto;
-   costos;
-   capacidades soportadas;
-   limitaciones conocidas.

Esta información facilita auditorías y reproduce resultados históricos.

------------------------------------------------------------------------

# Compatibilidad

Cambiar un modelo puede afectar:

-   calidad de las respuestas;
-   formato de salida;
-   consumo de tokens;
-   latencia;
-   uso de herramientas;
-   comportamiento de agentes.

Por ello es recomendable definir contratos entre la aplicación y el
modelo.

La plataforma debería permitir sustituir un modelo sin modificar el
resto de la arquitectura.

------------------------------------------------------------------------

# Estrategias de despliegue

Una actualización no siempre debe llegar simultáneamente a todos los
usuarios.

Entre las estrategias más utilizadas se encuentran:

## Blue/Green

Dos entornos idénticos conviven temporalmente.

El tráfico se redirige al nuevo entorno únicamente cuando las
validaciones resultan satisfactorias.

## Canary

Un porcentaje reducido de usuarios utiliza inicialmente la nueva
versión.

Si las métricas son correctas, el despliegue se amplía progresivamente.

## Rollback

Toda actualización debe contemplar un mecanismo de retorno rápido a la
versión anterior.

------------------------------------------------------------------------

# Evaluación continua

Antes y después del despliegue conviene medir:

-   precisión;
-   costo por consulta;
-   tiempo de respuesta;
-   consumo de tokens;
-   utilización de herramientas;
-   satisfacción del usuario;
-   estabilidad operativa.

La decisión de adoptar un nuevo modelo debe basarse en evidencia y no
únicamente en anuncios del mercado.

------------------------------------------------------------------------

# Catálogo de modelos

Las organizaciones maduras suelen disponer de varios modelos
simultáneamente.

Por ejemplo:

-   uno optimizado para razonamiento complejo;
-   otro especializado en generación de código;
-   un modelo pequeño para tareas de clasificación;
-   modelos locales para información sensible.

El catálogo permite seleccionar el modelo más adecuado para cada caso de
uso.

------------------------------------------------------------------------

``` mermaid
flowchart LR

A[Evaluación]
--> B[Catálogo]

B --> C[Pruebas]

C --> D[Despliegue]

D --> E[Monitoreo]

E --> F[Reemplazo]

F --> B
```

------------------------------------------------------------------------

# Caso de estudio

Una empresa reemplaza su modelo principal por una versión más reciente.

Las pruebas funcionales son satisfactorias, pero el costo por millón de
tokens aumenta un 60 % y la latencia se incrementa de forma
significativa.

Gracias a una estrategia *canary*, solo una pequeña fracción de usuarios
experimenta el cambio.

Las métricas permiten revertir el despliegue antes de afectar al resto
de la organización.

------------------------------------------------------------------------

# Buenas prácticas

-   Mantener un catálogo centralizado de modelos.
-   Versionar configuraciones y capacidades.
-   Automatizar pruebas antes del despliegue.
-   Implementar estrategias de despliegue gradual.
-   Medir continuamente rendimiento y costos.
-   Disponer siempre de un mecanismo de rollback.

------------------------------------------------------------------------

# Ideas clave

-   Los modelos forman parte del ciclo de vida de la plataforma.
-   Versionar un modelo implica registrar contexto técnico y operativo.
-   Blue/Green, Canary y Rollback reducen riesgos.
-   La selección de un modelo debe apoyarse en métricas objetivas.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos la gestión de prompts como activos
de ingeniería, incluyendo versionado, pruebas, reutilización y
estrategias para mantener consistencia entre múltiples aplicaciones y
agentes.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
