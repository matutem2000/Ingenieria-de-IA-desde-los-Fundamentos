# Módulo 10 – Capítulo 05 – Sección 03

# Performance monitoring: latencia, throughput y tasa de error en serving

El monitoreo de performance del serving de modelos combina las métricas de un sistema de software tradicional (latencia, throughput, error rate) con métricas específicas de IA que no tienen equivalente en servicios convencionales (GPU utilization, model loading time, token generation speed). Las métricas de latencia para LLMs tienen una estructura especial: Time To First Token (TTFT) mide cuándo el usuario recibe el primer token y es crítico para la percepción de responsividad, mientras que Time Per Output Token (TPOT) mide la velocidad de generación continua y determina el tiempo total de respuesta; en sistemas de producción, el SLO típico es TTFT < 500ms para el p95 y TPOT < 50ms/token para el p95. El throughput se mide en requests per second (RPS) y en tokens per second (TPS), y debe monitorearse junto con la GPU utilization para detectar si el sistema está subutilizado (GPU < 60% con latencia alta indica cuello de botella en CPU o red) o sobreexigido (GPU > 95% con latencia alta indica falta de capacidad). La tasa de error se descompone en error rate de modelo (respuestas vacías, truncadas o con errores de formato) y error rate de infraestructura (timeouts, OOM de GPU, errores de Kubernetes), y ambas deben monitorearse por separado porque tienen causas raíz y remedios distintos.

## Métricas de performance para serving de modelos

- TTFT (Time To First Token): latencia desde el envío del request hasta recibir el primer token de la respuesta; crítico para UX en aplicaciones interactivas; SLO típico p95 < 500ms
- TPOT (Time Per Output Token): milisegundos por token generado; determina la velocidad de generación; depende del tamaño del modelo, el hardware (A100 vs L4) y el batch size del servidor de inferencia
- GPU Memory Utilization: porcentaje de VRAM ocupada por el modelo, el KV cache y los batches activos; mantener < 85% para evitar OOM en picos de tráfico no anticipados
- Error rate por tipo: distinguish entre errores 4xx (bad request, context length exceeded), 5xx (timeout, OOM del servidor), y errores de calidad del modelo (respuesta vacía, hallucination detectada por safety filter)
- Queue depth: número de requests en cola esperando ser procesados; una queue creciente con latencia estable indica necesidad de más réplicas; una queue estable con latencia creciente indica degradación de throughput por batch

## Para recordar

El SLO de latencia de un LLM en producción debe definirse en términos de TTFT y TPOT separadamente, no solo en tiempo total de respuesta: un usuario tolera 30 segundos de generación si el primer token aparece en 200ms, pero no tolera 3 segundos de espera antes de ver nada.
