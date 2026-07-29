# Módulo 9 – Capítulo 06 – Sección 01

# PII en sistemas de IA: detección, anonimización y pseudonimización

La gestión de Información de Identificación Personal (PII) en sistemas de IA es técnicamente más compleja que en sistemas tradicionales porque el PII puede aparecer en múltiples capas: en el input del usuario (nombres, emails, documentos de identidad), en los documentos del corpus RAG, en el historial de conversación usado para fine-tuning, en los logs de inferencia, y potencialmente en las respuestas del modelo si este memorizó PII de su pretraining. Herramientas como Microsoft Presidio (open-source), Amazon Comprehend PII Detection, y spaCy con modelos de NER pueden detectar automáticamente categorías estándar de PII (nombres, emails, números de teléfono, SSN, números de tarjeta de crédito) en texto, pero tienen falsos negativos para PII contextual o en idiomas no-inglés. La anonimización (eliminación irreversible del PII) y la pseudonimización (sustitución por identificadores reversibles) son técnicas complementarias con diferentes trade-offs para sistemas de IA: la anonimización es más segura pero puede degradar la calidad del modelo si el PII es relevante para la tarea; la pseudonimización preserva la utilidad pero requiere proteger la tabla de mapeo.

## Aspectos técnicos

- Detección automática de PII: Microsoft Presidio soporta 50+ entidades PII en múltiples idiomas, incluyendo nombres, emails, teléfonos, documentos de identidad, coordenadas geográficas y credenciales financieras; para PII contextual (por ejemplo, "mi jefe Juan López") se requieren modelos NER fine-tuned en el dominio específico
- Anonimización en el pipeline RAG: los documentos deben pasar por un pipeline de detección y redacción de PII antes de ser indexados en el vectorstore; el mismo documento sin PII debe servir a todos los usuarios, preservando la utilidad del sistema sin exponer datos personales entre usuarios
- Pseudonimización para fine-tuning: cuando los datos de fine-tuning contienen PII, la pseudonimización —sustitución de nombres reales por placeholders consistentes (PERSON_1, PERSON_2)— preserva las relaciones semánticas del texto mientras protege la identidad de los sujetos; la tabla de mapeo debe almacenarse con cifrado y controles de acceso estrictos
- PII en el historial de conversación: los sistemas que almacenan historial de conversación (para memoria multi-turn o para fine-tuning con datos de usuarios) acumulan PII que el usuario proporcionó en contexto; esta acumulación debe estar sujeta a TTL (tiempo de vida), cifrado y mecanismos de derecho al olvido (borrado a petición del usuario)
- Detección de PII en outputs: los outputs del modelo pueden contener PII memorizada del corpus de pretraining (fenómeno demostrado por Carlini et al.) o PII del contexto del usuario no redactada apropiadamente; un pipeline de validación de outputs debe escanear las respuestas antes de entregarlas al cliente para detectar PII no intencional

## Para recordar

La gestión de PII en sistemas de IA debe cubrir todas las capas donde el PII puede aparecer — input, corpus RAG, logs, historial, outputs — con controles técnicos específicos en cada capa: la detección automática es necesaria pero no suficiente, y debe complementarse con arquitecturas que minimicen la retención de PII desde el diseño del sistema.
