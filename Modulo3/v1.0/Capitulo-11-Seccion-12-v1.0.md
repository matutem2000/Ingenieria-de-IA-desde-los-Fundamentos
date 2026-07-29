# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 12: Checklist del AI Engineer

Este checklist está diseñado para uso práctico: puede imprimirse, adaptarse al contexto específico del proyecto e incorporarse a los procesos del equipo. Cubre las decisiones de Context Engineering en cada fase del ciclo de vida del software.

### Checklist de configuración inicial del proyecto

Antes de comenzar a usar asistencia de IA en un proyecto de software, verificar:

**Documentación base del proyecto**
- [ ] Existe un archivo de instrucciones del proyecto (`.claude/project.md`, `CONTEXT.md` o equivalente) en el repositorio
- [ ] El archivo documenta el stack tecnológico con versiones específicas
- [ ] El archivo documenta las convenciones de código del equipo
- [ ] El archivo documenta los patrones de diseño adoptados
- [ ] El archivo incluye instrucciones específicas para el asistente (qué hacer y qué no hacer)
- [ ] El archivo está configurado para ser incluido automáticamente en el IDE del equipo
- [ ] Existe un proceso para mantener el archivo actualizado cuando cambian las convenciones

**Configuración del repositorio como fuente de contexto**
- [ ] Los mensajes de commit del equipo siguen una convención descriptiva (no mensajes como "fix" o "changes")
- [ ] Los ADRs del proyecto están disponibles en el repositorio (no solo en wikis externos)
- [ ] Existe documentación de las convenciones de testing (frameworks, estructura de tests, uso de mocks)
- [ ] El README del proyecto describe la estructura del repositorio de manera que el modelo pueda orientarse

**Preparación del pipeline de CI/CD**
- [ ] El pipeline proporciona contexto suficiente para las tareas de IA que ejecuta (diff, resultados de tests previos, políticas del equipo)
- [ ] Las revisiones automáticas de IA generan comentarios en el PR, no decisiones de merge automáticas
- [ ] Existe un proceso para evaluar los findings de la revisión automática

### Checklist por fase del ciclo de vida

**Análisis y relevamiento**
- [ ] El contexto de la sesión incluye las transcripciones o documentos fuente relevantes (no solo las preguntas)
- [ ] Se identificaron explícitamente qué documentos son de análisis de la tarea actual vs. documentos de otro dominio
- [ ] Los outputs del análisis asistido (especificaciones, user stories) fueron validados con stakeholders antes de cerrar la fase
- [ ] Los artefactos de análisis están en formato que las fases posteriores puedan usar como contexto

**Diseño y arquitectura**
- [ ] El contexto de las sesiones de diseño incluye los ADRs relevantes del proyecto
- [ ] Los principios arquitectónicos establecidos del proyecto están en el contexto antes de pedir evaluación de alternativas
- [ ] Las restricciones no funcionales (latencia, throughput, presupuesto) están documentadas y accesibles al modelo
- [ ] Los borradores de ADRs generados por IA fueron revisados por el arquitecto antes de ser aprobados
- [ ] Se verificó que el diseño propuesto es consistente con los requisitos funcionales del análisis

**Generación de código**
- [ ] El módulo destino del código está abierto/seleccionado en el IDE
- [ ] Las clases del dominio que el código debe usar están en el contexto
- [ ] Los tests que el código debe pasar están en el contexto (o se generaron como primer paso)
- [ ] Las convenciones del proyecto están en el contexto (via archivo de instrucciones o selección manual)
- [ ] El código generado pasó el linter antes de ser evaluado por el desarrollador
- [ ] El código generado tiene al menos una revisión humana antes de incluirse en el PR

**Pruebas y QA**
- [ ] Los tests se generan con la especificación funcional en el contexto, no solo el código
- [ ] Los tests existentes del módulo están en el contexto para evitar duplicación
- [ ] Los tests generados verifican comportamiento contra especificación (no solo que el código no lanza excepciones)
- [ ] Los casos borde identificados por el modelo fueron evaluados manualmente para determinar cuáles son relevantes
- [ ] El contexto de revisión de PR incluye el diff + funciones afectadas + requisito motivador + guías del proyecto

