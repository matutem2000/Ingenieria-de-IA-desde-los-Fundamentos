# Módulo 12 – Capítulo 09 – Sección 04

# Documentación de seguridad: modelo de amenazas, controles y limitaciones conocidas

La documentación de seguridad del sistema integrador es un documento técnico estructurado que cubre: el modelo de amenazas STRIDE resumido con las amenazas de mayor riesgo, los controles implementados con referencia al código que los implementa, las limitaciones conocidas del sistema de seguridad y el proceso para reportar vulnerabilidades. La sección de controles implementados lista cada control con: nombre del control, amenaza que mitiga, componente del sistema donde está implementado (nombre del módulo y línea de código de referencia), y efectividad medida en el red teaming (porcentaje de ataques mitigados en esa categoría). La sección de limitaciones conocidas es la más importante para la confianza del lector — documenta explícitamente qué ataques el sistema no puede prevenir completamente: ataques de injection en idiomas poco representados en la lista negra, DoS de alto volumen sin WAF externo, y exfiltración de datos si el LLM del proveedor es comprometido. El proceso de reporte de vulnerabilidades incluye el canal (security@empresa.com con clave PGP), el SLA de respuesta (24h inicial, 72h para triage) y el proceso de coordinated disclosure.

## Secciones de la documentación de seguridad

- Threat model: tabla STRIDE con amenazas, probabilidad (High/Medium/Low), impacto y control mitigante para cada amenaza
- Controles implementados: lista con nombre, amenaza mitigada, módulo Python de implementación y efectividad medida en red teaming
- Limitaciones conocidas: ataques que el sistema mitiga parcialmente o no mitiga, con justificación técnica y riesgo residual aceptado
- Security testing: frecuencia del red teaming (trimestral), scope y herramientas usadas (OWASP LLM Top 10 como referencia)
- Vulnerability reporting: canal de reporte, SLA de respuesta y proceso de coordinated disclosure con timeline

## Para recordar

Documentar las limitaciones conocidas de seguridad no es un signo de debilidad del sistema — es el estándar de transparencia de los sistemas en producción responsables, y es lo que distingue una postura de seguridad madura de una que oculta sus debilidades.
