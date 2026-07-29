# Módulo 4 – Capítulo 08 – Sección 02

## Escalado Horizontal y Vertical

La elección entre escalado horizontal y vertical no es una preferencia tecnológica: es una decisión que depende de las características del componente a escalar, del perfil de demanda del sistema, y del presupuesto operativo. Para sistemas de IA, la mayoría de los componentes del pipeline tienen características que favorecen una estrategia específica, y la combinación de ambas estrategias en un mismo sistema es la norma, no la excepción.

**Escalado horizontal del servicio de inferencia** es el patrón predominante cuando se usan APIs de LLM comerciales (OpenAI, Anthropic, Google). En este caso, el "escalado" horizontal no significa agregar instancias del modelo propio sino distribuir las solicitudes entre múltiples claves de API o entre múltiples proveedores, usando estrategias de round-robin o de enrutamiento por carga. Cuando el equipo opera su propia infraestructura de inferencia — bien sea con modelos open source como Llama, Mistral o Qwen —, el escalado horizontal se implementa con servidores de inferencia especializados. Las opciones principales son:

- **vLLM:** servidor de inferencia open source que implementa PagedAttention para gestión eficiente de la KV cache, permitiendo alta concurrencia con la misma GPU. Soporta múltiples modelos y es la opción de referencia para inferencia de alta concurrencia en hardware propio o arrendado.
- **Text Generation Inference (TGI) de Hugging Face:** servidor de inferencia optimizado para modelos de la biblioteca Hugging Face, con soporte nativo para continuous batching (agrupa múltiples solicitudes para maximizar el uso de la GPU) y tensor parallelism para distribuir un modelo grande entre múltiples GPUs.
- **KServe:** plataforma de serving de modelos de IA sobre Kubernetes, agnóstica al framework de modelo. Proporciona escalado automático, A/B testing de modelos, y gestión del ciclo de vida. Es la opción preferida en organizaciones con infraestructura Kubernetes existente.
- **Ray Serve (ray.io):** sistema de serving escalable que funciona sobre el framework Ray de computación distribuida. Especialmente adecuado para pipelines de IA complejos donde la lógica de serving requiere orquestación de múltiples modelos o componentes.

**Escalado horizontal de la base vectorial** requiere una comprensión de la arquitectura de la base vectorial específica. Pinecone gestiona el sharding automáticamente como servicio gestionado. Weaviate soporta escalado horizontal mediante sharding de colecciones entre múltiples nodos, con replicación para disponibilidad. Qdrant implementa sharding distribuido con rebalanceo automático. pgvector, al operar sobre PostgreSQL, escala a través de los mecanismos de PostgreSQL: réplicas de lectura para distribuir las consultas de búsqueda, y escalado vertical del nodo principal para las escrituras.

**Escalado vertical** es apropiado para componentes donde la distribución horizontal introduce overhead inaceptable. Los modelos de reranking — especialmente los cross-encoders de alta calidad como Cohere Rerank o BGE-Reranker-Large — se benefician del escalado vertical porque procesan la consulta y cada chunk de forma conjunta en la misma instancia, y fragmentar ese procesamiento introduce latencia. Una instancia más potente (más GPU memory, más VRAM) permite procesar batches más grandes y reducir la latencia total. Los modelos de embedding también pueden beneficiarse del escalado vertical cuando el volumen de indexación es alto: una GPU de mayor clase puede generar embeddings a mayor velocidad que dos GPUs de menor clase con el overhead de coordinación.

La combinación correcta para un sistema de IA productivo típico es:

- Servicio de inferencia: escalado horizontal con vLLM o TGI, autoscaling basado en queue depth y TTFT.
- Base vectorial: escalado horizontal mediante sharding gestionado, con réplicas de lectura para alta disponibilidad.
- Servicio de reranking: escalado vertical hasta el límite razonable, con escalado horizontal de backup para picos de demanda.
- Pipeline de ingesta: escalado horizontal con workers batch, sin restricciones de latencia.
- Servicios de soporte (cache, auth, orchestration): escalado horizontal stateless.

> **Nota del Arquitecto:** El error más frecuente en el escalado de sistemas de IA es escalar el servicio de inferencia cuando el cuello de botella real está en la base vectorial o en el servicio de reranking. Antes de tomar cualquier decisión de escalado, siempre mida la latencia de cada etapa del pipeline bajo la carga que produce el problema. La respuesta "necesitamos más GPUs" casi siempre requiere validación: ¿es el GPU realmente el cuello de botella, o es la red entre servicios, o es la base vectorial que necesita más RAM para mantener el índice en caché?

La decisión de escalado horizontal vs. vertical no es permanente: a medida que el sistema crece, la estrategia óptima puede cambiar. Un sistema que comienza con una única instancia vertical potente puede migrar a una arquitectura horizontal a medida que la demanda crece y la paralelización se vuelve más eficiente que el escalado vertical adicional.
