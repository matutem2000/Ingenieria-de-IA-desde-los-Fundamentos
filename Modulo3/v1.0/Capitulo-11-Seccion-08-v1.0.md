# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 08: Integración con IDEs, repositorios y CI/CD

El Context Engineering no opera en el vacío. Opera dentro del ecosistema de herramientas que los equipos de desarrollo ya usan: IDEs, sistemas de control de versiones, plataformas de CI/CD. Esta sección analiza cómo ese ecosistema determina qué contexto está disponible, cómo se recupera y cómo se entrega al modelo.

El enfoque es deliberadamente agnóstico de herramientas. Las plataformas específicas — GitHub vs. GitLab, GitHub Actions vs. Jenkins, VSCode vs. Cursor — evolucionan rápidamente. Los principios de cómo estructurar el contexto en cada capa del ecosistema permanecen estables.

### El IDE como interfaz de contexto

El IDE es el punto de contacto más inmediato entre el desarrollador y el modelo. Las herramientas modernas de asistencia de código (Cursor, GitHub Copilot, Codeium, y similares) operan directamente dentro del IDE y tienen acceso a contexto que otras interfaces no tienen de forma natural.

**Contexto disponible en el IDE:**
- El archivo actualmente abierto
- Los archivos abiertos en pestañas activas
- El cursor y la selección actual (qué código está mirando el desarrollador)
- El proyecto completo (con limitaciones de tamaño)
- La definición de funciones y tipos accesibles vía Language Server Protocol (LSP)

**Lo que el AI Engineer puede configurar:**

El contexto disponible en el IDE puede expandirse mediante archivos de instrucciones del proyecto. Herramientas como Cursor permiten definir archivos `.cursorrules` o `.claude/project.md` que se incluyen automáticamente en el contexto de cada sesión. Estos archivos documentan:

- Las convenciones de código del proyecto
- Los patrones de diseño adoptados
- Las instrucciones específicas para el asistente ("siempre usar Decimal para valores monetarios", "nunca usar print para debugging, usar el logger del proyecto")
- Las restricciones de seguridad ("no incluir credenciales en el código")

Este archivo de instrucciones de proyecto es una de las inversiones de mayor retorno en Context Engineering para IDEs: se escribe una vez y mejora cada sesión de desarrollo en el proyecto.

```
EJEMPLO: .claude/project.md para un proyecto de e-commerce

# Proyecto: E-Commerce Platform Backend

## Stack
- Python 3.11, FastAPI, SQLAlchemy 2.0
- PostgreSQL (producción), SQLite (tests)
- Kafka para mensajería asincrónica
- structlog para logging

## Convenciones de código
- Type hints obligatorios en todas las funciones
- Docstrings en formato Google Style
- Decimal para todos los valores monetarios, nunca float
- Manejo de errores con excepciones custom en each domain

## Patrones de diseño
- Repository pattern para acceso a datos
- Event-driven para comunicación entre dominios
- CQRS para módulos con alta frecuencia de lectura

## Instrucciones para el asistente
- Al generar código de un servicio, verificar que usa el logger del proyecto
- Al generar tests, usar factory_boy para fixtures
- No usar print() para debugging
- Verificar que los imports corresponden a dependencias del pyproject.toml
```

### El repositorio como fuente de contexto estructurado

El repositorio de código es la fuente de contexto más rica disponible para el AI Engineer. Contiene no solo el código actual, sino la historia completa de decisiones técnicas.

Los artefactos del repositorio que son fuentes de contexto de alta calidad:

**git log con mensajes de commit descriptivos.** Los commits con mensajes de la forma "feat(orders): add minimum amount validation for discount rules" son mucho más útiles que "fix stuff". El mensaje de commit es el contexto del por qué del cambio, que el modelo necesita para razonar sobre el impacto de modificaciones.

**Pull requests con comentarios de revisión.** Los comentarios en PRs históricos documentan el razonamiento técnico del equipo: por qué una solución fue rechazada, qué trade-offs se evaluaron, qué preocupaciones de seguridad o performance fueron identificadas.

**Issues y sus estados.** Las issues cerradas documentan qué problemas existieron y cómo se resolvieron. Las issues abiertas documentan el trabajo pendiente y los problemas conocidos.

**Archivos de configuración.** `pyproject.toml`, `package.json`, `.eslintrc`, `Makefile` — documentan las dependencias, las herramientas de calidad adoptadas y los comandos estándar del proyecto.

El AI Engineer que diseña un sistema de asistencia debe considerar cuáles de estas fuentes se incluyen en el contexto de manera sistemática y cuáles se recuperan bajo demanda.

### El pipeline de CI/CD como contexto automatizado

