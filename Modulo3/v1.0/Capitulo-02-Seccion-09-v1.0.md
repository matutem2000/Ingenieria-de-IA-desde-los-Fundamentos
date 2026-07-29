# Capitulo-02-Seccion-09-v1.0

# Políticas, restricciones y seguridad del contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

En una aplicación empresarial no basta con proporcionar información al modelo. También es necesario definir **qué información puede utilizar**, **qué acciones están permitidas** y **qué límites nunca debe sobrepasar**.

Las políticas y restricciones forman parte del contexto porque condicionan directamente el comportamiento del modelo durante la inferencia.

---

# La seguridad comienza antes del LLM

Un error frecuente consiste en asumir que el modelo será quien haga cumplir las reglas de negocio.

En realidad, la responsabilidad principal recae sobre la aplicación.

Antes de construir el contexto deben verificarse:

- identidad del usuario;
- autenticación;
- autorización;
- pertenencia a una organización;
- permisos sobre los recursos solicitados.

El LLM debe recibir únicamente la información que el usuario está autorizado a conocer. Garantizar esto también protege frente a técnicas como el *prompt injection*, donde un atacante intenta manipular el comportamiento del modelo a través del contenido del contexto. Este tipo de ataques se analizará en profundidad en el Capítulo 14 (Seguridad, Gobernanza y Compliance).

---

# Tipos de restricciones

Una arquitectura profesional suele combinar distintos niveles de control:

## Restricciones funcionales

Determinan qué operaciones puede realizar el asistente.

Ejemplos:

- solo consulta;
- consulta y creación;
- aprobación de solicitudes.

## Restricciones de datos

Limitan qué información puede incorporarse al contexto.

Por ejemplo:

- expedientes de un organismo;
- tickets de un área;
- documentos clasificados.

## Restricciones de formato

Definen cómo debe responder el modelo.

Ejemplos:

- Markdown;
- JSON válido;
- tablas;
- lenguaje técnico.

---

# El principio del mínimo privilegio

Una regla ampliamente utilizada en ciberseguridad consiste en otorgar únicamente los permisos necesarios para realizar la tarea.

Aplicado al Context Engineering significa:

- recuperar solo los documentos necesarios;
- consultar únicamente las APIs requeridas;
- enviar al modelo la mínima cantidad de datos sensibles.

Reducir el contexto también reduce la superficie de exposición.

---

# Información sensible

Es recomendable evitar incorporar al contexto:

- contraseñas;
- claves API;
- secretos;
- tokens de autenticación;
- datos personales innecesarios;
- información financiera sin justificación.

Cuando estos datos sean imprescindibles, deben protegerse mediante controles adicionales definidos por la aplicación.

---

# Caso práctico

Supongamos un asistente de Recursos Humanos.

Dos usuarios realizan exactamente la misma consulta:

> "Mostrame el legajo de Juan Pérez."

Aunque el prompt sea idéntico, el contexto será diferente.

- Un analista de RR. HH. puede acceder al expediente completo.
- Un gerente puede visualizar solo determinados campos.
- Un empleado común no debería recibir información confidencial.

La diferencia no está en el modelo, sino en el contexto construido por la aplicación.

---

# Buenas prácticas

- Validar permisos antes de recuperar información.
- Evitar mezclar información de distintos niveles de confidencialidad en el mismo contexto.
- Revisar periódicamente las políticas de acceso a medida que el sistema evoluciona.

---

# Resumen

Las políticas y restricciones constituyen una capa esencial de la anatomía del contexto. Permiten adaptar el comportamiento del modelo a las reglas del negocio y proteger la información sensible antes de que llegue al LLM.

En la próxima sección integraremos todos los componentes estudiados para construir un modelo conceptual completo de la anatomía del contexto.
