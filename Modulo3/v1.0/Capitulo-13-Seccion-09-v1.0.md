# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 09: Patrones y anti-patrones de observabilidad

La experiencia colectiva de equipos que han operado sistemas de IA en producción durante años ha producido un conjunto de patrones que funcionan de forma consistente y un conjunto de anti-patrones que crean ilusión de observabilidad sin la capacidad real de diagnóstico. Esta sección los cataloga de forma directa, sin rodeos, porque el reconocimiento temprano de los anti-patrones ahorra semanas de trabajo en la dirección equivocada.

### Patrones que funcionan

**Patrón: Observabilidad como ciudadano de primera clase.** Los equipos que obtienen mejores resultados operativos de sus sistemas de IA tratan la observabilidad con el mismo rigor que el código de producción. Esto significa: instrumentación diseñada en la misma sprint que el feature que instrumenta, tests de la instrumentación (que verifican que los spans se producen correctamente), y code review que incluye revisión de si el cambio tiene la observabilidad adecuada. Cuando la observabilidad es una tarea de segunda clase, se omite bajo presión y el sistema entra en producción opaco.

**Patrón: Métricas en capas.** Las métricas se organizan en niveles de granularidad: las métricas de sistema (latencia, errores, costo) se ven de forma agregada y continua; las métricas de calidad (groundedness, relevancia) se calculan sobre muestras y se ven en períodos más largos; las métricas de negocio (satisfacción, escalaciones) se revisan mensualmente. Cada capa tiene su propio dashboard y su propia cadencia de revisión. Los equipos que intentan ver todo en el mismo dashboard producen vistas que son útiles para nadie.

**Patrón: Trazabilidad por defecto para incidentes.** Cuando se abre un incidente, el primer paso del playbook es siempre recuperar las trazas de los casos afectados. Esta es una disciplina, no una opción. Los equipos que no la tienen como primer paso tienden a pasar tiempo formulando hipótesis sin datos, lo que lleva a diagnósticos incorrectos y soluciones que no resuelven el problema real. La trazabilidad de contexto solo es útil si se usa sistemáticamente.

**Patrón: Golden set como referencia permanente.** El golden set no se usa solo para las pruebas de lanzamiento; se ejecuta periódicamente y sus resultados se comparan siempre contra la línea base de lanzamiento, no solo contra el período anterior. Esto impide la normalización de la degradación. Un equipo que compara solo con el período anterior puede no notar que el sistema lleva seis meses degradándose gradualmente.

**Patrón: Separación entre alertas operativas y alertas de calidad.** Las alertas operativas (errores técnicos, latencia extrema, costo inusual) y las alertas de calidad (groundedness bajo, satisfacción del usuario cayendo) se manejan con canales y playbooks diferentes. Las alertas operativas requieren respuesta en minutos y son responsabilidad del equipo de infraestructura. Las alertas de calidad requieren investigación en horas y son responsabilidad del equipo de IA. Mezclarlas en el mismo canal produce confusión sobre quién debe responder y con qué urgencia.

**Patrón: Revisión humana estratificada.** La evaluación humana se aplica donde tiene mayor valor: a los casos extremos (scores de calidad muy bajos o muy altos para calibración del evaluador automático), a los nuevos patrones de consulta que no estaban en los datos de calibración, y a los dominios de alto riesgo donde las consecuencias de una respuesta incorrecta son graves. No se distribuye uniformemente sobre todo el tráfico, donde la mayoría de los casos son ordinarios y la evaluación humana tiene rendimientos decrecientes.

### Anti-patrones que crean ilusión de observabilidad

**Anti-patrón: Monitorear solo la API.** El equipo implementa monitoreo de la llamada a la API del proveedor del modelo —latencia, errores, costo— y lo llama "observabilidad". Pueden ver si el sistema responde, pero no si responde bien. Las cuatro dimensiones de observabilidad quedan reducidas a una. Los problemas de calidad son invisibles hasta que los usuarios se quejan.

**Anti-patrón: Confiar en los scores del LLM-as-judge sin calibración.** El equipo configura un pipeline de evaluación automática, ve que el groundedness promedio es 0.87, y asume que el sistema está produciendo respuestas de alta calidad. Nunca calibra el evaluador contra evaluaciones humanas. Seis meses después, cuando una auditoría externa revisa las respuestas del sistema, descubre que el evaluador automático estaba sobreestimando la calidad de manera sistemática por un sesgo en el prompt de evaluación.

