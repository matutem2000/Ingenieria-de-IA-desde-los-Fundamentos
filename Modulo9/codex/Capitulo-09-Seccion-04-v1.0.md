# Módulo 9 – Capítulo 09 – Sección 04

# NIST AI RMF: marco de gestión de riesgos de IA del gobierno de Estados Unidos

El NIST AI Risk Management Framework (AI RMF 1.0, publicado en enero 2023) es el marco de gestión de riesgos de IA desarrollado por el National Institute of Standards and Technology del gobierno de EE.UU. que se está convirtiendo en el estándar de facto para organizaciones en el sector privado y gubernamental americano, y que complementa al EU AI Act para organizaciones que operan en ambos mercados. El AI RMF está organizado en dos partes: el Core (el marco conceptual sobre riesgo de IA) y los Profiles (adaptaciones específicas por sector o caso de uso). El Core define cuatro funciones interdependientes: GOVERN (establecer la cultura, políticas y procesos de gestión de riesgo), MAP (identificar y categorizar los riesgos de IA en el contexto de uso), MEASURE (cuantificar y monitorear los riesgos identificados) y MANAGE (responder a los riesgos identificados mediante mitigaciones, transferencia o aceptación). El AI RMF es voluntario (no tiene fuerza de ley como el EU AI Act) pero su adopción es esperada por reguladores sectoriales (FDA para dispositivos médicos con IA, NHTSA para vehículos autónomos) y por el gobierno federal en sus requisitos de contratación.

## Aspectos técnicos

- Función GOVERN: establecer políticas internas de gestión de riesgo de IA, definir roles y responsabilidades (AI Risk Owner, Data Steward, Model Validator), crear un comité de revisión de IA, y establecer procesos de escalation para sistemas de alto riesgo; equivale al AI Governance del Capítulo 1 del libro pero con estructura específica del NIST
- Función MAP: categorizar el sistema de IA según el dominio de aplicación, los usuarios afectados, y el nivel de autonomía del sistema; identificar las consecuencias potenciales de fallas (daño físico, daño financiero, discriminación, violación de privacidad); mapear al OWASP LLM Top 10 y MITRE ATLAS para amenazas específicas de IA
- Función MEASURE: definir métricas cuantificables para los riesgos identificados — por ejemplo, tasa de false positives del clasificador de contenido dañino, tiempo medio de detección de jailbreaks en producción, coverage porcentual del red teaming contra el threat model, y tasa de accuracy del modelo degradada por perturbaciones adversariales
- Función MANAGE: implementar y documentar controles de mitigación para riesgos priorizados; mantener un risk register actualizado con riesgo residual documentado; establecer procesos de revisión periódica (trimestral) del risk profile del sistema; y documentar las decisiones de aceptación de riesgo para riesgos no mitigados con justificación explícita
- AI RMF Playbook: NIST publicó el AI RMF Playbook (nist.gov/system/files/documents/2023/01/26/NIST.AI.100-1.pdf) con sugerencias específicas de acción para cada subcategoría del framework; es la guía de implementación más detallada disponible para equipos que quieren adoptar el AI RMF

## Para recordar

El NIST AI RMF proporciona el vocabulario y la estructura de proceso para gestionar el riesgo de IA de forma sistemática —GOVERN, MAP, MEASURE, MANAGE— y aunque es voluntario en EE.UU., su adopción se está convirtiendo en el estándar esperado para sistemas de IA en sectores regulados como salud, finanzas y gobierno federal.
