# Módulo 3 — Context Engineering

# Capítulo 06 — RAG (Retrieval-Augmented Generation) como componente del Context Engineering

## Sección 15 — Transición al Capítulo 07

---

## Lo que RAG resolvió y lo que no

Este capítulo construyó una capacidad específica para los sistemas de IA: acceder a conocimiento externo que el modelo no tiene en sus parámetros, recuperarlo en función de la relevancia para cada consulta e incorporarlo al contexto de la inferencia. Es una capacidad poderosa, pero tiene un alcance bien definido.

RAG resuelve bien el problema del conocimiento **semiestructurado o no estructurado que es relativamente estable**: documentos normativos, manuales técnicos, contratos, informes, bases de conocimiento institucional. El corpus puede actualizarse, pero no en tiempo real. La información existe en texto, está organizada en fragmentos, puede indexarse y puede recuperarse por similitud semántica.

Lo que RAG no resuelve es el problema del conocimiento **dinámico y transaccional**: el precio de una acción en este momento, el estado actual de un pedido, el resultado de ejecutar una consulta SQL sobre datos de producción, el contenido de una página web que cambió hace diez minutos, o el resultado de llamar a una API externa que no existía cuando se construyó el índice.

Para esa clase de información, el mecanismo de recuperación adecuado no es un índice vectorial pre-construido. Es una herramienta que el sistema puede invocar en tiempo real.

---

## El capítulo que viene: herramientas

El Capítulo 07 introduce la capacidad de uso de herramientas (tool use o function calling): la posibilidad de que el sistema de IA invoque funciones definidas por el desarrollador para acceder a información o ejecutar acciones en tiempo real.

Donde RAG recupera fragmentos de texto de un índice pre-construido, las herramientas ejecutan operaciones: consultan una base de datos, llaman a una API, leen un archivo del sistema, envían un correo, ejecutan código.

La distinción es clara:

| Característica | RAG | Herramientas (Tool Use) |
|---|---|---|
| Tipo de información | Semiestructurada, no estructurada | Dinámica, transaccional, en tiempo real |
| Mecanismo | Búsqueda por similitud en índice pre-construido | Invocación de función en tiempo de ejecución |
| Actualización | Periódica (minutos a días) | Instantánea (la herramienta devuelve el estado actual) |
| Trazabilidad | Fragmento con metadatos de fuente | Resultado de la invocación con parámetros registrados |
| Adecuado para | Bases de conocimiento, documentación, políticas | Precios, estado de sistemas, datos transaccionales |

En la práctica, muchos sistemas de producción usan ambos mecanismos en la misma aplicación. El asistente de una empresa de logística puede usar RAG para responder preguntas sobre políticas de envío (conocimiento documental estable) y herramientas para consultar el estado actual de un envío específico (dato transaccional en tiempo real). No son competidores: son complementos con ámbitos de responsabilidad distintos.

---

## La distinción que el módulo fue construyendo

Esta distinción entre RAG y herramientas no es nueva en el módulo. El Capítulo 02 la introdujo al comparar las estrategias para superar los límites de la ventana de contexto: la recuperación externa (antecedente de RAG) y las herramientas aparecieron como dos formas de acceder a información que el sistema no tiene en el contexto inmediato.

El Capítulo 06 desarrolló en profundidad la primera. El Capítulo 07 desarrollará en profundidad la segunda.

Comprender ambas —y cuándo usar cada una— es una de las capacidades fundamentales del AI Engineer en el diseño de sistemas de contexto.

---

## Lo que se viene

El Capítulo 07 cubrirá:

- Qué es el function calling y cómo el modelo decide cuándo invocar una herramienta.
- Cómo se define y documenta una herramienta para que el modelo la use correctamente.
- Patrones de diseño para herramientas robustas: idempotencia, manejo de errores, timeouts.
- Herramientas de lectura versus herramientas de escritura y los distintos riesgos que presentan.
- Cómo combinar RAG y herramientas en la misma arquitectura de sistema.
- Anti-patrones: herramientas demasiado genéricas, herramientas sin validación de parámetros, herramientas que producen efectos secundarios no auditados.

---

## Una nota sobre la progresión del módulo

Al llegar al final del Capítulo 06, el módulo ha cubierto las cuatro estrategias fundamentales del Context Engineering:

1. **Instrucciones del sistema** (Capítulo 05): definición de comportamiento, rol y restricciones.
2. **Memoria conversacional** (Capítulo 04): continuidad entre turnos y sesiones.
3. **RAG** (Capítulo 06): conocimiento externo semiestructurado, recuperado por relevancia.
4. **Herramientas** (Capítulo 07): información dinámica y acciones en tiempo real.

Los capítulos que siguen integrarán estas estrategias en arquitecturas de mayor complejidad: agentes, pipelines multi-step, sistemas de evaluación y operaciones de IA a escala.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
