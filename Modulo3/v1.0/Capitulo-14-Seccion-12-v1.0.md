# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 12: Checklist del AI Engineer — Seguridad en sistemas de Context Engineering

Esta lista de verificación organiza los controles de seguridad de este capítulo en tres fases del ciclo de vida de un sistema: diseño, implementación y operación. No es exhaustiva —cada sistema tiene características propias que pueden requerir controles adicionales—, pero cubre los puntos críticos que el AI Engineer debe verificar en cualquier sistema de Context Engineering que procese información sensible o sea accedido por usuarios externos.

### Fase 1: Diseño

Antes de escribir una línea de código, antes de seleccionar el stack tecnológico, el AI Engineer debe poder responder afirmativamente a estas preguntas:

**Amenazas y riesgos**
- [ ] Se ha realizado un análisis de amenazas (threat modeling) documentado para el sistema.
- [ ] Las amenazas de mayor prioridad han sido identificadas y tienen controles de mitigación diseñados.
- [ ] El perfil de riesgo del sistema ha sido categorizado (bajo / medio / alto) y revisado por el área de seguridad.

**Principio del mínimo privilegio**
- [ ] Las herramientas disponibles para el agente son las estrictamente necesarias para la función del sistema, no todas las técnicamente posibles.
- [ ] Los datos a los que puede acceder el sistema RAG están limitados al mínimo necesario para la función.
- [ ] Los tipos de usuarios que interactuarán con el sistema están definidos con sus niveles de acceso correspondientes.

**Privacidad**
- [ ] Se ha identificado qué datos personales procesará el sistema y cuál es la justificación para cada tipo.
- [ ] Se ha definido la política de retención para cada tipo de dato que el sistema almacena.
- [ ] Se ha evaluado si los datos pueden anonimizarse o pseudonimizarse antes de incluirse en el contexto.

**Gobernanza**
- [ ] El propietario del sistema ha sido identificado y es responsable de sus decisiones de diseño.
- [ ] El proceso de aprobación para cambios en producción (system prompt, herramientas, fuentes RAG) ha sido definido.
- [ ] El catálogo de fuentes de datos autorizadas para el sistema RAG ha sido documentado con niveles de clasificación.

### Fase 2: Implementación

Durante el desarrollo, el AI Engineer verifica que los controles diseñados están efectivamente implementados:

**Control del system prompt**
- [ ] El system prompt no contiene información técnica de infraestructura (nombres de servidores, esquemas de bases de datos, credenciales).
- [ ] El system prompt incluye instrucciones de resistencia a la manipulación y separación estructural de instrucciones y datos.
- [ ] El system prompt está bajo control de versiones con historial completo de modificaciones.
- [ ] Existe un proceso documentado para aprobar cambios al system prompt en producción.

**Seguridad del sistema RAG**
- [ ] El índice vectorial aplica metadatos de clasificación a todos los documentos.
- [ ] El pipeline de recuperación aplica filtros de acceso basándose en la identidad del usuario autenticado, no en la identidad del sistema.
- [ ] Existe un proceso para añadir nuevas fuentes al corpus que incluye revisión de seguridad y clasificación de contenido.
- [ ] Los documentos recuperados pasan por inspección heurística antes de añadirse al contexto.

**Seguridad de herramientas**
- [ ] Las herramientas de impacto alto o crítico tienen un punto de confirmación antes de ejecutarse.
- [ ] Las herramientas de ejecución de código o comandos de sistema corren en entornos aislados (sandbox).
- [ ] Los permisos de las herramientas (lectura, escritura, comunicación externa) han sido revisados y son los mínimos necesarios.
- [ ] Cada ejecución de herramienta genera un registro de auditoría con: usuario, herramienta ejecutada, parámetros, resultado, timestamp.

**Validación y filtrado**
- [ ] Los mensajes de usuarios pasan por al menos un mecanismo de detección de intentos de inyección antes de ser procesados.
- [ ] Las respuestas del modelo pasan por filtros de salida que detectan revelaciones no autorizadas (fragmentos del system prompt, datos de otros usuarios, información de infraestructura).
- [ ] El sistema implementa un mecanismo de "fail closed": si un componente de seguridad falla, la operación es denegada, no procesada sin control.

