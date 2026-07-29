# Módulo 9 – Capítulo 01 – Sección 06

# Cierre: la seguridad en IA comienza por entender que el modelo es también una superficie de ataque

La seguridad en sistemas de IA no es una extensión de la seguridad de aplicaciones tradicionales: es una disciplina nueva que requiere reconceptualizar qué significa "atacar" un sistema cuando el componente central —el modelo— no ejecuta código determinista sino que genera outputs probabilísticos basados en instrucciones en lenguaje natural. Un firewall de red no puede bloquear un prompt injection; un WAF tradicional no entiende la semántica de un jailbreak; un IDS convencional no detecta model extraction a través de patrones de consulta. Los fundamentos establecidos en este capítulo —superficie de ataque expandida, taxonomía de amenazas, CIA Triad reinterpretada, threat modeling con STRIDE+ATLAS, y responsabilidad compartida— son el marco conceptual sobre el cual se construyen todos los controles técnicos de los capítulos siguientes. Sin este marco, los controles se aplican de forma ad hoc y dejan brechas sistemáticas que los atacantes explotan de manera predecible.

*"Security is a process, not a product."* — Bruce Schneier, criptógrafo y experto en seguridad, en su ensayo seminal sobre la naturaleza de la seguridad en sistemas complejos.

## Conceptos clave del capítulo

- Superficie de ataque de IA: incluye pesos del modelo, prompts, vectorstores, tool interfaces y pipelines de entrenamiento — todas superficies sin equivalente en sistemas tradicionales
- Taxonomía operativa: OWASP LLM Top 10 + MITRE ATLAS como vocabulario común para describir y priorizar amenazas en sistemas de IA
- CIA Triad extendida: confidencialidad del modelo (memorización), integridad del comportamiento (backdoors) y disponibilidad ante prompt-DoS son dimensiones nuevas de seguridad
- Threat modeling iterativo: STRIDE aplicado a DFDs con trust boundaries explícitos entre capas del sistema de IA, actualizado con cada cambio de capacidad
- Responsabilidad compartida clara: el proveedor del modelo protege los pesos; el desarrollador protege todo lo demás — confundir estos límites es la fuente de la mayoría de las vulnerabilidades en producción

## Idea central

Entender la seguridad en IA como una disciplina específica —no como una extensión de la seguridad web— es el prerequisito para construir sistemas que resistan ataques reales en producción.
