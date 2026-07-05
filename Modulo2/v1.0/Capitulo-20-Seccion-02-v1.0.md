# Módulo 2 — Prompt Engineering Profesional

# Capítulo 20 — Arquitecturas Basadas en Prompts

> *"Una arquitectura escalable no depende de componentes más grandes. Depende de componentes mejor organizados."*

---

## Objetivos de aprendizaje

- Comprender los principios de composición de prompts.
- Analizar estrategias para construir flujos reutilizables.
- Diseñar arquitecturas modulares basadas en prompts especializados.
- Introducir patrones de orquestación entre prompts.

---

## Introducción

La sección anterior estableció que un prompt puede actuar como componente arquitectónico con responsabilidad única, contrato definido y ciclo de vida propio. Pocas aplicaciones empresariales resuelven un problema con un único componente.

La mayoría implementa una secuencia de prompts especializados que colaboran entre sí para alcanzar un objetivo común. En esos casos, la calidad de la solución deja de depender únicamente del diseño individual de cada prompt y pasa a depender de la forma en que estos interactúan.

---

## Composición de prompts

La composición consiste en organizar varios prompts especializados para resolver un problema complejo mediante una secuencia de tareas más simples.

Cada componente recibe una entrada, produce una salida y delega el siguiente paso cuando corresponde.

```mermaid
flowchart LR
A[Consulta]
--> B[Prompt de clasificación]

B --> C[Prompt de recuperación]

C --> D[Prompt de análisis]

D --> E[Prompt de validación]

E --> F[Prompt de generación]

F --> G[Respuesta]
```

Este enfoque favorece la separación de responsabilidades y reduce el impacto de los cambios: cuando la normativa de validación cambia, solo se modifica el componente de validación.

---

## El contrato entre componentes

Un aspecto central de la composición es la definición del contrato entre componentes. Un contrato especifica qué información recibe un prompt, qué formato debe tener esa entrada y qué estructura tendrá la salida.

Por ejemplo, un prompt de clasificación podría recibir texto libre y comprometerse a devolver siempre un objeto con un campo `categoria` y un campo `confianza`. El componente siguiente sabe que puede consumir esa estructura sin procesamiento adicional.

Este acuerdo explícito permite sustituir o mejorar un componente sin afectar al resto del flujo, siempre que el nuevo componente respete el mismo contrato. Sin él, los componentes quedan acoplados a los detalles internos del anterior y cualquier cambio se propaga en cascada.

---

## Beneficios de la modularidad

Una arquitectura modular ofrece ventajas tanto técnicas como operativas que resultan familiares para cualquier arquitecto de software.

| Beneficio | Descripción |
|-----------|-------------|
| Reutilización | Un mismo prompt puede participar en distintos procesos. |
| Mantenibilidad | Los cambios afectan únicamente al componente involucrado. |
| Escalabilidad | Es posible incorporar nuevos módulos sin rediseñar toda la solución. |
| Observabilidad | Permite medir el comportamiento de cada etapa del flujo. |
| Pruebas independientes | Cada prompt puede validarse de forma aislada. |

---

## Patrones de composición

Existen diversas formas de organizar una arquitectura basada en prompts:

- **Pipeline secuencial:** cada prompt consume la salida del anterior.
- **Ramificación:** diferentes prompts resuelven tareas específicas en paralelo.
- **Convergencia:** múltiples resultados se integran en una respuesta unificada.
- **Orquestación condicional:** el flujo cambia según el resultado de una etapa previa.

Las secciones siguientes profundizan en estos patrones: la orquestación condicional se desarrolla en la Sección 03 a través del orquestador, y las cadenas y bifurcaciones en la Sección 04 mediante grafos de prompts.

Una consideración práctica que no debe ignorarse es el impacto acumulado sobre la latencia y el consumo de tokens. Cada componente adicional en la cadena suma tiempo de procesamiento y tokens al costo de la operación. Un diseño que encadena prompts sin una estrategia clara puede alcanzar rápidamente límites operativos que comprometan tanto el rendimiento como la economía de la solución.

---

## Caso de estudio

Una aseguradora implementa un asistente para gestionar siniestros.

La solución se divide en cinco componentes:

1. clasificación de la consulta;
2. recuperación de información relevante;
3. validación de cobertura;
4. generación de recomendaciones;
5. construcción de la respuesta final.

Cada componente define su contrato: el de clasificación devuelve el tipo de siniestro; el de validación recibe ese tipo junto con los datos de la póliza y devuelve si la cobertura aplica y bajo qué condiciones.

Cuando cambia la normativa de cobertura, únicamente se modifica el prompt responsable de esa etapa. El resto de la arquitectura permanece inalterado porque los contratos siguen siendo válidos.

---

## Buenas prácticas

Las consideraciones propias de la composición complementan los principios generales establecidos en la sección anterior:

- Definir contratos de entrada y salida para cada componente antes de implementarlo.
- Diseñar componentes reutilizables que no asuman contexto externo implícito.
- Evitar dependencias innecesarias entre módulos.
- Documentar cada flujo de composición.
- Evaluar el impacto acumulado sobre latencia y tokens al diseñar cadenas largas.

---

## Errores frecuentes

- Encadenar prompts sin una estrategia de diseño que justifique cada eslabón.
- Transferir información redundante entre componentes, incrementando el consumo de tokens sin añadir valor.
- Acoplar varios procesos en un único prompt cuando podrían estar separados.
- Ignorar el impacto acumulado sobre la latencia y el costo operativo.

---

## Ideas clave

- La composición transforma prompts individuales en arquitecturas completas capaces de resolver problemas complejos.
- La modularidad facilita mantenimiento, pruebas y evolución independiente de cada componente.
- Un buen diseño reduce complejidad sin perder capacidad funcional, y lo hace mediante contratos explícitos que desacoplan los componentes entre sí.

---

## Transición hacia la siguiente sección

En la próxima sección estudiaremos arquitecturas jerárquicas de prompts, donde un componente coordinador distribuye responsabilidades entre prompts especializados siguiendo principios de orquestación propios del AI Engineering.
