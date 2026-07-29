# Capítulo 12 — Context Engineering Empresarial

## Sección 12: Checklist del AI Engineer

Esta lista de verificación es una herramienta de diagnóstico para proyectos de Context Engineering empresarial. No es un proceso secuencial; es un conjunto de preguntas que el AI Engineer debe poder responder afirmativamente antes de declarar que un sistema está listo para producción corporativa.

Las preguntas están organizadas en cinco áreas que corresponden a las dimensiones críticas del Context Engineering empresarial.

---

### Área 1: Arquitectura del contexto

- El sistema tiene definida una arquitectura de capas de contexto (corporativa, departamental, de aplicación).
- Cada capa tiene un responsable claramente identificado con autoridad para aprobar cambios.
- Las instrucciones del sistema están bajo control de versiones con historial de cambios.
- El sistema puede recuperar contexto de múltiples fuentes (base vectorial, sistemas dinámicos) sin mezclar conocimiento estático con datos en tiempo real en la misma capa.
- El sistema tiene definido un límite máximo de tokens de contexto por llamada y un mecanismo de truncación controlada cuando ese límite se aproxima.
- El contexto del sistema está optimizado: no hay instrucciones redundantes, ejemplos no utilizados o conocimiento indexado que ningún tipo de consulta recupera.
- El sistema está diseñado para el contexto mínimo suficiente, no para el contexto máximo posible.

---

### Área 2: Gobierno del conocimiento

- Cada fuente de conocimiento indexada en el sistema tiene un propietario designado con responsabilidad explícita sobre su vigencia y calidad.
- Existe un proceso documentado para incorporar nuevos documentos a la base de conocimiento, con criterios de calidad y tiempos de aprobación definidos.
- Existe un proceso documentado para retirar documentos obsoletos o incorrectos de la base de conocimiento.
- La frecuencia de revisión del conocimiento indexado está definida por tipo de fuente y es proporcional a la volatilidad de ese conocimiento.
- Existe un proceso de aprobación para cambios en las instrucciones del sistema de producción, con separación entre quien propone el cambio y quien lo aprueba.
- Los cambios en las instrucciones del sistema se prueban en staging antes de desplegarse a producción.
- Existe un mecanismo para propagar cambios en el conocimiento corporativo a todos los sistemas de IA que lo usan, sin requerir actualización manual en cada sistema.

---

### Área 3: Controles de acceso y seguridad

- El sistema de IA hereda los controles de acceso de la organización; no tiene un sistema de permisos propio que los reemplace o contradiga.
- Las credenciales de acceso a sistemas corporativos no están en el contexto del modelo ni son accesibles al modelo.
- El sistema registra cada consulta a sistemas corporativos en un log de auditoría que permite revisar qué información se usó para generar cada respuesta.
- El sistema aplica el principio de mínimo privilegio: las credenciales usadas para acceder a sistemas corporativos solo tienen los permisos mínimos necesarios.
- Si el sistema tiene múltiples equipos de usuarios, el contexto que recibe cada usuario está limitado al conocimiento al que ese usuario tiene autorización de acceso.

---

### Área 4: Integración y operación

- El sistema tiene degradación controlada definida para cada integración crítica: si el componente falla, el sistema se comporta de forma predecible y comunica el problema al usuario.
- Las integraciones con sistemas corporativos están abstraídas en una capa de servicio que protege al sistema de IA de cambios en las APIs de los sistemas subyacentes.
- El sistema tiene monitoreo implementado desde el primer día de producción, no como adición posterior.
- Existe un proceso de escalación para cuando el sistema produce respuestas incorrectas: quién lo reporta, quién investiga, quién aprueba la corrección.
- El sistema ha sido probado con la carga esperada en producción antes del despliegue, no solo con casos unitarios.

---

### Área 5: Métricas y valor de negocio

- Existe un baseline de métricas de negocio establecido antes del despliegue del sistema, que permite comparar el estado anterior y posterior.
- Las cinco métricas fundamentales están definidas y tienen fórmulas de cálculo acordadas: tiempo de resolución, tasa de escalación, satisfacción del usuario, cobertura del conocimiento y costo por consulta.
- Existe un dashboard que muestra las métricas de negocio (para la dirección) y las métricas de calidad del contexto (para el equipo técnico).
- La frecuencia de revisión de métricas está definida y acordada con las partes interesadas: semanal para el equipo técnico, mensual para la dirección.
- Existe un proceso para relacionar cambios en las métricas de negocio con cambios específicos en el diseño del contexto, permitiendo identificar qué intervenciones producen mejoras.

---

### Indicadores de alerta temprana

Los siguientes síntomas indican que el sistema necesita intervención antes de que el problema sea visible para los usuarios.

| Indicador | Umbral de alerta | Acción recomendada |
|---|---|---|
| Satisfacción del usuario | Cae más de 5 puntos en 2 semanas | Revisar muestras de respuestas, identificar tipos de consulta problemáticos |
| Tasa de escalación | Sube más de 8 puntos en 2 semanas | Diagnosticar si la base de conocimiento tiene lagunas en los temas que escalan |
| Precisión de recuperación | Cae por debajo del 70% en consultas de referencia | Auditar la calidad del conocimiento indexado, posible presencia de ruido |
| Vigencia del conocimiento | Más del 20% del conocimiento no fue revisado en el período programado | Activar proceso de revisión urgente con propietarios del conocimiento |
| Costo por consulta | Sube más de 30% sin aumento proporcional en calidad | Auditar el tamaño del contexto por tipo de consulta, identificar inflación |

---

### Uso de esta checklist

Esta checklist tiene dos usos complementarios.

El primer uso es pre-despliegue: antes de llevar un sistema de IA a producción corporativa, el AI Engineer verifica cada ítem. Los ítems no cumplidos representan riesgos que deben resolverse antes del despliegue o mitigarse con un plan explícito.

El segundo uso es revisión periódica: una vez el sistema está en producción, revisar la checklist cada trimestre identifica áreas donde el sistema se ha deteriorado desde el despliegue inicial —procesos de gobierno que no se están siguiendo, integraciones que se han vuelto frágiles, métricas que ya nadie revisa.

Un sistema que satisface esta checklist en el despliegue inicial y la revisa con rigor trimestralmente tiene una probabilidad significativamente mayor de mantenerse operativo y valioso para la organización a lo largo del tiempo.
