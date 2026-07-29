# Módulo 8 – Capítulo 04 – Sección 06

## Cierre: el hardware correcto depende del modelo elegido, no al revés

Un error frecuente en la planificación de proyectos de LLMs locales es invertir el orden del proceso: comprar o alquilar hardware primero y luego buscar qué modelo cabe en ese presupuesto. El proceso correcto es el inverso: definir el modelo que cumple los requisitos de calidad en la tarea específica, calcular sus necesidades de VRAM con las fórmulas establecidas en este capítulo, y entonces seleccionar el hardware que satisface esas restricciones al menor costo total de propiedad. Un equipo que compra una GPU de 16 GB sin considerar el KV cache para contextos largos descubrirá que su modelo de 13B no cabe en producción cuando los usuarios empiezan a enviar documentos largos; un equipo que sobredimensiona hacia H100 para un workload de inferencia de 7B con baja concurrencia paga 10x más de lo necesario.

El análisis de hardware que este capítulo ha construido —del tipo de arquitectura (GPU, CPU, Apple Silicon) a la VRAM necesaria (pesos + KV cache + overhead), al catálogo de GPUs disponibles, a la ventaja de la memoria unificada de Apple Silicon y al análisis de costo-rendimiento cloud vs local— proporciona todas las piezas para tomar esa decisión de forma sistemática. La madurez del ecosistema de hardware para LLMs en 2025 ofrece opciones viables en cada punto de precio: modelos de 1B-3B ejecutables en CPUs modernas sin GPU, modelos de 7B-13B en GPUs de consumo de 8-16 GB de VRAM, modelos de 13B-34B en Apple Silicon con memoria unificada de 32-64 GB, y modelos de 70B-405B en multi-GPU de datacenter.

La cuantización es la palanca que ajusta el tamaño del modelo al hardware disponible. Si el modelo elegido por sus cualidades de calidad no cabe en el hardware disponible, la cuantización permite reducirlo: de BF16 a Q8 se elimina el 50% del tamaño; de Q8 a Q4_K_M se elimina otro 50%, con una degradación de calidad que para la mayoría de las tareas de producción es inferior al umbral perceptible. Esta combinación de selección de modelo por calidad y ajuste de cuantización por hardware produce sistemas más eficientes que los que resultan de seleccionar el hardware primero y aceptar el modelo que quepa.

Conocer los requisitos de hardware antes de comenzar el diseño de la arquitectura de despliegue no solo evita sorpresas tardías sino que permite mantener una conversación fundamentada con los stakeholders sobre los costos de infraestructura. Presentar a la dirección técnica el análisis de break-even con los números reales de VRAM necesaria, las opciones de hardware viables y el costo mensual proyectado para cada opción es exponencialmente más útil que solicitar "un presupuesto para GPU" sin contexto.

## Buena práctica

Mantener una hoja de cálculo de requisitos de hardware actualizada con los modelos candidatos, sus variantes de cuantización, los requisitos de VRAM calculados con las fórmulas de este capítulo y las GPUs que los soportan. Esta tabla de referencia acelera la toma de decisiones en los proyectos y evita el análisis desde cero en cada nuevo proyecto.

---

*"Premature optimization is the root of all evil — but failing to estimate resource requirements before committing to an architecture is the root of most engineering disasters."* — Donald Knuth, adaptado al contexto de infraestructura ML, recordando que el análisis de capacidad debe preceder siempre a la selección de hardware.
