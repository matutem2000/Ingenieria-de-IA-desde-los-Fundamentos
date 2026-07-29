# Módulo 4 – Capítulo 01 – Sección 06

## Resumen

Este capítulo estableció las bases del pensamiento arquitectónico aplicado a soluciones de inteligencia artificial. No se trató de tecnología específica, sino del modo de razonamiento que el arquitecto de IA necesita para tomar decisiones que soporten el crecimiento del sistema a lo largo del tiempo.

Se exploró la diferencia fundamental entre construir un prototipo y diseñar un sistema listo para producción: la brecha no está en las herramientas utilizadas sino en la amplitud de las preguntas que se hacen antes de escribir la primera línea de infraestructura. Un prototipo pregunta si el sistema funciona; un sistema productivo pregunta cómo falla, cómo se detecta ese fallo, cómo se recupera de él y cuánto cuesta operarlo a escala.

El pensamiento sistémico amplió esa perspectiva al conjunto completo del ecosistema: usuarios, datos, modelos, infraestructura, costos, monitoreo y operación. Ninguna de estas dimensiones puede optimizarse de forma aislada sin generar consecuencias en las demás. El arquitecto que solo piensa en el modelo ignora los datos; el que solo piensa en los datos ignora los costos operativos; el que solo piensa en los costos ignora la calidad de las respuestas.

El análisis de trade-offs proporcionó el método concreto para navegar esas tensiones: identificar con precisión qué se gana y qué se pierde en cada decisión, comunicarlo a los stakeholders y documentarlo en registros de decisiones arquitectónicas. No existe la arquitectura perfecta; existe la arquitectura que resuelve los problemas actuales con los compromisos más aceptables para el negocio.

Las cinco decisiones que escalan — separación de responsabilidades, desacoplamiento, observabilidad, escalabilidad horizontal y automatización del despliegue — son las inversiones de diseño que producen dividendos durante años. Las cinco omisiones más costosas — tecnología por moda, ausencia de métricas, costos ignorados, acoplamiento excesivo y falta de planificación evolutiva — son los patrones de error que estos mismos principios previenen.

El Capítulo 02 traduce este marco conceptual al primer conjunto de decisiones concretas que el arquitecto enfrenta: la selección del patrón de arquitectura adecuado para el sistema. Monolito, microservicios, arquitecturas basadas en eventos, y la comparativa fundamental entre enriquecer el modelo (fine-tuning) versus enriquecer el contexto (RAG) son las decisiones que determinan la forma global del sistema antes de que cualquier componente específico sea implementado.

---

*"Good software architecture is about making the hard things easy and the wrong things hard."*
— Michael Feathers, autor de *Working Effectively with Legacy Code*
