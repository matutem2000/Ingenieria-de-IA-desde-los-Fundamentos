# Capitulo-03-Seccion-02-v1.0

# Tokens: la unidad fundamental del contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Cuando hablamos de una ventana de contexto de 128.000, 200.000 o un millón de tokens, no nos referimos a palabras ni a caracteres. Los modelos de lenguaje trabajan con una unidad propia denominada **token**.

Comprender qué es un token y cómo se contabiliza es imprescindible para diseñar aplicaciones eficientes.

---

# ¿Qué es un token?

Un token es la unidad mínima de información que procesa un modelo de lenguaje.

Dependiendo del idioma y del texto, un token puede representar:

- una palabra completa;
- parte de una palabra;
- un signo de puntuación;
- un número;
- un espacio;
- incluso un carácter individual.

Por esta razón, no existe una conversión exacta entre palabras y tokens.

---

# Un ejemplo sencillo

Considere la siguiente frase:

> "La inteligencia artificial transforma organizaciones."

Aunque contiene solo cinco palabras, el modelo podría dividirla en varios tokens adicionales según el algoritmo de tokenización utilizado.

Dos modelos distintos incluso pueden producir cantidades diferentes de tokens para el mismo texto.

---

# ¿Qué consume tokens?

Dentro de una solicitud al modelo consumen tokens:

- instrucciones del sistema;
- ejemplos (few-shot);
- historial conversacional;
- memoria recuperada;
- documentos RAG;
- resultados de herramientas;
- mensaje del usuario;
- respuesta generada por el modelo.

Es un error habitual pensar que únicamente cuenta el mensaje del usuario.

---

# Tokens de entrada y de salida

Conviene distinguir dos conceptos:

## Tokens de entrada

Son todos los tokens enviados al modelo como contexto.

## Tokens de salida

Son los tokens utilizados para construir la respuesta.

Muchos proveedores facturan ambos valores por separado.

---

# ¿Por qué importan?

El número de tokens influye directamente en:

- el costo de cada consulta;
- la velocidad de respuesta;
- el consumo de recursos;
- la cantidad de información disponible para el razonamiento.

Una aplicación bien diseñada optimiza el uso de los tokens en lugar de intentar ocupar toda la ventana disponible.

---

# Buenas prácticas

- Eliminar información redundante.
- Resumir conversaciones extensas.
- Recuperar únicamente documentos relevantes.
- Evitar ejemplos innecesarios.
- Medir periódicamente el consumo de tokens.

---

# Resumen

Los tokens constituyen la unidad básica con la que trabajan los modelos de lenguaje. Todo lo que incorporamos al contexto se transforma en tokens y compite por un espacio limitado dentro de la ventana de contexto.

En la próxima sección estudiaremos cómo los modelos tokenizan el texto y por qué diferentes proveedores pueden producir cantidades distintas de tokens para el mismo contenido.
