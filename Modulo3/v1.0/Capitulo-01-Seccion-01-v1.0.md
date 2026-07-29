# El nacimiento del Context Engineering

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Durante los primeros años de adopción de los modelos de lenguaje, la mayor parte del esfuerzo de los usuarios se concentró en aprender a escribir mejores prompts. La disciplina conocida como *Prompt Engineering* permitió descubrir que pequeños cambios en la forma de redactar una instrucción podían producir diferencias significativas en la calidad de las respuestas.

Sin embargo, a medida que los modelos evolucionaron, también lo hicieron las aplicaciones construidas sobre ellos. Los asistentes conversacionales dejaron de responder únicamente a una pregunta aislada y comenzaron a interactuar con herramientas, consultar bases de conocimiento, mantener memoria de conversaciones anteriores y ejecutar acciones sobre sistemas externos.

En ese nuevo escenario apareció un problema evidente: un excelente prompt ya no era suficiente.

Lo verdaderamente importante pasó a ser **todo el contexto** que recibe el modelo antes de generar una respuesta. El contexto puede definirse como:

> **Toda la información disponible para el modelo en el instante en que debe generar una respuesta.**

Esta definición incluye mucho más que el mensaje del usuario: instrucciones del sistema, historial conversacional, memoria persistente, documentos recuperados mediante RAG, resultados de herramientas, datos del usuario, políticas de seguridad y restricciones del dominio.

---

# Objetivos de esta sección

Al finalizar esta sección el lector podrá:

- Comprender por qué Prompt Engineering dejó de ser suficiente.
- Diferenciar un prompt de una arquitectura de contexto.
- Entender el concepto moderno de Context Engineering.
- Identificar los componentes que forman el contexto de un LLM.

---

# La evolución hacia el Context Engineering

Toda disciplina madura atraviesa un proceso de evolución. En el caso de la Ingeniería de IA, esa evolución fue especialmente rápida. Entre 2022 y 2026 el foco pasó de aprender a formular preguntas a diseñar sistemas completos capaces de proporcionar a un modelo toda la información necesaria para resolver un problema.

**Primera etapa: el prompt como protagonista.** Con la aparición de los primeros LLM de uso masivo, el éxito dependía principalmente de cómo se redactaba una instrucción. Los usuarios experimentaban con prompts más largos, ejemplos *few-shot*, definición de roles, cadenas de razonamiento y restricciones de formato. En esa etapa el prompt era prácticamente el único mecanismo de control.

**Segunda etapa: herramientas y conocimiento externo.** Pronto surgió una limitación evidente: los modelos no conocían información actualizada ni podían interactuar con sistemas externos. Para superar esa barrera aparecieron la recuperación de documentos (RAG), las llamadas a funciones (*Function Calling*), las búsquedas web y el acceso a bases de datos. El modelo comenzó a trabajar con información dinámica.

**Tercera etapa: memoria y estado.** Los asistentes modernos ya no resuelven una única consulta aislada. Necesitan recordar quién es el usuario, qué ocurrió anteriormente, qué tareas están en ejecución y cuáles son sus preferencias. La conversación se transforma en un proceso continuo y el contexto adquiere una dimensión temporal.

**Cuarta etapa: Context Engineering.** En la actualidad el desafío consiste en decidir qué información incorporar, cuál debe descartarse, cuándo recuperar conocimiento, cómo organizar la memoria, qué herramientas utilizar y qué restricciones aplicar. Estas decisiones forman parte del diseño de una arquitectura de contexto. El AI Engineer ya no optimiza únicamente un prompt: optimiza el flujo completo de información que rodea al modelo.

---

# Definición

**Context Engineering** es la disciplina que diseña, organiza y administra toda la información que un modelo de IA recibe durante una interacción para maximizar la calidad, precisión y utilidad de sus respuestas.

No se trata únicamente de escribir instrucciones. Se trata de decidir:

- qué información enviar;
- cuándo enviarla;
- en qué formato;
- con qué prioridad;
- durante cuánto tiempo conservarla.

Estas decisiones constituyen problemas de arquitectura y no simplemente de redacción.

---

# Comparación

| Prompt Engineering | Context Engineering |
|--------------------|--------------------|
| Optimiza una instrucción | Optimiza todo el contexto |
| Centrado en el prompt | Centrado en el sistema |
| Resultado puntual | Conversaciones persistentes |
| Poco estado | Gestión de memoria |
| Sin herramientas | Integración de herramientas y datos |

---

# Caso de estudio

Imagine un asistente corporativo para un sistema de tickets.

Si únicamente recibe el mensaje:

> "Mostrame los incidentes críticos."

la respuesta dependerá completamente del contexto disponible.

Si además conoce la identidad del usuario, su área de trabajo, el idioma preferido, los permisos asignados, el estado actual de los incidentes, la fecha y hora, y las políticas internas de la organización, la respuesta será considerablemente más precisa y útil.

La diferencia no la produjo un mejor prompt, sino un mejor contexto.

---

# Ideas clave

- Los prompts siguen siendo importantes.
- El contexto es más amplio que el prompt.
- La arquitectura del contexto determina gran parte de la calidad de una solución basada en IA.
- Context Engineering constituye una competencia fundamental para cualquier AI Engineer moderno.

---

# Resumen

El Prompt Engineering continúa siendo una habilidad valiosa, pero ya no resulta suficiente para construir soluciones empresariales complejas. Este módulo estudia cómo diseñar arquitecturas completas de contexto capaces de alimentar a un modelo con la información adecuada en el momento correcto.

En la siguiente sección analizaremos en detalle todos los componentes que conforman el contexto de un modelo de lenguaje moderno.
