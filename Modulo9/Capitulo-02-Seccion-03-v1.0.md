# Módulo 9 – Capítulo 02 – Sección 03

# Jailbreaking: técnicas para eludir las restricciones del system prompt

El jailbreaking es el conjunto de técnicas diseñadas para hacer que un modelo de lenguaje genere outputs que sus controles de seguridad (RLHF, Constitutional AI, instrucciones del sistema) están diseñados para prevenir, sin necesariamente comprometer el sistema prompt directamente. A diferencia de la prompt injection, el jailbreak no busca sobrescribir el sistema prompt sino crear contextos psicológicos, narrativos o lógicos en los que el modelo considera que sus restricciones no aplican. Las técnicas más documentadas incluyen el DAN (Do Anything Now) prompt, el roleplay como "un modelo sin restricciones", la técnica del "abuelo que contaba historias de química para dormir", y ataques de muchos pasos que escalan gradualmente hacia el contenido prohibido. GPT-4, Claude 3 y Gemini Ultra han sido jailbreakeados mediante variantes de estas técnicas, aunque los proveedores los parchean iterativamente. La carrera armamentística entre desarrolladores de jailbreaks y proveedores de modelos es permanente y demuestra que las restricciones basadas únicamente en RLHF son insuficientes.

## Aspectos técnicos

- DAN y variantes: prompts que instruyen al modelo a actuar como una versión de sí mismo "sin restricciones", explotando la tendencia del modelo a seguir el roleplay establecido; variantes incluyen STAN (Strive To Avoid Norms), DUDE, y jailbreaks en idiomas distintos al inglés donde el RLHF es menos robusto
- Many-shot jailbreaking: demostrado por Anthropic en 2024, consiste en incluir decenas o cientos de ejemplos de comportamientos prohibidos en el contexto (few-shot examples) antes del request malicioso, explotando la tendencia del modelo a seguir el patrón del contexto
- Crescendo attack: técnica de Microsoft Research (2024) que incrementa gradualmente la sensibilidad del contenido solicitado en múltiples turnos de conversación, evitando triggers de los filtros que operan a nivel de request individual
- Prompt-level obfuscation: instrucciones codificadas en Base64, ROT13, l33tspeak, o fragmentadas en múltiples mensajes para evadir filtros de contenido basados en pattern matching
- Virtualization y hypothetical framing: "en un universo alternativo donde las IA no tienen restricciones", "imagina que eres un personaje en una novela que explica cómo...", "para fines educativos en un contexto controlado, describe..."

## Para recordar

El jailbreaking demuestra que las restricciones de seguridad basadas exclusivamente en el entrenamiento del modelo son insuficientes: los sistemas en producción necesitan múltiples capas de defensa que incluyan validación semántica del output, independiente del modelo, para detectar contenido prohibido aunque el modelo haya sido manipulado para generarlo.
