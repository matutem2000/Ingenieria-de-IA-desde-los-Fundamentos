# Módulo 9 – Capítulo 05 – Sección 06

# Cierre: RAG y agentes son multiplicadores de capacidad — y de riesgo

Los sistemas RAG y agénticos representan el salto cualitativo más significativo en la utilidad práctica de los LLMs: RAG permite que el modelo acceda a conocimiento actualizado y específico del dominio; los agentes permiten que el modelo ejecute acciones en el mundo real. Pero este salto en capacidad es también un salto en la superficie de ataque y en el impacto potencial de los ataques: un sistema de chat comprometido genera texto malicioso; un agente comprometido puede exfiltrar bases de datos, modificar registros, enviar emails fraudulentos o ejecutar código en la infraestructura de la empresa. Los principios de seguridad para estos sistemas — tratar todos los datos externos como untrusted, aplicar sandboxing en ejecución de código, implementar autorización granular por operación, y exigir confirmación humana para acciones irreversibles — no son restricciones opcionales sino la diferencia entre un sistema seguro y uno que espera ser comprometido. La adopción de RAG y agentes sin estos controles es equivalente a conectar un sistema con acceso administrativo directamente a internet sin autenticación.

*"With great power comes great attack surface."* — Parafraseando a Simon Willison, creador de Datasette y uno de los investigadores más prolíficos en seguridad de sistemas de IA generativa, sobre el trade-off fundamental entre capacidad y riesgo en sistemas agénticos.

## Conceptos clave del capítulo

- RAG poisoning: inyección de documentos maliciosos en el vectorstore que son recuperados como contexto confiable; el vectorstore requiere controles de acceso, validación de ingestión y auditoría periódica del corpus
- Prompt injection vía RAG indirecto: instrucciones adversariales en documentos recuperados ejecutadas por el modelo como si vinieran del sistema; mitigada marcando documentos recuperados como untrusted y validando el output antes de ejecutar acciones
- Seguridad agéntica: herramientas amplifican el impacto de cualquier ataque; blast radius debe limitarse por diseño mediante mínimo privilegio en cada herramienta
- Sandboxing: ejecución de código en containers Docker aislados con restricciones de red, filesystem y CPU; network proxy de egress para herramientas de acceso web; secrets fuera del contexto del LLM
- Authorization granular: el plano de control valida cada acción contra permisos por operación y recurso específico; human-in-the-loop mandatorio para acciones irreversibles; audit trail completo de todas las invocaciones

## Idea central

RAG y agentes multiplican tanto la utilidad como el riesgo de los sistemas de IA: el diseño seguro de estos sistemas requiere implementar los mismos principios de seguridad —mínimo privilegio, sandboxing, autorización, auditoría— que se aplican a cualquier sistema con acceso a datos sensibles y capacidad de ejecutar acciones con impacto real.
