# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 08: Dashboards y operación en producción

Un sistema de IA en producción necesita un equipo que pueda responder en tiempo razonable cuando algo falla. Ese equipo no puede revisar logs crudos ni leer trazas individuales a escala. Necesita una vista condensada, actualizada y accionable del estado del sistema: un dashboard que comunique en segundos si el sistema está funcionando bien, y que señale con precisión dónde está el problema cuando no lo está.

Esta sección describe cómo diseñar los dashboards de operación para sistemas de IA, qué vistas son necesarias, cómo estructurar las alertas y cómo definir los playbooks de respuesta que el equipo ejecuta cuando una alerta se dispara.

### Los tres dashboards de un sistema de IA en producción

No existe un único dashboard que sirva para todos los propósitos. La información que necesita el ingeniero de guardia respondiendo un incidente a las 2am es diferente de la que necesita el gestor de producto revisando la evolución del sistema semana a semana. Hay tres dashboards que corresponden a tres audiencias y propósitos diferentes.

**Dashboard de guardia: visión en tiempo real.** Diseñado para detección rápida de incidentes. Muestra las métricas que pueden indicar que algo está fallando ahora mismo. La frecuencia de actualización es de segundos a minutos. El objetivo es que el ingeniero de guardia pueda determinar en menos de 60 segundos si hay un incidente activo y de qué tipo.

Elementos del dashboard de guardia:
- Tasa de solicitudes por minuto (con alerta si cae o sube abruptamente)
- Tasa de errores técnicos en tiempo real (con umbral de alerta visual)
- Latencia p95 de los últimos 5 minutos (con comparación contra la media histórica)
- Costo por minuto (para detectar anomalías de gasto)
- Estado de las dependencias críticas: APIs de proveedores de modelos, bases vectoriales, herramientas del agente
- Últimos incidentes abiertos con estado y responsable asignado

**Dashboard operacional: visión diaria y semanal.** Diseñado para el equipo de operaciones en su revisión regular. Muestra las métricas de las últimas 24 horas y la última semana, con comparaciones de tendencia. El objetivo es identificar deterioros que no generaron alertas inmediatas pero que son visibles al comparar períodos.

Elementos del dashboard operacional:
- Evolución de groundedness, relevancia y satisfacción del usuario (últimos 7 días)
- Distribución de tipos de consultas y cómo ha cambiado respecto a la semana anterior
- Top 10 de consultas con peor score de calidad (para diagnóstico de áreas débiles)
- Resultados de la ejecución periódica del golden set
- Evolución del costo por solicitud y token usage
- Casos pendientes de revisión humana

**Dashboard estratégico: visión mensual.** Diseñado para la dirección técnica y el equipo de negocio. Muestra la evolución del sistema en el período y el valor de negocio generado. El objetivo es responder: ¿el sistema está mejorando? ¿está generando el valor que se esperaba?

Elementos del dashboard estratégico:
- Tendencias de calidad del último mes versus el mes anterior y versus el lanzamiento
- Satisfacción del usuario y tasa de escalación a agentes humanos
- Costo total del sistema y costo por usuario activo (para ROI)
- Incidentes del mes: cuántos, de qué tipo, cuánto tiempo de resolución
- Experimentos completados y sus resultados (qué se mejoró, en qué porcentaje)

### Diseño de alertas efectivas

Las alertas son solo útiles si el equipo las toma en serio. Si el sistema genera demasiadas alertas con poca severidad, el equipo cae en la "fatiga de alertas": las alertas se vuelven ruido de fondo que se ignora, y cuando aparece una alerta crítica, no recibe la atención que merece.

Los principios del diseño de alertas efectivas para sistemas de IA:

**Cada alerta debe tener un dueño.** Si la alerta de groundedness bajo se dispara, debe haber una persona o un equipo específico que la recibe, con la responsabilidad explícita de investigarla. Las alertas sin dueño no se investigan.

**Las alertas deben incluir contexto de diagnóstico.** La alerta no debe ser solo "groundedness cayó por debajo de 0.75". Debe incluir: en qué tipos de consultas cayó, en qué horario, si coincide con algún cambio reciente en el sistema, y un enlace directo a los casos de peor score para inspección.

**Las alertas deben tener umbral de resolución, no solo de disparo.** Un sistema que alerta cuando una métrica cruza un umbral y no alerta cuando regresa al rango normal llena la bandeja de entrada sin cerrar el ciclo. Cada alerta debe resolverse explícitamente —investigada, intervenida, descartada— no simplemente ignorarse cuando la métrica mejora.

