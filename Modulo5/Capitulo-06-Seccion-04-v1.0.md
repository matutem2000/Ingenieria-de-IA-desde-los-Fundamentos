# Módulo 5 – Capítulo 06 – Sección 04

# Despliegue continuo: blue-green, canary y feature flags para modelos

Las estrategias de despliegue progresivo que minimizan el riesgo en software tradicional se adaptan directamente a sistemas de IA para gestionar la transición entre versiones de prompts, modelos o pipelines de procesamiento. En blue-green deployment para IA, se mantienen dos entornos de producción idénticos: el entorno activo (blue) con la versión actual del modelo y prompt, y el entorno preparado (green) con la nueva versión; el tráfico se redirige de blue a green a través de un load balancer o DNS flip una vez que las métricas de calidad del entorno green son satisfactorias. El canary deployment para IA expone la nueva versión a un porcentaje creciente del tráfico real (5% → 25% → 50% → 100%) mientras se monitorean las métricas de calidad en tiempo real; si las métricas del canary degradan respecto al baseline, el tráfico se revierte automáticamente al 0% sin intervención manual. Los feature flags son la implementación más flexible y granular: permiten activar la nueva versión del modelo para usuarios específicos (power users, usuarios beta), para ciertas geografías, o para ciertos tipos de consulta (clasificadas por un model router), con reversión instantánea.

## Aspectos técnicos del despliegue progresivo para modelos

- Canary con Kubernetes: usar `HorizontalPodAutoscaler` con dos deployments (stable y canary) y configurar el `weight` en el `Ingress` (nginx o istio) para distribuir el tráfico porcentualmente; las métricas de quality se leen desde el sistema de observabilidad y disparan un rollback automatizado
- A/B testing de modelos: asignar `user_id % 2 == 0` a modelo A y `user_id % 2 == 1` a modelo B, registrar en cada request el modelo usado como metadata, y analizar las métricas de calidad y las métricas de negocio (engagement, resolución en primer contacto) de forma diferencial
- Shadow mode: ejecutar la nueva versión del pipeline en paralelo con la versión de producción sin afectar la respuesta al usuario, comparando las salidas entre versiones para evaluar la nueva antes de cualquier exposición de tráfico real
- Rollback automático basado en métricas: Argo Rollouts (Kubernetes) o AWS CodeDeploy pueden configurarse para monitorear métricas custom (exportadas a Prometheus o CloudWatch) y revertir automáticamente el despliegue cuando una métrica supera un umbral de degradación definido
- Registro de experimentos: cada despliegue canary debe registrarse con `experiment_id`, fechas de inicio y fin, porcentaje de tráfico asignado, modelo/prompt exacto usado, y métricas resultantes para construir un historial de experimentos consultable

## Para recordar

El despliegue gradual no es opcional en sistemas de IA de producción: el comportamiento de un nuevo modelo o prompt sobre el tráfico real nunca se puede predecir completamente con datasets de evaluación offline, y la exposición gradual es el mecanismo que protege a todos los usuarios de una regresión masiva.
