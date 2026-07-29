# Módulo 12 – Capítulo 10 – Sección 06

# Cierre: la ingeniería de IA no termina con el despliegue — comienza con él

El proyecto final del libro demuestra que construir un sistema de IA que llega al primer despliegue en producción es solo el inicio del trabajo de ingeniería real. En producción, el sistema enfrenta distribuciones de queries que el golden dataset no cubre completamente, documentos desactualizados que degradan la calidad del retrieval, actualizaciones del LLM del proveedor que cambian el comportamiento, ataques que el red teaming no anticipó, y patrones de carga que los benchmarks de desarrollo no modelaron con precisión. La ingeniería de IA en producción es el ciclo continuo de medir, detectar degradaciones, diagnosticar con trazas, actualizar la base de conocimiento, re-evaluar con el golden dataset, mejorar los controles de seguridad y desplegar con el pipeline CI/CD. El AI Engineer que completa este libro no ha terminado de aprender — ha adquirido las herramientas y los criterios para seguir aprendiendo de sistemas reales en producción, que es donde ocurre la ingeniería de IA que importa.

## Aspectos técnicos que integra este capítulo

- Rúbrica cuantitativa: criterios verificables por dimensión (faithfulness >= 0.82, task completion >= 75%, bypass < 5%)
- Checklist de producción: 30 verificaciones en 6 categorías antes de considerar el sistema listo para producción
- Lecciones aprendidas: insights técnicos sobre chunking, reranking, ADRs, testing agéntico e instrumentación temprana
- Extensiones posibles: fine-tuning de embedding, soporte multimodal, feedback activo y multi-tenancy como siguientes pasos
- Síntesis del recorrido: la progresión desde usar LLMs hasta operar sistemas de IA evaluables en producción

## Para recordar

El primer despliegue a producción de un sistema de IA no es el punto final del proyecto — es el punto en el que el sistema comienza a generar las observaciones reales que permiten mejorarlo con evidencia en lugar de con suposiciones.

*"The best way to learn how to build AI systems is to build AI systems, run them in production, and pay attention to what breaks." — Andrej Karpathy*
