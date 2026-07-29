# Módulo 7 – Capítulo 10 – Sección 03

# Benchmarks de agentes: SWE-bench, GAIA, AgentBench

Los benchmarks de agentes son conjuntos de evaluación estandarizados que permiten comparar el desempeño de diferentes sistemas agénticos en tareas representativas de aplicaciones reales, facilitando la evaluación objetiva de modelos, frameworks y configuraciones de agentes. SWE-bench (Software Engineering Benchmark, Princeton/Chicago 2023) evalúa la capacidad de agentes para resolver issues reales de repositorios GitHub —leer el issue, navegar el repositorio, escribir código de corrección y pasar los tests existentes— con una tasa de resolución que los mejores sistemas alcanzan en el rango del 30-50% en SWE-bench Verified. GAIA (General AI Assistants benchmark, Meta/HuggingFace 2023) evalúa capacidades de asistente general con tareas que requieren búsqueda web, razonamiento multi-paso, procesamiento de archivos y aritmética, clasificadas en 3 niveles de dificultad; los mejores sistemas alcanzan ~70% en nivel 1 y ~30% en nivel 3. AgentBench (Tsinghua University 2023) evalúa agentes en 8 entornos distintos incluyendo OS, bases de datos, web, y juegos, con una métrica compuesta de desempeño cross-environment.

## Aspectos técnicos

- **SWE-bench**: 2294 issues de 12 repositorios Python populares (Django, Flask, Scikit-learn, Sympy); el agente recibe el issue text y el repositorio base; se evalúa si el patch generado pasa los tests del issue sin romper otros tests; métricas: % resolved, % partially_resolved
- **SWE-bench Lite y Verified**: versiones reducidas (300 issues) y verificadas manualmente (500 issues de alta calidad) para evaluación más rápida y confiable; la mayoría de papers publican resultados en Lite o Verified por el costo computacional de SWE-bench completo
- **GAIA (General AI Assistants)**: 466 preguntas en 3 niveles; nivel 1 (factual con 1 herramienta), nivel 2 (multi-step, 2-5 herramientas), nivel 3 (tareas complejas, >5 herramientas con razonamiento profundo); requiere capacidades de búsqueda web, procesamiento de archivos (PDF, Excel, imágenes) y razonamiento matemático
- **AgentBench**: 8 entornos incluyendo OS (comandos bash), DB (SQL y MongoDB), Knowledge Graph (SPARQL), Lateral Thinking (puzzles), Alfworld (navegación 3D), WebShop (e-commerce), Mind2Web (navegación web real) y HouseHold (simulación de hogar); promedia el desempeño sobre todos los entornos
- **Limitaciones de los benchmarks**: los benchmarks públicos pueden contaminar el entrenamiento de los modelos evaluados (data contamination); los benchmarks estáticos se vuelven obsoletos cuando los modelos los "memorizan"; evaluar agentes en benchmarks privados o dinámicamente generados es más indicativo del desempeño real en producción

## Principio rector

Los benchmarks públicos son útiles para comparación directa entre sistemas, pero el benchmark más relevante para un sistema de producción es uno construido con las tareas reales del dominio de aplicación; un agente que score 90% en SWE-bench puede ser inapropiado para tareas de customer support si el dominio requiere habilidades completamente diferentes.
