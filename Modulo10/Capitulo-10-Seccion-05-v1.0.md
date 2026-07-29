# Módulo 10 – Capítulo 10 – Sección 05

# Métricas de salud de la plataforma: adoption rate, time-to-deploy y incident rate

Las métricas de salud de una plataforma de IA son los indicadores que permiten al equipo de plataforma evaluar si su producto interno está cumpliendo su misión de multiplicar la productividad de los equipos consumidores, identificar áreas de deterioro antes de que se conviertan en problemas graves, y comunicar objetivamente el valor de la plataforma a la dirección. El conjunto mínimo de métricas de salud incluye: adoption rate (porcentaje de equipos elegibles que usan activamente cada componente de la plataforma, medido mensualmente), time-to-first-deploy para nuevos equipos (tiempo desde que un nuevo equipo empieza a usar la plataforma hasta su primer despliegue en producción exitoso), time-to-deploy para equipos existentes (tiempo medio entre registrar un nuevo modelo en el registry y tenerlo sirviendo en producción), y incident rate (número de incidentes de producción causados por fallas de la plataforma por equipo-mes, distinguiendo entre incidentes de infraestructura de la plataforma y incidentes de los equipos usuarios). La DORA (DevOps Research and Assessment) define cuatro métricas elite para equipos de software (deployment frequency, lead time for changes, change failure rate, MTTR); el equipo de plataforma de IA adapta estas métricas al contexto: deployment frequency de modelos, lead time desde experimento hasta producción, failure rate de deployments de modelos, y MTTR de incidentes de la plataforma.

## Métricas clave de salud de la plataforma

- Adoption rate por componente: porcentaje de equipos elegibles que han usado el componente al menos una vez en los últimos 30 días; medido automáticamente por los logs de uso de la plataforma; target > 80% para componentes maduros
- Time-to-first-deploy (onboarding metric): tiempo en días desde que un nuevo equipo es registrado en la plataforma hasta su primer deployment exitoso; proxy de la calidad del onboarding y la documentación; target < 5 días
- Deployment lead time: tiempo en horas desde que se registra un modelo en el registry hasta que está sirviendo tráfico en producción; incluye el tiempo en review/approval; target < 4 horas para deployments automatizados
- Platform-caused incident rate: número de incidentes donde la plataforma es la causa raíz (no el modelo del equipo consumidor) por mes; target < 1 incident/month; rastreado en el sistema de incidentes con label `caused-by: platform`
- NPS de la plataforma (Developer NPS): Net Promoter Score calculado trimestralmente de la encuesta de DevEx; mide si los ingenieros recomendarían el uso de la plataforma a otros equipos; target > +40 para plataformas maduras

## Para recordar

Las métricas de salud de la plataforma son útiles solo si se rastrean en el tiempo y se comparten públicamente con los equipos consumidores: la transparencia sobre la salud de la plataforma genera confianza, y la confianza genera adopción.
