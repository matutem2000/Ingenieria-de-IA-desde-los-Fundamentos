# Módulo 11 – Capítulo 10 – Sección 02

# Quick wins técnicos: proyectos de alto impacto y bajo riesgo para construir credibilidad interna

Los quick wins de IA enterprise son proyectos que pueden entregarse en 4-8 semanas, generan valor medible y visible para un stakeholder específico, no requieren cambios en sistemas críticos de negocio, y producen evidencia técnica (métricas de calidad, datos de uso, feedback de usuarios) que fundamenta la inversión en proyectos más ambiciosos. La selección correcta del primer proyecto de IA enterprise es crítica: elegir un proyecto demasiado ambicioso (integración con el ERP, automatización de procesos de aprobación multisistema) produce un fracaso visible en las primeras semanas que daña la credibilidad del equipo de IA por meses; elegir un proyecto demasiado trivial (un chatbot que solo responde FAQs con reglas hardcodeadas) produce un éxito que nadie toma en serio. Los mejores candidatos para quick wins combinan alta disponibilidad de datos (el caso de uso tiene datos limpios y accesibles sin integraciones complejas), alta visibilidad para stakeholders (el caso de uso resuelve un problema que el equipo directivo reconoce como importante), y baja complejidad de integración (puede desplegarse como una aplicación standalone sin modificar sistemas productivos). Los ejemplos más frecuentes de quick wins exitosos incluyen: asistente de búsqueda semántica sobre la documentación técnica interna (corpus estático, fácil de indexar, usuarios técnicos que valoran la mejora), generación asistida de respuestas para el helpdesk interno de IT (reduce la carga de los agentes de soporte, métricas de impacto claras), y extracción automática de información clave de contratos en PDF (proceso actualmente manual, impacto económico medible en horas ahorradas).

## Criterios de selección de quick wins

- Disponibilidad de datos: el corpus de documentos o datos necesarios está disponible, accesible sin integraciones complejas, y tiene calidad suficiente para alimentar el sistema de IA sin limpieza masiva previa
- Ciclo de feedback corto: los usuarios del sistema de IA pueden dar feedback sobre la calidad de las respuestas en el mismo día del uso, permitiendo iteraciones de mejora cada 1-2 semanas
- Stakeholder comprometido: existe un líder de negocio identificado que necesita el caso de uso, tiene autoridad para que su equipo lo use, y está dispuesto a medir el impacto antes y después
- Rollback simple: si el sistema de IA falla o produce resultados de calidad insuficiente, es fácil deshabilitar la funcionalidad y volver al proceso manual sin impacto operacional
- Reutilización de componentes: el quick win debe construirse usando los componentes de la plataforma que se quiere escalar (el mismo vector store, el mismo prompt registry, el mismo pipeline de evaluación) para que la deuda técnica del quick win sea parte de la plataforma final

## Para recordar

Un quick win que no genera datos de calidad (métricas de uso, feedback de usuarios, comparación pre/post) es una oportunidad desperdiciada — el resultado más valioso del quick win no es la aplicación en sí sino la evidencia que permite justificar la inversión en la plataforma.
