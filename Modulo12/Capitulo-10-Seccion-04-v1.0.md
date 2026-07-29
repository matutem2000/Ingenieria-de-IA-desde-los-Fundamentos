# Módulo 12 – Capítulo 10 – Sección 04

# Extensiones posibles: cómo seguir evolucionando el sistema más allá del alcance del proyecto

El sistema integrador del proyecto final es una base sobre la que pueden construirse capacidades adicionales siguiendo el mismo rigor de diseño, evaluación y documentación. La extensión de mayor impacto inmediato es el fine-tuning del modelo de embedding sobre el corpus técnico del dominio: entrenar text-embedding-3-small con pares de consultas y documentos relevantes del golden dataset mediante contrastive learning puede mejorar el recall@5 entre 0.05 y 0.12 puntos para terminología específica del dominio no cubierta por el modelo base. La segunda extensión es el soporte multimodal: incorporar documentos con diagramas de arquitectura, capturas de dashboards y tablas de métricas requiere un pipeline de OCR y descripción de imágenes (GPT-4o Vision o Anthropic Claude 3.5) que convierta el contenido visual en texto indexable. La tercera extensión es un sistema de feedback activo: capturar el rating explícito del usuario por respuesta, acumular los pares (query, respuesta, rating) en un dataset de preferencias y usarlos para RLHF o DPO sobre el modelo de generación.

## Extensiones priorizadas por impacto

- Fine-tuning de embedding: contrastive learning sobre pares del golden dataset para mejorar recall@5 en terminología del dominio
- Soporte multimodal: pipeline OCR + descripción de imágenes para indexar diagramas, tablas y capturas de dashboards
- Feedback activo: captura de ratings por respuesta, acumulación de dataset de preferencias y fine-tuning con DPO
- Multi-tenancy: aislamiento por tenant en Qdrant (colecciones separadas o particionamiento por payload) con RBAC por organización
- Agent memory: memoria persistente de largo plazo con base de datos de hechos aprendidos de conversaciones anteriores

## Para recordar

Las extensiones posibles del sistema deben priorizarse con el mismo rigor que el proyecto inicial: evaluación cuantitativa del impacto esperado, estimación del costo de implementación y documentación de la decisión en un nuevo ADR antes de comenzar.
