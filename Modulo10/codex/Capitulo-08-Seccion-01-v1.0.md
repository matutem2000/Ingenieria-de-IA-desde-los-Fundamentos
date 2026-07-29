# Módulo 10 – Capítulo 08 – Sección 01

# Data governance para IA: catalogación, clasificación y linaje de datos

El data governance para IA extiende el government de datos tradicional con tres necesidades específicas: los datos que alimentan modelos de ML tienen requisitos de linaje más estrictos (necesidad de reproducibilidad exacta de experimentos), los datos de entrenamiento con PII o datos sensibles requieren controles especiales antes de ser usados para entrenar modelos (anonimización, consentimiento verificado, prohibición de ciertas categorías), y el uso de datos en AI genera riesgos regulatorios que la GDPR, la AI Act europea y regulaciones sectoriales (FINRA, HIPAA) abordan explícitamente. La catalogación de datos para IA se implementa con herramientas como Apache Atlas, DataHub (open source de LinkedIn), o Collibra: estas plataformas mantienen un catálogo activo de todos los datasets con sus metadatos (schema, propietario, clasificación de sensibilidad, SLA de frescura), y para cada dataset de entrenamiento de un modelo, registran automáticamente qué modelos fueron entrenados con ese dataset, creando el grafo de linaje datos-modelos. La clasificación de datos es especialmente crítica en el contexto de IA: un dataset que contiene datos de comportamiento de usuarios clasificados como "anonymized" puede permitir re-identificación cuando se usa para entrenar ciertos tipos de modelos, y el data governance debe incluir políticas específicas sobre qué categorías de datos pueden usarse para entrenar qué tipos de modelos.

## Componentes del data governance para IA

- Data catalog: inventario centralizado de todos los datasets con schema, owner, classification label (public/internal/confidential/restricted), y SLA de frescura; actualizado automáticamente por crawlers del data lake
- Classification framework: taxonomía de sensibilidad de datos (PII, PHI, financial, trade secret, public) con reglas de clasificación automática y proceso de aprobación para uso de datos sensibles en modelos
- Lineage graph: grafo que conecta fuentes de datos → pipelines de procesamiento → datasets de entrenamiento → modelos → endpoints de serving; permite responder "¿qué modelos en producción usan datos de este sistema?"
- Data access requests: proceso formal (no necesariamente manual) para que un equipo solicite acceso a un dataset clasificado para entrenamiento, con registro de la justificación y aprobación del data owner
- Retention policies: reglas de cuánto tiempo se conservan los datasets de entrenamiento (requisito para reproducibilidad: al menos mientras el modelo derivado esté en producción), con eliminación automática al expirar

## Para recordar

El data governance para IA no es burocracia: es el conjunto de controles técnicos que garantizan que los modelos en producción pueden auditarse, que el uso de datos cumple con los compromisos legales con los usuarios, y que los incidentes de datos se pueden investigar con trazabilidad completa.
