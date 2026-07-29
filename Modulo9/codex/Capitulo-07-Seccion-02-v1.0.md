# Módulo 9 – Capítulo 07 – Sección 02

# Autenticación y autorización: OAuth2, API keys y control de acceso a modelos

La autenticación y autorización en APIs de IA sigue los estándares de la industria (OAuth 2.0, OpenID Connect, API keys con rotación), pero su implementación debe contemplar consideraciones específicas del contexto de IA: el control de acceso debe ser granular no solo a nivel de endpoint sino a nivel de capacidad del modelo (qué modelos puede usar cada cliente, con qué parámetros, en qué volumen), y los tokens de acceso no deben incluirse nunca en el contexto del modelo (ni en el system prompt ni en variables de entorno accesibles desde el código del agente). OAuth 2.0 con PKCE es el estándar para aplicaciones que actúan en nombre de usuarios finales; API keys con rotación automática son apropiadas para comunicación server-to-server; JWT (JSON Web Tokens) con claims de IA (modelo autorizado, límites de tokens, tenant_id) permiten autorización granular stateless en arquitecturas de microservicios. La separación entre autenticación (¿quién eres?) y autorización (¿qué puedes hacer?) es crítica: un sistema donde la misma API key da acceso a todos los modelos, todas las capacidades y todos los datos del tenant no implementa autorización, solo autenticación.

## Aspectos técnicos

- Jerarquía de API keys: clave maestra de organización (que no se usa directamente en código) → project keys con scope limitado (qué modelos, qué endpoints) → session tokens de corta duración para requests específicas; cada nivel tiene diferente capacidad de daño si se compromete y diferente frecuencia de rotación
- RBAC para modelos de IA: Role-Based Access Control donde diferentes roles tienen acceso a diferentes modelos y parámetros — por ejemplo, un rol "basic" tiene acceso solo a GPT-3.5-turbo con temperature máxima de 0.7, mientras un rol "advanced" tiene acceso a GPT-4o con parámetros completos; implementado mediante middleware de autorización que verifica los claims del JWT antes de reenviar la request al proveedor del modelo
- Rotación de API keys: las API keys de larga duración son un riesgo de seguridad significativo; la rotación debe ser automática (máximo 90 días) con un período de transición donde ambas claves son válidas; herramientas como HashiCorp Vault con Dynamic Secrets generan API keys de duración limitada (TTL de horas o días) que se revocan automáticamente
- Detección de uso de API keys comprometidas: patrones de uso anómalo (geolocalización diferente al patrón habitual, volumen de tokens inusualmente alto, endpoints no utilizados previamente) deben triggear alertas y opcionalmente suspensión temporal de la key para verificación
- Autorización de modelos fine-tuned: los modelos fine-tuned con datos de un tenant específico solo deben ser accesibles para ese tenant; la autorización debe verificar que el model_id en la request pertenece al tenant del token de autenticación — un cliente no debe poder acceder al modelo fine-tuned con datos propietarios de otro cliente

## Buena práctica

Las API keys nunca deben aparecer en el código fuente, en el historial de git, en logs de aplicación, ni en variables de entorno no cifradas en producción: deben gestionarse exclusivamente mediante secrets managers (AWS Secrets Manager, HashiCorp Vault, Azure Key Vault) con rotación automática y sin exposición al sistema de archivos del host.
