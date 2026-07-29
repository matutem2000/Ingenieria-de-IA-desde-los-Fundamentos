# Módulo 6 – Capítulo 08 – Sección 06

# Cierre: las extensiones de RAG amplían el dominio del problema resuelto

Las extensiones del RAG estándar (multimodal, estructurado, GraphRAG, con herramientas) no son variantes experimentales sino soluciones a limitaciones concretas que emergen cuando el sistema se enfrenta a la diversidad real del conocimiento empresarial. Una organización que solo indexa documentos de texto plano está ignorando el 40–60% de su conocimiento, que reside en tablas de bases de datos, imágenes de manuales, grabaciones de reuniones y presentaciones visuales; implementar RAG multimodal y sobre datos estructurados no es "añadir features" sino "resolver el problema completo". Cada extensión tiene un perfil de complejidad, costo y beneficio diferente: el RAG multimodal añade la complejidad de los parsers de contenido visual pero amplía el corpus dramáticamente; GraphRAG añade el costo de construcción del grafo pero habilita queries de síntesis global imposibles con embeddings planos; el RAG con herramientas añade latencia y complejidad de integración pero permite respuestas sobre datos en tiempo real. La clave para un AI Engineer es evaluar cuáles de estas extensiones resuelven casos de uso reales con frecuencia suficiente para justificar su costo de implementación y operación, comenzando siempre por la extensión de mayor impacto sobre los casos de uso más frecuentes en el sistema específico.

*"Todo debería hacerse tan simple como sea posible, pero no más simple."* — atribuido a Albert Einstein; en ingeniería de sistemas, la complejidad adicional solo se justifica cuando resuelve problemas reales que la solución más simple no puede resolver.

## Principio rector

Adoptar extensiones de RAG de forma incremental, guiadas por casos de uso concretos no resueltos por el sistema base, y evaluar cada extensión con métricas de calidad antes de incorporarla permanentemente al pipeline de producción.
