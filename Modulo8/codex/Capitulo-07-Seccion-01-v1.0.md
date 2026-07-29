# Módulo 8 – Capítulo 07 – Sección 01

# Proveedores de GPU en la nube: AWS, GCP, Azure, Lambda Labs, RunPod y Together AI

El mercado de GPU en la nube está segmentado entre hiperescaladores (AWS, GCP, Azure) con alta disponibilidad, SLAs empresariales y ecosistemas de servicios integrados, y proveedores especializados (Lambda Labs, RunPod, Together AI, Vast.ai) con precios significativamente menores, mayor flexibilidad y acceso a GPUs específicas que los hiperescaladores tienen en menor disponibilidad. AWS ofrece las familias p3 (V100), p4d (A100), p4de (A100 80GB) y p5 (H100) para entrenamiento, y g4dn (T4), g5 (A10G) para inferencia; los precios on-demand de una p5.48xlarge con 8 H100 superan los 98 USD/hora, mientras que las mismas GPUs en Spot pueden costar 30-40 USD/hora con riesgo de interrupción. GCP tiene las familias a2 (A100) y a3 (H100), con acceso a TPU v4/v5 para cargas de trabajo compatibles con JAX/PyTorch XLA; Azure compite con NDv2 (V100), NDm A100 v4 y ND H100 v5, frecuentemente el proveedor con mayor disponibilidad de H100 en regiones europeas para compliance. Los proveedores especializados como Lambda Labs ofrecen instancias A100 SXM de 40/80 GB desde 1.10 USD/hora (on-demand) vs los 3.97 USD/hora de AWS p4d.xlarge equivalente; RunPod y Vast.ai agregan capacidad GPU de terceros con precios variables que pueden llegar a 0.30-0.60 USD/hora para GPUs A100 en regiones con menor demanda.

## Características de los principales proveedores

- AWS: mayor ecosistema integrado (S3 para datasets, SageMaker para MLOps, EFS para almacenamiento compartido entre instancias); las instancias p4de.24xlarge ofrecen 8x A100 80GB con NVLink y 400 Gbps de red para multi-node training; Spot con EC2 Auto Scaling para entrenamiento tolerante a interrupciones
- GCP: las instancias a3-megagpu-8g con 8x H100 SXM con NVLink son las más potentes; acceso a TPU v5p para modelos grandes en JAX; integración con Vertex AI para pipelines MLOps; Spot VMs con preemptible notice de 30 segundos
- Lambda Labs: enfocado en ML con drivers NVIDIA preinstalados y entorno listos para usar; sin mínimo de compromiso; clusters multi-GPU disponibles para entrenamiento distribuido; interfaz simple pero sin el ecosistema de servicios de los hiperescaladores
- RunPod: mayor variedad de GPUs disponibles (RTX 4090, A100, H100, MI300X); modelo de marketplace donde pods son instancias de terceros; soporte para pods persistentes y serverless; precio basado en oferta/demanda, puede ser muy económico en horarios de baja demanda
- Together AI: especializado en inferencia de LLMs open source; API de inferencia serverless sin gestión de infraestructura; fine-tuning gestionado disponible; precios competitivos por millón de tokens vs openAI para modelos como Llama 3 y Mixtral

## Para recordar

Para entrenamiento distribuido con SLA empresarial usa hiperescaladores; para experimentos y prototipado cost-effective usa Lambda Labs o RunPod; para inferencia de producción con modelos open source sin gestionar infraestructura usa Together AI o Fireworks AI.
