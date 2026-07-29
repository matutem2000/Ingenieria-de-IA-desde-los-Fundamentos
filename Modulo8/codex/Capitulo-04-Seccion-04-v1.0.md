# Módulo 8 – Capítulo 04 – Sección 04

# Apple Silicon: MLX y la ventaja de la memoria unificada para modelos medianos

La arquitectura de memoria unificada (Unified Memory Architecture, UMA) de los chips Apple Silicon M-series representa una ventaja fundamental para inferencia de LLMs que no tiene equivalente directo en plataformas x86+GPU discreta: la CPU, GPU y Neural Engine comparten el mismo pool físico de RAM de alta velocidad (LPDDR5/5X), eliminando la transferencia PCIe que limita el offloading parcial de modelos en sistemas convencionales. En una Mac con M3 Max y 128 GB de memoria unificada, la GPU integrada puede acceder a toda esa memoria como VRAM efectiva, permitiendo cargar Llama 3 70B en Q4_K_M (~40 GB) completamente en "VRAM" y generar tokens a 15-25 tokens/s, rendimiento imposible de alcanzar con una sola GPU discreta de 24 GB y offloading CPU en hardware similar. MLX (Machine Learning eXplore) es el framework de aprendizaje automático nativo de Apple, desarrollado por Apple Research y diseñado específicamente para la arquitectura UMA de Apple Silicon: su diseño lazy evaluation y operaciones en el espacio de memoria unificada permiten eficiencia superior a llama.cpp/Metal en muchos modelos, con una API Python y Swift similar a NumPy/PyTorch. La librería `mlx-lm` implementa inferencia optimizada para los principales modelos (Llama, Mistral, Gemma, Phi, Qwen) con cuantización nativa en 4 bits vía `mlx.core.quantize()` y fine-tuning con LoRA directamente en Apple Silicon.

## Aspectos técnicos de Apple Silicon para LLMs

- Ancho de banda de memoria: los M3 Max/Ultra tienen 400-800 GB/s de ancho de banda de memoria unificada, comparable o superior al de algunas GPUs de datacenter; este ancho de banda es el factor determinante en la velocidad de generación de tokens (memory-bound)
- MLX vs llama.cpp en Apple Silicon: MLX generalmente supera a llama.cpp+Metal en tokens/s para modelos medianos (7B-34B) porque está diseñado desde cero para la arquitectura UMA; llama.cpp tiene más variedad de formatos y mayor portabilidad cross-platform
- Cuantización nativa en MLX: `mlx_lm.convert --hf-path <modelo> --mlx-path <destino> -q --q-bits 4` convierte un modelo de Hugging Face a formato MLX con cuantización INT4; los archivos resultantes son npz/safetensors con metadatos de cuantización propios del formato MLX
- Fine-tuning con LoRA en MLX: `mlx_lm.lora --model <modelo> --data <datos> --iters 1000 --lora-layers 8` ejecuta fine-tuning LoRA directamente en Apple Silicon; viable para modelos de hasta 7B en un M2 Pro/Max con 32-64 GB de memoria
- Limitaciones: no hay soporte multi-GPU en Apple Silicon (los chips Ultra son dos die conectados por die-to-die interconnect, no múltiples GPUs independientes); el ecosistema de software (vLLM, TensorRT) no soporta Apple Silicon para producción escalable

## Para recordar

Apple Silicon con MLX es la mejor opción para desarrollo local y producción de baja escala cuando se necesita ejecutar modelos de 13B-70B sin el costo y complejidad de una GPU de datacenter, aprovechando la memoria unificada como VRAM efectiva de alta capacidad.
