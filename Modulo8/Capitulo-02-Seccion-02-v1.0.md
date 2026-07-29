# Módulo 8 – Capítulo 02 – Sección 02

# GGUF: formato para inferencia en CPU y GPU con llama.cpp

GGUF (GPT-Generated Unified Format) es el formato de archivo binario diseñado por Georgi Gerganov como sucesor de GGML para distribuir modelos cuantizados optimizados para inferencia eficiente en CPU y GPU sin dependencias de PyTorch ni de CUDA. El formato almacena en un único archivo los pesos cuantizados, los hiperparámetros del modelo, la configuración del tokenizador, los templates de prompts y metadatos de cuantización como los factores de escala por grupo, eliminando la necesidad de archivos de configuración externos. GGUF soporta carga parcial en GPU mediante la opción `--n-gpu-layers` de llama.cpp: si el modelo no cabe completamente en VRAM, las capas más computacionalmente intensivas se ejecutan en GPU y las restantes en CPU usando RAM del sistema, permitiendo un balance dinámico entre velocidad y memoria disponible. Los archivos GGUF se identifican por su variante de cuantización en el nombre de archivo: `llama-3-8b-instruct.Q4_K_M.gguf` indica cuantización K-quant de 4 bits con mezcla media (M), el punto de equilibrio más popular entre tamaño y calidad.

## Componentes del formato GGUF

- Cabecera del archivo: magic number `GGUF` de 4 bytes seguido de versión, número de tensores y número de pares de metadatos key-value; permite validar el archivo antes de cargarlo completo
- Metadatos key-value: almacena configuración del modelo (n_head, n_layer, rope_freq_base, etc.), información del tokenizador (vocabulario, tokens especiales, template de chat) y provenance del archivo
- Tensores cuantizados: almacenados en orden de dependencia para permitir streaming desde disco; cada tensor incluye su nombre, dimensiones, tipo de cuantización y datos raw
- Variantes K-quant: Q2_K, Q3_K_S/M/L, Q4_K_S/M, Q5_K_S/M, Q6_K; la letra después de K indica el número de bits y la letra final el tamaño del grupo de cuantización (S=small, M=medium, L=large)
- Compatibilidad multiplataforma: llama.cpp compila con soporte para Metal (Apple Silicon), CUDA (NVIDIA), ROCm (AMD), Vulkan (cross-platform) y CPU pura; el mismo archivo GGUF funciona en todos sin recompilar el modelo

## Para recordar

GGUF es el formato estándar de facto para distribución de modelos cuantizados ejecutables localmente: su diseño de archivo único con metadatos embebidos simplifica enormemente la distribución y el despliegue reproducible de modelos.
