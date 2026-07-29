# Capítulo 15 — Proyecto Integrador

## Sección 15: Próximos pasos y cierre del Módulo 3

### Lo que construiste en este módulo

Cuando empezaste el Módulo 3, un sistema de IA era probablemente una caja negra con una API: envías texto, recibes texto. Al cerrar el módulo, esa caja negra tiene partes visibles, nombradas y diseñables.

Ahora sabes que la ventana de contexto es un presupuesto que se administra, no un depósito ilimitado. Que las instrucciones del sistema son el mecanismo principal de control del comportamiento del modelo, y que deben gestionarse como artefactos de software con versiones y responsables. Que la memoria persistente es una selección intencional, no una acumulación automática. Que RAG no es magia: es un pipeline de recuperación con etapas específicas, criterios de calidad y puntos de falla concretos. Que las herramientas le dan agencia al sistema, pero esa agencia requiere controles de acceso y confirmación humana para las acciones irreversibles. Que los agentes son la herramienta correcta cuando la tarea requiere condicionalidad en la secuencia de pasos, no cuando simplemente queremos que el sistema "sea más inteligente". Que observabilidad y seguridad se diseñan desde el primer diagrama de arquitectura, no se agregan como capas después del lanzamiento.

Esos son los instrumentos del Context Engineering profesional. Los tienes. El siguiente módulo los usa.

---

### Qué viene en el Módulo 4

El Módulo 4 se ocupa de las Arquitecturas Modernas de Sistemas de IA. Asume que el Context Engineering del Módulo 3 está dominado y construye sobre esa base.

Los tres saltos de complejidad que el Módulo 4 introduce:

**Primero: multiagencia.** En el Módulo 3, los agentes son unidades individuales con un conjunto de herramientas. En el Módulo 4, múltiples agentes colaboran en sistemas donde el trabajo se distribuye, los resultados se sintetizan, y la coordinación entre agentes requiere sus propios mecanismos de comunicación y control. El Context Engineering que diseñaste para un agente único aplica a cada agente del sistema multiagente, pero la arquitectura del sistema completo introduce desafíos nuevos: consistencia de estado entre agentes, gestión de conflictos, y supervisión de sistemas que toman decisiones distribuidas.

**Segundo: escala.** Los casos del Módulo 3 operan con decenas o cientos de usuarios. Los sistemas de producción a escala empresarial operan con miles o millones. La escala introduce restricciones que cambian las decisiones de diseño: el costo de tokens por millón de interacciones diarias, la latencia bajo carga concurrente alta, la consistencia de la base documental cuando múltiples pipelines de ingestión la modifican simultáneamente, y la operación de sistemas que no pueden tener tiempo de inactividad.

**Tercero: infraestructura de IA.** El Módulo 3 trató la infraestructura como un requisito (RNF-04: usa servicios de mercado). El Módulo 4 la trata como un dominio de diseño: cómo se seleccionan y combinan los modelos base, cuándo el fine-tuning justifica el costo de entrenamiento, cómo se diseñan los pipelines de evaluación continua que detectan degradaciones del comportamiento del sistema antes de que los usuarios las noten, y cómo se gestiona la evolución de un sistema de IA en producción a lo largo del tiempo.

El Context Engineering del Módulo 3 es el lenguaje que usarás para diseñar y razonar sobre esas arquitecturas más complejas. No lo reemplaza el Módulo 4: lo presupone.

---

### Recursos para continuar

El campo del Context Engineering y la ingeniería de sistemas de IA evoluciona rápidamente. Los conceptos del Módulo 3 son principios que trascienden versiones de modelos y frameworks, pero las implementaciones específicas cambian. Estos recursos te ayudarán a mantenerte actualizado:

**Documentación oficial de modelos y APIs.** Las páginas de documentación de los proveedores de LLM son la fuente más actualizada sobre capacidades de ventana de contexto, herramientas disponibles, y mejores prácticas de uso de cada modelo específico.

**El repositorio de Model Context Protocol (MCP).** La especificación oficial de MCP y sus implementaciones de referencia están publicadas en el repositorio de Anthropic. Para cualquier proyecto que use herramientas, la especificación MCP es la referencia definitiva sobre cómo estructurar la comunicación entre orquestador y herramientas.

**Evaluaciones y benchmarks públicos de RAG.** Los trabajos académicos sobre RAG (RAGAS, BEIR, MTEB) publican métricas de calidad de recuperación que te permiten calibrar si tu pipeline RAG tiene el rendimiento esperable. Son también la mejor fuente para entender las limitaciones de los enfoques actuales.

**Comunidades de práctica.** Los foros de discusión técnica alrededor de LangChain, LlamaIndex, y los SDKs de los principales proveedores de LLM son donde los equipos de ingeniería comparten problemas reales y soluciones concretas. Los problemas que encontrarás en tus primeros proyectos reales probablemente ya fueron resueltos por alguien en esas comunidades.

---

### Una nota final sobre el oficio

El Context Engineering no es una disciplina de año. Es una disciplina que se construye proyecto a proyecto, y que se mejora con cada sistema que se depura en producción, cada degradación de comportamiento que se diagnostica, y cada decisión de diseño que se revisa a la luz de cómo operó el sistema en la realidad.

Los principios del módulo son una base sólida. Pero la competencia real viene de aplicarlos, equivocarse en los detalles, diagnosticar lo que falló, y volver al diseño con esa experiencia. El checklist de la sección 12 es más útil la tercera vez que lo aplicas que la primera, porque la tercera vez ya sabrás de qué trata cada ítem desde la experiencia, no solo desde la lectura.

El Módulo 4 te espera con esa base construida. Continúa.
