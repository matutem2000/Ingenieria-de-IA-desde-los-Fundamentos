# Módulo 11 – Capítulo 05 – Sección 01

# LLMOps vs MLOps tradicional: qué cambia cuando el modelo es un LLM con miles de millones de parámetros

LLMOps es la adaptación de las prácticas de MLOps al ciclo de vida específico de los Large Language Models, y las diferencias con el MLOps tradicional no son superficiales: afectan los procesos de evaluación, despliegue, monitoreo, y actualización de manera profunda porque los LLMs tienen propiedades únicas que los modelos de ML clásicos (XGBoost, Random Forest, redes neuronales supervisadas) no tienen. La primera diferencia crítica es la evaluación: mientras un modelo de clasificación tiene métricas objetivas como accuracy, F1 score, y AUC-ROC que pueden calcularse automáticamente comparando predicciones contra etiquetas verdaderas, la calidad de un LLM en tareas de generación de texto es multidimensional (coherencia, relevancia, precisión factual, alineación con el estilo esperado) y frecuentemente requiere evaluadores LLM-as-a-judge (usando GPT-4 o Claude para calificar respuestas) o evaluaciones humanas, ambas con costo y latencia significativamente mayores que las métricas automáticas tradicionales. La segunda diferencia es el versionado: en MLOps tradicional, el artefacto principal que se versiona es el modelo (archivos .pkl, .pt, .onnx); en LLMOps, el artefacto más frecuentemente modificado es el prompt, que puede cambiar el comportamiento del sistema sin tocar el modelo, requiriendo un sistema de versionado de prompts tan riguroso como el versionado de código. La tercera diferencia es el costo de inferencia: un modelo de 70B parámetros en producción puede costar entre 100 y 1.000 veces más por inferencia que un modelo de ML clásico, haciendo que la optimización de costos sea una responsabilidad central del equipo de LLMOps.

## Diferencias técnicas entre LLMOps y MLOps

- Evaluación no determinista: los LLMs producen respuestas distintas con el mismo input (temperatura > 0), lo que invalida las suites de testing basadas en igualdad exacta y requiere comparación semántica o evaluadores LLM-as-a-judge
- Prompt como artefacto de ingeniería: los prompts deben versionarse en Git o en un prompt registry (LangSmith, PromptLayer, Langfuse), con changelog, tests de regresión, y proceso de review antes de desplegar a producción
- Costo de fine-tuning vs actualización de prompts: re-entrenar un LLM de 7B parámetros con LoRA cuesta entre 100 y 1.000 USD en GPU cloud; actualizar un prompt cuesta centavos — la decisión de cuándo hacer fine-tuning vs prompt engineering es central en LLMOps
- Inferencia a escala con vLLM: despliegue de modelos open-source con vLLM que soporta PagedAttention para maximizar el throughput de tokens por segundo y reducir el costo por inferencia frente a Hugging Face Transformers naïve
- Drift de comportamiento sin drift de datos: un LLM puede degradar su calidad de respuesta no por cambios en los datos de entrada sino por cambios en el contexto de uso, la distribución de preguntas, o actualizaciones del modelo base por parte del proveedor

## Para recordar

LLMOps requiere construir un sistema de evaluación continua antes de desplegar el primer modelo a producción — sin evaluación automatizada, no hay manera de detectar regresiones cuando el sistema cambia.
