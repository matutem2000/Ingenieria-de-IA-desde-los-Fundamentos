# Módulo 8 – Capítulo 04 – Sección 01

# GPU vs CPU vs Apple Silicon: cuándo usar cada arquitectura

La elección del hardware de inferencia para LLMs no es una decisión de presupuesto sino de arquitectura: cada tipo de procesador tiene ventajas y limitaciones específicas que lo hacen óptimo para rangos distintos de tamaños de modelo, patrones de uso y requisitos de latencia. Las GPUs NVIDIA son el estándar de producción para modelos de 7B parámetros o más que requieren alta velocidad de generación: su arquitectura SIMD con miles de núcleos CUDA opera las multiplicaciones matriciales de transformers con throughput 10-50x superior a una CPU de última generación, con la restricción fundamental de que el modelo completo debe caber en VRAM para máxima eficiencia. La inferencia en CPU es viable para modelos cuantizados de 3B-7B cuando la VRAM no está disponible o cuando la latencia total (no por token) es aceptable: llama.cpp con instrucciones AVX2 en un procesador moderno de 16 núcleos puede generar 15-25 tokens/s con un modelo Q4_K_M de 7B, suficiente para muchas aplicaciones interactivas. Apple Silicon (M1/M2/M3/M4) ocupa un nicho único gracias a su arquitectura de memoria unificada: la GPU integrada comparte el mismo pool de RAM con la CPU, eliminando el cuello de botella de transferencia PCIe y permitiendo usar toda la RAM del sistema como VRAM efectiva, haciendo viable la inferencia de modelos de 13B-34B con calidad Q8 en equipos de consumo.

## Cuándo usar cada arquitectura

- GPU NVIDIA dedicada: optimal para producción con múltiples usuarios concurrentes; required para fine-tuning con QLoRA; modelos de 7B+ con Q4 funcionan en GPUs de 8 GB VRAM; modelos de 70B requieren 48 GB+ VRAM o multi-GPU con tensor parallelism
- CPU moderna (x86-64 con AVX2): adecuada para desarrollo local, inferencia ocasional o cuando el presupuesto no permite GPU dedicada; modelos de hasta 13B en Q4_K_M funcionan con 32 GB RAM; la velocidad de generación (5-20 tokens/s) es acceptable para muchas tareas no interactivas
- Apple Silicon (M-series): el punto óptimo para desarrollo y producción de baja-media escala; un M3 Max con 128 GB de memoria unificada puede ejecutar Llama 3 70B en Q4 a 15-25 tokens/s; la integración Metal/MLX minimiza el overhead de gestión de memoria entre CPU y GPU
- GPU AMD con ROCm: viable en Linux con soporte ROCm 6.x; el soporte en llama.cpp, vLLM y PyTorch ha mejorado significativamente pero sigue siendo más inestable que CUDA; las GPU Radeon RX 7900 XTX (24 GB VRAM) son competitivas en precio/rendimiento para inferencia de 7B-13B
- Aceleradores especializados: NPUs en dispositivos móviles (Apple Neural Engine, Qualcomm Hexagon) son opciones emergentes para inferencia en el borde con modelos 1B-3B; Intel Gaudi y Google TPUs son relevantes para fine-tuning a escala pero no para inferencia individual

## Para recordar

La regla práctica más útil: si el modelo cabe en VRAM, usa GPU; si no cabe pero tienes suficiente RAM, usa Apple Silicon (memoria unificada) o CPU (más lenta pero funcional); si necesitas máxima escala y concurrencia, usa GPU multi-instancia en la nube.
