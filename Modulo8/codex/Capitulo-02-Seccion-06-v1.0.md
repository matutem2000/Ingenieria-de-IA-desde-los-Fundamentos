# Módulo 8 – Capítulo 02 – Sección 06

# Cierre: la cuantización es la técnica que hace posible ejecutar LLM en hardware accesible

La cuantización ha transformado radicalmente el panorama del despliegue de LLMs: lo que en 2022 requería un clúster de GPUs A100 para ser viable puede ejecutarse en 2025 en una laptop con 16 GB de RAM o en una GPU de consumo de 8 GB de VRAM con calidad apenas degradada. Las técnicas GPTQ, AWQ y los K-quants de GGUF han madurado al punto donde la degradación de calidad en 4 bits es frecuentemente indetectable para usuarios finales en tareas conversacionales, aunque sí medible en benchmarks de razonamiento complejo y matemáticas avanzadas. El proceso de selección de cuantización se ha vuelto parte del ciclo de vida estándar del modelo: organizaciones con prioridades distintas de velocidad, memoria y calidad eligen variantes distintas del mismo modelo base para distintos entornos de despliegue. La cuantización eficiente es además un prerequisito del fine-tuning eficiente: QLoRA, la técnica más popular de ajuste fino local, carga el modelo base en NF4 (4-bit NormalFloat) para reducir el footprint de memoria durante el entrenamiento, permitiendo fine-tuning de modelos de 70B en una sola GPU A100 de 40 GB.

## Idea central

La cuantización no es una solución de compromiso sino una decisión de ingeniería de sistemas: el modelo cuantizado correcto en el hardware correcto supera en latencia y costo total de propiedad a un modelo sin cuantizar en hardware más caro.

---

*"Quantization is not about losing quality — it's about finding the right precision for the right operation."* — Tim Dettmers, investigador de cuantización de redes neuronales y autor de bitsandbytes y QLoRA, sobre el principio fundamental que guía las técnicas modernas de compresión de modelos.
