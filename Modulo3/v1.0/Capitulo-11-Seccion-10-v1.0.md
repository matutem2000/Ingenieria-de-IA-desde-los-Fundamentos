# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 10: Caso de estudio empresarial

Esta sección reconstruye la implementación de Context Engineering en un equipo de desarrollo de software de tamaño mediano. El caso es representativo de equipos que han madurado su uso de IA desde herramientas de completado de código hacia sistemas de asistencia integrados en el ciclo de vida completo.

Los nombres del equipo y la organización son ficticios. Los problemas, las decisiones y los resultados son representativos de implementaciones reales.

### El contexto inicial: el equipo y sus problemas

El equipo desarrolla el backend de una plataforma de marketplace B2B. Son 12 desarrolladores, organizados en tres squads: Catálogo, Pedidos y Facturación. El stack es Python (FastAPI, SQLAlchemy), PostgreSQL y Kafka. El repositorio tiene aproximadamente 180.000 líneas de código Python.

Antes de la implementación, el equipo ya usaba herramientas de IA de manera informal:
- Varios desarrolladores usaban GitHub Copilot para completado de código
- Algunos usaban Claude o GPT-4 en ventanas separadas para debugging
- El uso era individual e inconsistente: sin convenciones de equipo, sin métricas, sin proceso definido

Los problemas que motivaron una implementación más estructurada:

**Inconsistencia del output.** El código generado por IA tenía calidad muy variable. Algunos desarrolladores obtenían sugerencias excelentes; otros reportaban que el completado generaba código inutilizable. La diferencia no estaba documentada — cada desarrollador tenía su propia intuición sobre "cómo hablar con la IA".

**Revisiones de código más lentas.** Los PRs con código asistido por IA frecuentemente incluían violaciones de convenciones del proyecto que alargaban las revisiones. El code style del proyecto no estaba disponible para el modelo.

**Falsa confianza en el debugging.** Varios incidentes de producción se investigaron con IA y el diagnóstico inicial fue incorrecto. Los desarrolladores habían proporcionado solo el stack trace, sin el contexto del código ni los cambios recientes.

### La intervención: qué se diseñó

El AI Engineer del equipo diseñó una intervención en tres niveles: contexto base del proyecto, flujos de trabajo estandarizados y un sistema de recuperación de contexto del repositorio.

**Nivel 1: Contexto base del proyecto**

Se creó un archivo `CONTEXT.md` en la raíz del repositorio con las convenciones del equipo, el stack tecnológico, los patrones de diseño adoptados y las instrucciones específicas para el asistente de IA. Este archivo se configuró para ser incluido automáticamente en Cursor (el IDE adoptado como estándar del equipo).

Sección de muestra del archivo:

```markdown
# Backend Platform — Contexto para Asistente IA

## Stack
Python 3.11, FastAPI 0.111, SQLAlchemy 2.0, Alembic, Kafka (confluent-kafka)
PostgreSQL 15 (producción), pytest + SQLite en memoria (tests)

## Convenciones obligatorias
- Decimal para todos los valores monetarios (nunca float)
- structlog para logging (nunca print ni logging stdlib directamente)
- Excepciones custom por dominio: orders/exceptions.py, catalog/exceptions.py
- Type hints obligatorios; Mypy en modo strict
- Tests con factory_boy para fixtures, no con fixtures hardcodeadas

## Patrones del proyecto
- Repository pattern: acceso a base de datos solo a través de repositorios
- Eventos de dominio: cambios de estado se publican a Kafka, nunca se llama
  a otros dominios directamente
- DTOs para entrada/salida de endpoints; modelos SQLAlchemy no se exponen
  directamente en las responses

## Instrucciones para el asistente
- Antes de generar código, verificar que usa las excepciones del dominio
  correcto, no excepciones genéricas de Python
- Los tests de integración usan una base de datos SQLite en memoria;
  no generar tests que requieran conexión a PostgreSQL real
- Todo código nuevo debe tener docstring en formato Google Style
```

**Nivel 2: Flujos de trabajo estandarizados**

El equipo documentó cuatro flujos de trabajo estándar para los casos de uso más frecuentes:

*Flujo de generación de código:* el desarrollador abre el módulo destino en Cursor, selecciona las clases relacionadas que usará, describe la función a generar, ejecuta los tests generados.

*Flujo de debugging:* el desarrollador ejecuta un script `debug-context.sh` que recibe el error de los logs y genera automáticamente un archivo de contexto con el stack trace, el código de las funciones implicadas, el diff de los últimos 5 commits de esos archivos y los tests que fallan. Ese archivo de contexto se usa como input para el modelo.

