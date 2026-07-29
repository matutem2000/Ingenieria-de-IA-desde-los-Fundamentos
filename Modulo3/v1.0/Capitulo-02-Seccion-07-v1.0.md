# Capitulo-02-Seccion-07-v1.0

# Memoria, historial y RAG: cuándo utilizar cada uno

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Uno de los errores más comunes al diseñar aplicaciones con modelos de lenguaje consiste en utilizar indistintamente memoria, historial y RAG como si fueran mecanismos equivalentes.

Aunque los tres forman parte del contexto, **resuelven problemas completamente diferentes**. Elegir el componente incorrecto suele producir aplicaciones más costosas, menos precisas y difíciles de mantener.

---

# Tres componentes, tres responsabilidades

| Componente | Propósito principal | Duración | Pregunta que responde |
|------------|---------------------|----------|-----------------------|
| Historial | Mantener el hilo de la conversación actual | Minutos u horas | ¿Qué ocurrió en esta conversación? |
| Memoria | Recordar información útil entre conversaciones | Días, meses o años | ¿Qué conviene recordar del usuario o del sistema? |
| RAG | Recuperar conocimiento externo actualizado | Bajo demanda | ¿Qué conocimiento necesito consultar ahora? |

---

# Ejemplo práctico

Un usuario pregunta:

> "Necesito continuar el informe que empezamos ayer."

La aplicación actúa de la siguiente manera:

- El **historial** aporta las últimas interacciones de la conversación.
- La **memoria** recuerda que el usuario suele trabajar en español y prefiere informes en Markdown.
- El **RAG** recupera la documentación del proyecto almacenada en la base de conocimiento.

El modelo recibe un contexto mucho más rico que si dependiera únicamente del mensaje del usuario.

---

# Un criterio sencillo

Antes de incorporar información al contexto, pregúntese:

1. ¿Solo sirve para esta conversación? → Historial.
2. ¿Será útil en conversaciones futuras? → Memoria.
3. ¿Proviene de documentos o datos externos? → RAG.

Este criterio evita gran parte de los errores de diseño.

---

# El caso borde: información que pertenece a más de una categoría

Un escenario frecuente en producción surge cuando una pieza de información podría pertenecer a más de una categoría simultáneamente.

Por ejemplo: durante una conversación, el equipo de arquitectura decide adoptar un nuevo estándar de nomenclatura para los servicios. Esa decisión es parte del historial de la sesión pero también debería quedar registrada en la base de conocimiento de la organización para ser consultada en el futuro.

El criterio general para estos casos es:

- si la información tiene valor operacional inmediato solo para esta conversación, va al historial;
- si tiene valor estructural y reutilizable para el sistema o para el negocio, va a RAG;
- si tiene valor personal y persistente sobre el usuario, va a memoria.

Cuando la información cumple más de un criterio, registrarla en ambos lugares es válido, siempre que exista una política clara sobre cuál es la fuente de verdad y cómo se mantienen sincronizadas.

---

# Errores frecuentes

## Guardar documentos completos en memoria

La memoria debe contener conocimiento persistente y estructurado, no grandes volúmenes de documentación. Los documentos extensos pertenecen a RAG.

## Usar el historial como base documental

El historial no reemplaza una base de conocimiento. A medida que crece, se vuelve costoso e ineficiente.

## Recuperar siempre los mismos documentos

El RAG debe recuperar únicamente la información relevante para la consulta actual, no un conjunto fijo de documentos por defecto.

---

# Patrón recomendado

Una arquitectura empresarial suele seguir este flujo:

```text
Usuario
   │
   ├── Historial reciente
   ├── Memoria persistente
   ├── Recuperación RAG
   └── Herramientas
          │
          ▼
      Contexto final
          │
          ▼
          LLM
```

Cada componente aporta información diferente sin superponer responsabilidades.

---

# Buenas prácticas

- Mantener separados los tres mecanismos con políticas de actualización independientes.
- Evitar duplicar información entre memoria y RAG sin una justificación explícita.
- Priorizar calidad antes que cantidad en cada capa.

---

# Ejercicio de diagnóstico

Un equipo implementa un asistente de atención al cliente con la siguiente arquitectura:

- El historial de la sesión actual se almacena junto con conversaciones de los últimos 30 días.
- La documentación del producto (manual de 400 páginas) se guarda completa en la memoria persistente del usuario.
- Las instrucciones del sistema incluyen: nombre del usuario autenticado, permisos de acceso y la hora de inicio de la sesión.
- Cuando el usuario consulta el estado de un pedido, el sistema recupera los mismos 10 documentos de la base RAG sin importar la consulta.

Identifique los errores de diseño aplicando los criterios aprendidos en este capítulo.

**Errores esperados:**

1. El historial de 30 días mezcla historial conversacional con memoria; los intercambios antiguos deberían resumirse o persistirse como memoria estructurada.
2. La documentación completa del producto pertenece a RAG, no a memoria persistente; almacenarla en memoria satura el contexto y lo encarece.
3. El nombre del usuario, los permisos y la hora de sesión son datos de contexto de ejecución, no reglas del sistema; incluirlos en el prompt de sistema los vuelve estáticos e incorrectos en la próxima sesión.
4. El RAG debería recuperar únicamente los documentos relevantes para la consulta actual, no siempre el mismo conjunto fijo.

---

# Resumen

Historial, memoria y RAG no compiten entre sí: se complementan. Una arquitectura de Context Engineering madura utiliza cada mecanismo para aquello que mejor sabe hacer, logrando asistentes más precisos, eficientes y fáciles de evolucionar.

En la próxima sección analizaremos el papel de las herramientas y los resultados de ejecución como parte de la anatomía del contexto.
