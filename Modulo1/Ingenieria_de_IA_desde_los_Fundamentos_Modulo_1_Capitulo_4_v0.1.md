# Ingeniería de IA desde los Fundamentos

# Módulo I --- Los Fundamentos de la Inteligencia Artificial

# Capítulo 4 --- Machine Learning

**Versión:** 0.1 (Primer borrador editorial)

------------------------------------------------------------------------

# Objetivos del capítulo

Al finalizar este capítulo deberías ser capaz de:

-   Explicar qué es Machine Learning sin utilizar definiciones
    memorizadas.
-   Comprender por qué surgió este paradigma.
-   Diferenciar software tradicional de Machine Learning.
-   Identificar los principales tipos de aprendizaje.
-   Saber cuándo utilizar Machine Learning y cuándo no.
-   Entender por qué Machine Learning no es sinónimo de Inteligencia
    Artificial.

------------------------------------------------------------------------

# Introducción

Hasta ahora vimos que la Inteligencia Artificial nació como una
pregunta: ¿es posible construir una máquina capaz de realizar tareas que
asociamos con la inteligencia?

Durante muchos años el enfoque predominante consistió en escribir
reglas.

Si queríamos que un programa resolviera un problema, debíamos decirle
exactamente qué hacer en cada situación.

Este enfoque funcionó extraordinariamente bien para miles de
aplicaciones.

Sin embargo, comenzó a fallar cuando aparecieron problemas donde
escribir todas las reglas era prácticamente imposible.

Machine Learning nació como respuesta a esa limitación.

------------------------------------------------------------------------

# El problema de las reglas

Imaginemos que queremos desarrollar un sistema capaz de reconocer perros
en fotografías.

Podríamos intentar programar reglas como:

-   Tiene cuatro patas.
-   Tiene orejas.
-   Tiene cola.
-   Tiene hocico.

Pronto descubriríamos que esas reglas son insuficientes.

¿Qué ocurre si el perro está sentado?

¿O de espaldas?

¿O parcialmente oculto?

¿O es un cachorro?

Cada nueva excepción obliga a escribir más reglas.

Llega un punto en que el enfoque deja de ser sostenible.

Aquí aparece la pregunta que cambió la historia de la informática:

> ¿Y si, en lugar de programar las reglas, enseñáramos a la máquina
> mediante ejemplos?

------------------------------------------------------------------------

# Un cambio de paradigma

En el desarrollo tradicional el conocimiento reside en el código.

``` text
Datos + Reglas escritas por un programador → Resultado
```

En Machine Learning el conocimiento se obtiene a partir de los datos.

``` text
Datos + Respuestas correctas → Modelo

Modelo + Nuevos datos → Predicción
```

La diferencia parece pequeña, pero cambia completamente la manera de
construir software.

------------------------------------------------------------------------

# ¿Qué significa aprender?

En Machine Learning, aprender no significa comprender como un ser
humano.

Significa ajustar un modelo matemático para encontrar patrones útiles en
los datos.

Cuantos más ejemplos representativos recibe el modelo, mejor puede
generalizar frente a situaciones nuevas.

Aprender, en este contexto, consiste en reducir progresivamente el error
de las predicciones.

------------------------------------------------------------------------

# Los tres grandes tipos de aprendizaje

## Aprendizaje supervisado

Disponemos de ejemplos junto con la respuesta correcta.

Ejemplos:

-   Detectar spam.
-   Predecir precios.
-   Clasificar documentos.
-   Reconocer enfermedades a partir de estudios médicos.

## Aprendizaje no supervisado

No conocemos la respuesta correcta.

El objetivo consiste en descubrir estructuras o agrupamientos dentro de
los datos.

Ejemplos:

-   Segmentación de clientes.
-   Agrupamiento de documentos.
-   Detección de comportamientos similares.

## Aprendizaje por refuerzo

Un agente aprende interactuando con un entorno y recibiendo recompensas
o penalizaciones.

Ejemplos:

-   Robots.
-   Videojuegos.
-   Optimización de estrategias.

------------------------------------------------------------------------

# ¿Dónde aparece Machine Learning en tu trabajo?

Muchos sistemas modernos ya incorporan Machine Learning aunque no lo
percibamos.

