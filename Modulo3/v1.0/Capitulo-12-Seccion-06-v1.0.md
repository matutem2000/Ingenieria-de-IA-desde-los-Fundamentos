# Capítulo 12 — Context Engineering Empresarial

## Sección 06: Contexto compartido entre equipos

Una de las consecuencias más visibles de escalar la IA en una organización sin planificación es la proliferación de silos de contexto: cada equipo construye su propio asistente de IA con su propia base de conocimiento, sus propias instrucciones del sistema y su propio criterio sobre qué información es correcta. El resultado es una organización donde diferentes asistentes de IA responden de formas distintas —y a veces contradictorias— a la misma pregunta, dependiendo de qué asistente consulte el empleado.

Este problema no es hipotético. En una empresa mediana que desplegó asistentes de IA en sus equipos de ventas, soporte, recursos humanos y operaciones de forma independiente, se observó que el asistente de ventas comunicaba una política de devoluciones diferente a la que comunicaba el asistente de soporte, que el asistente de recursos humanos describía los beneficios de salud con parámetros desactualizados respecto de los que figuraban en la intranet corporativa, y que el asistente de operaciones desconocía las novedades de producto que el equipo de marketing había comunicado oficialmente tres semanas antes.

El problema no era técnico. Era de gobierno del contexto compartido.

### La topología del contexto en una organización multiequipo

Cuando múltiples equipos usan sistemas de IA dentro de la misma organización, el contexto de cada sistema tiene una estructura que puede describirse en tres zonas.

**La zona de intersección.** Es el conocimiento que todos los equipos necesitan y que debe ser consistente entre todos los sistemas: la identidad de la organización, sus valores, sus políticas públicas, su glosario de términos, sus restricciones legales. Si el asistente de ventas describe la empresa de una manera y el asistente de soporte la describe de otra diferente, los usuarios perciben una falta de coherencia institucional que erosiona la confianza en ambos sistemas.

**La zona de solapamiento parcial.** Es el conocimiento que algunos equipos comparten pero no todos. El equipo de ventas y el equipo de soporte comparten el catálogo de productos; el equipo legal y el equipo de recursos humanos comparten las políticas internas de empleo; el equipo técnico y el equipo de producto comparten las especificaciones de la plataforma. Este conocimiento compartido parcialmente es el más difícil de gestionar porque requiere coordinación entre los equipos que lo comparten sin que haya una autoridad única clara.

**La zona de especificidad.** Es el conocimiento exclusivo de cada equipo: los guiones de venta del equipo comercial, los procedimientos de escalación del equipo de soporte, los modelos de contratos del equipo legal, los runbooks del equipo técnico. Este conocimiento pertenece inequívocamente a cada equipo y no necesita coordinación horizontal.

### El anti-patrón: contexto ad hoc por equipo

El anti-patrón más común en organizaciones que escalan la IA sin planificación es que cada equipo gestiona su contexto de forma ad hoc: crea su propia base de conocimiento, define sus propias instrucciones del sistema, decide unilateralmente qué información es vigente. No hay coordinación entre equipos sobre el conocimiento compartido. No hay proceso para propagar cambios en el conocimiento corporativo a todos los sistemas que lo usan.

Las consecuencias de este anti-patrón son predecibles y acumulativas.

La **inconsistencia de políticas** aparece cuando la misma política corporativa está codificada de formas diferentes en distintos sistemas. Un usuario que consulta la política de reembolso al asistente de ventas recibe una respuesta; el mismo usuario que la consulta al asistente de soporte puede recibir una respuesta diferente. Ninguno de los dos asistentes está mintiendo; ambos están siguiendo instrucciones que reflejan versiones diferentes de la misma política.

La **duplicación de esfuerzo de mantenimiento** se hace visible cuando la empresa cambia un dato corporativo —cambia una política, lanza un producto nuevo, modifica sus condiciones de servicio— y el cambio debe propagarse manualmente a cada base de conocimiento de cada equipo. Si hay cinco equipos con bases de conocimiento independientes, el responsable de la actualización debe coordinar cinco actualizaciones separadas. Inevitablemente, alguna se olvida o se hace incorrectamente.

La **fragmentación del aprendizaje organizacional** ocurre cuando los insights derivados del uso del sistema de IA en un equipo no fluyen hacia los demás. El equipo de soporte descubre que cierto tipo de pregunta genera respuestas incorrectas porque falta información en la base de conocimiento; el equipo de ventas tiene el mismo problema y lo descubre meses después, independientemente.

### El patrón correcto: contexto compartido con especialización controlada

La solución al problema del silo de contexto no es un sistema único monolítico que todos los equipos compartan —eso sacrificaría la especificidad que cada equipo necesita— sino una arquitectura de contexto compartido con zonas de especialización controlada.