**El número de alertas activas simultáneas debe ser manejable.** Si el equipo tiene más de cinco alertas activas al mismo tiempo, el sistema de alertas está mal calibrado. Las alertas de Nivel 1 deben ser excepcionales, no el estado normal del sistema.

### Playbooks de respuesta operacional

Un playbook es un protocolo documentado que el equipo sigue cuando ocurre un evento específico. Los playbooks son la diferencia entre una respuesta coordinada y eficiente y una respuesta improvisada que tarda el doble y llega a conclusiones incorrectas.

Los sistemas de IA en producción deben tener playbooks para al menos los siguientes eventos:

**Playbook: caída de calidad (groundedness o relevancia bajo umbral)**
1. Verificar si coincide con un cambio reciente en el sistema (despliegue de nueva versión, actualización de base vectorial, cambio de proveedor)
2. Ejecutar el golden set para confirmar si es un problema sistémico o localizado
3. Identificar los tipos de consultas más afectados usando el dashboard operacional
4. Recuperar las trazas de los casos con peor score para diagnóstico de contexto
5. Formular hipótesis (¿documentos desactualizados? ¿system prompt inadecuado para esta categoría de consulta? ¿model drift?)
6. Si se confirma la hipótesis, implementar intervención y monitorear
7. Si no se puede diagnosticar en 4 horas, escalar a Nivel 2 con rollback como opción

**Playbook: pico de latencia**
1. Verificar el estado de las dependencias del sistema (API del proveedor del modelo, base vectorial)
2. Analizar si el aumento coincide con un aumento en el volumen de tráfico
3. Revisar si hubo cambios en la configuración del sistema que aumenten el tamaño del contexto
4. Verificar si el pico es en el paso de recuperación RAG, en la llamada al modelo, o en el post-procesamiento
5. Si el cuello de botella es la API del proveedor, implementar cache o reducir llamadas concurrentes
6. Si el cuello de botella es el tamaño del contexto, revisar la estrategia de compresión

**Playbook: alerta de bucle en agente**
1. Identificar el identificador de las solicitudes en bucle usando el monitor de pasos por flujo
2. Inspeccionar las trazas de esas solicitudes para entender en qué paso se produce el bucle
3. Determinar si el bucle es por una herramienta que falla y devuelve un resultado que el agente no sabe interpretar, o por un criterio de terminación mal definido
4. Si el bucle produce costo descontrolado, implementar un límite de emergencia en el número máximo de pasos
5. Diseñar la corrección en el sistema de planificación del agente y probarla en staging
6. Desplegar la corrección y monitorear los primeros 100 flujos posteriores

### La documentación de incidentes como base de conocimiento

Cada incidente resuelto debe documentarse en un post-mortem estructurado. El post-mortem no es un documento de culpabilidad; es un registro de conocimiento sobre el comportamiento del sistema que sirve para:

- Identificar si el mismo tipo de incidente se ha repetido (lo que indica que la causa raíz no fue corregida de forma permanente)
- Capacitar a nuevos miembros del equipo con casos reales de diagnóstico
- Alimentar el diseño de nuevas alertas y actualizaciones de playbooks
- Comunicar al equipo de negocio qué ocurrió, cuál fue el impacto y qué se hizo para evitar recurrencia

Un post-mortem efectivo responde: qué ocurrió, cuándo se detectó, cuál fue el impacto, cuál fue la causa raíz, qué se hizo para resolverlo, y qué cambios en el sistema o en los procesos evitan la recurrencia.

### Nota del arquitecto

El diseño de dashboards y playbooks es frecuentemente la última tarea de un proyecto de despliegue de IA —la que se hace "cuando haya tiempo" después del lanzamiento. Este orden de prioridades produce equipos que reaccionan a los incidentes de forma ad-hoc durante las primeras semanas críticas de producción, cuando el riesgo de incidentes es mayor y el equipo tiene menos experiencia con el comportamiento real del sistema.

El momento correcto para diseñar los dashboards y los playbooks es antes del lanzamiento, durante las pruebas en staging, cuando hay tiempo para pensar sin la presión de un incidente activo. Los dashboards y los playbooks son parte del sistema tanto como el código que procesa las solicitudes. No son documentación adicional; son infraestructura operativa.

La siguiente sección examina los patrones de observabilidad que han probado su valor en producción y los anti-patrones que crean ilusión de observabilidad sin la capacidad real de diagnóstico.
