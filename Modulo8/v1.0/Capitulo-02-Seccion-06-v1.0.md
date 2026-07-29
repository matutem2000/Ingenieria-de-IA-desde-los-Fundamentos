# Módulo 8 – Capítulo 02 – Sección 06

## Cierre: la cuantización es la técnica que hace posible ejecutar LLM en hardware accesible

La cuantización ha transformado radicalmente el panorama del despliegue de LLMs en los últimos tres años. Lo que en 2022 requería un clúster de GPUs A100 para ser viable puede ejecutarse en 2025 en una laptop con 16 GB de RAM o en una GPU de consumo de 8 GB de VRAM con calidad apenas degradada para la mayoría de las tareas de producción. Esta democratización no es el resultado de mejoras incrementales en hardware sino de avances algorítmicos en representación numérica: GPTQ, AWQ y los K-quants de GGUF han madurado al punto donde la degradación de calidad en 4 bits es frecuentemente indetectable por usuarios finales en tareas conversacionales y de extracción de información.

Las tres técnicas de cuantización presentadas en este capítulo cubren diferentes necesidades operativas con el mismo objetivo. GPTQ optimiza el throughput en GPU NVIDIA con un proceso de calibración que tarda horas pero produce los modelos más eficientes para inferencia en hardware NVIDIA; es la elección para producción de alta demanda donde la velocidad por token es el KPI principal. AWQ prioriza la calidad sobre la velocidad de cuantización, identificando los canales más críticos del modelo y protegiéndolos con mayor precisión; su proceso tarda minutos y produce modelos con menor degradación que GPTQ, especialmente en modelos pequeños de 1B-7B. Las K-quants de GGUF equilibran ambas dimensiones dentro del ecosistema de llama.cpp: compatibles con CPU, GPU y Apple Silicon sin cambios en el archivo del modelo, con variantes que permiten ajustar el trade-off precisión/tamaño entre Q2_K y Q8_0 según los requisitos del hardware de despliegue.

El proceso de selección de cuantización ha llegado a ser parte del ciclo de vida estándar del modelo en organizaciones maduras. Un mismo modelo base —por ejemplo, Llama 3.1 8B— puede existir simultáneamente en Q4_K_M para despliegue en laptops de desarrolladores, en AWQ-4bit para el servidor de inferencia de producción con GPU A10G, y en BF16 completo para los runs de fine-tuning con QLoRA. Cada variante sirve un propósito distinto dentro del mismo ecosistema del producto, y la habilidad de gestionar estas variantes como artefactos de primera clase en el registry de modelos —con sus propias métricas de calidad evaluadas en el golden dataset— es una competencia diferenciadora del AI Engineer moderno.

La cuantización también es el prerrequisito del fine-tuning eficiente que se verá en el Capítulo 6: QLoRA carga el modelo base en NF4 (4-bit NormalFloat) durante el entrenamiento para reducir el footprint de memoria a la mitad respecto a BF16, permitiendo fine-tuning de modelos de 70B en una sola GPU A100 de 40 GB. El NF4 de QLoRA es una variante de cuantización diseñada específicamente para los valores de los pesos de redes neuronales, y su comprensión técnica requiere los conceptos de cuantización por grupos y de tipos de datos especializados introducidos en este capítulo.

## Idea central

La cuantización no es una solución de compromiso sino una decisión de ingeniería de sistemas: el modelo cuantizado correcto en el hardware correcto supera en latencia y costo total de propiedad a un modelo sin cuantizar en hardware más caro.

---

*"Quantization is not about losing quality — it's about finding the right precision for the right operation."* — Tim Dettmers, investigador de cuantización de redes neuronales y autor de bitsandbytes y QLoRA, sobre el principio fundamental que guía las técnicas modernas de compresión de modelos.
