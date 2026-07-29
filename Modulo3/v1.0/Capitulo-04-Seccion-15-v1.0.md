# Capítulo 04 — Sección 15

# Autoevaluación y cierre

## Preguntas de comprensión conceptual

Las siguientes preguntas verifican que los conceptos centrales del capítulo están asentados. Responder bien estas preguntas no requiere memorizar definiciones: requiere entender las relaciones entre los conceptos.

**1.** Un colega propone guardar el transcript completo de cada conversación en la base de datos de memoria. ¿Cuáles son los dos problemas principales de esta decisión? ¿Qué propondrías en su lugar?

**2.** Tienes un sistema de asistencia para médicos. El médico menciona en una conversación que "el paciente con asma severa que vino ayer tiene contraindicación para betabloqueantes". ¿Deberías persistir esta información en memoria? ¿Por qué sí o por qué no? ¿Qué consideraciones adicionales aplican al contexto médico?

**3.** Explica con tus propias palabras la diferencia entre memoria episódica y memoria semántica en un sistema de IA. Da un ejemplo concreto de información que sería episódica y uno de información que sería semántica para un asistente de análisis financiero.

**4.** Un usuario te reporta que el sistema le está respondiendo con información de un proyecto que cerró hace cuatro meses. Diagnosifica el problema: ¿qué componente falló y cómo lo corregirías?

**5.** ¿Por qué la memoria semántica y RAG son complementarios y no intercambiables? Da un ejemplo de un caso de uso donde necesitarías ambos al mismo tiempo.

**6.** Un startup decide no implementar controles de privacidad sobre la memoria porque "están en fase de prototipo y se lo dejan para después". ¿Qué riesgos concretos introduce esta decisión? ¿Qué mínimo de control de privacidad recomendarías implementar incluso en un prototipo?

---

## Ejercicios de aplicación

**Ejercicio 1 — Diseño de política de retención**

Estás diseñando el sistema de memoria de un asistente para equipos de recursos humanos de una empresa mediana. El sistema interactúa con cinco tipos de usuarios: recruiters, HR Business Partners, gerentes de área, empleados en proceso de onboarding, y el equipo de compensaciones.

Diseña una tabla de política de retención que especifique:
- Los tres tipos de información más importantes que merece persistir para cada rol de usuario
- El TTL sugerido para cada tipo de información
- Los criterios para actualización vs. reemplazo de la información

**Ejercicio 2 — Diagnóstico de anti-patrón**

Lee el siguiente fragmento de arquitectura:

> "Al inicio de cada sesión, el sistema recupera los últimos 50 registros de memoria del usuario ordenados por fecha de creación y los inyecta completos en el system prompt. Durante la sesión, cada mensaje del usuario se analiza y todos los sustantivos propios se guardan como memorias nuevas. Al final de cada mes, un script manual elimina los registros más antiguos."

Identifica al menos tres anti-patrones en este diseño. Para cada uno, explica el problema y propone la corrección.

**Ejercicio 3 — Extensión del laboratorio**

Extiende el código del laboratorio (sección 12) para implementar el Ejercicio 1 del checklist de extensión: TTL automático. Define TTLs distintos para los cuatro tipos de memoria (preferencia, trabajo, decisión, restricción). Verifica que el filtrado funciona creando memorias con fecha de creación manual en el pasado.

**Ejercicio 4 — Caso de diseño**

Eres el ingeniero de IA en una plataforma de e-learning que usa un tutor conversacional de IA. El tutor trabaja con estudiantes universitarios en cursos de matemáticas, programación y estadística. Los estudiantes interactúan con el tutor múltiples veces por semana durante un semestre.

Diseña la arquitectura de memoria del tutor respondiendo:
1. ¿Qué tipos de memoria (episódica, semántica, procedimental) necesita el tutor?
2. ¿Qué información específica debería persistir sobre cada estudiante?
3. ¿Qué información no debería persistir nunca?
4. ¿Qué TTL aplicarías a cada categoría?
5. ¿Qué backend de almacenamiento elegiría para cada tipo y por qué?
6. ¿Qué controles de privacidad son especialmente importantes dado que los usuarios son estudiantes (potencialmente menores de edad)?

---

## Cierre del capítulo

La memoria transformó los sistemas de IA de herramientas de sesión única en colaboradores con continuidad. Esa transformación no ocurrió sola: ocurrió porque ingenieros diseñaron sistemas explícitos de captura, almacenamiento, recuperación y olvido.

Lo que este capítulo establece es que ese diseño es una disciplina con principios propios. No basta con conectar un LLM a una base de datos. Hay que decidir qué recordar, cómo organizarlo, qué recuperar en cada momento, durante cuánto tiempo mantenerlo activo, y cómo garantizar que el usuario tenga control sobre su propia información en el sistema.

Un sistema de memoria bien diseñado es invisible para el usuario: simplemente experimenta que el asistente lo conoce, lo entiende y no le hace repetir las mismas cosas una y otra vez. Un sistema de memoria mal diseñado es frustrante de formas específicas y predecibles: olvida lo importante, recuerda lo trivial, mezcla contextos, o no sabe olvidar cuando debería.

La diferencia entre ambos es el criterio del ingeniero que lo diseñó.

En el próximo capítulo extenderemos la arquitectura de contexto hacia el diseño de herramientas y function calling: cómo los sistemas de IA no solo recuerdan, sino que actúan sobre el mundo externo de forma controlada y verificable.

---

### Conceptos clave del capítulo

| Concepto | Definición en una línea |
|---|---|
| Memoria de trabajo | Ventana de contexto activa del modelo en la sesión actual |
| Memoria episódica | Registro de eventos e interacciones pasadas, situados en el tiempo |
| Memoria semántica | Conocimiento factual destilado sobre el usuario y el dominio |
| Memoria procedimental | Instrucciones y flujos que definen cómo actúa el sistema |
| Context Assembly | Proceso de seleccionar y priorizar qué memoria inyectar en el contexto |
| Upsert semántico | Insertar o actualizar una memoria según similitud con memorias existentes |
| TTL | Time To Live: tiempo durante el cual un registro de memoria es válido |
| Consolidación | Comprimir memorias episódicas acumuladas en memorias semánticas |
| Olvido deliberado | Política explícita de qué eliminar, cuándo y con qué criterio |
| Memory Store | Patrón que encapsula el acceso al backend de almacenamiento de memoria |
