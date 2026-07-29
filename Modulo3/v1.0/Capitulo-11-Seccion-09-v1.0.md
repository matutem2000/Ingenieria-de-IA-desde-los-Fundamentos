# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 09: Patrones y anti-patrones

Las secciones anteriores describieron cómo construir buen contexto en cada fase del ciclo de vida. Esta sección cataloga los patrones que funcionan de manera consistente y los anti-patrones que generan problemas recurrentes. Estos patrones emergieron de la experiencia práctica de equipos que implementaron Context Engineering en proyectos reales.

### Anti-patrones: los errores más costosos

**Anti-patrón 1: El Contexto Vacío**

El anti-patrón más frecuente y más costoso. El desarrollador formula la petición al modelo sin ningún contexto adicional del proyecto: "Escribe una función que valide un email", "Crea un endpoint REST para pedidos", "Refactoriza esta función". El modelo genera una respuesta genérica que no corresponde al proyecto específico.

El costo no es solo el tiempo de la refactorización posterior. Es la cultura que ese anti-patrón crea: si el equipo experimenta repetidamente que el código generado no sirve, concluye que la IA no es útil para su proyecto. La IA no tenía contexto — no era inútil, era ciega.

Corrección: establecer un archivo de instrucciones del proyecto (`.claude/project.md` o equivalente) que sea incluido automáticamente en cada sesión, y entrenar al equipo en la práctica de proporcionar el módulo y las clases relacionadas antes de cada petición de generación.

**Anti-patrón 2: El Copy-Paste Sin Revisión**

El desarrollador recibe el código generado por el modelo y lo pega directamente al codebase sin revisión. El código compila. Los tests pasan. Se mergea.

Este anti-patrón es especialmente peligroso porque la mayor parte del tiempo funciona — lo cual genera falsa confianza. Los problemas aparecen en los casos que los tests no cubren: el código generado asume condiciones que no están garantizadas en el sistema real, viola un invariante de seguridad que estaba documentado en una issue que el modelo no vio, o introduce una dependencia de terceros con una licencia incompatible con el proyecto.

La corrección no es no usar IA — es establecer una cultura de revisión crítica. El código generado por IA debe pasar el mismo escrutinio que el código generado por un desarrollador junior: revisado por un desarrollador con conocimiento del sistema antes de que llegue a main.

**Anti-patrón 3: El Contexto Monolítico**

El desarrollador intenta resolver este problema yendo al extremo opuesto: incluye todo el repositorio en el contexto de cada petición. Esto degrada la calidad del razonamiento del modelo (la ventana de contexto tiene límites efectivos de atención, no solo de tokens), hace las peticiones lentas y costosas, y mezcla contexto relevante con irrelevante.

El modelo, cuando se le da demasiado contexto irrelevante, tiende a anclar en los primeros elementos del contexto y a dar menos atención a los elementos que aparecen en el medio. Un contexto grande y desorganizado es peor que un contexto selectivo y bien estructurado.

Corrección: contexto selectivo y relevante para la tarea específica. El arte del Context Engineering es elegir qué incluir y qué excluir, no incluir todo.

**Anti-patrón 4: La Revisión de IA Como Etapa Final**

El equipo configura una revisión automática de IA como el último paso del pipeline antes del merge. Si la IA aprueba, el PR se mergea sin revisión humana adicional.

Este anti-patrón invierte el rol correcto del modelo. La IA debe ser una capa de asistencia para el revisor humano, no un árbitro final. El modelo puede tener falsos negativos — aprobar código con problemas que el contexto disponible no le permitió identificar — y esos falsos negativos llegan a producción sin revisión.

Corrección: la revisión de IA es un paso de asistencia que produce findings para el revisor humano. La aprobación final siempre requiere un humano con conocimiento del sistema.

**Anti-patrón 5: El Contexto Desactualizado**

El equipo crea un archivo de instrucciones del proyecto y no lo actualiza. El proyecto migra a Python 3.12, adopta un nuevo framework de tests, cambia las convenciones de naming — pero el archivo de contexto sigue describiendo el estado del proyecto de hace seis meses. El modelo genera código con las convenciones viejas, que el equipo debe corregir manualmente.

Corrección: el archivo de instrucciones del proyecto se trata como documentación viva. Se incluye en el proceso de onboarding de nuevas decisiones técnicas: cuando el equipo adopta una nueva convención, la documenta en el archivo de contexto del proyecto.

### Patrones que funcionan

**Patrón 1: El Archivo de Contexto del Proyecto**

Un archivo mantenido en el repositorio (`.claude/project.md`, `CONTEXT.md`, `.cursorrules` o el equivalente de la herramienta) que documenta:

- Stack tecnológico con versiones
- Convenciones de código
- Patrones de diseño adoptados
- Instrucciones específicas para el asistente

