# Módulo 8 – Capítulo 05 – Sección 06

# Cierre: el serving eficiente es tan importante como el modelo mismo

Un modelo de alta calidad desplegado con un motor de inferencia ineficiente puede tener peor experiencia de usuario y mayor costo operativo que un modelo de menor calidad correctamente optimizado: la diferencia entre Hugging Face Transformers naivo y vLLM con PagedAttention en el mismo hardware puede ser un factor de 3-4x en throughput y un factor de 2x en TTFT para cargas concurrentes. El ecosistema de serving de LLMs ha madurado al punto donde la elección del motor de inferencia (llama.cpp para local, vLLM para GPU de producción, TRT-LLM para máxima eficiencia en NVIDIA) es una decisión arquitectónica de primer orden, no un detalle de implementación. Las métricas de serving no son métricas de infraestructura sino métricas de producto: un TTFT de 2 segundos en una aplicación de autocompletado de código destruye la experiencia de usuario independientemente de la calidad del modelo; un throughput insuficiente limita el número de usuarios que puede atender el producto, creando un techo de crecimiento técnico. El AI Engineer que diseña un sistema de serving de LLMs debe pensar simultáneamente en el modelo (calidad), el motor (throughput/latencia), el hardware (VRAM/costo) y los SLOs (TTFT P95, TBT P95, disponibilidad) como un sistema integrado donde la optimización de una dimensión afecta a las demás.

## Idea central

El triángulo de serving es calidad del modelo, latencia de respuesta y costo por token: siempre se puede mejorar uno de los tres a costa de los otros, y la decisión correcta depende exclusivamente de las prioridades del producto.

---

*"A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable."* — Leslie Lamport, Turing Award laureate, recordando que en sistemas de serving de LLMs, la cadena de dependencias (red, GPU driver, runtime, modelo) es tan frágil como su eslabón más débil.
