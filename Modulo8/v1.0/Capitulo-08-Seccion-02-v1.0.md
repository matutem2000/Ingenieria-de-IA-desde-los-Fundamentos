# Módulo 8 – Capítulo 08 – Sección 02

## Especulative decoding: acelerar la generación usando un modelo draft pequeño

La limitación física del decode —que cada token de salida requiere leer todos los pesos del modelo desde VRAM— parece insuperable. Si la física del ancho de banda establece un techo de 140 tokens/s para una request con un modelo de 7B en BF16 en una A100, la única forma de superarlo sería tener una GPU con mayor ancho de banda de VRAM o comprimir más el modelo. Speculative decoding viola esta aparente restricción con un insight algorítmico elegante: en lugar de generar tokens de a uno con el modelo objetivo, genera múltiples tokens candidatos con un modelo draft más pequeño y rápido, y los verifica todos en un único forward pass paralelo del modelo objetivo.

El mecanismo funciona en dos fases en cada iteración. Primero, un modelo draft pequeño (típicamente 1B-3B parámetros, 10-20x más rápido que el modelo objetivo) genera K tokens candidatos en K steps secuenciales de decode —la misma operación que haría el modelo objetivo, pero mucho más rápida por el menor número de parámetros a leer. Segundo, el modelo objetivo evalúa los K tokens candidatos en un **único forward pass paralelo**: en lugar de un único token de entrada como en el decode estándar, el modelo objetivo recibe los K tokens candidatos del draft y calcula simultáneamente la distribución de probabilidad que hubiera producido para cada uno. Si la distribución del modelo objetivo en la posición k es suficientemente similar a la del draft (controlado por un umbral de aceptación), el token se acepta; en el primer rechazo, el modelo objetivo genera el token correcto para esa posición y la secuencia de aceptación termina.

La propiedad matemática crucial es que el proceso de aceptación/rechazo garantiza que la distribución de tokens generados es **idéntica** a la que habría producido el modelo objetivo sin draft. No es una aproximación: si el draft propone el token A y el modelo objetivo hubiera generado con alta probabilidad exactamente ese token A, se acepta; si el draft propone B pero el modelo objetivo asigna alta probabilidad a C, se rechaza B y se genera C. El resultado final es una secuencia de tokens con la misma distribución probabilística que el modelo objetivo sin draft, pero generada más rápidamente cuando el draft predice correctamente.

La **tasa de aceptación del draft** es la métrica clave que determina la aceleración real: si el draft predice correctamente el 80% de los tokens (tasa de aceptación α = 0.8) con K=5 tokens candidatos, el número esperado de tokens aceptados por iteración es `K × α / (1 - αᴷ)` ≈ 3.4, obtenidos al costo de un único forward pass del modelo objetivo en lugar de 3.4 pasos de decode individuales. La aceleración efectiva es aproximadamente 2.5-3x en dominios donde el texto es predecible (conversación, código en lenguajes populares). En dominios de alta entropía (texto creativo, generación de datos diversos), la tasa de aceptación puede caer al 50-60%, reduciendo la aceleración a 1.5-2x.

La implementación en vLLM es directa: `vllm serve meta-llama/Llama-3.1-8B-Instruct --speculative-model meta-llama/Llama-3.2-1B-Instruct --num-speculative-tokens 5` activa speculative decoding con Llama 3.2 1B como draft para Llama 3.1 8B. La compatibilidad de vocabulario (mismo tokenizador) es un requisito estricto: modelos de la misma familia con el mismo tokenizador son siempre compatibles como pares objetivo/draft.

## Implementaciones y variantes del speculative decoding

- **Draft model selection:** el modelo draft debe ser de la misma familia que el objetivo para máxima tasa de aceptación; mismo tokenizador es requisito estricto; Llama 3.2 1B como draft para Llama 3.1 8B.
- **Medusa (self-speculation):** cabezas adicionales de predicción en el modelo objetivo para K+1, K+2... tokens en paralelo; sin segundo modelo; aceleración 1.5-2.5x; entrenamiento adicional requerido para las cabezas.
- **Eagle:** utiliza features del último token del modelo objetivo como input del draft; tasas de aceptación superiores a Medusa (0.85-0.95); aceleración 2-3.5x; disponible en vLLM con `--speculative-model Eagle-LLaMA3-Instruct-8B`.
- **Configuración en vLLM:** `--speculative-model <draft> --num-speculative-tokens 5`; `--speculative-draft-tensor-parallel-size 1` para draft con menos GPUs que el objetivo en configuraciones multi-GPU.
- **Cuándo NO usar speculative decoding:** batch size alto (>16 requests simultáneas); workloads con alta entropía de texto; cuando el overhead del modelo draft supera el ahorro en steps del modelo objetivo.

> **Nota del Arquitecto:** Speculative decoding beneficia más a los escenarios de baja concurrencia (1-4 requests simultáneas) donde el decode es claramente el cuello de botella y la GPU está subutilizada. Con batches grandes, la GPU ya está compute-bound en el decode del modelo objetivo, y el overhead del modelo draft reduce el throughput agregado en lugar de mejorarlo. Mide siempre el impacto en TTFT-P95 y TBT-P95 con tráfico representativo antes de activar speculative decoding en producción.

Speculative decoding es la técnica más efectiva para reducir la latencia percibida por usuarios individuales en escenarios de baja concurrencia. La sección siguiente presenta Flash Attention, la optimización que reduce la latencia de prefill y el uso de memoria para contextos largos.

---
