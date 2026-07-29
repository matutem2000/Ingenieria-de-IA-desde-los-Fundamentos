# Módulo 8 – Capítulo 01 – Sección 05

# Criterios de selección: tamaño, calidad, licencia, idioma y dominio

Seleccionar un modelo open weights para producción no es una decisión única sino un proceso iterativo que pondera múltiples restricciones simultáneamente: los requisitos de hardware disponible, la calidad mínima aceptable en la tarea objetivo, las restricciones legales de la licencia y el rendimiento en el idioma e dominio del producto. El tamaño del modelo en parámetros determina directamente los requisitos de VRAM: un modelo de 7B en precisión FP16 requiere aproximadamente 14 GB de VRAM, mientras que en Q4_K_M (cuantización de 4 bits) ocupa alrededor de 4 GB, ampliando significativamente el hardware viable. La calidad en idiomas distintos al inglés varía enormemente entre familias: Qwen 2.5 y Mistral-Nemo muestran rendimiento superior en español, árabe y asiático en comparación con Llama 3 del mismo tamaño, lo que hace que el idioma sea frecuentemente el criterio eliminatorio más importante para mercados no angloparlantes. La especialización en dominio importa cuando la tarea requiere conocimiento técnico profundo: modelos como DeepSeek-Coder o CodeLlama superan a modelos generales de mayor tamaño en tareas de completado de código en Python, SQL y Bash.

## Criterios de selección técnicos

- Tamaño vs hardware: modelos de 3B-7B son viables en GPUs de consumo (8-16 GB VRAM) y en CPU con cuantización; modelos de 13B-70B requieren múltiples GPUs o hardware especializado para inferencia en tiempo real
- Rendimiento en idioma nativo: evaluar con benchmarks específicos del idioma como XNLI, mC4 perplexity o traducción inversa; no asumir que el ranking en inglés se transfiere directamente a otros idiomas
- Licencia comercial: verificar explícitamente si la licencia permite uso en el producto, distribución de outputs a usuarios finales y entrenamiento de modelos derivados sin restricciones onerosas
- Especialización en dominio: modelos base generales son mejores punto de partida para fine-tuning; modelos instruction-tuned del dominio (médico, legal, código) son mejores para zero-shot cuando no hay datos de fine-tuning disponibles
- Frecuencia de actualización: familias con releases frecuentes (Qwen, Mistral) permiten incorporar mejoras sin cambiar la arquitectura; familias con ciclos largos ofrecen más estabilidad para producción a largo plazo

## Para recordar

El criterio de selección más frecuentemente ignorado es la calidad en el idioma de producción: ejecuta siempre una evaluación en el idioma real del producto antes de comprometerte con un modelo base.
