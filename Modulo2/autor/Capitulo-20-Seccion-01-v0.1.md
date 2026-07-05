# Capitulo-20-Seccion-01-v0.1

# Módulo 2 — Prompt Engineering Profesional

# Capítulo 20 — Arquitecturas Basadas en Prompts

**Versión:** 0.1  
**Estado:** Manuscrito del autor

> *"Cuando un prompt deja de ser una instrucción aislada y pasa a formar parte de una arquitectura, comienza la verdadera ingeniería."*

---

# Objetivos de aprendizaje

- Comprender el concepto de arquitecturas basadas en prompts.
- Diferenciar un prompt aislado de un componente arquitectónico.
- Analizar el papel de los prompts dentro de aplicaciones empresariales.
- Introducir principios de composición y reutilización.

---

# Introducción

Durante los capítulos anteriores estudiamos cómo diseñar prompts, cómo evaluarlos, cómo operarlos en producción y cómo integrarlos en conversaciones de larga duración.

Sin embargo, una aplicación moderna rara vez utiliza un único prompt.

Es habitual encontrar decenas o cientos de prompts especializados, cada uno responsable de una tarea concreta: clasificación, extracción de información, planificación, generación de respuestas, validación o coordinación de herramientas.

El desafío deja de ser escribir un buen prompt y pasa a ser **organizar un ecosistema de prompts**.

---

# Del prompt al componente

En AI Engineering, un prompt debe tratarse como cualquier otro componente de software.

Posee una responsabilidad específica, una interfaz de entrada, una salida esperada y un ciclo de vida propio.

```mermaid
flowchart LR
A[Aplicación]
--> B[Prompt de clasificación]
B --> C[Prompt de extracción]
C --> D[Prompt de razonamiento]
D --> E[Prompt de generación]
E --> F[Respuesta]
```

Cada prompt puede evolucionar independientemente siempre que mantenga su contrato funcional.

---

# Características de una arquitectura basada en prompts

Una arquitectura madura suele incorporar:

| Característica | Beneficio |
|----------------|-----------|
| Modularidad | Prompts con responsabilidades claras. |
| Reutilización | Un mismo prompt puede utilizarse en distintos procesos. |
| Bajo acoplamiento | Cambios locales con menor impacto global. |
| Versionado independiente | Evolución controlada de cada componente. |
| Observabilidad | Métricas por prompt y por flujo. |

---

# Responsabilidades bien definidas

Un error frecuente consiste en construir un único prompt gigantesco que intenta resolver todo el problema.

Este enfoque incrementa la complejidad, dificulta las pruebas y reduce la reutilización.

Una alternativa consiste en dividir la solución en componentes especializados:

- clasificación;
- recuperación de contexto;
- planificación;
- validación;
- generación de respuesta.

Cada componente puede evaluarse y evolucionar por separado.

---

# Caso de estudio

Una organización desarrolla un asistente para gestionar expedientes.

Inicialmente utiliza un único prompt para interpretar la consulta, recuperar información, analizar normativa y generar la respuesta.

Con el crecimiento del proyecto aparecen dificultades para mantener el sistema.

El equipo decide separar esas responsabilidades en prompts especializados conectados mediante un flujo de orquestación.

La solución mejora su mantenibilidad, facilita las pruebas y reduce el impacto de futuras modificaciones.

---

# Buenas prácticas

- Diseñar prompts con una única responsabilidad.
- Definir contratos claros entre componentes.
- Favorecer la reutilización.
- Versionar cada prompt de forma independiente.

---

# Errores frecuentes

- Concentrar toda la lógica en un único prompt.
- Acoplar prompts a un caso de uso específico.
- No documentar entradas y salidas.
- Impedir la reutilización mediante diseños excesivamente rígidos.

---

# Ideas clave

- Un prompt puede convertirse en un componente arquitectónico.
- La modularidad facilita la evolución de la solución.
- La arquitectura debe organizar los prompts igual que organiza servicios o módulos de software.

---

# Transición hacia la siguiente sección

En la próxima sección estudiaremos patrones de composición de prompts y analizaremos cómo construir flujos reutilizables que integren múltiples componentes dentro de una misma solución de AI Engineering.

---

> **"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."**
