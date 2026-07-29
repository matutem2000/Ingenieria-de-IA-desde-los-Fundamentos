# Capitulo-01-Seccion-02-v1.0

# La evolución de la interacción con los modelos de IA

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Toda disciplina madura atraviesa un proceso de evolución. En el caso de la Ingeniería de IA, esa evolución fue especialmente rápida. Entre 2022 y 2026 el foco pasó de aprender a formular preguntas a diseñar sistemas completos capaces de proporcionar a un modelo toda la información necesaria para resolver un problema.

Comprender esta evolución ayuda a entender por qué hoy hablamos de **Context Engineering** y no solamente de **Prompt Engineering**.

---

# Primera etapa: el prompt como protagonista

Con la aparición de los primeros LLM de uso masivo, el éxito dependía principalmente de cómo se redactaba una instrucción.

Los usuarios experimentaban con:

- prompts más largos;
- ejemplos (few-shot);
- definición de roles;
- cadenas de razonamiento;
- restricciones de formato.

En esa etapa el prompt era prácticamente el único mecanismo de control.

---

# Segunda etapa: herramientas y conocimiento externo

Pronto surgió una limitación evidente: los modelos no conocían información actualizada ni podían interactuar con sistemas externos.

Para superar esa barrera aparecieron nuevas capacidades:

- recuperación de documentos (RAG);
- llamadas a funciones (Function Calling);
- herramientas especializadas;
- búsquedas web;
- acceso a bases de datos.

El modelo dejó de responder únicamente con su conocimiento entrenado y comenzó a trabajar con información dinámica.

---

# Tercera etapa: memoria y estado

Los asistentes modernos ya no resuelven una única consulta aislada.

Necesitan recordar:

- quién es el usuario;
- qué ocurrió anteriormente;
- qué tareas están en ejecución;
- cuáles son sus preferencias;
- qué herramientas utilizó.

La conversación se transforma en un proceso continuo y el contexto adquiere una dimensión temporal.

---

# Cuarta etapa: Context Engineering

En la actualidad el desafío consiste en decidir:

- qué información incorporar;
- cuál debe descartarse;
- cuándo recuperar conocimiento;
- cómo organizar la memoria;
- qué herramientas utilizar;
- qué restricciones aplicar.

Estas decisiones forman parte del diseño de una arquitectura de contexto.

El AI Engineer ya no optimiza únicamente un prompt: optimiza el flujo completo de información que rodea al modelo.

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

# Caso práctico

Imagine un asistente para una mesa de ayuda.

En 2023 bastaba con escribir:

> "Clasificá este incidente."

En una solución moderna el sistema también proporciona:

- perfil del usuario;
- historial de incidentes;
- documentación técnica;
- políticas internas;
- resultados de búsquedas;
- estado del ticket;
- herramientas para consultar inventario.

El modelo produce una respuesta basada en todos esos elementos, no únicamente en el texto enviado por el usuario.

---

# Conclusiones

El Prompt Engineering continúa siendo una habilidad esencial, pero representa solo una parte de una disciplina mucho más amplia.

El Context Engineering incorpora arquitectura, integración, memoria, recuperación de conocimiento y administración del estado para construir soluciones empresariales robustas.

En la próxima sección estudiaremos la anatomía del contexto y analizaremos cada uno de sus componentes de forma individual.
