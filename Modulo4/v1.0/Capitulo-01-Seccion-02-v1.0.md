# Módulo 4 – Capítulo 01 – Sección 02

## El Pensamiento Sistémico

¿Por qué un sistema de IA que funciona correctamente en pruebas puede degradarse en producción sin que nadie haya cambiado una sola línea de código? La respuesta casi siempre está en algún componente del sistema que nadie estaba monitoreando: los documentos del knowledge base que dejaron de actualizarse, la latencia de la base vectorial que aumentó con el volumen de datos, o la distribución de las preguntas de los usuarios que derivó hacia dominios no cubiertos por el corpus de entrenamiento. El pensamiento sistémico es la capacidad de observar no los componentes en aislamiento, sino las relaciones entre ellos.

Un arquitecto de IA no diseña un modelo: diseña el ecosistema completo dentro del cual ese modelo opera. Ese ecosistema tiene al menos siete dimensiones que interactúan permanentemente. Los **usuarios** definen los patrones de uso reales, que raramente coinciden con los patrones de prueba. Los **datos** determinan la calidad de las respuestas con más fuerza que la elección del modelo. Los **modelos** son el núcleo de razonamiento, pero tienen ventanas de contexto, costos por token y fechas de conocimiento que limitan su comportamiento. La **infraestructura** establece los topes de latencia y disponibilidad. Los **costos** conectan cada decisión técnica con la sostenibilidad financiera del sistema. El **monitoreo** determina si el equipo puede detectar problemas antes de que los usuarios los reporten. Y la **operación** define si el sistema puede ser mantenido de forma sostenible por un equipo de tamaño razonable.

Considere un caso concreto: una empresa de seguros despliega un asistente RAG para que los agentes consulten pólizas. El sistema funciona bien durante los primeros tres meses. Luego, la calidad de las respuestas comienza a degradarse sin causa aparente. Una investigación sistémica revela que el equipo de contenidos comenzó a cargar documentos en formato Word con tablas complejas, que el pipeline de ingesta no estaba procesando correctamente. Los embeddings generados a partir de ese texto malformado produjeron recuperaciones irrelevantes, que el LLM intentó convertir en respuestas con información incompleta. El problema no era el modelo, ni la base vectorial, ni el prompt: era la calidad del proceso de ingesta, un componente que el equipo original no había instrumentado con métricas de calidad porque lo consideraba trivial.

El pensamiento sistémico previene ese tipo de fallos estableciendo desde el diseño que cada componente debe ser observable, que los contratos entre componentes deben estar definidos con precisión y que ninguna parte del sistema es tan simple como para no necesitar monitoreo. En la práctica, esto se traduce en una pregunta que el arquitecto hace en cada etapa del diseño: ¿qué pasa con el resto del sistema si este componente falla, se degrada o cambia de comportamiento?

- **Usuarios:** patrones de uso real vs. patrones de prueba; distribución de intenciones; carga pico y carga sostenida.
- **Datos:** calidad de documentos fuente, frescura del knowledge base, distribución de embeddings, cobertura temática.
- **Modelos:** ventana de contexto disponible, costo por token, latencia de inferencia, política de deprecación del proveedor.
- **Infraestructura:** throughput de la base vectorial, capacidad de la capa de API, tiempos de respuesta bajo carga.
- **Costos:** costo por consulta, costo por documento ingestado, costo por actualización de embeddings.
- **Monitoreo:** cobertura de métricas, alertas configuradas, trazabilidad de errores de extremo a extremo.
- **Operación:** procedimientos de actualización documental, runbooks de incidentes, capacidad del equipo para mantener el sistema.

El pensamiento sistémico no se adquiere estudiando tecnologías individuales, sino practicando la lectura de sistemas completos: ¿qué depende de qué? ¿qué falla cuando falla X? ¿qué mejora cuando mejora Y? La sección siguiente aplica este tipo de razonamiento al análisis de trade-offs, que es la herramienta concreta con la que el arquitecto toma decisiones entre alternativas que tienen ventajas y costos simultáneos.
