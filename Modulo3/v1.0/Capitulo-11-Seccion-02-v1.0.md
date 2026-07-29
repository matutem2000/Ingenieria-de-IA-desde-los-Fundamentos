# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 02: El ciclo de vida del software asistido por IA

El ciclo de vida del software — el recorrido desde la captura de un requisito hasta el mantenimiento del sistema en producción — es el marco organizador de este capítulo. No porque el ciclo de vida sea el único modo de organizar el trabajo de desarrollo, sino porque cada fase plantea un problema de contexto diferente, y el AI Engineer necesita comprender esas diferencias antes de diseñar cualquier solución.

Esta sección establece el mapa conceptual del capítulo: qué ocurre en cada fase, qué tipo de contexto requiere la IA para asistir de manera útil en esa fase, y cuáles son las señales que indican que el contexto no está siendo diseñado correctamente.

### Las fases del ciclo y sus demandas de contexto

El ciclo de vida del software moderno incluye seis fases principales desde la perspectiva de la asistencia con IA. Cada una tiene un perfil de contexto característico.

**Análisis y relevamiento.** El equipo trabaja con requisitos ambiguos, conversaciones con stakeholders, documentos de negocio y restricciones del sistema existente. La IA puede asistir en la structuración y síntesis de esta información, en la identificación de contradicciones o ambigüedades, y en la generación de preguntas que el equipo no ha formulado aún. El contexto en esta fase es predominantemente texto de dominio: actas de reuniones, especificaciones funcionales, documentos de arquitectura existente, registros de decisiones. El reto es que este contexto suele ser extenso, inconsistente y no estructurado.

**Diseño y arquitectura.** El arquitecto trabaja con restricciones técnicas, patrones de diseño, capacidades del equipo y requisitos no funcionales. La IA puede asistir en la evaluación de alternativas de diseño, en la identificación de trade-offs, en la documentación de decisiones y en la verificación de consistencia entre el diseño propuesto y los principios establecidos del sistema. El contexto en esta fase incluye diagramas de arquitectura (traducidos a texto), ADRs (Architecture Decision Records), documentación de APIs existentes y convenciones del proyecto.

**Generación de código.** El desarrollador traduce diseño en implementación. La IA puede generar código, completar funciones, sugerir implementaciones alternativas. El contexto en esta fase es el más técnico y el más preciso: el módulo donde se inserta el código, las interfaces que debe satisfacer, el estilo y las convenciones del proyecto, los tests que debe pasar, las funciones relacionadas existentes. Esta es la fase donde el impacto del contexto sobre la calidad del output es más inmediato y medible.

**Pruebas y aseguramiento de calidad.** El equipo de QA (o el mismo desarrollador) verifica que el código cumple los requisitos. La IA puede asistir en la generación de casos de prueba, en la identificación de escenarios no cubiertos, en el análisis de cobertura y en la revisión de pull requests. El contexto incluye la especificación funcional, el código bajo prueba, los tests existentes y las políticas de calidad del proyecto.

**Depuración y mantenimiento.** El desarrollador investiga comportamientos inesperados en el sistema existente. La IA puede asistir en el análisis de stack traces, en la hipótesis de causas raíz, en la revisión de cambios recientes relacionados y en la sugerencia de correcciones. El contexto incluye el error observado, el stack trace completo, el código de las funciones implicadas, el historial de cambios recientes y los tests que fallan.

**Integración y despliegue.** El pipeline automatiza la verificación y entrega del software. La IA puede asistir en la revisión de configuraciones de CI/CD, en el análisis de fallos de pipeline, en la generación de documentación de release y en la evaluación de impacto de cambios. El contexto incluye los archivos de configuración del pipeline, los logs de ejecución y las políticas de deployment.

### El problema de la discontinuidad de contexto

Un patrón que aparece consistentemente en proyectos de software asistidos por IA es el de la discontinuidad de contexto: el modelo tiene acceso a información de una fase del ciclo pero no de las fases anteriores.

Un ejemplo concreto: un agente de generación de código que tiene acceso al código del módulo actual pero no a la especificación de diseño que determinó la estructura de ese módulo. El agente puede generar código que compila y pasa los tests inmediatos, pero que viola una restricción de diseño que solo estaba documentada en el ADR de la fase anterior. El código generado es técnicamente correcto en el contexto estrecho que el agente ve, pero incorrecto en el contexto más amplio del proyecto.

