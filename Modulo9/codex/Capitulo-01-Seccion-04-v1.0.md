# Módulo 9 – Capítulo 01 – Sección 04

# Modelado de amenazas para aplicaciones de IA: STRIDE y AI-specific frameworks

STRIDE —Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege— es el framework de threat modeling más ampliamente adoptado en la industria, desarrollado por Microsoft, y su aplicación a sistemas de IA requiere extensiones específicas para cubrir las amenazas que emergen del comportamiento no determinista del modelo. El marco MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) complementa STRIDE con tácticas, técnicas y procedimientos (TTPs) específicos para sistemas de ML, categorizados en una matriz análoga a MITRE ATT&CK pero orientada a IA. OWASP LLM Top 10 proporciona una lista priorizada de vulnerabilidades específicas de LLMs que debe integrarse en cualquier ejercicio de threat modeling para aplicaciones basadas en modelos de lenguaje. La combinación de STRIDE + ATLAS + OWASP LLM Top 10 constituye el estándar de facto para threat modeling de sistemas de IA en 2024-2025.

## Componentes del modelado de amenazas para IA

- STRIDE aplicado a LLMs: Spoofing del identity del sistema vía prompt injection, Tampering de outputs vía manipulación del contexto, Repudiation por falta de logs inmutables de inferencia, Information Disclosure vía prompt leaking o memorización, DoS vía context-flooding, y Elevation of Privilege vía jailbreak
- MITRE ATLAS TTPs: las 14 tácticas incluyen ML Attack Staging, Model Evasion, Model Theft, y Data Poisoning; cada táctica tiene técnicas documentadas con ejemplos reales de ataques en producción
- Data Flow Diagrams (DFD) para IA: el DFD debe incluir el modelo como componente con trust boundaries explícitos entre usuario, gateway, LLM, vectorstore y herramientas externas
- AI-specific trust boundaries: el prompt del usuario, los documentos recuperados por RAG, los resultados de herramientas y el historial de conversación tienen trust levels diferentes que deben modelarse explícitamente
- Threat enumeration sistematizada: aplicar STRIDE a cada cruce de trust boundary en el DFD genera una lista completa de amenazas que puede priorizarse con DREAD (Damage, Reproducibility, Exploitability, Affected users, Discoverability) o CVSS adaptado

## Buena práctica

El threat model de un sistema de IA debe actualizarse cada vez que se agrega una nueva herramienta al agente, se cambia el modelo base o se expande el corpus del vectorstore, porque cada cambio introduce nuevas superficies de ataque que invalidan el modelo de amenazas anterior.
