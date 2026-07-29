# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 02: Amenazas específicas para LLM y agentes

La superficie de ataque de un sistema de Context Engineering es diferente a la de una aplicación web convencional. No es mejor ni peor en términos absolutos, pero es distinta: incluye vectores que el software tradicional no tiene, y algunos vectores clásicos directamente no aplican o aplican de manera diferente.

Esta sección cataloga las amenazas más relevantes para los sistemas basados en LLMs y agentes, con énfasis en aquellas que se originan en la forma en que el contexto se construye, se transmite y el modelo lo procesa. Las amenazas de infraestructura general —ataques de red, robo de credenciales de acceso a bases de datos, vulnerabilidades en sistemas operativos— son reales en cualquier sistema y deben tratarse con las prácticas estándar de seguridad de infraestructura; no son el foco de este capítulo.

### La superficie de ataque del Context Engineering

Para catalogar las amenazas, es útil partir del flujo de datos en un sistema de Context Engineering completo. En un ciclo típico de solicitud-respuesta, la información fluye de la siguiente manera:

1. El usuario envía un mensaje.
2. El sistema recupera contexto relevante: documentos del sistema RAG, historial de conversación, estado del agente.
3. El sistema construye el contexto completo: system prompt, contexto recuperado, herramientas disponibles, mensaje del usuario.
4. El contexto completo se envía al modelo.
5. El modelo genera una respuesta o decide ejecutar una herramienta.
6. Si ejecuta una herramienta, los resultados se añaden al contexto y el ciclo puede continuar.
7. La respuesta final llega al usuario.

Cada paso de este flujo es una superficie de ataque potencial. Las amenazas específicas del CE atacan distintos puntos de ese flujo.

### Amenaza 1: Prompt injection

El prompt injection es la amenaza más característica de los sistemas basados en LLMs. Consiste en incluir instrucciones en el contexto —ya sea en el mensaje del usuario, en documentos recuperados por RAG o en resultados de herramientas— con la intención de modificar el comportamiento del modelo más allá de lo que el diseñador del sistema autorizó.

Esta amenaza merece una sección propia por su importancia y complejidad. La siguiente sección la desarrolla en profundidad.

### Amenaza 2: Extracción del system prompt

El system prompt contiene las instrucciones de comportamiento del sistema: el rol del agente, las restricciones que debe respetar, el tono que debe mantener y, en algunos sistemas, lógica de negocio sensible o referencias a procedimientos internos.

Un usuario puede intentar extraer el contenido del system prompt mediante técnicas de elicitación: pedir al modelo que "repita sus instrucciones", que "traduzca sus instrucciones a otro idioma", que "describa cómo fue configurado" o que responda preguntas cuya respuesta implique revelar partes del prompt. Los modelos modernos tienen cierta resistencia a la extracción directa, pero no son inmunes, especialmente si el system prompt no fue diseñado con esta amenaza en mente.

La extracción del system prompt puede parecer inofensiva —"el usuario solo conoce las instrucciones"— pero en sistemas empresariales puede exponer flujos de trabajo internos, nombres de sistemas y bases de datos, criterios de clasificación de clientes o referencias a políticas de negocio que la organización prefiere no revelar.

### Amenaza 3: Jailbreaking

El jailbreaking es el intento de conseguir que el modelo ignore sus restricciones de comportamiento mediante técnicas de reencuadre, manipulación narrativa o explotación de inconsistencias en su entrenamiento.

Las técnicas más comunes incluyen: solicitar al modelo que actúe en un juego de roles donde las restricciones no aplican, pedir respuestas "hipotéticas" o "educativas" sobre comportamientos prohibidos, construir solicitudes en pasos pequeños donde ningún paso individual parece problemático pero la secuencia completa lleva a un resultado no autorizado, y explotar inconsistencias entre el system prompt y el entrenamiento base del modelo.

Para el AI Engineer, el jailbreaking es una amenaza difícil de eliminar completamente porque depende parcialmente del comportamiento del modelo base, que el ingeniero no controla. Los controles disponibles se centran en el diseño del system prompt, la validación de salidas y la detección de patrones de intento.

### Amenaza 4: Extracción de datos a través del contexto

