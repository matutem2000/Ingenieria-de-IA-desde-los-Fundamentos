# Capítulo 10 — Planificación y Razonamiento

## Sección 06: Reflexión y autoevaluación del agente

La reflexión es el mecanismo por el cual un agente evalúa su propio output, identifica deficiencias y genera una versión mejorada. Es uno de los patrones más importantes en sistemas de IA de producción y uno de los menos comprendidos: no porque sea difícil de implementar, sino porque requiere entender con precisión qué puede y qué no puede detectar un modelo cuando evalúa su propio trabajo.

### El patrón Reflexion

El patrón Reflexion (Shinn et al., 2023) formaliza el ciclo de autoevaluación en tres fases:

**Fase 1 — Generación:** El agente produce una respuesta a la tarea.

**Fase 2 — Evaluación:** El agente (o un segundo agente evaluador) revisa la respuesta contra criterios explícitos y produce una crítica. La crítica identifica específicamente qué está mal, qué falta y qué podría mejorarse.

**Fase 3 — Revisión:** El agente produce una nueva respuesta incorporando la crítica. La nueva respuesta tiene acceso al contexto original, la respuesta inicial y la crítica.

El ciclo puede repetirse: la respuesta revisada puede ser evaluada nuevamente, producir una nueva crítica y generar una tercera versión. En práctica, 2-3 ciclos son el límite útil; más iteraciones raramente mejoran el output y con frecuencia lo degradan al hacer que el modelo sea excesivamente cauteloso o redundante.

### Ciclo de reflexión completo: ejemplo paso a paso

**Tarea:** Generar una política de seguridad para el acceso a la API de un sistema de pagos.

---

**ITERACIÓN 1 — GENERACIÓN**

*Prompt al agente:*
```
Eres un especialista en seguridad de sistemas financieros. Genera una política
de control de acceso para la API REST de un sistema de pagos. La política debe
cubrir autenticación, autorización, rate limiting y auditoría.
```

*Respuesta inicial:*
```
POLÍTICA DE ACCESO — API DE PAGOS

1. Autenticación
   - Todos los clientes deben usar OAuth 2.0 con tokens JWT.
   - Los tokens expiran a las 24 horas.
   - Se requiere HTTPS para todas las conexiones.

2. Autorización
   - Modelo de permisos basado en roles (RBAC).
   - Roles disponibles: lectura, escritura, administración.

3. Rate Limiting
   - Máximo 1000 requests por hora por cliente.

4. Auditoría
   - Se registran todos los accesos a la API.
```

---

**ITERACIÓN 1 — EVALUACIÓN**

*Prompt al evaluador:*
```
Revisa esta política de control de acceso para una API de pagos.
Identifica: (a) qué requisitos de seguridad están ausentes o incompletos,
(b) qué valores o parámetros son inadecuados para un sistema financiero,
(c) qué aspectos regulatorios o de compliance deben considerarse.
```

*Crítica:*
```
DEFICIENCIAS IDENTIFICADAS:

(a) Elementos ausentes o incompletos:
- No especifica el algoritmo de firma del JWT ni el tamaño mínimo de clave.
- No menciona refresh tokens ni el proceso de rotación de tokens.
- El RBAC no especifica qué operaciones puede realizar cada rol.
- No hay política de bloqueo de cuentas ante intentos fallidos de autenticación.
- No se menciona validación de certificados en el cliente (mutual TLS).
- Falta política de revocación de tokens comprometidos.

(b) Valores inadecuados para sistema financiero:
- El token de 24 horas es excesivo para tokens de acceso en sistemas de pagos;
  PCI DSS recomienda tokens de acceso de corta vida (15-60 minutos) con refresh
  token separado.
- 1000 requests/hora puede ser demasiado permisivo o demasiado restrictivo
  según el volumen de operaciones; debe diferenciarse por operación (lectura
  vs. escritura vs. pago).

(c) Aspectos regulatorios ausentes:
- PCI DSS requiere retención de logs de auditoría por mínimo 12 meses.
- Debe especificarse qué datos se registran en auditoría (sin PAN completo).
- Falta referencia a requerimientos de SCA (Strong Customer Authentication)
  bajo PSD2 si aplica la jurisdicción europea.
```

---

**ITERACIÓN 2 — REVISIÓN**

*Prompt al agente:*
```
[contexto original] + [respuesta inicial] + [crítica]

Genera una versión revisada de la política incorporando todas las correcciones
identificadas en la crítica.
```

