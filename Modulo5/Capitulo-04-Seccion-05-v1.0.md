# Módulo 5 – Capítulo 04 – Sección 05

# Feature flags y despliegue gradual de capacidades de IA

Los feature flags (también llamados feature toggles) permiten activar o desactivar capacidades de IA en producción sin hacer un nuevo despliegue de código, habilitando estrategias de rollout gradual como canary releases (exponer al 5% de usuarios, luego al 25%, 50%, 100%), A/B testing de diferentes prompts o modelos, y rollback instantáneo ante degradación de calidad. Herramientas como LaunchDarkly, Unleash (open source), Flagsmith o AWS AppConfig almacenan la configuración de los flags en un backend centralizado y la distribuyen a los servicios vía SDK con latencia de actualización de segundos, sin requerir redeploy. En el contexto de IA, los feature flags tienen casos de uso específicos: desactivar un agente autónomo que está tomando decisiones erróneas, cambiar el modelo de `gpt-4o` a `claude-3-5-sonnet` para un segmento de usuarios, activar una capacidad experimental de análisis de documentos para usuarios beta, o redirigir el tráfico a un sistema de fallback cuando el proveedor primario tiene degradación. La granularidad del flag es clave: flags por usuario, por plan de suscripción, por región geográfica o por porcentaje de tráfico son estrategias diferentes con implementaciones distintas.

## Aspectos técnicos del despliegue gradual con feature flags

- Implementación con Unleash: `client.is_enabled("ai-agent-v2", context={"userId": user_id, "properties": {"plan": user.plan}})` retorna bool; el contexto de evaluación permite targeting por atributos del usuario sin modificar el código del flag
- Rollout porcentual: configurar el flag para que el 10% de los `user_id` (hasheados) reciban la nueva experiencia garantiza distribución determinista (el mismo usuario siempre recibe el mismo tratamiento) y reproducibilidad de experimentos
- Circuit breaker via feature flag: monitorear métricas de calidad (tasa de respuestas incorrectas, latencia P99) y desactivar el flag automáticamente via API del sistema de feature flags cuando una métrica supera un umbral, sin intervención manual
- Flags de configuración de modelo: en lugar de hardcodear el modelo en el código, leer `config.get("llm_model", "claude-3-5-sonnet-20241022")` del sistema de flags permite cambiar el modelo sin redeploy, con audit trail de quién hizo el cambio y cuándo
- Testing de flags: implementar tests unitarios que ejerciten ambas ramas de cada flag (flag habilitado y deshabilitado) para evitar que el código del flag deshabilitado se deteriore silenciosamente hasta que se necesite para un rollback

## Para recordar

Los feature flags son la herramienta de resiliencia más rápida para sistemas de IA en producción: un rollback via flag tarda segundos mientras que un rollback via redeploy puede tardar minutos, y en una degradación activa cada segundo cuenta.
