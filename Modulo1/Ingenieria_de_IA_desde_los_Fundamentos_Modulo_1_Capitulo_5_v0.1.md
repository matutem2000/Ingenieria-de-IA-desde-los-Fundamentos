# Ingeniería de IA desde los Fundamentos

# Módulo I --- Los Fundamentos de la Inteligencia Artificial

# Capítulo 5 --- Deep Learning

**Versión:** 0.1 (Primer borrador editorial)

------------------------------------------------------------------------

# Objetivos del capítulo

Al finalizar este capítulo deberías poder:

-   Explicar qué es Deep Learning y por qué surgió.
-   Diferenciar Machine Learning de Deep Learning.
-   Comprender el concepto de red neuronal sin recurrir a matemáticas
    avanzadas.
-   Entender por qué los datos y el hardware fueron claves para su
    desarrollo.
-   Saber cuándo Deep Learning aporta valor y cuándo no.

------------------------------------------------------------------------

# Introducción

En el capítulo anterior aprendimos que Machine Learning cambió la forma
de construir software: en lugar de programar reglas, los modelos
aprendían patrones a partir de datos.

Sin embargo, apareció un nuevo problema.

Muchos de los fenómenos del mundo real eran demasiado complejos para los
algoritmos tradicionales de Machine Learning.

Reconocer rostros, comprender lenguaje natural o interpretar imágenes
requería descubrir relaciones extremadamente complejas.

Así nació el impulso que dio origen al Deep Learning.

------------------------------------------------------------------------

# ¿Por qué "Deep"?

La palabra *Deep* significa "profundo".

No hace referencia a que el modelo sea más inteligente, sino a que
utiliza múltiples capas de procesamiento para transformar la
información.

Cada capa aprende representaciones progresivamente más abstractas.

Por ejemplo, en una fotografía:

-   Las primeras capas detectan bordes.
-   Las siguientes detectan formas.
-   Luego aparecen ojos, orejas o ruedas.
-   Finalmente el modelo identifica un perro, un automóvil o una
    persona.

El programador ya no describe esas características.

El modelo las descubre durante el entrenamiento.

------------------------------------------------------------------------

# La inspiración biológica

Las redes neuronales reciben ese nombre porque fueron inspiradas, de
manera muy simplificada, en el funcionamiento de las neuronas
biológicas.

No son un cerebro artificial.

No reproducen el funcionamiento del sistema nervioso.

Son modelos matemáticos que toman prestada una idea fundamental:

> Muchas unidades simples trabajando juntas pueden resolver problemas
> complejos.

Esta analogía ayuda a comprender el origen del concepto, pero no debe
interpretarse literalmente.

------------------------------------------------------------------------

# ¿Qué cambió respecto de Machine Learning?

Podemos resumir la diferencia así:

## Machine Learning clásico

El ingeniero suele definir manualmente muchas características relevantes
de los datos.

## Deep Learning

El propio modelo aprende automáticamente qué características son
importantes.

Este cambio redujo enormemente el trabajo manual en numerosos dominios.

------------------------------------------------------------------------

# ¿Por qué Deep Learning no apareció antes?

La idea existía desde hacía décadas.

Lo que faltaba era:

-   capacidad de procesamiento;
-   grandes volúmenes de datos;
-   hardware especializado (GPU);
-   mejores algoritmos de entrenamiento.

Cuando estos factores coincidieron, Deep Learning comenzó a superar
ampliamente a otros enfoques en múltiples tareas.

Una enseñanza importante es que la innovación tecnológica rara vez
depende de un único descubrimiento.

Generalmente requiere la convergencia de varias tecnologías.

------------------------------------------------------------------------

# Aplicaciones actuales

Deep Learning está presente en:

-   reconocimiento de imágenes;
-   reconocimiento de voz;
-   traducción automática;
-   vehículos autónomos;
-   diagnóstico por imágenes;
-   modelos de lenguaje;
-   generación de imágenes;
-   síntesis de audio.

En la práctica, gran parte de la IA generativa moderna está construida
sobre técnicas de Deep Learning.

------------------------------------------------------------------------

# Conversación con un arquitecto

**Director**

"Necesitamos Deep Learning."

**Arquitecto**

"¿Qué problema queremos resolver y qué datos tenemos disponibles?"

Deep Learning no es un objetivo.

Es una herramienta.

Su conveniencia depende del problema, los datos, el presupuesto y los
requisitos del negocio.

------------------------------------------------------------------------

# Ventajas

-   Excelente desempeño en problemas complejos.
-   Aprende representaciones automáticamente.
-   Escala muy bien con grandes cantidades de datos.
-   Es la base de los modelos generativos actuales.

# Desventajas

-   Requiere grandes volúmenes de datos.
-   Consume mucha capacidad de cómputo.
-   Puede resultar difícil de interpretar.
-   El entrenamiento suele ser costoso.

Estas limitaciones explican por qué no todos los proyectos necesitan
Deep Learning.

------------------------------------------------------------------------

# Relación jerárquica

``` text
Inteligencia Artificial
└── Machine Learning
    └── Deep Learning
        └── Transformers
            └── Large Language Models
```

Comprender esta estructura será fundamental para los capítulos
siguientes.

------------------------------------------------------------------------

# Caso aplicado

Imaginemos una empresa que desea detectar automáticamente defectos en
piezas industriales mediante fotografías.

Programar reglas para todas las posibles imperfecciones sería
prácticamente imposible.

Un modelo de Deep Learning entrenado con miles de imágenes etiquetadas
puede aprender patrones que un conjunto fijo de reglas difícilmente
capturaría.

Aquí Deep Learning aporta una ventaja clara.

------------------------------------------------------------------------

# Ideas clave

-   Deep Learning es una evolución de Machine Learning.
-   Aprende automáticamente representaciones complejas.
-   Su éxito depende tanto del algoritmo como de los datos y del
    hardware.
-   Es la base de los modelos modernos de IA generativa.

------------------------------------------------------------------------

# Laboratorio

1.  Elegí tres aplicaciones que utilicen imágenes, voz o lenguaje.
2.  Investigá si utilizan Deep Learning.
3.  Explicá qué problema resuelven y por qué un algoritmo tradicional
    tendría dificultades.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Más capas implican siempre mejores resultados?
-   ¿Qué ocurre si entrenamos con datos de baja calidad?
-   ¿Qué impacto tiene el hardware disponible sobre el rendimiento del
    modelo?

------------------------------------------------------------------------

# Resumen

Deep Learning permitió resolver problemas que durante muchos años
parecían inalcanzables para la informática tradicional.

Su capacidad para aprender representaciones complejas abrió el camino
hacia una nueva generación de modelos capaces de comprender imágenes,
voz y lenguaje natural.

Sin embargo, todavía existía un desafío importante: comprender
secuencias largas de texto de manera eficiente.

Ese problema dio origen a la arquitectura Transformer, protagonista del
próximo capítulo.

------------------------------------------------------------------------

# Lo que un arquitecto debería recordar

-   Deep Learning no reemplaza a Machine Learning; lo amplía.
-   No todo proyecto necesita redes profundas.
-   Los datos continúan siendo el recurso más valioso.
-   La elección tecnológica debe responder al problema y no a la moda.

------------------------------------------------------------------------

# Próximo capítulo

**Capítulo 6 --- Transformers**

Analizaremos la arquitectura que transformó definitivamente el
procesamiento del lenguaje natural y sentó las bases de ChatGPT, Claude,
Gemini y los modelos modernos.

> "Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones."
