# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 11: Laboratorio — Threat Modeling de un sistema de Context Engineering

El threat modeling (modelado de amenazas) es el proceso de identificar sistemáticamente las amenazas a las que está expuesto un sistema, evaluar su impacto potencial y diseñar controles para mitigarlas. Es la práctica de seguridad proactiva por excelencia: en lugar de esperar a que ocurra un incidente, el AI Engineer analiza su sistema antes del despliegue para identificar los riesgos.

Este laboratorio guía al estudiante a través de un ejercicio completo de threat modeling aplicado a un sistema de Context Engineering. El sistema sobre el que se trabaja es el asistente de soporte técnico diseñado en los capítulos anteriores del módulo: un asistente con RAG sobre documentación técnica, historial de conversaciones, capacidad de ejecutar herramientas de diagnóstico y conexión a un sistema de tickets.

### Marco del laboratorio: STRIDE aplicado al Context Engineering

El marco STRIDE es una metodología de threat modeling que organiza las amenazas en seis categorías. Adaptado al Context Engineering, cada categoría corresponde a un tipo de riesgo específico:

| Categoría | Amenaza que modela | Ejemplo en CE |
|-----------|-------------------|---------------|
| **S** — Spoofing (suplantación) | Atacante finge ser un usuario legítimo o el sistema | Usuario finge ser administrador para cambiar el comportamiento |
| **T** — Tampering (alteración) | Modificación no autorizada de datos o configuración | Alterar documentos del corpus RAG |
| **R** — Repudiation (repudio) | Negar haber realizado una acción | Ejecutar una herramienta y negar haberlo solicitado |
| **I** — Information Disclosure (divulgación) | Acceso no autorizado a información | Extraer system prompt, acceder a datos de otros usuarios |
| **D** — Denial of Service (denegación de servicio) | Interrumpir la disponibilidad del sistema | Consultas que agotan el presupuesto de tokens |
| **E** — Elevation of Privilege (escalación de privilegios) | Ganar permisos no autorizados | Inducir al agente a ejecutar herramientas sin permisos |

### Paso 1: Identificación de activos y componentes

El primer paso del threat modeling es describir el sistema: sus componentes, las conexiones entre ellos y los activos que se deben proteger.

**Ejercicio:** Completa la siguiente tabla para el asistente de soporte técnico:

| Componente | Descripción | Activos que contiene |
|------------|-------------|---------------------|
| System prompt | Instrucciones de comportamiento del asistente | Lógica de negocio, restricciones, referencias a sistemas |
| Índice RAG | Base de conocimiento de documentación técnica | Documentos internos, procedimientos, configuraciones |
| Historial de conversaciones | Registro de interacciones por usuario | Datos de usuario, consultas anteriores |
| Herramienta: diagnóstico | Ejecuta comandos de diagnóstico en sistemas | Acceso a logs de sistemas internos |
| Herramienta: tickets | Crea y consulta tickets de soporte | Datos de incidentes, información de clientes afectados |
| Base de datos de usuarios | Perfiles y permisos de los técnicos | PII del personal, niveles de acceso |

**Flujo de datos a documentar:**
Dibuja el flujo completo desde que el usuario envía un mensaje hasta que recibe la respuesta. Identifica en cada paso: qué datos fluyen, entre qué componentes y si la conexión es cifrada o no.

### Paso 2: Identificación de amenazas

Para cada componente y conexión del flujo, aplica las categorías STRIDE y genera amenazas concretas. A continuación se presentan ejemplos para tres componentes; el estudiante debe completar los restantes.

**Sistema prompt — Amenazas identificadas:**

| STRIDE | Amenaza concreta |
|--------|-----------------|
| Information Disclosure | Un técnico extrae el system prompt mediante elicitación repetida |
| Tampering | Un administrador con acceso al repositorio modifica el system prompt sin pasar por el proceso de revisión |
| Repudiation | Un cambio al system prompt no queda registrado con el autor |

**Índice RAG — Amenazas identificadas:**

| STRIDE | Amenaza concreta |
|--------|-----------------|
| Tampering | Un proveedor con acceso al sistema de documentación añade instrucciones maliciosas en un documento de procedimientos |
| Information Disclosure | Un técnico junior accede a documentos de configuración restringida porque el índice no aplica filtros de acceso |
| Denial of Service | Un documento extremadamente largo es recuperado repetidamente, agotando el presupuesto de tokens |

**Herramienta de diagnóstico — Amenazas identificadas:**

