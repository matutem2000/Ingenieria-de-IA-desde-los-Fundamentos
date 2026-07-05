# Informe Editorial — Capítulo 22

**Libro:** Ingeniería de IA desde los Fundamentos  
**Módulo:** 2 — Prompt Engineering Profesional  
**Capítulo:** 22 — Proyecto Integrador del Módulo 2  
**Secciones revisadas:** 01 a 07  
**Versión revisada:** 0.1  
**Fecha del informe:** 2026-07-01

---

## 1. Fortalezas

**Progresión lógica del ciclo de vida del proyecto (Secciones 01 a 06)**

La estructura del capítulo sigue fielmente el ciclo de vida de un proyecto profesional de AI Engineering: definición del problema (Sección 02), arquitectura (Sección 03), diseño funcional (Sección 04), pruebas (Sección 05), despliegue y operación (Sección 06), cierre (Sección 07). Esta progresión es la fortaleza pedagógica más sólida del capítulo: el lector transita las mismas etapas que transitaría un equipo real.

**Uso consistente de tablas y diagramas Mermaid (Secciones 02, 03, 04, 05, 06, 07)**

Las tablas de actores, componentes, métricas y competencias son claras y bien delimitadas. Los diagramas Mermaid refuerzan visualmente las relaciones entre componentes sin reemplazar la explicación textual. Su presencia en cada sección con un propósito específico —no decorativo— es una buena decisión pedagógica.

**Casos de estudio concretos y bien situados (Secciones 02, 03, 04, 05, 06, 07)**

Cada sección incluye un caso de estudio breve que ilustra el contenido principal. Los casos son coherentes entre sí: todos orbitan alrededor del mismo asistente corporativo, lo cual genera continuidad narrativa. El caso de la Sección 02 es particularmente efectivo: el equipo descubre que el problema real no era el que parecía al principio, lo que enseña algo no trivial sobre análisis de negocio.

**Separación clara entre buenas prácticas y errores frecuentes (todas las secciones)**

El formato recurrente de "Buenas prácticas / Errores frecuentes / Ideas clave" al final de cada sección funciona como un cierre pedagógico limpio. El lector sabe qué esperar y puede consultar esas secciones como referencia rápida.

**Transiciones bien escritas (Secciones 02 a 06)**

Los párrafos de transición entre secciones conectan explícitamente el contenido anterior con el siguiente. Esto reduce la sensación de fragmentación y ayuda al lector a mantener el hilo del proyecto a lo largo de las siete secciones.

**El caso de estudio de la Sección 07 tiene potencia de cierre**

La comparación entre dos organizaciones que usan el mismo modelo con resultados opuestos articula de forma contundente la tesis central del módulo: "La diferencia no reside en el modelo, sino en la ingeniería aplicada." Es una forma de cierre eficaz.

---

## 2. Debilidades

**La Sección 01 actúa como resumen del capítulo, no como introducción del proyecto (Sección 01)**

La Sección 01 describe el desafío, el alcance, los entregables y los criterios de evaluación, y luego añade buenas prácticas, errores frecuentes, ideas clave y transición hacia el Módulo 3. El resultado es que comprime en una sola sección lo que el resto del capítulo desarrollará en detalle. Esto genera una sensación de redundancia anticipada: el lector ya conoce los entregables antes de que las secciones los trabajen uno a uno. El problema se agrava porque también incluye la transición hacia el Módulo 3, que es idéntica a la que aparece en la Sección 07.

**La cita de cierre es idéntica en todas las secciones (Secciones 01 a 07)**

"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones." aparece siete veces, al final de cada sección, de manera literal. La repetición mecánica vacía la frase de impacto. En un capítulo integrador con secciones temáticas diferenciadas, esta uniformidad resulta empobrecedora.

**Escasa diferencia entre las secciones "Buenas prácticas" de distintas secciones (Secciones 02, 03, 04, 05, 06, 07)**

