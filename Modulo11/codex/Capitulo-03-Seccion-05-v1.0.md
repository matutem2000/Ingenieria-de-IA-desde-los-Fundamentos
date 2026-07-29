# Módulo 11 – Capítulo 03 – Sección 05

# Gestión del cambio técnico: actualizar el legado gradualmente sin interrumpir el negocio

La modernización de sistemas legacy para habilitarlos como fuentes de datos para IA no puede hacerse mediante big bang rewrites que interrumpan el negocio: la estrategia técnica correcta combina el patrón Strangler Fig (introducir el nuevo sistema en paralelo y migrar gradualmente el tráfico del legacy al nuevo sistema) con cambios incrementales instrumentados mediante feature flags que permiten activar y desactivar capacidades nuevas sin despliegues adicionales. El patrón Strangler Fig aplicado a la integración con legacy funciona así: en lugar de reemplazar el sistema de gestión documental legacy por completo, se introduce una capa de abstracción (el facade) que inicialmente redirige el 100% del tráfico al sistema legacy, y paulatinamente se migran módulos funcionales al nuevo sistema mientras el facade gestiona el routing, permitiendo en cualquier momento hacer rollback completo al legacy si aparecen problemas. La gestión del cambio técnico en enterprise requiere además coordinar con el equipo de Change Management para obtener aprobación del Change Advisory Board (CAB) para cada modificación a sistemas productivos: este proceso, aunque burocráticamente costoso, protege al negocio de cambios no coordinados que pueden tener efectos en cascada sobre sistemas interdependientes. Las pruebas de regresión automatizadas son imprescindibles en este contexto: un test suite que valide el comportamiento del sistema legacy antes y después de cada cambio de integración es la única forma de detectar regresiones antes de que lleguen a producción.

## Puntos críticos de la gestión del cambio

- Strangler Fig pattern: facade que inicialmente proxea el 100% al legacy, con routing gradual al nuevo sistema basado en porcentajes controlados mediante feature flags (LaunchDarkly, Unleash)
- Feature flags para rollout incremental: activar nuevas integraciones para el 5% del tráfico inicialmente, monitorear métricas de calidad de respuesta y latencia, y aumentar gradualmente hasta el 100% solo si los SLOs se mantienen
- Pruebas de contrato (contract testing): Pact o Spring Cloud Contract para validar que el productor (sistema legacy) y el consumidor (sistema de IA) mantienen la compatibilidad de interfaces antes de cada despliegue
- Shadow mode deployment: ejecutar el nuevo sistema de integración en paralelo al legacy, comparando respuestas para detectar discrepancias sin impacto en el usuario final, antes de activar el corte de tráfico
- Documentación de change requests: RFC técnicos con análisis de impacto, plan de rollback probado (no solo documentado), criterios de éxito cuantificables, y notificación a todos los equipos con sistemas dependientes

## Buena práctica

Nunca realizar el corte de un sistema legacy a producción sin haber ejecutado previamente un rollback simulado en staging: si el plan de rollback no se puede ejecutar en menos de 15 minutos, el change no está listo para producción.
