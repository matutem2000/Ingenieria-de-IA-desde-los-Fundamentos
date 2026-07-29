# Módulo 8 – Capítulo 05 – Sección 02

# OpenAI-compatible API con vLLM: despliegue listo para producción

vLLM incluye un servidor HTTP integrado que expone una API completamente compatible con OpenAI, iniciado con `vllm serve <modelo> --host 0.0.0.0 --port 8000`, que habilita los endpoints `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings` y `/v1/models` con el mismo contrato de request/response que la API oficial de OpenAI, incluyendo soporte para streaming con Server-Sent Events y structured outputs con JSON schema. El comando de despliegue mínimo para producción es `vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 1 --max-model-len 8192 --gpu-memory-utilization 0.90`, donde `--gpu-memory-utilization 0.90` reserva el 90% de la VRAM disponible para el KV cache pool de vLLM, dejando el 10% restante para el sistema; incrementar este valor aumenta el throughput pero puede causar OOM errors en requests con contextos muy largos. La compatibilidad con el SDK de OpenAI es inmediata: `openai.OpenAI(base_url="http://mi-servidor:8000/v1", api_key="<token>")` permite usar vLLM como backend en cualquier aplicación existente; los tokens de autenticación se configuran con `--api-key` y soportan un único token compartido o integración con sistemas de autenticación externos vía middleware. Para producción de alta disponibilidad, vLLM se despliega típicamente como un Pod de Kubernetes con un Deployment de una o más réplicas, un Service de tipo ClusterIP y un Ingress con soporte para WebSocket (necesario para streaming).

## Configuración de producción de vLLM

- Parámetros críticos de memoria: `--max-model-len` controla el contexto máximo por request; `--gpu-memory-utilization` determina el porcentaje de VRAM destinado al KV cache pool; `--max-num-seqs` limita las requests concurrentes máximas en el batch
- Cuantización en vLLM: `--quantization awq` o `--quantization gptq` para modelos pre-cuantizados; `--quantization fp8` para modelos en FP8 nativo en H100; `--quantization bitsandbytes` para cuantización dinámica INT8 sin necesidad de un modelo pre-cuantizado
- Structured outputs: `vllm serve <modelo> --enable-prefix-caching --guided-decoding-backend xgrammar` habilita JSON Schema-guided generation; compatible con el parámetro `response_format` del SDK de OpenAI para salidas estructuradas garantizadas
- Health checks: los endpoints `/health` y `/v1/models` permiten configurar readiness y liveness probes en Kubernetes; vLLM devuelve HTTP 200 solo cuando el modelo está completamente cargado y listo para servir
- Métricas Prometheus: `--disable-log-stats=false` expone métricas en `/metrics` incluyendo `vllm:num_requests_running`, `vllm:gpu_cache_usage_perc`, `vllm:time_to_first_token_seconds` y `vllm:request_success_total`

## Para recordar

La compatibilidad drop-in de vLLM con la API de OpenAI significa que el path de migración de una API propietaria a un modelo local es técnicamente trivial; el trabajo real está en la selección del modelo, la configuración de hardware y la validación de calidad.
