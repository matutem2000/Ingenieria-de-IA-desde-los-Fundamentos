# Capítulo 5 --- Sección 06 de 10

# Observabilidad en plataformas de IA: comprender el comportamiento del sistema

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Si una plataforma de IA no puede explicar qué hizo, cuándo lo hizo y
> por qué lo hizo, no está preparada para producción."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender la importancia de la observabilidad en plataformas de IA.
-   Diferenciar logs, métricas y trazas distribuidas.
-   Diseñar estrategias de monitoreo para modelos, agentes y sistemas
    RAG.
-   Incorporar mecanismos de detección temprana de anomalías.

------------------------------------------------------------------------

# Introducción

Toda plataforma empresarial necesita responder preguntas sobre su estado
operativo.

En una aplicación tradicional esto implica conocer el uso de CPU,
memoria, tiempos de respuesta o errores de una API.

Las plataformas de IA añaden nuevas dimensiones.

Ahora también es necesario comprender:

-   qué modelo respondió;
-   qué herramientas utilizó;
-   qué documentos recuperó;
-   cuántos tokens consumió;
-   cuál fue el costo de la operación;
-   qué decisiones tomó el agente.

Responder estas preguntas requiere una estrategia integral de
observabilidad.

------------------------------------------------------------------------

# Los tres pilares

La observabilidad moderna suele apoyarse en tres componentes
principales.

## Logs

Registran eventos relevantes ocurridos durante la ejecución.

Por ejemplo:

-   inicio de una solicitud;
-   selección del modelo;
-   invocación de herramientas;
-   errores;
-   resultados obtenidos.

## Métricas

Permiten medir el comportamiento del sistema a lo largo del tiempo.

Algunos indicadores frecuentes incluyen:

-   latencia;
-   consumo de tokens;
-   cantidad de consultas;
-   utilización de herramientas;
-   costos diarios;
-   errores por componente.

## Trazas

Las trazas permiten reconstruir el recorrido completo de una solicitud.

Resultan especialmente útiles cuando intervienen múltiples agentes,
microservicios y herramientas externas.

------------------------------------------------------------------------

# Observabilidad específica para IA

Las plataformas de IA requieren indicadores adicionales.

Entre ellos:

-   modelo utilizado;
-   versión del prompt;
-   embedding empleado;
-   estrategia de recuperación;
-   documentos recuperados;
-   cantidad de iteraciones del agente;
-   herramientas invocadas;
-   duración de cada etapa;
-   intervención humana;
-   evaluación automática obtenida.

Estos datos facilitan tanto el diagnóstico como la mejora continua.

------------------------------------------------------------------------

# Monitoreo de costos

El costo operativo constituye un aspecto central.

La plataforma debería registrar información como:

-   consumo de tokens por modelo;
-   costo por solicitud;
-   costo por usuario;
-   costo por agente;
-   utilización de GPU;
-   almacenamiento vectorial;
-   llamadas a servicios externos.

Estas métricas permiten optimizar la arquitectura y detectar
comportamientos anómalos.

------------------------------------------------------------------------

# Detección de anomalías

Una plataforma madura no espera a que un usuario reporte un problema.

Debe identificar automáticamente situaciones como:

-   aumento inesperado de latencia;
-   incremento del consumo de tokens;
-   crecimiento del porcentaje de errores;
-   disminución de la precisión;
-   uso excesivo de herramientas;
-   fallos reiterados de un proveedor externo.

La detección temprana reduce el impacto sobre el negocio.

------------------------------------------------------------------------

# Arquitectura de observabilidad

``` mermaid
flowchart LR

REQ[Solicitud]
--> ORQ[Orquestador]

ORQ --> LLM[Modelo]
ORQ --> RAG[RAG]
ORQ --> TOOLS[Herramientas]

LLM --> OBS[Observabilidad]
RAG --> OBS
TOOLS --> OBS
ORQ --> OBS

OBS --> LOGS[Logs]
OBS --> MET[Métricas]
OBS --> TRACE[Trazas]

TRACE --> DASH[Dashboard]
```

La observabilidad atraviesa toda la plataforma.

No constituye un componente aislado.

------------------------------------------------------------------------

# Caso de estudio

Una organización detecta un incremento del 40 % en el costo diario de su
plataforma.

El monitoreo revela que un agente comenzó a ejecutar innecesariamente
una herramienta de búsqueda en cada iteración del ciclo de razonamiento.

Sin observabilidad, el problema habría permanecido oculto durante
semanas.

Gracias a las trazas distribuidas y al análisis de métricas, el equipo
identifica la causa y corrige el flujo de planificación.

------------------------------------------------------------------------

# Buenas prácticas

-   Registrar únicamente la información necesaria para diagnóstico y
    auditoría.
-   Evitar almacenar datos sensibles sin protección.
-   Centralizar logs, métricas y trazas.
-   Asociar cada ejecución con su versión de modelo y prompt.
-   Construir tableros orientados al negocio y no solo a la
    infraestructura.
-   Automatizar alertas ante comportamientos anómalos.

------------------------------------------------------------------------

# Ideas clave

-   La observabilidad permite comprender el comportamiento completo de
    la plataforma.
-   Logs, métricas y trazas cumplen funciones complementarias.
-   Las plataformas de IA requieren indicadores específicos que no
    existen en aplicaciones tradicionales.
-   El monitoreo continuo facilita optimización, auditoría y control de
    costos.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos la seguridad y el gobierno de
plataformas de IA, abordando gestión de identidades, protección de
datos, aislamiento de modelos, cumplimiento normativo y políticas de uso
responsable.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
