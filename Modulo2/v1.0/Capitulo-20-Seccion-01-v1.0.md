# Módulo 2 — Prompt Engineering Profesional

# Capítulo 20 — Arquitecturas Basadas en Prompts

> *"Cuando un prompt deja de ser una instrucción aislada y pasa a formar parte de una arquitectura, comienza la verdadera ingeniería."*

---

## Objetivos de aprendizaje

- Comprender qué es una arquitectura basada en prompts y en qué se diferencia de un conjunto de prompts encadenados.
- Diferenciar un prompt aislado de un componente arquitectónico.
- Analizar el papel de los prompts dentro de aplicaciones empresariales.
- Introducir los principios fundamentales de composición y reutilización que guiarán el resto del capítulo.

---

## Introducción

Durante los capítulos anteriores estudiamos cómo diseñar prompts, cómo evaluarlos, cómo operarlos en producción y cómo integrarlos en conversaciones de larga duración.

Sin embargo, una aplicación moderna rara vez utiliza un único prompt.

Es habitual encontrar decenas o cientos de prompts especializados, cada uno responsable de una tarea concreta: clasificación, extracción de información, planificación, generación de respuestas, validación o coordinación de herramientas.

El desafío deja de ser escribir un buen prompt y pasa a ser **organizar un ecosistema de prompts**.

---

## Del prompt al componente

Antes de avanzar conviene precisar el término. En este capítulo, una **arquitectura basada en prompts** es una organización explícita de prompts especializados que se relacionan mediante contratos definidos, flujos de orquestación y responsabilidades claramente delimitadas. Lo que distingue a una arquitectura de una simple colección de prompts encadenados es que cada componente tiene una interfaz conocida, puede evolucionar de forma independiente y contribuye a un objetivo mayor sin acoplar su lógica interna al resto del sistema.

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

Cada prompt puede evolucionar independientemente siempre que mantenga su **contrato funcional**: el acuerdo sobre el formato de entrada que acepta y la salida que produce. Sin ese contrato, cualquier modificación en un componente se propaga en cascada hacia el resto del sistema.

---

## Características de una arquitectura basada en prompts

Una arquitectura madura suele incorporar las siguientes propiedades:

| Característica | Beneficio |
|----------------|-----------|
| Modularidad | Prompts con responsabilidades claras. |
| Reutilización | Un mismo prompt puede utilizarse en distintos procesos. |
| Bajo acoplamiento | Cambios locales con menor impacto global. |
| Versionado independiente | Evolución controlada de cada componente. |
| Observabilidad | Métricas por prompt y por flujo. |

Estas propiedades no son exclusivas del AI Engineering: son principios bien establecidos en la arquitectura de software que mantienen plena vigencia cuando el componente en cuestión es un prompt en lugar de un módulo de código.

---

## Responsabilidades bien definidas

Un error frecuente consiste en construir un único prompt gigantesco que intenta resolver todo el problema.

Este enfoque incrementa la complejidad, dificulta las pruebas y reduce la reutilización. Además, la lógica de negocio crítica queda enterrada dentro del prompt, fuera del control directo de la aplicación. La lógica de negocio debe permanecer bajo el control de la aplicación, no dentro del modelo.

Una alternativa consiste en dividir la solución en componentes especializados:

- clasificación;
- recuperación de contexto;
- planificación;
- validación;
- generación de respuesta.

Cada componente puede evaluarse y evolucionar por separado.

---

## Caso de estudio

Una organización desarrolla un asistente para gestionar expedientes.

Inicialmente utiliza un único prompt para interpretar la consulta, recuperar información, analizar normativa y generar la respuesta.

Con el crecimiento del proyecto aparecen dificultades para mantener el sistema: cualquier cambio en la normativa afecta al prompt completo y las pruebas deben repetirse íntegramente ante cada modificación.

El equipo decide separar esas responsabilidades en prompts especializados conectados mediante un flujo de orquestación. Cada componente expone un contrato claro: el prompt de clasificación recibe texto libre y devuelve una categoría; el de análisis normativo recibe la categoría y el expediente y devuelve una evaluación estructurada.

La solución mejora su mantenibilidad, facilita las pruebas y reduce el impacto de futuras modificaciones.

---

## Buenas prácticas

Los principios que se listan a continuación constituyen el fundamento de toda la discusión del capítulo. Las secciones siguientes añadirán únicamente las consideraciones específicas de cada patrón.

- Diseñar prompts con una única responsabilidad.
- Definir contratos claros entre componentes: qué entra, qué sale y en qué formato.
- Favorecer la reutilización frente al diseño ad hoc.
- Versionar cada prompt de forma independiente.
- Mantener la lógica de negocio crítica bajo el control de la aplicación, no dentro del prompt.

---

## Errores frecuentes

- Concentrar toda la lógica en un único prompt.
- Acoplar prompts a un caso de uso específico que impida su reutilización.
- No documentar las entradas y salidas de cada componente.
- Impedir la reutilización mediante diseños excesivamente rígidos.

---

## Ideas clave

- Un prompt puede convertirse en un componente arquitectónico con responsabilidad, interfaz y ciclo de vida propios.
- La modularidad facilita la evolución controlada de la solución.
- La arquitectura debe organizar los prompts con los mismos principios que aplica a servicios o módulos de software.

---

## Transición hacia la siguiente sección

En la próxima sección estudiaremos patrones de composición de prompts y analizaremos cómo construir flujos reutilizables que integren múltiples componentes dentro de una misma solución de AI Engineering.
