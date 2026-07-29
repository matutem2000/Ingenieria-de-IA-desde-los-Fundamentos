# Módulo 11 – Capítulo 03 – Sección 01

# El desafío del legado: datos en silos, APIs inconsistentes y formatos heterogéneos

Los sistemas legacy enterprise — entendidos como aquellos con más de 10 años de antigüedad, frecuentemente sin documentación actualizada, y desarrollados en tecnologías que ya no cuentan con soporte activo de sus fabricantes — son la realidad operacional de la mayoría de las grandes empresas, y representan el principal obstáculo técnico para la integración de sistemas de IA que requieren acceso a datos de negocio consolidados y actualizados. El problema no es solo técnico sino también de información: los sistemas legacy a menudo no tienen APIs — exponen datos mediante extractos de archivos planos (CSV, TXT, fixed-width) generados por batch jobs nocturnos, o mediante bases de datos que solo son accesibles directamente mediante JDBC/ODBC desde la intranet corporativa, con esquemas no documentados que solo el equipo de mainframe comprende. Los silos de datos emergen históricamente porque cada sistema fue construido para optimizar su función específica sin considerar la interoperabilidad: el sistema de ERP (SAP, Oracle E-Business Suite) mantiene los datos maestros de clientes con un formato, el CRM (Salesforce) mantiene datos de contacto con duplicados no reconciliados, y el sistema de facturación legacy en COBOL mantiene el historial de transacciones con claves foráneas que solo tienen sentido dentro de ese sistema. La heterogeneidad de formatos (XML, JSON, CSV, EDI X12, SWIFT MT, HL7 FHIR, PDF no estructurado, emails) requiere capas de normalización que consumen tiempo de ingeniería significativo antes de que los datos puedan alimentar un sistema de IA.

## Puntos críticos de los sistemas legacy

- Ausencia de APIs REST: la única interfaz disponible es un endpoint SOAP con WSDL de 2003, un procedimiento almacenado en Oracle que retorna un cursor, o un job batch que genera un archivo CSV cada 24 horas
- Esquemas no documentados: tablas con nombres como T_MSTDAT_001 y columnas como COD_FLAG_X que requieren ingeniería inversa consultando al equipo de mantenimiento del sistema
- Calidad de datos degradada: duplicados, valores nulos en campos obligatorios, fechas en formatos inconsistentes (YYYYMMDD vs DD/MM/YYYY vs timestamps Unix), y encoding de caracteres mezclado (Latin-1 con UTF-8)
- Dependencias ocultas: cambiar un campo en el sistema legacy puede romper silenciosamente 15 sistemas downstream que nadie recuerda que dependen de ese campo exacto en esa posición del fixed-width file
- Restricciones de disponibilidad: ventanas de mantenimiento nocturnas donde el sistema no está disponible, y prohibiciones de carga adicional durante horario pico por riesgo de afectar el negocio principal

## Para recordar

El primer paso para integrar IA con sistemas legacy es producir un mapa de dependencias de datos actualizado — sin ese mapa, cualquier integración introduce riesgos que no pueden cuantificarse.
