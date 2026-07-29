# Módulo 9 – Capítulo 04 – Sección 03

# Red teaming manual: técnicas de adversarios humanos especializados

El red teaming manual sigue siendo insustituible para un subconjunto de vulnerabilidades que los sistemas automatizados no pueden descubrir: aquellas que requieren comprensión cultural profunda, creatividad para construir narrativas adversariales convincentes, conocimiento de dominio especializado (por ejemplo, cómo un médico malicioso pediría información sobre sobredosis), o ataques multi-turn que evolucionan adaptativamente basados en la respuesta del modelo. Los equipos de red teaming humano más efectivos son interdisciplinarios: incluyen expertos en seguridad informática, psicólogos especializados en persuasión y manipulación, expertos en el dominio de la aplicación (medicina, derecho, finanzas), y personas con conocimiento de culturas y contextos específicos donde las restricciones del modelo podrían ser eludidas mediante referencias locales. Anthropic, OpenAI y Google contratan red teamers externos con perfiles muy específicos para evaluar sus modelos antes de cada release, y los hallazgos de estos ejercicios alimentan directamente el proceso de RLHF.

## Aspectos técnicos del red teaming manual

- Técnicas de ingeniería social aplicada al modelo: construir personas adversariales (investigador académico que necesita información sensible, periodista investigando un tema, escritor de ficción), roleplay elaborado con backstory detallado, y escalada gradual (crescendo technique) para reducir la resistencia del modelo paso a paso
- Ataques multilingues y multiculturales: el RLHF de la mayoría de los modelos es más robusto en inglés que en otros idiomas; ataques en árabe, chino mandarín, ruso o idiomas con alfabetos no-latinos pueden eludir restricciones que son efectivas en inglés; el red team debe incluir hablantes nativos de múltiples idiomas
- Ataques de dominio especializado: un experto en química puede construir requests que parecen legítimas en contexto académico pero solicitan información peligrosa; un abogado puede construir argumentos que hacen que el modelo genere advice legal no autorizado; estos ataques requieren conocimiento de dominio que los sistemas automatizados no tienen
- Multi-turn adversarial conversations: ataques que se desarrollan en múltiples turnos, donde cada respuesta del modelo se usa para guiar el siguiente prompt hacia el comportamiento objetivo; requieren adaptabilidad humana en tiempo real que los sistemas automatizados no pueden replicar con la misma efectividad
- Documentación de técnicas: el equipo de red teaming debe mantener un playbook actualizado de técnicas exitosas, incluyendo el prompt exacto, el contexto de conversación previo, el modelo y versión target, y la respuesta obtenida — esta documentación es el activo de seguridad más valioso del ejercicio

## Para recordar

El red teaming manual es la única metodología que descubre las vulnerabilidades más sofisticadas y contextualmente específicas de un sistema de IA, especialmente aquellas que requieren creatividad adversarial, conocimiento de dominio especializado, o comprensión cultural que los sistemas automatizados no pueden emular.
