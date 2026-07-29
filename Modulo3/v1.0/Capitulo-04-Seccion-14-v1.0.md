# Capítulo 04 — Sección 14

# Resumen del capítulo

Este capítulo convirtió la memoria de una estrategia de administración del contexto —como la nombramos en el capítulo anterior— en una disciplina de diseño con componentes, patrones y criterios propios.

## Los conceptos centrales

**La taxonomía cognitiva como marco de diseño.** Los cuatro tipos de memoria de la psicología cognitiva —de trabajo, episódica, semántica y procedimental— mapean directamente sobre los componentes de un sistema de memoria de IA. Este mapeó nos dio el vocabulario para distinguir tipos de información que requieren tratamientos radicalmente distintos: la ventana de contexto es memoria de trabajo; el historial de conversaciones es memoria episódica; el perfil del usuario es memoria semántica; las instrucciones del sistema son memoria procedimental.

**Los cinco componentes de la arquitectura de memoria.** Todo sistema de memoria pasa por los mismos cinco pasos: captura (¿qué vale la pena recordar?), procesamiento (¿cómo se estructura?), almacenamiento (¿dónde y con qué backend?), recuperación (¿qué es relevante para esta consulta?) e inyección (¿cómo se incorpora al contexto activo?). Un fallo en cualquiera de estos componentes degrada la calidad de todo el sistema.

**Las estrategias de memoria conversacional.** Para gestionar el historial dentro de una sesión, hay cuatro enfoques con trade-offs distintos: historial completo (máxima coherencia, costo alto), ventana deslizante (costo controlado, pérdida de contexto antiguo), resumen progresivo (preserva información a menor costo en tokens) e híbrida (mayor robustez, mayor complejidad). La elección depende de la longitud típica de las conversaciones y de la criticidad de la información histórica.

**Los backends de almacenamiento persistente y cuándo elegir cada uno.** Key-value stores para perfiles estructurados de acceso por ID. Bases de datos vectoriales para recuperación semántica por similitud. Grafos de conocimiento para relaciones complejas entre entidades. La elección del backend debe seguir al patrón de recuperación, no al revés.

**La distinción entre memoria semántica y RAG.** La memoria semántica es conocimiento construido por la aplicación sobre el usuario y el dominio de uso. RAG es conocimiento recuperado de documentos externos. Ambos usan tecnologías similares, pero resuelven problemas distintos. Un sistema completo puede tener ambos; un ingeniero que los confunde diseña mal ambos.

**El olvido como función de diseño.** La consolidación y el olvido deliberado son componentes tan críticos como la captura. Los sistemas que no diseñan el olvido acumulan ruido, mantienen información desactualizada y crecen sin control. Las políticas de retención deben ser explícitas, con TTL diferenciados por tipo de información y mecanismos de resolución de conflictos cuando la nueva información contradice la anterior.

**Los patrones que funcionan.** Memory Store (abstracción del backend), Context Assembler (selección y priorización para inyección), Memory Extractor (captura selectiva vía LLM), Memory Updater con upsert semántico (resolución de conflictos), y Sesión con Checkpoint (resiliencia ante interrupciones).

**Los anti-patrones que no funcionan.** Memoria esponja (guardar todo), context dumping (inyectar todo sin filtro), memoria muerta (sin actualización), memoria fantasma (sin TTL), memoria opaca (sin control del usuario) y hardcoding de contexto (contexto estático en lugar de memoria dinámica).

## Las conexiones con el resto del módulo

Este capítulo es el punto de articulación entre varios temas del módulo:

**Hacia atrás:** la memoria es la cuarta estrategia de administración del contexto que el capítulo 03 identificó. Este capítulo la desarrolló en profundidad técnica.

**Hacia adelante — Capítulo 06 (RAG):** la memoria semántica y RAG son complementarios. Este capítulo estableció que la memoria semántica gestiona el conocimiento sobre el usuario y el dominio de uso; RAG gestiona el conocimiento sobre documentos externos. El capítulo 06 desarrollará la arquitectura RAG en su totalidad.

**Hacia adelante — Capítulo 09 (Arquitecturas Multiagente):** la memoria compartida entre agentes introduce complejidad adicional: el olvido debe ser coordinado, las escrituras concurrentes deben ser gestionadas, y la consistencia de la memoria entre múltiples agentes es un problema de diseño distribuido. El capítulo 09 lo desarrollará desde la perspectiva de la arquitectura multiagente.

**Hacia adelante — Capítulo 14 (Seguridad y Privacidad):** el diseño de memoria tiene implicancias directas de privacidad: qué se guarda, durante cuánto tiempo, quién puede acceder, cómo se elimina bajo solicitud. El checklist de la sección anterior anticipa esas consideraciones; el capítulo 14 las desarrolla en el contexto regulatorio completo.

## Lo que el ingeniero debería llevarse

El diseño de memoria no es un problema de almacenamiento resuelto con una base de datos vectorial. Es un problema de criterio:

- Criterio sobre qué guardar.
- Criterio sobre cuánto tiempo guardar.
- Criterio sobre qué recuperar y cuánto recuperar.
- Criterio sobre qué olvidar y cuándo.
- Criterio sobre qué controles tiene el usuario sobre su propia información.

Un sistema de memoria bien diseñado no es el que recuerda más. Es el que recuerda lo correcto, con la granularidad correcta, durante el tiempo correcto, y olvida el resto de forma limpia.

---

*La última sección del capítulo es la autoevaluación: preguntas de comprensión y ejercicios de reflexión que permiten al lector verificar que los conceptos centrales están asentados antes de continuar.*
