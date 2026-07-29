# Módulo 12 – Capítulo 02 – Sección 01

# ADR (Architecture Decision Record): estructura y propósito de documentar decisiones técnicas

Un Architecture Decision Record (ADR) es un documento breve y estructurado que captura una decisión arquitectónica significativa junto con su contexto, las opciones evaluadas, la opción elegida y las consecuencias esperadas. El formato popularizado por Michael Nygard en 2011 y adoptado por Thoughtworks incluye cinco secciones: Título, Estado (Proposed / Accepted / Superseded), Contexto, Decisión y Consecuencias. Los ADRs se versionan junto al código fuente del proyecto — típicamente en un directorio `docs/adr/` — para que cada commit de código pueda asociarse con las decisiones arquitectónicas vigentes en ese momento. En sistemas de IA, los ADRs son especialmente valiosos porque las decisiones sobre modelo, chunking, retrieval y seguridad tienen impacto en la calidad, el costo y el riesgo del sistema, y deben poder auditarse en caso de degradación de comportamiento.

## Estructura de un ADR efectivo

- Título: identificador numérico secuencial (ADR-001) más una frase que nombre la decisión sin ambigüedad
- Estado: Proposed / Accepted / Deprecated / Superseded (con referencia al ADR que lo reemplaza)
- Contexto: problema técnico que motiva la decisión, restricciones activas y fuerzas en tensión
- Decisión: la opción elegida expresada con precisión, sin lenguaje evasivo ni condicionales innecesarios
- Consecuencias: efectos positivos esperados, trade-offs aceptados y riesgos residuales identificados

## Para recordar

Un ADR documenta el razonamiento detrás de una decisión, no solo la decisión — sin el contexto de por qué se eligió una opción, el equipo no puede evaluar cuándo es válido cambiarla.
