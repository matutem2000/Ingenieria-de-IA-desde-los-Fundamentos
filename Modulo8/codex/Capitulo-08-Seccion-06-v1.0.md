# Módulo 8 – Capítulo 08 – Sección 06

# Cierre: la optimización de inferencia local es una disciplina de sistemas, no solo ML

Las técnicas de optimización de inferencia de LLMs (Flash Attention, speculative decoding, prefix caching, PagedAttention) son fundamentalmente innovaciones de sistemas de computación que se aplican a un dominio ML específico: requieren comprensión de arquitecturas de GPU, jerarquías de memoria, pipelines de IO, scheduling de procesos y teoría de colas para ser implementadas e interpretadas correctamente. Un ingenieros de IA que entiende únicamente los aspectos de modelo (arquitectura, parámetros, benchmarks) pero no los aspectos de sistemas (ancho de banda de VRAM, block size del KV cache, scheduling de requests) tomará decisiones de optimización subóptimas porque atacará los síntomas visibles (modelo lento) en lugar de las causas raíz (GPU memory-bound, fragmentación del KV cache, scheduling ineficiente). La brecha de rendimiento entre una implementación naiva y una implementación optimizada del mismo modelo es frecuentemente de un orden de magnitud: vLLM sirviendo Llama 3 8B con PagedAttention, Flash Attention 2 y prefix caching puede lograr 10x más requests por hora con el mismo hardware que Hugging Face Transformers en modo básico. La optimización de inferencia no es un lujo de grandes organizaciones sino una necesidad de cualquier producto que paga por GPU tiempo: el costo por token es directamente proporcional a la eficiencia del sistema de inferencia, y cada mejora de eficiencia se traduce directamente en mayor margen o menor precio al usuario final.

## Idea central

Optimizar la inferencia de un LLM local no termina con elegir el modelo y la cuantización correctos: Flash Attention, speculative decoding, prefix caching y el motor de serving correcto son multiplicadores de rendimiento que juntos pueden reducir el costo por token 5-10x sobre la misma GPU.

---

*"The purpose of abstracting is not to be vague, but to create a new semantic level in which one can be absolutely precise."* — Edsger W. Dijkstra, padre de los algoritmos modernos, recordando que las abstracciones de los motores de inferencia (PagedAttention, Flash Attention) no ocultan la complejidad sino que crean el nivel correcto donde la optimización puede ser exacta y medible.
