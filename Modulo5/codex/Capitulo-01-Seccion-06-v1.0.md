# Módulo 5 – Capítulo 01 – Sección 06

# Cierre: el stack mínimo viable para un ingenieros de IA

El stack mínimo viable para construir y operar aplicaciones de IA en producción converge en un conjunto acotado de herramientas: un SDK oficial de proveedor para las llamadas al modelo, un gestor de secretos o variables de entorno para las credenciales, una biblioteca de logging estructurado (Python `structlog` o el módulo estándar `logging` con formato JSON), y una herramienta de observabilidad como Langfuse o LangSmith para capturar trazas de prompts y respuestas. Sobre este núcleo se añaden herramientas según la complejidad creciente del sistema: un framework de orquestación solo cuando las cadenas superan 3-4 pasos interdependientes, una base de datos vectorial solo cuando el volumen de documentos supera los 10.000 chunks, y un sistema de evaluación automatizado desde el primer sprint de desarrollo, no como etapa final. La tentación de adoptar prematuramente todo el stack posible —LangChain, LlamaIndex, un vector DB, un observability platform, un evaluation framework— genera deuda técnica y dependencias que dificultan el diagnóstico de problemas. El principio rector del ingenieros de IA experimentado es: comenzar con el stack más simple que resuelva el problema y añadir complejidad solo cuando la evidencia de producción lo justifique.

## Componentes del stack mínimo viable

- SDK del proveedor: `openai`, `anthropic` o `google-generativeai` para las llamadas al modelo con tipado estricto y retry automático
- Gestión de secretos: `.env` + `python-dotenv` en desarrollo, Secret Manager o variables de entorno del CI/CD en producción
- Logging estructurado: captura de prompts, respuestas, tokens usados, latencia y errores en formato JSON para análisis posterior
- Observabilidad básica: Langfuse (open source, self-hosteable) o LangSmith para trazas de llamadas, costos acumulados y comparación de versiones de prompts
- Testing desde el primer día: pytest con mocks del cliente LLM para unit tests y un conjunto de casos de evaluación con salida esperada para regression testing

## Para recordar

*"Simplicity is a prerequisite for reliability."* — Edsger Dijkstra. En AI Engineering, cada herramienta adicional en el stack introduce un punto potencial de fallo, una versión que actualizar y un concepto que el equipo debe dominar; el stack mínimo viable no es una limitación sino la base de un sistema confiable.
