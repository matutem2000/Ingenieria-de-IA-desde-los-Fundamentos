# Módulo 8 – Capítulo 08 – Sección 06

## Cierre: la optimización de inferencia local es una disciplina de sistemas, no solo ML

Las técnicas presentadas en este capítulo —Flash Attention, speculative decoding, prefix caching, chunked prefill, y el perfilado con Nsight y Prometheus— son fundamentalmente innovaciones de sistemas de computación aplicadas al dominio de los LLMs. Requieren comprensión de la jerarquía de memoria de las GPUs (HBM vs SRAM on-chip), del perfil de operaciones de los transformers (memory-bound vs compute-bound), del scheduling de requests en sistemas concurrentes (continuous batching, KV cache management), y de la teoría de colas (queue depth, percentiles de latencia). Un AI Engineer que solo comprende los aspectos de modelo —arquitectura, benchmarks, cuantización— pero no los aspectos de sistemas, tomará decisiones de optimización subóptimas porque atacará los síntomas visibles en lugar de las causas raíz.

La brecha de rendimiento entre una implementación naiva y una optimizada del mismo modelo es frecuentemente de un orden de magnitud. Considerar Llama 3 8B en BF16 sirviendo usuarios en producción: con Hugging Face Transformers en modo básico sin batching, el throughput puede ser de 100-200 tokens/s por GPU y el TTFT de 500ms-2s para prompts moderados; con vLLM + PagedAttention + continuous batching + prefix caching + Flash Attention 2 + chunked prefill, el mismo modelo en el mismo hardware puede superar 2.500 tokens/s de throughput agregado y TTFT < 200ms para el P95 bajo carga moderada. Esa diferencia de 10-15x no proviene de ningún cambio en el modelo: proviene de cómo se gestiona la memoria, cómo se planifican las requests y cómo se implementa matemáticamente la operación de atención.

La optimización de inferencia tampoco es un proyecto único de mejora sino un proceso continuo. Los modelos se actualizan (nuevas versiones de Llama, Mistral, Qwen con diferentes tamaños de KV cache o ventanas de atención), el tráfico del producto evoluciona (mayores contextos promedio a medida que los usuarios aprenden a usar el producto), y el hardware se renueva (nuevas generaciones de GPU con FP8 nativo o mayor ancho de banda de VRAM). Cada uno de estos cambios puede desplazar el cuello de botella a un componente distinto y requerir re-perfilar para aplicar la optimización correcta en el nuevo contexto.

Lo que distingue al AI Engineer maduro en este dominio es la capacidad de leer las métricas de Prometheus, identificar el componente limitante del sistema actual, seleccionar la técnica de optimización correspondiente, medirla después de aplicarla, y iterar. Esta disciplina de optimización empírica guiada por datos, aplicada a sistemas de serving de LLMs, es exactamente la misma que los ingenieros de bases de datos aplican con EXPLAIN ANALYZE en SQL o los ingenieros de sistemas aplican con perf en C++: el dominio es nuevo, el método es el mismo.

## Idea central

Optimizar la inferencia de un LLM local no termina con elegir el modelo y la cuantización correctos: Flash Attention, speculative decoding, prefix caching y el motor de serving correcto son multiplicadores de rendimiento que juntos pueden reducir el costo por token 5-10x sobre la misma GPU.

---

*"The purpose of abstracting is not to be vague, but to create a new semantic level in which one can be absolutely precise."* — Edsger W. Dijkstra, padre de los algoritmos modernos, recordando que las abstracciones de los motores de inferencia (PagedAttention, Flash Attention) no ocultan la complejidad sino que crean el nivel correcto donde la optimización puede ser exacta y medible.
