# Módulo 11 – Capítulo 05 – Sección 05

# Rollback de LLM: estrategias para revertir cuando la actualización del modelo degrada calidad

El rollback de LLM en producción enterprise es el proceso más crítico del ciclo de vida del sistema y el más difrecuentemente subestimado en los planes de despliegue: cuando la actualización de un modelo de LLM (cambio de GPT-4 a GPT-4o, actualización del modelo base de un proveedor, o nuevo fine-tune) produce una degradación detectable en métricas de calidad o seguridad, el equipo necesita revertir al comportamiento anterior en minutos, no en horas. La primera capa del plan de rollback es la más simple: mantener el modelo anterior disponible y recuperar su endpoint en la configuración del servicio de orquestación, lo que requiere que el sistema de routing de modelos soporte múltiples versiones simultáneamente y que la configuración del modelo activo sea modificable sin despliegue de código (mediante feature flags o un config service). La segunda capa, más compleja, aplica cuando el rollback no es posible porque el modelo anterior fue deprecado por el proveedor (como ocurrió con la transición de gpt-4 a gpt-4-turbo en OpenAI): en este caso, el plan de rollback debe incluir un modelo alternativo de respaldo (fallback model) que se activa automáticamente cuando el modelo principal no está disponible o su calidad cae por debajo del threshold definido. La detección automática que activa el rollback es tan importante como el mecanismo de rollback en sí: un sistema de alertas que monitorea las métricas de calidad de producción en tiempo real (rolling average de los últimos 100 requests con alertas en Grafana o Datadog cuando la métrica cae un 10% respecto a la baseline) permite detectar regresiones en minutos en lugar de esperar el reporte de un usuario insatisfecho.

## Estrategias técnicas de rollback

- Blue-green deployment para LLMs: mantener dos versiones del servicio de inferencia activas simultáneamente (blue: versión actual, green: versión nueva), con el router enviando el 100% del tráfico a blue durante el período de validación de green
- Canary rollout con rollback automático: desplegar la nueva versión al 5% del tráfico con un sistema de monitoreo que revierte automáticamente al 0% si las métricas de calidad caen más de un umbral configurable (ej. 5% de degradación en LLM-as-a-judge score)
- Feature flag para versión de modelo: el modelo activo se configura mediante un feature flag (no hardcodeado), permitiendo rollback instantáneo modificando una variable de configuración sin despliegue de código
- Snapshot de prompts asociados: cuando se hace rollback del modelo, también se revierte automáticamente a los prompts optimizados para esa versión del modelo (prompts diseñados para GPT-4 pueden no funcionar óptimamente con GPT-4o)
- Runbook de rollback documentado y practicado: procedimiento paso a paso con tiempos esperados por etapa, responsables, y criterios de éxito, ejecutado en un fire drill trimestral para garantizar que funciona cuando se necesita

## Para recordar

Un plan de rollback que no se ha practicado no es un plan — es una esperanza; los fire drills regulares de rollback de LLM son tan importantes en LLMOps como los game days en Site Reliability Engineering.
