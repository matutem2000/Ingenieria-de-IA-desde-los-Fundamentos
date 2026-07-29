# Módulo 8 – Capítulo 02 – Sección 05

## Comparación: Q4_K_M vs Q5_K_M vs Q8_0 — trade-offs de precisión y velocidad

Seleccionar la variante de cuantización correcta para un despliegue concreto no es una decisión estética sino un análisis de ingeniería: el modelo cuantizado demasiado agresivamente puede fallar en la tarea objetivo del producto, mientras que el cuantizado insuficientemente ocupa más memoria de la necesaria y limita las opciones de hardware viables. Las variantes K-quant del formato GGUF —Q4_K_M, Q5_K_M, Q6_K y Q8_0— representan cuatro puntos bien definidos en este espacio de trade-offs, cada uno con un perfil de tamaño, velocidad y calidad documentado empíricamente.

La nomenclatura K-quant codifica la estrategia de cuantización: el número indica los bits base, la letra K señala que se aplica cuantización adaptativa con factores de escala por grupos, y la letra final (S, M, L) indica el tamaño de esos grupos. Q4_K_M usa 4 bits para la mayoría de los pesos pero eleva a 6 bits las capas más sensibles del modelo (las primeras y últimas capas, más las cabezas de atención críticas), lo que explica por qué logra 4.65 bits efectivos por parámetro en lugar de exactamente 4. Para un modelo de 7B parámetros, esto produce un archivo de aproximadamente 4.1 GB que se genera entre 10 y 20 tokens por segundo en CPU moderna, con una degradación de perplexity de 0.15-0.25 puntos respecto al modelo en BF16. Esta combinación hace de Q4_K_M el punto de inicio recomendado para la mayoría de los despliegues en hardware de consumo.

Q5_K_M incrementa los bits efectivos a 5.68 por parámetro, resultando en un archivo de aproximadamente 5.0 GB para el mismo modelo de 7B. La mejora de calidad respecto a Q4_K_M es consistente pero moderada: la degradación de perplexity cae a 0.05-0.10 puntos, una mejora que en evaluaciones de usuario humano frecuentemente solo se percibe en tareas con alta densidad de razonamiento o en generación de código con lógica compleja. Para equipos con hardware de 8-10 GB de VRAM o RAM y que reportan degradación visible con Q4_K_M en su tarea específica, Q5_K_M es el siguiente paso natural antes de considerar hardware adicional.

Q6_K alcanza 6.56 bits efectivos y degradación de perplexity inferior a 0.05 puntos: en evaluaciones ciegas por usuarios humanos en tareas conversacionales y de extracción de información, esta diferencia respecto al modelo FP16 original es prácticamente indetectable. Q6_K ocupa 5.9 GB para un modelo de 7B y es la elección correcta para tareas donde la precisión es crítica —generación de código en dominios especializados, síntesis de documentos médicos, razonamiento matemático— sin necesidad de incrementar el hardware al completo modelo en BF16.

Q8_0 es cuantización de 8 bits sin agrupamiento, produciendo archivos de 7.2 GB con pérdida de perplexity inferior a 0.01 puntos: es prácticamente indistinguible del modelo original en cualquier benchmark. Su desventaja frente a las K-quants es que no aprovecha la aceleración INT4 de los Tensor Cores NVIDIA y ocupa significativamente más memoria sin la mejora de calidad que justificaría ese tamaño adicional. Q8_0 tiene sentido principalmente para uso en CPU cuando se quiere la máxima calidad posible sin modificar el hardware y la velocidad de generación es secundaria.

## Trade-offs de precisión y velocidad

- **Q4_K_M (recomendado para uso general):** 4.65 bits efectivos, ~4.1 GB para 7B, pérdida de perplexity de 0.15-0.25 puntos; mejor relación calidad/tamaño; para hardware con 6-8 GB de RAM/VRAM.
- **Q5_K_M (calidad prioritaria):** 5.68 bits efectivos, ~5.0 GB para 7B, pérdida de 0.05-0.10 puntos; cuando la calidad importa más que el tamaño y se dispone de 8-10 GB.
- **Q6_K (casi sin pérdida):** 6.56 bits efectivos, ~5.9 GB para 7B, pérdida inferior a 0.05 puntos; para tareas críticas como código especializado o razonamiento médico.
- **Q8_0 (cuantización mínima):** 8 bits, ~7.2 GB para 7B, pérdida inferior a 0.01 puntos; máxima calidad en CPU cuando el tamaño no es restricción.
- **Velocidad en CPU vs GPU:** Q4_K_M es hasta un 30% más rápido que Q8_0 en CPU por menor ancho de banda de memoria necesario; en GPU con aceleración INT4, Q4_K_M puede ser 2x más rápido en throughput de tokens.

> **Nota del Arquitecto:** El proceso correcto de selección de variante es empírico, no teórico: descarga el modelo en Q4_K_M, ejecútalo en tu golden dataset del Capítulo 1, y mide si la calidad cumple el umbral del producto. Si no cumple, sube a Q5_K_M y repite. En más del 80% de los proyectos de producción que he visto, Q4_K_M supera el umbral de calidad y permite usar hardware significativamente más económico que el requerido por Q8_0 o BF16.

La elección de variante de cuantización completa el perfil técnico del modelo seleccionado: combinando familia, tamaño y variante K-quant, el AI Engineer puede calcular exactamente los requisitos de hardware para el despliegue. El siguiente capítulo cubre las herramientas que ejecutan estos modelos GGUF en la práctica, comenzando con llama.cpp y Ollama.

---
