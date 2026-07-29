# Patrones de administración del contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Ninguna estrategia de administración del contexto sirve para todos los casos. La elección del patrón correcto depende del tipo de aplicación, la naturaleza del conocimiento que debe gestionarse, el presupuesto disponible y la complejidad que el equipo puede sostener en producción.

En esta sección describimos los cuatro patrones arquitectónicos más utilizados en aplicaciones profesionales. Cada uno define una forma distinta de organizar el contexto: qué se conserva, qué se descarta, qué se recupera y cómo se combinan las distintas fuentes de información.

---

# Patrón 1: Sliding Window (Ventana deslizante)

## Descripción

La Sliding Window conserva únicamente las últimas N interacciones de la conversación. Cuando se agrega un nuevo mensaje, el más antiguo del conjunto se elimina para mantener el tamaño del contexto constante.

```text
Solicitud N:   [sistema] [msg-6] [msg-7] [msg-8] [usuario]
Solicitud N+1: [sistema] [msg-7] [msg-8] [nuevo] [usuario]
```

El system prompt permanece fijo; solo el historial rota.

## Cuándo utilizarlo

- Conversaciones de soporte o atención donde cada consulta es mayoritariamente independiente.
- Aplicaciones de chat general donde el contexto reciente es más relevante que el histórico.
- Prototipos y sistemas que necesitan una solución simple y predecible.

## Ventajas

- Implementación trivial: solo requiere mantener una lista y eliminar el elemento más antiguo.
- Costo predecible: el tamaño del contexto nunca crece más allá de N mensajes.
- Latencia estable: no depende de operaciones externas de recuperación.

## Compromisos

- Pierde información histórica. Si el usuario retoma un tema tratado hace veinte turnos, el modelo no tendrá acceso a ese contexto.
- No escala bien para sesiones de larga duración donde la continuidad histórica es importante.
- La elección del valor N implica un equilibrio entre cobertura histórica y costo.

---

# Patrón 2: Summary + Window (Resumen más ventana reciente)

## Descripción

Este patrón combina un bloque de resumen histórico con una ventana de los mensajes más recientes. El resumen se actualiza periódicamente —al final de cada sesión, cada N mensajes o cuando el historial supera un umbral— y captura las decisiones, hechos y compromisos acumulados.

```text
Contexto: [sistema] [resumen-histórico] [msg-reciente-1] [msg-reciente-2] [usuario]
```

El resumen actúa como memoria de trabajo comprimida; los mensajes recientes aportan el contexto inmediato.

## Cuándo utilizarlo

- Asistentes empresariales con sesiones de trabajo continuas a lo largo de días o semanas.
- Agentes que gestionan proyectos o tareas de larga duración.
- Cualquier aplicación donde la continuidad histórica importa pero el historial completo no cabe en la ventana.

## Ventajas

- Equilibra continuidad histórica con eficiencia de tokens.
- Permite conversaciones de duración indefinida sin perder el hilo.
- El resumen puede auditarse y corregirse manualmente en aplicaciones críticas.

## Compromisos

- La calidad del sistema depende de la calidad del resumen. Un resumen deficiente propaga errores.
- Requiere decidir cuándo y cómo actualizar el resumen, lo que agrega complejidad al ciclo de vida de la sesión.
- El resumen mismo consume tokens; si es demasiado detallado, pierde su ventaja sobre el historial completo.

---

# Patrón 3: RAG First (Recuperación prioritaria)

## Descripción

En el patrón RAG First, el conocimiento permanente de la aplicación —manuales, políticas, documentación técnica, bases de datos— no reside en el contexto de forma fija. Se recupera en tiempo real para cada consulta, seleccionando solo los fragmentos relevantes según el contenido del mensaje del usuario.

```text
Consulta del usuario
        │
        ▼
  Sistema de recuperación (embeddings + búsqueda)
        │
        ▼
  Top-K documentos relevantes
        │
        ▼
Contexto: [sistema] [doc-1] [doc-2] [historial-reciente] [usuario]
```

El historial conversacional puede combinarse con los documentos recuperados o administrarse por separado.

## Cuándo utilizarlo

