# Capítulo 15 — Proyecto Integrador

## Sección 09: Buenas prácticas y errores frecuentes en sistemas integrados

Los capítulos anteriores del módulo documentaron las buenas prácticas y anti-patrones de cada componente por separado: cómo estructurar instrucciones del sistema, cómo gestionar la ventana de contexto, cómo diseñar el pipeline RAG, cómo implementar herramientas seguras, cómo controlar agentes. No tiene sentido repetir esos catálogos aquí.

Esta sección se ocupa de algo diferente: los errores que solo se manifiestan cuando todos los componentes operan juntos. Son errores de integración, no de componente. Aparecen en producción, no en pruebas unitarias. Y son, por esa razón, los más costosos de detectar y corregir.

### Error de integración 1: Conflicto entre memoria persistente e instrucciones del sistema

**Descripción:** El módulo de memoria persistente almacena preferencias del usuario. La instrucción del sistema del departamento establece el comportamiento esperado del asistente. Cuando ambas están en conflicto, el sistema puede comportarse de manera impredecible.

**Ejemplo concreto:** Un empleado de Legal establece en su perfil de memoria: "Responde siempre en inglés." La instrucción del sistema del departamento Legal dice: "Usa terminología jurídica en español." En una sesión, el LLM recibe ambas instrucciones en el contexto. El comportamiento resultante depende del orden en que aparecen las instrucciones y de cómo el LLM resuelve las contradicciones. Ese comportamiento no es predecible ni estable.

**Solución:** Establecer una jerarquía explícita de precedencia en el contexto: las instrucciones del sistema del departamento siempre prevalecen sobre las preferencias del usuario para los aspectos que afectan cumplimiento, seguridad o estilo institucional. Las preferencias del usuario prevalecen en aspectos de formato y conveniencia personal. La instrucción del sistema debe enunciar esta jerarquía explícitamente:

```
Las preferencias de formato del usuario (longitud de respuesta, uso de 
listas) son bienvenidas. Sin embargo, el idioma de las respuestas y la 
terminología legal son estándares del departamento y no se modifican 
por preferencias individuales.
```

**Buena práctica:** Definir antes del diseño qué aspectos del comportamiento son configurables por el usuario y cuáles son fijos por la institución. Documentar esa decisión en la instrucción del sistema.

---

### Error de integración 2: Latencia acumulativa no anticipada

**Descripción:** Cada componente del pipeline tiene una latencia propia. En pruebas aisladas, cada componente es aceptablemente rápido. Pero la latencia total del sistema es la suma de todas las latencias, y esa suma puede exceder los objetivos cuando los componentes operan bajo carga real.

**Ejemplo concreto:** El módulo de memoria tarda 80 ms en recuperar el perfil del usuario. El motor RAG tarda 450 ms en procesar la consulta y devolver fragmentos. El LLM tarda 3.200 ms en generar la respuesta. El filtrado de salida tarda 120 ms. La latencia total es 3.850 ms: dentro del objetivo de 6 segundos. Pero si el motor RAG tiene un día con alta carga y tarda 1.800 ms, la latencia total sube a 5.200 ms, todavía dentro del objetivo. Y si además el LLM experimenta latencia alta de 5.500 ms, la latencia total llega a 7.500 ms, superando el umbral de alerta.

La latencia del peor caso de cada componente no es la suma de los promedios; es la suma de los percentiles 95 o 99 de cada uno. Ese cálculo generalmente revela que el sistema tiene margen mucho menor del que parece.

**Solución:** Presupuestar la latencia por componente con percentiles P95, no con promedios. El presupuesto total de latencia (por ejemplo, 8 segundos) se distribuye entre componentes con límites explícitos. Si un componente excede su límite de latencia, el orquestador debe tomar una decisión: degradar ese componente (servir sin memoria, sin RAG, con menos fragmentos) o devolver un error parcial al usuario.

**Buena práctica:** Implementar circuit breakers en cada componente. Si el módulo RAG supera 1 segundo de latencia tres veces consecutivas en un período, el orquestador sirve sin RAG y registra el degradado. El usuario recibe una respuesta basada solo en la instrucción del sistema y la memoria, con una nota: "No pude acceder a la documentación interna en este momento."

---

### Error de integración 3: Fragmentos RAG contaminando el razonamiento del agente

**Descripción:** El agente de análisis de incidentes usa RAG para recuperar runbooks relevantes. El pipeline RAG puede recuperar fragmentos de documentos de diferentes versiones del mismo runbook si el índice no está correctamente actualizado. El agente recibe fragmentos contradictorios y produce un diagnóstico incoherente.

