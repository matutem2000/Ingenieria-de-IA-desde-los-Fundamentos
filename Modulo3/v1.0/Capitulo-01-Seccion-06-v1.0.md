# Laboratorio rápido: diseñar una arquitectura de contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Los principios del Context Engineering se comprenden mejor cuando se aplican a un problema real. Este laboratorio propone un ejercicio estructurado de diseño que puede completarse en aproximadamente diez minutos.

El objetivo no es producir una implementación funcional, sino entrenar la capacidad de pensar en términos de capas de contexto antes de escribir una sola línea de código.

---

# Enunciado

Elija un asistente de IA que podría ser útil en su dominio de trabajo. Puede ser real o hipotético. Algunos ejemplos orientativos:

- un asistente para un equipo de desarrollo de software;
- un asistente jurídico para un estudio de abogados;
- un asistente de onboarding para nuevos empleados;
- un asistente de análisis de datos para un equipo de finanzas;
- un asistente de soporte técnico para un producto SaaS.

---

# Paso 1 — Definir el asistente

Responda brevemente:

- ¿Qué problema resuelve?
- ¿Quiénes son sus usuarios?
- ¿Cuál es la consulta más frecuente que recibirá?

---

# Paso 2 — Completar el esquema de capas

Para el asistente elegido, identifique qué información debería colocarse en cada capa del contexto. Use la siguiente plantilla:

```text
┌─────────────────────────────────────────────────────────────┐
│ INSTRUCCIONES DEL SISTEMA                                   │
│ Rol, objetivos, restricciones, tono, formato de salida      │
│                                                             │
│ →                                                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ PERFIL DEL USUARIO                                          │
│ Datos estables sobre quien realiza la consulta              │
│                                                             │
│ →                                                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ MEMORIA                                                     │
│ Información persistente entre conversaciones                │
│                                                             │
│ →                                                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ INFORMACIÓN RECUPERADA (RAG)                                │
│ Documentos o datos obtenidos dinámicamente                  │
│                                                             │
│ →                                                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ HERRAMIENTAS Y APIs                                         │
│ Acciones o fuentes de datos en tiempo real                  │
│                                                             │
│ →                                                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ POLÍTICAS Y RESTRICCIONES                                   │
│ Reglas de negocio, seguridad y cumplimiento                 │
│                                                             │
│ →                                                           │
└─────────────────────────────────────────────────────────────┘
```

---

# Paso 3 — Identificar decisiones de diseño

Una vez completado el esquema, responda:

1. ¿Qué capa tiene mayor impacto en la calidad de las respuestas para este caso de uso?
2. ¿Qué información podría recuperarse bajo demanda en lugar de enviarse siempre?
3. ¿Existe alguna capa vacía? ¿Es intencional o es un problema de diseño?
4. ¿Cómo resolverá el sistema un conflicto entre lo que pide el usuario y una política definida en el sistema?

---

# Ejemplo resuelto: asistente de soporte técnico

**Descripción:** asistente interno para un equipo de soporte de primer nivel de una empresa de software.

**Capa de sistema:** "Eres un agente de soporte técnico para [Producto]. Responde en el idioma del usuario. No compartas información de otros clientes. Escala los incidentes P1 al equipo de guardia de forma inmediata."

**Perfil del usuario:** nombre, área, nivel de acceso al sistema, tickets previos abiertos en los últimos 30 días.

**Memoria:** preferencias de comunicación del usuario (técnica vs. simplificada), historial de incidentes recurrentes.

**RAG:** base de conocimiento de soluciones conocidas, release notes de las últimas versiones, guías de troubleshooting.

**Herramientas:** API del sistema de tickets (consultar y actualizar estado), API de monitoreo (ver estado de servicios), directorio de contactos del equipo de guardia.

**Políticas:** los incidentes P1 no pueden cerrarse sin aprobación del equipo de ingeniería; no se comparte información de configuración de producción con usuarios sin acceso de nivel 3.

**Decisiones de diseño:**
- El estado del incidente se recupera en tiempo real (herramienta), no se precarga en memoria.
- Las políticas de escalamiento tienen precedencia sobre cualquier instrucción del usuario.
- La base de conocimiento se filtra por versión del producto antes de enviarse al modelo.

---

# Cierre del laboratorio

No existe una única respuesta correcta. La validez de un diseño de contexto se mide por su capacidad para producir respuestas precisas, predecibles y económicas a lo largo del tiempo.

En la siguiente sección integraremos todos estos conceptos mediante un caso de estudio completo que muestra la evolución de una solución real, desde un prompt inicial hasta una arquitectura profesional.
