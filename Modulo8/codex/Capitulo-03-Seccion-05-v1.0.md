# Módulo 8 – Capítulo 03 – Sección 05

# Limitaciones del despliegue local: concurrencia, latencia y gestión de memoria

El despliegue local con Ollama o llama.cpp tiene limitaciones estructurales que lo diferencian fundamentalmente de un servicio de inferencia escalable en la nube: la concurrencia está restringida por la memoria disponible, la latencia base es mayor que en GPUs de datacenter, y la gestión de múltiples peticiones simultáneas requiere configuración explícita en lugar del escalado automático. Ollama por defecto carga un único modelo en memoria y procesa peticiones de forma secuencial (cola FIFO): si dos usuarios envían peticiones simultáneas al mismo tiempo, la segunda petición espera a que termine la primera, produciendo latencias de respuesta que escalan linealmente con el número de peticiones concurrentes. La variable de entorno `OLLAMA_NUM_PARALLEL` permite configurar hasta 4 peticiones en paralelo en un mismo modelo, pero cada slot paralelo requiere su propio KV cache, multiplicando el uso de memoria en un factor equivalente al número de slots; con `OLLAMA_MAX_LOADED_MODELS` mayor a 1, Ollama puede mantener múltiples modelos en memoria simultáneamente, pero esto requiere disponer de memoria suficiente para todos ellos. La latencia del primer token (TTFT) en hardware local es típicamente mayor que en APIs de producción: un modelo de 7B en una RTX 3090 produce el primer token en 200-500ms vs los 50-150ms de servicios dedicados con GPUs A100/H100 en batch processing.

## Limitaciones técnicas del despliegue local

- Concurrencia limitada: sin `OLLAMA_NUM_PARALLEL`, Ollama procesa una petición a la vez por modelo; incluso con paralelismo habilitado, el máximo práctico es 4-8 peticiones simultáneas antes de que el uso de memoria del KV cache sea prohibitivo
- Sin autoscaling horizontal: Ollama no tiene capacidad nativa de distribuir carga entre múltiples instancias; escalar horizontalmente requiere un proxy externo (HAProxy, nginx, Traefik) con sesión sticky o round-robin sobre múltiples instancias de Ollama
- Latencia de carga inicial: si el modelo no está en memoria (arranque en frío), llama.cpp debe leer el archivo GGUF desde disco y cargarlo en RAM/VRAM, proceso que puede tardar 5-30 segundos para modelos de 7B-70B dependiendo de la velocidad del almacenamiento
- Interferencia de memoria: en sistemas con GPU compartida entre inferencia y otras tareas (renderizado, gaming, otras aplicaciones), los spikes de uso de VRAM de otras aplicaciones pueden provocar OOM errors en el proceso de llama.cpp con consecuente caída del servicio
- Ausencia de SLA: los despliegues locales con Ollama no tienen garantías de disponibilidad, monitoreo integrado ni capacidades de recuperación automática ante fallos; cualquier implementación de producción requiere un wrapper con health checks, reintentos y alertas

## Para recordar

Ollama es excelente para desarrollo y uso individual, pero para servir a múltiples usuarios concurrentes se necesita un motor de serving como vLLM o una arquitectura con múltiples instancias de Ollama detrás de un balanceador de carga.
