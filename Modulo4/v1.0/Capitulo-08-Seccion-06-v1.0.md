# Módulo 4 – Capítulo 08 – Sección 06

## Resumen

Este capítulo desarrolló la escalabilidad como la disciplina que determina si un sistema de IA puede crecer con el negocio sin convertirse en una carga operativa insostenible. Escalar un sistema de IA no es escalar un único servicio: es escalar un ecosistema de componentes interdependientes con perfiles de carga radicalmente distintos, y hacerlo de manera que el costo operativo crezca de forma proporcional al valor generado, no de forma exponencial.

Las estrategias de escalado horizontal y vertical deben aplicarse diferenciadamente por componente. El servicio de inferencia escala horizontalmente con servidores especializados como vLLM, TGI, KServe o Ray Serve, que maximizan la utilización de GPU mediante continuous batching. La base vectorial escala horizontalmente mediante sharding y replicación. Los modelos de reranking y los servicios con estado que no pueden fragmentarse eficientemente escalan verticalmente. El pipeline de ingesta escala horizontalmente con workers batch en instancias de bajo costo, aprovechando su tolerancia a la latencia.

El balanceo de carga en sistemas de IA va más allá del round-robin: el balanceo con conciencia de carga, el enrutamiento por características de la solicitud, el circuit breaker para APIs de LLM, y el caché semántico son mecanismos que distribuyen eficientemente una carga altamente heterogénea. La separación de pools de recursos para usuarios con distintos SLOs garantiza que la alta demanda de un segmento no degrada la experiencia de otro.

La optimización de costos es la dimensión de la escalabilidad más directamente conectada con la viabilidad del sistema. La selección del modelo por tipo de tarea — reservar los modelos poderosos para tareas que genuinamente los requieren — es la palanca de mayor impacto. El continuous batching, el prompt caching, el caché semántico de respuestas, y el procesamiento batch para el pipeline de ingesta son las optimizaciones técnicas más efectivas. La práctica de right-sizing basado en percentiles de demanda real, en lugar de capacidad de pico máximo, cierra el círculo.

La alta disponibilidad en sistemas de IA combina los mecanismos estándar — redundancia, despliegues sin interrupción, degradación controlada — con estrategias específicas del dominio: redundancia multi-proveedor de LLM, checkpointing de estado de agentes, y synthetic monitoring del flujo completo del sistema. El resultado no es un sistema que nunca falla, sino un sistema que falla de manera controlada y se recupera rápidamente.

El principio que une todas las dimensiones de la escalabilidad es el equilibrio: la mejor arquitectura no es la que soporta la mayor carga posible, sino la que puede crecer de manera controlada, sostenible y económicamente viable. El arquitecto que diseña con ese principio en mente construye sistemas que el negocio puede operar con confianza a medida que crece.

El Capítulo 09 cierra el arco operativo del módulo con la disciplina que da coherencia a todo lo anterior: el gobierno de plataformas de IA. Mientras la observabilidad, la seguridad y la escalabilidad son disciplinas técnicas de operación, el gobierno es la disciplina organizacional que asegura que todos esos esfuerzos técnicos se traducen en capacidades institucionales sostenibles.

---

*"La mejor arquitectura no es la que soporta la mayor carga, sino la que puede crecer de manera controlada, sostenible y económicamente viable."*
— Principio de escalabilidad en plataformas de IA
