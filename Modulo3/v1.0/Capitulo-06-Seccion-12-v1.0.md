# Módulo 3 — Context Engineering

# Capítulo 06 — RAG (Retrieval-Augmented Generation) como componente del Context Engineering

## Sección 12 — Checklist del AI Engineer

> *"Un checklist no reemplaza el criterio. Lo estructura para que el criterio no se pierda bajo la presión del proyecto."*

---

## Propósito

Este checklist está organizado en tres momentos del ciclo de vida de un sistema RAG: antes de construir, durante la implementación y en producción. No es exhaustivo: es el conjunto mínimo de preguntas que un AI Engineer debe poder responder en cada etapa. Si alguna respuesta es "no sé" o "no lo hemos definido", esa es la señal de que esa decisión requiere atención antes de avanzar.

---

## Antes de construir

### Validación del problema

- [ ] ¿El conocimiento que el sistema necesita está efectivamente fuera del modelo base (es reciente, privado o de nicho)?
- [ ] ¿La respuesta correcta depende de documentos específicos cuya fuente necesita ser trazable?
- [ ] ¿El conocimiento cambia con frecuencia suficiente como para que el fine-tuning sea impracticable?
- [ ] ¿Se evaluó si el problema puede resolverse con instrucciones del sistema bien diseñadas, sin necesidad de RAG?

### Definición del corpus

- [ ] ¿Están definidos qué documentos forman parte del corpus y cuáles no?
- [ ] ¿El corpus tiene una fuente canónica de verdad (un repositorio oficial, un sistema de gestión documental)?
- [ ] ¿Se identificaron documentos obsoletos, duplicados o de baja calidad que deben excluirse?
- [ ] ¿Existe un proceso claro para agregar nuevos documentos al corpus?

### Requisitos de seguridad y acceso

- [ ] ¿Hay documentos con distintos niveles de confidencialidad?
- [ ] ¿El sistema debe implementar control de acceso a nivel de fragmento?
- [ ] ¿El corpus puede enviarse a APIs externas o debe procesarse localmente por requisitos de privacidad?

---

## Durante la implementación

### Fase de indexación

- [ ] ¿Se evaluaron al menos dos estrategias de chunking (fija y semántica) sobre una muestra del corpus?
- [ ] ¿El tamaño del chunk es compatible con la longitud máxima del modelo de embedding?
- [ ] ¿Se definió el solapamiento y se justificó en función del tipo de documentos?
- [ ] ¿Los metadatos de cada fragmento incluyen fuente, fecha de creación/modificación, tipo de documento y nivel de acceso?
- [ ] ¿Se verificó que los fragmentos generados son coherentes (no parten ideas a mitad)?

### Modelo de embedding

- [ ] ¿El modelo de embedding fue evaluado en el idioma y dominio del corpus específico?
- [ ] ¿Se consultaron benchmarks públicos (MTEB u otro) para comparar opciones?
- [ ] ¿La misma versión del modelo se usará tanto para indexar documentos como para procesar consultas?

### Base vectorial

- [ ] ¿La base vectorial soporta filtrado por metadatos con la granularidad requerida?
- [ ] ¿El algoritmo de indexación (HNSW, IVF) está configurado para el volumen de fragmentos del corpus?
- [ ] ¿La base vectorial permite actualizaciones incrementales sin reindexación completa?
- [ ] ¿Se diseñó la estrategia de backup y recuperación del índice?

### Estrategia de recuperación

- [ ] ¿Se evaluó si el retrieval naive (top-k por similitud) es suficiente o si se requieren estrategias adicionales (HyDE, expansión de consulta, MMR)?
- [ ] ¿Se implementa búsqueda híbrida (dense + sparse) cuando el corpus requiere coincidencia exacta de términos?
- [ ] ¿El valor de k (número de candidatos recuperados) está justificado en función del presupuesto de contexto?

### Re-ranking y selección de contexto

- [ ] ¿Se implementa algún modelo de re-ranking (cross-encoder) o el retrieval vectorial es el criterio final?
- [ ] ¿El re-ranking temporal está habilitado para dominios con información que cambia frecuentemente?
- [ ] ¿El presupuesto de tokens para fragmentos está calculado correctamente, descontando instrucciones del sistema y reserva para la respuesta?
- [ ] ¿El orden de inserción de fragmentos en el contexto está optimizado para la atención del modelo?

### Conjunto de evaluación

- [ ] ¿Existe un conjunto de consultas de evaluación con los fragmentos esperados marcados?
- [ ] ¿Se calculó precision@k y recall@k baseline antes de desplegar a producción?
- [ ] ¿El conjunto de evaluación cubre los tipos de consulta más frecuentes en la aplicación?

---

## En producción

### Política de actualización del índice

- [ ] ¿Existe un proceso automatizado para detectar cambios en el corpus fuente?
- [ ] ¿El proceso de actualización elimina correctamente los fragmentos obsoletos?
- [ ] ¿Se registra en un log de auditoría cada operación de agregar, modificar o eliminar fragmentos?
- [ ] ¿Existe un mecanismo para invalidar manualmente fragmentos que se detecten incorrectos?

### Monitoreo de calidad

- [ ] ¿Se monitorea la latencia del pipeline completo (desde consulta hasta respuesta)?
- [ ] ¿Se registra qué fragmentos se recuperan para cada consulta (para análisis posterior)?
- [ ] ¿Existe una forma de detectar cuando el retrieval sistemáticamente no encuentra fragmentos relevantes?
- [ ] ¿Se calculan métricas de retrieval (precision@k, MRR) sobre muestras de producción periódicamente?

### Trazabilidad y auditoría

- [ ] ¿La respuesta del sistema incluye referencia a las fuentes utilizadas?
- [ ] ¿Los logs permiten reconstruir qué fragmentos se insertaron en el contexto para una consulta específica?
- [ ] ¿Se almacenan los metadatos de versión del documento fuente junto con cada respuesta?

### Seguridad

- [ ] ¿Se verifica en cada consulta que el usuario tiene permisos para ver los fragmentos recuperados?
- [ ] ¿El sistema previene que el contenido de fragmentos confidenciales aparezca en respuestas a usuarios no autorizados?
- [ ] ¿Se registran intentos de acceso a fragmentos fuera del nivel de autorización del usuario?

---

## Señales de alerta en producción

Estas son situaciones que indican degradación del sistema y requieren investigación inmediata:

- **Usuarios reportan que la información está desactualizada:** el índice no se está actualizando correctamente.
- **Las respuestas son genéricas aunque el corpus tiene información específica:** el retrieval no está encontrando los fragmentos correctos.
- **El modelo declara frecuentemente "no tengo información suficiente":** k puede ser demasiado bajo, o el chunking produce fragmentos poco coherentes.
- **La latencia del pipeline aumenta progresivamente:** el índice creció sin reconfigurar los parámetros del algoritmo de búsqueda.
- **Respuestas contradictorias para la misma consulta:** el índice puede contener versiones distintas del mismo documento.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
