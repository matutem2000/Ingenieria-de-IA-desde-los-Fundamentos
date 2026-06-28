# Capitulo-15-Seccion-07-v1.0

# Capítulo 15 --- Evaluación Final y Proyecto Integrador

**Versión:** 1.0\
**Estado:** Aprobado

> *"La excelencia operacional no aparece después del despliegue; debe
> diseñarse desde el primer día."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Diseñar la estrategia de operación del proyecto integrador.
-   Definir métricas e indicadores para una solución empresarial de IA.
-   Comprender el papel de la observabilidad y la mejora continua.
-   Incorporar prácticas de gobierno para modelos y datos.

------------------------------------------------------------------------

# Estrategia de operación

Una solución basada en Inteligencia Artificial no finaliza cuando entra
en producción. A partir de ese momento comienza una etapa permanente de
monitoreo, evaluación y evolución.

La operación debe garantizar que el sistema continúe aportando valor aun
cuando cambien los modelos, la documentación o las necesidades del
negocio.

------------------------------------------------------------------------

# Flujo operativo

``` mermaid
flowchart LR
A[Usuarios] --> B[Aplicación]
B --> C[Métricas]
B --> D[Logs]
B --> E[Trazas]
C --> F[Observabilidad]
D --> F
E --> F
F --> G[Alertas]
G --> H[Equipo de Operación]
H --> I[Mejora Continua]
I --> B
```

------------------------------------------------------------------------

# Indicadores recomendados

  Indicador                  Objetivo
  -------------------------- -------------------------------
  Latencia promedio          Medir experiencia del usuario
  Disponibilidad             Garantizar continuidad
  Precisión de respuestas    Evaluar calidad funcional
  Uso de contexto            Detectar problemas en RAG
  Costo por consulta         Controlar eficiencia
  Satisfacción del usuario   Medir valor generado

------------------------------------------------------------------------

# Gobierno del sistema

La operación deberá contemplar:

-   versionado de modelos;
-   versionado de prompts;
-   actualización del conocimiento documental;
-   revisión periódica de métricas;
-   auditoría de accesos;
-   gestión de incidentes.

------------------------------------------------------------------------

# Buenas prácticas

-   Definir umbrales de alerta antes del despliegue.
-   Automatizar la recolección de métricas.
-   Mantener tableros de observabilidad accesibles.
-   Documentar todas las modificaciones relevantes.
-   Revisar periódicamente el comportamiento del sistema.

------------------------------------------------------------------------

# Ideas clave

-   Operar una solución de IA implica mucho más que mantener servidores
    activos.
-   La observabilidad permite detectar degradaciones antes de que
    afecten al negocio.
-   La mejora continua constituye una responsabilidad permanente del
    equipo de ingeniería.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección se realizará el cierre del proyecto integrador,
consolidando las lecciones aprendidas y estableciendo una metodología
para abordar futuros proyectos de Ingeniería de Inteligencia Artificial.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
