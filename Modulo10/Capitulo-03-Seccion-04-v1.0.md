# Módulo 10 – Capítulo 03 – Sección 04

# Versionado semántico de modelos: cuándo es un patch, un minor o un major release

Aplicar versionado semántico (SemVer: MAJOR.MINOR.PATCH) a modelos de ML requiere adaptar las convenciones de software a las características propias de los modelos: a diferencia de una librería de software donde el contrato es la API pública, en un modelo el contrato incluye la arquitectura, el input schema, el output schema, y las distribuciones de predicción esperadas. Un cambio de **PATCH** (1.0.0 → 1.0.1) corresponde a ajustes que no cambian el comportamiento observable del modelo: corrección de un bug en el pre/postprocessing, reentrenamiento con datos adicionales que mejora métricas sin cambiar la arquitectura, o actualización de dependencias de serving sin cambiar el modelo en sí. Un cambio de **MINOR** (1.0.0 → 1.1.0) corresponde a mejoras backward-compatible: fine-tuning con nueva tarea manteniendo el mismo input/output schema, expansión del vocabulario que no rompe inferencias existentes, o mejora de latencia por quantización sin degradación de calidad. Un cambio de **MAJOR** (1.0.0 → 2.0.0) indica cambios breaking: cambio de arquitectura base (de BERT a RoBERTa), cambio en el input schema (nuevos campos obligatorios), cambio en la distribución de outputs que requiere recalibración de los sistemas downstream, o cambio en el idioma o dominio del modelo.

## Puntos críticos del versionado semántico de modelos

- PATCH release: reentrenamiento incremental (mismo arquitectura, mismos hiperparámetros, datos adicionales), bugfix en pre/postprocessing, actualización de dependencias de runtime sin cambio de modelo
- MINOR release: fine-tuning que añade capacidades nuevas sin romper las existentes, mejora de latencia por optimización (quantización, pruning, distilación) con degradación de calidad dentro de tolerancia
- MAJOR release: cambio de arquitectura base, cambio en el input schema (ej. añadir campo obligatorio), cambio en el output schema, cambio en el idioma/dominio que invalida evaluaciones previas
- Comunicación de breaking changes: notificación con mínimo 30 días de antelación a los equipos consumidores, con guía de migración específica y período de soporte del modelo anterior en paralelo
- Automated compatibility testing: test suite que verifica que el nuevo modelo (en Staging) produce outputs dentro de umbrales aceptables comparado con el modelo en Production antes de autorizar la promotion

## Para recordar

La versión de un modelo es un contrato con los sistemas que lo consumen: incrementar el MAJOR sin notificar y proveer guía de migración es equivalente a introducir un breaking change silencioso en una librería de software.
