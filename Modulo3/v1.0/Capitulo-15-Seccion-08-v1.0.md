# Capítulo 15 — Proyecto Integrador

## Sección 08: Estrategia de despliegue y operación

Un sistema bien diseñado que no puede desplegarse de manera confiable no tiene valor en producción. Esta sección define la estrategia de despliegue de TechCore: cómo se lleva el sistema de desarrollo a producción, cómo se mantiene operativo, y cómo se gestiona su evolución después del lanzamiento inicial.

### El principio del despliegue incremental

TechCore no se despliega en un único momento para todos sus usuarios. La estrategia es incremental: se valida en contextos controlados antes de exponer el sistema a toda la organización. Esto reduce el riesgo de un fallo masivo y permite recoger retroalimentación real antes de que el sistema opere a escala completa.

La estrategia de despliegue tiene cuatro fases:

**Fase 0 — Entorno de desarrollo.** El sistema opera en un entorno aislado con datos ficticios. Los desarrolladores interactúan con él para verificar el comportamiento funcional de cada componente. No hay usuarios reales. La base documental RAG contiene documentos de prueba, no la documentación corporativa real.

**Fase 1 — Piloto con equipo de TI (semanas 1–4).** Se despliega el sistema con datos reales solo para el equipo de TI, que es el departamento con el caso de uso más complejo (el agente de incidentes). El objetivo de esta fase es identificar fallas en el pipeline de RAG con documentación real, validar que el agente de incidentes se comporta correctamente, y calibrar los umbrales de latencia con carga real. Al final de la fase 1, se tiene un sistema funcional validado con un departamento.

**Fase 2 — Expansión a todos los departamentos (semanas 5–8).** Se onboardean los perfiles de Legal, RRHH y Finanzas. La base documental RAG se amplía con la documentación de esos departamentos. El objetivo de esta fase es validar que el control de acceso por departamento funciona correctamente con múltiples perfiles activos simultáneamente. Al final de la fase 2, todos los departamentos pueden usar el sistema.

**Fase 3 — Despliegue a toda la organización (semana 9 en adelante).** El sistema se abre a todos los empleados. Se activa el monitoreo operacional completo. Se establece el proceso de gestión de incidentes del propio sistema de IA (separado del agente de incidentes de TI, que es una funcionalidad, no la operación del sistema).

### La infraestructura de cada componente

Conforme a RNF-04, TechCore v1.0 usa infraestructura de mercado accesible, no infraestructura propietaria.

| Componente              | Tecnología de mercado          | Alternativa de contingencia         |
|-------------------------|--------------------------------|-------------------------------------|
| LLM principal           | API de proveedor (ej. Anthropic, OpenAI) | Segundo proveedor configurado como fallback |
| Embeddings              | API del mismo proveedor        | Modelo de embeddings local (menor calidad) |
| Base vectorial          | Servicio gestionado (ej. Pinecone, Weaviate) | PostgreSQL con extensión pgvector |
| Memoria persistente     | Redis gestionado               | PostgreSQL como KV store            |
| Logging                 | Servicio de logs estructurados | Archivos locales + rotación         |
| Orquestador             | Servicio de aplicación (contenedor) | VM con auto-reinicio              |
| Capa de presentación    | Aplicación web + API REST      | Bot de mensajería corporativa       |

La columna de alternativas de contingencia no es un plan B menor: es un plan B explícito y probado. Cada alternativa debe estar documentada y haber sido ejercitada en el entorno de desarrollo antes del lanzamiento.

### Gestión de versiones de la base documental

La base documental RAG no es estática. Los runbooks se actualizan, las políticas cambian, los contratos se renuevan. TechCore necesita un proceso para mantener el índice vectorial sincronizado con la documentación real.

El proceso de actualización de la base documental tiene cuatro pasos:

**Paso 1 — Detección de cambios.** El sistema de gestión documental de TechCore (SharePoint, Confluence, o equivalente) tiene webhooks configurados que notifican al pipeline de ingestión cuando un documento es creado, modificado o eliminado.

**Paso 2 — Re-ingestión del documento modificado.** El pipeline de ingestión procesa el documento actualizado: lo fragmenta, genera los embeddings de cada fragmento, y los almacena en el índice vectorial con los metadatos actualizados.

