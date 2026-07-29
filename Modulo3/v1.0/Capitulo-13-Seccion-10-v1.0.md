# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 10: Caso de estudio empresarial

Una empresa de servicios financieros con 800,000 clientes activos desplegó un asistente virtual de atención al cliente basado en RAG para responder consultas sobre productos de inversión, crédito hipotecario y seguros. El sistema fue diseñado para reducir el volumen de llamadas al contact center —que estaba saturado— y mejorar el tiempo de respuesta a los clientes.

Este caso describe cómo el equipo de IA enfrentó los problemas de producción y cómo la observabilidad fue la diferencia entre resolver esos problemas y perder el proyecto.

### El contexto del proyecto

El asistente fue lanzado en producción en el mes 0. La arquitectura inicial era competente: un sistema RAG con una base vectorial que indexaba el catálogo de productos, los manuales de tarifas y las preguntas frecuentes del área de soporte. El system prompt definía el tono de la institución financiera, las restricciones de lo que el asistente podía y no podía hacer, y las instrucciones para escalar a un agente humano cuando la consulta lo requería.

La instrumentación del lanzamiento era mínima: logging de errores técnicos, latencia de la API del modelo y costo por solicitud. No había medición de calidad de respuestas, no había trazabilidad de contexto y no había golden set.

Durante las primeras tres semanas, los indicadores visibles eran positivos: el sistema respondía, los errores técnicos eran inferiores al 0.5%, la latencia era aceptable. El equipo estaba satisfecho.

### El problema que no se veía

En la semana cuatro, el equipo de negocio reportó dos hallazgos preocupantes. Primero, la tasa de escalación a agentes humanos no había disminuido; de hecho, había aumentado ligeramente respecto a antes del lanzamiento. Segundo, el equipo de atención al cliente recibía más quejas que de costumbre sobre información incorrecta que los clientes decían haber obtenido del asistente virtual.

El equipo de IA revisó los logs técnicos y no encontró nada inusual. El sistema estaba funcionando correctamente desde una perspectiva técnica. No había forma de determinar qué respuestas específicas habían sido incorrectas ni por qué el sistema las había producido.

La discusión entre el equipo técnico y el equipo de negocio fue improductiva durante dos semanas. El equipo técnico argumentaba que los logs no mostraban problemas. El equipo de negocio argumentaba que los clientes estaban recibiendo información incorrecta. Nadie podía resolver la discusión con datos.

### La intervención de observabilidad

El equipo de IA tomó la decisión de parar el roadmap de nuevas funcionalidades durante dos semanas y dedicar ese tiempo a implementar observabilidad completa. Fue una decisión difícil de defender porque el sistema técnicamente funcionaba.

La implementación cubrió las cuatro dimensiones:

**Trazabilidad de contexto.** Se agregó instrumentación para registrar, en cada solicitud: los documentos recuperados con sus metadatos de fecha de actualización, el score de relevancia de cada documento recuperado, la versión del system prompt activa, y el número de tokens de cada componente del contexto.

**Evaluación automática de calidad.** Se implementó un pipeline de LLM-as-judge que evaluaba groundedness y relevancia en una muestra del 15% del tráfico. El pipeline tomaba la consulta del usuario, el contexto recuperado y la respuesta generada, y producía scores en ambas dimensiones.

**Golden set.** Se construyó un golden set de 200 casos con participación del equipo de negocio y del equipo de atención al cliente, que identificaron los tipos de consultas más frecuentes y las respuestas esperadas para cada una. Se ejecutó el golden set como prueba de lanzamiento de la observabilidad.

**Dashboard operacional.** Se construyó un dashboard semanal que mostraba las tendencias de groundedness, relevancia y satisfacción del usuario, con desglose por tipo de consulta.

### Los hallazgos de la observabilidad

Los resultados de la primera semana de observabilidad completa revelaron el problema con precisión.

El groundedness promedio del sistema era de 0.91 para las consultas sobre preguntas frecuentes y tarjetas de crédito. Pero para las consultas sobre créditos hipotecarios, el groundedness era de 0.67. El sistema producía respuestas sobre hipotecas que no podían rastrearse hasta los documentos del contexto recuperado.

La revisión de las trazas de las solicitudes hipotecarias reveló la causa raíz: el catálogo de productos hipotecarios había sido actualizado hace seis semanas con nuevas tasas de interés y condiciones de financiamiento. El documento actualizado existía en el servidor documental de la empresa, pero no había sido reindexado en la base vectorial del sistema RAG. El sistema seguía recuperando el documento de la versión anterior, con las tasas de interés antiguas.