Este archivo se incluye automáticamente en cada sesión de trabajo. Su mantenimiento es responsabilidad del equipo, igual que el CHANGELOG o el README.

**Patrón 2: El Contexto Mínimo Suficiente**

Para cada tarea, el desarrollador identifica los elementos de contexto sin los cuales el modelo no puede producir un output útil:

- Para generación de código: el módulo destino, las clases del dominio a usar, los tests que debe pasar
- Para debugging: el stack trace, el código de las funciones implicadas, los cambios recientes
- Para revisión de PR: el diff, el requisito que motivó el cambio, las guías de estilo

Nada menos que eso (degradaría la calidad), nada más que eso (desperdiciaría la ventana de contexto).

**Patrón 3: Verificación Antes de Integración**

El output del modelo siempre pasa por verificación antes de integrarse:

- Código generado: linter → tests unitarios → revisión humana
- Diagnóstico de bug: reproducción local antes de aplicar el fix
- Revisión de PR: evaluación humana de los findings antes de comentar

La IA acelera el trabajo; la verificación asegura la calidad.

**Patrón 4: El Contexto Escalonado**

Para tareas complejas que requieren múltiples pasos de razonamiento, el contexto se construye de manera escalonada. En lugar de dar todo el contexto de una vez y pedir el resultado final, el desarrollador trabaja en pasos:

1. "Dado este stack trace y este código, ¿qué hipótesis de causa raíz son plausibles?"
2. El desarrollador evalúa las hipótesis y selecciona la más probable.
3. "Dada esta hipótesis de causa raíz, ¿qué fix propondrías?"
4. El desarrollador evalúa el fix propuesto, lo verifica localmente.
5. "Escribe el test que habría detectado este bug antes del deployment."

Cada paso usa el output del paso anterior como contexto adicional, construyendo el razonamiento de manera incremental.

**Patrón 5: La Revisión Bidireccional**

El desarrollador usa el modelo para revisar su propio trabajo antes de enviarlo a revisión del equipo. Proporciona su código + las guías del proyecto y pide una revisión crítica. Esto captura problemas obvios antes de la revisión de pares, haciendo esa revisión más eficiente.

La revisión bidireccional también tiene un efecto secundario positivo: el desarrollador aprende de los problemas que el modelo señala, lo que mejora su calidad de código a lo largo del tiempo.

```
TAXONOMÍA DE PATRONES Y ANTI-PATRONES

ANTI-PATRONES:
  1. Contexto vacío          → Output genérico, no útil para el proyecto
  2. Copy-paste sin revisión → Riesgo de bugs y violaciones de política
  3. Contexto monolítico     → Degradación del razonamiento, costo innecesario
  4. IA como árbitro final   → Falsos negativos sin contrapeso humano
  5. Contexto desactualizado → Output con convenciones obsoletas

PATRONES:
  1. Archivo de contexto del proyecto → Contexto base consistente en cada sesión
  2. Contexto mínimo suficiente       → Calidad máxima con costo mínimo
  3. Verificación antes de integrar   → Calidad asegurada por proceso
  4. Contexto escalonado              → Razonamiento incremental de calidad
  5. Revisión bidireccional           → Mejora antes del proceso formal de revisión
```

### Señales de que el Context Engineering está funcionando

Los equipos que implementan Context Engineering efectivamente observan las siguientes señales:

- El código generado requiere ajustes mínimos antes de ser integrable
- Los desarrolladores junior producen código que sigue las convenciones del proyecto desde el primer intento
- El tiempo de debugging de bugs reportados en producción se reduce
- Los comentarios en PRs generados por IA son específicos y accionables, no genéricos
- Los desarrolladores confían en usar el asistente de IA para tareas complejas, no solo para completar código trivial

### Señales de que el Context Engineering está fallando

- El código generado se descarta frecuentemente o requiere reescritura significativa
- El equipo percibe que la IA "no sirve para nuestro proyecto"
- Los comentarios de revisión de IA son genéricos ("considera agregar manejo de errores") sin especificidad del proyecto
- Los bugs introducidos por código generado sin revisión llegan a producción
- El equipo tiene reglas informales como "nunca uses IA para el módulo X" por malas experiencias previas

Estas señales de fallo son casi siempre síntomas de un problema de contexto, no de un problema del modelo.

### Nota del arquitecto

La lista de anti-patrones anterior no es exhaustiva, y el orden de impacto varía según el equipo. Pero el anti-patrón 2 (Copy-Paste Sin Revisión) merece énfasis especial porque es el que tiene consecuencias más difíciles de revertir: código con bugs en producción, vulnerabilidades de seguridad introducidas sin intención y deuda técnica acumulada sin visibilidad. La cultura de revisión crítica del código asistido por IA es la base sobre la que todo lo demás funciona.

La siguiente sección materializa estos patrones en un contexto concreto: un caso de estudio empresarial que muestra cómo un equipo real implementó Context Engineering en su ciclo de desarrollo.
