# Módulo 10 – Capítulo 10 – Sección 02

# Migraciones de modelos: actualizar modelos sin interrumpir a los equipos usuarios

Una migración de modelo es el proceso de reemplazar un modelo en producción por una nueva versión (ya sea un patch minor, una actualización de arquitectura, o un cambio de proveedor) de forma que los equipos consumidores del endpoint no experimenten interrupciones de servicio, degradaciones de calidad inesperadas, ni necesiten cambios en su código. Las estrategias de migración dependen del tipo de cambio: para migraciones de PATCH y MINOR (sin cambios breaking en el schema de API), se usa despliegue rolling o blue-green con el mismo endpoint URL, los consumidores no necesitan hacer nada, y el rollback es inmediato volviendo al modelo anterior; para migraciones de MAJOR (con cambios breaking), se despliega el nuevo modelo en un endpoint con versión explícita (`/v2/completions`), se notifica a los consumidores con al menos 30 días de antelación, se ofrece un período de coexistencia de ambas versiones, y se depreca la versión anterior solo cuando todos los consumidores han migrado. Los mecanismos técnicos de migración segura incluyen: shadow mode (el nuevo modelo procesa todos los requests en paralelo con el modelo actual pero sus respuestas no se retornan al usuario, solo se comparan métricas), canary deployment (el 5-10% del tráfico se dirige al nuevo modelo y se comparan métricas entre ambos antes de aumentar el porcentaje), y feature flags (el equipo consumidor puede activar el nuevo modelo para sus usuarios beta antes del rollout general).

## Etapas de una migración de modelo segura

- Preparación: publicar el nuevo modelo en Staging con documentation completa de cambios, guía de migración si hay breaking changes, y período de disponibilidad en staging para que los equipos consumidores hagan testing
- Shadow mode (opcional para cambios mayores): el nuevo modelo sirve el 100% del tráfico en shadow, sin retornar respuestas al usuario; métricas de calidad, latencia y costo se comparan automáticamente durante 24-72 horas
- Canary rollout: 5% → 10% → 25% → 50% → 100% del tráfico, con períodos de observación de 24-48 horas entre cada paso; rollback automático si las métricas de producción se degradan >N% respecto al baseline
- Monitoring intensivo post-migración: durante las primeras 48 horas post-migración completa, reducir los umbrales de alerta al 50% de los valores normales para detectar degradaciones sutiles antes de que escalen
- Deprecación del modelo anterior: período de retención del endpoint del modelo anterior (normalmente 30 días post-migración completa) para que los equipos rezagados puedan migrar; luego se archiva en el registry y se elimina el endpoint

## Buena práctica

La mejor migración de modelo es aquella que los equipos consumidores no notan porque fue completamente transparente: la inversión en infrastructure de shadow mode y canary deployment se amortiza en la confianza que genera en los equipos usuarios de la plataforma.
