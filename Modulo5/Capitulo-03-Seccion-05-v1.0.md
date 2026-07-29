# Módulo 5 – Capítulo 03 – Sección 05

# Cuándo no usar un framework: complejidad accidental y dependencias innecesarias

La complejidad accidental es la complejidad que introduce la solución más allá de la inherente al problema, y los frameworks de orquestación pueden ser su mayor fuente en proyectos de IA cuando se adoptan prematuramente. LangChain v0.1 a v0.3 sufrió múltiples breaking changes que obligaron a equipos a reescribir su código de integración; proyectos que usaban implementación directa no se vieron afectados. Añadir LangChain o LlamaIndex a un proyecto agrega entre 50 y 200 dependencias transitivas de Python, incrementando el tiempo de build del contenedor Docker, la superficie de vulnerabilidades de seguridad (CVEs) y la probabilidad de conflictos de versión con otras bibliotecas del proyecto. Casos concretos donde no usar un framework: un endpoint de API que simplemente toma el input del usuario, lo envía a Claude con un system prompt fijo y devuelve la respuesta no necesita ningún framework; un script de batch que procesa 1.000 documentos con un prompt fijo tampoco; un clasificador de intenciones con 5 categorías que usa una sola llamada al LLM definitivamente no.

## Señales de que un framework no está justificado

- Flujo de un solo paso: si la aplicación hace exactamente una llamada al LLM por request sin ramificación ni composición, cualquier framework es overhead puro sin beneficio real de abstracción
- Equipo pequeño o junior: los frameworks requieren que todo el equipo entienda sus abstracciones; en equipos de 1-2 personas, el costo de aprendizaje supera el beneficio de composición para la mayoría de los casos de uso
- Alta necesidad de control y debuggabilidad: cuando los bugs son costosos o difíciles de reproducir, tener el stack de llamadas completo en código propio facilita el diagnóstico; un error dentro de un `RunnableSequence` de LangChain puede tener un traceback de 15 frames antes de llegar al código del usuario
- Requisitos de rendimiento extremo: los frameworks añaden overhead de serialización y deserialización en cada paso de la cadena; para sistemas con SLA de latencia <100ms, cada capa de abstracción importa
- Caso de uso estable y bien entendido: si el flujo no cambiará significativamente en los próximos 6-12 meses, la implementación directa con buena estructura interna es más mantenible que una cadena de LCEL

## Idea central

La decisión de usar un framework debe evaluarse con la misma rigurosidad que cualquier otra dependencia de terceros: ¿qué problema específico resuelve que no se puede resolver en menos código propio y con menos complejidad?
