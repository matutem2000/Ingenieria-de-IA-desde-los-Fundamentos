# Capítulo 09 — Arquitecturas Multiagente

## Sección 11 — Laboratorio práctico

Este laboratorio es un ejercicio de diseño arquitectónico. No requiere código. Requiere aplicar los criterios, patrones y principios desarrollados en las secciones anteriores para diseñar un sistema multiagente completo para un caso de negocio real.

El objetivo del laboratorio no es producir el diseño perfecto en el primer intento. Es desarrollar el proceso de pensamiento que un AI Engineer necesita para abordar sistemáticamente el diseño de un sistema multiagente: hacer las preguntas correctas, en el orden correcto, y tomar decisiones explícitas con sus fundamentos.

### El escenario

Una empresa de medios digitales publica artículos de análisis económico y financiero para una audiencia de ejecutivos y analistas. El equipo editorial actualmente produce doce artículos por semana, con un proceso que incluye investigación de fuentes, análisis de datos, redacción, verificación de hechos y revisión editorial.

El director editorial quiere un sistema de IA que pueda producir borradores de artículos a partir de un brief editorial breve. El brief especifica el tema, la audiencia objetivo, los puntos principales que el artículo debe cubrir, las fuentes que el equipo ya identificó como relevantes y la extensión aproximada.

El output esperado es un borrador de artículo completo, estructurado, con datos verificados y fuentes citadas, listo para revisión editorial humana. La revisión humana es obligatoria: el sistema no publicará directamente. Pero la calidad del borrador debe ser suficientemente alta para que la revisión sea un proceso de refinamiento, no de reescritura.

El equipo editorial producirá un mínimo de tres briefs por día hábil. Cada artículo tiene entre 800 y 1.500 palabras.

### Estructura del ejercicio

El estudiante debe producir un documento de diseño que incluya los siguientes elementos, en orden:

**1. Análisis de justificación**

Responde las cuatro preguntas de la sección 02 para este escenario específico:

- ¿Hay subtareas independientes que se benefician del paralelismo? ¿Cuáles son?
- ¿Los distintos aspectos de la tarea requieren especialización fundamentalmente distinta? ¿En qué dominios?
- ¿La criticidad del output justifica verificación independiente? ¿Por qué sí o por qué no?
- ¿El volumen de información puede exceder la ventana de contexto de un agente único? ¿En qué condiciones?

La respuesta a cada pregunta debe incluir el razonamiento, no solo la conclusión.

**2. Definición de agentes**

Para cada agente del sistema, especifica:

- Nombre del agente y su rol funcional.
- Alcance funcional: qué hace y qué no hace.
- Herramientas que necesita (búsqueda web, acceso a bases de datos específicas, herramientas de cómputo, etc.).
- Un párrafo que describe su instrucción de sistema en términos generales: qué objetivos tiene, qué restricciones aplican, qué formato de output produce.

El número de agentes no está predefinido. El estudiante decide cuántos son necesarios con base en el análisis de la tarea.

**3. Topología del sistema**

Dibuja (o describe en texto con suficiente detalle para que pueda dibujarse) el diagrama de topología del sistema:

- Cada agente, representado como un nodo con su nombre y rol.
- Las conexiones entre agentes, con la dirección del flujo de información (quién le envía qué a quién).
- El orden de ejecución: qué agentes actúan en paralelo, qué agentes actúan en secuencia, qué dependencias existen entre ellos.

**4. Protocolo de comunicación**

Para las tres conexiones más importantes del sistema (las que tienen mayor impacto en la calidad o el rendimiento):

- El formato del mensaje que fluye por esa conexión (descripción del esquema JSON o del formato elegido).
- Si la comunicación es síncrona o asíncrona, y por qué.
- Qué debe hacer el receptor si el mensaje llega malformado o si el emisor no responde dentro del tiempo esperado.

**5. Estrategia de memoria compartida**

Describe el almacén de estado del sistema:

- Qué información se guarda en el estado compartido.
- Qué información permanece local a cada agente.
- Cómo se resuelven los conflictos de escritura simultánea (si existen en tu diseño).
- Qué información persiste después de que la tarea termina y cuál se descarta.

**6. Manejo de fallos**

Para cada uno de estos escenarios de fallo, describe qué debe hacer el sistema:

- El agente de búsqueda de fuentes no encuentra ninguna fuente relevante.
- El agente verificador de datos detecta que una afirmación del borrador no puede ser verificada.
- El agente redactor produce un output que no cumple el esquema de formato esperado.
- El sistema recibió dos briefs simultáneamente y los recursos están al límite.

**7. Estimación de costo y latencia**

Estima, con los supuestos que consideres razonables y que debes explicitar:

- Tiempo total esperado para producir un borrador de 1.200 palabras.
- Número aproximado de llamadas al modelo de lenguaje que realiza el sistema para esa tarea.
- Los dos factores que más influyen en el costo del sistema y cómo podrían optimizarse si el presupuesto fuera restrictivo.

### Criterios de evaluación del diseño

Un buen diseño en este laboratorio tiene las siguientes características:

- Los roles de los agentes son claros, no solapados y necesarios: no sobran agentes ni faltan.
- La topología elegida es coherente con la naturaleza de las subtareas (paralelas o secuenciales).
- Los protocolos de comunicación están definidos con suficiente precisión para ser implementables sin ambigüedad.
- El manejo de fallos es explícito y cubre los escenarios más probables, no solo el caso nominal.
- Las decisiones de diseño tienen fundamentos articulados: cuando hay varias opciones posibles, el diseño elige una y explica por qué.

Un diseño que cumple estas características demuestra que el estudiante puede tomar las decisiones arquitectónicas que un sistema multiagente real requiere. No demuestra que ese sea el único diseño correcto: hay múltiples diseños válidos para el mismo problema. Lo que distingue un buen diseño es la coherencia entre el problema, las decisiones tomadas y los fundamentos que las sustentan.

### Variante de extensión

Para quienes quieran profundizar el ejercicio, la variante de extensión plantea el siguiente desafío adicional:

El director editorial quiere que el sistema pueda aceptar un artículo publicado anteriormente por un competidor como referencia de estilo y tono. El sistema debe producir borradores que se acerquen al estilo del artículo de referencia sin copiar su contenido.

¿Cómo modifica esta nueva funcionalidad el diseño del sistema? ¿Requiere un agente adicional? ¿Cambia la instrucción de sistema del agente redactor? ¿Qué parte del estado compartido necesita actualizarse?

---

*La sección 12 provee la checklist operativa que consolida los criterios de decisión, los requisitos de diseño y las verificaciones de calidad de este capítulo en un formato accionable para el trabajo diario del AI Engineer.*
