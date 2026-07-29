# Módulo 5 – Capítulo 04 – Sección 06

# Cierre: integración de IA sin reescribir el sistema existente

El principio de integración incremental —añadir capacidades de IA como nuevas capas sobre el sistema existente sin reestructurar la base— es el enfoque más pragmático y de menor riesgo para organizaciones con software en producción. Un sistema CRM existente no necesita ser reescrito para añadir un asistente de redacción de emails: basta con un nuevo endpoint que recibe el contexto del cliente desde la base de datos existente, llama al LLM y devuelve el borrador; el frontend añade un botón que consume ese endpoint. Este patrón de strangler fig aplicado a IA permite entregar valor en semanas en lugar de meses, validar el caso de uso con usuarios reales antes de comprometer recursos de reescritura, y mantener el sistema existente en operación sin interrupciones durante la transición. Los antipatrones que deben evitarse son: integrar el SDK del LLM directamente en el ORM o en la lógica de negocio existente (creando acoplamiento fuerte), usar el mismo objeto de sesión del framework web para almacenar el historial conversacional (no escala), y hardcodear el proveedor de LLM en múltiples puntos del código (impide migración posterior).

## Buenas prácticas de integración incremental

- Strangler fig para IA: identificar las funciones de negocio que se benefician de IA (redacción, clasificación, análisis), crear endpoints nuevos paralelos a los existentes y migrar gradualmente el tráfico, sin tocar el código heredado
- Adapter pattern para el LLM: encapsular toda la interacción con el proveedor de LLM en una sola clase o módulo con una interfaz estable, de modo que cambiar de proveedor o versión de modelo requiera modificar solo ese adaptador
- Separación de concerns: la lógica de negocio no debe saber que existe un LLM; debe llamar a un servicio de "análisis" o "generación" que internamente usa el LLM, manteniendo la abstracción limpia y testeable
- Compatibilidad hacia atrás en schemas de base de datos: añadir columnas nuevas (nullable) para almacenar outputs del LLM en tablas existentes, con migraciones que no bloquean la tabla en producción usando `ADD COLUMN IF NOT EXISTS` en PostgreSQL
- Monitoreo diferencial: comparar métricas de negocio (satisfacción del usuario, tiempo de resolución, tasa de conversión) entre usuarios que usan las nuevas capacidades de IA y los que usan el flujo tradicional para validar el valor real antes de un rollout completo

*"Make it work, make it right, make it fast."* — Kent Beck. En AI Engineering aplicado a sistemas existentes, el orden es: hacer que la capacidad de IA funcione correctamente en un subconjunto del tráfico, luego integrarla limpiamente en la arquitectura, y finalmente optimizar para escala y costo cuando el valor está validado.
