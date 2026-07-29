# Módulo 8 – Capítulo 02 – Sección 01

## Por qué cuantizar: reducción de memoria y aceleración de inferencia con pérdida controlada

El modelo base seleccionado en el capítulo anterior pesa, en su forma de entrenamiento en BF16 (2 bytes por parámetro), 14 GB para un modelo de 7B parámetros. Esta cifra define el hardware mínimo requerido sin cuantización: una GPU de 16 GB de VRAM con margen suficiente para buffers de activación y el KV cache. Para la mayoría de los equipos que trabajan con modelos locales, este requisito elimina del presupuesto las GPUs de consumo más accesibles y obliga a optar por hardware de datacenter o nube para inferencia en producción. La cuantización es la técnica que rompe esta barrera: reduce la representación numérica de los pesos de 16 a 4 u 8 bits, comprimiendo el mismo modelo de 7B a 3.5-7 GB con una pérdida de calidad que, para la mayoría de las tareas de producción, es prácticamente imperceptible.

Cuantizar significa representar los pesos del modelo con menos bits que los utilizados durante el entrenamiento. El entrenamiento moderno usa BF16 (bfloat16, 16 bits, con amplio rango dinámico), pero una vez que los pesos están fijados, es posible reducirlos a INT8 (1 byte), INT4 (medio byte efectivo con agrupación) o incluso INT2, asumiendo una pérdida de precisión que impacta en el rendimiento del modelo de formas medibles pero frecuentemente tolerables. La reducción de precisión no es un daño uniforme: algunas capas son mucho más sensibles a la cuantización que otras. Las primeras y últimas capas del modelo (embedding y lm_head) y las capas de atención tienden a ser más críticas; las capas intermedias de las proyecciones FFN toleran mayor compresión. Esta observación es la base de las técnicas de cuantización mixta que aplican más bits donde el modelo es más sensible.

El trade-off cuantitativo de una cuantización Q4_K_M sobre Llama 3 8B ilustra bien la práctica: reducción del 75% en uso de memoria (de 14 GB a ~4.1 GB), velocidad de generación en CPU que puede mejorar respecto a FP16 por menor ancho de banda de memoria necesario, y una degradación de perplexity de aproximadamente 0.15-0.3 puntos en WikiText-2. La perplexity es una métrica de fluencia del modelo (cuánto "sorprenden" al modelo los tokens del texto de test): un incremento de 0.15-0.3 puntos sobre una perplexity base de 5-7 representa una degradación relativa del 2-5%, que para la mayoría de las aplicaciones conversacionales, de extracción de información o de código no es detectable por usuarios humanos.

Esta sección también establece la referencia canónica de la fórmula de memoria del modelo, que será utilizada en los capítulos de hardware (Capítulo 4) y serving (Capítulo 5):

**Fórmula de VRAM para pesos del modelo:**
```
VRAM_pesos (GB) = parámetros × bits_cuantización / 8 / 1e9
```
Ejemplos: 7B en Q4: `7e9 × 4 / 8 / 1e9 = 3.5 GB`; en Q8: `7 GB`; en BF16: `14 GB`.

A esta cifra debe sumarse el **KV cache** (que se detalla en el Capítulo 4) y un **overhead del framework** del 10-15% para buffers de activación y el runtime de CUDA o Metal. En hardware con VRAM limitada, la cuantización es la palanca que hace posible cargar el modelo; el KV cache y el overhead determinan si queda VRAM suficiente para el contexto de inferencia.

## Aspectos técnicos de la cuantización

- **Cuantización post-entrenamiento (PTQ):** se aplica sobre pesos ya entrenados sin reentrenamiento; la técnica más usada en producción; incluye GPTQ, AWQ y GGUF con variantes K-quant.
- **Cuantización durante el entrenamiento (QAT):** simula el error de cuantización durante el fine-tuning; produce modelos más robustos ante cuantización pero requiere el pipeline de entrenamiento completo.
- **Tipos de datos:** FP32 (4 bytes), BF16 (2 bytes, rango dinámico amplio, preferido para entrenamiento), FP16 (2 bytes, riesgo de overflow en rangos extremos), INT8 (1 byte), INT4 (0.5 bytes efectivos con agrupación).
- **Cuantización por grupos:** factores de escala separados por grupos de 32 o 128 pesos mejoran la precisión a costa de ~3-5% de overhead de memoria adicional.
- **Aceleración en hardware:** las GPUs NVIDIA con Tensor Cores aceleran operaciones INT8 e INT4 mediante instrucciones especializadas (DP4A, IMMA); Apple Silicon acelera INT8 en el Neural Engine; CPUs con AVX-512 VNNI aceleran INT8 nativo.

> **Nota del Arquitecto:** El proceso correcto de cuantización no es "comprimir al máximo posible" sino "encontrar el mínimo de bits que no degrada la calidad en la tarea específica del producto". Evalúa siempre Q4_K_M primero en tu golden dataset: si la calidad es suficiente, ganas el 75% de reducción de memoria. Si no es suficiente, prueba Q5_K_M. Rara vez necesitarás más de Q6_K para aplicaciones de producción que no sean matemáticas avanzadas o generación de código crítico.

La cuantización es la primera técnica de ingeniería aplicada al modelo seleccionado, y determina el hardware mínimo viable para el despliegue. Las secciones siguientes detallan los tres formatos principales de cuantización para producción: GGUF para inferencia CPU/GPU con llama.cpp, GPTQ para máximo throughput en GPU NVIDIA, y AWQ para la mejor relación calidad/compresión en modelos pequeños.

---
