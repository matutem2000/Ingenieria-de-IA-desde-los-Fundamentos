# Capítulo 12 — Context Engineering Empresarial

## Sección 11: Laboratorio práctico

### Descripción del ejercicio

Este laboratorio es un ejercicio de diseño de plataforma, no de implementación de código. El objetivo es que el estudiante tome decisiones de arquitectura de Context Engineering para una organización concreta, aplicando los principios del capítulo y explicitando el razonamiento detrás de cada decisión.

El ejercicio simula la situación real más frecuente en proyectos de IA empresarial: un profesional que debe diseñar la arquitectura de contexto para una organización que ya tiene múltiples necesidades de IA activas, sistemas corporativos existentes y restricciones organizacionales concretas.

---

### La organización: Meridian Legal Group

**Meridian Legal Group** es un estudio jurídico con 220 empleados distribuidos en cuatro divisiones:

- **División Corporativa** (55 abogados + 20 analistas): contratos comerciales, fusiones y adquisiciones, reestructuraciones.
- **División Laboral** (30 abogados + 15 analistas): asesoría en derecho laboral, conflictos, cumplimiento normativo.
- **División Regulatoria** (25 abogados + 10 analistas): asesoría en regulación sectorial, compliance, trámites ante organismos.
- **División de Litigios** (35 abogados + 20 analistas): representación en procesos judiciales, arbitraje.
- **Equipo de soporte** (10 personas): tecnología, documentación, administración.

**Sistemas corporativos existentes:**

- **Sistema de gestión documental** (SharePoint): 180.000 documentos, incluyendo contratos de clientes, memorandos internos, jurisprudencia recopilada, plantillas de documentos y guías de práctica.
- **Sistema de gestión de casos** (software especializado legal): registro de todos los casos activos e históricos, con estado, responsables, fechas clave y notas de seguimiento.
- **Sistema de facturación y horas** (TimeTracker): registro de horas billables por abogado y caso, facturas, cobros.
- **Directorio corporativo** (Active Directory): gestión de identidades, grupos de seguridad por división y niveles de acceso.

**Restricciones específicas de Meridian:**

- La información de clientes está sujeta al secreto profesional. Ningún abogado de una división puede acceder a información de clientes de otra división sin autorización explícita del cliente.
- La jurisprudencia interna —las posiciones que el estudio ha tomado en casos anteriores— es altamente sensible competitivamente. No debe estar disponible para personas externas.
- Las guías de práctica y plantillas son comunes a todo el estudio, pero cada división las personaliza para su práctica específica.

**Las necesidades de IA identificadas por la dirección de Meridian:**

1. **Asistente de investigación jurídica**: ayudar a abogados y analistas a encontrar jurisprudencia relevante, doctrina y precedentes internos para un caso específico.
2. **Asistente de revisión de contratos**: asistir en la revisión de contratos recibidos, identificando cláusulas que se desvíen de los estándares del estudio o que representen riesgos no habituales.
3. **Asistente de documentación de casos**: ayudar a generar resúmenes de casos, memorandos de posición y minutas de reuniones en el formato estándar del estudio.
4. **Asistente de búsqueda regulatoria**: para la División Regulatoria, acceso rápido a regulaciones vigentes, modificaciones recientes y criterios de los organismos de contralor relevantes.

---

### Parte 1: Diseño de la arquitectura de capas (45 minutos)

**Tarea:** Diseñar la arquitectura de capas de conocimiento para la plataforma de IA de Meridian.

Para cada capa, el estudiante debe especificar:

**a) Contenido de la capa corporativa.**
¿Qué conocimiento de Meridian debe estar disponible para todos los asistentes de todas las divisiones? Proponer al menos seis elementos concretos que pertenecerían a esta capa.

**b) Contenido de las capas divisionales.**
Para cada una de las cuatro divisiones, ¿qué conocimiento específico debe estar disponible solo para los asistentes de esa división? Proponer al menos tres elementos por división.

**c) Diseño del control de acceso.**
Dado el requisito de secreto profesional entre divisiones, describir cómo el sistema de IA gestionaría los permisos de acceso al conocimiento de clientes específicos. ¿Qué mecanismo técnico se usaría para garantizar que un abogado de la División Laboral no pueda, mediante el asistente de IA, acceder a información de un cliente de la División Corporativa?

