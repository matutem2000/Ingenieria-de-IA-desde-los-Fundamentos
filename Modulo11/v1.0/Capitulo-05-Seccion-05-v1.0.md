# Módulo 11 – Capítulo 05 – Sección 05

## Rollback de LLM: estrategias para revertir cuando la actualización del modelo degrada calidad

El plan de rollback de LLM es el componente del ciclo de vida del sistema que se documenta con menor rigor y que más se necesita cuando todo lo demás ha fallado. En la mayoría de los equipos, el plan de rollback existe como una sección al final del documento de despliegue que dice algo como "si hay problemas, revertir al modelo anterior". Esta descripción es insuficiente: no especifica qué constituye "problemas" (¿qué threshold de degradación activa el rollback?), no define el mecanismo técnico (¿cómo se cambia el modelo activo — despliegue de código, cambio de configuración, feature flag?), no indica cuánto tiempo toma el rollback en condiciones reales, y no documenta si el plan fue probado antes de que se necesitara en producción.

La primera capa del plan de rollback — y la más simple de implementar — es mantener el modelo anterior disponible y recuperarlo en la configuración del servicio de orquestación sin despliegue de código nuevo. Esto requiere que dos condiciones se cumplan desde el diseño: el endpoint de modelo activo debe ser un valor de configuración (feature flag, variable en el config service) que puede modificarse en tiempo real sin reiniciar el servicio, y el modelo anterior debe seguir siendo accesible — lo que no siempre está garantizado si el proveedor depreca versiones periódicamente.

La segunda capa, más robusta, implementa el **blue-green deployment para LLMs**: mantener dos versiones del servicio de inferencia activas simultáneamente (blue: versión actual en producción, green: versión nueva en validación), con el router de modelos enviando el 100% del tráfico a blue durante el período de validación de green. Cuando se decide promover green a producción, el router cambia el 100% del tráfico a green. Si se detecta una degradación, el rollback es instantáneo: el router vuelve a enviar el 100% a blue. El tiempo de rollback en este modelo es de segundos — el tiempo de propagación del cambio de configuración del router, no el tiempo de despliegue de una nueva imagen Docker.

El **canary rollout con rollback automático** es el mecanismo más sofisticado: desplegar la nueva versión al 5% del tráfico con un sistema de monitoreo que evalúa continuamente las métricas de calidad de la variante nueva versus la actual, y revierte automáticamente al 0% si las métricas de la variante nueva caen más del threshold configurado (por ejemplo, 5% de degradación en el LLM-as-a-judge score promedio de las últimas 100 peticiones). El rollback automático convierte la validación de nuevas versiones de modelos en un proceso continuo y sin riesgo: los usuarios que experimentan la variante nueva están siendo protegidos por el sistema de monitoreo que revertirá la exposición antes de que la degradación sea significativa.

Un aspecto crítico del rollback de LLMs que no existe en el rollback de modelos ML tradicionales es la relación entre el modelo y el prompt. Los prompts están frecuentemente optimizados para la versión específica del modelo con la que fueron desarrollados: un prompt diseñado y refinado para GPT-4 puede no producir el mismo comportamiento con GPT-4o, y viceversa. El plan de rollback del modelo debe incluir el rollback simultáneo al prompt asociado a esa versión del modelo — el prompt registry debe mantener el vínculo entre cada versión de prompt y la versión de modelo para la que fue optimizada.

## Estrategias técnicas de rollback

- **Blue-green deployment para LLMs:** dos versiones del servicio de inferencia activas simultáneamente con conmutación instantánea del router, sin tiempo de despliegue en el rollback — solo tiempo de propagación del cambio de configuración.
- **Canary rollout con rollback automático:** despliegue al 5% del tráfico con monitoreo continuo y rollback automático si las métricas de calidad caen más del threshold, convirtiendo el rollout en un proceso de validación continua con datos reales.
- **Feature flag para versión de modelo:** el modelo activo configurado mediante feature flag (no hardcodeado), con rollback instantáneo modificando una variable de configuración desde el dashboard del sistema de feature flags.
- **Snapshot de prompts asociados al modelo:** cuando se hace rollback del modelo, también se revierte automáticamente al prompt optimizado para esa versión, preservando la coherencia entre el modelo y la estrategia de prompting.
- **Runbook de rollback documentado y practicado:** procedimiento paso a paso con tiempos esperados por etapa (objetivo: rollback completo en menos de 10 minutos), responsables identificados, y criterios de éxito verificables, ejecutado como fire drill trimestral.

---

**Para recordar:** Un plan de rollback que no se ha practicado no es un plan — es una esperanza. Los fire drills regulares de rollback de LLM son tan importantes en LLMOps como los game days en Site Reliability Engineering: revelan los pasos que faltan, los tiempos que se subestimaron, y las dependencias que nadie documentó.

El cierre del capítulo integra los cinco componentes de LLMOps en una visión de sistema: por qué la infraestructura de LLMOps es la diferencia entre un equipo que puede operar sus sistemas de IA con confianza y uno que opera en modo reactivo permanente.
