# Módulo 4 – Capítulo 08 – Sección 01

## Escalabilidad en Plataformas de IA

Escalar un sistema de IA es considerablemente más complejo que escalar un sistema de software convencional. En una aplicación web tradicional, escalar horizontalmente significa agregar más instancias del servidor de aplicaciones detrás de un balanceador de carga. En un sistema de IA, la demanda se distribuye entre componentes con perfiles de carga radicalmente distintos: el servicio de inferencia del LLM (con alta demanda de GPU y costo variable según el modelo), la base vectorial (con demanda de memoria y IOPS para la búsqueda), el pipeline de ingesta (con demanda de CPU y GPU para la generación de embeddings), y los servicios de soporte (autenticación, caching, orquestación). Escalar un componente sin entender los cuellos de botella de los demás produce arquitecturas que escalan parcialmente y fallan en el punto que no se optimizó.

La planificación de la escalabilidad comienza con la comprensión del perfil de carga. Los sistemas de IA tienen perfiles de carga distintos a los de los sistemas transaccionales convencionales. La inferencia de un LLM es CPU/GPU intensiva y tiene latencia variable según la longitud del contexto y la temperatura configurada. La búsqueda vectorial tiene alta demanda de memoria (el índice debe estar en RAM para búsquedas de baja latencia) y es sensible al número concurrente de consultas. El pipeline de ingesta es batch y tolerante a la latencia pero puede tener alta demanda de CPU/GPU para la generación de embeddings. Estas diferencias requieren estrategias de escalado diferenciadas por componente.

Los cuatro patrones de escalado que un arquitecto de IA debe dominar son:

**Escalado horizontal:** agregar más instancias de un servicio para distribuir la carga. Requiere que el servicio sea stateless o que el estado esté externalizado (en Redis, en una base de datos). El servicio de inferencia, el pipeline de recuperación y los agentes workers son candidatos naturales al escalado horizontal. La base vectorial puede escalar horizontalmente mediante sharding, pero requiere configuración cuidadosa para mantener la consistencia de búsqueda.

**Escalado vertical:** aumentar los recursos de una instancia existente (más CPU, más GPU, más memoria). Es apropiado cuando el servicio no puede fragmentarse de manera efectiva — por ejemplo, un modelo de reranking que necesita mantener toda su representación en memoria para funcionar con baja latencia. El escalado vertical tiene límites físicos y es más costoso por unidad de recurso que el escalado horizontal a gran escala.

**Escalado automático (autoscaling):** ajustar dinámicamente el número de instancias según la demanda en tiempo real. En servicios de inferencia, el autoscaling debe configurarse con métricas de cola de solicitudes y latencia, no solo con CPU — la latencia de respuesta es la señal más directa de que se necesita más capacidad. Kubernetes HPA (Horizontal Pod Autoscaler) con métricas personalizadas es el mecanismo estándar en entornos cloud.

**Escalado serverless:** para cargas de trabajo con demanda muy variable o intermitente, el modelo serverless — pagar solo por el tiempo de ejecución, sin capacidad reservada — puede ser más económico. Las funciones serverless son adecuadas para el pipeline de ingesta (ejecutado periódicamente, no continuamente) y para servicios de soporte ligeros. No son adecuadas para el servicio de inferencia principal si el cold start es inaceptable para la experiencia del usuario.

Las métricas que guían las decisiones de escalado en sistemas de IA incluyen:

- **Queue depth:** cuántas solicitudes están esperando ser procesadas. Un queue depth creciente es la señal más clara de insuficiencia de capacidad.
- **Time-to-first-token (TTFT):** en servicios de generación con streaming, el tiempo hasta que el usuario recibe el primer token es la métrica de experiencia más importante. La degradación del TTFT bajo carga indica necesidad de escalado del servicio de inferencia.
- **GPU utilization:** en infraestructura propia de inferencia, la utilización de GPU por debajo del 70-80% indica potencial de compactación; por encima del 90% indica necesidad de escalado.
- **Latencia de búsqueda vectorial:** el P95 y P99 de la búsqueda en la base vectorial deben mantenerse dentro de los SLO definidos bajo carga máxima esperada.

El principio rector de la escalabilidad en sistemas de IA es la sostenibilidad económica. Escalar sin controles de costo produce sistemas que soportan cualquier carga pero que no son financieramente viables a escala. La arquitectura correcta no es la que puede soportar la mayor carga posible, sino la que puede crecer de manera controlada manteniendo el equilibrio entre rendimiento, resiliencia y economía. Las secciones siguientes desarrollan cada una de las estrategias de escalado con herramientas concretas y criterios de decisión.
