# Módulo 12 – Capítulo 04 – Sección 06

# Cierre: el agente convierte el sistema de recuperación de información en un asistente activo

El sistema agéntico del proyecto final transforma el pipeline RAG de un motor de búsqueda sofisticado en un asistente técnico capaz de razonar sobre múltiples fuentes, reformular queries cuando el primer retrieval es insuficiente, y sintetizar información de varios documentos en respuestas estructuradas. La clave de esa transformación es la integración correcta entre el agente y el RAG: encapsulando el retrieval detrás de un contrato de herramienta tipado, el agente puede usar el conocimiento de forma flexible sin acoplarse a los detalles de implementación del pipeline de búsqueda. El testing sistemático de escenarios de fallo, los criterios de aceptación cuantitativos y la observabilidad con LangSmith garantizan que el agente se comporte de forma predecible en producción. La observabilidad agéntica — trazas de razonamiento, métricas de completitud, tool usage rates — es el mecanismo que cierra el loop operativo y permite mejorar el sistema con evidencia en lugar de intuición.

## Aspectos técnicos que integra este capítulo

- Grafo de estado LangGraph con nodos ReAct, condiciones de parada y fallback documentados
- Contratos de herramientas tipados con Pydantic, manejo de errores estructurado y timeout por herramienta
- Integración RAG-agente mediante encapsulación del pipeline detrás de un contrato de función
- Testing en tres niveles: unit, integration y behavior, con cobertura de escenarios adversariales
- Observabilidad: trazas OpenTelemetry por paso ReAct, LangSmith para debugging visual, métricas de completitud

## Para recordar

Un agente sin observabilidad y sin criterios de aceptación cuantitativos no es un sistema — es un experimento en producción.

*"The goal of AI agents is not to replace human judgment but to extend human capability — and that requires the agent to be transparent about what it knows, what it doesn't, and what it did to find out." — Andrew Ng*
