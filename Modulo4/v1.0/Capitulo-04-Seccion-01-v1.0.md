# Módulo 4 – Capítulo 04 – Sección 01

## Arquitecturas Basadas en Agentes

Un sistema RAG, por sofisticado que sea, es fundamentalmente reactivo: recibe una consulta, recupera contexto y genera una respuesta. No puede iniciar acciones, encadenar múltiples pasos de razonamiento con herramientas externas, o adaptar su estrategia cuando el primer intento no produce el resultado esperado. Para los casos de uso que requieren esas capacidades — automatizar un proceso de múltiples pasos, investigar un problema iterando sobre herramientas, ejecutar una transacción en un sistema externo basándose en la interpretación de lenguaje natural — el patrón RAG no es suficiente. Se necesita una arquitectura de agentes.

El concepto de agente, en el contexto de sistemas de IA basados en LLMs, tiene una definición arquitectónica precisa: un agente es un sistema que utiliza un modelo de lenguaje como motor de razonamiento para decidir qué acciones tomar, ejecuta esas acciones mediante herramientas, observa los resultados de esas acciones, y utiliza esas observaciones para decidir el siguiente paso, hasta alcanzar un objetivo o agotarse por un límite configurado. Esta definición distingue a un agente de un chatbot sofisticado o de un pipeline RAG: el agente tiene autonomía para decidir el camino hacia el objetivo, no solo para generar texto.

El lector familiarizado con los patrones Planning y Delegation del Módulo 3 reconocerá los fundamentos conceptuales de las arquitecturas de agentes. El patrón Planning describe cómo instruir a un LLM para que descomponga un objetivo complejo en pasos ejecutables. El patrón Delegation describe cómo un agente orquestador puede asignar subtareas a sub-agentes especializados. Las arquitecturas de agentes del Módulo 4 toman esos patrones y los convierten en sistemas productivos: con estado persistente, herramientas reales, mecanismos de fallo controlado, observabilidad y límites de autonomía.

Los temas que este capítulo desarrolla son:

- **Componentes de un agente:** el modelo de razonamiento, los tipos de memoria, el registro de herramientas, y el bucle de observación-acción que define el comportamiento del agente.
- **Memoria y estado:** cómo un agente mantiene contexto entre interacciones, cuándo usar memoria episódica versus memoria semántica, y cómo gestionar el estado en agentes de larga duración.
- **Patrones de diseño:** los patrones ReAct, Planner-Executor, Supervisor-Workers y Reflection, con criterios para elegir entre ellos y sus fallos característicos.
- **Casos de uso empresariales:** los escenarios donde los agentes producen valor real y los escenarios donde añaden complejidad sin beneficio.

> **Nota del Arquitecto:** La principal trampa de las arquitecturas de agentes es pensar que "más autonomía es mejor". En la práctica, cada grado de autonomía que se concede a un agente aumenta el espacio de comportamientos posibles, incluidos los no deseados. Un agente que puede ejecutar código, leer y escribir archivos, y hacer llamadas a APIs externas tiene una superficie de impacto enorme si su razonamiento se desvía del objetivo. Los mejores sistemas agénticos que he visto en producción son los que definen con precisión qué puede hacer el agente, qué no puede hacer, y en qué condiciones debe pausar y solicitar confirmación humana antes de continuar.

El valor real de las arquitecturas de agentes no reside en el modelo de lenguaje que las impulsa, sino en la cuidadosa ingeniería de sus componentes, la robustez de sus herramientas y la precisión de sus límites de autonomía. Las secciones siguientes desarrollan cada uno de estos elementos.
