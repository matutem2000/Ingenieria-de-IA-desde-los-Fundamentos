# Capítulo 04 — Sección 13

# Checklist del AI Engineer

Este checklist cubre las decisiones de diseño que deben estar respondidas antes de llevar un sistema con memoria a producción. No es una lista de verificación de implementación —asume que la implementación ya está hecha— sino una lista de preguntas de diseño que, si no tienen respuesta, indican áreas de riesgo.

Organiza el checklist en cinco dimensiones: captura, almacenamiento, recuperación, ciclo de vida y privacidad.

---

## Dimensión 1: Captura

**¿Tengo criterios explícitos de qué se guarda y qué no?**
No basta con "lo que parece importante". Los criterios deben estar documentados y deben ser verificables: dado un fragmento de conversación, cualquier miembro del equipo debería poder decir si ese fragmento se guarda o no según los criterios.

**¿El sistema distingue entre hechos explícitos e inferidos?**
Los hechos que el usuario dijo directamente tienen mayor confiabilidad que los que el sistema infirió. El diseño debe reflejar esta diferencia —en el almacenamiento, en la recuperación y en cómo se presentan al modelo.

**¿El usuario sabe que sus datos están siendo capturados?**
No necesariamente con un pop-up legal, pero sí hay una expectativa razonable de transparencia. ¿La documentación del sistema lo menciona? ¿Hay alguna señal en la interfaz?

**¿El sistema captura en tiempo real o al cierre de sesión?**
Ambas opciones son válidas, pero la elección tiene consecuencias: la captura en tiempo real puede guardar fragmentos incompletos; la captura al cierre puede perder información si la sesión se interrumpe abruptamente.

---

## Dimensión 2: Almacenamiento

**¿El backend elegido es el correcto para el patrón de recuperación?**
Recuperación por ID exacto → key-value. Recuperación por similitud semántica → base de datos vectorial. Recuperación con queries complejas o joins → relacional. ¿El backend que elegiste hace bien lo que necesitas?

**¿Toda la memoria tiene `user_id` como metadato indexado?**
Es el requisito mínimo para poder: recuperar toda la memoria de un usuario, eliminar toda la memoria de un usuario, aislar la memoria entre usuarios. Sin `user_id` indexado, estas operaciones son caras o imposibles.

**¿El volumen de memoria esperado está dentro de los límites del backend elegido?**
Una base de datos vectorial self-hosted en un servidor modesto puede manejar millones de vectores. Una base de datos vectorial en memoria (Chroma sin persistencia) no escala más allá de decenas de miles. ¿Hiciste la estimación de volumen?

**¿Hay backups y recuperación ante fallos para el almacenamiento de memoria?**
La memoria es datos de usuario. Perder la base de datos de memoria no es solo un problema técnico —es una degradación de servicio que el usuario notará inmediatamente.

---

## Dimensión 3: Recuperación

**¿La recuperación filtra correctamente por usuario?**
En una base de datos vectorial sin filtro por `user_id`, una búsqueda semántica puede devolver memorias de otros usuarios con alta similitud. Este es un bug de privacidad, no solo un bug de calidad.

**¿Cuántos tokens ocupa la memoria inyectada en el peor caso?**
Si tienes un usuario con 500 memorias y no hay límite de recuperación, una consulta puede inyectar miles de tokens en el contexto. ¿Hay un límite definido de tokens o registros para la inyección de memoria?

**¿La recuperación tiene latencia aceptable?**
Una búsqueda vectorial sobre una colección pequeña toma milisegundos. Sobre una colección grande, puede tomar segundos. ¿El sistema tiene un timeout de recuperación? ¿Qué sucede si la recuperación falla?

**¿La memoria recuperada es relevante para el tipo de consulta?**
Haz una prueba manual: crea un conjunto de memorias de prueba para un usuario y verifica que para diez consultas distintas, la memoria recuperada es la que efectivamente ayuda a responder.

---

## Dimensión 4: Ciclo de vida

**¿Hay políticas de TTL o expiración para distintos tipos de memoria?**
Si toda la memoria persiste indefinidamente, el sistema producirá comportamientos basados en información desactualizada. ¿Tienes TTL diferenciados por tipo de dato?

**¿El sistema resuelve conflictos cuando captura información contradictoria?**
Sin resolución de conflictos, la memoria acumula versiones contradictorias del mismo hecho. ¿El sistema detecta y resuelve esto?

**¿Hay un proceso de consolidación para memorias episódicas acumuladas?**
Con el tiempo, docenas de memorias episódicas sobre el mismo tema deberían consolidarse en una memoria semántica. Sin consolidación, el sistema crece sin control y la recuperación se degrada.

**¿El sistema ha sido probado después de 6 meses de uso simulado?**
Muchos problemas de memoria —acumulación de ruido, información desactualizada, conflictos no resueltos— solo emergen después de un período prolongado de uso. ¿Tienes un test de carga temporal?

---

## Dimensión 5: Privacidad y control del usuario

**¿El usuario puede ver qué recuerda el sistema sobre él?**
Si la respuesta es no, el usuario no tiene ningún mecanismo de control sobre su propia información. Esto es un problema de diseño y potencialmente un problema legal.

**¿El usuario puede eliminar memorias específicas?**
Ver no es suficiente. El usuario debe poder eliminar registros incorrectos o que no quiere que el sistema recuerde.

**¿La eliminación completa de memoria de un usuario está implementada y probada?**
No solo "implementada" en el sentido de que hay una función. Probada: ejecuta la eliminación para un usuario de prueba y verifica que no queda ningún registro —ni en el vector store, ni en el key-value, ni en ningún caché.

**¿El sistema cumple con las regulaciones de privacidad aplicables en los países donde opera?**
GDPR (Europa), LGPD (Brasil), Ley 25.326 (Argentina), CCPA (California) tienen distintos requisitos sobre retención, eliminación y transparencia. ¿El equipo legal revisó el diseño?

**¿Hay un proceso documentado para responder solicitudes de eliminación?**
Cuando un usuario solicita que se eliminen sus datos, ¿hay un proceso claro de quién lo recibe, quién lo ejecuta y cómo se confirma que se ejecutó correctamente?

---

## Puntuación del checklist

Cada pregunta del checklist tiene tres posibles estados:

- **Sí / Resuelto:** el diseño contempla esto explícitamente.
- **Parcialmente / En progreso:** existe una solución incompleta o en desarrollo.
- **No / Pendiente:** no hay diseño para esto todavía.

Un sistema listo para producción debería tener todas las preguntas en "Sí" o con un plan documentado para las que están en "Parcialmente". Cualquier pregunta en "No" representa un riesgo conocido que el equipo debería aceptar de forma explícita, no ignorar.

---

*La siguiente sección es el resumen del capítulo: los conceptos centrales consolidados, las conexiones con otros capítulos del módulo, y las ideas que el lector debería llevarse como puntos de partida para su propio trabajo de diseño.*