Varios ítems de buenas prácticas se repiten casi textualmente entre secciones. "Documentar decisiones relevantes" aparece en la Sección 03 y en la Sección 07. "Medir antes de modificar/optimizar" aparece en Sección 06 y Sección 07. "Pensar en la evolución futura" aparece en Secciones 03 y 07. Esta redundancia diluye el valor de cada sección como unidad específica de aprendizaje.

**La Sección 04 introduce el rol "Evaluador" sin vincularlo con la Sección 05 (Secciones 04 y 05)**

En la Sección 04 aparece el "Evaluador" como componente funcional dentro del flujo de interacción (diagrama Mermaid incluido). Sin embargo, la Sección 05 desarrolla la estrategia de validación como si empezara desde cero, sin referenciar ese componente. Hay una oportunidad de continuidad perdida: el "Evaluador" de la Sección 04 y los "Evaluation Sets" de la Sección 05 son el mismo concepto visto desde distintos ángulos, pero el texto no lo explicita.

**Falta de andamiaje para conceptos técnicos que se dan por conocidos (Secciones 03 y 04)**

Términos como "contratos de interacción", "desacoplamiento", "puntos de acoplamiento" y "contrato funcional" se usan sin definición. Siendo este un proyecto integrador que consolida el módulo, es razonable asumir cierto nivel de conocimiento previo; sin embargo, no hay ninguna referencia a dónde el lector puede refrescar esos conceptos si los olvidó. Una remisión explícita a los capítulos anteriores del módulo donde se trabajaron esas ideas sería útil.

**El diagrama de la Sección 03 y el de la Sección 01 son casi idénticos (Secciones 01 y 03)**

El diagrama Mermaid de la Sección 01 (alcance del proyecto) y el de la Sección 03 (arquitectura de referencia) representan el mismo sistema con diferencias menores de notación y nivel de detalle. No se señala explícitamente qué agrega el segundo respecto al primero. Sin esa aclaración, el lector puede percibirlos como duplicados.

**La Sección 07 lista competencias que no se articulan con las secciones anteriores (Sección 07)**

La tabla de competencias en la Sección 07 ("Diseñar prompts", "Evaluar resultados", etc.) no indica en qué sección de este capítulo —ni del módulo— se desarrolló cada una. El lector no puede trazar esa conexión sin hacer el trabajo por su cuenta.

---

## 3. Conceptos que conviene ampliar

**El rol del Orquestador (Sección 03 y Sección 04)**

El Orquestador aparece en el diagrama de arquitectura como el nodo central, pero su funcionamiento concreto nunca se describe en el texto. ¿Qué decisiones toma? ¿Con qué criterios elige qué componente activar? En la Sección 04 se menciona que "el orquestador únicamente incorpora una nueva decisión" al añadir RAG, pero no se explica en qué consiste esa decisión ni cómo se implementa. Este es el componente más importante de la arquitectura y el que menos desarrollo recibe.

**La distinción entre memoria y estado conversacional (Sección 03)**

La tabla de componentes diferencia "Estado conversacional" de "Memoria" como dos entidades separadas, pero el texto no explica en qué se distinguen operacionalmente. ¿El estado persiste solo en sesión? ¿La memoria persiste entre sesiones? ¿Cuál de los dos gestiona qué tipo de información? Esta distinción es conceptualmente relevante y el lector no tiene herramientas para comprenderla con lo que se provee.

**Los criterios de aceptación (Sección 05)**

La sección menciona que hay que definir "porcentaje de respuestas correctas" y "ausencia de alucinaciones críticas" como criterios de aceptación, pero no ofrece ninguna orientación sobre cómo se mide ninguno de los dos. Para un lector que llega a este punto del módulo sin experiencia previa, esas métricas son abstractas. Un ejemplo concreto de cómo se calcularía el porcentaje de respuestas correctas para el caso del asistente corporativo daría sustancia a ese concepto.

**La conexión entre "Evaluation Sets" y herramientas concretas (Sección 05)**

