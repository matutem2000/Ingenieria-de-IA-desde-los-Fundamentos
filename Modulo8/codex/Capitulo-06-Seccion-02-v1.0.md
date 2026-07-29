# Módulo 8 – Capítulo 06 – Sección 02

# LoRA (Low-Rank Adaptation): adaptar modelos grandes con parámetros mínimos

LoRA (Low-Rank Adaptation), introducida por Hu et al. de Microsoft Research en 2021, es una técnica de fine-tuning eficiente en parámetros que congela todos los pesos del modelo pre-entrenado y aprende únicamente matrices de adaptación de bajo rango que se suman a las proyecciones de atención (y opcionalmente a las capas FFN), reduciendo el número de parámetros entrenables en 10.000x o más respecto al full fine-tuning. La idea matemática central de LoRA es que las actualizaciones de pesos durante el fine-tuning tienen intrínsecamente bajo rango: para una capa de peso W₀ ∈ R^(d×k), LoRA aprende ΔW = BA donde B ∈ R^(d×r) y A ∈ R^(r×k) con r << min(d,k); la actualización completa es W = W₀ + αBA/r donde α es el parámetro de escala que controla la magnitud de la adaptación. Para un modelo Llama 3 8B con rank r=16, los adaptadores LoRA en las proyecciones Q, K, V y O de todas las capas suman aproximadamente 41 millones de parámetros entrenables (vs 8.000 millones del modelo completo), permitiendo el entrenamiento en una GPU de 24 GB sin reducir el batch size; en producción, los pesos LoRA se fusionan con los pesos base usando `merge_and_unload()` sin overhead de latencia adicional. Los hiperparámetros clave de LoRA son el rango `r` (típicamente 8-64, valores mayores aumentan capacidad pero también número de parámetros y riesgo de overfitting), `lora_alpha` (factor de escala, frecuentemente igual a `r` o el doble) y `target_modules` (qué proyecciones reciben adaptadores).

## Conceptos técnicos de LoRA

- Módulos objetivo típicos: en arquitecturas de atención, los módulos más beneficiados son `q_proj`, `k_proj`, `v_proj` y `o_proj`; incluir `gate_proj`, `up_proj` y `down_proj` en las capas MLP mejora la calidad en tareas de conocimiento pero duplica el número de parámetros LoRA
- Rank selection: rank=16 es el punto de inicio estándar; para tareas simples (clasificación, reformateo) rank=4-8 es suficiente; para tareas complejas de razonamiento o conocimiento de dominio, rank=32-64 puede mejorar la calidad con impacto mínimo en memoria
- DoRA (Weight-Decomposed Low-Rank Adaptation): variante que descompone la actualización en magnitud y dirección; consistentemente supera a LoRA estándar con el mismo número de parámetros, disponible como `use_dora=True` en PEFT
- Saving y carga: los adaptadores LoRA se guardan como archivos de ~50-300 MB (dependiendo del rank y los módulos) con `model.save_pretrained()` en formato SafeTensors; se cargan y fusionan en segundos con `PeftModel.from_pretrained()`
- Stacking de adaptadores: es posible tener múltiples adaptadores LoRA para distintas tareas y cambiar entre ellos dinámicamente con `model.set_adapter("tarea_1")`; útil para servir múltiples specializations del mismo modelo base con una única instancia en VRAM

## Para recordar

LoRA es la técnica de fine-tuning más universalmente aplicable: su combinación de eficiencia en parámetros, compatibilidad con cualquier arquitectura Transformer y overhead de inferencia cero tras fusión la convierten en el punto de inicio estándar para cualquier proyecto de adaptación de LLMs.
