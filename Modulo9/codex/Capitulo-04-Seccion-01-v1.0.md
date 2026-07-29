# Módulo 9 – Capítulo 04 – Sección 01

# Qué es el red teaming de IA: ataque estructurado para encontrar vulnerabilidades

El red teaming de IA es un proceso de evaluación adversarial en el que un equipo de personas o sistemas automatizados adopta el rol de un atacante para identificar vulnerabilidades, comportamientos no deseados y fallas de seguridad en un sistema de IA antes de que lo haga un adversario real en producción. A diferencia de las pruebas unitarias, de integración o de evaluación de calidad convencionales, el red teaming parte de la perspectiva del adversario: no busca verificar que el sistema funciona correctamente en condiciones normales, sino encontrar las condiciones anormales, el inputs edge-case, y las secuencias de interacción que hacen que el sistema se comporte de maneras no autorizadas, dañinas o que violan sus especificaciones de seguridad. OpenAI, Anthropic y Google realizan red teaming extensivo de sus modelos antes de cada release público, y el AI Safety Framework de la Casa Blanca (Executive Order on AI, octubre 2023) establece la obligatoriedad de red teaming para modelos frontier antes de su despliegue. El red teaming manual y el automatizado son complementarios: los humanos encuentran vulnerabilidades creativas e inesperadas; los sistemas automatizados cubren el espacio de amenazas a escala.

## Componentes principales del red teaming de IA

- Objetivo del red team: encontrar vulnerabilidades de seguridad (prompt injection, jailbreak, exfiltración de datos), comportamientos dañinos (generación de contenido peligroso, desinformación), y fallas de alineación (el modelo hace lo que dice el usuario, no lo que el diseñador del sistema pretendía)
- Alcance del ejercicio: definir el threat model (quién es el adversario, con qué motivación y recursos), los sistemas incluidos (modelo base, fine-tuning, RAG, herramientas del agente), y los criterios de éxito para un ataque (qué outputs se consideran vulnerabilidades reportables)
- Diferencia con penetration testing clásico: el pentesting busca vulnerabilidades en código, configuración y red; el red teaming de IA busca comportamientos adversariales del modelo — la "vulnerabilidad" no está en el código sino en las representaciones aprendidas del modelo y en el diseño del sistema de prompts
- Tipos de ejercicio: red teaming de safety (el modelo genera contenido dañino), red teaming de security (el sistema es comprometido por un atacante), red teaming de alineación (el modelo no hace lo que el operador intendió), y red teaming de privacidad (datos sensibles son extraídos o expuestos)
- Integración con el ciclo de desarrollo: el red teaming debe ocurrir antes de cada release de modelo o capacidad nueva, antes de desplegar nuevas herramientas en agentes, y periódicamente en producción para detectar drifts de comportamiento o nuevas técnicas de ataque

## Para recordar

El red teaming de IA es la única metodología que descubre vulnerabilidades que no pueden anticiparse mediante análisis estático o testing funcional: es la respuesta de la industria al hecho de que el comportamiento de un LLM ante inputs adversariales no puede predecirse completamente sin exploración adversarial activa.
