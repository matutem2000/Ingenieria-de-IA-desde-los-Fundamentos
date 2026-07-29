# Módulo 9 – Capítulo 01 – Sección 05

# Responsabilidad compartida: proveedor de modelo, plataforma y aplicación

El modelo de responsabilidad compartida, consolidado en cloud computing por AWS, Azure y GCP, se aplica con matices específicos a los sistemas de IA: el proveedor del modelo base (OpenAI, Anthropic, Google, Meta) es responsable de la seguridad del modelo durante pretraining, RLHF y los controles de seguridad embebidos; la plataforma de serving (Azure OpenAI, AWS Bedrock, Vertex AI) gestiona la infraestructura, el aislamiento de tenants y los controles de red; y el desarrollador de la aplicación es responsable de todo lo que ocurre en la capa de aplicación: prompt engineering seguro, validación de inputs, control de acceso, logging y manejo seguro de outputs. En la práctica, la mayoría de los incidentes de seguridad en sistemas de IA ocurren en la capa de aplicación, que es la responsabilidad exclusiva del equipo de desarrollo. Entender exactamente dónde termina la responsabilidad del proveedor y dónde comienza la del desarrollador es crítico para evitar asumir una seguridad que no existe por defecto.

## Puntos críticos del modelo de responsabilidad

- Proveedor de modelo base: seguridad de los pesos, RLHF/Constitutional AI para reducir outputs dañinos, filtros de contenido embebidos, y protección de la infraestructura de entrenamiento — el desarrollador no puede auditar ni modificar estos controles
- Proveedor de plataforma (API): rate limiting, autenticación de API keys, TLS en tránsito, aislamiento de requests entre clientes, y SLA de disponibilidad — el desarrollador configura pero no implementa estos controles
- Desarrollador de la aplicación: prompt design seguro, validación y sanitización de user inputs, implementación de guardrails adicionales (LlamaGuard, Azure Content Safety), control de acceso a endpoints, logging de seguridad y manejo seguro de PII en contexto
- Zonas grises de responsabilidad: prompt injection sobre datos recuperados por RAG es responsabilidad del desarrollador aunque el modelo sea el ejecutor; las respuestas del modelo con contenido inapropiado en contextos específicos requieren guardrails adicionales a nivel de aplicación
- Fine-tuning y modelos propios: cuando el equipo realiza fine-tuning, la responsabilidad de la seguridad del modelo derivado recae completamente en el equipo, incluyendo la protección del proceso de entrenamiento contra data poisoning

## Principio rector

En un sistema de IA en producción, la seguridad que el proveedor del modelo garantiza es el piso mínimo, no la protección completa: cada capa de la aplicación debe implementar sus propios controles independientes porque ningún proveedor puede proteger al desarrollador de sus propias decisiones de diseño.
