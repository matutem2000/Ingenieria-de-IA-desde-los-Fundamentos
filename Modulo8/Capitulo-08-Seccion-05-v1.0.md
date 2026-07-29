# Módulo 8 – Capítulo 08 – Sección 05

# Perfilado de inferencia: identificar cuellos de botella con herramientas de profiling

El perfilado de inferencia de LLMs requiere herramientas que operen en múltiples niveles simultáneamente: nivel de GPU (utilización de Streaming Multiprocessors, uso de VRAM, ancho de banda de memoria), nivel de sistema (throughput de requests, distribución de TTFT y TBT) y nivel de aplicación (tiempo por componente: tokenización, prefill, decode, postprocesamiento), ya que el cuello de botella puede estar en cualquiera de estas capas y el diagnóstico erróneo lleva a optimizaciones ineficaces. NVIDIA Nsight Systems (`nsys profile`) y Nsight Compute (`ncu`) son las herramientas de profiling de GPU más detalladas: Nsight Systems genera una traza temporal de todas las operaciones de CUDA (kernel launches, memcpy, sincronizaciones) en un formato visual que permite identificar cuándo la GPU está idle, cuándo los kernels se solapan y cuándo hay transferencias lentas; Nsight Compute analiza el rendimiento a nivel de kernel individual mostrando el throughput de instrucciones, la tasa de ocupancia de SMs y el bound (compute-bound vs memory-bound). `nvidia-smi dmon -s puct -d 1` proporciona monitoreo en tiempo real de utilización de GPU, VRAM, temperatura y potencia a 1 Hz, suficiente para detectar problemas de utilización en producción sin overhead de profiling completo. Para benchmarking end-to-end de throughput y latencia, `vllm benchmark_throughput.py` y `vllm benchmark_latency.py` incluidos en el repositorio de vLLM proveen métricas de throughput (requests/s, tokens/s) y latencia (TTFT P50/P95/P99, TBT) con workloads sintéticos configurables.

## Herramientas de perfilado por nivel

- GPU compute: `nsys profile --trace=cuda,nvtx python -m vllm.entrypoints.openai.api_server ...` captura la traza completa de kernels CUDA; identifica si el modelo está compute-bound (SM utilization >90%) o memory-bound (SM utilization baja, alta presión sobre HBM bandwidth)
- VRAM monitoring: `torch.cuda.memory_summary()` y `torch.cuda.memory_allocated()` permiten monitorear el uso de VRAM por componente (pesos, KV cache, activaciones) durante la inferencia; útil para detectar memory leaks y calibrar el `--gpu-memory-utilization` óptimo de vLLM
- Métricas de producción: vLLM expone métricas Prometheus que permiten crear dashboards Grafana con TTFT por percentil, TBT por percentil, GPU cache utilization y queue depth; definir alertas sobre P99 TTFT y queue depth excesiva permite detección temprana de degradación
- py-spy para CPU bottlenecks: `py-spy top --pid <pid_vllm>` muestra en tiempo real qué funciones de Python consumen más CPU; útil cuando el cuello de botella no está en la GPU sino en el preprocessing/postprocessing de Python (tokenización, formateado de respuestas)
- Torch profiler integrado: `torch.profiler.profile(activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA])` dentro del código de forward pass captura el tiempo exacto por operación en CPU y GPU con resolución de microsegundos; exporta trazas compatibles con TensorBoard y perfetto.dev

## Para recordar

El perfilado de inferencia debe hacerse con workloads representativos de producción, no con requests individuales en aislamiento: muchos problemas de rendimiento (memory contention, scheduling overhead, queue dynamics) solo aparecen bajo carga concurrente real.
