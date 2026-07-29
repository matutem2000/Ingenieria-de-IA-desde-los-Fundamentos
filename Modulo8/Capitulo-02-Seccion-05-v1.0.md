# Módulo 8 – Capítulo 02 – Sección 05

# Comparación: Q4_K_M vs Q5_K_M vs Q8_0 — trade-offs de precisión y velocidad

Las variantes K-quant del formato GGUF (Q4_K_M, Q5_K_M, Q6_K, Q8_0) representan puntos distintos en el espacio de trade-offs entre tamaño del modelo, velocidad de inferencia y calidad de generación, y la selección correcta depende del hardware disponible y de los requisitos de calidad del producto. Q4_K_M cuantiza la mayoría de los pesos a 4 bits con un subconjunto de capas sensibles en 6 bits, logrando un archivo que ocupa aproximadamente 4.1 GB para un modelo de 7B con velocidades de generación en CPU de 10-20 tokens/s en hardware moderno. Q5_K_M usa 5 bits para la mayoría de los pesos y 6 bits para las capas críticas, ocupando 4.8 GB para 7B con una mejora medible de 0.1-0.2 puntos de perplexity respecto a Q4_K_M, considerado el punto óptimo para usuarios con RAM entre 6-8 GB. Q8_0 es cuantización de 8 bits sin agrupamiento, produciendo archivos de 7.2 GB para modelos de 7B con calidad prácticamente indistinguible del modelo en FP16 original, pero requiriendo más memoria que los modelos de 4-5 bits sin la aceleración INT4 que ofrecen las variantes K-quant en hardware compatible.

## Trade-offs de precisión y velocidad

- Q4_K_M (recomendado para uso general): 4.65 bits por peso efectivos, tamaño ~4.1 GB para 7B, pérdida de perplexity de 0.15-0.25 puntos respecto a FP16, mejor relación calidad/tamaño; ideal para hardware con 6-8 GB de RAM/VRAM
- Q5_K_M (para calidad prioritaria): 5.68 bits por peso efectivos, tamaño ~5.0 GB para 7B, pérdida de perplexity de 0.05-0.10 puntos; recomendado cuando la calidad importa más que el tamaño y se dispone de 8-10 GB
- Q6_K (casi sin pérdida): 6.56 bits por peso efectivos, tamaño ~5.9 GB para 7B, pérdida de perplexity inferior a 0.05 puntos; prácticamente indistinguible de FP16 en evaluación humana; útil para tareas críticas como generación de código o razonamiento médico
- Q8_0 (cuantización mínima): 8 bits por peso, tamaño ~7.2 GB para 7B, pérdida de perplexity inferior a 0.01 puntos; más rápido que FP16 en CPU por menor transferencia de datos, pero no tan optimizado como las K-quants en GPU
- Velocidad en CPU vs GPU: en CPU, Q4_K_M es hasta 30% más rápido que Q8_0 por menor ancho de banda de memoria necesario; en GPU con aceleración INT4, Q4_K_M puede ser 2x más rápido que Q8_0 en throughput de tokens

## Para recordar

Para la mayoría de las aplicaciones de producción con hardware de consumo, Q4_K_M es el punto de inicio recomendado: si la calidad en tu tarea es insuficiente, sube a Q5_K_M; si supera el presupuesto de memoria, baja a Q3_K_M con una evaluación cuidadosa de la degradación.
