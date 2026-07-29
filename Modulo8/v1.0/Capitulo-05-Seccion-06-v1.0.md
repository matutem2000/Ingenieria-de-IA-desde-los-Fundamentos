# Módulo 8 – Capítulo 05 – Sección 06

## Cierre: el serving eficiente es tan importante como el modelo mismo

La infraestructura de serving de LLMs no es el envoltorio de un modelo: es una de las decisiones técnicas más impactantes en la economía de un producto de IA. Un modelo de alta calidad desplegado con un motor de inferencia ineficiente puede tener peor experiencia de usuario y mayor costo operativo que un modelo de menor calidad correctamente optimizado. La diferencia entre Hugging Face Transformers en modo básico y vLLM con PagedAttention en el mismo hardware puede ser un factor de 3-5x en throughput y un factor de 2x en TTFT para cargas concurrentes, sin ninguna diferencia en el modelo, los pesos o la cuantización.

El ecosistema de serving de LLMs ha madurado al punto donde la elección del motor de inferencia es una decisión arquitectónica de primer orden que debe tomarse con el mismo rigor que la elección del modelo. La guía de selección presentada al inicio del capítulo —Ollama para prototipado local, vLLM para producción GPU de un modelo, Triton para múltiples tipos de modelos, TRT-LLM para máxima eficiencia en NVIDIA— captura la lógica de selección. Aplicarla correctamente requiere conocer los SLOs de latencia y throughput del producto antes de evaluar opciones de motor, y medir con métricas reales (TTFT P95, TBT P95, throughput agregado) en lugar de benchmarks sintéticos en aislamiento.

Las métricas de serving no son métricas de infraestructura sino métricas de producto. Un TTFT de 2 segundos en una aplicación de autocompletado de código destruye la experiencia de usuario independientemente de la calidad del modelo; un throughput insuficiente limita el número de usuarios que puede atender el producto, creando un techo de crecimiento técnico que solo puede resolverse con más hardware o con un motor más eficiente. El AI Engineer que diseña un sistema de serving de LLMs debe pensar simultáneamente en el modelo (calidad), el motor (throughput/latencia), el hardware (VRAM/costo) y los SLOs (TTFT P95, TBT P95, disponibilidad) como un sistema integrado donde la optimización de una dimensión afecta a las demás.

El capítulo siguiente aborda la especialización de los modelos mediante fine-tuning: cómo adaptar un modelo base a una tarea o dominio específico para mejorar la calidad en la tarea sin incrementar el costo de inferencia. Los capítulos de hardware (4) y serving (5) que acabas de completar son el contexto necesario para entender las restricciones de fine-tuning: QLoRA requiere al menos 8 GB de VRAM, Axolotl con DeepSpeed multi-GPU requiere conocer el hardware disponible en la nube, y el fine-tuned model debe eventualmente desplegarse en el motor de serving que ya tienes configurado.

## Idea central

El triángulo de serving es calidad del modelo, latencia de respuesta y costo por token: siempre se puede mejorar uno de los tres a costa de los otros, y la decisión correcta depende exclusivamente de las prioridades del producto.

---

*"A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable."* — Leslie Lamport, Turing Award laureate, recordando que en sistemas de serving de LLMs, la cadena de dependencias (red, GPU driver, runtime, modelo) es tan frágil como su eslabón más débil.
