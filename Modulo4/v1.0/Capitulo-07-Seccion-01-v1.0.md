# Módulo 4 – Capítulo 07 – Sección 01

## Seguridad en Soluciones de IA

Los sistemas de IA introducen una superficie de ataque que no existía en los sistemas de software convencionales. Los mecanismos de seguridad tradicionales — firewall, autenticación, cifrado en tránsito, control de acceso basado en roles — siguen siendo necesarios, pero no son suficientes. Un sistema de IA puede ser comprometido a través de su propio mecanismo de razonamiento: atacando el prompt que guía al modelo, manipulando los documentos que alimentan el sistema de recuperación, o explotando la capacidad del modelo para generar contenido que elude los filtros de seguridad convencionales. Diseñar la seguridad de un sistema de IA requiere comprender estos vectores específicos y sus controles correspondientes.

La referencia de amenazas más completa y actualizada para sistemas de LLM es el **OWASP LLM Top 10**, publicado por el Open Web Application Security Project. Esta lista documenta las diez categorías de vulnerabilidades más críticas en aplicaciones que usan modelos de lenguaje, en orden de prevalencia y impacto. Las categorías más relevantes para el arquitecto incluyen: LLM01 (Prompt Injection), LLM02 (Insecure Output Handling), LLM03 (Training Data Poisoning), LLM06 (Sensitive Information Disclosure), y LLM08 (Excessive Agency). Conocer esta taxonomía proporciona un vocabulario preciso para evaluar el perfil de riesgo de un sistema y comunicar las mitigaciones necesarias al equipo de seguridad.

Los vectores de ataque específicos de sistemas de IA se pueden organizar en tres categorías:

**Ataques al razonamiento del modelo:** acciones que manipulan el comportamiento del LLM para que actúe fuera de sus instrucciones originales. El prompt injection — tanto directo (en la consulta del usuario) como indirecto (en documentos recuperados por el sistema RAG) — es el ataque más frecuente. La ingeniería de jailbreak busca eludir las restricciones del modelo mediante formulaciones específicas de la consulta. La manipulación de contexto busca introducir instrucciones maliciosas en el contexto que el modelo procesa para alterar su output.

**Ataques a los datos del sistema:** acciones que comprometen la información almacenada en la base vectorial, los documentos de conocimiento o el historial de interacciones. La extracción de información sensible mediante consultas diseñadas específicamente para provocar que el modelo cite información confidencial de la base de conocimiento es un riesgo real en sistemas con control de acceso inadecuado.

**Ataques a la cadena de herramientas:** en sistemas de agentes, las herramientas que el agente puede invocar son vectores de ataque. Si un atacante puede manipular el razonamiento del agente para invocar una herramienta con parámetros diseñados maliciosamente — por ejemplo, una herramienta de acceso a base de datos con una query de inyección SQL — el sistema de IA se convierte en un amplificador del ataque.

Los principios de diseño seguro para sistemas de IA son:

- **Seguridad desde el diseño (Security by Design):** las consideraciones de seguridad deben incorporarse en la arquitectura desde el primer día, no añadirse como un layer posterior al desarrollo. Un sistema diseñado sin seguridad requiere una refactorización significativa para añadirla; un sistema diseñado con seguridad puede añadir funcionalidades sin comprometer sus controles.
- **Principio de mínimo privilegio:** cada componente del sistema — el LLM, los agentes, las herramientas — debe tener acceso solo a los recursos estrictamente necesarios para su función. Un agente que solo necesita leer documentación técnica no debe tener acceso a los datos de RR.HH.
- **Defensa en profundidad:** ningún control de seguridad es suficiente por sí solo. Las capas de controles — validación de input, guardrails de output, monitoreo de comportamiento, autenticación de API — se refuerzan mutuamente: si una capa falla, las siguientes deben contener el daño.

Las secciones de este capítulo desarrollan los controles específicos para cada vector: la protección de prompts contra inyección y exfiltración, la seguridad de datos en la base vectorial y los documentos de conocimiento, el control de acceso a modelos y herramientas, y el cumplimiento de seguridad regulatoria. Incorporar seguridad desde la arquitectura resulta considerablemente menos costoso que corregir vulnerabilidades una vez que el sistema está en producción — y exponencialmente menos costoso que responder ante una brecha de seguridad.
