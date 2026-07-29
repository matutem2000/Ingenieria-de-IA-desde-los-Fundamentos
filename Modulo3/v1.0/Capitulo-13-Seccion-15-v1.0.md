# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 15: Transición al Capítulo 14

La observabilidad da al AI Engineer la capacidad de ver qué ocurre dentro de su sistema de IA. Permite detectar cuando las respuestas son incorrectas, diagnosticar por qué lo son, medir si el sistema mejora o se deteriora con el tiempo, y operar el sistema con intención basada en datos. Es una capacidad indispensable para cualquier sistema de IA en producción.

Pero ver no es lo mismo que proteger.

### El límite de la observabilidad

Todos los modos de degradación que el capítulo describió tienen en común una característica: son el resultado de dinámicas no adversariales. El modelo deriva porque el proveedor actualiza su versión. El contexto se desactualiza porque los procesos de actualización fallan. Los agentes entran en bucles porque sus criterios de terminación están mal definidos. Los usuarios producen tipos de consulta no anticipados porque sus necesidades evolucionan. Ninguno de estos problemas es el resultado de que alguien esté deliberadamente intentando dañar el sistema.

Los sistemas de IA en producción enfrentan también amenazas deliberadas: actores que intentan extraer información que el sistema no debería revelar, manipular el comportamiento del sistema a través de entradas cuidadosamente diseñadas, usar el sistema como vector para ataques contra la organización o sus usuarios, o eludir las restricciones de seguridad y cumplimiento que el sistema debe respetar.

Estas amenazas no son detectables por la observabilidad estándar. Un ataque de prompt injection —donde una entrada maliciosa intenta reescribir las instrucciones del system prompt— puede no producir ninguna alerta de latencia, costo o groundedness. El sistema responde, el contexto está presente, los scores de calidad pueden ser altos. Y sin embargo, el sistema está siendo manipulado de formas que pueden tener consecuencias graves.

### Lo que la seguridad y la gobernanza agregan

El capítulo 14 desarrolla la dimensión de la operación responsable que la observabilidad por sí sola no puede proveer: cómo proteger un sistema de IA de las amenazas deliberadas que caracterizan un entorno adversarial, y cómo estructurar el gobierno de esos sistemas para que operen dentro de los límites legales, éticos y organizacionales que la organización y la regulación exigen.

La seguridad de sistemas de IA tiene un conjunto de vulnerabilidades específicas que no tienen equivalente directo en el software tradicional. Las amenazas de prompt injection, jailbreaking, data poisoning y exfiltración de información del contexto son propias de la arquitectura de los LLMs. Requieren controles específicos de diseño —no solo monitoreo de incidentes— que el AI Engineer debe incorporar en la arquitectura del sistema desde el inicio.

La gobernanza, por su parte, responde a las preguntas sobre quién tiene autoridad para tomar qué decisiones sobre el sistema: quién puede modificar el system prompt de producción, quién aprueba los cambios en la base de conocimiento, quién determina qué casos de uso son apropiados para un sistema de IA y cuáles no, cómo se documenta el razonamiento detrás de las decisiones de diseño para cumplir con los requisitos de explicabilidad que las regulaciones emergentes exigen.

### La relación entre observabilidad y seguridad

Observabilidad y seguridad no son dimensiones independientes. Se refuerzan mutuamente.

La observabilidad es una condición previa para la seguridad operativa: si el sistema de IA no tiene trazabilidad de contexto, un incidente de seguridad —una respuesta que reveló información que no debía, una interacción donde el sistema fue manipulado para producir contenido inapropiado— es imposible de investigar retroactivamente. El equipo de seguridad no puede saber qué ocurrió exactamente, cómo ocurrió, y cuántas veces ocurrió antes de ser detectado.

La seguridad, a su vez, define qué es visible en la observabilidad. Si el sistema de IA maneja datos personales o información corporativa sensible, los datos que se registran en las trazas deben estar sujetos a controles de acceso, cifrado en reposo y políticas de retención que cumplan con las regulaciones aplicables. La observabilidad no puede ser ilimitada en los sistemas que manejan información sensible; debe diseñarse dentro de los límites que la seguridad y la privacidad establecen.

### Lo que el capítulo 14 construye sobre este capítulo

El AI Engineer que llega al capítulo 14 con los conceptos de este capítulo internalizados tiene una ventaja: entiende que las decisiones de seguridad y gobernanza no son restricciones arbitrarias sobre el diseño técnico. Son respuestas a amenazas reales en entornos reales, y deben diseñarse con el mismo rigor que la arquitectura del contexto o el pipeline de observabilidad.

El capítulo 14 estructura esas respuestas: las vulnerabilidades específicas de los sistemas de IA, los controles de diseño que las mitigan, y el marco de gobernanza que permite a las organizaciones operar sistemas de IA dentro de los límites que la responsabilidad empresarial y la regulación exigen.

Ver qué ocurre en el sistema es el primer paso de la operación responsable. Proteger el sistema de lo que puede ocurrir es el segundo. Ambos pasos son necesarios. Ninguno es suficiente sin el otro.
