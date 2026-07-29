# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 04: Gobernanza de modelos y datos

La gobernanza de un sistema de IA es el conjunto de políticas, procesos y responsabilidades que definen cómo se toman las decisiones sobre el sistema: qué se cambia, quién lo aprueba, qué se registra y quién rinde cuentas. Sin gobernanza, la seguridad técnica es frágil: un sistema perfectamente instrumentado puede ser comprometido por un cambio no revisado en el system prompt realizado por alguien sin autoridad para hacerlo, o por la incorporación de una fuente de datos que no fue evaluada.

La gobernanza no es burocracia por la burocracia. Es la diferencia entre un sistema de IA que una organización puede controlar y uno que simplemente opera, esperando que nada salga mal.

### El sistema prompt como activo crítico

El system prompt es el artefacto de diseño más influyente de un sistema de Context Engineering. Define el comportamiento, las restricciones, el rol y los límites del sistema. Una modificación no autorizada o no revisada puede alterar el comportamiento del sistema de manera difícil de detectar sin observabilidad activa.

En muchas organizaciones que despliegan sistemas de IA por primera vez, el system prompt vive en una variable de entorno, en un archivo de configuración sin control de versiones o en el código de la aplicación sin proceso de revisión. Cualquier desarrollador con acceso puede modificarlo. Los cambios no se registran. No hay manera de saber cuándo fue la última modificación ni por qué.

La gobernanza del system prompt comienza por tratarlo como lo que es: un artefacto de software crítico que requiere los mismos controles que cualquier otro activo de producción.

**Control de versiones:** el system prompt vive en un repositorio de control de versiones con historial completo de modificaciones. Cada cambio tiene autor, timestamp y descripción.

**Proceso de aprobación:** los cambios al system prompt en producción requieren revisión por al menos dos personas: el AI Engineer que propone el cambio y un revisor —que puede ser otro ingeniero, un especialista en seguridad o un responsable del área de negocio— que verifica que el cambio no introduce riesgos no contemplados.

**Entornos separados:** los cambios se prueban en un entorno de staging antes de llegar a producción. El entorno de staging replica la configuración de producción y tiene datos representativos (anonimizados si es necesario) para evaluar el comportamiento del sistema con el nuevo prompt.

**Registro de despliegues:** cada despliegue de una nueva versión del system prompt queda registrado: quién lo aprobó, cuándo se desplegó, qué versión reemplazó. Este registro es necesario para investigar incidentes: si el sistema empieza a comportarse de manera anómala, el equipo puede correlacionar el inicio del problema con un cambio de configuración.

### Gobernanza del acceso a modelos

En organizaciones donde múltiples equipos despliegan sistemas de IA, es necesario establecer qué equipos pueden desplegar qué tipos de sistemas. No todos los equipos tienen la madurez técnica ni el conocimiento de seguridad para desplegar un agente con herramientas de escritura. No todos los casos de uso justifican el acceso a modelos de mayor capacidad o mayor costo.

Un marco de gobernanza de acceso a modelos establece:

**Niveles de sistema:** sistemas de solo lectura (el agente puede responder pero no ejecutar acciones), sistemas con herramientas de lectura (puede consultar bases de datos o APIs), sistemas con herramientas de escritura (puede modificar datos o enviar comunicaciones), sistemas con herramientas de alto impacto (puede autorizar transacciones, modificar configuraciones críticas). Cada nivel requiere un proceso de aprobación más riguroso.

**Propietarios del sistema:** cada sistema de IA en producción tiene un propietario identificado —una persona o un equipo— que es responsable de su comportamiento, de mantener la documentación actualizada y de responder ante incidentes. La propiedad no es nominal: el propietario debe recibir alertas cuando el sistema produce errores o comportamientos anómalos.

**Proceso de alta y baja:** los sistemas de IA nuevos requieren un proceso de alta que incluye revisión de seguridad, documentación de riesgos y aprobación del propietario. Los sistemas que dejan de usarse requieren un proceso de baja que incluye la eliminación de credenciales, el cierre de integraciones y el archivo o eliminación de datos asociados.

### Gobernanza de datos: qué puede entrar al contexto

La decisión de qué datos pueden incluirse en el contexto del modelo es una de las más importantes de la gobernanza. Los datos que entran al contexto están expuestos al modelo, potencialmente al usuario y, en sistemas de RAG, a cualquier otro componente del pipeline.

El principio rector es la **minimización de datos**: incluir en el contexto solo la información que el modelo necesita para completar la tarea, no toda la información disponible.

