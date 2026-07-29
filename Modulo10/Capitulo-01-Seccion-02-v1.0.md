# Módulo 10 – Capítulo 01 – Sección 02

# El caso de negocio de una plataforma interna: escala, consistencia y reducción de duplicación

Sin una plataforma centralizada, cada equipo de IA tiende a construir su propia infraestructura de entrenamiento, sus propios scripts de despliegue y sus propias soluciones de monitoreo, resultando en deuda técnica multiplicada por el número de equipos. Un análisis de Spotify publicado en su engineering blog identificó que, antes de construir su plataforma interna, más del 60% del tiempo de los ML Engineers se dedicaba a tareas de infraestructura repetitivas en lugar de a la mejora de modelos. El caso de negocio de una plataforma se construye sobre tres ejes medibles: reducción del time-to-production desde experimento hasta endpoint en producción, reducción del costo operativo por modelo desplegado mediante compartición de compute y herramientas, y aumento de la tasa de reutilización de features y componentes entre proyectos. Empresas como Uber (Michelangelo), Airbnb (Bighead) y LinkedIn (Pro-ML) documentaron reducciones de 4x a 10x en el tiempo necesario para llevar un nuevo modelo a producción después de centralizar su infraestructura de ML.

## Métricas que justifican la inversión en una plataforma

- Time-to-production: días desde el merge de un experimento hasta el primer request de producción atendido por el endpoint
- Costo por predicción: compute cost dividido por volumen de inferencias, rastreable por equipo vía resource tagging en AWS Cost Explorer o GCP Billing
- Duplicación de código: número de repositorios privados con implementaciones equivalentes de data loaders, eval harnesses o serving wrappers
- Incident rate causado por configuración: porcentaje de postmortems cuya causa raíz es una configuración de infraestructura inconsistente entre equipos
- Developer satisfaction score (DevEx): encuesta trimestral que mide percepción de productividad de los ingenieros que consumen la plataforma

## Principio rector

El ROI de una plataforma de IA se mide en tiempo de ingeniería recuperado y en incidentes de producción evitados, no en el número de features que la plataforma misma despliega.