-   Filtros de correo no deseado.
-   Motores de recomendación.
-   Detección de fraude.
-   OCR.
-   Traducción automática.
-   Predicción de demanda.
-   Asistentes virtuales.

Es importante comprender que Machine Learning es una herramienta para
resolver determinados problemas, no una solución universal.

------------------------------------------------------------------------

# Conversación con un arquitecto

**Cliente**

"Queremos usar IA porque está de moda."

**Arquitecto**

"¿Disponen de datos suficientes para entrenar o evaluar un modelo?"

Muchas iniciativas fracasan porque se piensa primero en la tecnología y
recién después en los datos.

En Machine Learning ocurre exactamente lo contrario.

Sin datos adecuados no existe aprendizaje útil.

------------------------------------------------------------------------

# Relación entre IA y Machine Learning

Una confusión muy frecuente consiste en utilizar ambos términos como
sinónimos.

No lo son.

Podemos imaginar la siguiente relación:

``` text
Inteligencia Artificial
│
├── Sistemas basados en reglas
├── Búsqueda y planificación
├── Sistemas expertos
├── Machine Learning
│      ├── Deep Learning
│      └── Modelos de Lenguaje
└── Otras técnicas
```

Machine Learning es una rama dentro de la Inteligencia Artificial.

Deep Learning es una rama dentro de Machine Learning.

Los LLM pertenecen a Deep Learning.

Comprender esta jerarquía evita muchas confusiones.

------------------------------------------------------------------------

# ¿Cuándo conviene utilizar Machine Learning?

Generalmente cuando:

-   Existen muchos ejemplos históricos.
-   Es difícil escribir reglas manualmente.
-   El problema cambia con el tiempo.
-   Los patrones son complejos.

No suele ser la mejor opción cuando:

-   Las reglas son simples y estables.
-   Existen pocos datos.
-   Se necesita una explicación completamente determinística.
-   El costo de equivocarse es extremadamente alto sin supervisión.

------------------------------------------------------------------------

# Caso aplicado

Supongamos que una empresa desea clasificar automáticamente reclamos.

Opción A:

Crear cientos de reglas manuales.

Opción B:

Entrenar un modelo utilizando miles de reclamos históricos correctamente
clasificados.

¿Cuál elegir?

La respuesta dependerá del volumen de datos, la estabilidad del dominio,
el costo del mantenimiento y la precisión requerida.

La tarea del arquitecto consiste en evaluar esas variables antes de
decidir.

------------------------------------------------------------------------

# Ideas clave

-   Machine Learning surge porque escribir reglas no siempre es posible.
-   Aprender significa ajustar un modelo a partir de datos.
-   Los datos son tan importantes como el algoritmo.
-   Machine Learning no reemplaza al software tradicional; lo
    complementa.

------------------------------------------------------------------------

# Laboratorio

1.  Elegí tres aplicaciones que utilices diariamente.
2.  Identificá si emplean reglas tradicionales o Machine Learning.
3.  Justificá tu respuesta.
4.  Pensá cómo las implementarías sin Machine Learning.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Puede existir Machine Learning sin datos?
-   ¿Más datos siempre implican mejores modelos?
-   ¿Qué riesgos aparecen cuando los datos contienen errores o sesgos?
-   ¿Qué impacto tendría esto en una organización?

Estas preguntas volverán a aparecer cuando estudiemos Deep Learning y
modelos de lenguaje.

------------------------------------------------------------------------

# Resumen

Machine Learning representó uno de los mayores cambios de paradigma en
la historia del desarrollo de software.

En lugar de describir el mundo mediante reglas escritas por un
programador, comenzó a aprender patrones a partir de ejemplos.

Ese cambio abrió el camino para Deep Learning, Transformers y los
modelos de lenguaje que estudiaremos en los próximos capítulos.

------------------------------------------------------------------------

# Lo que un arquitecto debería recordar

-   Comenzar por el problema.
-   Verificar si existen datos suficientes.
-   No utilizar Machine Learning cuando un algoritmo clásico resuelve el
    problema de forma más simple.
-   Comprender que un buen modelo nunca compensará datos de mala
    calidad.

------------------------------------------------------------------------

# Próximo capítulo

**Capítulo 5 --- Deep Learning**

Analizaremos por qué las redes neuronales profundas transformaron
Machine Learning y sentaron las bases de la IA moderna.

> "Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones."
