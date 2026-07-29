# Capitulo-03-Seccion-03-v1.0

# Cómo funciona la tokenización

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Antes de que un modelo pueda interpretar una solicitud, debe convertir el texto en una representación que pueda procesar matemáticamente. Ese proceso se conoce como **tokenización**.

La tokenización transforma una secuencia de caracteres en una secuencia de tokens, que posteriormente serán convertidos en identificadores numéricos (IDs) y, finalmente, en vectores utilizados durante la inferencia.

---

# Del texto al modelo

De forma simplificada, el recorrido de una consulta es el siguiente:

```text
Texto del usuario
        │
        ▼
 Tokenizador
        │
        ▼
 Secuencia de tokens
        │
        ▼
 IDs numéricos
        │
        ▼
 Embeddings
        │
        ▼
 Modelo de lenguaje
```

El modelo nunca "lee" palabras directamente. Todo el procesamiento ocurre sobre representaciones numéricas.

---

# ¿Por qué no se utilizan palabras?

Podría parecer más sencillo dividir el texto por espacios, pero ese enfoque presenta numerosos problemas:

- palabras compuestas;
- distintos idiomas;
- errores ortográficos;
- abreviaturas;
- emojis;
- signos de puntuación;
- nombres propios.

Los tokenizadores modernos utilizan algoritmos que encuentran unidades reutilizables para representar eficientemente millones de textos diferentes.

---

# Diferentes modelos, diferentes tokenizadores

Cada familia de modelos suele incorporar su propio tokenizador.

Como consecuencia:

- un mismo párrafo puede generar cantidades distintas de tokens;
- el costo de procesarlo puede variar;
- la ventana de contexto efectiva también puede cambiar.

Por este motivo, las estimaciones de consumo deben realizarse sobre el modelo concreto que utilizará la aplicación.

---

# Ejemplo conceptual

Supongamos la palabra:

> internacionalización

Un tokenizador podría dividirla en varias partes reutilizables, mientras que otro podría representarla con una combinación completamente diferente.

El objetivo no es preservar las palabras originales, sino obtener una representación eficiente para el aprendizaje y la inferencia.

---

# Implicancias para el ingenieros de IA

Comprender la tokenización permite:

- estimar con mayor precisión el consumo de contexto;
- diseñar prompts más eficientes;
- reducir costos de operación;
- evitar superar el límite de la ventana de contexto.

Aunque normalmente no será necesario implementar un tokenizador, sí resulta esencial conocer su impacto sobre la arquitectura.

---

# Buenas prácticas

- Medir el consumo de tokens durante el desarrollo.
- No asumir equivalencias entre palabras y tokens.
- Probar el comportamiento con el modelo definitivo.
- Evitar incorporar información redundante al contexto.

---

# Resumen

La tokenización constituye el primer paso del procesamiento de cualquier modelo de lenguaje. Convertir correctamente el texto en tokens permite representar información compleja de forma eficiente y determina, en gran medida, el costo y la capacidad de una aplicación basada en LLM.

En la próxima sección analizaremos cómo evolucionaron las ventanas de contexto y qué capacidades ofrecen los modelos modernos.
