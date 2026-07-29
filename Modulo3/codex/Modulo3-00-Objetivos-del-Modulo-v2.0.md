# Módulo 3 — Context Engineering profesional

## Propósito del módulo

> Diseñar el contexto que permite que un sistema basado en modelos de lenguaje produzca respuestas pertinentes, conserve el estado necesario y utilice conocimiento y herramientas de manera controlada.

## Introducción

Los dos primeros módulos presentaron los fundamentos de los modelos de lenguaje y el diseño de prompts. Ese conocimiento sigue siendo necesario, pero no alcanza para construir soluciones confiables: un buen prompt no puede compensar información ausente, memoria irrelevante, herramientas mal definidas ni datos recuperados sin criterios de calidad.

El **Context Engineering** aborda ese problema como una disciplina de arquitectura. Su objeto no es una instrucción aislada, sino el conjunto de información que la aplicación selecciona, organiza y entrega al modelo durante una ejecución: instrucciones, historial, estado, memoria, conocimiento recuperado, resultados de herramientas y metadatos.

En este módulo, el lector adoptará la perspectiva de un arquitecto de contexto. Aprenderá a decidir qué información debe recibir un Large Language Model (LLM), de dónde proviene, cuándo incorporarla, con qué prioridad y bajo qué controles. También analizará los compromisos entre calidad, costo, latencia, seguridad y mantenibilidad.

## Objetivos de aprendizaje

Al finalizar el módulo, el lector podrá:

- Explicar la diferencia y la relación entre Prompt Engineering y Context Engineering.
- Identificar las fuentes y las capas que componen el contexto de una aplicación basada en LLM.
- Diseñar estrategias para seleccionar, ordenar, comprimir y descartar información dentro de una Context Window.
- Diferenciar memoria conversacional, episódica, semántica y procedimental, y elegir mecanismos de persistencia apropiados.
- Incorporar estado, perfiles, eventos y otras fuentes de contexto dinámico sin mezclar datos de usuarios o sesiones.
- Integrar herramientas, interfaces de programación de aplicaciones (API), archivos, bases de datos y conocimiento recuperado.
- Definir instrucciones, políticas, restricciones y controles con prioridades explícitas.
- Aplicar patrones de recuperación, planificación, enrutamiento, reflexión y delegación cuando el problema los justifique.
- Evaluar una arquitectura de contexto mediante métricas de calidad, costo, latencia, seguridad y trazabilidad.
- Preparar soluciones que utilicen Retrieval-Augmented Generation (RAG), Model Context Protocol (MCP) y agentes.

## Alcance

El módulo se concentra en el diseño de la capa de contexto y en su integración con la aplicación. No presupone que el modelo razone, recuerde o comprenda como una persona: esas expresiones se usarán, cuando corresponda, como abreviaturas de comportamientos observables del sistema.

El tratamiento prioriza principios y decisiones de arquitectura por encima de proveedores, modelos o productos específicos.

## Perfil de egreso

Al completar el módulo, el lector podrá diseñar y documentar la capa de contexto de una solución empresarial de IA. Será capaz de justificar qué información se incorpora, cómo se gobierna su ciclo de vida, qué riesgos introduce y cómo se valida su aporte al comportamiento del sistema.

## Evidencias de aprendizaje

El dominio de los objetivos se demostrará mediante:

- laboratorios con resultados reproducibles y criterios de aceptación;
- decisiones de arquitectura documentadas;
- diagramas de flujo de contexto y de integración;
- evaluaciones comparativas de calidad, costo y latencia;
- un proyecto integrador con trazabilidad entre requisitos, decisiones, implementación propuesta y métricas.

## Criterios editoriales del módulo

Cada capítulo incluirá, como mínimo:

- objetivos de aprendizaje;
- motivación y definición del problema;
- desarrollo conceptual desde primeros principios;
- analogías que complementen, sin reemplazar, la explicación técnica;
- diagramas y ejemplos aplicados;
- un caso real y una conversación con un arquitecto;
- errores frecuentes y buenas prácticas;
- un laboratorio reproducible;
- preguntas de reflexión, resumen y checklist;
- bibliografía y referencias cruzadas;
- conexión explícita con el capítulo siguiente.

> Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones.