La minimización de datos tiene dos dimensiones:

**Minimización por tipo:** no todos los tipos de datos son apropiados para el contexto de un modelo. Los datos de identificación personal (PII) que no son necesarios para la tarea no deben incluirse. Los secretos corporativos que no son relevantes para la consulta no deben recuperarse. Las credenciales de sistemas internos no deben aparecer en el contexto bajo ninguna circunstancia.

**Minimización por usuario:** en sistemas multiusuario, el contexto de cada sesión debe contener solo los datos que ese usuario está autorizado a ver. Si el sistema RAG recupera un documento confidencial de otro departamento porque es semánticamente similar a la consulta, ese documento no debe llegar al contexto del usuario si ese usuario no tiene acceso a él.

### El catálogo de fuentes de datos

Un componente práctico de la gobernanza de datos es el catálogo de fuentes autorizadas: un registro de qué fuentes de datos puede indexar el sistema RAG, con qué frecuencia se actualizan, quién es el propietario de cada fuente y qué nivel de confidencialidad tiene su contenido.

| Fuente | Propietario | Clasificación | Actualización | Usuarios autorizados |
|--------|-------------|---------------|---------------|---------------------|
| Documentación de producto | Equipo de producto | Pública | Semanal | Todos |
| Procedimientos de RRHH | RRHH | Interna | Mensual | Empleados |
| Contratos con clientes | Legal | Confidencial | Manual | Legal, dirección |
| Configuraciones de sistema | Infraestructura | Restringida | Continua | Solo operaciones |

El catálogo establece qué fuentes pueden indexarse, qué filtros de acceso aplican a cada una y quién aprueba la incorporación de nuevas fuentes. Sin un catálogo, el sistema RAG puede indexar fuentes que nadie recuerda haber añadido, y el equipo de seguridad no tiene visibilidad de qué datos están siendo procesados.

### Proceso de aprobación para nuevas fuentes de datos

Añadir una nueva fuente de datos al sistema RAG debe seguir un proceso que incluya:

1. **Solicitud:** el equipo solicitante documenta qué fuente quiere añadir, por qué la necesita, qué tipo de datos contiene y quién es el propietario de los datos.

2. **Revisión de clasificación:** el propietario de los datos confirma la clasificación de confidencialidad del contenido.

3. **Revisión de seguridad:** el equipo de seguridad verifica que los filtros de acceso del sistema RAG sean compatibles con la clasificación. Si la fuente contiene datos de nivel "confidencial", el sistema debe poder filtrar los resultados de recuperación basándose en los permisos del usuario que realiza la consulta.

4. **Aprobación:** el propietario del sistema de IA aprueba la incorporación.

5. **Registro:** la nueva fuente se añade al catálogo con la fecha de incorporación y los detalles del proceso.

### Notas sobre el principio del mínimo privilegio

El capítulo 02 de este módulo introdujo brevemente el principio del mínimo privilegio en el contexto del diseño de herramientas para agentes. La gobernanza es el mecanismo que hace ese principio operativo a escala organizacional.

El mínimo privilegio aplicado a los sistemas de IA significa:
- El sistema recibe acceso solo a los datos que necesita para su función.
- Las herramientas habilitadas tienen solo los permisos que la función del sistema requiere.
- Los usuarios tienen acceso solo a los datos y funcionalidades que su rol autoriza.
- Los cambios que amplían privilegios requieren aprobación explícita.

Un sistema de atención al cliente no necesita acceso a los contratos con proveedores. Un asistente de redacción no necesita acceso a las bases de datos de clientes. Un agente de análisis de datos no necesita herramientas de envío de correo. Cada vez que el sistema tiene más acceso del que necesita, la superficie de ataque se amplía innecesariamente.

### Nota del arquitecto

La gobernanza es percibida frecuentemente como un freno al ritmo de desarrollo. En las primeras fases de un proyecto de IA, cuando el equipo está experimentando y el sistema aún no está en producción, es razonable operar con procesos ligeros. Pero el momento de establecer los controles de gobernanza no es después del lanzamiento, sino antes. Un sistema que lleva meses en producción sin gobernanza tiene deuda acumulada: system prompts que nadie sabe exactamente qué versión es la actual, fuentes de datos que nadie recuerda quién añadió, permisos que se ampliaron "temporalmente" y nunca se revisaron.

La siguiente sección aborda la privacidad: los principios de diseño para garantizar que la información personal de los usuarios sea tratada de manera apropiada en todas las etapas del pipeline del contexto.
