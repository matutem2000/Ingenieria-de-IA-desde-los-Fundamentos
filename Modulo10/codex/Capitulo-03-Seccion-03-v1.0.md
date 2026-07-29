# Módulo 10 – Capítulo 03 – Sección 03

# Hugging Face Hub enterprise: gestión de modelos privados y control de acceso

Hugging Face Hub Enterprise (también llamado Hugging Face Enterprise Hub) es la versión privada y gestionada del Hub público de Hugging Face, diseñada para organizaciones que necesitan alojar modelos propietarios, datasets privados y Spaces internos sin exponerlos públicamente, manteniendo al mismo tiempo la experiencia de usuario del ecosistema estándar de Hugging Face (CLI `huggingface-cli`, `from_pretrained()`, Inference Endpoints). A diferencia del Hub público, la versión Enterprise añade: Single Sign-On (SSO) vía SAML 2.0 o OIDC integrado con el IdP corporativo (Okta, Azure AD, Google Workspace), control de acceso basado en roles a nivel de organización, equipo y repositorio, audit logs de todas las operaciones de descarga y push, y la opción de despliegue en infraestructura VPC del cliente (AWS, GCP, Azure) para cumplir con requisitos de residencia de datos. El control de acceso se modela en tres niveles: organización (con billing y SSO centralizados), teams (grupos de usuarios con permisos heredables), y repositorios individuales (públicos, privados o internos a la organización); un modelo puede ser `private` (visible solo al owner), `internal` (visible a todos los miembros de la organización), o `gated` (requiere aprobación explícita para descarga).

## Componentes principales de Hugging Face Hub Enterprise

- Private model repositories: repositorios Git LFS para modelos con acceso restringido a teams específicos, con política de descarga controlada vía tokens de usuario con scopes limitados (`read`, `write`, `admin`)
- Inference Endpoints Enterprise: despliegue de modelos privados como APIs en AWS/GCP/Azure con autoscaling, VPC peering y sin salida de datos a internet; soporte para GPUs A10G, A100 y L4
- SSO y RBAC: integración con SAML/OIDC para autenticación federada; permisos granulares por repositorio con roles predefinidos (reader, contributor, admin) y custom roles
- Audit logs: registro inmutable de todas las acciones (push, pull, delete, permission change) con timestamp, usuario y IP, exportable a SIEM corporativo vía webhook o API
- Spaces privados: aplicaciones Gradio y Streamlit internas para demos y herramientas de evaluación de modelos, accesibles solo desde la red corporativa

## Idea central

Hugging Face Hub Enterprise permite a las organizaciones beneficiarse del ecosistema open source de Hugging Face (transformers, datasets, evaluate) manteniendo el control total sobre quién accede a sus modelos propietarios y desde dónde.
