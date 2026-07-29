# Módulo 8 – Capítulo 07 – Sección 02

# Spot vs On-demand: estrategias de costo para inferencia y entrenamiento

Las instancias Spot (AWS EC2 Spot), Preemptible (GCP) y Low-Priority (Azure) ofrecen capacidad GPU a descuentos del 60-90% sobre el precio on-demand a cambio de poder ser interrumpidas con un aviso de 2 minutos (AWS) o 30 segundos (GCP) cuando el proveedor necesita recuperar la capacidad, lo que las hace adecuadas para workloads tolerantes a interrupciones pero no para inferencia de producción con SLAs de disponibilidad. Para entrenamiento de LLMs con Spot, la estrategia clave es checkpoint frecuente: guardar el estado del optimizador, los pesos y la posición en el dataset cada 100-500 steps (dependiendo de la duración del step) permite reanudar desde el último checkpoint cuando la instancia es recuperada y reemplazada; Hugging Face `Trainer` soporta esto con `save_steps=100` y `resume_from_checkpoint=True`. El costo de entrenamiento de un modelo de 7B con LoRA durante 10.000 steps en un A100 40 GB (300W, ~0.30 kWh/hora) toma aproximadamente 2-4 horas en Spot a ~0.50-1.10 USD/hora, resultando en un costo total de 1-5 USD vs 8-15 USD en on-demand; para un ciclo de experimentación con docenas de runs de fine-tuning, esta diferencia acumula ahorros significativos. La inferencia en Spot es viable únicamente con arquitecturas que toleran reemplazos de instancias: load balancers que detectan la terminación de instancias via Instance Interruption Notices y redirigen el tráfico en 60-90 segundos, idealmente con al menos una instancia on-demand como safety net.

## Estrategias de gestión de Spot

- Interruption handling en entrenamiento: usar AWS EC2 Instance Interruption Warning (CloudWatch Events o IMDS endpoint `/latest/meta-data/spot/termination-time`) para guardar checkpoint inmediato al recibir el aviso de 2 minutos antes de la terminación
- Mixed instances (AWS): Auto Scaling Groups con `MixedInstancesPolicy` puede usar un tipo de instancia on-demand más pequeña y múltiples tipos Spot; si no hay Spot disponible, usa on-demand automáticamente; reduce el riesgo de quedarse sin capacidad en horas de alta demanda
- Spot en Kubernetes: AWS Karpenter y Cluster Autoscaler soportan spot instances con fallback a on-demand; el cordon y drain automático de nodos Spot antes de la terminación permite que los pods migren a nodos disponibles
- Estrategia de diversificación: solicitar el mismo tipo de GPU en múltiples availability zones y con múltiples tipos de instancia equivalentes (e.g., p4d.24xlarge y p4de.24xlarge) aumenta la probabilidad de obtener capacidad Spot y reduce el riesgo de interrupción simultánea
- Análisis de break-even Spot vs on-demand para inferencia: si la tasa de interrupción es del 10% mensual y cada interrupción cuesta 5 minutos de downtime, el costo esperado de downtime se suma al precio Spot; si el costo total (Spot + downtime) es menor que on-demand, Spot tiene sentido con la arquitectura correcta

## Para recordar

Spot es casi obligatorio para entrenamiento de LLMs cuando el presupuesto es limitado: la única condición es implementar checkpoint frecuente y reanudación automática, lo que convierte la mayor parte de los runs de fine-tuning en workloads tolerantes a interrupciones sin cambios en el código de entrenamiento.