Se describe qué son los Evaluation Sets y por qué son importantes, pero no se menciona ningún mecanismo para implementarlos: ni frameworks, ni formatos de archivo, ni sistemas de ejecución automática. La "Ejecución automática" que aparece en el diagrama Mermaid queda como caja negra. Aunque el libro pueda querer mantenerse agnóstico respecto a herramientas específicas, al menos un ejemplo de qué estructura podría tener un caso de prueba dentro de un Evaluation Set ayudaría a concretar el concepto.

**La estrategia de rollback (Sección 06)**

La tabla de despliegue gradual menciona la posibilidad de "retroceder" ante cada etapa, pero no desarrolla qué implica ese retroceso en el contexto de un sistema basado en LLM. ¿Se revierte el prompt? ¿Se revierte la versión del modelo? ¿Se revierte la configuración del orquestador? Este es un punto de alta relevancia práctica que queda sin respuesta.

**El vínculo entre observabilidad y decisiones de arquitectura (Sección 06)**

La "Ideas clave" de la Sección 06 afirma que "la mejora continua transforma datos operativos en decisiones de arquitectura", pero esta afirmación no se desarrolla en el cuerpo de la sección. El diagrama de observabilidad termina en "Mejora continua" como nodo final, pero no ilustra cómo un dato operativo concreto (por ejemplo, alta tasa de consultas ambiguas) se traduce en una decisión arquitectónica específica. El caso de estudio de la Sección 06 es el más cercano a explicarlo, pero lo hace de manera implícita.

---

## 4. Conceptos que pueden resumirse

**La Sección 01 en su totalidad (Sección 01)**

La Sección 01 cumple el papel de índice anticipado del capítulo. Contiene el desafío, el alcance con diagrama, los entregables, los criterios de evaluación, el caso de estudio, las buenas prácticas, los errores frecuentes, las ideas clave y la transición al Módulo 3. Todo ese contenido se repite —de forma más elaborada y justificada— en las secciones siguientes. Como introducción, podría reducirse a: el desafío, el alcance (con o sin diagrama simplificado), los entregables esperados y una orientación sobre cómo leer las secciones siguientes. Los criterios de evaluación podrían moverse a la Sección 07 como parte del cierre.

**Las secciones "Buenas prácticas" y "Errores frecuentes" en las secciones intermedias (Secciones 02 a 06)**

Dado que la Sección 07 incluye una síntesis de buenas prácticas del módulo completo, los bloques de buenas prácticas de las secciones intermedias podrían acortarse a dos o tres ítems exclusivos de esa sección, eliminando los que ya aparecen en la Sección 07 o en otras secciones. Actualmente, la acumulación de listas similares en siete secciones genera fatiga de lectura sin añadir valor diferencial.

**El bloque "Actividades propuestas" de cada sección (Secciones 02 a 06)**

Las actividades propuestas son útiles pero presentan un nivel de detalle uniforme y esperado que podría agruparse en un apéndice o en una guía de trabajo separada. En el flujo de lectura, interrumpen la progresión del contenido técnico sin aportar comprensión adicional. Si el libro tiene un componente de ejercicios separado, estos bloques son candidatos naturales a ese espacio.

**La introducción de la Sección 07 (Sección 07)**

Los tres primeros párrafos de la Sección 07 repiten lo que el lector ya sabe si leyó las secciones anteriores: que el capítulo ya terminó, que el objetivo no fue escribir prompts aislados, que se recorrió el ciclo de vida. Una introducción de cierre más breve, que aporte una reflexión nueva en lugar de recapitular, sería más efectiva.

---

## 5. Recomendaciones editoriales

**1. Redefinir el rol de la Sección 01 como orientadora, no como anticipo exhaustivo (Sección 01)**

La Sección 01 debería presentar el proyecto, motivar al lector y anticipar la estructura del capítulo, sin incluir criterios de evaluación, errores frecuentes ni transición al Módulo 3. Esos elementos tienen mejor lugar en la Sección 07. La transición al Módulo 3 que aparece en la Sección 01 es idéntica a la de la Sección 07: una de las dos debería eliminarse.