**d) Tratamiento del conocimiento sensible.**
La jurisprudencia interna es competitivamente sensible. ¿Debe incluirse en la base vectorial? Si sí, ¿con qué controles? Si no, ¿cómo puede el asistente de investigación jurídica acceder a ella?

---

### Parte 2: Diseño del gobierno del conocimiento (30 minutos)

**Tarea:** Diseñar el proceso de gobierno del conocimiento para Meridian.

**a) Asignación de propietarios.**
Para cada fuente de conocimiento identificada en la Parte 1, asignar un propietario específico dentro de la estructura organizacional de Meridian. Justificar la asignación.

**b) Proceso de incorporación.**
Diseñar el proceso de incorporación de nuevos documentos a la capa corporativa y a las capas divisionales. ¿Qué pasos tiene? ¿Cuánto tiempo debería tomar? ¿Qué criterios de calidad aplican?

**c) Proceso de actualización.**
Meridian actualiza sus guías de práctica dos veces al año y actualiza la jurisprudencia interna continuamente. Diseñar el proceso de actualización para cada tipo de conocimiento, especificando frecuencia, responsables y mecanismo de propagación a las bases vectoriales.

**d) Proceso de retiro.**
Cuando un cliente termina su relación con el estudio, ¿qué debe ocurrir con la información de ese cliente en el sistema de IA? Diseñar el proceso de retiro.

---

### Parte 3: Diseño de integración y métricas (30 minutos)

**a) Mapa de integración con sistemas existentes.**
Para cada uno de los cuatro asistentes de IA requeridos, especificar qué sistemas corporativos debe consultar y con qué patrón de integración (conocimiento indexado en base vectorial, recuperación dinámica como herramienta, o ninguna integración directa). Justificar cada decisión.

**b) Diseño del asistente de investigación jurídica.**
Este asistente es el de mayor complejidad y mayor valor potencial. Diseñar el contexto que recibe para una consulta típica: "encontrar jurisprudencia relevante sobre cláusulas de limitación de responsabilidad en contratos de tecnología". Especificar:
- Qué está en las instrucciones del sistema.
- Qué se recupera de qué fuente de conocimiento.
- Qué datos dinámicos se recuperan, si alguno.
- Qué restricciones de acceso aplican.

**c) Métricas de negocio.**
Meridian no tiene métricas históricas del tiempo que sus abogados dedican a tareas de investigación y documentación porque nunca lo midió de forma sistemática. Diseñar un plan de medición de baseline que permita, en los tres meses previos al despliegue, establecer las métricas necesarias para demostrar el ROI del sistema de IA. ¿Qué se mide? ¿Cómo? ¿Con qué herramientas?

---

### Criterios de evaluación

El trabajo se evalúa en cuatro dimensiones.

**Completitud técnica:** ¿El diseño cubre todos los componentes necesarios para que los cuatro asistentes funcionen en producción? ¿Se identificaron las integraciones necesarias? ¿Se especificó el control de acceso?

**Adecuación al contexto:** ¿Las decisiones de diseño reflejan las restricciones específicas de Meridian —secreto profesional, sensibilidad competitiva, estructura divisional— o son genéricas? Un diseño correcto para Meridian puede no ser correcto para otra organización, y viceversa.

**Viabilidad organizacional:** ¿Los procesos de gobierno propuestos son factibles para una organización de 220 personas? ¿El proceso de incorporación de documentos es lo suficientemente ágil como para que los abogados lo usen sin resistencia?

**Razonamiento explícito:** ¿El estudiante explicó por qué tomó cada decisión de diseño, incluyendo las alternativas que consideró y las razones para descartarlas? Las decisiones sin razonamiento no demuestran comprensión; demuestran memorización.

---

### Nota del laboratorio

No existe una solución única correcta para este ejercicio. Existen soluciones mejor y peor argumentadas, mejor y peor adaptadas al contexto específico de Meridian, más y menos viables operacionalmente. El objetivo no es encontrar la solución perfecta; es desarrollar el proceso de razonamiento de diseño que un AI Engineer necesita para abordar situaciones similares en contextos reales.

Un profesional que completa este ejercicio con rigor estará preparado para llevar a una primera reunión con la dirección de una organización mediana una propuesta de arquitectura coherente, con decisiones justificadas y con claridad sobre los riesgos y las limitaciones del diseño propuesto.
