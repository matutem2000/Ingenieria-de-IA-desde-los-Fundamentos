# Módulo 8 – Capítulo 04 – Sección 06

# Cierre: el hardware correcto depende del modelo elegido, no al revés

Un error frecuente en la planificación de proyectos de LLMs locales es seleccionar el hardware primero y luego buscar qué modelo cabe en ese presupuesto; el proceso correcto es el inverso: definir el modelo que cumple los requisitos de calidad en la tarea específica, calcular sus necesidades de VRAM y throughput, y entonces seleccionar el hardware que satisface esas restricciones al menor costo total de propiedad. Un equipo que compra una GPU de 16 GB sin considerar el KV cache para contextos largos descubrirá que su modelo de 13B no cabe en producción; un equipo que sobredimensiona hacia H100 para un workload de inferencia de 7B con baja concurrencia paga 10x más de lo necesario. La madurez del ecosistema de hardware para LLMs en 2025 ofrece opciones viables en cada punto de precio: modelos de 1B-3B son ejecutables en CPUs modernas, modelos de 7B-13B son viables en GPUs de consumo de 8-16 GB, modelos de 13B-34B en Apple Silicon de 32-64 GB de memoria unificada, y modelos de 70B-405B en multi-GPU de datacenter. El ingenieros de IA moderno debe ser capaz de calcular los requisitos de hardware de un modelo antes de comprometerse con una arquitectura de despliegue, y ajustar la cuantización como palanca para hacer que el modelo elegido quepa en el hardware disponible.

## Buena práctica

Mantén una hoja de cálculo de requisitos de hardware actualizada con los modelos candidatos, sus variantes de cuantización, los requisitos de VRAM calculados y las GPUs que los soportan; esta tabla de referencia acelera la toma de decisiones de hardware en los proyectos.

---

*"Premature optimization is the root of all evil — but failing to estimate resource requirements before committing to an architecture is the root of most engineering disasters."* — Donald Knuth, adaptado al contexto de infraestructura ML, recordando que el análisis de capacidad debe preceder siempre a la selección de hardware.
