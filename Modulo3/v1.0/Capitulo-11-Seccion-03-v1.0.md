# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 03: Contexto para análisis y relevamiento

La fase de análisis y relevamiento es donde el proyecto toma forma. El equipo trabaja con información heterogénea — conversaciones con usuarios, documentos de negocio, sistemas existentes, restricciones legales, objetivos estratégicos — y debe convertirla en especificaciones que el equipo técnico pueda implementar. Es la fase con mayor ambigüedad y, paradójicamente, donde las decisiones tienen mayor impacto en el costo total del proyecto.

La IA puede asistir en esta fase de maneras concretas y de alto valor. Pero solo si el contexto está bien diseñado. Esta sección describe cómo construir ese contexto.

### El problema del análisis sin asistencia

Los analistas y product owners trabajan típicamente con grandes volúmenes de información: grabaciones de entrevistas, correos con stakeholders, documentos de requerimientos de versiones anteriores, reportes de problemas de usuarios y actas de reuniones. Sintetizar toda esa información en requisitos funcionales coherentes, sin contradicciones y con criterios de aceptación claros, es un trabajo que consume semanas.

La IA puede acelerar ese proceso — pero solo si tiene acceso al material de entrada. Un analista que le pregunta al modelo "¿cuáles son los requisitos para el módulo de pagos?" sin proporcionarle ningún documento previo recibirá una respuesta genérica sobre módulos de pagos típicos. Útil como punto de partida, pero no específica para el proyecto.

### Las fuentes de contexto en la fase de análisis

El contexto para la IA en la fase de análisis proviene de cuatro fuentes principales:

**Entrevistas y sesiones de relevamiento.** Las transcripciones de entrevistas con usuarios y stakeholders son una fuente densa de información sobre requisitos reales. Cuando el modelo tiene acceso a estas transcripciones, puede identificar patrones repetidos ("el stakeholder A y el stakeholder C mencionan el mismo problema de tres formas diferentes"), contradicciones ("el departamento de ventas quiere X, el departamento de operaciones quiere lo opuesto"), y preguntas sin respuesta ("nadie mencionó cómo manejar el caso en que el usuario no tiene conexión").

**Documentos de negocio.** Contratos de servicio, regulaciones aplicables, políticas internas, documentación del sistema legado — todos estos son restricciones que el sistema debe respetar. La IA, con acceso a estos documentos, puede verificar que las especificaciones que el equipo está generando no violen restricciones que están documentadas pero que el analista puede haber pasado por alto.

**Sistema existente.** Si hay un sistema previo (legado o versión anterior), el código y la documentación de ese sistema son contexto invaluable. El modelo puede analizar el sistema existente para identificar funcionalidades implícitas que no están documentadas pero que los usuarios conocen y esperan que se preserven.

**Decisiones anteriores.** Los ADRs y registros de decisiones de proyectos anteriores del mismo equipo o dominio son contexto estratégico: qué alternativas fueron evaluadas y descartadas, por qué razones, con qué restricciones. Evitan que el equipo repierta debates que ya tuvo.

### Cómo estructurar el contexto de análisis

La ventana de contexto de cualquier modelo tiene límites. Para proyectos grandes, la suma de todas las fuentes anteriores excede con creces esa ventana. El AI Engineer necesita una estrategia de selección.

El principio general es el de relevancia para la tarea específica. No se incluye "toda la documentación del proyecto" en el contexto — se incluye la documentación relevante para la tarea que se está ejecutando en ese momento.

```
TAREA: Identificar contradicciones en los requisitos del módulo de notificaciones

CONTEXTO RELEVANTE:
  ✓ Acta de reunión con el equipo de marketing (mencionan notificaciones push)
  ✓ Acta de reunión con el equipo de legal (restricciones de consentimiento GDPR)
  ✓ Issues del sistema actual relacionadas con notificaciones
  ✓ Especificación funcional de notificaciones v1.0 (versión anterior)

CONTEXTO NO INCLUIDO:
  ✗ Actas de reuniones sobre el módulo de pagos (diferente dominio)
  ✗ Contratos de proveedores de infraestructura (no relevante para esta tarea)
  ✗ Código del sistema legado (para análisis, no es la fuente primaria)
```

