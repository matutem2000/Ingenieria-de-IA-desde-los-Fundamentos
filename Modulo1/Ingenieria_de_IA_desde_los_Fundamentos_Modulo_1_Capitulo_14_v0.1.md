# Ingeniería de IA desde los Fundamentos

# Módulo I --- Los Fundamentos de la Inteligencia Artificial

# Capítulo 14 --- Casos de Estudio

**Versión:** 0.1 (Primer borrador editorial)

------------------------------------------------------------------------

# Objetivos

Al finalizar este capítulo deberías poder:

-   Aplicar los conceptos estudiados a problemas reales.
-   Justificar técnicamente la elección de una solución basada en IA.
-   Identificar cuándo conviene utilizar un LLM, un RAG o un algoritmo
    tradicional.
-   Analizar ventajas, riesgos y limitaciones desde la perspectiva de un
    arquitecto.

------------------------------------------------------------------------

# Introducción

Hasta este punto hemos estudiado los fundamentos de la Inteligencia
Artificial.

Sin embargo, conocer conceptos no es suficiente.

El verdadero valor aparece cuando somos capaces de decidir qué
tecnología utilizar para resolver un problema concreto.

En este capítulo analizaremos distintos escenarios similares a los que
un profesional puede encontrar en una organización.

------------------------------------------------------------------------

# Caso 1 --- Chatbot para documentación interna

## Problema

Una empresa posee miles de documentos técnicos.

Los empleados tardan demasiado tiempo en encontrar información.

## Alternativas

### Opción A

Implementar un buscador tradicional.

### Opción B

Implementar un sistema RAG.

### Opción C

Entrenar un modelo propio.

## Análisis

En la mayoría de los casos, un sistema RAG ofrece el mejor equilibrio
entre costo, mantenimiento y calidad.

No es necesario volver a entrenar el modelo.

La documentación permanece actualizada y puede incorporarse
progresivamente.

------------------------------------------------------------------------

# Caso 2 --- Consulta a un Data Warehouse

## Problema

Los usuarios desean consultar información utilizando lenguaje natural.

Ejemplo:

> "Mostrame las ventas del último trimestre."

## Arquitectura sugerida

Usuario

↓

Aplicación

↓

LLM

↓

Generación de SQL

↓

Base de datos

↓

Validación

↓

Respuesta

## Riesgos

-   consultas incorrectas;
-   acceso a información sensible;
-   consultas costosas.

## Recomendaciones

-   limitar permisos;
-   validar SQL;
-   registrar auditorías;
-   definir reglas de seguridad.

------------------------------------------------------------------------

# Caso 3 --- Clasificación automática de documentos

## Problema

La organización recibe miles de documentos diariamente.

## Alternativas

-   reglas manuales;
-   Machine Learning;
-   LLM.

## Reflexión

No siempre el LLM representa la mejor alternativa.

En algunos casos un modelo de clasificación tradicional resulta más
económico y suficiente.

------------------------------------------------------------------------

# Caso 4 --- Asistente para desarrolladores

## Problema

El equipo necesita comprender proyectos grandes y generar código.

## Alternativas

-   ChatGPT;
-   Claude;
-   modelo local;
-   RAG con documentación propia.

## Arquitectura recomendada

LLM + documentación del proyecto + herramientas de búsqueda.

El valor no reside únicamente en el modelo.

La arquitectura completa determina el resultado.

------------------------------------------------------------------------

# Caso 5 --- Diagnóstico asistido

## Problema

Un profesional desea comparar un nuevo caso con diagnósticos históricos.

## Posible solución

-   embeddings;
-   búsqueda semántica;
-   recuperación de antecedentes;
-   LLM para elaborar una propuesta.

## Observación

El modelo no reemplaza al especialista.

Asiste el proceso de decisión.

------------------------------------------------------------------------

# Caso 6 --- Automatización de procesos

## Problema

Enviar automáticamente correos luego de determinadas acciones.

## ¿Conviene IA?

No.

Un flujo de automatización tradicional resulta suficiente.

Este ejemplo demuestra que no todo problema requiere Inteligencia
Artificial.

------------------------------------------------------------------------

# Conversación con un arquitecto

**Director**

"¿Cuál es el mejor modelo?"

**Arquitecto**

"No existe un mejor modelo universal. Existe un modelo más adecuado para
un problema determinado."

------------------------------------------------------------------------

# Ideas clave

-   El problema siempre precede a la tecnología.
-   La arquitectura completa importa más que el modelo aislado.
-   IA y software tradicional suelen convivir.
-   La decisión debe justificarse técnica y económicamente.

------------------------------------------------------------------------

# Actividad

Elegí un proyecto de tu organización.

Respondé:

1.  ¿Cuál es el problema?
2.  ¿Realmente requiere IA?
3.  ¿Qué arquitectura propondrías?
4.  ¿Qué riesgos existen?
5.  ¿Cómo medirías el éxito?

------------------------------------------------------------------------

# Caso integrador

Diseñá conceptualmente una solución para una organización que desea:

-   consultar documentación;
-   generar reportes;
-   acceder mediante lenguaje natural a información corporativa;
-   mantener privacidad de los datos.

No pienses primero en el modelo.

Pensá primero en la arquitectura.

------------------------------------------------------------------------

# Resumen

La diferencia entre un usuario y un arquitecto no consiste únicamente en
conocer más herramientas.

Consiste en saber justificar por qué una determinada tecnología resulta
adecuada para un problema específico.

Los casos analizados muestran que la Inteligencia Artificial forma parte
de una solución más amplia donde intervienen datos, procesos, seguridad,
infraestructura y software tradicional.

------------------------------------------------------------------------

# Lo que un arquitecto debería recordar

-   Comenzar siempre por el problema.
-   Evaluar varias alternativas.
-   Considerar costos y riesgos.
-   Diseñar la arquitectura completa antes de elegir el modelo.

------------------------------------------------------------------------

# Próximo capítulo

**Capítulo 15 --- Evaluación Final del Módulo I**

Integraremos todos los conceptos estudiados mediante preguntas de
reflexión, ejercicios y un caso práctico que servirá como punto de
partida para el Módulo II.

> "Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones."
