# Capítulo 5 --- Sección 05 de 10

# Evaluación continua: garantizando calidad en plataformas de IA

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Una plataforma de IA no puede considerarse estable porque una
> demostración funcionó. Debe demostrar su calidad de manera continua."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender por qué la evaluación continua es un pilar de LLMOps.
-   Diferenciar pruebas funcionales, técnicas y operativas.
-   Diseñar pipelines automáticos de validación.
-   Incorporar métricas de calidad, costo, rendimiento y seguridad.

------------------------------------------------------------------------

# Introducción

En el desarrollo tradicional, una batería de pruebas permite detectar
errores antes del despliegue.

Las plataformas de IA presentan un desafío adicional.

Una modificación aparentemente menor ---como cambiar un prompt, un
modelo de embeddings o una estrategia de recuperación--- puede alterar
significativamente el comportamiento del sistema.

Por ello, la evaluación debe integrarse en todo el ciclo de vida.

------------------------------------------------------------------------

# ¿Qué debe evaluarse?

Una solución moderna combina múltiples componentes.

Cada uno requiere validaciones específicas.

-   modelos fundacionales;
-   prompts;
-   pipelines RAG;
-   agentes;
-   herramientas;
-   memoria;
-   políticas de seguridad;
-   integración con sistemas externos.

La plataforma debe medir el comportamiento del conjunto y no únicamente
de cada componente aislado.

------------------------------------------------------------------------

# Dimensiones de evaluación

## Calidad funcional

Verifica que las respuestas satisfagan los objetivos del negocio.

## Rendimiento

Analiza latencia, concurrencia y utilización de recursos.

## Costos

Evalúa consumo de tokens, llamadas a modelos y utilización de
infraestructura.

## Seguridad

Comprueba cumplimiento de políticas, permisos y protección de datos.

## Robustez

Valida el comportamiento frente a entradas ambiguas, incompletas o
maliciosas.

------------------------------------------------------------------------

# Datasets de evaluación

Las pruebas deben ejecutarse sobre conjuntos representativos.

Conviene incluir:

-   consultas frecuentes;
-   casos límite;
-   escenarios sin respuesta;
-   intentos de prompt injection;
-   documentos desactualizados;
-   ejemplos reales del negocio.

Estos datasets evolucionan junto con la plataforma.

------------------------------------------------------------------------

# Automatización

Las evaluaciones pueden incorporarse al pipeline de despliegue.

``` mermaid
flowchart LR

DEV[Cambio]
--> BUILD[Construcción]

BUILD --> TEST[Evaluaciones automáticas]

TEST --> MET[Métricas]

MET -->|Aprobado| DEPLOY[Producción]

MET -->|Falló| FIX[Corrección]
```

El despliegue solo debería continuar cuando las métricas cumplen los
criterios definidos por la organización.

------------------------------------------------------------------------

# Detección de regresiones

No todas las mejoras producen mejores resultados.

Puede ocurrir que una nueva versión:

-   reduzca la precisión;
-   incremente costos;
-   aumente la latencia;
-   degrade la recuperación documental.

Comparar automáticamente versiones permite detectar estas regresiones
antes de afectar a los usuarios.

------------------------------------------------------------------------

# Métricas habituales

Una plataforma puede registrar indicadores como:

-   precisión de recuperación;
-   exactitud de respuestas;
-   tiempo promedio de inferencia;
-   consumo de tokens;
-   costo por solicitud;
-   porcentaje de errores;
-   utilización de herramientas;
-   satisfacción del usuario;
-   tasa de intervención humana.

Las métricas deben relacionarse con objetivos de negocio y no únicamente
con indicadores técnicos.

------------------------------------------------------------------------

# Caso de estudio

Un equipo modifica el algoritmo de *chunking* para reducir el número de
fragmentos indexados.

Las pruebas muestran una reducción del costo de almacenamiento.

Sin embargo, el pipeline automático detecta una caída significativa en
Recall@10 y un aumento en las respuestas incompletas.

La actualización se detiene antes del despliegue.

El problema se identifica durante la validación y no en producción.

------------------------------------------------------------------------

# Buenas prácticas

-   Automatizar todas las evaluaciones repetitivas.
-   Comparar siempre contra una línea base conocida.
-   Mantener datasets representativos.
-   Medir simultáneamente calidad, rendimiento y costos.
-   Versionar resultados de evaluación.
-   Incorporar pruebas de seguridad y resiliencia.

------------------------------------------------------------------------

# Ideas clave

-   La evaluación continua forma parte del ciclo de vida de la
    plataforma.
-   Calidad, costo y rendimiento deben analizarse conjuntamente.
-   La automatización reduce el riesgo de regresiones.
-   Las métricas deben reflejar el valor entregado al negocio.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos la observabilidad de plataformas de
IA, analizando trazas, métricas, registros, costos y monitoreo para
operar soluciones empresariales con criterios de confiabilidad.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
