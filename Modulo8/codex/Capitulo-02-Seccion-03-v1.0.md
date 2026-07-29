# Módulo 8 – Capítulo 02 – Sección 03

# GPTQ: cuantización post-entrenamiento de 4 bits optimizada para GPU

GPTQ (Generative Pre-trained Transformer Quantization) es un algoritmo de cuantización post-entrenamiento desarrollado por Frantar et al. (2022) que resuelve el problema de cuantización capa por capa minimizando el error cuadrático medio entre la salida de la capa original en FP16 y la salida de la capa cuantizada, usando la matriz Hessiana del error para determinar el orden óptimo de cuantización de los pesos. La innovación central de GPTQ es el uso del Optimal Brain Surgeon (OBS) framework adaptado para escalar a modelos de decenas de miles de millones de parámetros: cuantiza un peso a la vez y ajusta los pesos restantes de la misma fila para compensar el error introducido, logrando mejor calidad que la cuantización naive de redondeo a la baja con un overhead computacional razonable. Los modelos GPTQ se distribuyen en formato SafeTensors y requieren librerías específicas para inferencia: `auto-gptq` o `exllamav2` son los backends más utilizados, con exllamav2 ofreciendo throughput 2-3x superior a auto-gptq en GPUs NVIDIA modernas. GPTQ con 4 bits por peso y un tamaño de grupo de 128 logra perplexity comparable a FP16 en la mayoría de los benchmarks, con una degradación inferior al 1% en WikiText-2 para modelos de 7B o más parámetros.

## Aspectos técnicos de GPTQ

- Proceso de calibración: requiere entre 128 y 1024 muestras de texto de calibración (típicamente de C4 o WikiText) para calcular la matriz Hessiana; tarda entre 30 minutos y varias horas dependiendo del tamaño del modelo y la GPU disponible
- Tamaño de grupo (group size): valores comunes son 32, 64, 128 y -1 (sin agrupación); grupos más pequeños mejoran la calidad pero aumentan el overhead de memoria para los factores de escala; group_size=128 es el estándar más usado
- Actq (activation quantization): GPTQ original no cuantiza activaciones, solo pesos; variantes como GPTQ-Actq o AQLM extienden la cuantización a activaciones para mayor compresión
- Formato de distribución: los modelos GPTQ se publican en Hugging Face con sufijo `-GPTQ` o `-4bit`; incluyen archivos `quantize_config.json` con los metadatos de cuantización (bits, group_size, desc_act) necesarios para carga correcta
- Compatibilidad de hardware: GPTQ en INT4 requiere soporte para operaciones de dequantización eficiente en GPU; en NVIDIA funciona desde Pascal (GTX 1080) hacia adelante; no soporta AMD ROCm de forma nativa en todas las librerías

## Para recordar

GPTQ es la opción preferida para despliegue de inferencia de alta velocidad en GPU NVIDIA cuando se dispone de tiempo de calibración y se busca el máximo throughput con memoria VRAM limitada.
