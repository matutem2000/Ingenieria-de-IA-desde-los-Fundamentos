# Módulo 8 – Capítulo 04 – Sección 03

# GPUs para inferencia: NVIDIA RTX/A-series, AMD Instinct y sus características

El mercado de GPUs para inferencia de LLMs está segmentado en tres categorías con características técnicas muy distintas: GPUs de consumo (RTX series), GPUs profesionales de estación de trabajo (A/L-series y equivalentes AMD) y aceleradores de datacenter (H100/A100 NVIDIA, MI300X AMD), cada una con diferente capacidad de VRAM, ancho de banda de memoria, soporte de FP8 y costo por GB de VRAM. Las GPUs RTX 4000/5000 de NVIDIA son la opción más accesible para despliegue local de LLMs: la RTX 4090 ofrece 24 GB de GDDR6X con 1.008 TB/s de ancho de banda de memoria a un precio de mercado que hace viable construir un servidor de inferencia de un único usuario; la RTX 4080 Super ofrece 16 GB y la RTX 3090 Ti/4080 16 GB a precios menores, siendo todos viables para modelos de 7B-13B. Los aceleradores NVIDIA H100 (80 GB HBM3, 3.35 TB/s de ancho de banda) y A100 (80 GB HBM2e, 2 TB/s) son los estándares de producción para serving a escala: su capacidad de memoria y ancho de banda permiten cargar modelos de 70B en precisión completa y servir decenas de peticiones simultáneas con baja latencia.

## GPUs relevantes para inferencia de LLMs

- NVIDIA RTX 4090: 24 GB GDDR6X, 1.008 TB/s ancho de banda, 82.6 TFLOPS FP16, soporte INT8 y FP8 vía Tensor Cores Ada Lovelace; ideal para modelos de 7B-13B en Q8 o hasta 34B en Q4; precio de mercado ~1.600 USD
- NVIDIA RTX 3090/4080: 24/16 GB GDDR6X, capacidad para modelos de 7B en FP16 o 13B-34B en variantes Q4; soporte INT8 en Tensor Cores Ampere/Ada; opción más económica para desarrollo y producción de baja escala
- NVIDIA A100 (40/80 GB): HBM2e con 1.55/2 TB/s ancho de banda; soporte para NVLink de alta velocidad entre múltiples GPUs; estándar de la industria para serving de modelos 13B-70B; disponible principalmente en cloud (AWS p4d, GCP a2)
- NVIDIA H100 (80 GB): HBM3 con 3.35 TB/s ancho de banda, soporte FP8 nativo con transformers engine; throughput 3x superior a A100 en inferencia de LLMs; disponible en cloud como AWS p5, GCP a3
- AMD Instinct MI300X (192 GB): mayor VRAM disponible en el mercado con 192 GB HBM3; throughput competitivo con H100 en modelos grandes; soporte ROCm con vLLM y PyTorch; disponible en cloud providers como Lambda Labs y Azure ND MI300X

## Para recordar

Para inferencia local de producción, la RTX 4090 con 24 GB es el mejor punto de entrada en precio/rendimiento; para producción escalable en la nube, H100 o A100 son el estándar con el ecosistema de software más maduro.
