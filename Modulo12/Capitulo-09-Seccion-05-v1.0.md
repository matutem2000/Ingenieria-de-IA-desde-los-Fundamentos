# Módulo 12 – Capítulo 09 – Sección 05

# Guía de contribución: cómo extender el sistema y añadir nuevas capacidades

La guía de contribución del proyecto documenta los tres tipos de extensión más comunes: agregar una nueva herramienta al agente, agregar una nueva fuente de datos al pipeline de ingesta, y cambiar el modelo de LLM o embedding. Para agregar una nueva herramienta al agente, la guía detalla: la interfaz que debe implementar (decorador `@tool`, esquema Pydantic de inputs, docstring que el LLM leerá para decidir cuándo usarla), cómo registrarla en el grafo LangGraph, cómo escribir los tests unitarios con mock del resultado, y cómo actualizar el system prompt del agente para que tenga conciencia de la nueva capacidad. Para agregar una nueva fuente de datos, la guía explica: cómo implementar la interfaz `BaseDocumentParser`, cómo registrar el parser en la fábrica de conectores, y cómo testear la ingesta con una colección de documentos de ejemplo. La guía incluye además el proceso de code review: criterios de aceptación, a quién solicitar review y el tiempo esperado de respuesta.

## Extensiones documentadas en la guía de contribución

- Nueva herramienta del agente: interfaz @tool, schema Pydantic, docstring, registro en LangGraph, tests con mock y update del system prompt
- Nueva fuente de ingesta: implementar BaseDocumentParser, registrar en la fábrica de conectores, testear con fixture de documentos
- Cambio de modelo LLM: proceso de benchmark contra golden dataset, actualización del ADR-001 y del archivo .env.example
- Cambio de modelo de embedding: requiere re-indexación completa de Qdrant; proceso blue-green documentado paso a paso
- Proceso de PR: checklist de tests, criterios de code review, quién debe aprobar y tiempo esperado de respuesta (48h)

## Para recordar

Una guía de contribución que documenta las extensiones más comunes del sistema reduce el tiempo de onboarding de nuevos ingenieros de semanas a días, y es el mecanismo que convierte el conocimiento tácito del equipo fundador en conocimiento explícito del equipo.
