# Módulo 8 – Capítulo 06 – Sección 03

# QLoRA: fine-tuning con cuantización de 4 bits para hardware limitado

QLoRA (Quantized LoRA), publicada por Dettmers et al. de la Universidad de Washington en mayo de 2023, combina tres innovaciones técnicas que permiten fine-tuning de modelos de 65B parámetros en una sola GPU de 48 GB (o modelos de 7B en GPUs de 8 GB): cuantización del modelo base a NF4 (Normal Float 4-bit), paginación del estado del optimizador a CPU RAM cuando la VRAM se satura, y adaptadores LoRA entrenados en BF16 sobre el modelo base cuantizado. NF4 (NormalFloat 4-bit) es el tipo de dato central de QLoRA: a diferencia de INT4 que usa representación de enteros uniforme, NF4 distribuye los 16 posibles valores de 4 bits de acuerdo con la distribución normal de los pesos de redes neuronales entrenadas con SGD, logrando menor error de cuantización que INT4 para los valores más frecuentes. La precisión doble (double quantization) de QLoRA cuantiza adicionalmente los factores de escala de la cuantización NF4 (que en cuantización estándar se almacenan en FP32) a FP8, reduciendo el uso de memoria en ~0.37 bits adicionales por parámetro; combinado con el tamaño de grupo de 64, QLoRA logra 4.5 bits por parámetro efectivos vs 16 bits en BF16. El overhead de dequantización de NF4 a BF16 durante el forward pass introduce una penalización de velocidad de 15-30% respecto a LoRA sobre un modelo en BF16, pero el acceso a GPUs de menor costo o mayor capacidad de modelo más que compensa esta penalización en la mayoría de los escenarios.

## Aspectos técnicos de QLoRA

- Cuantización NF4: divide el rango de valores en 16 cuantiles igualmente probables según una distribución normal estándar; los valores de cuantización son asimétricos (-1.0, -0.69, -0.52, ..., 0.52, 0.69, 1.0) vs INT4 uniformes; reduce el MSE de cuantización 35% respecto a INT4 para pesos pre-entrenados
- Paginación a CPU (paged optimizers): la librería bitsandbytes implementa un optimizador Adam de 8 bits con paginación automática a CPU cuando la VRAM se satura; el overhead de paginación es mínimo (<5%) cuando solo ocurre ocasionalmente; disponible con `optim="paged_adamw_8bit"`
- Configuración mínima con transformers + PEFT: `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16)` carga el modelo base en NF4; `LoraConfig(r=16, lora_alpha=32, target_modules=["q_proj","v_proj"])` define los adaptadores; `get_peft_model()` combina ambos
- Gradient checkpointing: `model.enable_input_require_grads()` y `training_args.gradient_checkpointing=True` reduce la memoria de activaciones durante el backward pass a costa de recalcular activaciones; esencial para aumentar el sequence length o batch size dentro del presupuesto de VRAM
- Comparación memoria vs LoRA estándar: fine-tuning LoRA de Llama 3 8B en BF16 requiere ~20 GB de VRAM; el mismo fine-tuning con QLoRA requiere ~8 GB de VRAM, haciendo viable el entrenamiento en GPUs de consumo de 8-12 GB

## Para recordar

QLoRA democratiza el fine-tuning de LLMs de 7B-13B en hardware de consumo: la penalización de velocidad del 20-30% respecto a LoRA en BF16 es un costo razonable cuando la alternativa es no poder entrenar el modelo por restricciones de VRAM.
