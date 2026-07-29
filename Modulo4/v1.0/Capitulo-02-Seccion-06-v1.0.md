# Módulo 4 – Capítulo 02 – Sección 06

## Resumen

Este capítulo desarrolló el vocabulario arquitectónico fundamental que el arquitecto de IA necesita para tomar las decisiones de más alto nivel de un sistema: cómo está organizado y dónde vive el conocimiento que el sistema utiliza para responder.

El patrón monolítico, frecuentemente subestimado, es la elección correcta para sistemas en etapa de validación, equipos pequeños y presupuestos limitados. Su ventaja — simplicidad operativa — se convierte en limitación cuando el sistema escala o cuando diferentes componentes requieren ciclos de despliegue y recursos de hardware distintos. El monolito no es el enemigo de los sistemas de IA; es el punto de partida adecuado para muchos de ellos.

Los microservicios resuelven las limitaciones del monolito a costa de una complejidad operativa significativa. Los beneficios — escalado granular, despliegues independientes, isolation de fallos — justifican esa complejidad cuando el sistema ha demostrado su valor en producción y los límites del dominio están suficientemente claros. En sistemas de IA, los patrones específicos de microservicios como el sidecar de observabilidad y el circuit breaker para LLMs externos son mecanismos que protegen al sistema de los comportamientos particulares de las APIs de modelos de lenguaje.

Las arquitecturas basadas en eventos son el mecanismo natural para los pipelines asíncronos de sistemas de IA: ingesta de documentos, evaluación periódica de calidad, procesamiento de lotes y pipelines de fine-tuning disparados por umbrales de datos. Su valor está en el desacoplamiento temporal: el productor no espera al consumidor, lo que incrementa la resiliencia y la capacidad de escalar cada etapa independientemente.

La decisión de mayor jerarquía — prompt engineering, RAG o fine-tuning — debe tomarse antes de cualquier decisión de infraestructura, porque determina el tipo de sistema que se construirá. El prompt engineering es simple pero limitado en volumen y frecuencia de actualización. El RAG es el patrón correcto para conocimiento voluminoso y dinámico, con alta trazabilidad. El fine-tuning es adecuado para adaptar el comportamiento del modelo cuando el conocimiento es estático y especializado, pero su costo de actualización lo hace inadecuado para dominios que cambian frecuentemente.

El arquitecto correcto no es el que conoce todos los patrones, sino el que puede articular con precisión por qué elige uno sobre otro en un contexto dado. Esa articulación — las necesidades del negocio, el presupuesto, el equipo, el volumen de uso, la frecuencia de cambio del conocimiento — es exactamente lo que diferencia una decisión arquitectónica de una preferencia tecnológica.

El Capítulo 03 aplica estos principios al patrón de mayor adopción en sistemas de IA empresariales actuales: la arquitectura RAG en producción, con toda su infraestructura de ingesta, recuperación, generación y operación continua.

---

*"La arquitectura de software no trata de las herramientas que usas. Trata de las decisiones que tomas antes de usar cualquier herramienta."*
— Martin Fowler, autor de *Patterns of Enterprise Application Architecture*
