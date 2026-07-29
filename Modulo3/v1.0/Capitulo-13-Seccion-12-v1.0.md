# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 12: Checklist del AI Engineer

Este checklist recoge las verificaciones que el AI Engineer debe completar antes de lanzar un sistema de IA a producción y como parte de la operación regular. Está organizado en seis bloques que corresponden a las dimensiones del capítulo.

### Bloque 1: Diseño de la observabilidad (antes del lanzamiento)

- [ ] Las cuatro dimensiones de observabilidad están diseñadas: inferencia, contexto, calidad y comportamiento
- [ ] La instrumentación está implementada en el mismo sprint que el feature que instrumenta, no como tarea posterior
- [ ] Se han definido identificadores de traza que permiten correlacionar todos los eventos de una solicitud a través de las etapas del pipeline
- [ ] La versión del system prompt se registra en cada traza
- [ ] Los documentos recuperados se registran con sus metadatos: identificador, fuente, fecha de creación, fecha de modificación, score de relevancia
- [ ] Las herramientas ejecutadas por el agente se registran con sus parámetros y resultados
- [ ] La instrumentación tiene tests que verifican que los spans se producen correctamente
- [ ] Las consideraciones de privacidad están resueltas: qué datos de usuario se registran, durante cuánto tiempo, quién puede acceder

### Bloque 2: Métricas y umbrales (antes del lanzamiento)

- [ ] Las métricas operacionales están definidas: latencia (p50, p95, p99), TTFT, tokens por solicitud, costo por solicitud, tasa de errores técnicos
- [ ] Las métricas de calidad están definidas y son específicas para el caso de uso: qué significa "relevante" y "correcto" para este dominio
- [ ] Cada métrica tiene un umbral de alerta definido, justificado con el criterio de negocio del sistema
- [ ] Cada umbral de alerta tiene una acción asociada: quién investiga, con qué prioridad
- [ ] Los umbrales de alerta han sido validados contra el comportamiento observado del sistema en staging, no definidos en abstracto
- [ ] Se ha definido con qué frecuencia se revisarán las métricas (tiempo real, diario, semanal, mensual)

### Bloque 3: Golden set y pipeline de evaluación (antes del lanzamiento)

- [ ] El golden set está construido con participación del equipo de negocio y del dominio
- [ ] El golden set cubre los tipos de consulta más frecuentes, los casos borde conocidos, y los casos adversariales relevantes para el dominio
- [ ] El golden set incluye casos que verifican las restricciones críticas del sistema (lo que el sistema nunca debe hacer)
- [ ] El pipeline de evaluación automática (LLM-as-judge) está implementado y ejecutado sobre una muestra del tráfico
- [ ] El prompt de evaluación del LLM-as-judge está calibrado contra evaluaciones humanas de referencia
- [ ] Se ha establecido la cadencia de evaluación humana: quién evalúa, con qué frecuencia, con qué protocolo
- [ ] El proceso de medición del acuerdo entre evaluadores humanos (inter-rater reliability) está definido

### Bloque 4: Alertas y dashboards (antes del lanzamiento)

- [ ] El dashboard de guardia está disponible: muestra métricas operacionales en tiempo real con alertas visuales
- [ ] El dashboard operacional está disponible: muestra tendencias de calidad con comparación de períodos
- [ ] Cada alerta tiene un dueño asignado: una persona o equipo específico que la recibe y es responsable de responderla
- [ ] Las alertas están separadas por canal: alertas operativas (infraestructura) y alertas de calidad (equipo de IA)
- [ ] El número de alertas activas configuradas es manejable: el equipo puede atender todas las que se disparan en un día normal
- [ ] El sistema de alertas incluye contexto de diagnóstico en cada notificación, no solo el número de la métrica

### Bloque 5: Playbooks de operación (antes del lanzamiento)

- [ ] Existe un playbook para caída de calidad (groundedness o relevancia bajo umbral)
- [ ] Existe un playbook para pico de latencia
- [ ] Existe un playbook para bucle o comportamiento anómalo en agentes (si el sistema tiene componentes agentivos)
- [ ] Existe un playbook para aumento inesperado de costo
- [ ] Existe un playbook para drift del modelo (el sistema empieza a comportarse diferente sin cambios en el código)
- [ ] Los playbooks incluyen criterios explícitos para decidir si se hace rollback
- [ ] Los playbooks han sido revisados por el equipo completo y no solo por el autor
- [ ] Existe una plantilla de post-mortem que se completa después de cada incidente de Nivel 2 o superior

### Bloque 6: Operación regular (cadencia continua)

**Diariamente:**
- [ ] Revisión del dashboard de guardia: sin alertas activas o con alertas en proceso de resolución
- [ ] Verificación de que el pipeline de evaluación automática ejecutó sin errores

**Semanalmente:**
- [ ] Revisión del dashboard operacional: tendencias de métricas de calidad y operacionales
- [ ] Revisión de los casos con peores scores de la semana: ¿hay un patrón? ¿hay una hipótesis de mejora?
- [ ] Revisión de los incidentes de la semana (si los hubo): ¿el playbook funcionó? ¿necesita actualizarse?
- [ ] Verificación de la antigüedad promedio de los documentos recuperados: ¿hay documentos que debería actualizarse?

**Mensualmente:**
- [ ] Ejecución del golden set y comparación con la línea base de lanzamiento
- [ ] Calibración del evaluador automático contra evaluaciones humanas
- [ ] Revisión del golden set: ¿sigue siendo representativo del uso actual del sistema?
- [ ] Análisis de tendencias a largo plazo: ¿el sistema está mejorando, estable o deteriorando?
- [ ] Revisión del costo acumulado del sistema y comparación con el valor de negocio generado
- [ ] Actualización del plan de optimización del próximo ciclo basada en los datos del mes

**Ante cada cambio en el sistema:**
- [ ] El golden set se ejecuta en staging antes de desplegar a producción
- [ ] Las métricas se comparan entre la versión nueva y la versión actual
- [ ] El cambio se documenta con la justificación, el resultado esperado y el resultado observado
- [ ] Se define el período de monitoreo intensivo posterior al cambio y el responsable de ese monitoreo

### Criterio de preparación para producción

Un sistema de IA está listo para producción desde la perspectiva de la observabilidad cuando puede responder afirmativamente a las siguientes preguntas:

1. Si el sistema produce una respuesta incorrecta ahora mismo, ¿el equipo puede saberlo en menos de 24 horas?
2. Si el equipo detecta una respuesta incorrecta, ¿puede diagnosticar la causa raíz en menos de 2 horas?
3. Si el sistema se degrada gradualmente durante cuatro semanas, ¿hay un mecanismo que lo detecte antes de que el impacto en los usuarios sea significativo?
4. ¿Hay un responsable definido para cada tipo de alerta que el sistema puede generar?
5. ¿Sabe el equipo qué acción tomar cuando cada tipo de alerta se dispara?

Si alguna de estas preguntas recibe una respuesta negativa, el sistema tiene una brecha de observabilidad que debe corregirse antes del lanzamiento, no después.
