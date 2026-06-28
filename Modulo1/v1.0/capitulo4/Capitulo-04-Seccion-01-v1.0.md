# Capítulo 4 --- Sección 01 de 10

# Agentes de IA: del procesamiento del lenguaje a la ejecución de tareas

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un modelo responde preguntas. Un agente persigue objetivos."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué es un agente de IA desde una perspectiva de
    ingeniería.
-   Diferenciar un LLM de un agente.
-   Entender por qué los agentes representan una evolución
    arquitectónica y no un nuevo tipo de modelo.
-   Identificar los componentes básicos de un sistema basado en agentes.

------------------------------------------------------------------------

# Introducción

Hasta este punto del libro analizamos cómo un Large Language Model
interpreta instrucciones, genera texto y, mediante arquitecturas RAG,
utiliza conocimiento externo para responder consultas fundamentadas.

Sin embargo, muchas aplicaciones empresariales requieren algo más que
generar respuestas.

Un asistente puede explicar cómo crear un usuario.

Un agente puede crear ese usuario.

Un asistente puede describir el procedimiento para generar un informe.

Un agente puede consultar distintos sistemas, consolidar la información
y entregar el informe terminado.

La diferencia ya no reside únicamente en comprender lenguaje.

Reside en actuar sobre el entorno.

------------------------------------------------------------------------

# El cambio de paradigma

Durante los primeros años de la IA generativa, la interacción seguía un
patrón simple:

1.  El usuario formula un objetivo.
2.  El modelo interpreta la solicitud.
3.  El sistema ejecuta una o más acciones.
4.  El resultado se valida y se devuelve al usuario.

Los agentes incorporan capacidades de planificación, uso de
herramientas, memoria y ejecución coordinada.

------------------------------------------------------------------------

# ¿Qué es un agente?

Desde una perspectiva de ingeniería, un agente es un sistema capaz de
perseguir un objetivo mediante la combinación de razonamiento, memoria,
herramientas y capacidad de ejecución.

El modelo de lenguaje continúa siendo un componente fundamental.

Sin embargo, ya no constituye todo el sistema.

El agente incorpora una capa de orquestación que coordina el resto de
los componentes.

------------------------------------------------------------------------

# Componentes principales

Una arquitectura basada en agentes suele incluir:

-   un modelo de lenguaje;
-   memoria;
-   herramientas (*tools*);
-   conectores hacia sistemas externos;
-   un planificador;
-   un orquestador;
-   mecanismos de observabilidad;
-   políticas de seguridad.

Cada componente posee una responsabilidad claramente definida.

------------------------------------------------------------------------

# Un ejemplo

Solicitud:

> "Prepará el informe mensual de ventas y enviáselo al director
> financiero."

Un agente podría:

1.  Consultar el ERP.
2.  Obtener las ventas del período.
3.  Generar gráficos.
4.  Redactar un resumen.
5.  Enviar el correo.
6.  Registrar la auditoría.

------------------------------------------------------------------------

``` mermaid
flowchart LR
U[Usuario] --> O[Orquestador]
O --> L[LLM]
O --> M[Memoria]
O --> T[Herramientas]
T --> ERP[ERP]
T --> API[APIs]
L --> O
M --> O
O --> R[Resultado]
```

------------------------------------------------------------------------

# Ideas clave

-   Un agente busca cumplir objetivos.
-   El LLM es solo uno de sus componentes.
-   Herramientas, memoria y planificación amplían sus capacidades.
-   La arquitectura determina el comportamiento final.

------------------------------------------------------------------------

## Próxima sección

Analizaremos la arquitectura interna de un agente moderno y el ciclo
completo de planificación y ejecución.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
