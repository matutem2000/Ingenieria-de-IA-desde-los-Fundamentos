# Capítulo 04 — Sección 11

# Caso de estudio empresarial

## Sistema de asistencia al equipo de consultoría — Firma de servicios profesionales

Esta sección traza la evolución de un sistema de asistencia de IA para un equipo de consultores de gestión. El caso es representativo de los problemas que cualquier equipo enfrenta cuando pasa de un prototipo de chat a un sistema de producción con múltiples usuarios, sesiones largas y expectativa de continuidad.

Los detalles específicos de la empresa son compuestos y anonimizados, pero los problemas y las soluciones son directamente derivados de patrones observados en implementaciones reales.

## El contexto

Una firma de consultoría de gestión con 80 consultores implementó un asistente de IA interno para apoyar el trabajo de investigación, redacción de propuestas y análisis de datos de sus proyectos. El piloto inicial fue un chatbot simple basado en un LLM con acceso a la documentación interna de la empresa.

El piloto fue bien recibido. Los consultores lo usaban para buscar metodologías de proyectos anteriores, redactar borradores de secciones de propuestas y explorar benchmarks de industria. Sin embargo, a los tres meses del piloto, emergieron quejas recurrentes:

- "Tengo que explicarle quién soy cada vez que abro el chat."
- "Sabe que estoy trabajando en el proyecto Antares, pero en la próxima sesión no recuerda nada."
- "Me propuso una metodología que yo mismo le dije que no aplica en nuestro contexto hace dos semanas."

El equipo de tecnología diagnosticó el problema correctamente: el sistema no tenía memoria persistente. Cada sesión comenzaba desde cero.

## La decisión de diseño: qué recordar

El primer debate fue sobre qué debería recordar el sistema. El equipo identificó tres categorías de información con distintos valores y distintos requisitos de actualización:

**Perfil del consultor (memoria semántica estable):**
- Nombre, rol y nivel de seniority
- Áreas de especialización (industrias, funciones de negocio, geografías)
- Proyectos activos y rol en cada uno
- Metodologías y frameworks preferidos
- Formato de trabajo preferido (más o menos estructura en los outputs)

**Contexto de proyecto (memoria episódica con TTL por proyecto):**
- Nombre del cliente y sector
- Objetivo central del proyecto y entregables
- Hipótesis de trabajo actuales
- Restricciones y limitaciones conocidas (confidencialidad, acceso a datos, presupuesto)
- Decisiones tomadas en iteraciones anteriores

**Historial de sesión (memoria conversacional con ventana deslizante):**
- Los últimos 8 turnos de la conversación actual
- Resumen comprimido de los turnos anteriores de la misma sesión

La decisión explícita fue no guardar: el contenido de los documentos del cliente (por confidencialidad), las consultas de exploración sin conclusión, y cualquier información que el consultor no hubiera validado (para evitar guardar inferencias incorrectas).

## La arquitectura implementada

El equipo eligió una arquitectura de doble backend:

- **Redis** para los perfiles de consultor (acceso por ID, baja latencia requerida).
- **Qdrant** (self-hosted, por requerimiento de privacidad) para las memorias de proyecto y las memorias episódicas, con recuperación semántica.

La capa de aplicación implementó los patrones de Memory Store, Context Assembler y Memory Extractor de las secciones anteriores.

```
FLUJO POR SESIÓN:

1. Usuario inicia sesión → se carga perfil del consultor desde Redis
2. Usuario selecciona proyecto activo → se recuperan memorias del proyecto desde Qdrant
3. Context Assembler construye el bloque de contexto:
   [perfil del consultor] + [memorias del proyecto relevantes] + [historial de sesión]
4. Durante la sesión: ventana deslizante + resumen progresivo
5. Al cerrar sesión: Memory Extractor identifica hechos memorables
6. Upsert semántico: los hechos nuevos se integran sin crear duplicados
```

El bloque de contexto de memoria tenía un límite de 1.200 tokens —un compromiso entre cobertura y costo.

