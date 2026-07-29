# Capítulo 15 — Proyecto Integrador

## Sección 05: Integración de RAG, herramientas y MCP

La memoria del sistema, desarrollada en la sección anterior, provee el contexto del usuario. RAG provee el conocimiento corporativo. Las herramientas proveen la capacidad de actuar sobre sistemas externos. Esta sección diseña la integración de esos tres componentes en el orquestador de TechCore.

### El pipeline de recuperación de documentos

El motor RAG de TechCore tiene cinco etapas secuenciales, cada una con un criterio de calidad específico.

**Etapa 1 — Ingestión y chunking.** Los documentos de la base documental corporativa se procesan en fragmentos (chunks) de aproximadamente 400 tokens, con solapamiento de 80 tokens entre fragmentos consecutivos. El solapamiento evita que un concepto que aparece en la frontera entre dos fragmentos quede sin contexto en ninguno de los dos.

Los metadatos de cada fragmento incluyen: nombre del documento, sección, fecha de última modificación, departamento propietario y nivel de clasificación (público interno / confidencial / restringido). Estos metadatos son la base del control de acceso en el nivel de recuperación.

```python
class FragmentoDocumental:
    texto: str          # contenido del fragmento
    embedding: list     # vector de 1536 dimensiones
    doc_nombre: str     # "Runbook-Incidentes-TI-v4.2.pdf"
    seccion: str        # "3.2 Escalación a soporte nivel 2"
    fecha_mod: date     # 2026-05-10
    departamento: str   # "ti"
    clasificacion: str  # "público_interno"
```

**Etapa 2 — Generación de embeddings.** Cada fragmento se convierte en un vector mediante el modelo de embeddings. Para TechCore, se usa el mismo proveedor de API que el LLM, asegurando compatibilidad y un único punto de gestión de credenciales. Los embeddings se generan una vez en la ingestión y se re-generan únicamente cuando el documento fuente cambia.

**Etapa 3 — Recuperación semántica.** Dado el mensaje del usuario, el orquestador genera el embedding de la consulta y ejecuta una búsqueda de similitud coseno en el índice vectorial. Se recuperan los k fragmentos más similares, donde k se fija en 5 para TechCore v1.0. Este valor de k es conservador: garantiza que los fragmentos RAG no excedan el presupuesto de la Zona 3 del contexto (aproximadamente 2.500 tokens).

**Etapa 4 — Filtrado por control de acceso.** Antes de incluir los fragmentos recuperados en el contexto, el orquestador verifica que el usuario tiene permiso para acceder al departamento propietario de cada fragmento. Un fragmento del runbook de TI nunca llega al contexto de un usuario de Legal, aunque sea semánticamente relevante para su consulta. Los fragmentos filtrados se descartan sin notificación al usuario (el usuario no debe saber qué documentos confidenciales existen).

**Etapa 5 — Construcción de la Zona 3.** Los fragmentos que superan el filtro de acceso se incluyen en el contexto con un formato explícito que le indica al LLM su naturaleza y origen:

```
[DOCUMENTACIÓN INTERNA RECUPERADA]

Fuente 1: Runbook-Incidentes-TI-v4.2.pdf — Sección 3.2 (actualizado 2026-05-10)
"El escalamiento a soporte de nivel 2 se activa cuando el tiempo de resolución 
supera los 45 minutos o cuando el impacto afecta a más de 10 usuarios..."

Fuente 2: Política-Gestión-Incidentes-v2.1.pdf — Sección 5 (actualizado 2026-03-22)
"Los incidentes P1 requieren notificación al Gerente de TI en un plazo máximo 
de 15 minutos desde la detección..."

[FIN DOCUMENTACIÓN RECUPERADA]
```

El formato explícito tiene dos funciones: le indica al LLM cuándo citar sus fuentes, y le permite al sistema de observabilidad extraer qué documentos contribuyeron a cada respuesta.

### Herramientas disponibles

TechCore v1.0 expone cuatro herramientas al LLM. Cada herramienta tiene una especificación completa de entrada, salida y condiciones de uso.

**Herramienta 1: `crear_ticket`**

```json
{
  "nombre": "crear_ticket",
  "descripcion": "Crea un nuevo ticket en el sistema de gestión de incidentes. 
                  Solo disponible para usuarios de TI. Requiere confirmación 
                  del usuario antes de ejecutarse.",
  "parametros": {
    "tipo": "incidente | solicitud | cambio",
    "titulo": "string (max 100 caracteres)",
    "descripcion": "string (max 1000 caracteres)",
    "prioridad": "P1 | P2 | P3 | P4",
    "asignado_a": "string (email) | null"
  },
  "respuesta": {
    "ticket_id": "string",
    "url": "string",
    "estado": "creado"
  },
  "permisos_requeridos": ["ti"],
  "requiere_confirmacion": true
}
```

**Herramienta 2: `consultar_directorio`**

```json
{
  "nombre": "consultar_directorio",
  "descripcion": "Busca empleados en el directorio corporativo por nombre 
                  o departamento. Disponible para todos los usuarios.",
  "parametros": {
    "nombre": "string | null",
    "departamento": "ti | legal | rrhh | finanzas | null"
  },
  "respuesta": {
    "empleados": [
      {
        "nombre": "string",
        "cargo": "string",
        "email": "string",
        "departamento": "string"
      }
    ]
  },
  "permisos_requeridos": [],
  "requiere_confirmacion": false
}
```

