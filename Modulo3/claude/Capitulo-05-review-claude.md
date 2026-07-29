# Informe Pedagógico — Capítulo 05: Diseño de Instrucciones del Sistema (System Instructions Engineering)

**Revisado por:** Director Pedagógico / Claude
**Fecha:** 2026-07-25

---

## NOTA EDITORIAL PRIORITARIA

**El capítulo está en estado de esqueleto estructural. No existe contenido desarrollado en ninguna de sus 15 secciones.** Cada sección contiene únicamente: título, nota editorial de contexto, lista de objetivos genéricos, lista de elementos "previstos" y una frase de transición estándar.

**El capítulo no puede publicarse ni revisarse pedagógicamente en profundidad hasta que el contenido sea desarrollado.**

---

## 1. Fortalezas

**El tema es el más práctico e inmediatamente aplicable del módulo.** El diseño de instrucciones del sistema es la primera habilidad que cualquier AI Engineer ejerce al construir una aplicación. Que este capítulo exista en el módulo de Context Engineering —y no en el de Prompt Engineering— es una decisión editorial correcta: sitúa las instrucciones del sistema dentro de la arquitectura completa del contexto en lugar de tratarlas como un ejercicio de redacción.

**La secuencia planificada de 15 secciones es progresiva y bien estructurada:**
- Secciones 01-02: marco conceptual (rol de las instrucciones, jerarquía de instrucciones en un LLM)
- Sección 03: anatomía de una system prompt profesional
- Secciones 04-08: tipos de problemas y decisiones de diseño
- Secciones 09-10: errores frecuentes y caso de estudio
- Secciones 11-15: laboratorio, checklist, cierre y transición

**La inclusión de "Instrucciones para agentes y uso de herramientas" (sección 07)** es un aporte diferencial. La mayoría de los tratamientos de system prompts se centran en asistentes conversacionales. Diseñar instrucciones para agentes que usan herramientas es un problema diferente y más complejo.

**La sección 06 ("Separación entre instrucciones y contexto dinámico")** ataca uno de los errores más comunes en producción: mezclar reglas permanentes con datos temporales en la capa de sistema. Es el concepto más importante del capítulo desde el punto de vista de arquitectura.

**La posición del capítulo en el módulo es correcta.** Viene después de memoria (capítulo 04) y antes de RAG (capítulo 06). Las instrucciones del sistema son la capa más estable del contexto; estudiarlas aquí, después de entender cómo funciona la memoria y antes de entender la recuperación dinámica, tiene sentido arquitectónico.

---

## 2. Debilidades

**La totalidad del contenido está ausente.** No hay definiciones, ejemplos de system prompts completos, patrones, anti-patrones, casos de uso ni notas del arquitecto.

**La sección 02 ("Jerarquía de instrucciones en un LLM")** promete uno de los temas más técnicamente complejos del capítulo: cómo los LLMs modernos priorizan instrucciones conflictivas entre el nivel de sistema, el nivel de usuario y el nivel de herramienta. Este tema fue mencionado en el capítulo 01 (sección 05) sin desarrollo. Si el capítulo 05 tampoco lo desarrolla con profundidad, existirá una deuda técnica acumulada de tres capítulos.

**La denominación "System Instructions Engineering" en el subtítulo** sugiere un nivel de formalización mayor que el del Prompt Engineering, pero sin contenido no es posible evaluar si el capítulo justifica esa denominación o si es solo un rótulo aspiracional.

**El capítulo 02 ya desarrolló la sección "Las instrucciones del sistema: el ADN del contexto" (sección 03 del capítulo 02).** Este capítulo debe agregar una capa de profundidad técnica significativa para no repetir lo ya cubierto. Sin contenido, no es posible confirmar si eso ocurrirá.

---

## 3. Conceptos a ampliar (recomendaciones para el desarrollo)

Los siguientes temas son críticos para que el capítulo justifique su extensión de 15 secciones:

**Plantillas de system prompt profesionales:** El lector necesita ver al menos tres ejemplos completos de instrucciones de sistema para dominios diferentes (soporte técnico, asistente jurídico, agente de análisis de datos), con comentarios que expliquen cada decisión.

**Jerarquía de instrucciones en LLMs modernos (sección 02):** Los modelos actuales tienen niveles de prioridad: instrucciones del operador (system prompt), instrucciones del usuario, instrucciones incluidas en documentos recuperados. El capítulo debe explicar cómo funciona esta jerarquía y cómo el diseñador puede influir en ella.

**Instrucciones para agentes con herramientas (sección 07):** Qué información debe incluirse en las instrucciones del sistema cuando el modelo tiene acceso a herramientas: descripción de capacidades disponibles, criterios de cuándo usar cada herramienta, manejo de errores y límites de autonomía.

**Versionamiento de instrucciones del sistema:** Las instrucciones del sistema evolucionan durante el ciclo de vida de una aplicación. El capítulo debería incluir una sección sobre cómo gestionar cambios, probar el impacto de modificaciones y mantener compatibilidad.

**Prompt injection y resistencia en instrucciones de sistema:** Cómo redactar instrucciones que sean robustas frente a intentos del usuario de modificar el comportamiento del sistema. Este es un tema de seguridad que conecta con el capítulo 14 pero debe anticiparse aquí.

---

## 4. Conceptos a resumir o eliminar

En el estado actual no hay contenido para resumir o eliminar.

Como advertencia preventiva: existe riesgo de redundancia con el capítulo 02 (sección 03: "Las instrucciones del sistema: el ADN del contexto") y con el Módulo 2 de Prompt Engineering. El autor debe verificar qué contenido sobre system prompts ya fue desarrollado en módulos anteriores y asegurarse de que este capítulo agregue profundidad técnica real, no solo extensión.

---

## 5. Recomendaciones editoriales

1. **Desarrollar las 15 secciones** antes de cualquier revisión pedagógica posterior.

2. **Abrir la sección 01 desde el capítulo 02** (que describió las instrucciones del sistema como "el ADN del contexto") y declarar explícitamente qué nivel de profundidad adicional aportará este capítulo respecto a lo ya visto.

3. **Incluir en la sección 03 al menos dos ejemplos completos de system prompts profesionales** (800-1200 tokens cada uno), con anotaciones que expliquen la función de cada bloque. Un ejemplo sin anotaciones tiene poco valor pedagógico para este público.

4. **Desarrollar la sección 02 con rigor técnico**: explicar el modelo de confianza de los principales proveedores (Anthropic Constitutional AI, OpenAI system/user/tool levels) y cómo esto afecta el diseño.

5. **La sección 06 ("Separación entre instrucciones y contexto dinámico")** debe incluir un anti-patrón concreto (una instrucción de sistema que incluye datos dinámicos) y mostrar cómo refactorizarla.

6. **Diseñar el laboratorio (sección 11)** para que el estudiante construya una instrucción de sistema completa para un caso empresarial, la pruebe con diferentes entradas y la refine en dos iteraciones. Incluir criterios de evaluación explícitos.

7. **Conectar la sección 07** (instrucciones para agentes) con una referencia anticipada al capítulo 08 (Agentes de IA), dejando claro que el tema se profundizará más adelante.

8. **El esquema del capítulo es sólido.** Una vez desarrollado el contenido, este capítulo tiene potencial para ser uno de los más prácticos y aplicables del módulo.
