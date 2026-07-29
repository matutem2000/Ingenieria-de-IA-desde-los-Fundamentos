# Módulo 8 – Capítulo 08 – Sección 01

# Anatomía de la latencia: prefill, decode y transferencia de datos

La latencia total de una petición de inferencia a un LLM se compone de tres fases secuenciales con perfiles de optimización completamente distintos: la fase de prefill (procesamiento del prompt de entrada), la fase de decode (generación autoregressiva de tokens de salida) y la latencia de red (serialización de la petición y transmisión de la respuesta), siendo cada una dominante en distintos escenarios y optimizable con técnicas diferentes. El prefill procesa todos los tokens del prompt en paralelo en un único forward pass utilizando la arquitectura causal de atención enmascarada; es computacionalmente intensivo pero rápido por token (una GPU puede prefill de 10.000 tokens en 500-1000ms), y su costo escala linealmente con el número de tokens del prompt. El decode genera un token a la vez en N forward passes secuenciales (uno por token de salida) utilizando el KV cache acumulado de los pasos anteriores; es memory-bandwidth-bound (no compute-bound), lo que significa que la velocidad de decode está limitada por la velocidad con que la GPU puede leer los pesos del modelo desde VRAM, no por su capacidad de cómputo. La transferencia de datos incluye la serialización del request JSON, la latencia de red hasta el servidor de inferencia y la deserialización de la respuesta, componente frecuentemente ignorado en benchmarks locales pero que puede dominar la latencia percibida en despliegues con streaming vía WebSocket o SSE a través de Internet.

## Desglose técnico de la latencia de inferencia

- Prefill (Time to prefill): crece O(n²) con la longitud del contexto por la naturaleza cuadrática de la atención; Flash Attention 2/3 reduce la constante a través de IO-aware tiling pero no cambia la complejidad asintótica; modelos con atención de ventana deslizante (Mistral SWA) reducen el prefill de contextos largos a O(n)
- Decode memory-bound: el cuello de botella del decode es el ancho de banda de VRAM: en cada paso, la GPU debe leer W pesos (donde W es el tamaño del modelo) para generar un token; una A100 con 2 TB/s de ancho de banda lee los 14 GB de un modelo 7B BF16 en ~7ms, limitando el decode a ~140 tokens/s por request en solitario
- KV cache growth: el KV cache crece en cada paso de decode (un bloque por token generado por capa); con contextos muy largos, la fase de decode se hace progresivamente más lenta porque el acceso al KV cache creciente consume más ancho de banda de VRAM
- Latencia de red y streaming: el patrón de streaming (SSE o WebSocket) envía cada token generado al cliente inmediatamente, eliminando la latencia de espera de la respuesta completa; la latencia de red por token en SSE es típicamente 1-5ms en redes de baja latencia, negligible respecto al tiempo de decode
- Chunked prefill: vLLM con `--enable-chunked-prefill` divide prompts largos en chunks de N tokens que se procesan intercalados con pasos de decode, evitando que un prefill largo bloquee completamente el decode de otras requests y reduciendo la variación del TTFT

## Para recordar

Optimizar la latencia de prefill y la latencia de decode requieren técnicas distintas: Flash Attention y chunked prefill para prefill; especulative decoding, batching óptimo y GPUs con mayor ancho de banda de VRAM para decode.
