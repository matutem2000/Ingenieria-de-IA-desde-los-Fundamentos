# Módulo 9 – Capítulo 02 – Sección 06

# Cierre: prompt injection es el SQL injection de los sistemas de IA

La analogía entre prompt injection y SQL injection no es solo retórica: ambas son vulnerabilidades de inyección que surgen de mezclar datos con instrucciones en el mismo canal sin separación criptográfica, y ambas fueron subestimadas inicialmente por la industria hasta convertirse en vectores de ataque masivos en producción. SQL injection devastó aplicaciones web durante los años 2000 porque los developers concatenaban strings de usuario directamente en queries SQL; prompt injection impacta aplicaciones de IA porque los developers concatenan inputs de usuario directamente en contextos de LLM. La solución para SQL injection fue parametrizar las queries —separar el código SQL de los datos mediante un mecanismo que el motor de base de datos entiende como límites infranqueables—; la solución estructural para prompt injection requerirá mecanismos análogos a nivel de arquitectura de LLMs. Hasta que esos mecanismos estén disponibles y ampliamente adoptados, la defensa en profundidad mediante validación de input, separadores estructurales, modelos de clasificación especializados y privilege separation es el estándar de la industria.

*"The most dangerous code in the world is the code that handles attacker-controlled input."* — Michal Zalewski (lcamtuf), investigador de seguridad y autor de "The Tangled Web", resumiendo el principio que unifica SQL injection, XSS y prompt injection como instancias del mismo problema fundamental.

## Conceptos clave del capítulo

- Prompt injection directa: el usuario inyecta instrucciones en su input para sobrescribir el system prompt; mitigada con instrucciones de refuerzo y separación de roles en la API del modelo
- Prompt injection indirecta: instrucciones maliciosas en documentos RAG, páginas web o emails que el agente procesa como contexto confiable; mitigada tratando todos los datos externos como untrusted
- Jailbreaking: técnicas narrativas, de roleplay y many-shot para eludir restricciones del modelo sin inyección directa; requiere validación semántica del output independiente del modelo
- Prompt leaking: extracción del system prompt confidencial mediante requests directos o indirectos; mitigada no incluyendo credenciales en el system prompt y validando outputs que contengan el texto del mismo
- Defensa multicapa: LlamaGuard + separadores estructurales + instrucciones de refuerzo + output validation + privilege separation es el stack mínimo de defensa para aplicaciones de IA en producción

## Idea central

Prompt injection es la vulnerabilidad más prevalente en sistemas de IA en 2024-2025 y ninguna solución aislada la elimina: la defensa efectiva requiere múltiples capas de control independientes aplicadas antes, durante y después de la inferencia del modelo.
