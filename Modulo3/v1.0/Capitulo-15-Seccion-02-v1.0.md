# Capítulo 15 — Proyecto Integrador

## Sección 02: Definición del problema de negocio

### El contexto organizacional

TechCore S.A. es una empresa de servicios tecnológicos con doscientos empleados distribuidos en cuatro departamentos operativos: Tecnología de la Información (TI), Legal, Recursos Humanos y Finanzas. La compañía maneja una base documental interna extensa: políticas de seguridad, contratos tipo, manuales de procedimientos, runbooks de operaciones y normativas de cumplimiento. Esa documentación existe en formatos heterogéneos —PDF, documentos de texto, wikis internas, correos archivados— y está dispersa en sistemas distintos.

El problema no es la falta de información. El problema es el costo de acceder a ella. Un analista de TI que necesita el procedimiento de escalación de incidentes críticos puede tardarse veinte minutos en localizar el runbook correcto entre carpetas compartidas. Un empleado nuevo de Recursos Humanos que quiere saber el protocolo de baja por enfermedad consulta a tres personas distintas antes de obtener una respuesta definitiva. Un abogado interno que necesita una cláusula estándar de confidencialidad recorre los contratos archivados a mano.

### El proyecto

TechCore decide construir un asistente empresarial interno accesible vía interfaz de chat. El asistente debe responder preguntas operativas de los empleados usando la documentación interna como fuente de verdad, ejecutar acciones en sistemas corporativos cuando el usuario lo solicita, y recordar preferencias y contexto de conversaciones anteriores para no obligar al usuario a repetirse.

### Requisitos funcionales

El asistente debe satisfacer los siguientes requisitos para ser considerado una solución completa:

**RF-01. Respuestas contextualizadas por departamento.** El comportamiento del asistente varía según el departamento del usuario. Un empleado de TI recibe respuestas orientadas a procedimientos técnicos. Un empleado de Legal recibe respuestas con referencias normativas. La personalización del sistema debe ser transparente para el usuario pero configurable por el administrador.

**RF-02. Recuperación de documentación interna.** El asistente accede a la base documental corporativa y recupera fragmentos relevantes para cada consulta. No genera información que no esté en la documentación: cuando no encuentra respuesta, lo dice explícitamente y sugiere con quién consultar.

**RF-03. Ejecución de acciones en sistemas.** El asistente puede crear tickets de soporte en el sistema de gestión de incidentes, consultar el directorio de empleados, verificar el estado de solicitudes en curso y agendar recordatorios en el calendario corporativo. Todas las acciones requieren confirmación del usuario antes de ejecutarse.

**RF-04. Memoria de usuario.** El asistente recuerda, entre sesiones, las preferencias del usuario (idioma, nivel de detalle preferido, rol dentro del departamento) y el contexto de solicitudes en curso. Si un empleado estaba gestionando un incidente la semana anterior, el asistente puede retomar ese hilo cuando el empleado vuelva.

**RF-05. Análisis de incidentes de TI.** Para el departamento de TI, el asistente puede operar como un agente de análisis: dado un incidente reportado, consulta el historial de incidentes similares, revisa el runbook aplicable, propone pasos de diagnóstico ordenados y escala automáticamente al nivel de soporte correspondiente si el incidente supera los umbrales predefinidos.

**RF-06. Control de acceso por departamento y rol.** Los documentos de cada departamento son accesibles únicamente para empleados de ese departamento. Los documentos de alta confidencialidad (contratos activos, datos salariales) requieren nivel de autorización adicional. El asistente nunca revela información de un departamento a un usuario que no pertenece a él.

### Requisitos no funcionales

**RNF-01. Latencia aceptable.** Las respuestas simples (preguntas de procedimiento sin herramientas) deben llegar en menos de tres segundos. Las respuestas que implican recuperación de documentos deben llegar en menos de ocho segundos. Las respuestas del agente de análisis de incidentes pueden tomar hasta treinta segundos.

**RNF-02. Disponibilidad.** El sistema debe estar disponible durante el horario laboral extendido (6:00–22:00 hora local) con un objetivo de disponibilidad del 99 %.

**RNF-03. Auditoría.** Toda interacción debe quedar registrada con: identificador del usuario, departamento, marca de tiempo, consulta, respuesta y fuentes recuperadas. Los registros deben ser inmutables y conservarse durante doce meses.

**RNF-04. Infraestructura accesible.** La primera versión del sistema debe poder desplegarse con herramientas de mercado accesibles: un proveedor de LLM mediante API, una base vectorial gestionada, un almacén de clave-valor para la memoria, y servicios de logging estándar. No se asume infraestructura propietaria ni equipos de ML internos.

### Decisiones de alcance

El asistente de TechCore v1.0 tiene tres exclusiones explícitas de alcance:

1. **No entrena modelos propios.** Usa el LLM mediante API, sin fine-tuning. La personalización se logra exclusivamente vía Context Engineering.
2. **No opera en multiagente en la primera versión.** El agente de análisis de incidentes es un agente único con un conjunto fijo de herramientas. La arquitectura multiagente queda fuera del alcance de v1.0.
3. **No procesa imágenes ni documentos escaneados no procesados.** La base documental debe estar en texto extraíble. El procesamiento de imágenes y OCR es un requisito de v2.0.

### Por qué este caso ejerce todos los componentes del módulo

| Componente del módulo        | Requisito de TechCore que lo activa       |
|------------------------------|-------------------------------------------|
| Instrucciones del sistema    | RF-01 — comportamiento por departamento   |
| Ventana de contexto          | RF-04 — contexto de conversaciones largas |
| Memoria persistente          | RF-04 — memoria entre sesiones            |
| RAG                          | RF-02 — recuperación de documentación     |
| Herramientas                 | RF-03 — acciones en sistemas corporativos |
| Agentes                      | RF-05 — análisis de incidentes de TI      |
| Observabilidad               | RNF-01, RNF-03 — latencia y auditoría     |
| Seguridad                    | RF-06 — control de acceso por rol         |

Ningún componente queda sin uso. Esa cobertura completa es el criterio que valida TechCore como caso de referencia para el proyecto integrador.

---

Con los requisitos definidos, la siguiente sección construye la arquitectura que los satisface y produce el diagrama de referencia del capítulo.
