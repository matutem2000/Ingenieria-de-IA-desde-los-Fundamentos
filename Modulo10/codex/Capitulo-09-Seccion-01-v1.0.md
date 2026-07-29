# Módulo 10 – Capítulo 09 – Sección 01

# Taxonomía de costos: inferencia, almacenamiento, pipelines de datos y herramientas

Los costos de operar una plataforma de IA tienen una estructura significativamente diferente a los costos de operar aplicaciones web tradicionales: el costo de inferencia de LLMs (basado en tokens de input y output) puede dominar todos los demás costos combinados en aplicaciones de alta frecuencia, mientras que el costo de GPU para entrenamiento tiene picos pronunciados y períodos de inactividad que dificultan la predicción. La taxonomía completa de costos de una plataforma de IA incluye cuatro categorías principales: costos de inferencia (API calls a proveedores externos como OpenAI/Anthropic por tokens consumidos, o GPU time para modelos self-hosted), costos de compute de entrenamiento (GPU hours para fine-tuning o preentrenamiento, que pueden ser spot instances para reducir costo hasta un 70%), costos de almacenamiento (object storage para datasets y pesos de modelos en S3/GCS, feature store online en Redis, y feature store offline en Delta Lake o Iceberg), y costos de herramientas y plataforma (licencias de MLflow Enterprise, Weights & Biases, Tecton, herramientas de observabilidad, y el costo de operar el cluster de Kubernetes de la plataforma). La categoría más difícil de controlar es la de inferencia porque es altamente variable: una sola feature de una aplicación de producción que hace llamadas a GPT-4 puede representar 80% del gasto total de IA de una organización si no se tienen controles de rate limiting y optimización.

## Categorías de costos y su estructura

- Costos de inferencia externa: se facturan por tokens (input + output) en modelos de API como OpenAI o Anthropic; altamente variables según el volumen de uso, el modelo seleccionado y el tamaño del contexto; optimizables con caching y selección de modelo
- Costos de compute de entrenamiento: GPU hours en EC2 (p4d.24xlarge: $32/h, g5.48xlarge: $16/h) o GCP (A100 x8: $30/h); uso de spot/preemptible instances reduce costo 60-90% para jobs tolerantes a interrupciones
- Costos de almacenamiento: S3 Standard: $0.023/GB-month para datasets activos; S3 Glacier: $0.004/GB-month para datasets de entrenamiento históricos; Redis en ElastiCache: $0.2-0.8/GB-month para el feature store online
- Costos de MLOps tooling: Weights & Biases Team: $150/user-month; MLflow Enterprise (Databricks): variable según DBU consumption; Tecton: contrato enterprise; Grafana Cloud Pro: $8/metric-month
- Costos de la plataforma (overhead): cluster de Kubernetes de control (nodos de sistema, ingress, monitoring): $1,000-5,000/month dependiendo del tamaño de la plataforma y la región cloud

## Para recordar

El primer paso para optimizar costos de IA es tener visibilidad: sin tagging de recursos por equipo y proyecto, y sin reportes de atribución de costos, es imposible identificar qué está generando el gasto y dónde están las oportunidades de optimización.
