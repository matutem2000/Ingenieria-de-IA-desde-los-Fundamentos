# Módulo 9 – Capítulo 03 – Sección 06

# Cierre: los ataques adversariales son una realidad en producción, no solo un problema de investigación

Los ataques adversariales contra sistemas de ML fueron durante años considerados un problema académico interesante pero con poca relevancia práctica en producción: la idea de que un atacante necesitaba acceso whitebox al modelo o condiciones de laboratorio parecía alejarlos del mundo real. Esa percepción cambió fundamentalmente con los trabajos de Carlini et al. sobre extracción de datos de entrenamiento de GPT en producción, con la demostración de ataques de transferencia que funcionan en modelos propietarios, y con los primeros casos documentados de data poisoning en pipelines de fine-tuning con datos de usuarios en producción. Hoy, model extraction, membership inference, y data poisoning son riesgos que los equipos de AI Engineering deben incorporar explícitamente en sus threat models, especialmente en sistemas que procesan datos sensibles, tienen alta valoración de mercado por su comportamiento propietario, o usan datos de usuarios para fine-tuning continuo. Las defensas disponibles —differential privacy, auditoría de datasets, detección de backdoors, rate limiting para extracción, watermarking— son maduras pero requieren implementación intencional desde la fase de diseño.

*"Adversarial examples are not bugs, they are features — and understanding that changes how we think about the security of machine learning systems."* — Ian Goodfellow, investigador de DeepMind y creador de las Generative Adversarial Networks, explicando por qué la vulnerabilidad adversarial es una propiedad estructural de los modelos, no un defecto corregible.

## Conceptos clave del capítulo

- Ataques adversariales en texto: perturbaciones mínimas (homoglifos, sinónimos, inserción de tokens) que cambian drásticamente la predicción del modelo; targets primarios son clasificadores de contenido y sistemas de moderación
- Transferibilidad: un ataque generado contra LLaMA puede funcionar contra GPT-4 sin modificación; la defensa basada en la opacidad del modelo es insuficiente ante este fenómeno
- Model extraction: reconstrucción del comportamiento propietario vía queries sistemáticas a la API; técnicamente indistinguible de distillation legítima; prevenida con rate limiting y monitoreo de patrones de query
- Membership inference: determinación estadística de si un dato fue parte del entrenamiento; LLMs memorizan y reproducen verbatim datos del corpus; mitigada con differential privacy y deduplicación del training set
- Data poisoning y backdoors: contaminación del pipeline de entrenamiento con ejemplos que insertan comportamientos latentes activados por triggers; la única ventana de detección es antes de que el modelo entre en producción

## Idea central

Los ataques adversariales en producción no requieren acceso a los internals del modelo: con solo acceso a la API y los outputs, un adversario sofisticado puede extraer el modelo, inferir datos de entrenamiento o preparar ataques transferibles — lo que hace indispensable que la seguridad de sistemas de IA sea parte del diseño desde el día cero.
