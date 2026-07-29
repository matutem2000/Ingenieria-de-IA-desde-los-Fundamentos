# Capítulo 09 — Arquitecturas Multiagente

## Sección 05 — Coordinación, comunicación y protocolos

La topología define la estructura del sistema. La comunicación es lo que hace que esa estructura funcione. Dos sistemas con topologías idénticas pueden tener comportamientos radicalmente distintos si sus mecanismos de comunicación difieren. Y los errores de comunicación entre agentes —mensajes malformados, mensajes perdidos, mensajes entregados en el orden incorrecto— son una de las causas más frecuentes de fallo en sistemas multiagente en producción.

Esta sección desarrolla cómo se comunican los agentes: qué formatos de mensaje funcionan, qué modelos de comunicación existen y cuándo usar cada uno, y cómo diseñar la comunicación de forma que los errores sean detectables y recuperables.

### El mensaje como unidad fundamental

En un sistema multiagente, toda interacción entre agentes ocurre a través de mensajes. Un mensaje es una unidad de información que un agente envía a otro, con la intención de transferir datos, solicitar una acción o reportar un resultado. Que el mensaje viaje directamente de un agente a otro, a través de un bus de mensajes, o mediante un estado compartido es un detalle de implementación. Lo que no es un detalle es el contenido y la estructura del mensaje.

Un mensaje bien diseñado tiene cuatro componentes:

**El tipo:** qué clase de mensaje es. Un mensaje puede ser una tarea (solicitud de que el agente receptor ejecute algo), un resultado (output de una tarea completada), un error (reporte de que algo falló), o un estado (actualización sobre el progreso de una tarea en curso). El tipo determina cómo el agente receptor debe procesar el mensaje.

**El identificador:** un identificador único que permite correlacionar un resultado o un error con la tarea que lo originó. Sin identificador, un sistema que ejecuta múltiples tareas en paralelo no puede saber a qué solicitud corresponde cada respuesta.

**El payload:** el contenido propio del mensaje. Para una tarea, el payload es la descripción de la tarea a ejecutar con todos los datos que el agente receptor necesita. Para un resultado, el payload es el output estructurado de la tarea. Para un error, el payload es la descripción del error con suficiente contexto para que el agente coordinador pueda decidir cómo responder.

**Los metadatos:** información de contexto que el agente receptor puede necesitar sin que sea parte del payload principal. El agente de origen, la marca temporal, la prioridad, el número de reintentos realizados.

### Formatos de mensaje: texto natural vs. estructura formal

Una decisión de diseño frecuente en sistemas multiagente es si los mensajes entre agentes deben estar en lenguaje natural o en un formato estructurado como JSON.

El lenguaje natural entre agentes parece intuitivo: los modelos de lenguaje son buenos procesando texto. El problema es que introduce ambigüedad donde se necesita precisión. Cuando el agente A le dice al agente B "analiza el documento y dime qué encontraste", el agente B necesita inferir qué tipo de análisis, con qué criterios, en qué formato debe devolver el resultado. Si ese análisis es parte de un sistema automatizado donde el output del agente B será procesado por el agente C programáticamente, la variabilidad en el formato del output puede romper el procesamiento.

Los mensajes estructurados en JSON eliminan esa ambigüedad. Un mensaje que especifica `{"tarea": "analisis_sentimiento", "texto": "...", "categorias": ["positivo", "negativo", "neutro"], "formato_salida": "json_con_puntuacion"}` no deja lugar a interpretación. El agente receptor sabe exactamente qué debe hacer, con qué datos y en qué formato debe responder.

La regla práctica: usa lenguaje natural cuando el receptor es humano. Usa formatos estructurados cuando el receptor es otro agente o código que procesará el resultado. Esta regla no impide que un agente procese texto en lenguaje natural como parte del payload —puede hacerlo— pero los metadatos, el tipo, el identificador y los parámetros de la tarea deben estar en formato estructurado.

### Comunicación síncrona vs. asíncrona