*Respuesta revisada:*
```
POLÍTICA DE ACCESO — API DE PAGOS v2

1. Autenticación
   - Todos los clientes usan OAuth 2.0 con tokens JWT firmados con RS256
     (clave mínima 2048 bits).
   - Tokens de acceso: vigencia de 30 minutos. Refresh tokens: vigencia de
     8 horas, rotación automática en cada uso.
   - HTTPS obligatorio (TLS 1.2 mínimo). Para clientes institucionales:
     mutual TLS con certificado de cliente válido.
   - Bloqueo temporal de cliente tras 5 intentos fallidos en 10 minutos.
     Desbloqueo manual por administrador o automático a las 2 horas.
   - Proceso de revocación de emergencia: invalidación inmediata de todos los
     tokens del cliente mediante endpoint de revocación.

2. Autorización (RBAC)
   - Rol "lectura": consultar estado de transacciones propias.
   - Rol "pago": iniciar transacciones de pago (requiere autenticación 2FA
     adicional para montos superiores a umbral configurable).
   - Rol "administración": gestionar clientes, configurar límites, acceder
     a reportes agregados.
   - Las operaciones de pago requieren verificación adicional por SCA
     cuando aplique PSD2.

3. Rate Limiting (por cliente y por tipo de operación)
   - Consultas: 5000 requests/hora.
   - Iniciación de pagos: 100 requests/hora (límite más restrictivo por
     impacto financiero).
   - Administración: 500 requests/hora.
   - Alertas automáticas al 80% del límite; bloqueo temporal al 100%.

4. Auditoría
   - Se registra todo acceso con: timestamp, cliente ID, endpoint, resultado,
     IP de origen. Sin datos de PAN completo (solo últimos 4 dígitos).
   - Retención de logs: mínimo 12 meses en línea, 7 años en archivo (PCI DSS).
   - Logs inmutables: no modificables ni eliminables por ningún rol incluyendo
     administración.
   - Alertas en tiempo real para: autenticaciones fallidas repetidas, accesos
     fuera de horario habitual, volúmenes de transacción inusualmente altos.
```

---

### Qué puede y qué no puede detectar la reflexión

**La reflexión es efectiva para detectar:**

- Omisiones de elementos que deberían estar presentes (la crítica puede revisar una lista de requisitos conocidos)
- Inconsistencias internas en el output (contradicciones entre partes del mismo documento)
- Violaciones de restricciones explícitas (longitud, formato, inclusión de elementos requeridos)
- Brechas de cobertura (temas mencionados en el prompt que no aparecen en el output)

**La reflexión no puede detectar de forma confiable:**

- Errores factuales en dominios donde el evaluador tiene el mismo conocimiento incorrecto que el generador
- Errores de razonamiento matemático o lógico donde el modelo produce resultados incorrectos con confianza alta
- Violaciones de requisitos no especificados en el prompt (el modelo no puede saber lo que no se le dijo)

Esta limitación es la razón por la que la verificación externa — examinada en la siguiente sección — es un complemento necesario, no un sustituto, de la reflexión interna.

### El evaluador separado

Una mejora significativa al patrón de reflexión básico es usar un evaluador separado: un modelo diferente, con un prompt diferente, que actúa como crítico independiente. Esto reduce el riesgo de que el evaluador comparta los puntos ciegos del generador.

En práctica, incluso usar el mismo modelo con un prompt de evaluación muy diferente al prompt de generación produce evaluaciones más útiles que pedir al modelo que evalúe su propio output directamente. El prompt de evaluación debe:

- Especificar criterios de evaluación explícitos
- Pedir al modelo que busque activamente deficiencias, no que confirme calidad
- Proporcionar ejemplos de los tipos de problemas que debe encontrar
- Instruir al modelo para que sea específico, no genérico ("la sección X omite Y" en lugar de "podría ser más completo")

### Nota del arquitecto

La reflexión no es gratuita. Agrega latencia y costo en proporción al número de iteraciones. El AI Engineer debe definir a priori cuántas iteraciones son válidas y qué criterio determina cuándo la reflexión ha convergido. Un output aceptable después de dos iteraciones es mejor que un output ligeramente mejor después de cinco iteraciones si la latencia adicional tiene un costo en la experiencia del usuario o en el costo operativo del sistema.

La siguiente sección examina la verificación de resultados: el mecanismo externo que complementa la reflexión interna cuando la tarea requiere garantías de corrección que el modelo solo no puede proporcionar.
