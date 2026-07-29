# Módulo 11 – Capítulo 04 – Sección 04

# Personalización por tenant: modelos, prompts y comportamientos específicos por cliente

La personalización por tenant en plataformas de IA enterprise va más allá de cambiar el logo y el color del interfaz: incluye la capacidad de configurar el modelo de LLM subyacente por tenant (algunos tenants pueden tener contratos propios con OpenAI o requerir modelos on-premise por restricciones de datos), personalizar el system prompt con instrucciones específicas del dominio y la persona del asistente de cada cliente, configurar los guardrails de seguridad con las restricciones temáticas específicas de cada negocio, y definir los índices vectoriales propios que alimentan el RAG con el conocimiento particular de cada organización. La gestión de configuración por tenant debe implementarse mediante un tenant configuration service que almacena en base de datos (PostgreSQL con JSONB o DynamoDB) la configuración específica de cada tenant — modelo elegido, system prompt base, temperatura, max tokens, idioma por defecto, documentos de base de conocimiento, integraciones habilitadas — y la expone mediante una API de configuración que el servicio de orquestación consulta en cada petición o cachea con TTL corto en Redis para no introducir latencia adicional. El fine-tuning por tenant es la forma más avanzada de personalización: permite adaptar el comportamiento del modelo a los datos, el vocabulario, y los patrones de respuesta específicos de cada cliente mediante LoRA adapters o adaptadores PEFT que se cargan dinámicamente sobre el modelo base compartido, sin requerir un modelo completamente separado por tenant.

## Mecanismos de personalización por tenant

- System prompt por tenant: almacenado en el prompt registry versionado, con capacidad de A/B testing entre versiones de prompt para un mismo tenant sin afectar a otros tenants
- Selección de modelo por tenant: routing configurable que permite a tenants Enterprise elegir entre GPT-4o, Claude Sonnet, Gemini Pro, o modelos open-source self-hosted, con fallback configurable si el modelo primario no está disponible
- Índices RAG por tenant: cada tenant tiene su colección en la base de datos vectorial con sus propios documentos, chunking strategy, y configuración de reranker — completamente separados de los de otros tenants
- LoRA adapters por tenant: fine-tuning ligero (4-8B parameters adapter) que personaliza el comportamiento del modelo base para el vocabulario y los patrones de respuesta específicos del tenant, cargado dinámicamente con vLLM's LoRA adapter loading
- Feature flags por tenant: sistema de configuración granular (LaunchDarkly o Unleash) que habilita o deshabilita capacidades específicas (búsqueda web, ejecución de código, acceso a herramientas externas) según el plan o las necesidades del tenant

## Idea central

La personalización por tenant debe ser un sistema de configuración dinámico y auditable — no hardcodeado por tenant en el código fuente — para que los cambios de configuración sean desplegables sin modificar el código y reversibles sin rollback de infraestructura.
