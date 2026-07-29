# Introducción a las ventanas de contexto

> Módulo 3 — Context Engineering Profesional

---

# Objetivos del capítulo

En este capítulo aprenderemos a:

- comprender cómo miden los modelos el contexto;
- interpretar el concepto de token;
- optimizar el uso de la ventana disponible;
- aplicar técnicas de compresión y resumido;
- diseñar aplicaciones escalables para conversaciones y documentos extensos.

---

# ¿Qué es una ventana de contexto?

Todo modelo de lenguaje posee un límite en la cantidad de información que puede procesar simultáneamente. Ese límite recibe el nombre de **ventana de contexto**.

Dentro de esa ventana conviven todos los elementos que el modelo necesita para generar una respuesta:

- instrucciones del sistema;
- historial conversacional;
- memoria recuperada;
- documentos obtenidos mediante RAG;
- resultados de herramientas;
- mensaje actual del usuario.

La capacidad de diseñar y administrar este espacio es una de las competencias centrales del Context Engineering.

---

# Una analogía útil

Imagine un escritorio de trabajo.

Solo puede colocar una cantidad limitada de documentos sobre él. Si incorpora demasiadas hojas, deberá retirar algunas, resumir otras o reorganizar el espacio disponible.

La ventana de contexto funciona de manera similar: el modelo únicamente puede "ver" aquello que entra dentro de su capacidad máxima.

---

# ¿Por qué es importante?

Una gestión inadecuada de la ventana puede provocar:

- pérdida de información relevante;
- respuestas inconsistentes;
- aumento del costo por consulta;
- mayor latencia;
- degradación del rendimiento.

En aplicaciones empresariales, estos problemas suelen aparecer mucho antes de alcanzar el límite máximo de tokens.

---

# ¿Qué ocupa espacio?

No solo el mensaje del usuario consume tokens.

También ocupan espacio:

- las instrucciones del sistema;
- los ejemplos (few-shot);
- el historial;
- la memoria;
- los documentos recuperados;
- las respuestas previas del modelo.

Por este motivo, ampliar el contexto sin una estrategia suele empeorar los resultados.

---

# Resumen

La ventana de contexto representa uno de los recursos más valiosos de cualquier LLM. Administrarla correctamente es tan importante como elegir el modelo adecuado.

En la próxima sección estudiaremos qué es un token y cómo influye en el funcionamiento interno de los modelos de lenguaje.
