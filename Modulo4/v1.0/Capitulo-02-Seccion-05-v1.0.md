# Módulo 4 – Capítulo 02 – Sección 05

## Fine-tuning vs RAG vs Prompt Engineering: La Decisión Arquitectónica Fundamental

Antes de seleccionar entre monolito, microservicios o eventos, el arquitecto de IA debe responder una pregunta de mayor jerarquía: ¿dónde vive el conocimiento que el sistema necesita para responder correctamente? Esta decisión — enriquecer el modelo, enriquecer el contexto o enriquecer las instrucciones — tiene implicaciones arquitectónicas que afectan el costo, la complejidad operativa, la frecuencia de actualización del conocimiento y la trazabilidad de las respuestas. Es posiblemente la decisión de mayor impacto en todo el diseño de un sistema de IA.

Las tres estrategias principales son prompt engineering, RAG (Retrieval-Augmented Generation) y fine-tuning. No son mutuamente excluyentes, pero cada una resuelve un tipo distinto de problema y viene con un perfil de costo y complejidad muy diferente.

**Prompt Engineering — el conocimiento está en las instrucciones**

El prompt engineering consiste en dotar al modelo de conocimiento a través de instrucciones, ejemplos y contexto incluidos directamente en el prompt del sistema. Es la estrategia más simple arquitectónicamente: no requiere infraestructura adicional, no tiene costo de entrenamiento y produce resultados inmediatos. Es la elección correcta cuando el dominio de conocimiento es estable, bien delimitado y puede describirse en unas pocas páginas. Un asistente de clasificación de tickets de soporte que debe seguir una taxonomía de veinte categorías fijas puede implementarse exclusivamente con prompt engineering. Un asistente que debe responder preguntas sobre un catálogo de diez mil productos que cambia diariamente no puede.

**RAG — el conocimiento está en el sistema**

RAG enriquece el contexto del modelo en tiempo de consulta: recupera fragmentos relevantes del knowledge base y los incluye en el prompt antes de enviar la solicitud al modelo. El modelo no necesita "saber" nada: lo busca en el momento en que lo necesita. Esta estrategia es correcta cuando el conocimiento es voluminoso (no cabe en el prompt del sistema), cambia con frecuencia (se actualiza semanalmente o diariamente), o tiene requisitos de trazabilidad (el arquitecto necesita saber exactamente qué fuente informó cada respuesta).

Los costos de RAG son principalmente operativos: infraestructura de la base vectorial, pipeline de ingesta, costo de generación de embeddings para cada documento nuevo. El costo de entrenamiento es cero, pero el costo de operación es continuo y escala con el volumen de documentos y el número de consultas.

**Fine-tuning — el conocimiento está en el modelo**

El fine-tuning adapta los pesos del modelo mediante entrenamiento adicional sobre un conjunto de datos específico del dominio. El modelo "aprende" el conocimiento y puede responder sin necesidad de recuperar contexto externo. Es la estrategia correcta cuando el sistema necesita que el modelo adopte un estilo de respuesta muy específico que el prompting no logra (por ejemplo, seguir un formato médico estricto), cuando la latencia de la recuperación de contexto es inaceptable, o cuando el conocimiento es estático y altamente especializado.

El fine-tuning tiene costos de entrenamiento significativos (compute, tiempo de ingeniería para preparar el dataset de entrenamiento), costos de evaluación (se necesita un proceso riguroso de evaluación antes de desplegar el modelo fino), y un costo de actualización alto: cada vez que el conocimiento cambia, el proceso de fine-tuning debe repetirse.

| Dimensión | Prompt Engineering | RAG | Fine-tuning |
|---|---|---|---|
| Costo de setup | Muy bajo | Medio-alto | Alto |
| Costo de actualización | Muy bajo | Bajo | Alto |
| Capacidad de conocimiento | Limitada (ventana de contexto) | Alta (base vectorial ilimitada) | Alta (pesos del modelo) |
| Trazabilidad | Limitada | Alta (chunks recuperados visibles) | Baja (conocimiento opaco) |
| Latencia de respuesta | Baja | Media (retrieval + inferencia) | Baja |
| Frescura del conocimiento | Inmediata (cambio de prompt) | Alta (ingesta continua) | Baja (requiere reentrenamiento) |

**Cuándo ninguna estrategia es suficiente por sí sola**

Existen casos en los que ninguna de las tres estrategias individualmente resuelve el problema: el sistema necesita razonar sobre conocimiento dinámico (RAG), adaptarse a un estilo de respuesta específico (fine-tuning), y ejecutar acciones en sistemas externos (agentes). En esos casos, la arquitectura correcta combina las tres estrategias en capas: el modelo fino provee la base de comportamiento, el RAG provee el conocimiento actualizado, y las herramientas del agente proveen las capacidades de acción. El Capítulo 04 examina esa arquitectura en detalle.

> **Nota del Arquitecto:** La pregunta que el arquitecto debe hacer antes de decidir entre RAG y fine-tuning no es "¿cuál produce mejores respuestas?" sino "¿con qué frecuencia cambia el conocimiento y quién es responsable de mantenerlo actualizado?" Si el conocimiento cambia mensualmente y hay un equipo dedicado a curar el dataset de entrenamiento, el fine-tuning puede ser viable. Si el conocimiento cambia diariamente y los responsables de contenido no tienen experiencia técnica, el RAG con un pipeline de ingesta automatizado es la única opción operacionalmente sostenible.

La decisión entre estas estrategias debe tomarse antes de cualquier otra decisión arquitectónica, porque determina qué tipo de infraestructura necesita el sistema, qué equipos deben estar involucrados en el mantenimiento y cuál será el presupuesto operativo a largo plazo. La sección siguiente cierra el capítulo con un marco de criterios para seleccionar entre los patrones de infraestructura estudiados.