El modelo síncrono de comunicación funciona así: el agente A envía un mensaje al agente B y espera. No hace nada más hasta recibir la respuesta. El modelo asíncrono funciona así: el agente A envía un mensaje al agente B, continúa su propio procesamiento, y maneja la respuesta del agente B cuando esta llega, sin haber bloqueado su ejecución en el intervalo.

La elección entre ambos modelos depende de si el agente A necesita el resultado del agente B para continuar su propio trabajo:

**Comunicación síncrona:** cuando el agente A no puede avanzar sin el resultado del agente B. El orquestador que espera el resultado de todos los agentes especializados antes de sintetizar la respuesta final opera de forma síncrona con cada agente en el sentido de que necesita todos los resultados para producir la síntesis.

**Comunicación asíncrona:** cuando el agente A puede continuar con otras tareas mientras el agente B trabaja. Un agente investigador que lanzó cinco búsquedas en paralelo no tiene razón para bloquear su ejecución esperando la primera: puede continuar otras actividades y procesar las respuestas a medida que llegan.

Los sistemas reales con frecuencia combinan ambos modelos: el orquestador lanza todas las tareas de forma asíncrona (no espera a que la primera termine para lanzar la segunda), pero luego espera de forma síncrona hasta tener todos los resultados antes de sintetizar.

### El bus de mensajes y el estado compartido

Hay dos mecanismos fundamentales para implementar la comunicación entre agentes:

**El bus de mensajes (message bus):** los agentes publican mensajes en un canal compartido y se suscriben a los canales que les interesan. Un agente que completa una tarea publica el resultado en el canal de resultados. El agente que inició la tarea escucha ese canal y procesa el resultado cuando llega. El bus de mensajes desacopla a los agentes: el emisor no necesita saber quién va a procesar su mensaje, y el receptor no necesita saber quién lo originó.

**El estado compartido (shared state store):** existe un almacén de estado centralizado al que todos los agentes tienen acceso de lectura y escritura. Los agentes leen el estado para obtener contexto, ejecutan su trabajo y escriben sus resultados en el estado. Otros agentes leen esos resultados y actúan sobre ellos. El estado compartido hace que toda la información del sistema esté en un lugar, lo que facilita la visibilidad y la depuración, pero introduce problemas de concurrencia que la sección 07 trata con detalle.

En la práctica, muchos sistemas combinan ambos: el bus de mensajes para la coordinación de tareas (quién debe hacer qué) y el estado compartido para los datos de larga duración (el contexto acumulado que todos los agentes necesitan consultar).

### Diseño para la resiliencia comunicacional

Un mensaje que llega mal formado, que nunca llega, o que llega dos veces son escenarios que el sistema debe manejar sin colapsar. El diseño de comunicación resiliente implica:

**Validación en la entrada:** cada agente que recibe un mensaje debe validar su estructura y contenido antes de procesarlo. Un mensaje que no cumple el esquema esperado debe rechazarse inmediatamente con un mensaje de error claro, no intentar procesarse de forma tolerante.

**Idempotencia:** si un mensaje se entrega dos veces —por un error del sistema de mensajería— el procesamiento debe producir el mismo resultado en ambas entregas. La idempotencia se logra verificando el identificador del mensaje antes de procesarlo: si ya fue procesado, el resultado se devuelve sin reejecutar el trabajo.

**Confirmación de recepción:** el emisor de un mensaje debe poder saber si el receptor lo recibió y lo procesó. Sin confirmación, un fallo silencioso puede dejar al emisor esperando indefinidamente un resultado que nunca llegará.

**Timeouts:** todo mecanismo de espera debe tener un tiempo máximo. Un agente que espera una respuesta que nunca llega debe tener un timeout después del cual reporta el error y permite que el sistema decida cómo continuar.

---

*La sección 06 toma los mecanismos de comunicación de esta sección y los examina desde la perspectiva del control: cómo un agente planificador descompone las tareas del sistema, y cómo un agente supervisor garantiza la calidad de los resultados. Estos dos roles —planificador y supervisor— son los que elevan un conjunto de agentes a un sistema cohesivo.*