- Aplicaciones de búsqueda sobre bases de conocimiento extensas: manuales técnicos, repositorios de políticas, catálogos de productos.
- Sistemas donde la documentación cambia con frecuencia y mantenerla en el system prompt sería impracticable.
- Cualquier caso donde el conocimiento relevante para una consulta es una fracción pequeña de un conjunto grande.

## Ventajas

- El contexto siempre contiene información actualizada: modificar la base de conocimiento no requiere cambiar el system prompt.
- Eficiente en tokens: solo se incluye lo relevante para cada consulta específica.
- Escalable a bases de conocimiento de cualquier tamaño.

## Compromisos

- La calidad de las respuestas depende de la calidad de la recuperación. Si los documentos recuperados no son los correctos, el modelo no podrá responder bien aunque la respuesta exista en la base.
- Agrega latencia por la operación de búsqueda y la distancia de embeddings.
- Requiere mantener un índice vectorial actualizado y un pipeline de indexación.

---

# Patrón 4: Memoria + Historial + RAG (Arquitectura de tres capas)

## Descripción

Este patrón combina los tres mecanismos anteriores asignando una responsabilidad específica y diferenciada a cada capa del contexto:

- **Memoria persistente:** hechos duraderos sobre el usuario, sus preferencias, su historial de interacciones anteriores. Se recupera al inicio de cada sesión.
- **Historial reciente:** los últimos mensajes del turno actual, con o sin resumen histórico.
- **Documentos RAG:** conocimiento técnico o documental recuperado en tiempo real para la consulta actual.

```text
Contexto: [sistema] [memoria-usuario] [resumen] [docs-RAG] [historial-reciente] [usuario]
```

Cada capa tiene su propio almacenamiento, su propia política de actualización y su propio ciclo de vida.

## Cuándo utilizarlo

- Asistentes de alto valor donde la personalización y la continuidad a largo plazo son requisitos del negocio.
- Agentes empresariales que coordinan múltiples dominios de conocimiento.
- Aplicaciones donde el usuario espera que el sistema "recuerde" quién es y qué ha pedido antes, al mismo tiempo que accede a documentación actualizada.

## Ventajas

- Ofrece la mayor continuidad y personalización posible.
- Cada capa puede optimizarse independientemente.
- Separa claramente las responsabilidades, lo que facilita el mantenimiento y la auditoría.

## Compromisos

- Es el patrón más complejo de implementar y operar.
- Requiere tres sistemas de almacenamiento distintos: base de memoria, sistema de vectores para RAG y almacén de historial.
- La coordinación entre capas puede introducir inconsistencias si no se gestiona correctamente.
- El costo operativo es significativamente mayor que los patrones simples.

---

# Guía de selección

| Caso de uso | Patrón recomendado |
|---|---|
| Chat simple o prototipo | Sliding Window |
| Conversaciones de larga duración | Summary + Window |
| Búsqueda sobre base de conocimiento | RAG First |
| Asistente empresarial personalizado | Memoria + Historial + RAG |

En la práctica, muchos sistemas evolucionan desde el patrón más simple hacia el más complejo a medida que los requisitos del negocio lo demandan. Comenzar con Sliding Window y agregar capas progresivamente es una estrategia de desarrollo sostenible.

---

# Buenas prácticas

- Elegir el patrón más simple que satisfaga los requisitos: la complejidad adicional tiene costos de desarrollo y operación reales.
- Documentar explícitamente qué capa del contexto es responsable de cada tipo de información.
- Implementar monitoreo independiente para cada capa: detectar qué capa falla cuando la calidad degrada.
- Planificar la evolución del patrón desde el inicio: un sistema diseñado solo para Sliding Window puede ser difícil de migrar a un patrón de tres capas sin refactorización importante.

---

# Resumen

Los cuatro patrones de administración del contexto —Sliding Window, Summary + Window, RAG First y Memoria + Historial + RAG— no son alternativas excluyentes en un catálogo fijo. Son puntos de referencia en un espacio de diseño continuo. La elección correcta depende del dominio, el presupuesto, la complejidad de los requisitos y la madurez del equipo.

En la próxima sección aplicaremos estos conceptos en un ejercicio práctico de diseño de contexto para una aplicación empresarial real.
