# Módulo 8 – Capítulo 06 – Sección 02

## LoRA (Low-Rank Adaptation): adaptar modelos grandes con parámetros mínimos

El fine-tuning completo de un modelo de 7B parámetros en BF16 requiere calcular gradientes para todos los 7.000 millones de parámetros, almacenar el estado del optimizador Adam (dos momentos por parámetro: 2 × 7B × 4 bytes = 56 GB solo para el optimizador), y los buffers de gradiente (otros 14 GB). El total supera los 100 GB de VRAM para un modelo de 7B, lo que hace el full fine-tuning impracticable en cualquier hardware que no sea un sistema multi-GPU de datacenter de alta gama. LoRA resuelve este problema con una observación matemática elegante: las actualizaciones de pesos durante el fine-tuning son intrínsecamente de bajo rango.

La idea central de LoRA es que para una capa de peso `W₀ ∈ R^(d×k)`, en lugar de aprender la actualización completa `ΔW ∈ R^(d×k)`, se aprende una aproximación de bajo rango `ΔW = BA` donde `B ∈ R^(d×r)` y `A ∈ R^(r×k)` con `r << min(d,k)`. La actualización efectiva es `W = W₀ + αBA/r` donde `α` es el hiperparámetro de escala (lora_alpha). Para un modelo Llama 3 8B con rank `r=16`, los adaptadores LoRA en las proyecciones Q, K, V y O de todas las 32 capas del transformer suman aproximadamente 41 millones de parámetros entrenables, comparado con los 8.000 millones del modelo completo. El ratio de compresión es de casi 200x en parámetros entrenables.

Esta reducción tiene consecuencias prácticas inmediatas: los gradientes y el estado del optimizador solo se calculan para los 41 millones de parámetros LoRA, no para los 8.000 millones congelados del modelo base. El resultado es que el fine-tuning LoRA de Llama 3 8B en BF16 completo requiere aproximadamente 20 GB de VRAM —dentro del alcance de GPUs de 24 GB de consumo— mientras el full fine-tuning requeriría más de 100 GB. Cuando se combina con la cuantización del modelo base a 4 bits (QLoRA, presentada en la siguiente sección), el requisito de VRAM cae a 8-10 GB, haciendo el fine-tuning viable en GPUs de consumo de 12 GB o incluso 8 GB.

En inferencia, los adaptadores LoRA no introducen overhead de latencia cuando se fusionan con el modelo base: `model.merge_and_unload()` de la librería PEFT calcula `W = W₀ + αBA/r` para cada capa y almacena el resultado directamente en los pesos del modelo, produciendo un modelo fusionado idéntico en arquitectura al modelo base original pero con los pesos ajustados al dominio de fine-tuning. El modelo fusionado puede ser exportado a GGUF para servicio con Ollama/llama.cpp o desplegado directamente en vLLM sin ningún overhead adicional respecto al modelo base sin adaptadores.

Los hiperparámetros de LoRA más importantes son: `r` (el rango de la aproximación, típicamente 8-64), `lora_alpha` (el factor de escala, frecuentemente igual a `r` o el doble), y `target_modules` (qué proyecciones reciben adaptadores). Para tareas de conocimiento de dominio o formato específico, `target_modules=["q_proj", "k_proj", "v_proj", "o_proj"]` es el estándar; incluir las capas MLP (`gate_proj`, `up_proj`, `down_proj`) mejora la calidad en tareas de conocimiento pero duplica el número de parámetros LoRA. La variante DoRA (Weight-Decomposed Low-Rank Adaptation) separa la actualización en magnitud y dirección, consistentemente superando a LoRA estándar con el mismo número de parámetros: disponible como `use_dora=True` en la librería PEFT.

## Conceptos técnicos de LoRA

- **Módulos objetivo típicos:** `q_proj`, `k_proj`, `v_proj`, `o_proj` en las capas de atención; incluir capas MLP mejora calidad en tareas de conocimiento pero duplica parámetros.
- **Selección de rank:** `r=16` es el punto de inicio estándar; `r=4-8` para tareas simples (clasificación, reformateo); `r=32-64` para tareas complejas de razonamiento o conocimiento profundo.
- **DoRA:** variante que descompone la actualización en magnitud y dirección; consistentemente supera a LoRA estándar; disponible como `use_dora=True` en PEFT.
- **Saving y carga:** los adaptadores se guardan como archivos de ~50-300 MB en formato SafeTensors; se cargan y fusionan en segundos con `PeftModel.from_pretrained()`.
- **Stacking de adaptadores:** múltiples adaptadores LoRA para distintas tareas; cambio dinámico con `model.set_adapter("tarea_1")`; útil para servir múltiples especializaciones del mismo modelo base.

> **Nota del Arquitecto:** El rango del adaptador LoRA es frecuentemente el hiperparámetro más importante para la calidad del fine-tuning. Con `r=8` y datos de alta calidad, obtendrás buenos resultados para tareas de formato y estilo. Con `r=16`, cubrirás la mayoría de las tareas de conocimiento de dominio. Solo en casos donde el dominio es extremadamente técnico y los ejemplos son pocos necesitarás `r=32-64`. Escalar el rango más allá de ese punto pocas veces mejora la calidad y aumenta el riesgo de overfitting.

LoRA establece la base de todos los métodos de fine-tuning eficiente presentados en este capítulo. La sección siguiente presenta QLoRA, que combina LoRA con cuantización del modelo base a 4 bits para hacer viable el fine-tuning en hardware de consumo.

---
