# Módulo 10 – Capítulo 01 – Sección 05

# El equipo de plataforma de IA: roles, responsabilidades y producto interno

Un equipo de AI Platform Engineering funciona como un equipo de producto interno cuyo cliente son los demás equipos de AI Engineering de la organización, aplicando el principio de Team Topologies donde el equipo de plataforma es un "enabling team" o un "platform team" que reduce la carga cognitiva de los "stream-aligned teams". La composición típica incluye Platform Engineers con experiencia en Kubernetes y cloud (AWS/GCP/Azure), ML Engineers con experiencia en frameworks de entrenamiento y serving, Site Reliability Engineers responsables de los SLOs de la plataforma, y un Developer Experience Engineer que gestiona la documentación, los golden paths y el developer portal en Backstage. El equipo opera el Internal Developer Platform como un producto real: tiene un roadmap trimestral, recoge feedback mediante encuestas de DevEx, mide adoption rate de cada nuevo feature, y establece SLAs de soporte para los equipos consumidores. El modelo de financiación suele ser centralizado (FinOps de plataforma), con chargeback a los equipos usuarios basado en el cómputo y almacenamiento consumido.

## Roles y responsabilidades

- Platform Engineer: diseña y opera la infraestructura de Kubernetes, networking, storage y seguridad que sostiene todos los servicios de la plataforma
- ML Infrastructure Engineer: implementa y mantiene los servicios específicos de ML: training cluster, serving layer, model registry y feature store
- SRE de plataforma: define SLOs, gestiona on-call, conduce postmortems y automatiza runbooks para reducir toil operativo
- Developer Experience Engineer: construye CLIs, SDKs internos, plantillas y documentación; mide el NPS del desarrollador trimestralmente
- Product Manager de plataforma: prioriza el backlog de la plataforma basándose en impacto medido (tiempo ahorrado, incidentes evitados) y mantiene la hoja de ruta visible para todos los equipos

## Para recordar

El equipo de plataforma de IA debe tratarse a sí mismo como un equipo de producto: si sus usuarios internos no adoptan sus herramientas de forma voluntaria, la plataforma ha fallado en su diseño o en su comunicación.
