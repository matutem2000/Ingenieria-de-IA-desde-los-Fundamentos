# Módulo 5 – Capítulo 03 – Sección 04

# Comparación: LangChain vs LlamaIndex vs implementación directa

Elegir entre LangChain, LlamaIndex o llamadas directas al SDK del proveedor requiere evaluar honestamente la complejidad del caso de uso, el tamaño y experiencia del equipo, y el costo de mantenimiento de la abstracción a lo largo del tiempo. LangChain es la opción más versátil para flujos complejos con múltiples herramientas, agentes con estado y composición declarativa de cadenas; su mayor costo es el alto ritmo de cambios en la API entre versiones y la curva de aprendizaje de LCEL y LangGraph. LlamaIndex es la opción dominante para sistemas RAG con múltiples fuentes de datos, índices heterogéneos y query engines avanzados; su ecosistema de conectores de datos (150+) y su abstracción de pipeline de ingesta son difíciles de replicar a mano. La implementación directa con el SDK del proveedor es la opción más controlable, predecible y fácil de diagnosticar para flujos simples de 1-3 pasos; cualquier desarrollador Python puede leer y entender el código sin conocer los abstracciones del framework.

## Aspectos técnicos comparativos

- LangChain: fortalezas en composición de agentes complejos, integración con 200+ herramientas y vectorstores, LangGraph para flujos cíclicos y LangSmith para observabilidad nativa; debilidades en overhead de abstracción, frecuentes breaking changes y debugging complejo cuando el error ocurre dentro de un runnable anidado
- LlamaIndex: fortalezas en ingesta multi-fuente, chunking avanzado, evaluación de recuperación con `RetrieverEvaluator`, y abstracciones de `SubQuestionQueryEngine` para RAG sobre múltiples documentos; debilidades en flujos que no son recuperación-síntesis y en la curva de aprendizaje de su API de bajo nivel
- Implementación directa: fortalezas en control total del flujo, cero dependencias de terceros más allá del SDK, debugging trivial con breakpoints, y código comprensible para cualquier desarrollador Python; debilidades en la necesidad de reimplementar retry, streaming, manejo de herramientas y gestión de memoria conversacional desde cero
- Criterio de decisión por líneas de código: si el flujo requiere >200 líneas de código sin framework para manejar correctamente los casos borde, un framework está justificado; si caben en <100 líneas limpias, la implementación directa es preferible
- Combinación de frameworks: es válido y común usar LlamaIndex para la capa de recuperación RAG y llamadas directas o LangChain para la capa de agencia y composición, sin comprometerse a un solo framework en toda la aplicación

## Buena práctica

Prototipar primero con implementación directa para entender los requisitos reales del flujo, y solo entonces evaluar qué framework resuelve mejor las partes que resultaron complejas de implementar.