## Los problemas que surgieron en producción

### Problema 1: El consultor se va del proyecto pero la memoria no

A los dos meses del despliegue, un consultor que había rotado fuera del proyecto Antares recibía memorias del proyecto Antares en sus sesiones de un proyecto completamente distinto. El Qdrant devolvía memorias del proyecto anterior porque tenían alta similitud semántica con las consultas nuevas (ambos proyectos eran del sector retail).

**Solución:** añadir un filtro de `proyecto_activo` en la recuperación. Las memorias de proyecto solo se recuperan cuando el proyecto está marcado como activo para ese consultor. Al cerrar un proyecto, sus memorias se archivan (se marca el campo `activo: false`) y quedan fuera de los resultados de recuperación estándar.

### Problema 2: El resumen de sesión perdía detalles críticos

El resumen progresivo de sesiones largas perdía a veces restricciones importantes que el consultor había mencionado temprano en la sesión ("no podemos proponer soluciones que impliquen cambios en el ERP"). El prompt de resumen no las priorizaba adecuadamente.

**Solución:** modificar el prompt de resumen para que identifique y preserve explícitamente las restricciones y los acuerdos antes de comprimir el contenido narrativo. Se añadió un bloque dedicado de `restricciones_de_sesión` en el contexto, con alta prioridad de preservación.

### Problema 3: Un consultor rechazó la memoria, generando un incidente de privacidad

Un consultor senior descubrió que el sistema había inferido y guardado como "preferencia" algo que él consideraba una hipótesis de trabajo, no una decisión permanente. Solicitó saber exactamente qué tenía el sistema guardado sobre él y quería eliminarlo todo.

**Solución:** el equipo implementó en una semana un endpoint de API que devolvía todos los registros de memoria asociados a un `user_id`. Dentro del chat, el comando `/mi-memoria` listaba todas las memorias del perfil. El comando `/olvidar [texto]` permitía eliminar registros específicos. La eliminación completa de un usuario fue probada y documentada como procedimiento.

Este incidente llevó al equipo a revisar el criterio de captura de memorias inferidas: solo se guardan con el tipo `inferida` y con un score de confianza `media`, diferenciado de los hechos `explicitos` que el consultor expresó directamente.

## Resultados a los seis meses

Después de seis meses de operación con la arquitectura de memoria:

- El 78% de los consultores reportó que el sistema "los conoce" y produce respuestas más relevantes que en el piloto inicial.
- El promedio de turnos por sesión para llegar a un output útil bajó de 6,2 a 3,8, atribuido a la reducción de contexto explicativo que el consultor necesita dar al inicio de cada sesión.
- El equipo de tecnología identificó que el 23% de las memorias capturadas era ruido (información sin valor para sesiones futuras). La revisión del criterio de extracción mejoró este indicador.
- El primer incidente de privacidad resultó en la implementación de controles que el equipo reconoció como necesarios desde el inicio pero que habían postergado.

## Lecciones del caso

**La memoria no es un feature, es una promesa.** Cuando el sistema empieza a recordar a un usuario, ese usuario desarrolla expectativas de continuidad. Si esas expectativas se rompen —porque la memoria falla, porque guarda mal, porque no actualiza— la confianza se degrada más rápido que si el sistema nunca hubiera tenido memoria.

**La privacidad del usuario es un requisito de diseño, no un requisito de cumplimiento.** El equipo lo aprendió por un incidente. Un diseño proactivo habría evitado el incidente.

**Los bugs de memoria son difíciles de diagnosticar.** Cuando el sistema produce una respuesta subóptima por culpa de una memoria incorrecta, el usuario generalmente no lo sabe: atribuye el error al modelo, no a la memoria. Esto hace que los bugs de memoria sean silenciosos y su impacto, subestimado.

---

*La siguiente sección es el laboratorio práctico: el estudiante implementa un sistema de memoria persistente simple —basado en JSON—, con criterios explícitos de captura, recuperación y eliminación.*
