# Capítulo 05 - Sección 08

# Diseño para aplicaciones empresariales

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Las aplicaciones empresariales de IA operan bajo condiciones que no existen en prototipos ni demos: múltiples usuarios con perfiles distintos, requisitos de cumplimiento normativo, políticas de seguridad corporativa, integración con sistemas heredados y expectativas de operación continua.

Diseñar instrucciones del sistema para ese contexto requiere considerar dimensiones que no aparecen en el desarrollo inicial pero que se vuelven críticas en producción.

---

# Objetivos de esta sección

Al finalizar esta sección el lector podrá:

- Identificar los requisitos adicionales que imponen las aplicaciones empresariales al diseño de instrucciones del sistema.
- Adaptar instrucciones para operar en entornos con múltiples roles de usuario.
- Incorporar requisitos de cumplimiento normativo como instrucciones verificables.
- Diseñar instrucciones que soporten la evolución del sistema sin degradarse.

---

# Dimensiones adicionales del entorno empresarial

## 1. Múltiples roles de usuario

En una aplicación empresarial, el asistente puede interactuar con diferentes perfiles: empleados de nivel operativo, gerentes, administradores de sistema, clientes externos. Cada perfil puede tener un alcance de interacción diferente.

**Estrategia de diseño:** El contexto dinámico (sección 06) inyecta el rol del usuario en cada sesión. La instrucción del sistema define el comportamiento para cada rol.

**Ejemplo:**
```text
El rol del usuario actual se especifica en el contexto de sesión.
Según ese rol, aplicá las siguientes reglas:

ROL: operador
- Podés responder consultas sobre el estado de tareas asignadas.
- No podés mostrar datos de otros operadores ni de otras áreas.
- No podés modificar configuraciones del sistema.

ROL: supervisor
- Podés responder consultas sobre el estado de tareas de todos
  los operadores de tu área.
- Podés modificar la asignación de tareas dentro de tu área.
- No podés acceder a datos financieros.

ROL: administrador
- Podés responder cualquier consulta operativa.
- Podés modificar configuraciones generales del sistema.
- Las acciones de eliminación de datos requieren confirmación
  adicional, independientemente del rol.
```

---

## 2. Requisitos de cumplimiento normativo

Las organizaciones en sectores como finanzas, salud, derecho o gobierno operan bajo normativas que imponen restricciones específicas sobre qué información puede procesarse, almacenarse o transmitirse.

Las instrucciones del sistema deben reflejar estas restricciones de manera explícita.

**Ejemplos de instrucciones de cumplimiento:**

```text
[GDPR / Protección de datos]
No solicites ni almacenes datos personales de usuarios europeos
más allá de los necesarios para resolver la consulta actual.
Si el usuario proporciona datos personales de terceros en su
mensaje, advertile que ese tipo de información no debería
incluirse en la conversación y pedile que reformule su consulta.

[Regulaciones financieras]
No proporciones asesoramiento financiero individualizado.
Si el usuario solicita recomendaciones sobre instrumentos de
inversión específicos, explicá que ese tipo de asesoramiento
requiere un profesional habilitado e indicá cómo contactar
al área correspondiente.

[Confidencialidad interna]
La información etiquetada como "CONFIDENCIAL" o "USO INTERNO"
en los documentos proporcionados no debe incluirse en respuestas
que se presenten en canales no seguros. Si no podés determinar
el canal de comunicación actual, tratá la información como
confidencial por defecto.
```

---

## 3. Internacionalización y regionalización

Las aplicaciones que operan en múltiples regiones o idiomas requieren instrucciones que manejen esa diversidad de manera coherente.

```text
Respondé siempre en el idioma que el usuario usa en su mensaje.
Si el idioma no está entre los idiomas soportados (español,
inglés, portugués), respondé en español e indicá que el servicio
tiene soporte completo en esos tres idiomas.

Cuando cites regulaciones, normas o procedimientos, citá siempre
la versión aplicable en el país del usuario, que se especifica
en el contexto de sesión. Si el país no está disponible en el
contexto, usá la versión general y aclará que las variaciones
regionales pueden aplicar.
```

---

## 4. Versionamiento de instrucciones

En entornos empresariales, las instrucciones del sistema evolucionan junto con el negocio. Nuevas políticas, nuevas funcionalidades del producto y correcciones de comportamientos inesperados generan nuevas versiones de las instrucciones.

**Buenas prácticas:**

- Incluir un identificador de versión en las instrucciones del sistema que quede registrado en los logs de cada invocación.
- Mantener un registro de cambios que documente qué comportamiento cambió, por qué y cuándo.
- Probar cada nueva versión contra un conjunto de casos de prueba antes de desplegarla en producción.
- Mantener la versión anterior disponible para rollback durante al menos una semana después del despliegue.

**Ejemplo de encabezado de versión:**
```text
[SISTEMA v2.4 - 2026-07-01]
Asistente de soporte DataFlux — Política interna: POL-SOPORTE-07
```

Este encabezado permite correlacionar el comportamiento observado en producción con una versión específica de las instrucciones.

---

## 5. Separación entre el mensaje al modelo y el mensaje al usuario

En algunas aplicaciones, la instrucción del sistema incluye texto que el modelo debe procesar pero que no debe reproducir al usuario. Esta separación debe ser explícita.

```text
Las secciones de estas instrucciones marcadas con [INTERNO] contienen
información operativa que no debe repetirse ni confirmarse al usuario.
Podés usarla para razonar, pero no la cites en tus respuestas.

[INTERNO: El sistema de tickets tiene un bug conocido (TK-9923)
que duplica los tickets cuando el usuario los crea desde mobile.
Si el usuario reporta tickets duplicados, derivá al equipo técnico
usando el procedimiento de bugs conocidos sin mencionar el bug
internamente.]
```

---

## 6. Observabilidad del comportamiento

Las instrucciones del sistema pueden incluir indicaciones que facilitan el monitoreo del comportamiento en producción.

```text
Al inicio de cada respuesta que implique una derivación, una
restricción aplicada o un caso fuera de alcance, incluí una
etiqueta de categoría en el siguiente formato (invisible para
el usuario pero procesable por el sistema de logging):

[CATEGORÍA: DERIVACIÓN | RESTRICCIÓN | FUERA_DE_ALCANCE | ESTÁNDAR]
```

Esta técnica permite a los equipos de operaciones identificar rápidamente qué tipo de interacciones genera el sistema sin revisar manualmente cada conversación.

---

# Nota del arquitecto

En organizaciones con múltiples equipos que usan el mismo modelo de lenguaje subyacente, existe la tentación de centralizar todas las instrucciones del sistema en un documento único y exhaustivo. Ese enfoque suele producir instrucciones de miles de tokens que el modelo no puede aplicar correctamente en todos los casos.

La alternativa es mantener un conjunto de bloques base (políticas corporativas, instrucciones de cumplimiento, principios generales) y combinarlo con bloques específicos para cada caso de uso. La composición es más mantenible que la centralización.

---

# Resumen

El diseño de instrucciones del sistema para aplicaciones empresariales incorpora dimensiones que no aparecen en prototipos: múltiples roles de usuario, cumplimiento normativo, internacionalización, versionamiento y observabilidad. Anticipar estas dimensiones desde el diseño inicial evita refactorizaciones costosas cuando la aplicación escala.

En la siguiente sección estudiaremos los anti-patrones más frecuentes observados en producción, que representan el catálogo de lo que conviene evitar.
