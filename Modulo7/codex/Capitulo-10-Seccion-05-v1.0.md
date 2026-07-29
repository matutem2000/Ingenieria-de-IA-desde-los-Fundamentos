# Módulo 7 – Capítulo 10 – Sección 05

# Mejora continua: aprender de los fallos del agente en producción

Los fallos del agente en producción son la fuente más valiosa de información para mejorar el sistema: representan casos reales del dominio de aplicación donde el agente no satisfizo las expectativas del usuario, con contexto completo (input real, trayectoria real, output real) que no puede simularse perfectamente en un entorno de evaluación controlado. El pipeline de mejora continua basado en fallos de producción sigue un ciclo: identificar fallos (mediante señales explícitas como thumbs-down del usuario, feedback de texto, o señales implícitas como abandono de sesión, repetición de la misma pregunta), categorizar los fallos por tipo (razonamiento incorrecto, herramienta incorrecta, información desactualizada, fallo de herramienta sin recuperación), analizar las causas raíz en un subconjunto anotado, proponer una intervención (cambio de prompt, nueva herramienta, ajuste de descripción de herramienta, fine-tuning), implementar la intervención y medir su impacto en el test set y en producción.

## Aspectos técnicos

- **Recolección de señales de fallo**: implementar múltiples mecanismos de captura: feedback explícito del usuario (rating, thumbs up/down, texto libre), detección automática de señales implícitas (el usuario repite la misma pregunta reformulada en la misma sesión, el agente llega a max_steps sin completar), y monitoreo de métricas que se degradan (TCR cae por debajo del umbral, latencia P95 aumenta)
- **Categorización de fallos con LLM-judge**: para escalar el análisis de fallos, usar un LLM-judge que categoriza automáticamente cada fallo reportado según un taxonomy predefinida: reasoning_error, wrong_tool_selection, tool_execution_failure, context_window_overflow, hallucination, prompt_injection, user_misunderstanding
- **Root cause analysis (RCA) de fallos sistémicos**: cuando la misma categoría de fallo aparece en >5% de las sesiones, escalar a una RCA formal; revisar manualmente 20-50 casos, identificar el patrón común, y proponer una hipótesis de causa raíz que sea testeable con un experimento controlado
- **A/B testing de mejoras**: antes de desplegar una mejora (cambio de prompt, nueva herramienta) al 100% del tráfico, desplegarlo a un 10-20% y medir el impacto sobre las métricas de evaluación en producción; revertir si el cambio no mejora o degrada otras métricas
- **Dataset de fallos como activo estratégico**: el conjunto de fallos categorizados y anotados de producción es el activo más valioso para el entrenamiento y fine-tuning futuro del agente; almacenarlo en un formato estructurado (task, expected_output, actual_output, failure_category, root_cause) para facilitar su uso en ciclos de mejora futuros

## Para recordar

Los fallos del agente en producción no son fracasos del sistema; son el dataset de entrenamiento del próximo ciclo de mejora: cada fallo bien diagnosticado y categorizado es una oportunidad de hacer el agente más robusto ante esa clase de situación.
