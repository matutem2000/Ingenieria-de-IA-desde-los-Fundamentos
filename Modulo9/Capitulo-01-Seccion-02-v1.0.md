# Módulo 9 – Capítulo 01 – Sección 02

# Taxonomía de amenazas: input attacks, model attacks, supply chain attacks y data attacks

Una taxonomía clara de amenazas es el prerrequisito para un modelo de amenazas riguroso: sin categorías bien definidas, los controles se aplican de forma reactiva y desorganizada. OWASP LLM Top 10 (2023-2024) y el marco MITRE ATLAS proporcionan taxonomías complementarias que cubren desde ataques a nivel de prompt hasta compromisos de la cadena de suministro del modelo. Los input attacks operan en tiempo de inferencia, los model attacks comprometen los pesos o el proceso de entrenamiento, los supply chain attacks afectan las dependencias del sistema y los data attacks apuntan a los datos de entrenamiento o recuperación. Mapear cada amenaza a esta taxonomía permite asignar controles preventivos en la capa correcta del sistema.

## Categorías de amenazas en sistemas de IA

- Input attacks: prompt injection directa e indirecta, jailbreaking, prompt leaking y ataques de denegación de servicio mediante prompts de alta complejidad computacional (context-flooding con ventanas de 128k tokens)
- Model attacks: model extraction via consultas sistemáticas a la API para reconstruir el comportamiento del modelo, membership inference para detectar si un dato específico fue parte del entrenamiento, y fine-tuning adversarial para insertar backdoors activados por tokens trigger
- Supply chain attacks: descarga de modelos de Hugging Face con pesos modificados mediante pickle exploitation, dependencias maliciosas en packages de ML (torch, transformers, accelerate) y datasets adulterados en pipelines de data ingestion
- Data attacks: RAG poisoning mediante inyección de documentos maliciosos en Pinecone, Weaviate o Chroma que el modelo recuperará como contexto confiable, y training data poisoning para degradar accuracy o insertar comportamientos backdoor específicos
- Infrastructure attacks: explotar vulnerabilidades en el serving layer (Triton Inference Server, vLLM, TGI), escalar privilegios desde el contexto del modelo hacia el host del container, o comprometer el pipeline de MLflow/Kubeflow para inyectar modelos maliciosos

## Para recordar

Cada categoría de amenaza requiere controles en una capa diferente del sistema: los input attacks se mitigan en el gateway, los model attacks en el pipeline de ML, los supply chain attacks en la gestión de dependencias y los data attacks en la pipeline de ingestión de datos.
