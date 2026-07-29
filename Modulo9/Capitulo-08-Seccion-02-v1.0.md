# Módulo 9 – Capítulo 08 – Sección 02

# Inmutabilidad de logs: protección contra alteración de registros de auditoría

Los logs de seguridad solo tienen valor como evidencia regulatoria y forense si son inmutables: un log que puede ser modificado o borrado por el mismo sistema —o por un atacante que lo comprometió— no puede usarse para determinar qué ocurrió durante un incidente ni para demostrar compliance ante reguladores. La inmutabilidad de logs es un requisito explícito de frameworks regulatorios como PCI DSS (Requirement 10.5: "Secure audit trails so they cannot be altered"), HIPAA (Audit Controls Standard), y es implícita en el requisito de trazabilidad del GDPR y el EU AI Act. Las técnicas para garantizar inmutabilidad van desde soluciones simples (write-once storage en S3 Object Lock) hasta más sofisticadas (firma criptográfica de cada entrada de log con appending-only verification). En el contexto específico de sistemas de IA, la inmutabilidad de los logs de inferencia es crítica porque un atacante que compromete el sistema de IA puede intentar borrar evidencia de sus acciones modificando los logs antes de ser detectado.

## Aspectos técnicos

- Amazon S3 Object Lock en COMPLIANCE mode: previene cualquier modificación o borrado de objetos durante el retention period definido, incluyendo por usuarios root de la cuenta de AWS — el modo COMPLIANCE es más restrictivo que GOVERNANCE (que permite a administradores con permisos especiales desbloquear); adecuado para logs de auditoría de sistemas de IA bajo GDPR o HIPAA
- Azure Immutable Blob Storage: política time-based retention que, una vez aplicada con lock habilitado, no puede ser modificada ni reducida; compatible con Azure WORM (Write Once, Read Many) compliance certification
- Firma criptográfica de logs: cada entrada de log se firma con HMAC-SHA256 usando una clave de signing que vive en un KMS separado del sistema de log; cualquier modificación del log (inserción, borrado, modificación de una entrada) invalida las firmas, haciendo la alteración detectable; la cadena de firmas (cada firma incluye el hash de la entrada anterior) proporciona tamper evidence a nivel de secuencia
- Forwarding a SIEM centralizado: transmitir los logs a un SIEM (Splunk, Elastic SIEM, Microsoft Sentinel) independiente del sistema de IA como copia inmutable secundaria; el SIEM debe estar en una cuenta o suscripción de cloud diferente al sistema principal para garantizar independencia ante compromisos
- Verificación de integridad de logs: ejecutar periódicamente (diariamente) una verificación de la cadena de firmas o del checksum de los archivos de log contra un valor de referencia almacenado en un sistema independiente; alertar si se detecta discrepancia — la verificación pasiva (solo si se consulta) es insuficiente

## Para recordar

La inmutabilidad de logs debe ser una propiedad verificable del sistema, no una propiedad declarada: la configuración de S3 Object Lock en COMPLIANCE mode, la cadena de firmas criptográficas y la forwarding a un SIEM independiente deben estar documentadas y probadas periódicamente como parte del programa de auditoría del sistema.
