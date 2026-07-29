# Módulo 8 – Capítulo 07 – Sección 04

# Autoscaling de inferencia: escalar a cero y respuesta a demanda variable

El autoscaling de inferencia de LLMs presenta un desafío único respecto al autoscaling de servicios web tradicionales: el tiempo de cold start (cargar un modelo de 7B en GPU tarda 30-120 segundos, un modelo de 70B puede tardar 5-10 minutos) hace que las estrategias de scale-to-zero agresivas sean inaceptables para aplicaciones interactivas, requiriendo compromisos entre costo de instancias en idle y latencia de arranque. En Kubernetes, el Horizontal Pod Autoscaler (HPA) puede escalar réplicas de pods de inferencia basándose en métricas personalizadas de vLLM expuestas via Prometheus (requests en cola, GPU utilization, tiempo medio en cola) mediante el Custom Metrics API; el VPA (Vertical Pod Autoscaler) no es aplicable a GPUs donde el tamaño del recurso determina el modelo que puede cargarse. Las plataformas managed de serving como AWS SageMaker Async Inference, Google Cloud Vertex AI Endpoints y las GPU serverless de Modal, Replicate y BentoCloud implementan scale-to-zero con cold start caching: los pesos del modelo se almacenan en almacenamiento de alta velocidad (NVMe local o S3 con 10 Gbps) y se cargan al inicio de la instancia, reduciendo el cold start de minutos a 30-60 segundos para modelos de 7B. El patrón de warm pool (mantener N instancias siempre activas sin carga) es la solución práctica para aplicaciones con SLA estrictos: cubre los picos de demanda con scale-out horizontal mientras asegura que las requests en períodos de baja actividad tienen siempre una instancia disponible.

## Estrategias de autoscaling para inferencia de LLMs

- Metrics-based HPA: usar `vllm:num_requests_waiting` (requests en cola) como trigger primario de escala; si la métrica supera un umbral (e.g., 5 requests en cola por más de 30 segundos), añadir una réplica; escala hacia abajo cuando la cola es cero por N minutos consecutivos
- Predictive scaling: usar datos históricos de tráfico para predecir picos y pre-calentar instancias antes de que ocurran; AWS Application Auto Scaling y Karpenter soportan scheduled scaling; especialmente útil para patrones diarios o semanales de tráfico predecibles
- Scale-to-zero con pre-warming: plataformas como Modal.com permiten configurar `min_instances=0` con un pool de instancias pre-inicializadas con el modelo en RAM pero sin GPU asignada; la asignación de GPU al recibir una petición es más rápida que el cold start completo
- KEDA (Kubernetes Event Driven Autoscaler): extiende HPA con más de 60 scalers incluyendo métricas de Prometheus, longitud de colas SQS/RabbitMQ/Kafka; permite escalar deployments de inferencia basándose en la profundidad de una cola de trabajo, ideal para procesamiento async de LLMs
- Multi-modelo en una GPU: vLLM con `--enable-lora` puede servir múltiples adaptadores LoRA sobre el mismo modelo base sin recargar los pesos base entre switches; esto permite alta densidad de modelos por GPU con autoscaling por adaptador independientemente

## Para recordar

El autoscaling de inferencia de LLMs siempre es un compromiso entre costo (instancias idle) y latencia (cold start): define primero el SLO de latencia de cold start aceptable para tu aplicación y eso determinará el tamaño mínimo del warm pool que debes mantener.
