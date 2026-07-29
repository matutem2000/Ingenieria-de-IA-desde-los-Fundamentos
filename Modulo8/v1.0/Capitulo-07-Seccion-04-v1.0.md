# Módulo 8 – Capítulo 07 – Sección 04

## Autoscaling de inferencia: escalar a cero y respuesta a demanda variable

El autoscaling de servicios de LLMs tiene un desafío que no existe en el autoscaling de servicios web tradicionales: el tiempo de cold start. Cuando un nuevo pod de inferencia se levanta para absorber demanda adicional, debe descargar el modelo desde el almacenamiento (o leerlo del volumen montado), cargarlo en VRAM capa por capa, inicializar el pool de KV cache de PagedAttention, y ejecutar un forward pass de warmup antes de estar listo para servir. Para un modelo de 7B cargado desde un PersistentVolume en NVMe local, este proceso toma 30-60 segundos; para modelos de 70B, puede tomar 3-8 minutos. Esta ventana de cold start limita cuán agresivamente se puede escalar a cero en sistemas con SLA de latencia estrictos.

El mecanismo de autoscaling estándar en Kubernetes para inferencia de LLMs es el **Horizontal Pod Autoscaler (HPA)** configurado con métricas personalizadas de vLLM expuestas via Prometheus. La métrica más efectiva como trigger de escalado es `vllm:num_requests_waiting`: cuando hay más de N requests esperando en la cola por más de M segundos, el HPA añade una réplica adicional. La implementación requiere el stack Prometheus + adapter de métricas personalizadas (kube-prometheus-stack + prometheus-adapter) que traduce las métricas de Prometheus en el formato que el Custom Metrics API de Kubernetes expone al HPA. Cuando la cola baja a cero por K minutos consecutivos, el HPA escala hacia abajo, pero para mantener el SLA de latencia se configura siempre un número mínimo de réplicas mayor a cero (el warm pool).

**KEDA (Kubernetes Event Driven Autoscaler)** extiende las capacidades del HPA con más de 60 scalers, incluyendo métricas de Prometheus, colas SQS, tópicos Kafka y más. KEDA es especialmente valioso para arquitecturas de inferencia asíncrona donde los requests de LLM se encolan en SQS o RabbitMQ y los workers de inferencia los consumen: KEDA puede escalar el número de pods de inferencia basándose en la profundidad de la cola SQS directamente, sin necesitar un HPA personalizado con métricas complejas de Prometheus.

Para el escenario de scale-to-zero en aplicaciones con tráfico completamente discontinuo —aplicaciones que reciben peticiones durante el horario laboral y tienen cero tráfico por la noche— las plataformas serverless resuelven el cold start con técnicas de pre-warming: Modal.com y BentoCloud permiten configurar un pool de instancias pre-inicializadas en RAM pero sin GPU asignada; cuando llega una petición, la GPU se asigna a la instancia pre-inicializada en segundos (en lugar de los minutos de un cold start completo) y el modelo ya está en RAM lista para cargarse en VRAM. Esta técnica reduce el cold start efectivo de 5-8 minutos a 30-60 segundos para modelos de 7B.

El **predictive scaling** es la optimización más sofisticada para aplicaciones con patrones de tráfico predecibles: los datos históricos de tráfico muestran picos de demanda en horarios específicos (inicio de jornada laboral, almuerzo, fin de tarde en distintas zonas horarias). AWS Application Auto Scaling con scheduled scaling, o el scheduled scaling de Karpenter, pueden pre-calentar instancias adicionales 5-10 minutos antes del pico esperado, eliminando el cold start en el momento crítico de mayor demanda.

## Estrategias de autoscaling para inferencia de LLMs

- **HPA con métricas personalizadas de vLLM:** `vllm:num_requests_waiting` como trigger primario; añadir réplica si la cola supera N requests por M segundos; requerir kube-prometheus-stack + prometheus-adapter.
- **Warm pool mínimo:** mantener siempre al menos N réplicas activas para garantizar el SLA de latencia; el tamaño del warm pool depende del cold start time aceptable según el SLO del producto.
- **KEDA para inferencia asíncrona:** escalar pods de inferencia basándose en profundidad de colas SQS/Kafka; ideal para pipelines de procesamiento batch de LLMs con tolerancia a latencia.
- **Scale-to-zero con pre-warming:** plataformas como Modal o BentoCloud permiten instancias pre-inicializadas en RAM sin GPU; la asignación de GPU al recibir una petición es más rápida que el cold start completo.
- **Multi-LoRA serving:** vLLM con `--enable-lora --max-loras 4` puede servir múltiples adaptadores LoRA sobre el mismo modelo base; permite alta densidad de modelos por GPU con autoscaling por adaptador independiente.

> **Nota del Arquitecto:** El warm pool es la decisión de costo más importante del autoscaling de LLMs. Calcular el número correcto de instancias mínimas requiere conocer: (1) el SLO de TTFT máximo aceptable, (2) el tiempo de cold start del modelo en el hardware elegido, y (3) el patrón de tráfico durante el valle nocturno. Con esos tres datos, puedes calcular cuántas instancias mantener activas durante el valle para absorber el primer pico de mañana sin cold start visible para el usuario.

El autoscaling bien configurado convierte el sistema de inferencia en una plataforma elástica que escala automáticamente con la demanda sin intervención manual. La sección siguiente presenta las estrategias de optimización de costos adicionales que complementan el autoscaling.

---
