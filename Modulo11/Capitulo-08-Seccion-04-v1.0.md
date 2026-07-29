# Módulo 11 – Capítulo 08 – Sección 04

# AI Act enterprise: obligaciones de documentación, transparencia y evaluación de riesgos

El AI Act de la Unión Europea (en vigor desde agosto de 2024) es el primer marco regulatorio integral específico para sistemas de IA, y clasifica los sistemas en cuatro niveles de riesgo (inaceptable, alto, limitado, mínimo) con obligaciones técnicas y de documentación proporcionales al nivel de riesgo asignado, lo que obliga a las empresas enterprise que operan en la UE a realizar una clasificación formal de cada sistema de IA que desarrollan o despliegan. Los sistemas de IA de alto riesgo (que incluyen sistemas usados en contratación de personal, evaluación de crédito, sistemas educativos de evaluación, sistemas de diagnóstico médico, y sistemas usados por autoridades públicas) deben cumplir con requisitos técnicos específicos antes de poder ser desplegados en la UE: documentación técnica detallada que incluye la descripción del sistema, el proceso de entrenamiento y evaluación, los datos usados, las métricas de rendimiento desagregadas por grupos demográficos, y las medidas de supervisión humana implementadas. La evaluación de conformidad (para la mayoría de los sistemas de alto riesgo, puede realizarse mediante auto-evaluación con documentación; para algunos subsectores como infraestructura crítica, requiere una tercera parte notificada) genera un Technical Documentation File que debe mantenerse actualizado durante toda la vida operacional del sistema y proporcionarse a las autoridades de supervisión cuando lo requieran. Los proveedores de modelos de propósito general (GPAI) con más de 10^25 FLOPs de cómputo de entrenamiento tienen obligaciones adicionales de transparencia y evaluación de riesgo sistémico.

## Obligaciones técnicas del AI Act para sistemas enterprise

- Clasificación de riesgo: proceso documentado de análisis del artículo 6 y Annex III del AI Act para determinar si cada sistema desarrollado cae en la categoría de alto riesgo, con decisión firmada por el DPO y el área legal
- Technical Documentation File: documento técnico conforme al Annex IV que incluye descripción general, proceso de entrenamiento, datos utilizados, métricas de performance desagregadas, gestión de riesgos, y plan de supervisión humana
- Logging de operaciones de alto riesgo: sistemas de alto riesgo deben generar logs automáticos de su operación que sean trazables, con retención suficiente para permitir revisión posterior por autoridades supervisoras
- Supervisión humana: los sistemas de alto riesgo deben incluir mecanismos técnicos que permitan a los operadores humanos comprender el output del sistema, ignorarlo o anularlo, e interrumpir su operación — documentados y verificables
- Post-market monitoring: sistema de monitoreo continuo del comportamiento del modelo en producción, con proceso para escalar a la autoridad competente si se detectan riesgos no anticipados durante la evaluación de conformidad inicial

## Para recordar

El AI Act aplica no solo a los desarrolladores del sistema de IA sino también a los desplegadores (empresas que usan un sistema de IA desarrollado por un tercero en un contexto de alto riesgo): la clasificación de riesgo debe hacerse evaluando el caso de uso específico, no solo el sistema base.
