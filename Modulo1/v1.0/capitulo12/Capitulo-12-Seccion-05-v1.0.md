# Capitulo-12-Seccion-05-v1.0

# Capítulo 12 --- Mitos sobre la Inteligencia Artificial

**Versión:** 1.0\
**Estado:** Aprobado

> *"La mejor solución no es la que utiliza más recursos, sino la que
> resuelve el problema con el menor costo y la mayor confiabilidad."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Comprender por qué un modelo de mayor tamaño no siempre produce la
    mejor solución.
-   Analizar el equilibrio entre capacidad, costo, latencia y precisión.
-   Incorporar criterios para seleccionar modelos en arquitecturas
    empresariales.
-   Evitar decisiones basadas únicamente en el tamaño del modelo.

------------------------------------------------------------------------

# El mito: "El modelo más grande siempre es el mejor"

Una idea frecuente consiste en asumir que la elección del modelo debe
realizarse únicamente observando el número de parámetros.

Aunque los modelos de mayor tamaño suelen exhibir mejores capacidades
generales, esa característica no implica que constituyan la mejor
alternativa para todos los escenarios.

Desde una perspectiva de ingeniería, la pregunta correcta no es cuál
modelo es más potente, sino cuál resuelve el problema con el nivel de
calidad requerido y el menor costo operativo posible.

------------------------------------------------------------------------

# Ingeniería basada en restricciones

Toda arquitectura debe equilibrar múltiples variables.

Entre ellas:

-   precisión;
-   latencia;
-   costo por inferencia;
-   consumo de memoria;
-   consumo energético;
-   disponibilidad;
-   privacidad;
-   facilidad de despliegue.

En muchos escenarios un modelo pequeño especializado ofrece mejores
resultados prácticos que un modelo generalista considerablemente más
grande.

  Escenario                        Modelo recomendado
  -------------------------------- --------------------------
  Clasificación simple             Modelo pequeño
  Extracción de entidades          Modelo pequeño o mediano
  Asistente documental con RAG     Modelo mediano
  Análisis complejo multidominio   Modelo grande
  Uso local sin GPU                Modelo optimizado

``` mermaid
flowchart LR
A[Problema] --> B[Requisitos]
B --> C[Costo]
B --> D[Latencia]
B --> E[Precisión]
C --> F[Selección del modelo]
D --> F
E --> F
```

------------------------------------------------------------------------

# Caso de estudio

Una empresa decide reemplazar un modelo local de 8 mil millones de
parámetros por uno de más de 70 mil millones.

La calidad mejora ligeramente, pero el tiempo de respuesta se duplica y
el costo mensual de infraestructura aumenta varias veces.

Tras analizar el comportamiento real de los usuarios, la organización
descubre que el modelo anterior satisfacía el 98 % de las consultas.

La decisión final consiste en mantener el modelo pequeño para la
operación diaria y derivar únicamente los casos complejos al modelo de
mayor capacidad.

La arquitectura híbrida obtiene mejores resultados funcionales y
económicos.

------------------------------------------------------------------------

# Buenas prácticas

-   Definir métricas antes de seleccionar un modelo.
-   Medir calidad sobre datos reales del negocio.
-   Evaluar el costo total de operación.
-   Diseñar arquitecturas que permitan reemplazar modelos sin modificar
    la aplicación.

------------------------------------------------------------------------

# Errores frecuentes

  Error                                        Consecuencia
  -------------------------------------------- -----------------------------
  Elegir el modelo más grande por defecto      Costos innecesarios
  Ignorar la latencia                          Mala experiencia de usuario
  No medir calidad                             Decisiones subjetivas
  Acoplar la aplicación a un único proveedor   Baja flexibilidad

------------------------------------------------------------------------

# Ideas clave

-   Más parámetros no garantizan una mejor solución.
-   La selección del modelo constituye una decisión arquitectónica.
-   Optimizar implica equilibrar rendimiento, costo y mantenibilidad.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección analizaremos otro mito habitual: la creencia de
que basta con incorporar Inteligencia Artificial para que un proyecto
tenga éxito.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