*Flujo de revisión de PR:* el CI/CD ejecuta automáticamente una revisión asistida en cada PR, con el diff, el contexto de las funciones afectadas y las guías del proyecto. Los findings aparecen como comentarios del bot en el PR, para evaluación del revisor humano.

*Flujo de generación de tests:* el desarrollador proporciona la función a testear + su especificación funcional, y pide la generación de tests. Los tests generados se revisan antes de incluirlos en el PR.

**Nivel 3: Sistema de recuperación de contexto del repositorio**

Para las tareas más complejas que requieren contexto de múltiples partes del repositorio, el equipo implementó un sistema simple de indexación: un script semanal que genera embeddings de las funciones del repositorio usando sentence-transformers y los almacena en un índice vectorial local (Chroma). Cuando un desarrollador trabaja en una tarea compleja, puede ejecutar `context-retrieval.py "descripción de la tarea"` y el script recupera las 10 funciones más semánticamente similares del repositorio como contexto adicional.

Este sistema no requirió infraestructura en la nube: corre localmente en la máquina del desarrollador y se actualiza semanalmente con el contenido del repositorio.

### Los resultados: qué cambió

El equipo midió cuatro métricas antes y después de la implementación, durante un período de tres meses:

**Tasa de aceptación del código generado.** El porcentaje del código sugerido por IA que se acepta sin modificaciones significativas. Antes: 34%. Después: 61%. La mejora se atribuye principalmente al archivo de contexto del proyecto, que evita las violaciones de convenciones más frecuentes.

**Tiempo promedio de revisión de PR.** El tiempo desde que se abre un PR hasta que recibe su primera revisión humana. Antes: 4.2 horas. Después: 2.8 horas. La revisión automática de IA identifica los problemas más obvios antes de que el revisor humano abra el PR, haciendo su revisión más focada.

**Tiempo de diagnóstico de incidentes.** El tiempo desde que se reporta un error de producción hasta que el equipo tiene una hipótesis de causa raíz. Antes: 47 minutos (promedio de 12 incidentes del período previo). Después: 18 minutos (promedio de 9 incidentes del período posterior). La reducción se atribuye principalmente al script `debug-context.sh` y al flujo estandarizado de debugging.

**Satisfacción del equipo con las herramientas de IA.** Survey interno. Antes: 3.1/5 ("útil para tareas simples"). Después: 4.2/5 ("útil para tareas complejas también"). El cambio más significativo fue en la percepción de los desarrolladores senior, que antes evitaban las herramientas de IA para tareas complejas.

### Las lecciones del caso

**La documentación del proyecto ya existía parcialmente.** El equipo tenía convenciones documentadas en un wiki que nadie leía. El paso más impactante fue hacer esa documentación accesible al modelo en el formato correcto (archivo en el repositorio, no en el wiki). El contenido ya existía; el problema era la accesibilidad.

**El cambio cultural tomó más tiempo que el técnico.** Implementar el archivo de contexto y el script de debugging tomó dos semanas. Lograr que todo el equipo lo usara de manera consistente tomó tres meses. La resistencia no era técnica — era de hábito. Los desarrolladores con años de uso individual de herramientas de IA tenían sus propias rutinas y les costaba adoptar el flujo estandarizado.

**Los flujos de trabajo fallaron antes de funcionar bien.** El primer intento del flujo de revisión de PR generó demasiados falsos positivos — el modelo señalaba como problemas estilos de código perfectamente válidos que no estaban documentados en el archivo de contexto. El equipo refinó el archivo de contexto durante dos semanas de feedback hasta que la tasa de falsos positivos bajó a un nivel aceptable.

**El tamaño del contexto importa.** El equipo probó inicialmente incluir el repositorio completo en el contexto de las revisiones de PR. La calidad de los findings cayó y el costo de las llamadas al modelo aumentó. La reducción al contexto mínimo suficiente (diff + funciones afectadas + guías del proyecto) mejoró ambas métricas.

### Nota del arquitecto

Este caso ilustra un patrón general de implementación: el valor de Context Engineering no está en la complejidad técnica de la solución — el archivo de contexto del proyecto es un archivo Markdown, el script de debugging es un script de shell — sino en la consistencia de su aplicación. El equipo que aplica principios simples de manera consistente obtiene mejores resultados que el equipo que implementa sistemas sofisticados de manera inconsistente.

La siguiente sección proporciona al lector la oportunidad de aplicar estos principios directamente: el laboratorio práctico del capítulo.