El pipeline de CI/CD es el contexto más dinámico del ecosistema: cambia con cada commit, con cada deployment, con cada ejecución. Y es también el contexto donde la IA puede automatizar tareas de alta frecuencia con mayor impacto.

Los principios para integrar IA en pipelines de CI/CD, independientemente de la plataforma:

**Principio 1: El contexto del pipeline debe incluir siempre el diff.**

Cualquier tarea que el modelo ejecuta en el pipeline — revisión de código, análisis de seguridad, generación de documentación de release — requiere el diff del cambio que triggerea el pipeline. Sin el diff, el modelo no sabe qué cambió.

**Principio 2: El contexto del pipeline debe incluir los resultados de pasos anteriores.**

Si el pipeline incluye tests unitarios, análisis estático y revisión de código en ese orden, la revisión de código tiene acceso al output de los tests y del análisis estático. Ese output es contexto: informa al modelo sobre problemas ya detectados antes de que realice su propia revisión.

**Principio 3: El contexto del pipeline debe respetar las políticas del equipo.**

Las políticas de merge del equipo — qué condiciones deben cumplirse para que un PR sea elegible para merge — son contexto que el modelo necesita para evaluar si un cambio cumple los estándares del proyecto. Si la política dice que todo código nuevo debe tener cobertura de tests mayor al 80%, el modelo debe tener acceso a ese requisito para verificar si el PR lo cumple.

```
ESTRUCTURA DE CONTEXTO EN UN PIPELINE DE CI/CD

[EVENTO]: Pull Request abierto - rama: feat/add-fixed-discount
[DIFF]: [contenido del git diff]
[METADATOS]: Autor, rama base, número de commits, archivos modificados

[PASO 1: Tests automáticos]
  Output: ✓ 247 tests pasaron, 0 fallaron
  Coverage: 84% (umbral: 80%) → PASA

[PASO 2: Análisis estático]
  Output: 2 warnings de tipo - function without return type hint
  0 errores críticos → CONTINÚA CON WARNINGS

[PASO 3: Revisión asistida por IA]
  Contexto disponible:
    - Diff completo
    - Output de tests (paso 1)
    - Warnings de tipo (paso 2)
    - Guías de estilo del proyecto
    - Políticas de merge
  
  Tarea: Revisar el PR y comentar sobre:
    1. Los warnings de tipo (¿son intencionales o errores?)
    2. Casos borde no cubiertos por los nuevos tests
    3. Consistencia con las guías del proyecto
```

### Recuperación de contexto del repositorio en tiempo real

Para sistemas de asistencia más sofisticados, el contexto del repositorio se recupera de manera dinámica según la tarea específica. Esto requiere un sistema de indexación del repositorio.

Los elementos que se indexan:
- Código fuente (chunkeado por función o clase)
- Documentación y comentarios
- Mensajes de commit
- ADRs y documentación de arquitectura

La recuperación se realiza mediante similitud semántica (embeddings) o mediante búsqueda léxica (grep avanzado). Cuando el desarrollador formula una tarea, el sistema recupera los fragmentos más relevantes del repositorio y los incluye en el contexto del modelo.

Este enfoque resuelve el problema de repositorios grandes: en lugar de intentar meter todo el codebase en la ventana de contexto (imposible), el sistema recupera selectivamente el contexto más relevante para la tarea específica.

### Integración con herramientas de observabilidad

En la fase de mantenimiento y operaciones, las herramientas de observabilidad (sistemas de logging centralizado, métricas, trazas distribuidas) son fuentes de contexto que complementan al repositorio.

El AI Engineer puede diseñar integraciones que, dado un alert de producción, recuperan automáticamente:
- Los logs del servicio en el rango de tiempo del alert
- El stack trace completo del error
- El código del módulo afectado (del repositorio)
- Los commits recientes en ese módulo

Este ensamblaje automático del contexto de diagnóstico — integrando observabilidad y repositorio — reduce el tiempo de respuesta ante incidentes de producción de manera significativa.

### Nota del arquitecto

La tentación al diseñar integraciones de IA en el pipeline de CI/CD es hacer la revisión del modelo bloqueante: el pipeline no avanza hasta que el modelo da su aprobación. Esto es un error de diseño. El modelo puede tener falsos positivos que bloqueen merges legítimos, y puede tener falsos negativos que aprueben código problemático.

El rol correcto de la revisión asistida por IA en el pipeline es de asistencia al humano, no de árbitro automático. El modelo señala problemas; el desarrollador evalúa y decide. El pipeline puede informar sobre los findings del modelo, puede generar comentarios automáticos en el PR, pero la decisión de merge sigue siendo humana.

La siguiente sección sintetiza lo que el capítulo enseña sobre errores frecuentes y patrones de éxito: los anti-patrones que deben evitarse y los patrones que funcionan en producción.