**Gestión de identidades**
- [ ] La identidad del usuario autenticado se propaga a todos los componentes del sistema que la necesitan para aplicar controles de acceso.
- [ ] Los roles de usuario están documentados con sus niveles de acceso a datos y herramientas.
- [ ] Los tokens de sesión tienen expiración configurada y el sistema revoca el acceso cuando la sesión expira.
- [ ] Las identidades de servicio (service accounts) del sistema tienen permisos mínimos.

**Aislamiento de datos**
- [ ] La memoria del agente está aislada por usuario y por sesión, sin posibilidad de acceder a datos de otras sesiones.
- [ ] El historial de conversaciones no persiste datos recuperados del RAG en la memoria de largo plazo.
- [ ] En sistemas multitenancy, existe aislamiento de namespace en el índice vectorial y en el almacenamiento de memoria.

### Fase 3: Operación

Una vez el sistema está en producción, el AI Engineer verifica que los controles operativos están activos:

**Logging y auditoría**
- [ ] Todos los accesos a datos sensibles quedan registrados con: usuario, dato accedido, timestamp.
- [ ] Los cambios de configuración (system prompt, herramientas, fuentes RAG) quedan registrados con: autor, cambio realizado, timestamp, aprobador.
- [ ] Los intentos de inyección detectados quedan registrados y generan alertas al equipo de seguridad.
- [ ] Los logs de auditoría están protegidos contra modificación (firma digital o sistema de inmutabilidad).
- [ ] El período de retención de los logs está definido y es cumplido por el sistema de almacenamiento.

**Monitoreo y respuesta**
- [ ] Existe una alerta configurada para patrones inusuales de uso (volumen de consultas, tipos de herramientas ejecutadas, errores repetidos).
- [ ] Existe un proceso documentado de respuesta a incidentes de seguridad para este sistema.
- [ ] El equipo tiene capacidad para desactivar herramientas específicas sin detener el sistema completo.
- [ ] Existe un proceso para notificar a los usuarios afectados si ocurre un incidente de seguridad que involucra sus datos.

**Revisiones periódicas**
- [ ] Los permisos de herramientas se revisan cada trimestre para verificar que siguen siendo los mínimos necesarios.
- [ ] Las fuentes de datos del catálogo RAG se revisan semestralmente para verificar que siguen siendo apropiadas.
- [ ] El sistema prompt se revisa antes de cada actualización significativa para verificar que no ha acumulado información técnica innecesaria.
- [ ] El análisis de amenazas se actualiza cuando el sistema cambia significativamente en capacidades o alcance.

**Compliance**
- [ ] El sistema está documentado con el nivel de detalle requerido por las regulaciones aplicables (AI Act, GDPR, regulaciones sectoriales).
- [ ] Si el sistema procesa datos de ciudadanos europeos, ha sido evaluado bajo el AI Act y categorizado con su nivel de riesgo correspondiente.
- [ ] Existe un mecanismo para que los usuarios soliciten información sobre qué datos tiene el sistema sobre ellos y para solicitar su eliminación.
- [ ] El equipo responsable del sistema conoce los requisitos de notificación ante una brecha de seguridad en la jurisdicción aplicable.

### Cómo usar este checklist

Este checklist no es una lista de tareas que se completan una vez. Es una herramienta de revisión que se aplica:

- Al inicio del diseño, para identificar controles que deben ser parte de la arquitectura.
- Antes del despliegue a producción, para verificar que la implementación cumple con el diseño de seguridad.
- Periódicamente en operación, para verificar que los controles siguen siendo efectivos.
- Después de cambios significativos, para evaluar si los controles deben ser actualizados.

Los ítems marcados como no aplicables deben tener una justificación documentada. "No aplica porque el sistema es solo interno" es una justificación válida para algunos ítems; "no aplica porque no tuvimos tiempo de implementarlo" no lo es.

La siguiente sección resume los conceptos centrales del capítulo.