La estructura de esta arquitectura es la de las capas descritas en la sección 03, aplicada ahora con el foco en los mecanismos de coordinación entre equipos.

**El núcleo compartido.** Un conjunto de instrucciones del sistema y de conocimiento indexado que todos los asistentes de la organización heredan sin modificación. Las instrucciones corporativas del núcleo son responsabilidad de la función que coordina la iniciativa de IA de la organización —puede ser un equipo de IA centralizado, la dirección de tecnología, o un comité representativo—. Ningún equipo modifica el núcleo de forma unilateral; los cambios pasan por un proceso de aprobación que involucra a los representantes de los equipos que comparten ese contexto.

**Las capas de especialización.** Cada equipo extiende el núcleo con conocimiento y comportamientos específicos de su dominio. El equipo de soporte agrega sus procedimientos de escalación y su catálogo de soluciones conocidas. El equipo de ventas agrega sus guiones y su información de pricing específico por segmento. Estas capas de especialización son responsabilidad de cada equipo y no requieren aprobación del núcleo corporativo, siempre que no contradigan las instrucciones del núcleo.

**El protocolo de conflicto.** La arquitectura debe definir explícitamente qué ocurre cuando las instrucciones de una capa de especialización entran en conflicto con las del núcleo corporativo. La respuesta correcta es siempre que el núcleo tiene precedencia: un equipo no puede instruir a su asistente de IA a comunicar una política diferente a la política corporativa oficial, aunque tenga buenas razones comerciales para hacerlo. Este principio debe ser técnicamente reforzado —no solo una política declarada— de modo que el sistema de construcción de contexto detecte y rechace instrucciones que contradigan el núcleo.

### Mecanismos prácticos de compartición

La compartición de contexto entre equipos requiere mecanismos concretos que van más allá de un principio arquitectónico.

**Biblioteca de instrucciones compartidas.** Un repositorio centralizado —bajo control de versiones— que contiene los bloques de instrucciones del sistema que todos los equipos pueden usar como componentes. Un bloque de "tono de comunicación corporativo", un bloque de "restricciones legales aplicables", un bloque de "política de precios vigente". Los equipos componen sus instrucciones combinando bloques de la biblioteca con sus extensiones específicas. Cuando un bloque de la biblioteca cambia, el cambio se propaga a todos los sistemas que lo usan.

**Proceso de propagación de actualizaciones.** Cuando el conocimiento corporativo cambia, el proceso de propagación define cómo ese cambio llega a todas las bases de conocimiento que lo indexan. En la implementación más simple, el equipo responsable del cambio notifica a todos los equipos que usan ese conocimiento, y cada equipo actualiza su base vectorial. En implementaciones más sofisticadas, un sistema de suscripción detecta automáticamente los cambios en las fuentes autorizadas y desencadena la reindexación en todas las bases vectoriales dependientes.

**Foro de coordinación inter-equipos.** Un espacio —puede ser una reunión periódica, un canal de comunicación dedicado— donde los responsables de IA de cada equipo comparten problemas de calidad del conocimiento compartido, propuestas de cambio al núcleo y aprendizajes de la operación. Este foro es el mecanismo humano que complementa la arquitectura técnica: la arquitectura define qué puede modificarse sin aprobación y qué requiere coordinación; el foro es donde esa coordinación ocurre.

### Contexto compartido como ventaja competitiva

Las organizaciones que resuelven bien el problema del contexto compartido obtienen una ventaja que no está en las especificaciones técnicas de ningún producto de IA: la coherencia institucional de sus sistemas de IA. Cuando un cliente interactúa con el asistente de ventas y después con el asistente de soporte, recibe la misma versión de la política de la empresa, el mismo catálogo de productos, el mismo tono. Esa coherencia es costosa de construir y casi imposible de imitar de forma ad hoc.

### Nota del arquitecto

El gobierno del contexto compartido es uno de los problemas más frecuentemente subestimados en proyectos de IA empresarial. Los equipos de ingeniería tienden a enfocarse en el problema técnico de la compartición —cómo sincronizar las bases vectoriales, cómo versionar las instrucciones— y a asumir que el problema organizacional —quién decide qué va en el núcleo, cómo se resuelven los conflictos entre equipos— se resolverá por sí solo. No se resuelve. Requiere estructuras de gobierno explícitas, procesos de toma de decisiones acordados y patrocinadores con autoridad suficiente para hacer que esos procesos se cumplan.

La siguiente sección examina cómo operar un sistema de IA empresarial a escala: los problemas de escalabilidad que aparecen cuando el sistema pasa de decenas a cientos o miles de usuarios, y cómo el Context Engineering interviene en la operación continua.
