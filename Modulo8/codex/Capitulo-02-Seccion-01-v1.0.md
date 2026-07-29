# Módulo 8 – Capítulo 02 – Sección 01

# Por qué cuantizar: reducción de memoria y aceleración de inferencia con pérdida controlada

La cuantización es el proceso de representar los pesos de un modelo neuronal con menos bits de los utilizados durante el entrenamiento (típicamente reduciendo de FP32 o BF16 a INT8, INT4 o incluso INT2), reduciendo el footprint de memoria y acelerando las operaciones matriciales en hardware que soporta aritmética de enteros. Un modelo de 7B parámetros en BF16 requiere 14 GB de VRAM (2 bytes por parámetro); el mismo modelo en INT4 ocupa aproximadamente 3.5 GB, habilitando su ejecución en una GPU de 4 GB de VRAM o incluso en CPU con RAM suficiente. La pérdida de precisión introducida por la cuantización no es uniforme: capas de atención y las primeras/últimas capas del modelo son más sensibles, razón por la cual técnicas como GGUF K-quants y GPTQ aplican cuantización mixta usando más bits en las capas críticas y menos en las capas menos sensibles. El trade-off concreto de una cuantización Q4_K_M sobre Llama 3 8B es una reducción del 75% en uso de memoria con una degradación en perplexity de aproximadamente 0.15-0.3 puntos, considerada aceptable para la mayoría de las aplicaciones de producción.

## Aspectos técnicos de la cuantización

- Cuantización post-entrenamiento (PTQ): se aplica sobre pesos ya entrenados sin reentrenamiento; es la técnica más usada en producción por su rapidez; incluye GPTQ, AWQ y GGUF con sus variantes K-quant
- Cuantización durante el entrenamiento (QAT): simula el error de cuantización durante el fine-tuning para que el modelo aprenda a compensarlo; produce modelos más robustos pero requiere acceso al pipeline de entrenamiento completo
- Tipos de datos: FP32 (4 bytes), BF16 (2 bytes, rango dinámico amplio, preferido para entrenamiento), FP16 (2 bytes, precisión similar a FP16 pero con riesgo de overflow), INT8 (1 byte), INT4 (0.5 bytes efectivos con agrupación)
- Cuantización por grupos (group quantization): en lugar de un único factor de escala por capa, se usan factores de escala por grupos de 32 o 128 pesos, mejorando la precisión a costa de overhead de memoria adicional del 3-5%
- Aceleración en hardware: las GPUs NVIDIA con Tensor Cores aceleran operaciones INT8 e INT4 mediante instrucciones especializadas como DP4A e IMMA; Apple Silicon acele INT8 en el Neural Engine; las CPUs modernas con AVX-512 VNNI aceleran INT8

## Para recordar

La cuantización no es una degradación de calidad sino un trade-off de ingeniería: encontrar el punto de cuantización donde la pérdida de calidad en tu tarea específica es menor que el beneficio operativo de ejecutar el modelo en hardware disponible.
