# Capítulo 12 — Context Engineering Empresarial

## Sección 10: Caso de estudio empresarial

**TechServe Solutions** es una empresa de servicios de tecnología gestionada con 380 empleados, tres oficinas y aproximadamente 1.200 clientes corporativos medianos. Su estructura tiene cuatro áreas principales: soporte técnico (90 personas), ventas y renovaciones (45 personas), operaciones internas (60 personas) e ingeniería de productos (185 personas). El resto son funciones administrativas, finanzas y dirección.

En el año anterior al caso, TechServe enfrentó un problema conocido: el equipo de soporte técnico estaba saturado. El tiempo de resolución de tickets había subido de un promedio de 4 horas a 7 horas en 18 meses, la tasa de satisfacción del cliente había caído del 82% al 71%, y el equipo estaba procesando 800 tickets diarios con una tasa de escalación del 38% a ingenieros especializados.

La dirección de tecnología propuso implementar un sistema de asistencia de IA para el equipo de soporte, con el objetivo de reducir el tiempo de resolución y la tasa de escalación. Lo que empezó como un proyecto de un asistente de soporte evolucionó, durante dieciocho meses, en una plataforma de IA empresarial utilizada por los cuatro equipos.

### Fase 1: El asistente de soporte (meses 1 a 5)

El equipo de IA construyó el primer asistente siguiendo los principios del capítulo de RAG: indexó la base de conocimiento técnico existente —5.000 artículos de la wiki interna, 1.200 documentos de resolución de incidentes históricos, los manuales de los productos que TechServe gestionaba para sus clientes— en una base vectorial, definió las instrucciones del sistema y desplegó un asistente que el equipo de soporte podía consultar antes de responder al cliente.

**Los primeros resultados** fueron promisorios pero no espectaculares. El tiempo de resolución bajó de 7 horas a 5,2 horas en promedio. La tasa de escalación bajó del 38% al 29%. La satisfacción del cliente subió del 71% al 74%. El equipo de soporte encontraba el asistente útil para consultas sobre configuraciones conocidas, pero le reportaba dos problemas recurrentes: el asistente daba respuestas desactualizadas sobre los productos que habían cambiado su interfaz en las últimas versiones, y no tenía acceso a los datos del cliente específico que estaba reportando el problema.

**El diagnóstico de context engineering** identificó dos brechas. Primera: la base de conocimiento técnico no tenía proceso de actualización; se había indexado en el mes 1 y no había sido actualizada desde entonces, aunque los productos habían lanzado nuevas versiones. Segunda: el contexto del asistente era genérico —no sabía qué productos específicos tenía configurado el cliente, cuál era su historial de incidentes anteriores, ni si el cliente tenía contratos de soporte de nivel premium que implicaban tiempos de respuesta garantizados diferentes.

**Las decisiones de diseño** para resolver estas brechas fueron:

Para la vigencia del conocimiento: implementar un proceso de actualización semanal de la base vectorial, sincronizado con el ciclo de publicación de notas de versión de los productos. El propietario del conocimiento técnico —el equipo de ingeniería de productos— se designó como responsable de revisar y actualizar la documentación técnica relevante con cada nuevo release.

Para el contexto del cliente: integrar el sistema con el CRM de TechServe como herramienta dinámica. Cuando el asistente procesa una consulta de soporte, primero recupera del CRM el perfil del cliente: productos contratados, versiones en uso, historial de los últimos diez incidentes, nivel de contrato de soporte. Esa información se incluye en el contexto de la llamada al modelo, permitiendo respuestas personalizadas al contexto específico del cliente.

Cinco meses después de estas mejoras, el tiempo de resolución bajó a 3,8 horas, la tasa de escalación al 22% y la satisfacción del cliente al 81%.

### Fase 2: La expansión a ventas y el primer silo (meses 6 a 9)

El éxito del asistente de soporte generó interés en el equipo de ventas, que quería su propio asistente para ayudar a los ejecutivos de cuenta durante las llamadas con clientes: acceso rápido a propuestas de valor, comparativas de competidores, historial de la relación comercial con cada cliente y el catálogo de servicios actualizado.

El equipo de ventas, entusiasmado y con cierta urgencia comercial, construyó su asistente de forma independiente. Indexó sus propios documentos, definió sus propias instrucciones del sistema y desplegó su solución en tres meses.

**El problema** apareció en el mes nueve, cuando un cliente llamó al equipo de soporte para reclamar que el ejecutivo de ventas le había comunicado unas condiciones de servicio que el asistente de soporte describía de forma diferente. Investigando, el equipo descubrió que las instrucciones del sistema del asistente de ventas describían las condiciones de soporte incluidas en el contrato básico usando terminología de un año anterior, cuando esas condiciones habían sido actualizadas. El asistente de soporte usaba la versión vigente. Dos asistentes de IA de la misma empresa comunicaban la misma política de formas contradictorias.

Este incidente —un cliente molesto y una reunión de dirección para explicar qué había pasado— fue el catalizador que llevó a TechServe a pasar de tener asistentes independientes a diseñar una plataforma de IA empresarial.

