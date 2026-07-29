# Módulo 9 – Capítulo 06 – Sección 06

# Cierre: la privacidad en IA es una propiedad del sistema, no solo del almacenamiento

La privacidad en sistemas de IA trasciende el paradigma clásico de "cifrar los datos en reposo y en tránsito": un sistema puede tener todas sus bases de datos cifradas con AES-256, todos sus canales protegidos con TLS 1.3, y aun así violar la privacidad de sus usuarios si el modelo memoriza y reproduce datos personales de entrenamiento, si el historial de conversación se usa para fine-tuning sin consentimiento informado, o si documentos de un usuario son recuperados por RAG como contexto para la respuesta de otro usuario sin controles de segmentación. La privacidad en IA es una propiedad emergente del sistema completo —del diseño del pipeline de datos, del proceso de entrenamiento, de la arquitectura del sistema de inferencia, de los controles de acceso al vectorstore— que debe diseñarse intencionalmente desde la arquitectura, no remendarse con cifrado posterior. Los frameworks regulatorios (GDPR Art. 25 "privacy by design", EU AI Act) exigen este enfoque sistémico, y los casos de uso de alto riesgo (salud, finanzas, legal) lo hacen técnicamente obligatorio.

*"Privacy is not a feature you add; it's an architecture you design."* — Ann Cavoukian, inventora del marco "Privacy by Design" y ex Comisionada de Información y Privacidad de Ontario, Canadá, cuyo principio de privacidad desde el diseño es hoy requisito legal en el GDPR (Artículo 25).

## Conceptos clave del capítulo

- PII en todas las capas: detección automática con Microsoft Presidio antes de indexar en RAG, anonimización/pseudonimización del corpus de fine-tuning, validación de outputs para prevenir exposición de PII memorada
- Cifrado integral: TLS 1.3 en tránsito para todas las APIs, AES-256 con claves KMS para vectorstores y artefactos de modelo en reposo, logs de inferencia como datos sensibles de primera clase
- Memorización de training data: riesgo cuantificable y documentado (Carlini et al.); mitigado con deduplicación del corpus y differential privacy (DP-SGD con Opacus) con epsilon documentado
- Differential privacy: garantía matemática de privacidad con trade-off utilidad/privacidad calibrado al epsilon; PEFT+DP como combinación práctica para fine-tuning con datos sensibles
- Audit log para compliance: registro inmutable de model_id, user_id, retrieved_document_ids, tool_calls y outputs; retention con soporte de borrado selectivo para DSAR de GDPR

## Idea central

La privacidad en un sistema de IA debe diseñarse arquitectónicamente desde el inicio — en el pipeline de datos, en el proceso de entrenamiento y en los controles de acceso a los componentes — porque añadirla posteriormente mediante cifrado puntual no resuelve los riesgos de memorización, extracción de datos de entrenamiento y cross-user contamination que son estructurales al diseño del sistema.
