# Módulo 10 – Capítulo 08 – Sección 03

# Control de acceso basado en roles (RBAC) para datos y modelos

El RBAC (Role-Based Access Control) en una plataforma de IA extiende el modelo de permisos tradicional de sistemas de software a los artefactos específicos de IA: datasets en el feature store y el data lake, modelos en el model registry, endpoints de inferencia, experimentos en el tracking server, y pipelines de entrenamiento. El modelo de roles para una plataforma de IA típicamente incluye: `data-viewer` (puede leer catálogo de datasets y sus metadatos, no puede descargar datos raw), `data-consumer` (puede descargar datasets aprobados para entrenamiento, previa aprobación del data owner), `ml-engineer` (puede lanzar training jobs, registrar modelos en Staging, desplegar en ambientes de development/staging), `model-approver` (puede promover modelos de Staging a Production, requiere pertenencia al Model Review Board), y `platform-admin` (acceso completo, reservado al equipo de plataforma). La implementación técnica se apoya en múltiples capas: en Kubernetes, RBAC nativo con Roles y RoleBindings por namespace; en el feature store, permisos por feature group y por proyecto; en el model registry (MLflow), gestión de permisos por experiment y por registered model; en el LLM Gateway, permisos de acceso por modelo y por endpoint. La sincronización entre el IdP corporativo (Okta, Azure AD) y los sistemas de la plataforma se implementa mediante SCIM 2.0 (provisioning automático de usuarios y grupos) y OIDC/SAML para autenticación federada.

## Componentes clave del RBAC para plataformas de IA

- Roles predefinidos: conjunto mínimo de roles que cubren las operaciones principales (viewer, developer, deployer, approver, admin) con principio de mínimo privilegio; el 90% de los usuarios solo necesitan viewer o developer
- Resource-level permissions: permisos aplicados a instancias específicas de recursos (ej. acceso a un modelo específico, no a todos los modelos del registry), implementados vía resource policies o attribute-based tags
- Temporary access grants: mecanismo para solicitar acceso temporal a recursos de mayor privilegio (ej. acceso a datos de producción para debugging) con expiración automática y log de todas las operaciones durante el período de acceso
- Cross-team access: proceso formal para que el modelo del equipo A sea consumido por el equipo B vía el serving layer, con acuerdo de SLA y visibilidad de uso por el equipo propietario del modelo
- Just-in-time access: integración con sistemas de PAM (CyberArk, HashiCorp Boundary) para acceso privilegiado temporal con aprobación de un segundo factor humano y sesión grabada para auditoría

## Para recordar

El RBAC para plataformas de IA debe diseñarse para el caso de uso real, no para el caso ideal: si los roles son demasiado restrictivos y los ingenieros los bypassean usando cuentas de servicio con permisos excesivos, el sistema de control de acceso ha fracasado.
