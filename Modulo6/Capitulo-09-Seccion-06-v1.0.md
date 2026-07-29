# Módulo 6 – Capítulo 09 – Sección 06

# Cierre: la optimización de RAG es un proceso continuo de medición y ajuste

La optimización de un sistema RAG de producción no tiene un punto final: el corpus evoluciona con nuevos documentos y formatos, la distribución de queries cambia con el tiempo a medida que los usuarios descubren nuevos casos de uso, los modelos de embedding y de generación se actualizan con versiones que tienen perfiles de rendimiento distintos, y los SLOs de calidad se vuelven más exigentes a medida que los usuarios elevan sus expectativas. Los equipos que tratan la optimización de RAG como un proyecto con fin determinado tipicamente experimentan una curva de calidad que sube durante el desarrollo inicial, se estabiliza en el lanzamiento y luego decrece silenciosamente en los meses siguientes por la acumulación de corpus drift, modelo drift y query drift no detectados. La diferencia entre los sistemas RAG que mantienen calidad en producción durante meses y años versus los que se degradan no está en la sofisticación de las técnicas de recuperación sino en la existencia de procesos de medición continua: un golden dataset actualizado trimestralmente, un pipeline de evaluación automatizado que corre en CI/CD, dashboards de monitoring con alertas calibradas y un equipo con ownership claro sobre las métricas de calidad del sistema. La optimización de RAG es una práctica de ingeniería de calidad aplicada a sistemas de IA, no un conjunto de técnicas que se aplican una vez.

*"En Dios confiamos; todos los demás deben traer datos."* — W. Edwards Deming, pionero del control estadístico de calidad en procesos industriales; principio igualmente aplicable a la optimización de sistemas de AI Engineering.

## Principio rector

Institucionalizar la medición continua de calidad del sistema RAG con el mismo rigor que se aplica al monitoring de disponibilidad y latencia; sin métricas de calidad automatizadas, la degradación del sistema es invisible hasta que los usuarios lo reportan.
