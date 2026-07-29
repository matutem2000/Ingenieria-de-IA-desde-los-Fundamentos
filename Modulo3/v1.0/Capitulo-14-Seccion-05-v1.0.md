# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 05: Privacidad y protección de información

La privacidad en sistemas de Context Engineering no es un problema legal que el equipo jurídico resuelve antes del lanzamiento. Es una propiedad de diseño que el AI Engineer construye o destruye en cada decisión sobre qué datos incluir en el contexto, cómo se almacenan las conversaciones y qué puede ver el modelo sobre cada usuario.

Esta sección no pretende ser una guía legal de privacidad —las regulaciones varían por jurisdicción y evolucionan constantemente—. Lo que desarrolla son los principios de privacidad por diseño aplicados específicamente al Context Engineering: principios que se mantienen válidos independientemente de la regulación aplicable y que, en la mayoría de los casos, suponen cumplir con los requisitos regulatorios como consecuencia.

### El problema específico del contexto

Los sistemas de Context Engineering tienen características que crean riesgos de privacidad específicos:

**El contexto concentra información.** Un sistema de RAG con memoria puede construir un contexto que incluye el historial de conversaciones del usuario, documentos recuperados de su carpeta personal, su nombre, su cargo y su actividad reciente. Esa concentración de información en un único flujo de texto que el modelo recibe es conveniente para el sistema pero es también una concentración de riesgo: si ese contexto es interceptado, registrado sin los controles apropiados o accedido por un usuario no autorizado, el daño es mayor que si cada pieza de información estuviera dispersa.

**Los LLMs pueden memorizar datos de entrenamiento.** Si el sistema se ajusta con datos de usuarios, el modelo puede "memorizar" información específica y revelarla en respuestas a otros usuarios. Este riesgo es más relevante para sistemas que hacen fine-tuning continuo con datos de producción.

**La memoria del agente persiste.** En sistemas con memoria persistente (capítulo 09), el agente acumula información del usuario a lo largo de múltiples sesiones. Esa información puede incluir datos personales que el usuario compartió en una conversación y que no esperaba que permanecieran en el sistema indefinidamente.

**Las respuestas pueden contener datos de terceros.** En sistemas de RAG que indexan documentos de múltiples usuarios, el sistema puede recuperar e incluir en su respuesta información sobre una persona diferente al usuario que realizó la consulta.

### Privacidad por diseño: los siete principios aplicados al contexto

La privacidad por diseño es un enfoque establecido que propone incorporar la protección de datos en el diseño del sistema, no como una capa posterior. Sus siete principios, aplicados al Context Engineering, producen decisiones de diseño concretas:

**1. Proactivo, no reactivo.** Los riesgos de privacidad se identifican antes del lanzamiento, no después de un incidente. En la práctica: realizar un análisis de impacto en privacidad (Privacy Impact Assessment) antes de que el sistema procese datos reales de usuarios.

**2. Privacidad por defecto.** La configuración predeterminada del sistema protege la privacidad. En la práctica: la memoria del agente está desactivada por defecto y el usuario debe activarla explícitamente; el contexto incluye por defecto el mínimo de datos del usuario necesario para la tarea.

**3. Privacidad integrada en el diseño.** La privacidad no es una función adicional sino parte de la arquitectura. En la práctica: el pipeline de construcción del contexto incluye un paso de filtrado de PII antes de que los datos lleguen al modelo; el sistema RAG aplica filtros de acceso por usuario antes de recuperar documentos.

**4. Funcionalidad total.** La privacidad no sacrifica la funcionalidad del sistema. En la práctica: en lugar de excluir datos que el sistema necesita para funcionar, se anonimiza la información que no necesita ser personal (usar "el usuario" en lugar del nombre real cuando el nombre no es necesario para la tarea).

**5. Seguridad de extremo a extremo.** La protección opera en todo el ciclo de vida del dato. En la práctica: los datos del usuario se cifran en tránsito y en reposo; el historial de conversaciones tiene una política de retención definida y se elimina al final del período.

**6. Visibilidad y transparencia.** El usuario puede conocer qué datos tiene el sistema sobre él. En la práctica: el sistema ofrece un mecanismo para que el usuario consulte qué información tiene almacenada y para solicitar su eliminación.

**7. Respeto por la privacidad del usuario.** El sistema no recopila más datos de los que necesita. En la práctica: el sistema no registra el contenido completo de las conversaciones si solo necesita registrar métricas de uso; no almacena el historial de consultas si la funcionalidad que ofrece es de solo una sesión.

### El flujo de decisión: ¿este dato debe estar en el contexto?

La decisión práctica más frecuente a la que se enfrenta el AI Engineer en materia de privacidad es simple en su formulación pero compleja en su aplicación: ¿este dato debe incluirse en el contexto?

