# Módulo 9 – Capítulo 01 – Sección 03

# CIA Triad aplicada a IA: confidencialidad, integridad y disponibilidad en sistemas LLM

La CIA Triad —Confidentiality, Integrity, Availability— es el modelo fundacional de seguridad de la información, pero su aplicación a sistemas LLM requiere reinterpretaciones específicas que van más allá de las definiciones clásicas. La confidencialidad en un sistema de IA no solo abarca los datos en tránsito o en reposo, sino también la información que el modelo puede memorizar de su entrenamiento y revelar en respuestas futuras, incluyendo PII, credenciales y datos propietarios. La integridad no solo aplica a los datos almacenados, sino al comportamiento consistente del modelo: un ataque de fine-tuning malicioso compromete la integridad del modelo mismo. La disponibilidad incluye la resistencia a ataques de prompt que consumen excesivos tokens o provocan respuestas infinitamente largas, afectando la capacidad de servir requests legítimos.

## Aspectos técnicos de la CIA en sistemas LLM

- Confidencialidad del model behavior: los pesos del modelo pueden revelar datos de entrenamiento mediante ataques de extracción; el system prompt puede ser filtrado mediante prompt leaking; las respuestas pueden contener PII memorizada del corpus de pretraining
- Integridad del modelo: el comportamiento del modelo debe ser predecible y consistente con sus especificaciones; un backdoor insertado durante fine-tuning compromete la integridad funcional aunque los pesos no estén "corruptos" en el sentido clásico
- Integridad de los datos de inferencia: los documentos en el vectorstore (Pinecone, pgvector, Weaviate) deben provenir de fuentes validadas; un documento inyectado maliciosamente compromete la integridad del contexto del modelo
- Disponibilidad frente a prompt attacks: prompts diseñados para generar respuestas de máxima longitud o activar loops de razonamiento infinito (en chain-of-thought) son ataques de DoS específicos de LLMs
- Confidencialidad del pipeline de MLOps: los artefactos de modelo en MLflow, los datasets en S3/GCS y los logs de entrenamiento contienen información sensible que requiere controles de acceso equivalentes a los datos que procesaron

## Idea central

La CIA Triad aplicada a sistemas LLM exige extender las definiciones tradicionales para cubrir el modelo como un activo de información en sí mismo, cuya confidencialidad, integridad y disponibilidad deben protegerse con los mismos controles rigurosos que cualquier base de datos crítica.