**2. Diferenciar las citas de cierre por sección (Secciones 01 a 07)**

Si se mantiene el formato de cita al final de cada sección, conviene asignar una cita diferente a cada una, elegida en función del tema específico de esa sección. La cita actual es válida, pero reservarla para la Sección 07 —donde tiene más peso como cierre del módulo— y variar las demás añadiría riqueza sin cambiar el estilo.

**3. Conectar explícitamente el "Evaluador" de la Sección 04 con los "Evaluation Sets" de la Sección 05 (Secciones 04 y 05)**

Un párrafo de apertura en la Sección 05 que establezca que "el componente Evaluador descrito en la sección anterior opera a través de conjuntos de casos de prueba conocidos como Evaluation Sets" eliminaría la discontinuidad actual y reforzaría la coherencia arquitectónica del capítulo.

**4. Agregar una nota de referencia a los capítulos previos cuando se usen términos técnicos específicos (Secciones 03 y 04)**

Cuando se mencionan "contratos de interacción", "desacoplamiento" o "contrato funcional", una referencia del tipo "tal como se estudió en el Capítulo X" anclaría el contenido al módulo y evitaría que el lector sienta que esos conceptos caen del vacío.

**5. Diferenciar visualmente los diagramas de la Sección 01 y la Sección 03 o eliminar el de la Sección 01 (Secciones 01 y 03)**

Si se decide mantener ambos diagramas, convendría añadir una aclaración explícita de qué añade el de la Sección 03 respecto al de la Sección 01: por ejemplo, que el primero muestra el alcance conceptual y el segundo muestra la arquitectura técnica con responsabilidades diferenciadas. Si se simplifica la Sección 01 conforme a la Recomendación 1, el diagrama de esa sección podría eliminarse y el lector llegaría al de la Sección 03 sin haber visto ya algo parecido.

**6. Añadir al menos un ejemplo estructural de caso de prueba dentro de un Evaluation Set (Sección 05)**

No hace falta un framework ni código. Bastaría con una tabla de tres columnas —entrada, salida esperada, criterio de aceptación— con dos o tres filas del caso del asistente corporativo para que el concepto pase de abstracto a concreto.

**7. Desarrollar brevemente qué implica la decisión del Orquestador (Sección 03 o 04)**

No se pide una descripción técnica exhaustiva, sino al menos un párrafo que indique qué tipo de información usa el Orquestador para decidir qué componente activar (por ejemplo: la intención detectada por el clasificador, el estado de la sesión, la disponibilidad de documentación RAG relevante). Sin eso, el Orquestador es el componente más importante del diagrama y el más opaco del capítulo.

**8. Vincular la tabla de competencias de la Sección 07 con las secciones donde se trabajaron (Sección 07)**

Agregar una columna "Sección de referencia" a la tabla de competencias de la Sección 07 permitiría al lector volver al material específico si quiere repasar una habilidad puntual. Esto también refuerza la función integradora del capítulo.

**9. Explicitar la distinción entre estado conversacional y memoria (Sección 03)**

En la tabla de componentes, agregar una descripción de una línea que diferencie operacionalmente ambos conceptos evitaría que el lector los trate como sinónimos. No requiere una sección nueva: una nota al pie de la tabla o una fila adicional en la propia tabla con la distinción bastaría.

**10. Añadir al ciclo de mejora continua un ejemplo de cómo un dato operativo genera una decisión arquitectónica (Sección 06)**

El paso de "observar comportamiento" a "decisión de arquitectura" es el núcleo del argumento de la Sección 06, pero queda implícito. El caso de estudio existente es el mejor candidato para hacerlo explícito: señalar qué dato operativo específico llevó al equipo a ajustar el diseño conversacional, en lugar de dejarlo como una afirmación genérica.

---

*Informe generado en rol de Director Pedagógico y Revisor Editorial. No implica modificaciones directas al texto del autor.*
