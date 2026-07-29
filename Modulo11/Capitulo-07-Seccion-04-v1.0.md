# Módulo 11 – Capítulo 07 – Sección 04

# Infrastructure optimization: reserved instances, spot instances y contratos enterprise con proveedores de IA

La optimización de infraestructura para sistemas de IA enterprise tiene dos dimensiones distintas: la optimización de los recursos de cómputo propios (GPU instances en AWS, GCP, o Azure para modelos self-hosted) y la negociación de los contratos de consumo con proveedores de LLM externos (OpenAI, Anthropic, Google). Para recursos de cómputo propios, el modelo de compra impacta directamente los costos: las Reserved Instances (RI) de AWS o los Committed Use Discounts de GCP ofrecen descuentos del 30-60% sobre el precio on-demand para instancias GPU (A100, H100) con compromiso de 1-3 años, lo que es apropiado para workloads de inferencia con demanda predecible y constante. Las Spot Instances ofrecen descuentos del 60-90% sobre el precio on-demand con el riesgo de interrupción (2 minutos de aviso en AWS, 30 segundos en GCP), lo que las hace adecuadas para workloads tolerantes a interrupciones: jobs de indexación batch, fine-tuning de modelos, y procesamiento asíncrono de documentos. La mezcla óptima para sistemas de IA enterprise es típicamente: Reserved Instances para la capacidad base de inferencia en tiempo real (el mínimo de carga constante garantizado), On-Demand para el burst de inferencia durante picos, y Spot para los jobs de procesamiento batch y reentrenamiento. Con proveedores externos de LLM, las organizaciones que consumen más de 50.000-100.000 USD mensuales pueden negociar contratos enterprise con descuentos del 15-30% sobre el precio de tarifa, SLAs de disponibilidad mejorados, y compromisos de soporte técnico dedicado.

## Estrategias de optimización de infraestructura

- Reserved Instances para inferencia base: compromiso de 1 año para instancias GPU (g4dn.xlarge para modelos < 7B, p3.2xlarge para modelos 7-13B) que cubren el 60-70% de la carga típica con descuentos del 30-40% sobre on-demand
- Spot Instances para batch processing: jobs de indexación RAG, generación de embeddings en batch, y fine-tuning de modelos en Spot con Spot Instance Interruption Handlers para checkpoint y restart automático
- vLLM para maximizar throughput de GPU self-hosted: PagedAttention de vLLM aumenta el throughput de tokens por segundo en 2-4x respecto a Hugging Face Transformers, reduciendo el número de GPUs necesarias para la misma carga
- Quantization para reducir costo de GPU: modelos cuantizados a 4-bit (GGUF/GPTQ) requieren 60-70% menos VRAM que los modelos en FP16 con degradación de calidad del 1-3%, permitiendo ejecutar modelos 13B en GPUs con 8-12GB de VRAM
- Contratos enterprise con proveedores: negociar Prepaid Commitments con OpenAI o Anthropic (pago por adelantado de 100.000+ USD a cambio de descuentos del 15-30%) cuando el consumo histórico justifica la certeza de esa demanda

## Buena práctica

Implementar un sistema de FinOps de IA que tagee cada petición de inferencia con el equipo, el caso de uso, y el tenant responsable, permitiendo el showback de costos y la identificación de las cargas de trabajo que más se beneficiarían de optimización o migración a modelos self-hosted.
