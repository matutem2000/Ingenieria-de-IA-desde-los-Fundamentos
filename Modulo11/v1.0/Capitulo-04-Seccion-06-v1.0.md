# Módulo 11 – Capítulo 04 – Sección 06

## Cierre: el multi-tenancy en IA exige aislamiento técnico riguroso en cada capa del stack

Una plataforma multi-tenant de IA que no puede garantizar el aislamiento riguroso de datos entre tenants no puede operar en sectores regulados, no puede firmar los DPAs que los clientes enterprise exigen, y expone a la organización a responsabilidades legales en caso de un incidente de cross-tenant data access. Esta restricción no es negociable: a diferencia de otros aspectos del diseño donde los trade-offs son continuos y reversibles, el aislamiento de datos en multi-tenancy es una propiedad que el sistema tiene o no tiene — y cuando no la tiene, el descubrimiento del fallo ocurre típicamente en el peor momento posible.

El conjunto de controles técnicos cubiertos en este capítulo — los tres modelos de tenancy con sus trade-offs explícitos, el cifrado por tenant con CMKs revocables, la separación de índices vectoriales mediante namespaces y Row Level Security, el rate limiting distribuido con Redis y Token Bucket, la personalización dinámica con el tenant configuration service, y el cost allocation por inferencia — constituyen el mínimo técnico para operar una plataforma multi-tenant de IA con datos sensibles en un contexto enterprise. La conexión con el Capítulo 06 de este módulo es directa: cuando se implemente el RAG empresarial multi-tenant, el aislamiento de índices vectoriales descrito aquí es exactamente el mecanismo que garantiza que el permission-aware retrieval del RAG funciona correctamente — los documentos de un tenant solo pueden ser recuperados en el contexto de ese tenant.

El aislamiento no es un estado binario sino un espectro, y cada capa adicional de aislamiento reduce el riesgo pero aumenta el costo operacional y la complejidad del sistema. El modelo Bridge — pool para tenants estándar, silo para tenants Enterprise — es la solución que equilibra el espectro de manera pragmática para la mayoría de los casos enterprise: permite operar eficientemente el 80% del catálogo de tenants mientras ofrece las garantías de aislamiento más fuertes para el 20% que las requiere contractualmente. La decisión sobre el nivel de aislamiento apropiado debe tomarse explícitamente, documentarse en la arquitectura de referencia del sistema, y revisarse periódicamente a medida que crece el número de tenants y cambia su perfil de cumplimiento.

El siguiente capítulo lleva el foco al ciclo de vida operacional de los LLMs: cómo se evalúan continuamente, cómo se versionan y despliegan los prompts como artefactos de ingeniería, y cómo se planifican y ejecutan los rollbacks cuando una actualización del modelo degrada la calidad del sistema.

---

*"La seguridad no es un producto sino un proceso: el aislamiento multi-tenant debe diseñarse, implementarse, monitorearse y auditarse continuamente, porque los atacantes no descansan."* — Bruce Schneier, criptógrafo y experto en seguridad informática
