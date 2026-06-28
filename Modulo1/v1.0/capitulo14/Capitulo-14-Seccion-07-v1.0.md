# Capitulo-14-Seccion-07-v1.0

# Capítulo 14 --- Casos de Estudio de Ingeniería de Inteligencia Artificial

**Versión:** 1.0\
**Estado:** Aprobado

> *"La transformación digital del Estado requiere procesos transparentes
> antes que algoritmos sofisticados."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Analizar un caso de uso de IA en la administración pública.
-   Comprender cómo combinar eficiencia, transparencia y trazabilidad.
-   Identificar restricciones legales y organizacionales.
-   Diseñar una arquitectura que preserve el control institucional.

------------------------------------------------------------------------

# Caso de estudio 6 --- Asistente para expedientes administrativos

## Contexto

Un organismo público administra cientos de miles de expedientes por año.
Los agentes deben localizar normativa, identificar antecedentes y
clasificar documentación antes de emitir un dictamen.

La incorporación de IA busca reducir tiempos de análisis y mejorar la
consistencia de las respuestas sin reemplazar la responsabilidad del
funcionario actuante.

------------------------------------------------------------------------

# Restricciones

La solución debe respetar:

-   normativa vigente;
-   trazabilidad completa de las acciones;
-   conservación del expediente original;
-   control de accesos por perfil;
-   posibilidad de auditoría posterior.

------------------------------------------------------------------------

# Arquitectura propuesta

``` mermaid
flowchart LR
A[Agente] --> B[Portal]
B --> C[Motor RAG]
C --> D[Normativa]
C --> E[Expedientes]
C --> F[LLM]
F --> G[Sugerencias]
G --> H[Validación]
H --> I[Sistema de Gestión]
```

------------------------------------------------------------------------

# Decisiones arquitectónicas

  Decisión                           Justificación
  ---------------------------------- -----------------------------------------
  RAG sobre normativa vigente        Evitar respuestas desactualizadas
  Historial de consultas             Facilitar auditorías
  Validación obligatoria             Mantener responsabilidad administrativa
  Separación entre IA y expediente   Preservar integridad documental
  Registro de versiones              Garantizar trazabilidad

------------------------------------------------------------------------

# Resultados esperados

-   Disminución del tiempo de análisis.
-   Mayor uniformidad entre dictámenes similares.
-   Reducción de búsquedas manuales.
-   Conservación del control humano sobre cada resolución.

------------------------------------------------------------------------

# Buenas prácticas

-   Mantener actualizadas las fuentes normativas.
-   Exigir referencias documentales en todas las respuestas.
-   Monitorear indicadores de calidad y tiempos de respuesta.
-   Capacitar a los usuarios sobre las limitaciones del sistema.

------------------------------------------------------------------------

# Ideas clave

-   La IA acelera el trabajo administrativo sin reemplazar la decisión
    institucional.
-   La transparencia y la trazabilidad constituyen requisitos
    arquitectónicos.
-   Los proyectos gubernamentales requieren equilibrio entre innovación
    y cumplimiento normativo.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección analizaremos un caso de estudio correspondiente al
sector financiero, donde la Inteligencia Artificial interviene en la
detección de anomalías y el análisis de riesgo.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
