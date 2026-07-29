# Módulo 11 – Capítulo 06 – Sección 04

# Knowledge management: actualización continua del índice con nuevos documentos corporativos

El índice vectorial de un sistema RAG enterprise no es un artefacto estático que se construye una vez y se usa indefinidamente: es un sistema vivo que debe reflejar el estado actual del conocimiento corporativo, con documentos que se agregan (nuevas políticas aprobadas, contratos firmados, versiones actualizadas de procedimientos), documentos que se modifican (revisiones de procedimientos, actualizaciones de precios, enmiendas contractuales), y documentos que se eliminan o revocan (políticas obsoletas, contratos cancelados, información que no debe estar disponible para el sistema RAG). La gestión del ciclo de vida de los documentos en el índice vectorial es el componente de knowledge management más crítico y más frecuentemente ignorado en implementaciones iniciales: cuando una política interna es actualizada, el sistema RAG debe reemplazar los chunks del documento anterior con los chunks del nuevo documento, no simplemente agregar los nuevos — de lo contrario, el índice contiene simultáneamente la versión antigua y la nueva del mismo documento, y el LLM puede sintetizar respuestas que combinan información contradictoria de ambas versiones. El pipeline de actualización incremental del índice se activa típicamente mediante eventos del DMS (Document Management System): cuando SharePoint, Confluence, o el DMS corporativo notifica un cambio mediante webhook, el pipeline identifica el documento_id afectado, elimina todos los chunks del índice vectorial con ese document_id, rechunkea y re-embeddea el documento actualizado, e inserta los nuevos chunks con el timestamp de la versión actual.

## Aspectos técnicos del knowledge management

- Event-driven indexing: webhooks de SharePoint Online, Confluence Cloud, o S3 Event Notifications que disparan el pipeline de indexación incremental cuando se crea, modifica, o elimina un documento en el DMS
- Document versioning en el índice: cada chunk almacena el document_id, la version del documento (hash SHA-256 del contenido o número de versión del DMS), y el timestamp de indexación, permitiendo detectar y reemplazar chunks de versiones anteriores
- Eliminación lógica vs física: cuando un documento se elimina del DMS, sus chunks deben eliminarse del índice vectorial o marcarse como deleted para que no aparezcan en las búsquedas — la eliminación física en Pinecone o Weaviate es posible mediante el document_id
- Freshness scoring: metadata de antigüedad en cada chunk (indexed_at, document_created_at, document_modified_at) que permite al sistema de retrieval penalizar chunks de documentos muy antiguos cuando existen versiones más recientes disponibles
- Monitoring de lag de indexación: alerta cuando el tiempo entre la modificación de un documento en el DMS y su disponibilidad en el índice vectorial supera el SLO definido (típicamente menos de 5 minutos para documentos críticos de negocio)

## Buena práctica

Implementar un test de regresión de knowledge currency que verifique semanalmente que los documentos más críticos del corpus (las 50 políticas más consultadas, los contratos activos más importantes) tienen su versión actualizada en el índice vectorial.
