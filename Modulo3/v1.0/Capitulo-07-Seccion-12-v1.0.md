# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 12 — Checklist del AI Engineer

Esta checklist consolida las decisiones de diseño, implementación y operación que determinan si un sistema con herramientas es robusto, seguro y mantenible. Está organizada en fases del ciclo de desarrollo. Cada elemento puede usarse como criterio de revisión antes de llevar un sistema a producción.

---

### Fase 1: Diseño de herramientas

**Definición y propósito**

- [ ] Cada herramienta tiene exactamente una responsabilidad. Ninguna herramienta combina múltiples operaciones en un parámetro de "acción".
- [ ] Las herramientas de consulta y las herramientas de acción están claramente separadas. No existen herramientas de consulta con efectos secundarios ocultos.
- [ ] Cada herramienta de acción tiene documentados sus efectos secundarios en la descripción.
- [ ] Las herramientas irreversibles están identificadas y marcadas como tales en la descripción.

**Descripciones**

- [ ] Cada descripción indica qué hace la herramienta, cuándo invocarla y qué devuelve.
- [ ] Las descripciones de herramientas similares incluyen una distinción explícita entre ellas.
- [ ] Ninguna descripción usa lenguaje tan genérico que aplique a casi cualquier situación.
- [ ] El formato de retorno está documentado en la descripción (campos, tipos, estructura).

**Esquemas de parámetros**

- [ ] Los tipos de cada parámetro son específicos (usar `date` en lugar de `string` cuando aplique, usar `enum` para valores predefinidos).
- [ ] Los parámetros opcionales tienen `default` definido.
- [ ] Los parámetros obligatorios están en el array `required`.
- [ ] Los valores de `enum` cubren todos los casos válidos, incluyendo un valor genérico cuando aplique ("todos", "otro").

---

### Fase 2: Implementación

**Contratos de respuesta**

- [ ] Cada herramienta devuelve un contrato de respuesta fijo con campos `exito`, `datos` (en caso de éxito) y `error` (en caso de fallo).
- [ ] Los errores incluyen: código de error, mensaje legible por el modelo, y una sugerencia accionable.
- [ ] Los errores no exponen detalles del stack técnico, nombres de variables internas ni estructuras de la base de datos.
- [ ] Los errores del sistema subyacente se registran en los logs del sistema pero se transforman en mensajes comprensibles antes de enviarse al modelo.

**Robustez**

- [ ] Todas las llamadas a sistemas externos tienen timeout explícito.
- [ ] Las herramientas de acción tienen mecanismo de idempotencia para manejar reintentos.
- [ ] El tamaño de las respuestas está limitado. Las herramientas de listado tienen paginación.
- [ ] Las herramientas validan los parámetros de entrada antes de ejecutar la operación subyacente.

**Loop de ejecución**

- [ ] El loop tiene un límite máximo de iteraciones configurado.
- [ ] El loop maneja el escenario en que `stop_reason` tiene un valor inesperado.
- [ ] Cuando se alcanza el límite de iteraciones, el sistema devuelve una respuesta de fallback al usuario en lugar de fallar silenciosamente.
- [ ] El loop puede ejecutar herramientas en paralelo cuando el modelo genera múltiples invocaciones en un mismo turno.

---

### Fase 3: Seguridad

**Control de acceso**

- [ ] El conjunto de herramientas disponibles se construye dinámicamente según el rol y los permisos del usuario autenticado.
- [ ] Los usuarios sin permisos de escritura no reciben herramientas de acción en el contexto.
- [ ] Las credenciales que usan las herramientas tienen los permisos mínimos necesarios (principio del mínimo privilegio).
- [ ] Las credenciales están almacenadas en un gestor de secretos, no en el código ni en variables de entorno sin gestión.

**Confirmación humana**

- [ ] Las herramientas de acción irreversible requieren confirmación explícita del usuario antes de ejecutarse.
- [ ] El mensaje de confirmación está en lenguaje del negocio, no en formato técnico.
- [ ] El sistema registra quién confirmó cada acción de alto impacto.

**Protección contra manipulación**

- [ ] El system prompt establece que el contenido obtenido de herramientas son datos externos, no instrucciones.
- [ ] Los resultados de herramientas que pueden contener texto no confiable están envueltos en marcadores que los distinguen del contexto de instrucciones.
- [ ] Las herramientas de acción tienen confirmación humana como defensa adicional contra prompt injection indirecto.

---

### Fase 4: Observabilidad

**Registro de ejecución**

- [ ] Cada invocación de herramienta genera un registro con: timestamp, sesión, usuario, nombre de herramienta, argumentos, resultado, duración y error si aplica.
- [ ] Los registros de acciones irreversibles tienen política de retención de largo plazo.
- [ ] Los argumentos registrados están sanitizados para no incluir datos sensibles (contraseñas, tokens, datos personales).

**Monitoreo**

- [ ] Hay alertas configuradas para: tasa de error de herramientas superior al umbral, tiempo de respuesta de herramienta superior al SLA, tasa de escalación al equipo humano superior al umbral esperado.
- [ ] El dashboard de operaciones muestra: herramientas más invocadas, herramientas con mayor tasa de error, tiempo promedio de respuesta por herramienta.

---

### Fase 5: Mantenimiento

**Evolución del conjunto de herramientas**

- [ ] Existe un proceso para agregar nuevas herramientas: prueba de descripción, validación del esquema, revisión de seguridad, despliegue gradual.
- [ ] Cuando se modifica la descripción o el esquema de una herramienta, se evalúa el impacto en el comportamiento del modelo antes del despliegue.
- [ ] Las herramientas deprecadas se retiran del contexto activo antes de eliminarlas del código.

**Documentación**

- [ ] Existe un registro de todas las herramientas del sistema: nombre, propósito, sistemas externos que accede, permisos requeridos y propietario responsable.
- [ ] Las decisiones de diseño no obvias (por qué una herramienta fue dividida en dos, por qué se eligió un enum específico) están documentadas.

---

### Indicadores de sistema listo para producción

Un sistema con herramientas está listo para producción cuando:

- Las tasas de error de herramientas en un entorno de staging son inferiores al 2% en condiciones normales de operación.
- El comportamiento del modelo ante errores de herramientas ha sido verificado con errores deliberados en cada tipo de herramienta.
- El tiempo de respuesta end-to-end (desde la solicitud del usuario hasta la respuesta final) cumple el SLA definido en el 95 percentil de las interacciones.
- El equipo puede diagnosticar cualquier interacción pasada usando únicamente los logs de ejecución, sin reproducir la interacción manualmente.
- Existe un proceso documentado para escalar al equipo humano cuando el sistema no puede resolver una solicitud.
