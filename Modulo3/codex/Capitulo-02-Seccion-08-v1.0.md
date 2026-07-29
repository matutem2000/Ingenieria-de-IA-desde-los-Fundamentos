# Capitulo-02-Seccion-08-v1.0

# Herramientas como parte del contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Los primeros modelos de lenguaje solo podían responder utilizando la información con la que habían sido entrenados y el contexto recibido. Hoy, los LLM modernos pueden interactuar con herramientas externas para consultar información, ejecutar acciones y enriquecer el contexto antes de producir una respuesta.

En Context Engineering, las herramientas no son un complemento: forman parte de la arquitectura del contexto.

---

# ¿Qué entendemos por herramienta?

Una herramienta es cualquier mecanismo externo que permite al modelo obtener información o ejecutar una acción que no puede realizar por sí mismo.

Ejemplos habituales:

- APIs REST;
- bases de datos;
- sistemas ERP y CRM;
- motores de búsqueda;
- servicios de correo electrónico;
- calendarios;
- repositorios de documentos;
- sistemas de tickets.

El modelo no accede directamente a estos recursos. Es la aplicación la que ejecuta la herramienta y devuelve el resultado al contexto.

---

# Flujo de trabajo

Una interacción típica sigue este esquema:

```text
Usuario
   │
   ▼
Aplicación
   │
   ├── Detecta la necesidad de usar una herramienta
   ▼
API / Base de datos / Servicio
   │
   ▼
Resultado
   │
   ▼
Contexto actualizado
   │
   ▼
LLM
   │
   ▼
Respuesta final
```

El dato importante es que el modelo razona sobre el **resultado** de la herramienta, no sobre la herramienta en sí.

---

# Ejemplo

Un usuario pregunta:

> "¿Cuántos incidentes críticos siguen abiertos?"

El modelo no conoce esa información.

La aplicación:

1. consulta el sistema de tickets;
2. obtiene el listado actualizado;
3. incorpora el resultado al contexto;
4. solicita al LLM que genere una respuesta comprensible.

---

# Herramientas versus conocimiento

Una herramienta responde preguntas sobre el estado actual del mundo.

Un documento RAG responde preguntas sobre conocimiento.

Por ejemplo:

- Manual de uso → RAG.
- Estado de un ticket → Herramienta.
- Política institucional → RAG.
- Cantidad de usuarios activos → Herramienta.

Comprender esta diferencia evita arquitecturas innecesariamente complejas.

---

# Errores frecuentes

- Enviar resultados excesivamente largos al modelo.
- No validar errores devueltos por una API.
- Confiar ciegamente en información incompleta.
- Ejecutar herramientas cuando el contexto ya contiene la respuesta.

Cada llamada tiene un costo y un impacto sobre la latencia.

---

# Buenas prácticas

- Recuperar únicamente la información necesaria.
- Normalizar los resultados antes de enviarlos al LLM.
- Registrar el origen de los datos.
- Manejar adecuadamente errores y tiempos de espera.
- Evitar consultas redundantes.

---

# Nota del arquitecto

Las herramientas no reemplazan al modelo y el modelo no reemplaza a las herramientas.

Una arquitectura profesional combina ambos componentes para aprovechar las fortalezas de cada uno.

---

# Resumen

Las herramientas permiten que un modelo interactúe con sistemas externos y trabaje con información actualizada. Sus resultados pasan a formar parte del contexto y amplían significativamente las capacidades de una solución basada en IA.

En la próxima sección estudiaremos cómo la seguridad, las políticas y las restricciones también forman parte de la anatomía del contexto y condicionan el comportamiento del modelo.