El siguiente flujo de decisión proporciona una guía práctica:

```
¿El modelo necesita este dato para completar la tarea?
    ├── No → No incluir en el contexto.
    └── Sí ↓
        ¿El usuario está informado de que este dato se procesa?
            ├── No → Informar antes de procesar.
            └── Sí ↓
                ¿El dato contiene PII que puede anonimizarse
                sin perder utilidad para la tarea?
                    ├── Sí → Anonimizar antes de incluir.
                    └── No ↓
                        ¿El dato pertenece solo a este usuario
                        o incluye datos de terceros?
                            ├── Incluye terceros → Revisar
                            │   autorización o anonimizar.
                            └── Solo este usuario → Incluir
                                con los controles de retención
                                apropiados.
```

Este flujo no elimina todas las ambigüedades, pero establece una disciplina de razonamiento que lleva al AI Engineer a considerar la privacidad antes de añadir datos al contexto, en lugar de hacerlo después de que el sistema ya los esté procesando.

### Técnicas de protección de PII en el contexto

Cuando el dato debe estar en el contexto pero contiene PII, existen técnicas que reducen el riesgo sin eliminar la utilidad:

**Anonimización:** reemplazar los identificadores personales por tokens genéricos. El nombre "María López" se convierte en "el usuario", la dirección exacta se convierte en "la dirección del cliente". Esta técnica es apropiada cuando el modelo no necesita conocer la identidad específica para completar la tarea.

**Pseudonimización:** reemplazar los identificadores por identificadores ficticios consistentes. El usuario "María López" se convierte en "Usuario_A7F3" en todos los registros de la sesión. A diferencia de la anonimización, la pseudonimización permite vincular eventos de la misma sesión sin revelar la identidad real. Es apropiada para sistemas de análisis que necesitan seguir el comportamiento de un usuario sin conocer su identidad.

**Tokenización:** los datos sensibles (números de tarjeta, identificadores de seguridad social) se reemplazan por tokens que el sistema puede usar para referencias pero que no tienen valor informativo fuera del sistema. El token se resuelve a través de un sistema seguro solo cuando la transacción lo requiere.

**Minimización de precisión:** en lugar de incluir la dirección exacta del usuario, incluir solo el código postal. En lugar de incluir la fecha de nacimiento exacta, incluir solo el grupo etario. La precisión reducida disminuye el riesgo sin necesariamente impedir la función del sistema.

### Política de retención de datos del contexto

El contexto que el sistema genera y procesa en cada sesión contiene información que puede ser sensible. La política de retención define por cuánto tiempo se conserva esa información y bajo qué condiciones se elimina.

Para sistemas de IA, una política de retención mínima incluye:

- **Logs de inferencia:** los registros de qué contexto recibió el modelo y qué respuesta generó. Estos registros son necesarios para la observabilidad y la investigación de incidentes. El período de retención típico es de 30 a 90 días. Los logs no deben conservarse más tiempo del necesario para sus fines operativos.

- **Historial de conversaciones:** en sistemas con memoria, las conversaciones pasadas que se incluyen en el contexto de sesiones futuras. El período de retención debe estar alineado con la expectativa del usuario: si el usuario espera que el asistente "recuerde" conversaciones de la semana pasada, la retención de una semana es apropiada; si el usuario no tiene esa expectativa, el historial no debe persistir entre sesiones.

- **Datos de memoria del agente:** la información estructurada que el agente extrae de las conversaciones y almacena como memoria a largo plazo. Debe existir un mecanismo para que el usuario consulte y elimine esta información.

- **Datos de evaluación:** los fragmentos de conversaciones usados para evaluar y mejorar el sistema. Estos datos deben ser anonimizados antes de usarse para evaluación y solo pueden conservarse para ese fin con el consentimiento apropiado del usuario.

### Nota del arquitecto

El error más frecuente en la gestión de privacidad de sistemas de IA no es el incumplimiento deliberado, sino la ausencia de política: el sistema registra todo porque "puede ser útil para depuración", el historial de conversaciones nunca se elimina porque "nadie configuró la eliminación automática", los documentos recuperados quedan en caché sin política de expiración. La privacidad por diseño exige que cada tipo de dato tenga una política explícita: qué se guarda, por cuánto tiempo, quién puede acceder y cómo se elimina. Un sistema que no tiene esas políticas definidas tiene, en la práctica, una política de retención indefinida y acceso no controlado.

La siguiente sección aborda la gestión de identidades y permisos: cómo el sistema controla quién puede hacer qué, tanto para los usuarios que interactúan con él como para los componentes del sistema que operan en su nombre.
