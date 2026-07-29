# Módulo 5 – Capítulo 06 – Sección 05

# Rollback automático basado en métricas de calidad

El rollback automático en sistemas de IA requiere una definición precisa de qué métricas monitoreables en producción constituyen una señal de degradación, con qué umbral y con qué latencia de detección: un sistema que tarda 4 horas en detectar una degradación de calidad ya habrá expuesto a miles de usuarios a respuestas incorrectas. Las métricas más efectivas para triggers de rollback automático son las que combinan señales de calidad del modelo con señales de comportamiento del usuario: tasa de thumbs-down o feedback negativo explícito (signal directo de calidad), tasa de abandono de sesión conversacional (proxy de insatisfacción), tasa de llamadas de seguimiento inmediatas sobre la misma pregunta (señal de respuesta insuficiente), y métricas de evaluación automática online (LLM-as-judge en tiempo real sobre una muestra del tráfico). La implementación técnica del rollback automático sigue el patrón: métricas a Prometheus → alertas en Alertmanager con regla de degradación → notificación al sistema de CD (Argo Rollouts, Spinnaker, o script de AWS SDK) → rollback al deployment anterior via `kubectl rollout undo` o reconfiguración del feature flag.

## Puntos críticos del rollback automático

- Definición de umbrales de rollback: umbrales que disparan el rollback deben ser definidos antes del despliegue (no después), en reunión con producto y negocio; un umbral muy sensible dispara rollbacks falsos, un umbral muy permisivo permite degradaciones prolongadas
- Ventana de observación: los primeros 5-15 minutos de un canary release tienen métricas ruidosas por bajo volumen; el sistema de rollback debe esperar una ventana de confianza estadística mínima (N requests o N minutos) antes de evaluar el trigger
- Rollback de prompts vs rollback de código: un sistema de feature flags permite revertir la versión del prompt en segundos sin hacer rollback del código del servicio; separar estos dos planos de rollback reduce el tiempo medio de recuperación (MTTR)
- Post-mortem de rollback: cada rollback automático debe generar automáticamente un issue en el sistema de tracking con las métricas que dispararon el rollback, el timestamp exacto, el modelo/prompt de la versión revertida, y los pasos de diagnóstico sugeridos
- Testing del mecanismo de rollback: el rollback automático debe testarse en staging deliberadamente: desplegar una versión intencionalmente degradada, verificar que el sistema la detecta dentro de la ventana esperada y ejecuta el rollback correctamente

## Principio rector

Un sistema de rollback automático que nunca se ha testado no es un sistema de rollback: es un script que no se sabe si funcionará en el momento en que más se necesita, que es siempre un momento de alta presión operacional.
