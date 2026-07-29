# Módulo 8 – Capítulo 07 – Sección 03

# Contenedores para inferencia: Docker, NVIDIA Container Toolkit y Kubernetes

El despliegue containerizado de LLMs en GPU requiere una cadena específica de tecnologías que va más allá del Docker estándar: el NVIDIA Container Toolkit (anteriormente nvidia-docker) expone los drivers CUDA del host dentro del contenedor sin incluir los drivers en la imagen, permitiendo que los contenedores accedan a las GPUs del host mientras la imagen permanece portable y ligera. La imagen base estándar para contenedores de inferencia de LLMs es `nvcr.io/nvidia/cuda:12.4-cudnn9-devel-ubuntu22.04` o la variante `runtime` para producción (sin las herramientas de compilación de la variante `devel`), sobre la cual se instalan las librerías de Python (vLLM, transformers, etc.) y los modelos se montan como volúmenes o se descargan al inicio del contenedor. El acceso a GPU en Docker se habilita con `docker run --gpus all` (para todas las GPUs) o `--gpus device=0,1` (para GPUs específicas); en Kubernetes, el NVIDIA Device Plugin for Kubernetes expone los recursos de GPU como `nvidia.com/gpu: 1` en los `requests` y `limits` del pod spec. Las imágenes de contenedor de LLMs son frecuentemente grandes (5-15 GB sin los pesos del modelo); optimizar el tamaño con multi-stage builds, usar imágenes base slim y separar el entorno de los pesos del modelo (montados en tiempo de ejecución desde un PVC o descargados desde Hugging Face Hub) reduce los tiempos de deploy y los costos de almacenamiento de registry.

## Configuración de contenedores para inferencia de LLMs

- NVIDIA Container Toolkit: instalación en el host con `apt install nvidia-container-toolkit`; configuración de Docker para usar el runtime NVIDIA por defecto con `nvidia-ctk runtime configure --runtime=docker && systemctl restart docker`; verifica con `docker run --rm --gpus all nvidia/cuda:12.0-base nvidia-smi`
- Dockerfile para vLLM: imagen base `vllm/vllm-openai:latest` incluye vLLM preinstalado y listo para usar; `ENTRYPOINT ["python", "-m", "vllm.entrypoints.openai.api_server"]` con variables de entorno para MODEL_NAME, TENSOR_PARALLEL_SIZE y GPU_MEMORY_UTILIZATION
- Kubernetes GPU scheduling: el NVIDIA Device Plugin declara recursos `nvidia.com/gpu` por nodo; `nodeSelector: nvidia.com/gpu.product: A100-SXM4-80GB` permite scheduling en GPUs específicas; `runtimeClassName: nvidia` es necesario en algunas distribuciones para activar el runtime NVIDIA
- Almacenamiento de pesos: los modelos de Hugging Face se cachean en `~/.cache/huggingface` por defecto; en Kubernetes, montar un PersistentVolume en `/root/.cache/huggingface` compartido entre pods evita descargar el mismo modelo múltiples veces; usar volúmenes ReadWriteMany con NFS o un DaemonSet de precarga en producción
- Health checks: `livenessProbe` y `readinessProbe` en el pod spec apuntando al endpoint `/health` de vLLM; configurar `initialDelaySeconds: 120` (o mayor para modelos grandes) para dar tiempo al proceso de cargar el modelo antes de comenzar a recibir tráfico

## Para recordar

La containerización de LLMs en GPU es más compleja que la de servicios web estándar: el NVIDIA Container Toolkit, el tamaño de las imágenes y la gestión del almacenamiento de pesos son los tres aspectos críticos que requieren diseño explícito antes de primer despliegue.
