# Módulo 10 – Capítulo 10 – Sección 01

# Technical debt en plataformas de IA: identificación y gestión planificada

La deuda técnica en plataformas de IA tiene características específicas que la hacen más peligrosa que en aplicaciones de software convencional: un componente de la plataforma con deuda técnica alta (ej. el model registry sin tests automáticos, el feature store sin validación de schema) puede bloquear a múltiples equipos simultáneamente cuando falla, multiplicando el impacto por el número de equipos que dependen de él. Los tipos de deuda técnica más comunes en plataformas de IA incluyen: dependencias de versiones de Python y CUDA sin pinning explícito que se rompen silenciosamente cuando se actualiza el entorno base, falta de tests de integración entre los componentes de la plataforma (registry + serving + monitoring), configuraciones hardcodeadas en vez de paramétrica (ej. el bucket de S3 hardcodeado en 15 scripts distintos), y abstracciones con fugas que exponen detalles de Kubernetes a los consumidores de la plataforma en lugar de encapsularlos. La identificación de deuda técnica en plataformas de IA requiere métricas proxy: número de incidentes causados por componentes específicos (MTTR alto indica falta de observabilidad o de runbooks), tiempo de configuración manual requerido para operaciones rutinarias (indica falta de automatización), y ratio de PRs de "plumbing" vs PRs de nuevas capacidades en el repositorio de la plataforma (un ratio >50% indica acumulación de deuda). La gestión planificada de la deuda sigue el modelo de "tech debt sprints" o "innovation tokens" de Stripe: reservar un porcentaje fijo del capacity del equipo (20-30%) para reducción de deuda, documentado en el roadmap con la misma visibilidad que las nuevas capacidades.

## Tipos de technical debt específicos de plataformas de IA

- Dependency drift: dependencias de Python (transformers, torch, numpy) sin versiones pinned que se rompen con actualizaciones; requiere dependency lockfiles (pip-compile, poetry.lock) y testing automático de compatibilidad
- Observabilidad incompleta: componentes de plataforma sin métricas en Prometheus, sin logs estructurados, o con logs que no incluyen request_id para correlación; detectado cuando el MTTR de incidentes es >30 minutos
- Configuración hardcodeada: valores de configuración (bucket names, endpoint URLs, thresholds) embebidos en el código en lugar de inyectados vía environment variables o ConfigMaps; cada cambio de configuración requiere redeploy
- Abstracciones con fugas: los consumidores de la plataforma necesitan entender detalles de Kubernetes, Helm o AWS IAM para usar las abstracciones; síntoma de que el SDK interno no encapsula suficiente complejidad
- Tests de integración ausentes: los componentes de la plataforma son testeados unitariamente pero no como sistema integrado; los bugs de integración entre registry, serving y monitoring solo se detectan en producción

## Para recordar

La deuda técnica en una plataforma es deuda con interés compuesto: cada mes que pasa sin reducirla, el costo de resolverla aumenta porque más equipos han construido encima de ella asumiendo los comportamientos incorrectos como si fueran el contrato correcto.
