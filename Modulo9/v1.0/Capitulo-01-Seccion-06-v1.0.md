# Módulo 9 – Capítulo 01 – Sección 06

## Cierre: la seguridad en IA comienza por entender que el modelo es también una superficie de ataque

La seguridad en sistemas de IA no es una extensión de la seguridad de aplicaciones web: es una disciplina que requiere reconceptualizar qué significa "atacar" un sistema cuando el componente central no ejecuta código determinista sino que genera outputs probabilísticos basados en instrucciones en lenguaje natural. Un firewall de red no puede bloquear un prompt injection porque el payload malicioso llega dentro de texto semánticamente válido en el protocolo HTTP. Un WAF tradicional no detecta un jailbreak porque la "firma" del ataque no está en los bytes de la request sino en la intención comunicada en el lenguaje natural. Un IDS convencional no identifica model extraction porque los patrones de queries que recopilan el comportamiento del modelo son indistinguibles, en la capa de red, de un usuario que simplemente hace muchas preguntas.

Esta asimetría entre las herramientas de seguridad disponibles y la naturaleza de las amenazas específicas de IA es la razón por la que el módulo comienza con un capítulo conceptual antes de entrar en controles específicos. Los fundamentos establecidos aquí —superficie de ataque expandida que incluye el modelo, el vectorstore, el pipeline de fine-tuning y el serving layer; taxonomía de amenazas en cinco categorías (input, model, supply chain, data, infrastructure); CIA Triad reinterpretada para cubrir la memorización del modelo, la integridad del comportamiento y el prompt-DoS; threat modeling con STRIDE y ATLAS sobre DFDs con trust boundaries explícitas; y modelo de responsabilidad compartida con tres capas— son el marco conceptual sobre el que se construyen todos los controles técnicos de los capítulos siguientes.

Sin este marco, los controles se aplican de forma ad hoc: se añade un guardrail aquí porque hubo un incidente, se endurece el rate limiting allá porque un cliente se quejó, se añade logging cuando un regulador lo exige. El resultado es un sistema con controles desconectados que dejan brechas sistemáticas que los adversarios explotan de manera predecible, precisamente porque los equipos sin marco conceptual tienden a proteger las mismas superficies visibles mientras ignoran las mismas superficies invisibles. El Capítulo 02 entra de inmediato en la amenaza de mayor prevalencia en producción —prompt injection directa e indirecta— armados con el mapa conceptual que este capítulo ha establecido.

## Conceptos clave del capítulo

- **Superficie de ataque de IA:** incluye pesos del modelo, prompts, vectorstores, tool interfaces, pipelines de entrenamiento y serving layer (vLLM, TGI, Triton), todas superficies sin equivalente directo en sistemas de software tradicional.
- **Taxonomía operativa de amenazas:** cinco categorías (input, model, supply chain, data, infrastructure) que mapean a capas específicas del sistema y a controles en esas capas; OWASP LLM Top 10 y MITRE ATLAS como vocabulario común.
- **CIA Triad extendida:** confidencialidad del modelo (memorización de PII del corpus de pretraining), integridad del comportamiento (backdoors que no corrompen bytes pero sí el comportamiento), y disponibilidad ante prompt-DoS (context-flooding con ventanas de 128k tokens).
- **Threat modeling iterativo:** STRIDE aplicado a DFDs con trust boundaries explícitas entre las capas del sistema de IA, actualizado obligatoriamente ante cada cambio de capacidad, mantenido como código versionado en el repositorio del proyecto.
- **Responsabilidad compartida clara:** el proveedor del modelo protege los pesos y el alignment; la plataforma de serving protege la infraestructura; el desarrollador protege todo lo demás —el system prompt, los guardrails adicionales, la validación de inputs y outputs, el logging, el manejo de PII.

## Idea central

Entender la seguridad en IA como una disciplina específica —no como una extensión de la seguridad web— es el prerequisito para construir sistemas que resistan ataques reales en producción. Los controles que funcionan para APIs REST convencionales son necesarios pero no suficientes: los sistemas de IA requieren controles adicionales específicos para las amenazas que emergen del comportamiento probabilístico del modelo, de la semántica del lenguaje natural como vector de ataque, y de la naturaleza de los datos que fluyen por el pipeline.

---

*"Security is a process, not a product."* — Bruce Schneier, criptógrafo y autor de "Secrets and Lies", articulando el principio que unifica todos los controles de este módulo: la seguridad no es un estado que se alcanza con la instalación del producto correcto, sino un proceso continuo de evaluación, mejora y adaptación ante adversarios que también evolucionan.
