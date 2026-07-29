# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 07: Detección de degradación y deriva

Un sistema de IA puede degradarse sin que nadie lo note. La degradación no siempre es abrupta —una falla técnica que genera alertas inmediatas— sino frecuentemente gradual: la calidad de las respuestas se deteriora lentamente durante semanas, la tasa de satisfacción del usuario baja dos puntos por mes, el sistema tarda un poco más de lo que tardaba hace tres meses. Si no se tienen las métricas correctas y los mecanismos de detección apropiados, la degradación solo se descubre cuando el problema es suficientemente grave como para que llegue por otras vías: quejas de usuarios, reportes del equipo de negocio, caída en métricas de negocio.

Esta sección describe los tres tipos de degradación que afectan a los sistemas de IA en producción, los mecanismos para detectarlos y el framework de alertas que determina qué acción corresponde a cada nivel de severidad.

### Los tres tipos de degradación

**Deriva del modelo (model drift).** El comportamiento del modelo cambia sin que el sistema haya sido modificado. Esto ocurre cuando el proveedor del modelo actualiza silenciosamente su versión de producción —una práctica común en APIs de LLMs comerciales—, cuando las restricciones de alineación del modelo se ajustan, o cuando la distribución de entrenamiento del modelo se actualiza de formas que no están documentadas en el changelog del proveedor.

La deriva del modelo puede manifestarse como un cambio en el tono de las respuestas (de directo a más cauteloso, o viceversa), un cambio en la longitud promedio de las respuestas, un cambio en la frecuencia con que el modelo se niega a responder ciertas categorías de consultas, o un cambio en la capacidad de seguir instrucciones complejas del system prompt.

La detección de model drift requiere ejecutar el golden set periódicamente y comparar los resultados con la línea base. Si el mismo conjunto de casos que antes producía scores de 0.90 ahora produce scores de 0.82, hay evidencia de deriva del modelo que debe investigarse —incluyendo verificar con el proveedor si hubo una actualización del modelo.

**Deriva del contexto (context drift).** El conocimiento que alimenta el sistema se vuelve desactualizado. Las políticas cambian pero los documentos en la base vectorial no se actualizan. Los productos se discontinúan pero sus fichas técnicas siguen siendo recuperadas. Las regulaciones evolucionan pero la documentación legal indexada refleja la versión anterior.

La deriva del contexto es el tipo de degradación más frecuente y más silencioso. Es silencioso porque el sistema técnicamente sigue funcionando: recupera documentos, construye contextos, genera respuestas coherentes. El problema es que esas respuestas describen un mundo que ya no existe.

La detección de context drift requiere monitorear la antigüedad del conocimiento que el sistema está usando. Si el 30% de los documentos recuperados tienen más de seis meses de antigüedad en un dominio donde el conocimiento cambia mensualmente, hay un problema de vigencia que debe atenderse. También se puede detectar mediante evaluación humana periódica de muestras de respuestas, comparándolas con las fuentes autorizadas actuales.

**Deriva de los datos (data drift).** Los usuarios cambian la forma en que interactúan con el sistema. Las consultas que recibe el sistema en el mes 12 de operación son cualitativamente diferentes de las del mes 1: los usuarios más casuales se fueron, quedaron los más sofisticados; el dominio de uso se expandió a áreas que el sistema no fue diseñado para cubrir; eventos externos —una campaña de marketing, un incidente de producto, un cambio regulatorio— generan un pico de consultas sobre temas específicos que el sistema no tiene bien cubiertos.

La data drift se detecta analizando la distribución de consultas en el tiempo. Si la distribución semántica de las consultas de este mes es significativamente diferente de la del mes anterior —medida por técnicas como embedding drift detection—, hay un cambio en el uso del sistema que puede requerir adaptaciones en la arquitectura del contexto.

### Framework de alertas por nivel de severidad

No todas las señales de degradación requieren la misma respuesta. Un sistema de alertas bien diseñado tiene tres niveles de severidad con acciones distintas.

**Nivel 1 — Logging y análisis posterior.** Señales de degradación leve que deben registrarse para análisis, pero que no requieren acción inmediata porque pueden ser fluctuaciones normales o problemas menores que el equipo puede abordar en el ciclo regular de optimización.

Ejemplos de señales de Nivel 1:
- Groundedness cae 0.03 puntos en la semana, dentro del rango histórico de variabilidad
- Un tipo específico de consulta tiene latencia p95 10% más alta que la semana anterior
- La distribución de consultas muestra una nueva categoría emergente que representa el 5% del tráfico

Acción: registrar automáticamente en el log de observabilidad, revisar en la reunión semanal de operaciones, agregar al backlog de optimización si se confirma como tendencia.

**Nivel 2 — Revisión activa.** Señales de degradación moderada que requieren investigación activa en las próximas 24-48 horas. El sistema sigue operativo pero hay evidencia de un problema que puede agravarse si no se atiende.

Ejemplos de señales de Nivel 2:
- Groundedness cae más de 0.10 puntos en la semana, consistentemente en múltiples días
- La tasa de satisfacción del usuario cae más de 10 puntos en dos semanas consecutivas
- El costo por solicitud aumenta más de 30% sin aumento proporcional en el tráfico
- El golden set muestra una caída de calidad de más de 0.08 puntos comparado con la semana anterior
- El número promedio de pasos por flujo agentivo aumenta más de 40% en 48 horas

Acción: notificación al equipo de ingeniería de IA, asignación de un responsable de investigación, diagnóstico utilizando las trazas de las solicitudes con peores métricas, plan de intervención con plazo definido.