**Depuración**
- [ ] El contexto de diagnóstico incluye: comportamiento observado vs. esperado (no solo el mensaje de error)
- [ ] El stack trace completo está en el contexto
- [ ] El código de las funciones que aparecen en el stack trace está en el contexto
- [ ] El git log reciente de los archivos afectados está en el contexto
- [ ] Los tests que fallan están en el contexto
- [ ] Las hipótesis de causa raíz generadas por el modelo fueron verificadas localmente antes de aplicar fixes
- [ ] Se escribió un test de regresión para el bug antes de cerrar el fix

**Integración y despliegue**
- [ ] El pipeline incluye el diff del cambio como contexto para cualquier tarea de IA
- [ ] Los resultados de pasos anteriores del pipeline están disponibles como contexto para pasos posteriores
- [ ] Las políticas de merge del equipo están documentadas y accesibles al modelo
- [ ] Los logs de fallo del pipeline incluyen suficiente contexto para diagnóstico asistido

### Checklist de calidad del sistema de asistencia

Para evaluar periódicamente si el sistema de Context Engineering está funcionando:

**Señales de salud**
- [ ] La tasa de aceptación del código generado sin modificaciones significativas es creciente
- [ ] Los comentarios de revisión de IA son específicos al proyecto (no genéricos)
- [ ] El tiempo de diagnóstico de incidentes se redujo respecto al baseline
- [ ] El equipo usa las herramientas de IA para tareas complejas, no solo para completado trivial
- [ ] Los desarrolladores nuevos en el proyecto usan el asistente productivamente desde las primeras semanas

**Señales de alerta**
- [ ] Los desarrolladores reportan que el código generado "no sirve para nuestro proyecto"
- [ ] Hay reglas informales de "no usar IA para el módulo X"
- [ ] Los falsos positivos de la revisión automática superan el 20% de los comentarios
- [ ] El archivo de instrucciones del proyecto no ha sido actualizado en más de 3 meses
- [ ] El código de producción contiene bugs cuya causa raíz fue un fix de IA no revisado

**Acciones de mantenimiento**
- [ ] El archivo de instrucciones del proyecto se revisa cuando se adoptan nuevas convenciones
- [ ] El equipo tiene una retrospectiva periódica sobre el uso de herramientas de IA (mensual o por sprint)
- [ ] Las métricas de uso y calidad del sistema se miden y comparten con el equipo

### Preguntas de diagnóstico para el AI Engineer

Cuando el sistema de asistencia no está produciendo los resultados esperados, estas preguntas ayudan a identificar el problema:

1. ¿El modelo tiene acceso a las convenciones del proyecto? Si el código generado viola las convenciones, probablemente no las tiene.

2. ¿El modelo tiene acceso a las clases del dominio que debe usar? Si el código generado inventa sus propias estructuras de datos, probablemente no las tiene.

3. ¿El modelo tiene acceso a las restricciones de la tarea? Si el código generado ignora casos borde documentados en la especificación, esa especificación no está en el contexto.

4. ¿El modelo tiene demasiado contexto irrelevante? Si las respuestas son lentas, genéricas o parecen no leer el contexto específico de la pregunta, puede haber exceso de contexto.

5. ¿El flujo de revisión está funcionando? Si los bugs de IA llegan a producción, el problema puede no ser el modelo sino la ausencia de revisión antes de la integración.

### Nota del arquitecto

Este checklist está diseñado para ser adaptado, no seguido mecánicamente. Cada proyecto tiene un contexto diferente: lo que es crítico en un equipo de 5 personas que trabaja en un microservicio puede ser excesivo para un equipo de 30 que trabaja en un monolito complejo. El AI Engineer debe identificar qué puntos del checklist tienen mayor impacto en su contexto específico y comenzar por ahí.

La siguiente sección resume las ideas centrales del capítulo para consolidar el aprendizaje.
