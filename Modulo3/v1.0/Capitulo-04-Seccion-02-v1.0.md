# Capítulo 04 — Sección 02

# La memoria humana como inspiración

La psicología cognitiva distingue varios sistemas de memoria en los seres humanos, cada uno con características propias de almacenamiento, duración y función. Esta distinción no es solo académica: cuando empezamos a diseñar sistemas de IA que necesitan recordar, descubrimos que la taxonomía cognitiva mapea con sorprendente precisión sobre los problemas de arquitectura que tenemos que resolver.

No estamos diciendo que la IA funciona como el cerebro humano. No lo hace. Estamos usando la taxonomía cognitiva como andamiaje conceptual porque es una de las pocas formas que tenemos de nombrar con precisión las diferencias entre tipos de información que los sistemas de IA necesitan gestionar de maneras fundamentalmente distintas.

## Los cuatro tipos de memoria y su equivalente en IA

### Memoria de trabajo

En la cognición humana, la memoria de trabajo es el espacio mental activo donde procesamos la información en este momento. Tiene capacidad limitada —se estima entre 4 y 7 elementos simultáneos—, se volatiliza rápidamente cuando no se le presta atención, y es el escenario de todo razonamiento consciente.

En los sistemas de IA, el equivalente exacto es la **ventana de contexto**. Todo lo que el modelo puede "pensar" en este momento está dentro de esa ventana. Tiene un límite de tokens. Su contenido desaparece cuando termina la sesión. Y es el lugar donde ocurre el razonamiento del modelo.

Este equivalente no es metafórico: es funcional. Cuando diseñamos la ventana de contexto —qué incluir, en qué orden, con qué formato— estamos literalmente diseñando la memoria de trabajo del sistema.

### Memoria episódica

La memoria episódica almacena eventos específicos con su contexto temporal: "la reunión del martes", "la llamada de ayer con el cliente", "lo que acordamos en el sprint anterior". Es personal, situada en el tiempo, y permite reconstruir secuencias de eventos.

En los sistemas de IA, la **memoria conversacional persistida** cumple esta función. Son los registros de interacciones pasadas que el sistema puede consultar para entender la historia de su relación con el usuario: qué se discutió, qué decisiones se tomaron, qué problemas surgieron. Una base de datos de conversaciones estructuradas, un historial de acciones ejecutadas por un agente, un log de tareas completadas —todos son formas de memoria episódica artificial.

La característica clave es que estos registros son **situados en el tiempo y en el evento**. No es conocimiento general: es "esto pasó, en este contexto, en este momento".

### Memoria semántica

La memoria semántica almacena conocimiento general sobre el mundo: hechos, conceptos, relaciones entre ideas. No está ligada a un evento específico —no recordamos cuándo aprendimos que París es la capital de Francia—, sino que representa conocimiento descontextualizado y disponible para su uso general.

En los sistemas de IA, la **memoria semántica** corresponde al conocimiento estructurado sobre el dominio, el usuario o la organización que el sistema acumula a través del tiempo. No es "en la sesión del martes el usuario dijo X" sino "el usuario trabaja en el sector financiero, prefiere respuestas sintéticas, y tiene expertise en derivados de renta fija". Es el perfil destilado, el conocimiento factual sobre el dominio de aplicación, las reglas de negocio aprendidas.

Esta es la forma de memoria con mayor valor a largo plazo y la que más cuidado requiere en términos de actualización y mantenimiento.

### Memoria procedimental

La memoria procedimental almacena cómo se hacen las cosas: habilidades, procedimientos, rutinas. Es la memoria que activa el pianista cuando toca sin pensar en cada nota, o la del conductor que cambia de marcha sin reconstruir el proceso consciente.

En los sistemas de IA, la **memoria procedimental** se implementa de varias formas: como instrucciones de sistema que definen el comportamiento esperado, como flujos de herramientas guardados que el agente reutiliza, o como plantillas y estructuras de respuesta que el sistema aplica automáticamente a ciertos tipos de solicitudes. Es el "cómo actúa" del sistema, no el "qué sabe".

## Mapeando la taxonomía a la arquitectura

```
TIPO DE MEMORIA    |  DURACIÓN     |  CONTENIDO              |  EQUIVALENTE EN IA
-------------------|---------------|-------------------------|----------------------------
Memoria de trabajo |  Segundos/min |  Información activa     |  Ventana de contexto
Memoria episódica  |  Días/años    |  Eventos y conversac.   |  Historial persistido
Memoria semántica  |  Permanente   |  Conocimiento factual   |  Perfiles y knowledge base
Memoria procedum.  |  Permanente   |  Procedimientos         |  System prompts y flujos
```

Este mapa tiene implicancias de diseño directas. Cuando un ingeniero de IA decide qué información guardar y dónde, está respondiendo implícitamente a la pregunta: ¿qué tipo de memoria es esta? Un evento de conversación va a memoria episódica. Una preferencia estable del usuario va a memoria semántica. Una instrucción de comportamiento va a memoria procedimental. El contexto activo de la sesión actual va a la ventana de trabajo.

Confundir estas categorías produce sistemas con problemas predecibles: sistemas que guardan todo en el contexto activo (y se quedan sin tokens), sistemas que no distinguen entre hechos temporales y permanentes (y contaminan la memoria semántica con datos caducos), o sistemas que no tienen memoria procedimental explícita (y producen comportamientos inconsistentes entre sesiones).

## Una nota sobre el límite de la analogía

La analogía cognitiva es útil como marco, pero tiene límites que el ingeniero debe tener presentes.

La memoria humana es reconstructiva —cuando recordamos, reinterpretamos y completamos—, mientras que la memoria artificial es, en principio, literal: recuperamos lo que guardamos. Esto es una ventaja (precisión) y un riesgo (sin criterio de qué guardar, guardamos ruido con la misma fidelidad que guardamos señal).

La memoria humana olrida adaptativamente —los recuerdos que no se activan se degradan—, mientras que la memoria artificial persiste indefinidamente a menos que diseñemos mecanismos explícitos de degradación o eliminación. Este aspecto —el olvido como función de diseño— lo desarrollaremos en detalle en la sección 07.

La memoria humana tiene un cuerpo, un sistema emocional y un contexto social que modulan qué se recuerda. Los sistemas de IA no tienen ninguna de estas señales naturales de relevancia. Por eso el ingeniero debe diseñar criterios explícitos de relevancia y prioridad donde el cerebro humano los tiene implícitamente.

---

*La siguiente sección presenta la arquitectura general de memoria en sistemas de IA: cómo se organizan los componentes, cómo fluye la información entre ellos, y qué decisiones de diseño determinan si un sistema de memoria funciona bien en producción.*
