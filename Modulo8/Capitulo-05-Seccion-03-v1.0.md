# Módulo 8 – Capítulo 05 – Sección 03

# NVIDIA Triton Inference Server: serving de múltiples modelos y formatos

NVIDIA Triton Inference Server es una plataforma de serving de modelos de producción empresarial que soporta múltiples frameworks de ML (TensorFlow, PyTorch, ONNX Runtime, TensorRT, FIL para modelos de árbol) en un único servidor, permitiendo exponer decenas de modelos distintos a través de una API gRPC y REST unificada con gestión dinámica de batching, concurrencia y recursos de GPU. A diferencia de vLLM que está especializado en LLMs autoregresivos, Triton es un serving framework generalista que puede servir simultáneamente un modelo de embeddings ONNX, un clasificador de imágenes TensorRT y un LLM via el backend TensorRT-LLM, con aislamiento de recursos configurado por modelo. El modelo repository de Triton sigue una estructura de directorio estricta: `<repo>/nombre_modelo/1/model.plan` (TensorRT), `<repo>/nombre_modelo/1/model.onnx` (ONNX) o `<repo>/nombre_modelo/config.pbtxt` con la configuración de batching, número de instancias y uso de GPU. El protocolo de Triton soporta autoscaling de instancias por modelo: `instance_group { kind: KIND_GPU count: 2 gpus: [0, 1] }` en el `config.pbtxt` levanta dos instancias del mismo modelo en GPUs distintas, distribuyendo las peticiones automáticamente con round-robin balancing.

## Componentes de Triton Inference Server

- Model repository: directorio estructurado donde cada subdirectorio es un modelo con versiones numeradas; Triton monitorea cambios en el repositorio y carga/descarga modelos automáticamente sin reiniciar el servidor
- Dynamic batching: agrupa requests individuales en batches automáticamente dentro de una ventana de tiempo configurable (`max_queue_delay_microseconds`); reduce el overhead por request y maximiza el uso de GPU para modelos no-autoregresivos
- Model ensembles: permite definir pipelines de modelos en `config.pbtxt` donde la salida de un modelo alimenta la entrada de otro; útil para pipelines de preprocessing + embedding + reranking servidos como una única llamada API
- Backend TensorRT-LLM: integra TRT-LLM como backend especializado para LLMs; combina las optimizaciones de TensorRT (fusión de kernels, precisión mixta) con las capacidades de batching de Triton; el más eficiente en términos de latencia en GPUs NVIDIA para producción
- Métricas y trazas: expone métricas Prometheus en `/metrics` con latencia por modelo, throughput y uso de GPU; soporte para OpenTelemetry tracing con `--trace-config triton,rate=100` para muestreo de trazas de peticiones

## Para recordar

Triton es la opción correcta cuando se necesita servir múltiples tipos de modelos (LLMs, embeddings, clasificadores, rerankers) desde una única infraestructura de GPU con gestión centralizada de recursos y batching automático.
