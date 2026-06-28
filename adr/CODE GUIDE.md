# CODE_GUIDE.md

# Guía para el Desarrollo de Código
**Proyecto:** Ingeniería de IA desde los Fundamentos

**Versión:** 1.0

---

# Objetivo

Definir los estándares para todo el código fuente incluido en el libro.

El código no debe ser solamente funcional.

Debe ser una herramienta didáctica.

El lector debe comprender:

- qué hace;
- por qué fue construido de esa manera;
- qué alternativas existen;
- cuáles son sus limitaciones.

---

# Filosofía

El código debe enseñar.

No impresionar.

Siempre debe privilegiarse la claridad antes que la complejidad.

Un ejemplo sencillo correctamente explicado tiene mucho más valor que un ejemplo sofisticado difícil de comprender.

---

# Principios

Todo ejemplo debe ser:

- Correcto.
- Ejecutable.
- Reproducible.
- Minimalista.
- Comentado cuando aporte valor.
- Fácil de modificar.

---

# Tecnologías oficiales del proyecto

Siempre que sea posible, los ejemplos utilizarán tecnologías ampliamente difundidas.

## Backend

- Python
- .NET
- Node.js

## Frontend

- HTML
- CSS
- JavaScript
- TypeScript

## IA

- Ollama
- OpenAI API
- Anthropic API
- Gemini API
- LangChain (cuando sea apropiado)
- LlamaIndex (cuando aporte valor)

## Infraestructura

- Docker
- Docker Compose

Más adelante se incorporarán ejemplos con Kubernetes, MCP, agentes y herramientas de observabilidad.

---

# Organización del código

Cada ejemplo deberá tener una estructura similar a la siguiente:

```text
proyecto/

README.md

src/

tests/

requirements.txt
```

Cuando corresponda incluir Docker:

```text
Dockerfile

docker-compose.yml
```

---

# Convenciones

## Variables

Utilizar nombres descriptivos.

Correcto:

```python
customer_name
```

Incorrecto:

```python
cn
```

---

## Funciones

Cada función debe realizar una única tarea.

Evitar funciones extremadamente largas.

---

## Comentarios

Los comentarios deben explicar decisiones.

No describir literalmente el código.

Incorrecto:

```python
x = x + 1
# suma uno
```

Correcto:

```python
# Se incrementa el contador para evitar procesar nuevamente el mismo documento.
```

---

# Ejemplos progresivos

Los ejemplos deben crecer en complejidad.

Nivel 1

Concepto mínimo.

Nivel 2

Caso práctico.

Nivel 3

Caso empresarial.

---

# Calidad

Todo ejemplo debe:

- funcionar;
- ser probado;
- utilizar buenas prácticas;
- evitar código obsoleto.

---

# Anti-patrones

Evitar:

- código innecesariamente complejo;
- copiar ejemplos sin explicación;
- variables con nombres ambiguos;
- dependencias innecesarias;
- configuraciones difíciles de reproducir.

---

# Casos empresariales

Siempre que sea posible, los ejemplos estarán inspirados en escenarios reales.

Por ejemplo:

- RAG documental.
- Chat corporativo.
- Consulta SQL mediante lenguaje natural.
- Clasificación de documentos.
- Automatización empresarial.
- Agentes con herramientas.
- Integración mediante APIs.

---

# Revisión

Antes de incorporar un ejemplo verificar:

- ¿Compila?
- ¿Se ejecuta?
- ¿Está explicado?
- ¿Tiene README?
- ¿Puede reproducirse?
- ¿Ayuda a comprender el concepto?

Si alguna respuesta es negativa, el ejemplo no debe incorporarse al libro.

---

# Historial

## v1.0

Creación inicial del CODE_GUIDE.