Cuando el sistema respondía preguntas sobre hipotecas, citaba tasas que ya no estaban vigentes. Los clientes que llamaban al contact center para contratar un hipoteca recibían condiciones diferentes de las que el asistente había prometido. De ahí las quejas y las escalaciones.

El tiempo entre la identificación de la causa raíz y la solución fue de cuatro horas: reindexar el documento actualizado, verificar que el sistema estaba recuperando la versión correcta, ejecutar el golden set para confirmar que el groundedness de las consultas hipotecarias había subido al nivel esperado.

### La mejora del proceso

El hallazgo tuvo una consecuencia adicional más valiosa que la corrección inmediata: reveló que el proceso de actualización de la base vectorial no estaba integrado con el proceso de actualización de documentos. Cuando el equipo de productos actualizaba un documento, no había ningún mecanismo que notificara al equipo de IA que el documento debía ser reindexado.

El equipo diseñó un proceso de actualización automática: cuando un documento en el sistema de gestión documental era modificado y marcado como aprobado, un webhook disparaba automáticamente la reindexación del documento en la base vectorial. Si la reindexación fallaba, se generaba una alerta. El proceso eliminó la clase de error que había causado el problema hipotecario.

### Los resultados cuatro meses después

Con observabilidad completa y el proceso de actualización corregido, los indicadores del sistema cambiaron de forma medible.

La tasa de escalación a agentes humanos disminuyó un 28% respecto al nivel previo al lanzamiento. Las quejas sobre información incorrecta cayeron a casi cero en las primeras semanas después de la corrección del proceso. El groundedness promedio del sistema se estabilizó en 0.89 en todos los tipos de consulta.

El equipo pudo, por primera vez, responder con datos la pregunta que el equipo de negocio hacía: ¿el asistente está funcionando bien? Y pudo identificar con precisión los dos tipos de consultas que seguían teniendo calidad más baja —consultas sobre seguros de vida y sobre inversiones en fondos de renta variable— para enfocar el siguiente ciclo de optimización en esas áreas.

### Lecciones del caso

**Primera lección.** La ausencia de incidentes técnicos no es evidencia de que el sistema funciona bien. El sistema de esta empresa funcionaba técnicamente durante cuatro semanas mientras producía información incorrecta que causaba impacto real a los clientes. Las métricas técnicas y las métricas de calidad son dimensiones distintas.

**Segunda lección.** Sin trazabilidad, el tiempo de diagnóstico se mide en semanas y depende de conjeturas. Con trazabilidad, el diagnóstico se mide en horas y se basa en evidencia. La diferencia no es marginal; es la diferencia entre un equipo que puede operar el sistema y uno que no puede.

**Tercera lección.** La observabilidad no es solo un instrumento de diagnóstico reactivo. Es un instrumento de mejora continua. Sin los datos que la observabilidad produce, el equipo no sabe qué tipos de consultas mejorar, qué documentos están mal indexados ni qué cambios en el sistema tienen impacto positivo. Con esos datos, el equipo puede operar con intención en lugar de con intuición.

**Cuarta lección.** El costo de implementar observabilidad antes del lanzamiento habría sido significativamente menor que el costo de las dos semanas de parálisis del equipo, las quejas de clientes, la pérdida de confianza del equipo de negocio y la implementación de urgencia que finalmente ocurrió. La observabilidad como inversión inicial tiene retorno positivo en casi cualquier sistema de IA en producción.

### Nota del arquitecto

El caso descrito es representativo de un patrón que se repite con variaciones en la mayoría de las implementaciones de IA empresarial que no tienen observabilidad desde el inicio. Los detalles cambian —el dominio, el tipo de falla, el impacto en el negocio— pero la estructura es la misma: el sistema funciona técnicamente, el impacto en los usuarios es invisible hasta que llega por canales de negocio, el diagnóstico es imposible sin instrumentación, el equipo pierde tiempo y credibilidad.

La observabilidad no evita todos los problemas. Pero hace que los problemas sean detectables, diagnosticables y resolvibles. En un sistema de producción que opera durante meses o años, esa capacidad es el diferenciador entre un sistema que mejora con el tiempo y uno que se deteriora sin que nadie lo note.

La siguiente sección traduce todos estos conceptos en un ejercicio práctico: el laboratorio donde el lector define su propio framework de observabilidad para un caso de uso específico.
