# Módulo 9 – Capítulo 09 – Sección 06

# Cierre: el cumplimiento regulatorio es el piso mínimo de seguridad, no el techo

Los marcos regulatorios —EU AI Act, GDPR, HIPAA, NIST AI RMF— establecen el piso mínimo de controles de seguridad que cualquier sistema de IA debe implementar para operar legalmente en sus respectivas jurisdicciones, pero cumplir con estos requisitos no garantiza que el sistema sea seguro contra adversarios sofisticados ni que esté protegido ante amenazas emergentes que los reguladores aún no han anticipado. Los ataques de prompt injection, jailbreaking avanzado, y técnicas de model extraction de vanguardia no están explícitamente cubiertos en HIPAA ni en el AI Act porque los reguladores legislan sobre amenazas conocidas, no sobre el estado del arte de la investigación adversarial. Un equipo de AI Engineering que trata el compliance regulatorio como el objetivo de seguridad en lugar del piso mínimo construirá un sistema que puede aprobar una auditoría de ISO 27001 y aun así ser vulnerado mediante un ataque de RAG poisoning que ninguna regulación actual contempla explícitamente. El verdadero objetivo de seguridad es construir un sistema resiliente ante la amenaza real, y el compliance es una consecuencia necesaria pero insuficiente de ese objetivo.

*"Compliance is not security. Meeting a checklist tells you where you were last year — not where the attackers are today."* — Mikko Hyppönen, Chief Research Officer de WithSecure y uno de los investigadores de ciberseguridad más reconocidos mundialmente, sobre la diferencia fundamental entre compliance y seguridad operacional real.

## Conceptos clave del capítulo

- EU AI Act: clasificación por riesgo (inaceptable/alto/limitado/mínimo) con aplicación a la aplicación completa, no solo al modelo base; requisitos técnicos de high-risk systems incluyen risk management system, data governance, robustez y human oversight
- GDPR en IA: base legal por cada finalidad de procesamiento, minimización activa de datos en logs, machine unlearning para el derecho al olvido, BAAs con proveedores de cloud, transferencias internacionales via SCCs
- HIPAA en IA: Technical Safeguards para PHI (access control, audit controls, integrity, transmission security), de-identificación Safe Harbor o Expert Determination, BAA con todos los proveedores de nube que acceden a PHI
- NIST AI RMF: framework voluntario GOVERN-MAP-MEASURE-MANAGE adoptado como estándar de facto en EE.UU.; proporciona vocabulario y estructura de proceso para gestión sistemática de riesgos de IA
- Control matrix: mapeo explícito de requisito regulatorio → control técnico → evidencia de implementación; documento vivo, versionado en git, actualizado semestralmente y ante cambios en guidance regulatorio

## Idea central

El compliance regulatorio es el piso que la ley exige y no el techo que la seguridad requiere: los mejores equipos de AI Engineering construyen primero el sistema más seguro posible basado en el threat model real, y luego verifican que ese sistema también satisface los requisitos regulatorios — no al revés.
