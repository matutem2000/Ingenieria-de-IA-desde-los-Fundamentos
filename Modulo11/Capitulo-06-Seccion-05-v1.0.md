# Módulo 11 – Capítulo 06 – Sección 05

# Casos de uso enterprise: soporte interno, asistentes de ventas, análisis de contratos y generación de código

Los cuatro casos de uso de RAG enterprise más frecuentes y de mayor impacto tienen requisitos técnicos específicos que diferencian cada implementación y que deben comprenderse antes de diseñar la arquitectura del sistema. El asistente de soporte interno (HR, IT helpdesk, Legal FAQ) es el caso de uso con menor riesgo y mayor velocidad de despliegue: el corpus es relativamente estable (políticas, procedimientos, FAQs), los usuarios son empleados autenticados con permisos conocidos, y las métricas de éxito son medibles (reducción del 30-50% en tickets de soporte de primer nivel). El asistente de ventas (product information, pricing, competitive intelligence) introduce mayor complejidad de actualización porque los precios y la disponibilidad de productos cambian con alta frecuencia y la información desactualizada tiene un impacto directo y medible en el negocio. El análisis de contratos (extracción de cláusulas clave, comparación con templates, identificación de riesgos y obligaciones) es el caso de uso con mayor impacto por documento procesado y mayor exigencia de precisión: los errores de extracción pueden tener consecuencias legales, por lo que el sistema debe incluir siempre la cita exacta del texto del contrato junto a cada extracción, y debe presentarse como asistente de revisión (no como tomador de decisiones autónomo). La generación de código con contexto del codebase corporativo (RAG sobre código fuente, documentación técnica, y patrones de arquitectura internos) requiere embeddings especializados para código (CodeBERT, text-embedding-3-large con chunking por función) y un índice separado del corpus de texto para evitar interferencia entre dominios.

## Características técnicas por caso de uso

- Soporte interno: corpus de 1.000-10.000 documentos de política y procedimientos, chunking semántico con overlap, filtros de departamento para separar HR de IT de Legal, latencia de respuesta < 3 segundos, y métricas de deflection rate de tickets
- Asistente de ventas: integración con PIM (Product Information Management) y ERP para datos de precios en tiempo real via Text-to-SQL, corpus de documentación de producto, y sistema de alertas cuando la información del índice tiene más de 24 horas de antigüedad
- Análisis de contratos: pipeline de procesamiento de PDF con extracción estructurada (PyPDF2, pdfplumber, Unstructured.io), clasificadores de tipo de cláusula, extraction templates con Pydantic models para validar los campos extraídos, y UI de revisión con citas exactas del texto original
- RAG sobre codebase: indexación de repositorios Git con tree-sitter para parsing de código, chunking por función o clase, embeddings con Voyage Code-3 o text-embedding-3-large, y filtros por repositorio y rama para usuarios con permisos de acceso al código

## Para recordar

Cada caso de uso de RAG enterprise tiene una métrica de negocio específica que debe definirse antes de la implementación — sin ella, es imposible demostrar el valor del sistema una vez en producción.
