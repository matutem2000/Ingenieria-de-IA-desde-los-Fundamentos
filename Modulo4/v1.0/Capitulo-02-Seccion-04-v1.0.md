# Módulo 4 – Capítulo 02 – Sección 04

## Arquitecturas Basadas en Eventos

No todas las operaciones de un sistema de IA tienen el mismo perfil de temporalidad. Cuando un usuario hace una pregunta, espera una respuesta en segundos: esa interacción es síncrona por naturaleza. Pero cuando un nuevo documento se incorpora al knowledge base de un sistema RAG, el proceso de extracción, limpieza, chunking, generación de embeddings y almacenamiento puede tomar minutos y no necesita completarse antes de que el usuario reciba ninguna confirmación inmediata. Esta diferencia de temporalidad es exactamente el problema que resuelven las arquitecturas basadas en eventos.

En una arquitectura basada en eventos, los componentes del sistema no se llaman directamente entre sí. En cambio, publican eventos en una cola o bus de mensajes, y otros componentes se suscriben a esos eventos para procesarlos de forma asíncrona. Cuando un editor de contenidos sube un nuevo documento al repositorio corporativo, ese acto publica un evento `documento.creado` en una cola (por ejemplo, AWS SQS, Azure Service Bus, o Apache Kafka). El servicio de ingesta de RAG está suscrito a ese evento y procesa el documento en segundo plano, sin bloquear ninguna operación del usuario. Cuando el documento ha sido procesado y sus embeddings están disponibles en la base vectorial, el servicio publica un evento `documento.indexado`, que puede disparar una notificación al editor o un proceso de validación de calidad.

**Beneficios específicos para sistemas de IA:**

- **Desacoplamiento temporal:** el productor del evento no necesita esperar al consumidor. El editor que carga un documento no espera a que el pipeline de ingesta termine. El servicio de negocio que actualiza la información de un producto no espera a que el vector store se actualice.
- **Resiliencia por reintentos:** si el servicio de embeddings está temporalmente indisponible, el mensaje permanece en la cola y el servicio lo procesará cuando recupere disponibilidad. No se pierden documentos por fallos transitorios.
- **Escalado elástico del pipeline de ingesta:** cuando se cargan cien documentos simultáneamente (por ejemplo, durante una migración de contenidos), el pipeline de ingesta puede escalar horizontalmente leyendo múltiples mensajes de la cola en paralelo, sin afectar la latencia de las consultas de usuarios.
- **Procesamiento por lotes:** los eventos pueden acumularse y procesarse en lotes durante períodos de baja demanda, reduciendo el costo de las llamadas a APIs de embeddings que cobran por volumen.

**Casos de uso en sistemas de IA:**

- Actualización del knowledge base de un sistema RAG cuando documentos fuente cambian (repositorio de documentos → cola → pipeline de ingesta → base vectorial).
- Evaluación periódica de calidad de respuestas: un proceso nocturno extrae conversaciones del día, las procesa con métricas RAGAS y publica resultados en un dashboard de calidad.
- Pipeline de fine-tuning disparado por eventos: cuando el volumen de conversaciones humanas anotadas supera un umbral, se dispara automáticamente un job de fine-tuning.
- Notificaciones asíncronas en sistemas de agentes: cuando un agente completa una tarea de larga duración (análisis de un informe de 200 páginas), el resultado se publica como evento en lugar de mantener una conexión HTTP abierta.

**Limitaciones que el arquitecto debe gestionar:**

- **Consistencia eventual:** los componentes que leen datos procesados asincrónicamente pueden leer datos desactualizados durante el período entre el evento y su procesamiento. Para sistemas RAG, esto significa que puede haber una ventana de tiempo en la que un documento actualizado aún no está disponible en la base vectorial.
- **Dificultad de debugging:** rastrear un flujo de datos a través de múltiples consumidores de eventos requiere correlación de trazas distribuidas, lo cual es más complejo que rastrear una llamada síncrona.
- **Complejidad operativa:** la cola de mensajes es una infraestructura adicional que debe ser monitoreada, con métricas propias como profundidad de cola, tasa de mensajes sin procesar y latencia de procesamiento.

> **Nota del Arquitecto:** Las arquitecturas basadas en eventos son el mecanismo natural para los pipelines de ingesta de sistemas RAG en producción. Pero el error que cometen muchos equipos es usarlas también para la ruta crítica de consultas del usuario, donde la sincronicidad es un requisito del producto. Un sistema RAG bien diseñado usa eventos para la ingesta (asíncrona, tolerante a latencia) y llamadas síncronas para las consultas de usuario (donde la latencia es un atributo de calidad percibida).

Las tres secciones anteriores han presentado los patrones de arquitectura más frecuentes en sistemas de IA. La sección siguiente aborda la pregunta más fundamental de todo el capítulo: cómo elegir entre ellos, y en particular, cómo tomar la decisión que precede a cualquier elección de patrón de infraestructura — si enriquecer el modelo o enriquecer el contexto.
