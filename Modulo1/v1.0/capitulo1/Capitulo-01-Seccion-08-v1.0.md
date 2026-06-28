# Capítulo 1 --- Sección 08 de 10

# El ciclo de vida de un sistema de Inteligencia Artificial

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Entrenar un modelo es un evento. Mantener un sistema de IA es un
> proceso continuo."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender las etapas que atraviesa un sistema de IA desde su
    concepción hasta su operación.
-   Diferenciar el ciclo de vida de un modelo del ciclo de vida de una
    aplicación tradicional.
-   Identificar los desafíos que aparecen una vez que el sistema entra
    en producción.
-   Comprender por qué la mejora continua forma parte del diseño
    arquitectónico.

------------------------------------------------------------------------

# Introducción

Cuando un equipo desarrolla una aplicación tradicional, suele pensar en
un flujo relativamente conocido: analizar requisitos, desarrollar,
probar, desplegar y mantener.

Los proyectos de Inteligencia Artificial comparten muchas de esas
etapas, pero incorporan otras que resultan críticas.

Un sistema de IA no solo depende del código. También depende de los
datos, del modelo, de su comportamiento frente a situaciones nuevas y de
la evolución constante del contexto donde opera.

Por esa razón, el trabajo no termina cuando la aplicación llega a
producción.

En muchos casos, allí recién comienza.

------------------------------------------------------------------------

# Una visión de extremo a extremo

De forma simplificada, un sistema de IA atraviesa las siguientes etapas:

1.  Definición del problema.
2.  Obtención y evaluación de los datos.
3.  Selección del enfoque técnico.
4.  Entrenamiento o integración del modelo.
5.  Validación funcional y técnica.
6.  Despliegue.
7.  Monitoreo.
8.  Mejora continua.

Cada una de estas fases puede requerir equipos, herramientas y métricas
diferentes.

------------------------------------------------------------------------

# Diagrama general

``` mermaid
flowchart LR

A[Problema] --> B[Datos]
B --> C[Modelo]
C --> D[Validación]
D --> E[Producción]
E --> F[Monitoreo]
F --> G[Mejora Continua]
G --> B
```

El diagrama muestra una diferencia importante respecto del software
clásico.

El proceso no termina en producción.

Existe un ciclo permanente de observación y ajuste.

------------------------------------------------------------------------

# El problema del cambio

Supongamos que una organización desarrolla un clasificador automático de
correos electrónicos.

Durante los primeros meses el sistema obtiene excelentes resultados.

Sin embargo, con el paso del tiempo los usuarios comienzan a escribir de
otra manera, aparecen nuevos productos y cambian los procesos internos.

Aunque el modelo no haya sufrido modificaciones, su desempeño comienza a
deteriorarse.

Este fenómeno recibe distintos nombres según el contexto, pero todos
reflejan una misma realidad: el mundo cambia y los modelos deben
adaptarse.

------------------------------------------------------------------------

# Monitorear también es diseñar

Un arquitecto no solo diseña cómo funcionará un sistema.

También diseña cómo sabrá si dejó de funcionar correctamente.

Algunas preguntas habituales son:

-   ¿Cómo mediremos la calidad de las respuestas?
-   ¿Qué indicadores observaremos?
-   ¿Cómo detectaremos una degradación?
-   ¿Cuándo será necesario actualizar el modelo?
-   ¿Quién aprobará esos cambios?

Estas decisiones deben formar parte del diseño desde el inicio del
proyecto.

------------------------------------------------------------------------

# Caso real

Una empresa implementa un asistente para responder consultas sobre su
catálogo de productos.

El sistema funciona correctamente durante varios meses.

Luego se incorpora una nueva línea de productos y se modifican los
nombres comerciales existentes.

Las respuestas comienzan a perder precisión.

El problema no es un error del modelo.

El conocimiento disponible ya no representa la realidad actual de la
organización.

Una arquitectura bien diseñada contempla mecanismos para actualizar
información, medir el desempeño y validar nuevamente el sistema.

------------------------------------------------------------------------

# Resumen

La Ingeniería de IA no finaliza con el despliegue de un modelo.

Los sistemas inteligentes evolucionan junto con el negocio y con los
datos que los alimentan.

Comprender su ciclo de vida permite construir soluciones sostenibles y
preparadas para el cambio.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
