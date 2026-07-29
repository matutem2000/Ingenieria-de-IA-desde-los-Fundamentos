# Módulo 4 – Capítulo 10 – Sección 02

## Diseño Evolutivo

El diseño evolutivo es el conjunto de principios y prácticas de arquitectura que minimizan el costo de los cambios futuros. No es una metodología específica sino una actitud de diseño: cada decisión se evalúa no solo por su idoneidad hoy sino por su impacto en la capacidad de cambiar mañana. Un sistema construido con principios de diseño evolutivo puede reemplazar su modelo de lenguaje, migrar su base vectorial a una tecnología más reciente, o refactorizar la estrategia de chunking — todo ello sin reconstruir el sistema completo y sin tiempo de inactividad significativo.

**Separación de responsabilidades por velocidad de cambio** es el principio central del diseño evolutivo aplicado a sistemas de IA. Los componentes se organizan en capas según con qué frecuencia se espera que cambien:

- **Capa de interfaz de usuario y experiencia:** cambia frecuentemente con el diseño del producto. Debe estar completamente desacoplada de la lógica del pipeline de IA.
- **Capa de lógica de negocio y orquestación:** define qué hace el sistema. Cambia cuando el caso de uso evoluciona, con frecuencia moderada. Esta capa debe ser independiente del modelo específico y del framework de orquestación.
- **Capa de integración con IA:** abstrae el acceso a los modelos de lenguaje, el retriever y las herramientas. Cambia cuando el ecosistema de herramientas evoluciona. Esta capa es el punto de adaptación a los cambios tecnológicos.
- **Capa de datos:** la base vectorial, el almacenamiento de documentos, el historial de conversaciones. Cambia con menor frecuencia pero con mayor impacto cuando cambia. La migración de datos es costosa — la arquitectura de datos debe ser especialmente cuidadosa.

**Contratos estables entre componentes** son la garantía de que los cambios en un componente no producen cambios en cascada en los demás. Un contrato es la interfaz acordada entre dos componentes: qué datos recibe, en qué formato, y qué devuelve. Si el contrato del servicio de recuperación define que recibe una consulta en texto y devuelve una lista de chunks con sus metadatos, la implementación interna del retriever puede cambiar (de búsqueda semántica pura a búsqueda híbrida, de Pinecone a Qdrant, de embeddings de OpenAI a embeddings de BGE) sin que ningún otro componente del sistema lo note.

Los contratos deben ser: explícitos (documentados en un schema formal, no en comentarios de código), versionados (con políticas claras de compatibilidad hacia atrás), y verificables (con tests de contrato que se ejecutan en el pipeline de CI/CD y detectan violaciones antes del despliegue).

**Reemplazo gradual de tecnologías** es el mecanismo de ejecución del diseño evolutivo. Cuando llega el momento de cambiar un componente — migrar la base vectorial, actualizar el modelo de embeddings, cambiar el framework de agentes —, el reemplazo gradual permite hacerlo con riesgo mínimo:

1. La nueva implementación se desarrolla detrás del contrato existente, sin modificar la interfaz.
2. El tráfico se divide gradualmente entre la implementación antigua y la nueva (patrón strangler fig).
3. Las métricas de calidad y rendimiento se comparan entre las dos implementaciones.
4. Cuando la nueva implementación supera o iguala a la antigua en todas las métricas clave, el tráfico se transfiere completamente.
5. La implementación antigua se retira.

Este proceso — análogo al Blue-green deployment pero aplicado a componentes individuales en lugar de versiones completas del sistema — permite actualizaciones tecnológicas continuas sin "big bang migrations" que concentran el riesgo en una sola transición.

**Modularización del conocimiento del dominio** es el tercer principio del diseño evolutivo en sistemas de IA. El conocimiento del dominio — las reglas de negocio, los criterios de calidad de las respuestas, las restricciones de comportamiento del sistema — debe estar explícito y separado de la implementación técnica. Un sistema que codifica su conocimiento del dominio en el prompt de sistema, en los criterios de evaluación, y en la base de conocimiento curada tiene ese conocimiento en lugares gestionables y actualizables. Un sistema que codifica su conocimiento del dominio en los pesos del modelo (a través de fine-tuning) tiene ese conocimiento en un lugar costoso de actualizar y difícil de auditar.

> **Nota del Arquitecto:** La señal de que un sistema no fue diseñado para evolucionar es cuando cualquier cambio técnico requiere una reunión de impacto con múltiples equipos, semanas de análisis, y miedo al despliegue. En un sistema bien diseñado evolutivamente, la pregunta "¿podemos cambiar el modelo de embeddings?" debería poder responderse con "sí, tomará dos sprints": uno para implementar la nueva versión detrás del contrato existente, y otro para comparar métricas y migrar el tráfico. Si la respuesta es "necesitamos tres meses y un proyecto completo", el sistema tiene deuda de diseño evolutivo.

El diseño evolutivo no es costoso de implementar: los contratos bien definidos, la separación de responsabilidades por velocidad de cambio, y los mecanismos de reemplazo gradual son prácticas de arquitectura que cuestan poco tiempo adicional en el diseño inicial pero ahorran costos enormes en las actualizaciones futuras.
