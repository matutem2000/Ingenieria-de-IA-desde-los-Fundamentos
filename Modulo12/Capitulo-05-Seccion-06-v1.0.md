# Módulo 12 – Capítulo 05 – Sección 06

# Cierre: un sistema de IA sin hardening es un prototipo — no un producto en producción

La seguridad de un sistema de IA en producción no se agrega al final del proyecto como una capa de barniz — se diseña desde el threat model inicial, se implementa como controles concretos y verificables, y se valida mediante red teaming sistemático antes de cada despliegue. El proyecto final demuestra este ciclo completo: threat model STRIDE documentado en el ADR-004, controles implementados en tres capas (input validation, prompt hardening, output filtering), autorización a nivel de herramientas agénticas que filtra automáticamente por permisos del usuario, y red teaming de 50 ataques con documentación de resultados. La seguridad del sistema se mide con la misma precisión que su calidad RAG: tasa de bypass de prompt injection, tasa de accesos no autorizados, PII detectada en outputs y tiempo de detección ante ataques DoS. Un sistema que no puede auditarse ante un incidente de seguridad no cumple los requisitos mínimos de un producto en producción.

## Aspectos técnicos que integra este capítulo

- Threat model STRIDE con amenazas específicas de sistemas RAG agénticos y nivel de riesgo por amenaza
- Controles anti-injection: delimitadores XML, lista negra de patrones, clasificador de intent y sanitización de documentos
- RBAC a nivel de herramientas: allowed_document_types del JWT aplicado como filtro automático en cada query a Qdrant
- Input validation multicapa: schema Pydantic + lista negra + clasificador de intent antes de procesar cada query
- Red teaming documentado: 50 ataques en 4 categorías con tasa de bypass objetivo < 5% y bypasses como regresiones

## Para recordar

El hardening de un sistema de IA es un proceso continuo, no un hito de proyecto — cada nueva capacidad del sistema introduce nuevas superficies de ataque que deben modelarse y mitigarse.

*"Security is always excessive until it's not enough." — Robbie Sinclair, Head of Security, Country Energy*
