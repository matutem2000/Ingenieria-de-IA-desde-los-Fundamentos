# Módulo 11 – Capítulo 05 – Sección 03

# Prompt versioning y prompt registry: gestionar prompts como artefactos de ingeniería

Un prompt en producción enterprise es un artefacto de software con el mismo ciclo de vida que el código fuente: tiene una historia de versiones, introduce cambios que pueden causar regresiones, requiere testing antes de desplegarse a producción, y puede necesitar rollback si la nueva versión degrada el comportamiento del sistema. Sin embargo, la mayoría de los equipos en etapas tempranas gestionan los prompts como strings hardcodeados en el código fuente o en archivos de configuración sin versionado explícito, lo que hace imposible rastrear qué versión de un prompt generó una respuesta problemática semanas atrás o comparar el comportamiento del sistema con diferentes versiones del mismo prompt de manera sistemática. Un prompt registry es el componente de infraestructura que resuelve este problema: almacena cada versión de cada prompt con su hash, su metadata (autor, fecha, caso de uso, modelo objetivo, temperatura sugerida), y su historial de evaluaciones, y expone una API que el servicio de orquestación llama para obtener el prompt activo para un caso de uso específico — permitiendo cambiar el prompt en producción sin desplegar código nuevo y con la capacidad de rollback inmediato a la versión anterior. Herramientas como LangSmith, Langfuse, PromptLayer, o un sistema propio construido sobre PostgreSQL + Redis pueden cumplir este rol, con la selección dependiendo de si se prefiere una solución managed o una solución self-hosted con mayor control sobre los datos de los prompts.

## Aspectos técnicos del prompt registry

- Versionado semántico de prompts: cada prompt tiene un identificador único (prompt_id) y una versión (v1.0.0, v1.1.0, v2.0.0), con convención semántica: major para cambios de estructura, minor para refinamientos, patch para correcciones menores
- Metadata y trazabilidad: cada versión registra el autor, la fecha, el modelo objetivo y su versión, los parámetros de inferencia recomendados (temperatura, top_p, max_tokens), y el resultado de la evaluación de calidad contra el golden set
- Canary prompts: capacidad de desplegar una nueva versión de prompt al 5-10% del tráfico mientras la versión anterior continúa sirviendo el 90-95% restante, monitoreando métricas de calidad antes de completar el rollout
- Prompt templates con variables: prompts parametrizados con Jinja2 o f-strings tipados que reciben variables de contexto en tiempo de ejecución, permitiendo reutilizar la estructura del prompt con contenido dinámico
- Audit trail de cambios: log inmutable de qué versión de prompt generó cada respuesta en producción, indexado por timestamp y conversation_id, crítico para investigar incidentes de calidad o compliance

## Principio rector

Gestionar prompts como código — con versionado en Git, revisión por pares, testing automatizado, y despliegue controlado — es la diferencia entre un equipo que puede operar sus sistemas de IA con confianza y uno que opera en modo apaga-incendios permanente.