| STRIDE | Amenaza concreta |
|--------|-----------------|
| Elevation of Privilege | Un prompt injection induce al agente a ejecutar un comando de diagnóstico con parámetros no autorizados |
| Repudiation | El agente ejecuta un comando y no queda registro de qué usuario originó la solicitud |
| Tampering | Los resultados del diagnóstico son modificados antes de llegar al modelo (si la comunicación no está cifrada) |

**Tarea del estudiante:** Completa el análisis STRIDE para el historial de conversaciones, la herramienta de tickets y la base de datos de usuarios.

### Paso 3: Evaluación de riesgo

Para cada amenaza identificada, evalúa su riesgo con dos dimensiones:

**Probabilidad:** ¿Qué tan probable es que esta amenaza se materialice? (Baja / Media / Alta)

**Impacto:** Si la amenaza se materializa, ¿cuál es el daño? (Bajo / Medio / Alto / Crítico)

**Prioridad:** Probabilidad × Impacto determina la prioridad de mitigación.

Ejemplo de matriz de riesgo para tres amenazas del caso:

| Amenaza | Probabilidad | Impacto | Prioridad |
|---------|-------------|---------|-----------|
| Extracción del system prompt | Media | Medio | Media |
| Prompt injection indirecto en RAG | Media | Alto | Alta |
| Acceso no autorizado a documentos restringidos | Alta | Alto | Crítica |
| Ejecución de comando con parámetros no autorizados | Baja | Crítico | Alta |

**Tarea del estudiante:** Completa la matriz de riesgo para todas las amenazas identificadas en el paso 2. Ordénalas de mayor a menor prioridad.

### Paso 4: Diseño de controles

Para las cinco amenazas de mayor prioridad, diseña un control técnico específico. El control debe especificar:
- Dónde se implementa (en qué componente o paso del flujo).
- Cómo funciona (descripción funcional, puede incluir pseudocódigo).
- Qué amenaza mitiga.
- Qué limitaciones tiene.

Ejemplo de control diseñado para la amenaza de acceso no autorizado a documentos restringidos:

**Control:** Filtro de acceso en el pipeline de recuperación RAG.

**Implementación:** Cada documento en el índice tiene metadatos de clasificación. El pipeline de recuperación recibe el perfil del usuario autenticado (su rol, su equipo, su nivel de acceso) y aplica un filtro que excluye documentos cuyo nivel de clasificación supere el del usuario. El filtro se aplica en el momento de la recuperación, no en el momento de la presentación al usuario.

**Mitiga:** Acceso no autorizado a documentos restringidos mediante consultas al RAG.

**Limitaciones:** No mitiga el caso en que el propietario del documento cambia su nivel de clasificación después de que el documento fue indexado sin re-indexación inmediata. Requiere un proceso de re-indexación cuando cambia la clasificación de un documento.

**Tarea del estudiante:** Diseña controles para las cuatro amenazas restantes de alta prioridad.

### Paso 5: Verificación

Para cada control diseñado, define un caso de prueba que verifique que el control funciona:

**Control a verificar:** Filtro de acceso en RAG.

**Caso de prueba:**
1. Crear un documento con metadatos `nivel_acceso: "restringido"` en el índice.
2. Autenticarse con un usuario con nivel de acceso "estandar".
3. Realizar una consulta cuya respuesta semánticamente está en ese documento.
4. Verificar que el documento no aparece en los resultados de recuperación.
5. Autenticarse con un usuario con nivel "restringido" y repetir la consulta.
6. Verificar que el documento sí aparece ahora.

**Resultado esperado:** El documento solo es recuperado cuando el nivel de acceso del usuario lo permite.

### Entrega del laboratorio

El estudiante entrega un documento de threat modeling completo que incluye:

1. Diagrama del flujo de datos del sistema.
2. Tabla de activos y componentes.
3. Análisis STRIDE completo (todas las amenazas identificadas).
4. Matriz de riesgo con todas las amenazas evaluadas.
5. Controles diseñados para las cinco amenazas de mayor prioridad.
6. Casos de prueba para verificar cada control.

El objetivo no es encontrar todas las amenazas posibles —eso es imposible— sino demostrar que el AI Engineer puede razonar sistemáticamente sobre los riesgos de seguridad de un sistema que ha diseñado, y proponer controles concretos y verificables.

La siguiente sección consolida los conceptos de este capítulo en una lista de verificación práctica para el AI Engineer que diseña, implementa y opera sistemas de Context Engineering en entornos empresariales.