**Anti-patrón: Dashboard sin umbral.** El equipo construye un dashboard con múltiples métricas, pero no define umbrales de alerta ni criterios de interpretación. Cada semana, el equipo mira los números y tiene una discusión subjetiva sobre si el sistema está funcionando bien. Sin umbrales, los deterioros graduales no se detectan hasta que son obvios para todos. Sin criterios de interpretación, el equipo no sabe cuándo actuar.

**Anti-patrón: Instrumentación retroactiva bajo presión.** Cuando ocurre un incidente serio, el equipo descubre que no tiene la instrumentación para diagnosticarlo. Se instrumenta el sistema de urgencia durante el incidente, bajo presión, con código que no está bien testeado y que puede introducir nuevos problemas. La instrumentación retroactiva de emergencia es siempre más cara, más lenta y de peor calidad que la instrumentación diseñada antes del lanzamiento.

**Anti-patrón: Alertas sin dueño.** El equipo configura decenas de alertas, pero no asigna un dueño a cada tipo de alerta. Cuando las alertas se disparan, hay una pausa de varios minutos (o más) mientras el equipo determina quién debe responder. En sistemas donde los usuarios están siendo afectados activamente, esa pausa tiene un costo real.

**Anti-patrón: Evaluar la calidad solo con el equipo técnico.** El AI Engineer o el equipo de ML evalúa las respuestas del sistema según criterios técnicos de calidad. Pero los criterios de calidad técnica no siempre coinciden con los criterios de calidad del negocio. Una respuesta técnicamente correcta —groundedness 0.95, coherente, bien estructurada— puede ser inapropiada para el tono de la marca o puede omitir información que el usuario de negocio considera esencial. La evaluación de calidad debe incluir al menos periódicamente a representantes del negocio y de los usuarios finales.

**Anti-patrón: Optimizar una métrica a expensas de otras.** El equipo está bajo presión para mejorar el score de relevancia del sistema. Modifica el sistema de recuperación para privilegiar la relevancia. El score de relevancia sube. La latencia también sube 40%, y la satisfacción del usuario cae porque el sistema ahora tarda demasiado. Este anti-patrón ocurre cuando el proceso de optimización no tiene un criterio de éxito multidimensional y cuando no hay un paso explícito de verificar el impacto en métricas secundarias antes de consolidar un cambio.

**Anti-patrón: Golden set estático que nunca se actualiza.** El equipo construye un golden set al momento del lanzamiento y lo usa indefinidamente. A medida que el dominio evoluciona —nuevos productos, nuevas políticas, nuevos tipos de consulta de los usuarios—, el golden set queda desactualizado. El sistema puede pasar con scores altos en un golden set que ya no representa el uso real del sistema.

### La heurística del operador honesto

Una prueba práctica para evaluar si el sistema de observabilidad es adecuado: cuando el sistema tiene un problema de calidad que impacta a los usuarios, ¿el equipo puede diagnosticar la causa raíz sin conjeturas en menos de dos horas? Si la respuesta es no —si el diagnóstico requiere más de dos horas, involucra conjeturas sin datos que las soporten, o requiere agregar instrumentación que no existía— el sistema de observabilidad tiene una brecha que debe corregirse.

Esta heurística no garantiza que el sistema de observabilidad sea perfecto. Garantiza que es funcionalmente suficiente para el propósito que justifica su existencia: mantener el sistema operable con calidad sostenida en producción.

### Nota del arquitecto

Los anti-patrones descritos no son errores de equipos incompetentes. Son las respuestas naturales de equipos competentes bajo presiones reales: presión de tiempo que lleva a dejar la instrumentación para después, presión de costo que lleva a reducir la evaluación humana, presión de resultados que lleva a optimizar una métrica sin revisar las otras. El AI Engineer que reconoce estos anti-patrones en su propio contexto no necesita juzgarlos; necesita diseñar contra ellos: estructurar el trabajo de forma que la presión de tiempo no pueda eliminar la observabilidad como primera baja.

La siguiente sección integra todos los conceptos del capítulo en un caso de estudio empresarial concreto: cómo una organización implementó observabilidad completa para un sistema de IA de soporte al cliente y qué resultados obtuvo.