### Fase 3: La plataforma de IA empresarial (meses 10 a 18)

La dirección de tecnología encargó al equipo de IA diseñar una plataforma común. Las decisiones arquitectónicas tomadas en este punto fueron las que determinaron el éxito posterior.

**Decisión 1: Arquitectura de capas.** Se definió un núcleo corporativo de instrucciones y conocimiento que todos los asistentes heredarían sin modificación: las políticas vigentes, las condiciones de servicio actuales, el tono de comunicación oficial y las restricciones legales aplicables. El equipo legal y la dirección de comunicaciones se designaron como co-propietarios de este núcleo. Cualquier cambio al núcleo requería su aprobación.

**Decisión 2: Proceso de gobierno.** Se creó un Comité de Gobierno de IA con representantes de las cuatro áreas y coordinado por el equipo de IA. El comité se reunía mensualmente para revisar la calidad del conocimiento corporativo, aprobar cambios al núcleo y resolver conflictos entre las necesidades de las áreas y las restricciones del núcleo. El proceso de incorporación de documentos al núcleo requería una revisión de 48 horas del comité; el proceso para las capas departamentales era más ágil, requiriendo solo la aprobación del responsable del área.

**Decisión 3: Integración con sistemas corporativos.** Se construyó una capa de servicio intermediaria que encapsulaba las integraciones con el CRM, el sistema de tickets y el ERP. Los asistentes de IA no llamaban directamente a los sistemas corporativos; llamaban a la capa de servicio, que gestionaba la autenticación, los rate limits y la transformación de datos. Esta capa permitía que un cambio en la API del CRM se absorbiera en la capa de servicio sin afectar a ninguno de los asistentes.

**Decisión 4: Métricas de negocio formales.** Se estableció un dashboard de métricas operado por el equipo de IA que mostraba, por área: tiempo de resolución promedio, tasa de escalación o conversión (según el caso de uso), satisfacción del usuario y costo por consulta. El dashboard se revisaba mensualmente en el Comité de Gobierno y se incluía en las revisiones de presupuesto de tecnología.

### Los resultados al mes 18

Dieciocho meses después del inicio del proyecto, TechServe tenía cuatro asistentes de IA en producción —soporte, ventas, recursos humanos e ingeniería interna— sobre la plataforma corporativa común.

Los resultados de negocio para el área de soporte, que tenía el baseline más sólido:

- Tiempo de resolución: de 7 horas (baseline) a 3,1 horas (mes 18). Reducción del 56%.
- Tasa de escalación: del 38% al 19%. Reducción de 19 puntos porcentuales.
- Satisfacción del cliente: del 71% al 84%. Mejora de 13 puntos.
- Costo por ticket: reducción estimada del 34% respecto del baseline, considerando el costo de inferencia y la reducción de tiempo de operador.

El ROI del proyecto, calculado con las métricas del equipo de soporte solamente y excluyendo el valor generado por los otros tres asistentes:

```
Inversión total (desarrollo + operación año 1): USD 180.000
Ahorro anual estimado (tiempo de operador + reducción de escalaciones): USD 320.000
ROI año 1: (320.000 - 180.000) / 180.000 = 78%
```

### Las lecciones del caso

TechServe aprendió tres lecciones que no están en ningún manual técnico de IA.

La primera: el incidente del silo de contexto no fue una falla técnica. Fue una consecuencia predecible de construir sistemas de IA en silos sin arquitectura compartida. La arquitectura de capas no es una opción de diseño avanzada; es el requisito mínimo para una organización con más de un sistema de IA.

La segunda: el Comité de Gobierno de IA fue la decisión más importante del proyecto. No el modelo elegido, no la base vectorial seleccionada, no la arquitectura de recuperación. El comité fue el mecanismo que resolvió los conflictos, mantuvo el conocimiento actualizado y aseguró que los sistemas de IA siguieran alineados con la realidad cambiante de la organización.

La tercera: las métricas de negocio formales —con baseline establecido antes del despliegue— fueron lo que convirtió el proyecto de IA de un gasto de tecnología en una inversión con retorno demostrable. Sin esas métricas, el proyecto habría sido difícil de defender en las revisiones de presupuesto del año siguiente.

### Nota del arquitecto

El caso de TechServe es deliberadamente representativo de una organización de mediana escala —no una corporación global con recursos ilimitados ni una startup con libertad de experimentar sin restricciones—. La mayoría de los proyectos de IA empresarial real ocurren en este espacio: organizaciones con presupuestos reales, sistemas heredados reales y procesos organizacionales que preexisten la iniciativa de IA. Las decisiones que funcionaron en TechServe no son las únicas decisiones posibles; son las decisiones correctas para esas condiciones específicas. El AI Engineer que entiende el razonamiento detrás de esas decisiones puede adaptarlo a las condiciones de su organización particular.

La siguiente sección convierte este conocimiento en práctica: un laboratorio donde el estudiante diseña la arquitectura de una plataforma de IA empresarial para un escenario concreto.