**Paso 3 — Eliminación de los fragmentos anteriores.** Los fragmentos del documento anterior se eliminan del índice para evitar que el sistema recupere información desactualizada. La eliminación usa el identificador del documento como clave de búsqueda y eliminación masiva.

**Paso 4 — Registro del cambio.** El evento de actualización queda registrado en el log de administración con: nombre del documento, número de fragmentos anteriores eliminados, número de fragmentos nuevos indexados, y timestamp.

Este proceso asegura que el índice vectorial refleja siempre la versión más reciente de cada documento. No es necesario re-indexar toda la base documental cuando un documento cambia: solo se re-indexa el documento modificado.

### El proceso de actualización de instrucciones del sistema

Las instrucciones del sistema se actualizan con mayor frecuencia que el código de la aplicación. Un cambio de política del departamento de TI puede requerir ajustar la instrucción del sistema del perfil TI sin tocar el código.

Para que ese proceso sea ágil y seguro, TechCore implementa un sistema de versionado de instrucciones:

```
Instrucciones del sistema — Estructura de versionado

/instrucciones/
  ti/
    v1.0.txt  → versión en producción
    v1.1.txt  → versión en prueba A/B (10% del tráfico TI)
    draft.txt → borrador sin desplegar
  legal/
    v1.0.txt  → versión en producción
  rrhh/
    v1.0.txt  → versión en producción
  finanzas/
    v1.0.txt  → versión en producción
```

El orquestador lee la instrucción del sistema activa para cada perfil desde este almacén. Cambiar la instrucción del sistema en producción es una operación de escritura en el almacén, no un re-despliegue del servicio. El cambio tarda menos de un minuto en propagarse.

La funcionalidad de prueba A/B permite validar una nueva instrucción del sistema con un subconjunto del tráfico antes de activarla para todos los usuarios. Si las métricas de calidad del grupo de prueba son superiores al grupo de control, se promueve la nueva versión.

### Mantenimiento operacional

El sistema en producción requiere cuatro actividades de mantenimiento recurrentes:

**Revisión semanal de métricas.** El responsable de operaciones revisa el panel de monitoreo y verifica que las nueve métricas operacionales están dentro de los objetivos. Si alguna métrica se acerca a su umbral de alerta, se abre un ticket de investigación.

**Revisión mensual de la base documental.** El equipo de cada departamento verifica que los documentos en el índice RAG están actualizados. Comparan la lista de documentos del índice contra el sistema documental corporativo y señalan cualquier discrepancia.

**Revisión trimestral de instrucciones del sistema.** El responsable de cada departamento revisa la instrucción del sistema de su perfil y verifica que sigue alineada con las políticas actuales del departamento. Si hay cambios relevantes, actualiza la instrucción y la somete a prueba A/B antes de promoverla.

**Revisión anual de costos y proveedor.** El equipo técnico revisa los costos de la API del LLM, la base vectorial y los servicios gestionados. Evalúa si la estructura de costos actual es sostenible y si existen alternativas que ofrezcan mejor relación costo-calidad para el volumen actual de uso.

### Gestión de incidentes del propio sistema

TechCore tiene un agente de análisis de incidentes de TI, pero ese agente es una funcionalidad del sistema. El sistema mismo también puede tener incidentes: el orquestador puede quedar no disponible, la base vectorial puede degradarse, la API del LLM puede devolver errores.

El proceso de gestión de incidentes del sistema de IA sigue el mismo proceso que cualquier sistema de software corporativo: reporte en el sistema de tickets, clasificación por severidad, asignación al equipo responsable, y resolución documentada. La única diferencia es que el equipo responsable del sistema de IA necesita acceder a las trazas de interacción para diagnosticar qué falló y en qué etapa del pipeline.

Ese acceso está disponible a través del panel de monitoreo y de las consultas directas al sistema de logs. La traza de interacción completa, con latencias por etapa y errores registrados, es la herramienta de diagnóstico principal.

---

Con el diseño completo del sistema establecido en las secciones 03 a 08, el capítulo entra en su bloque de revisión crítica. La siguiente sección identifica los errores que emergen específicamente cuando se integran todos los componentes, distintos de los errores que ya aparecieron en capítulos individuales.