En sistemas de múltiples usuarios, el contexto de un usuario puede contener datos de otro usuario si el sistema de aislamiento no está correctamente implementado. Un atacante puede intentar extraer datos del contexto de otras sesiones mediante preguntas que fuercen al sistema a revelar información que no debería estar disponible en esa sesión particular.

Esta amenaza es especialmente relevante en sistemas de RAG con documentos multiusuario: si el índice vectorial no aplica filtros de autorización por usuario, una consulta puede recuperar documentos de otros usuarios. Y si la memoria del agente no está correctamente aislada por sesión, el historial de un usuario puede filtrarse a la sesión de otro.

### Amenaza 5: Uso excesivo de herramientas (tool misuse)

Los agentes con acceso a herramientas —ejecutar código, enviar correos, modificar bases de datos, llamar APIs externas— tienen una superficie de ataque adicional: alguien que logra influir en el comportamiento del agente puede dirigirlo a ejecutar acciones no autorizadas.

El tool misuse puede ser consecuencia de un prompt injection exitoso: el atacante incluye instrucciones que llevan al agente a llamar una herramienta con parámetros maliciosos. Pero también puede ocurrir sin un atacante externo, si el diseño del sistema permite que un usuario legítimo induzca al agente a ejecutar herramientas de formas no previstas.

La característica más peligrosa de esta amenaza es su irreversibilidad: a diferencia de una respuesta de texto que simplemente puede ignorarse, una herramienta que borra datos, envía comunicaciones o autoriza transacciones produce efectos en el mundo real que pueden ser difíciles o imposibles de revertir.

### Amenaza 6: Ataques a la cadena de suministro del contexto

Un sistema de RAG recupera documentos de repositorios, bases de conocimiento y fuentes externas. Si esas fuentes pueden ser modificadas por un atacante —ya sea porque el atacante tiene acceso directo a ellas o porque el sistema indexa contenido público que el atacante puede controlar—, el atacante puede inyectar instrucciones maliciosas en los documentos que el sistema RAG recuperará y añadirá al contexto del modelo.

Este ataque, conocido como prompt injection indirecto, es más peligroso que el directo porque el atacante no necesita acceso al usuario del sistema: solo necesita poder modificar algún documento en el corpus que el sistema RAG indexa. Un documento de ayuda en un portal empresarial, una página de un proveedor en una base de conocimiento o un artículo en un repositorio de políticas pueden convertirse en vectores de ataque si el sistema los recupera y los incluye en el contexto sin inspección.

### Amenaza 7: Degradación adversarial del modelo

En sistemas que incorporan feedback del usuario para ajustar el comportamiento —sistemas con aprendizaje en línea o ajuste fino continuo—, un atacante puede enviar feedback falso deliberadamente para degradar el comportamiento del modelo en una dirección específica. Esta amenaza es más sofisticada y requiere acceso sostenido al sistema, pero es relevante en sistemas de larga duración con loops de aprendizaje.

### Priorización de amenazas para el Context Engineering

No todas las amenazas tienen la misma probabilidad ni el mismo impacto en todos los sistemas. Para el AI Engineer que diseña un sistema de Context Engineering empresarial, la priorización recomendada es la siguiente:

**Alta prioridad:** prompt injection (directo e indirecto), extracción de datos a través del contexto, tool misuse. Estas tres amenazas son las más probables en sistemas con usuarios externos y herramientas habilitadas, y sus consecuencias pueden ser severas.

**Media prioridad:** extracción del system prompt, jailbreaking. Son amenazas frecuentes pero su impacto depende de cuánta información sensible contiene el system prompt y de qué restricciones impone el modelo.

**Prioridad contextual:** ataques a la cadena de suministro del contexto (relevante si el sistema RAG indexa fuentes externas o controladas por terceros), degradación adversarial (relevante si el sistema tiene loops de aprendizaje en producción).

### Nota del arquitecto

El catálogo de amenazas de sistemas de IA está en evolución permanente. El OWASP Top 10 para LLMs —publicado en 2023 y actualizado anualmente— es la referencia más accesible y actualizada para el AI Engineer que necesita un marco de amenazas reconocido. El AI Engineer no necesita memorizar todas las amenazas posibles; necesita entender la lógica de cada clase de ataque para poder identificar instancias específicas en sus propios sistemas.

La siguiente sección analiza el prompt injection en profundidad: los dos tipos, cómo funcionan en la práctica y qué controles de diseño reducen el riesgo.