**Nivel 3 — Acción inmediata o rollback.** Señales de degradación severa que requieren acción inmediata porque el sistema está causando un impacto negativo significativo en los usuarios o en la organización.

Ejemplos de señales de Nivel 3:
- La tasa de errores técnicos supera el 5% del tráfico
- El groundedness cae por debajo de 0.60 en promedio (el sistema está alucinando consistentemente)
- Se detectan respuestas que contradicen activamente políticas corporativas críticas
- El costo por solicitud se quintuplica de forma inexplicable
- El sistema está en bucle: más del 15% de los flujos agentivos alcanzan el límite de pasos
- El golden set muestra una caída de calidad de más de 0.20 puntos respecto a la línea base

Acción: escalación inmediata, evaluación de rollback a la versión anterior, posible desactivación temporal del sistema si el daño potencial es alto, notificación al equipo de negocio.

```
FRAMEWORK DE ALERTAS — NIVELES DE RESPUESTA

┌──────────────────────────────────────────────────────────────┐
│  NIVEL 1 — LOGGING                                           │
│  Señal: degradación dentro de la variabilidad histórica      │
│  Acción: registrar → revisar en ciclo semanal → backlog      │
│  Tiempo de respuesta: próximo ciclo regular (≤ 7 días)       │
└──────────────────────────────────────────────────────────────┘
         ↓ si persiste o se agrava
┌──────────────────────────────────────────────────────────────┐
│  NIVEL 2 — REVISIÓN ACTIVA                                   │
│  Señal: degradación significativa y sostenida                │
│  Acción: asignar responsable → diagnosticar → intervenir     │
│  Tiempo de respuesta: 24-48 horas                            │
└──────────────────────────────────────────────────────────────┘
         ↓ si es crítica o impacto alto
┌──────────────────────────────────────────────────────────────┐
│  NIVEL 3 — ACCIÓN INMEDIATA                                  │
│  Señal: degradación severa con impacto en usuarios/negocio   │
│  Acción: escalar → evaluar rollback → notificar negocio      │
│  Tiempo de respuesta: horas                                  │
└──────────────────────────────────────────────────────────────┘
```

### Detección de alucinaciones en producción

La detección automática de alucinaciones es uno de los problemas más difíciles de la operación de sistemas de IA, y merece un tratamiento específico. Una alucinación es una afirmación que el modelo produce con confianza pero que no está soportada por el conocimiento disponible en su contexto. En sistemas de IA de producción, las alucinaciones pueden tener consecuencias prácticas graves: un asistente de soporte que cita una política de garantía que no existe, un agente que reporta datos financieros incorrectos, un sistema legal que menciona jurisprudencia que no corresponde.

Las técnicas de detección automática de alucinaciones en producción se dividen en dos categorías.

**Detección por contraste con el contexto.** El sistema verifica que las afirmaciones de la respuesta pueden rastrearse hasta fragmentos del contexto que el modelo recibió. Esta es la base de la métrica de groundedness. Si la respuesta contiene una afirmación que no puede vincularse con ningún fragmento del contexto recuperado, la respuesta tiene una posible alucinación. La limitación de esta técnica es que no detecta alucinaciones que son consistentes con el contexto pero incorrectas en el mundo real —si el contexto contiene un documento desactualizado, la respuesta puede ser "groundada" e incorrecta al mismo tiempo—.

**Detección por verificación cruzada.** Para afirmaciones de alto riesgo —precios, fechas, nombres, cifras—, el sistema puede verificar automáticamente que las afirmaciones de la respuesta coinciden con la fuente autoritativa de esos datos. Por ejemplo, un sistema que genera respuestas sobre precios puede verificar que los precios mencionados en la respuesta coincidan con los que están en la base de datos de productos en ese momento.

Ninguna técnica detecta todas las alucinaciones. El enfoque práctico en producción es: (1) maximizar la groundedness del sistema mediante una buena arquitectura de contexto, (2) implementar detección automática para las categorías de afirmaciones de mayor riesgo, y (3) incluir en el proceso de evaluación humana una revisión periódica específica de respuestas en dominios de alto riesgo.

### Monitoreo de tendencias a largo plazo

Además de las alertas de corto plazo, el equipo de operaciones debe mantener una vista de tendencias a largo plazo: cómo han evolucionado las métricas del sistema durante los últimos tres meses, seis meses, un año. Esta vista permite detectar degradaciones muy graduales que no disparan ninguna alerta individual pero que, vistas en perspectiva, representan un deterioro significativo.

Una forma práctica de implementarlo es un informe mensual que compara las métricas del mes actual contra el mismo mes del año anterior y contra el mes en que el sistema se lanzó a producción. Si el sistema era más rápido, más barato y producía mejores scores de calidad en su primer mes de producción que en el mes 12, hay un problema de degradación acumulada que los sistemas de alerta corta no capturaron.

### Nota del arquitecto

El mayor riesgo de la degradación silenciosa es que el equipo se adapta a ella. Si el sistema va degradándose un punto de calidad por semana, los usuarios y el equipo de operaciones normalizan cada nuevo nivel como "el estado actual del sistema". Al cabo de tres meses, el sistema tiene una calidad significativamente peor que al inicio, pero nadie lo percibe porque la degradación fue gradual.

El antídoto es mantener siempre una referencia absoluta: la calidad del sistema en su mejor momento documentado. La comparación relevante no es "¿está peor que la semana pasada?" sino "¿está peor que cuando el sistema funcionaba mejor?". El golden set, ejecutado periódicamente con comparación contra la línea base de lanzamiento, provee esa referencia absoluta.

La siguiente sección examina cómo organizar toda esta información de observabilidad en dashboards de operación que permitan al equipo mantener el sistema bajo control en producción continua.
