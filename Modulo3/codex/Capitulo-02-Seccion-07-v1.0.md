# Capitulo-02-Seccion-07-v1.0

# Memoria, historial y RAG: cuándo utilizar cada uno

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Uno de los errores más comunes al diseñar aplicaciones con modelos de lenguaje consiste en utilizar indistintamente memoria, historial y RAG como si fueran mecanismos equivalentes.

Aunque los tres forman parte del contexto, **resuelven problemas completamente diferentes**. Elegir el componente incorrecto suele producir aplicaciones más costosas, menos precisas y difíciles de mantener.

---

# Tres componentes, tres responsabilidades

| Componente | Propósito principal | Duración |
|------------|---------------------|----------|
| Historial | Mantener el hilo de la conversación actual | Minutos u horas |
| Memoria | Recordar información útil entre conversaciones | Días, meses o años |
| RAG | Recuperar conocimiento externo actualizado | Bajo demanda |

Cada uno responde a una pregunta distinta.

- **Historial:** ¿Qué ocurrió en esta conversación?
- **Memoria:** ¿Qué conviene recordar del usuario o del sistema?
- **RAG:** ¿Qué conocimiento necesito consultar ahora?

---

# Ejemplo práctico

Un usuario pregunta:

> "Necesito continuar el informe que empezamos ayer."

La aplicación podría actuar de la siguiente manera:

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

# Errores frecuentes

## Guardar documentos completos en memoria

La memoria debe contener conocimiento persistente y estructurado, no grandes volúmenes de documentación.

## Usar el historial como base documental

El historial no reemplaza una base de conocimiento. A medida que crece, se vuelve costoso e ineficiente.

## Recuperar siempre los mismos documentos

El RAG debe recuperar únicamente la información relevante para la consulta actual.

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

- Mantener separados los tres mecanismos.
- Definir políticas de actualización independientes.
- Evitar duplicar información entre memoria y RAG.
- Auditar periódicamente qué información se incorpora al contexto.
- Priorizar calidad antes que cantidad.

---

# Resumen

Historial, memoria y RAG no compiten entre sí: se complementan. Una arquitectura de Context Engineering madura utiliza cada mecanismo para aquello que mejor sabe hacer, logrando asistentes más precisos, eficientes y fáciles de evolucionar.

En la próxima sección analizaremos el papel de las herramientas y los resultados de ejecución como parte de la anatomía del contexto.
