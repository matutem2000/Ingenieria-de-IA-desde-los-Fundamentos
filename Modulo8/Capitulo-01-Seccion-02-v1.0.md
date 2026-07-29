# Módulo 8 – Capítulo 01 – Sección 02

# Familias de modelos: Llama, Mistral, Gemma, Phi, Qwen y sus características

El ecosistema de modelos abiertos converge en unas pocas familias dominantes que cubren rangos de parámetros desde 1B hasta 70B+, cada una con arquitecturas Transformer basadas en variantes de atención eficiente y tokenizadores propios. La familia Llama 3 de Meta introdujo atención con cabezas de consulta agrupada (GQA) y un vocabulario expandido a 128.256 tokens con BPE, mejorando significativamente el manejo multilingüe respecto a Llama 2. Mistral y su variante Mixtral implementan Sparse Mixture of Experts (SMoE) con 8 expertos y activación de 2 por token, permitiendo modelos de 46.7B parámetros totales pero con costo computacional equivalente a un modelo denso de 12.9B. Phi de Microsoft y Gemma de Google apuestan por modelos pequeños y eficientes entrenados con datos sintéticos de alta calidad y datasets filtrados, logrando rendimiento competitivo en benchmarks con menos de 4B parámetros.

## Características técnicas por familia

- Llama 3.1/3.2 (Meta): arquitectura RoPE con theta=500.000, GQA, contexto de 128K tokens, lanzado en tamaños 8B, 70B y 405B con soporte multimodal en variantes Vision
- Mistral/Mixtral (Mistral AI): ventana deslizante de atención (SWA) de 4.096 tokens en modelos densos, SMoE con balanceo de carga por pérdida auxiliar, tokenizador SentencePiece de 32K tokens
- Gemma 2 (Google): arquitectura con atención alternada local/global, destilación de conocimiento desde modelos Gemini más grandes, disponible en 2B y 9B con licencia permisiva para uso comercial
- Phi-3/Phi-4 (Microsoft): entrenamiento con datos de alta calidad incluyendo libros de texto sintéticos generados con GPT-4, phi-3-mini de 3.8B supera a Llama 2-7B en MMLU y HumanEval
- Qwen 2.5 (Alibaba): soporte nativo multilingüe con énfasis en chino y árabe, variantes especializadas en código (Qwen2.5-Coder) y matemáticas (Qwen2.5-Math) disponibles en tamaños de 0.5B a 72B

## Para recordar

Elegir una familia de modelos implica evaluar no solo el tamaño en parámetros sino la arquitectura de atención, el vocabulario del tokenizador y las restricciones de licencia que aplican a tu caso de uso específico.
