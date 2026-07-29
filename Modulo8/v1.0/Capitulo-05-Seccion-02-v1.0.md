# Módulo 8 – Capítulo 05 – Sección 02

## OpenAI-compatible API con vLLM: despliegue listo para producción

El servidor HTTP integrado de vLLM convierte el motor de inferencia en un servicio de producción con una sola línea de comando. El comando de inicio básico es `vllm serve meta-llama/Llama-3.1-8B-Instruct --host 0.0.0.0 --port 8000`, que descarga el modelo desde Hugging Face Hub si no está en caché local, lo carga en GPU usando PagedAttention, y levanta un servidor HTTP que expone los endpoints `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings` y `/v1/models` con el mismo contrato de request/response que la API oficial de OpenAI.

El parámetro `--gpu-memory-utilization` es la palanca principal de configuración del pool de KV cache: con `--gpu-memory-utilization 0.90`, vLLM reserva el 90% de la VRAM disponible para el KV cache pool, dejando el 10% restante para el overhead del framework y los buffers de activación. Este valor debe calibrarse según el patrón de uso: incrementarlo aumenta el throughput de requests concurrentes (más bloques disponibles en el pool) pero puede causar OOM errors si hay peticiones con contextos excepcionalmente largos; reducirlo da más margen de seguridad pero desperdicia VRAM disponible. Para producción, comenzar con `0.85` y ajustar basándose en las métricas de `vllm:gpu_cache_usage_perc` expuestas en el endpoint `/metrics`.

La configuración de `--max-model-len` determina el contexto máximo que el servidor puede aceptar: requests con más tokens que este valor son rechazadas con un error HTTP 400 antes de intentar procesarlas, evitando el OOM que resultaría de intentar asignar bloques de KV cache para un contexto que no cabe en el pool. Para modelos con ventanas de contexto largas (Llama 3.1 con 128K tokens), es importante limitar este valor al contexto máximo real que el producto necesita: un `--max-model-len 8192` es suficiente para la mayoría de las aplicaciones conversacionales y reduce significativamente el pool de KV cache necesario frente a 128K.

La cuantización de modelos pre-cuantizados es compatible con vLLM mediante flags específicos: `--quantization awq` para modelos en formato AWQ, `--quantization gptq` para modelos GPTQ, y `--quantization fp8` para modelos en FP8 nativo en GPUs H100. Para cuantización dinámica sin modelo pre-cuantizado, `--quantization bitsandbytes` aplica INT8 en tiempo de carga, aunque con menor eficiencia que los modelos pre-cuantizados. Los structured outputs, esenciales para aplicaciones que requieren respuestas en JSON con schemas específicos, se habilitan con `--guided-decoding-backend xgrammar`: este parámetro activa la generación guiada por gramática que garantiza que la respuesta del modelo sea siempre JSON válido según el schema especificado en el campo `response_format` de la petición.

Para producción de alta disponibilidad, vLLM se despliega en Kubernetes como un Deployment con `replicas: N`, cada pod con resources `limits: nvidia.com/gpu: 1` (o más para multi-GPU), y un Service de tipo ClusterIP o LoadBalancer. Los endpoints `/health` y `/v1/models` sirven como liveness y readiness probes: vLLM solo responde con HTTP 200 en el endpoint `/health` cuando el modelo está completamente cargado y el servidor está listo para procesar peticiones, evitando que el balanceador de carga envíe tráfico a pods en proceso de inicio de carga del modelo.

## Configuración de producción de vLLM

- **Parámetros críticos de memoria:** `--max-model-len` limita el contexto máximo por request; `--gpu-memory-utilization` determina el porcentaje de VRAM para el KV cache pool; `--max-num-seqs` limita las requests concurrentes máximas.
- **Cuantización en vLLM:** `--quantization awq/gptq` para modelos pre-cuantizados; `--quantization fp8` en H100; `--quantization bitsandbytes` para cuantización dinámica INT8.
- **Structured outputs:** `--guided-decoding-backend xgrammar` habilita JSON Schema-guided generation; compatible con el parámetro `response_format` del SDK de OpenAI.
- **Health checks:** `/health` devuelve HTTP 200 solo cuando el modelo está completamente cargado; `/v1/models` lista los modelos disponibles; ambos útiles como Kubernetes probes.
- **Métricas Prometheus:** `/metrics` expone `vllm:num_requests_running`, `vllm:gpu_cache_usage_perc`, `vllm:time_to_first_token_seconds` y `vllm:request_success_total` para dashboards y alertas.

> **Nota del Arquitecto:** La configuración más crítica para evitar problemas en producción es `--max-model-len`. Usarla con el valor máximo soportado por el modelo (128K para Llama 3.1) parece tentador pero desperdicia VRAM en un pool de KV cache que nunca se llenará si los usuarios del producto rara vez usan más de 8K tokens. Mide el percentil 99 de la longitud de contexto real de tus usuarios y usa ese número como `--max-model-len`; recuperarás VRAM que se traduce directamente en más requests concurrentes atendidas.

La configuración detallada de vLLM para producción incluye docenas de parámetros adicionales para casos especiales, pero los presentados en esta sección cubren el 90% de los escenarios de despliegue de producción. La sección siguiente presenta NVIDIA Triton Inference Server, el motor correcto para el 10% restante de casos donde se necesita servir múltiples tipos de modelos desde una única infraestructura.

---