Este problema no es un fallo del modelo. Es un problema de diseño del sistema: el arquitecto no estableció mecanismos para que el contexto de las fases anteriores esté disponible en las fases posteriores.

```
CICLO DE VIDA Y CONTEXTO ACUMULADO

  Análisis → Diseño → Código → Pruebas → Debug → Deploy
    ↓           ↓         ↓        ↓         ↓        ↓
  Actas       ADRs     Specs   Test cases  Traces  Config
  Reqs      Diagramas  Style   Coverage   Changelogs  Logs
  Restricc.  API docs  Tests   Políticas  Stack      Policies

  CONTEXTO DISPONIBLE EN CADA FASE (sin diseño explícito):
  Solo el artefacto inmediato de esa fase.

  CONTEXTO DISPONIBLE CON DISEÑO EXPLÍCITO:
  El artefacto de la fase actual + contexto seleccionado
  de las fases anteriores relevantes para la tarea.
```

### El principio de contexto acumulado selectivo

La solución no es incluir todo el contexto de todas las fases en cada llamada al modelo — eso agotaría la ventana de contexto y degradaría la calidad del razonamiento. La solución es diseñar el sistema para que recupere el contexto de fases anteriores de manera selectiva y relevante para la tarea específica.

Cuando el agente de generación de código trabaja en una función específica, el sistema debe ser capaz de recuperar: la especificación funcional de esa función (análisis), las restricciones de diseño que aplican al módulo (diseño), el estilo de código del proyecto (documentado en la fase de diseño o en un archivo de convenciones), y los tests existentes para funciones relacionadas (fase de pruebas anteriores). Esos cuatro elementos de contexto, combinados con la petición inmediata, producen un output radicalmente mejor que la petición sin contexto adicional.

El mecanismo para lograr esto varía según la escala del proyecto: puede ser tan simple como archivos de contexto pre-seleccionados por el desarrollador, o tan sofisticado como un sistema de RAG (Retrieval-Augmented Generation) que indexa todos los artefactos del proyecto y recupera los más relevantes en tiempo real. El principio es el mismo en ambos casos.

### Herramientas del ciclo de vida y su rol en el contexto

Las herramientas que los equipos de desarrollo ya usan — control de versiones, gestores de issues, sistemas de documentación, pipelines de CI/CD — son fuentes naturales de contexto para la IA. El AI Engineer que diseña un sistema de asistencia al desarrollo aprovecha estas fuentes sin necesidad de crear repositorios de información adicionales.

El historial de commits de git es un registro de decisiones técnicas con timestamps. Los mensajes de commit bien escritos son el contexto de por qué el código cambió, no solo qué cambió. Las issues cerradas son el contexto de por qué ciertas funcionalidades existen. Los comentarios en pull requests son el contexto del razonamiento técnico del equipo. Los archivos de configuración del linter son el contexto de las convenciones de código que el proyecto adoptó.

Todas estas fuentes ya existen. El problema es que los sistemas de asistencia de IA muchas veces no las consultan. Diseñar el sistema para que las consulte selectivamente — según la tarea específica — es una de las decisiones más rentables que el AI Engineer puede tomar.

### Nota del arquitecto

Al evaluar un proyecto de integración de IA en un equipo de desarrollo, la primera pregunta que hay que hacer no es "¿qué modelo vamos a usar?". La primera pregunta es "¿qué artefactos del ciclo de vida están disponibles como fuentes de contexto?". Si los mensajes de commit son descriptivos, si los ADRs están mantenidos, si las issues están bien documentadas, el sistema tiene una base rica para construir contexto de calidad. Si el repositorio tiene commits con mensajes como "fix" o "cambios", si no hay documentación de diseño, si las issues son epics sin subdividir, el sistema estará operando con contexto pobre independientemente de cuán sofisticado sea el modelo elegido.

La calidad de la ingeniería de software que el equipo practicaba antes de introducir IA determina, en gran medida, la calidad del contexto disponible para la IA. Invertir en Context Engineering y en prácticas de documentación del ciclo de vida son inversiones sinérgicas.

La siguiente sección comienza el análisis fase a fase. El primer punto de entrada es el análisis y relevamiento: cómo construir contexto útil para la IA a partir de la información más ambigua del ciclo de vida.
