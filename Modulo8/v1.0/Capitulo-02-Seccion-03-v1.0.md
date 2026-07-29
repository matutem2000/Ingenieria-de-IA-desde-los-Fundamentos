# Módulo 8 – Capítulo 02 – Sección 03

## GPTQ: cuantización post-entrenamiento de 4 bits optimizada para GPU

El formato GGUF con K-quants es la solución universal para inferencia local en cualquier plataforma, pero no es el formato de mayor throughput en GPU NVIDIA cuando la velocidad de generación de tokens es la métrica crítica. GPTQ fue diseñado con un objetivo diferente: extraer el máximo rendimiento de inferencia en GPU aplicando un algoritmo matemáticamente sofisticado que minimiza el error de cuantización de forma mucho más inteligente que el redondeo directo. El resultado es un modelo en INT4 que se comporta en GPU NVIDIA con throughput superior al de las variantes K-quant del mismo nivel de compresión.

GPTQ (Generative Pre-trained Transformer Quantization), desarrollado por Frantar et al. en 2022, resuelve el problema de cuantización capa por capa usando el Optimal Brain Surgeon (OBS) framework: cuantiza los pesos de una fila de la matriz de pesos en orden óptimo (determinado por la matriz Hessiana del error), ajustando los pesos restantes no cuantizados de esa misma fila para compensar el error introducido por cada cuantización individual. Este proceso es fundamentalmente más costoso computacionalmente que el redondeo directo —y por eso tarda horas en lugar de minutos— pero produce modelos con calidad significativamente superior para el mismo nivel de compresión.

La novedad de GPTQ respecto a técnicas anteriores es que adapta el OBS framework para escalar a modelos de decenas de miles de millones de parámetros. Para lograrlo, trabaja en bloques (columnas de la matriz de pesos) y usa una versión aproximada de la Hessiana calculada sobre un dataset de calibración: entre 128 y 1024 muestras de texto representativas del dominio de uso. La elección del dataset de calibración es una decisión de ingeniería con impacto en la calidad: calibrar con datos del mismo dominio del producto mejora la calidad del modelo cuantizado para ese dominio específico respecto a calibrar con datos genéricos de C4 o WikiText. Para un modelo de código, calibrar con código Python y SQL puede mejorar el rendimiento de cuantización en esas tareas.

Los modelos GPTQ se distribuyen en formato SafeTensors en Hugging Face con sufijos `–GPTQ` o `–4bit` en el nombre del repositorio, e incluyen un archivo `quantize_config.json` con los parámetros de cuantización usados: número de bits, tamaño de grupo (group_size, tipicamente 128), y si la cuantización de activaciones está habilitada. Para la inferencia, los modelos GPTQ requieren librerías específicas: `auto-gptq` es la opción más compatible con el ecosistema Hugging Face y permite cargar el modelo con `AutoGPTQForCausalLM.from_quantized(model_name)`. Para mayor velocidad, `exllamav2` ofrece kernels GPU optimizados que pueden superar el throughput de auto-gptq en un factor de 2-3x en GPUs NVIDIA modernas como la RTX 4090.

GPTQ con 4 bits y group_size=128 logra perplexity comparable a FP16 en la mayoría de los benchmarks, con una degradación inferior al 1% en WikiText-2 para modelos de 7B o más parámetros. En comparación, la variante Q4_K_M de GGUF logra una degradación ligeramente superior porque su algoritmo de cuantización es más simple. Para producción en GPU NVIDIA donde el throughput de tokens por segundo es la métrica crítica, GPTQ con exllamav2 es la opción preferida; para portabilidad y compatibilidad con múltiples plataformas, GGUF sigue siendo la elección correcta.

## Aspectos técnicos de GPTQ

- **Proceso de calibración:** 128-1024 muestras de texto para calcular la Hessiana; duración de 30 minutos a varias horas según el tamaño del modelo y la GPU; calibrar con datos del dominio del producto mejora la calidad para ese dominio.
- **Tamaño de grupo:** group_size de 32, 64 o 128 (128 es el estándar más usado); grupos más pequeños mejoran la calidad pero aumentan el overhead de los factores de escala.
- **Formato de distribución:** SafeTensors con `quantize_config.json` en el repositorio de Hugging Face; identificables por el sufijo `-GPTQ` o `-4bit`.
- **Librerías de inferencia:** `auto-gptq` para compatibilidad máxima; `exllamav2` para 2-3x mayor throughput en GPUs NVIDIA modernas con kernels CUDA optimizados.
- **Compatibilidad de hardware:** requiere soporte para dequantización INT4 eficiente en GPU; funciona desde GPUs Pascal (GTX 1080) en adelante para NVIDIA; soporte AMD ROCm limitado en algunas librerías.

> **Nota del Arquitecto:** El tiempo de calibración de GPTQ es una inversión única: una vez cuantizado, el modelo puede distribuirse y reutilizarse. En producción, la decisión entre GPTQ y GGUF Q4_K_M se reduce a: si usas exclusivamente GPU NVIDIA y la librería exllamav2 es viable en tu stack, GPTQ da mayor throughput; si necesitas portabilidad multiplataforma (Mac, AMD, CPU) o integración con Ollama, GGUF es más simple. Para la mayoría de los equipos pequeños, GGUF es la elección pragmática correcta porque reduce la complejidad operativa.

La siguiente sección examina AWQ, una técnica de cuantización más reciente que logra mejor calidad que GPTQ en modelos pequeños con un proceso de cuantización mucho más rápido, particularmente relevante para equipos que necesitan iterar entre versiones de modelos frecuentemente.

---
