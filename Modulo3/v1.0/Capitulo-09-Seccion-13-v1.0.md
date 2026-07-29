# Capítulo 09 — Arquitecturas Multiagente

## Sección 13 — Resumen del capítulo

Este capítulo construyó el marco completo para diseñar sistemas multiagente desde la decisión de arquitectura hasta la operación en producción. El hilo conductor es una idea simple pero no trivial: la arquitectura multiagente no es una versión mejorada del agente único. Es una respuesta diferente a una clase diferente de problemas.

### El marco mental que este capítulo establece

**El multiagente se justifica por el problema, no por la tecnología.** Hay cuatro condiciones que justifican una arquitectura multiagente: necesidad de paralelismo genuino, necesidad de especialización radicalmente distinta por dominio, necesidad de verificación independiente por criticidad del output, y necesidad de distribuir información que excede la ventana de contexto de un agente único. Cuando ninguna de estas condiciones está presente, el agente único es la arquitectura correcta, no el multiagente.

**La especialización de cada agente determina la calidad del sistema.** Un sistema multiagente con agentes mal definidos produce resultados de menor calidad que un agente único bien diseñado. La especialización no es un detalle de implementación: es el mecanismo principal de valor de la arquitectura. Un agente especializado tiene un rol limitado, herramientas mínimas necesarias y una instrucción de sistema orientada exclusivamente a su función.

**La topología es la decisión arquitectónica más importante después de la especialización.** La topología jerárquica centraliza la coordinación y facilita el control; la pipeline impone secuencialidad natural; la topología entre pares permite adaptación descentralizada; la basada en mercado distribuye carga dinámicamente. Cada topología tiene casos de uso óptimos y compromisos específicos. Los sistemas reales frecuentemente combinan varias.

**La comunicación entre agentes debe ser estructurada y resiliente.** Los mensajes entre agentes tienen un esquema definido, con tipo, identificador, payload y metadatos. La comunicación puede ser síncrona o asíncrona según si el emisor necesita el resultado del receptor antes de continuar. Todo mecanismo de comunicación debe estar diseñado para manejar mensajes malformados, pérdidas y entregas duplicadas.

**El planificador y el supervisor son los agentes de control del sistema.** El planificador transforma una tarea compleja en un plan de subtareas con dependencias explícitas. El supervisor verifica que los outputs de los agentes ejecutores cumplan criterios de calidad antes de que sean aceptados. Sin planificación, el sistema no puede manejar tareas no completamente anticipadas. Sin supervisión, los errores se propagan hasta el output final.

**La memoria compartida es un problema de ingeniería de sistemas, no de IA.** Cuando múltiples agentes acceden y modifican el mismo estado, se producen condiciones de carrera que generan inconsistencias. Las estrategias para manejar este problema —escrituras atómicas, control de concurrencia optimista, paso de mensajes— tienen cada una sus compromisos de consistencia y rendimiento. El diseñador del sistema debe elegir la estrategia apropiada y aplicarla consistentemente.

**La tolerancia a fallos no es opcional en producción.** Los fallos en sistemas multiagente son más frecuentes que en sistemas de agente único porque hay más componentes que pueden fallar. Los reintentos con backoff, los agentes de respaldo, los circuit breakers y los puntos de verificación son estrategias de resiliencia que deben diseñarse antes de la primera línea de código de producción. La observabilidad completa del sistema —trazas de mensajes, estados de subtareas, métricas de costo— es la condición necesaria para operar el sistema y detectar problemas antes de que sean reportados por usuarios.

**Los patrones y anti-patrones nombran lo que ya se sabe que funciona y lo que ya se sabe que falla.** El patrón de Reflexión mejora la calidad mediante verificación independiente. El patrón de Ejecución Paralela con Síntesis reduce la latencia en tareas descomponibles. El patrón de Escalada Supervisada reduce el costo promedio concentrando el uso del agente más capaz en los casos más complejos. El anti-patrón del Agente Dios produce sistemas difíciles de mantener. La Red de Charlas produce sistemas ineficientes. La Confianza No Verificada produce sistemas frágiles ante errores en agentes upstream. El Multiagente Innecesario produce sistemas costosos donde no había necesidad de complejidad.

### Lo que distingue un sistema multiagente bien diseñado

Un sistema multiagente bien diseñado tiene las siguientes propiedades observables:

- Los roles de los agentes son precisos: cualquier persona que lee la instrucción de sistema de un agente entiende exactamente qué hace y qué no hace.
- La topología refleja la naturaleza del problema: las partes paralelas del trabajo se ejecutan en paralelo, las secuenciales en secuencia, y hay un mecanismo de control que garantiza que las dependencias se respetan.
- Los fallos son detectables y recuperables: cuando algo falla, el sistema lo detecta, reporta y recupera sin perder el trabajo completado hasta ese punto.
- El costo está justificado por el valor: la diferencia de calidad o velocidad que produce el sistema multiagente sobre un agente único justifica el costo adicional de tokens, latencia y complejidad operacional.

### Lo que este capítulo no cubre

Un sistema multiagente bien diseñado es un componente de un sistema más amplio. Este capítulo desarrolló la arquitectura del sistema multiagente en sí. El Módulo 4 del libro amplía la perspectiva hacia los sistemas completos donde los agentes operan: la infraestructura de orquestación a escala, los mecanismos de evaluación continua, la integración con sistemas de software empresariales y los modelos de gobierno y auditoría que los sistemas de IA en producción requieren.

La transición de los fundamentos a la arquitectura de sistema completo es el paso siguiente. El capítulo 10 de este módulo establece el puente entre ambos: el problema del razonamiento y la planificación, que es la capacidad que permite a un sistema multiagente —o a un agente único— resolver problemas que no fueron completamente anticipados en su diseño.

---

*La sección 14 pone a prueba la comprensión del capítulo con preguntas que exigen razonamiento, no memorización. Las respuestas no están explícitamente en el texto: emergen de la aplicación de los marcos desarrollados a situaciones nuevas.*
