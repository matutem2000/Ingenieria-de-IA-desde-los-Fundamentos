# Índice definitivo

## Capítulo 1. Del Prompt Engineering al Context Engineering

- El problema que un prompt aislado no resuelve
- Evolución de las aplicaciones basadas en Large Language Models (LLM)
- Diferencias y complementariedad entre Prompt Engineering y Context Engineering
- El contexto como activo de arquitectura
- Calidad, costo, latencia y riesgo como variables de diseño
- Caso de estudio: del prototipo conversacional a una solución empresarial

## Capítulo 2. Anatomía del contexto

- Qué es contexto y qué no lo es
- Instrucciones del sistema y del usuario
- Historial de interacción
- Estado y memoria
- Conocimiento recuperado
- Herramientas y sus resultados
- Metadatos, permisos y procedencia
- Prioridad, orden y aislamiento de las fuentes

## Capítulo 3. Ventanas de contexto

- Tokens y límites de la Context Window
- Presupuesto de contexto
- Selección, priorización y descarte
- Ventana deslizante (*sliding window*)
- Resumen y compresión
- Caché de contexto (*context caching*)
- Pérdida de información y degradación de calidad
- Medición de costo, latencia y uso efectivo

## Capítulo 4. Diseño de memoria

- Diferencia entre historial, estado y memoria
- Memoria conversacional
- Memoria episódica
- Memoria semántica
- Memoria procedimental
- Persistencia, actualización y caducidad
- Recuperación, relevancia y resolución de conflictos
- Privacidad, aislamiento y derecho al olvido

## Capítulo 5. Ingeniería de instrucciones y políticas

- Roles y jerarquía de instrucciones
- Objetivos, restricciones y formato de salida
- Políticas y reglas de negocio
- Instrucciones reutilizables y composición
- Validación de entradas y salidas
- Controles técnicos (*guardrails*) y sus límites
- Conflictos de instrucciones e inyección de prompts

## Capítulo 6. Contexto dinámico

- Estado de la aplicación y de la tarea
- Perfil, preferencias y permisos del usuario
- Tiempo, ubicación y vigencia de los datos
- Variables, eventos y señales externas
- Ensamblado de contexto en tiempo de ejecución
- Separación entre datos, instrucciones y contenido no confiable
- Trazabilidad y depuración

## Capítulo 7. Herramientas y conocimiento externo

- Cuándo recuperar información y cuándo ejecutar una acción
- Llamadas a funciones (*function calling*)
- Interfaces de programación de aplicaciones (API)
- Bases de datos y archivos
- Retrieval-Augmented Generation (RAG)
- Model Context Protocol (MCP)
- Contratos, esquemas y validación
- Permisos, errores, reintentos e idempotencia

## Capítulo 8. Patrones de Context Engineering

- Recuperación (*retrieval*)
- Enrutamiento (*routing*)
- Planificación (*planning*)
- Reflexión y crítica
- Delegación
- Espacio de trabajo temporal (*scratchpad*)
- Composición de patrones
- Criterios de selección y anti-patrones

## Capítulo 9. Arquitecturas empresariales

- Chatbots, copilotos, agentes y sistemas híbridos
- Orquestación y ciclo de ejecución
- Separación de responsabilidades
- Observabilidad y evaluación continua
- Seguridad, privacidad y gobierno
- Escalabilidad, resiliencia y control de costos
- Decisiones de construcción, compra e integración
- Evolución desde el prototipo hasta producción

## Capítulo 10. Proyecto integrador

- Relevamiento de requisitos y restricciones
- Diseño de la arquitectura de contexto
- Estrategias de instrucciones, memoria y recuperación
- Integración segura de herramientas
- Evaluación de calidad, costo, latencia y riesgo
- Documentación de decisiones de arquitectura
- Plan de validación, operación y mejora
