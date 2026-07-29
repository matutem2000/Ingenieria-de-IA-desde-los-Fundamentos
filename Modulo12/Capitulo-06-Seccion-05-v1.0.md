# Módulo 12 – Capítulo 06 – Sección 05

# Gestión de configuraciones: variables de entorno, secrets management y configuración por entorno

La gestión de configuraciones del sistema integrador sigue el principio de los Twelve-Factor App: toda la configuración que varía entre entornos se almacena en variables de entorno, nunca en el código ni en archivos commiteados al repositorio. Los secrets (OPENAI_API_KEY, QDRANT_API_KEY, DATABASE_URL, JWT_PRIVATE_KEY) se almacenan en AWS Secrets Manager y se inyectan en los pods de Kubernetes mediante el External Secrets Operator, que sincroniza automáticamente los secrets de AWS SM con Kubernetes Secrets y los rota sin reiniciar los pods cuando cambia su valor en AWS. La configuración no sensible (parámetros del pipeline RAG, límites de rate limiting, umbrales de evaluación) se gestiona con ConfigMaps de Kubernetes, con un ConfigMap por servicio y por entorno. Para facilitar el desarrollo local, el proyecto incluye un archivo `.env.example` con todas las variables necesarias documentadas y sus valores de desarrollo seguro.

## Gestión de configuraciones por capa

- Secrets: AWS Secrets Manager con External Secrets Operator para sincronización automática con Kubernetes Secrets
- Rotación de secrets: AWS SM Secret Rotation con Lambda function que rota OPENAI_API_KEY cada 90 días automáticamente
- ConfigMaps: parámetros no sensibles (chunk_size, top_k, max_iterations, rate_limit_per_minute) por entorno
- Configuración de aplicación: Pydantic Settings con validación de tipos y valores al inicio de la aplicación, falla fast si falta un secret
- Trazabilidad: cada cambio de configuración en AWS SM emite un evento a CloudTrail para audit log completo

## Para recordar

La gestión de secrets es el control de seguridad más frecuentemente comprometido en sistemas de producción — un secret en el código o en un archivo .env commiteado es una vulnerabilidad crítica que puede explotarse durante años después del commit.