**Herramienta 3: `verificar_solicitud`**

```json
{
  "nombre": "verificar_solicitud",
  "descripcion": "Consulta el estado actual de una solicitud o ticket existente.",
  "parametros": {
    "id_solicitud": "string"
  },
  "respuesta": {
    "id": "string",
    "estado": "abierto | en_progreso | resuelto | cerrado",
    "titulo": "string",
    "creado": "datetime",
    "ultima_actualización": "datetime",
    "asignado_a": "string | null"
  },
  "permisos_requeridos": [],
  "requiere_confirmacion": false
}
```

**Herramienta 4: `agendar_recordatorio`**

```json
{
  "nombre": "agendar_recordatorio",
  "descripcion": "Crea un recordatorio en el calendario del usuario.",
  "parametros": {
    "fecha_hora": "datetime (ISO 8601)",
    "descripcion": "string (max 200 caracteres)"
  },
  "respuesta": {
    "id_recordatorio": "string",
    "confirmado": true
  },
  "permisos_requeridos": [],
  "requiere_confirmacion": true
}
```

### El ciclo de invocación de herramientas

El LLM no ejecuta herramientas directamente: solicita al orquestador que las ejecute. El flujo es:

```
Usuario: "Crea un ticket P1 por el servidor web-03 que está caído"
          │
          ▼
Orquestador → LLM (con contexto completo)
          │
          ▼
LLM responde con llamada a herramienta:
{
  "tool": "crear_ticket",
  "parametros": {
    "tipo": "incidente",
    "titulo": "Servidor web-03 caído",
    "descripcion": "El servidor web-03 no responde. Impacto: producción.",
    "prioridad": "P1"
  }
}
          │
          ▼
Orquestador valida permisos → usuario pertenece a TI ✓
          │
          ▼
Orquestador presenta al usuario:
"Voy a crear el siguiente ticket:
 - Tipo: Incidente P1
 - Título: Servidor web-03 caído
 - Descripción: El servidor web-03 no responde. Impacto: producción.
 ¿Confirmas? [Sí / No / Modificar]"
          │
          ▼ (usuario confirma)
Orquestador ejecuta herramienta → ticket_id: #4521
          │
          ▼
Resultado enviado al LLM como mensaje de herramienta
          │
          ▼
LLM genera respuesta final:
"Ticket #4521 creado correctamente. Puedes seguirlo aquí: [url]. 
Al ser P1, el equipo de guardia recibirá notificación automática."
```

### MCP como capa de integración

El protocolo MCP (Model Context Protocol) es el mecanismo estándar para que el orquestador y el LLM intercambien definiciones de herramientas y resultados de ejecución en un formato estructurado. Para TechCore, MCP resuelve tres problemas:

**Primero**, estandariza la descripción de herramientas: en lugar de que cada proveedor de LLM tenga su propio formato de function calling, MCP provee un esquema común que puede traducirse a cualquier proveedor. Esto hace que el orquestador no esté acoplado a un único proveedor de API.

**Segundo**, gestiona el ciclo de vida de las llamadas: MCP define claramente cuándo el LLM ha terminado de razonar y cuándo está esperando el resultado de una herramienta, lo que simplifica el bucle de control del orquestador.

**Tercero**, permite exponer servidores MCP externos: si TechCore decide integrar el sistema de tickets de un proveedor que ya tiene un servidor MCP publicado, puede conectarlo sin escribir código de integración a medida.

La implementación de MCP en TechCore v1.0 usa el cliente MCP estándar en el orquestador, con servidores MCP locales para cada herramienta corporativa. Los servidores locales hacen las llamadas reales a las APIs internas de TechCore y devuelven resultados en formato MCP al orquestador.

### Degradación controlada

Cuando una herramienta falla —el sistema de tickets no responde, el directorio está en mantenimiento— el sistema no debe fallar silenciosamente. El diseño de TechCore incluye respuestas de degradación controlada para cada herramienta:

| Herramienta          | Fallo                          | Respuesta al usuario                                    |
|----------------------|--------------------------------|---------------------------------------------------------|
| `crear_ticket`       | API no disponible              | "El sistema de tickets no responde. Intenta en [URL] directamente o contacta a soporte." |
| `consultar_directorio` | Timeout                      | "El directorio no está disponible ahora. El área de RRHH puede ayudarte." |
| `verificar_solicitud`| Registro no encontrado         | "No encontré la solicitud [id]. Verifica el identificador o consulta directamente." |
| `agendar_recordatorio` | Error de calendario          | "No pude agendar el recordatorio. Puedes hacerlo manualmente desde [URL]." |

La degradación controlada asegura que un fallo de herramienta no deje al usuario sin respuesta: el sistema siempre le indica qué alternativa tiene.

---

Con el diseño de RAG y herramientas establecido, la siguiente sección incorpora el componente más complejo de la arquitectura: el agente de análisis de incidentes de TI.