Este esquema de selección puede ser manual — el analista selecciona los documentos relevantes antes de la sesión — o automatizado mediante un sistema de RAG que indexa todos los artefactos del proyecto y recupera los más similares semánticamente a la tarea.

### El modelo como amplificador del analista, no como reemplazo

Es importante establecer con precisión el rol del modelo en la fase de análisis. El modelo no reemplaza al analista. No tiene el juicio de negocio, el conocimiento tácito de la organización ni la capacidad de evaluar la viabilidad política de una especificación. Lo que puede hacer es amplificar la capacidad del analista en tres dimensiones:

**Síntesis de volumen.** El analista puede darle al modelo 50 páginas de transcripciones y pedirle que identifique los temas recurrentes, las contradicciones y las preguntas sin respuesta. Esto reduce semanas de trabajo manual a horas.

**Exhaustividad.** El modelo, dado un conjunto de requisitos, puede generar sistemáticamente las preguntas que el analista debería hacer para completarlos: "¿Qué ocurre si el usuario no tiene email verificado?", "¿Cómo se maneja el timeout de la sesión?", "¿Quién tiene permiso para aprobar esta acción?". El analista evalúa cuáles de esas preguntas son relevantes para el proyecto.

**Consistencia.** El modelo puede verificar si un conjunto de requisitos es internamente consistente: si el requisito A dice que solo usuarios administradores pueden hacer X, y el requisito B dice que cualquier usuario puede hacer X, hay una contradicción que el modelo puede identificar aunque esté en páginas separadas del documento.

### Ejemplo concreto: estructurar requisitos desde entrevistas

Supóngase que el equipo tiene cuatro transcripciones de entrevistas sobre un sistema de gestión de tickets de soporte. El analista construye el siguiente contexto para el modelo:

```
CONTEXTO:
[Transcripción entrevista 1 - Agente de soporte senior]
[Transcripción entrevista 2 - Supervisor de soporte]
[Transcripción entrevista 3 - Cliente corporativo]
[Transcripción entrevista 4 - Director de operaciones]

REQUISITOS ACTUALES BORRADORES:
[5 requisitos que el analista ya tiene documentados]

TAREA:
Basándote en las transcripciones y los requisitos borradores:
1. Identifica requisitos implícitos que los entrevistados mencionan
   pero que no están en los borradores.
2. Identifica contradicciones entre lo que dijeron distintos entrevistados.
3. Lista las 10 preguntas más importantes que el equipo debería
   responder antes de cerrar el análisis.
```

El output de este prompt, con contexto bien construido, puede ahorrarle al analista dos o tres días de trabajo de síntesis. Sin el contexto de las transcripciones, el output sería genérico e inútil.

### Artefactos de salida del análisis como contexto para fases posteriores

Los artefactos que produce la fase de análisis — especificaciones funcionales, user stories, criterios de aceptación, restricciones documentadas — se convierten en contexto para todas las fases posteriores. Este es el primer eslabón de la cadena de contexto acumulado.

Si los criterios de aceptación están bien formulados en esta fase, la fase de pruebas tiene un contexto claro para la generación de casos de test. Si las restricciones de negocio están explícitamente documentadas, la fase de diseño tiene el contexto necesario para evaluar alternativas de arquitectura. Si las user stories incluyen casos borde, la fase de generación de código tiene el contexto para manejar esos casos.

La calidad del análisis y la calidad del contexto que produce para las fases posteriores son la misma cosa, vista desde ángulos distintos.

### Nota del arquitecto

El riesgo más alto en el uso de IA en la fase de análisis no es que el modelo genere especificaciones incorrectas — esas se verifican con los stakeholders. El riesgo más alto es que el equipo tome las especificaciones generadas por IA como un primer borrador incompleto y no las someta a la validación con usuarios reales. La IA puede identificar preguntas que el analista no hizo, pero no puede responderlas. Solo los stakeholders pueden hacerlo.

El flujo correcto es: IA genera borrador a partir del contexto disponible → analista revisa y valida con stakeholders → diferencias entre borrador y validación revelan puntos de ambigüedad → IA ayuda a resolverlos → ciclo continúa hasta que el análisis está completo.

La siguiente sección avanza a la fase de diseño y arquitectura: cómo construir el contexto para que la IA asista en decisiones técnicas sin suplantar el juicio del arquitecto de software.