**Ejemplo concreto:** El runbook de escalación fue actualizado en mayo de 2026: el nuevo umbral para escalar a P1 es de 45 minutos (antes era 60). Si el índice vectorial contiene fragmentos tanto de la versión anterior como de la nueva (porque la eliminación de fragmentos de la versión anterior no funcionó correctamente), el agente puede recuperar ambos fragmentos y generar una recomendación ambigua.

**Solución:** El proceso de actualización de la base documental (descrito en la sección 08) debe incluir una verificación post-actualización: consultar el índice para el documento recién actualizado y verificar que solo existen fragmentos de la nueva versión. Esa verificación puede automatizarse como parte del pipeline de ingestión.

**Buena práctica:** Incluir el número de versión y la fecha del documento en cada fragmento, y en la instrucción del agente indicar explícitamente que ante fragmentos contradictorios del mismo documento, debe usar el más reciente y reportar la inconsistencia.

---

### Error de integración 4: Contexto de memoria que invalida el control de acceso

**Descripción:** El módulo de memoria puede almacenar referencias a información que el usuario obtuvo en una sesión anterior con acceso a documentos que ya no puede ver (porque su nivel de autorización cambió, o porque el documento fue reclasificado). Al inicio de la nueva sesión, el orquestador inyecta esa memoria en el contexto, introduciendo información que el usuario ya no debería tener.

**Ejemplo concreto:** Un empleado de RRHH con nivel de autorización elevado consulta datos salariales de un directivo. El agente almacena en la memoria: "El usuario revisó el contrato de X en la sesión anterior." Tres días después, ese empleado es degradado a nivel de autorización estándar. En la siguiente sesión, la memoria inyectada en el contexto menciona el contrato de X, que el usuario ya no tiene permiso de ver.

**Solución:** El módulo de memoria no debe almacenar referencias a documentos confidenciales, solo referencias a documentos de clasificación `público_interno`. Las entradas de memoria que incluyen referencias a documentos deben pasar por el mismo filtro de control de acceso que el motor RAG, aplicado en el momento de recuperación (no en el momento de almacenamiento), usando el perfil de autorización actual del usuario.

**Buena práctica:** Al construir el contexto de memoria, aplicar el filtro de control de acceso sobre cada entrada antes de incluirla en el contexto. Si una entrada de memoria ya no es accesible para el usuario con su nivel de autorización actual, se omite silenciosamente.

---

### Error de integración 5: El agente entra en bucle por herramienta que siempre falla

**Descripción:** El agente de incidentes usa herramientas en su ciclo ReAct. Si una herramienta devuelve siempre un error (por ejemplo, el sistema de tickets está en mantenimiento), el agente puede reintentar la llamada a la herramienta en cada iteración hasta agotar el límite de iteraciones, consumiendo tokens y tiempo sin producir valor.

**Ejemplo concreto:** El agente intenta verificar_solicitud(#4521) en la iteración 1. El sistema de tickets devuelve un error 503. El agente razona que necesita esa información y vuelve a intentar verificar_solicitud(#4521) en la iteración 2. Error 503. El agente vuelve a intentar. Ocho iteraciones, ocho errores, ningún progreso.

**Solución:** El módulo de herramientas implementa un registro de fallos por herramienta dentro del ciclo del agente. Si una herramienta falla dos veces consecutivas, el orquestador la marca como no disponible para el resto del ciclo y provee al agente un mensaje explícito: "La herramienta verificar_solicitud no está disponible. Continúa sin esa información o indica que no puedes completar el análisis."

**Buena práctica:** Toda herramienta expuesta a un agente debe tener un mecanismo de degradación explícita. El agente debe ser capaz de producir un resultado parcial útil cuando una herramienta no está disponible, en lugar de fallar completamente.

---

### La tabla de errores de integración

| Error de integración          | Componentes involucrados           | Señal de detección           | Mitigación                              |
|-------------------------------|------------------------------------|------------------------------|-----------------------------------------|
| Conflicto memoria-instrucciones | Memoria + instrucción del sistema | Comportamiento inconsistente | Jerarquía de precedencia explícita      |
| Latencia acumulativa          | Todos los componentes del pipeline | P95 latencia > umbral        | Circuit breakers + degradación          |
| Fragmentos RAG contradictorios| RAG + agente                       | Diagnóstico ambiguo          | Verificación post-actualización         |
| Memoria con acceso inválido   | Memoria + control de acceso        | Información no autorizada    | Filtro de acceso en recuperación        |
| Bucle en herramienta fallida  | Agente + herramientas              | Iteraciones sin progreso     | Registro de fallos + herramienta desactivada |

La revisión de esta tabla debe formar parte del proceso de revisión técnica de cualquier sistema de IA que integre los cinco componentes involucrados.

---

Con los errores de integración identificados, la siguiente sección presenta el caso completo de implementación de TechCore como referencia consolidada.
