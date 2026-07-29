# Módulo 12 – Capítulo 01 – Sección 06

## Cierre: el diseño es la decisión más importante del proyecto

El Capítulo 1 estableció el terreno sobre el que se construye el proyecto final. No es un terreno vacío: está delimitado por restricciones de latencia, costo y seguridad que hacen imposible ciertas decisiones y necesarias otras. Está mapeado por una arquitectura de alto nivel que muestra cómo fluyen los datos desde un documento hasta una respuesta, y cómo se organiza el código en un repositorio que cualquier ingeniero puede navegar. Está orientado por criterios de éxito que convierten "el sistema funciona" en "el sistema alcanza faithfulness >= 0.85, latencia P95 < 3s y tasa de bypass < 5% con evidencia medible". Todo lo que viene después — los ADRs, la implementación, el despliegue, la evaluación — es la ejecución de las decisiones tomadas aquí.

La lección más importante del capítulo de diseño no es técnica: es de proceso. El error más costoso en sistemas de IA no es elegir el modelo equivocado o el framework subóptimo — estos errores son corregibles. El error más costoso es comenzar a implementar sin haber definido los criterios de éxito, sin haber documentado las alternativas evaluadas y sin haber trazado el flujo de datos del sistema completo. Cuando eso ocurre, el equipo construye durante semanas o meses y luego descubre que el sistema no puede evaluarse porque no se definió el golden dataset, no puede auditarse porque los logs no tienen trace_id, y no puede mejorarse porque no hay métricas de referencia contra las cuales medir el cambio. El diseño previo a la implementación no es burocracia — es la inversión que hace posible iterar con evidencia en lugar de con intuición.

Lo que este capítulo no resuelve — deliberadamente — es el detalle de implementación de cada decisión. Esas decisiones se documentan en los ADRs del Capítulo 2, que registran formalmente el razonamiento detrás de cada elección técnica importante: por qué GPT-4o sobre Claude 3.5 Sonnet, por qué text-embedding-3-small sobre text-embedding-3-large, por qué LangGraph sobre LangChain AgentExecutor, y qué controles de seguridad no son negociables. Los ADRs son el puente entre el diseño de alto nivel de este capítulo y la implementación de los capítulos 3 al 9.

## Lo que este capítulo resolvió

- **Propósito y contexto**: el proyecto final es un caso de uso enterprise real (asistente técnico para ingenieros de software), con aspectos enterprise presentes (RBAC, auditoría, restricciones de costo) y simplificaciones pedagógicas explícitas (sin integración con legacy systems, sin GDPR completo).
- **Alcance con exclusiones explícitas**: fuentes incluidas (Markdown, PDF técnico, OpenAPI, Confluence), fuentes excluidas (código fuente, emails, Slack), capacidades del agente (solo lectura), y por qué estas exclusiones son decisiones de seguridad tanto como de alcance.
- **Arquitectura con flujos de datos**: el flujo de ingesta asíncrona y el flujo de consulta síncrona como los dos caminos principales que el sistema ejecuta, con cada componente en su capa y la estructura del repositorio que los refleja.
- **Stack con justificación comparativa**: GPT-4o, text-embedding-3-small, Qdrant, LangGraph y FastAPI elegidos con criterios medibles y alternativas evaluadas y descartadas documentadas.
- **Criterios de éxito verificables**: faithfulness >= 0.85, latencia P95 < 3s, costo < 0.015 USD/req, bypass < 5%, con la explicación de por qué el gate de CI/CD usa umbrales ligeramente más permisivos (0.82) por razones estadísticas de muestreo.

> **Nota del Arquitecto**: El diseño de este capítulo tomará entre medio día y un día de trabajo de un ingeniero senior. Es la inversión de tiempo con mayor retorno de todo el proyecto. Cada hora de diseño previo ahorra entre 3 y 10 horas de refactoring posterior. Si el equipo siente la urgencia de "empezar a codear", ese es exactamente el momento en el que conviene resistir esa urgencia y dedicar otro ciclo a revisar si las restricciones están claras, si los criterios de éxito son medibles y si la arquitectura tiene interfaces limpias entre componentes.

El Capítulo 2 documenta las decisiones técnicas más importantes del proyecto en cuatro ADRs: elección del modelo fundacional (ADR-001), estrategia de RAG (ADR-002), diseño del agente (ADR-003) y estrategia de seguridad (ADR-004). Estos documentos son la memoria arquitectónica del sistema — la razón por la que, seis meses después del primer despliegue, el equipo puede explicar por qué el sistema funciona como funciona y bajo qué circunstancias tendría sentido cambiarlo.

**Para recordar**: El diseño de un sistema de IA comienza por las restricciones y los criterios de éxito — la tecnología viene después.

*"Good software systems are not built by accumulating features, but by restricting what they do." — Fred Brooks, The Mythical Man-Month*
