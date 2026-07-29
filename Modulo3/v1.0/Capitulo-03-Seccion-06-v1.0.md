# Técnicas de resumido y compresión del contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Las aplicaciones modernas no esperan a que la ventana se llene para actuar. Implementan estrategias de compresión progresiva que mantienen el contexto dentro de límites operativos sin sacrificar la continuidad de la conversación.

Resumir no es perder información: es preservar lo esencial eliminando lo prescindible. La calidad de un resumen depende tanto del algoritmo utilizado como del criterio empleado para decidir qué merece conservarse.

---

# Cinco técnicas de compresión

## 1. Resumen extractivo

El resumen extractivo selecciona y conserva fragmentos completos del texto original —frases o párrafos— ordenándolos para construir una versión más corta sin modificar su redacción.

**Cuándo utilizarlo:** cuando la fidelidad literal importa y no se puede permitir que el resumen reformule o interprete el contenido. Útil para contratos, especificaciones técnicas y declaraciones formales.

**Limitaciones:** puede resultar redundante si los fragmentos seleccionados se solapan, y su resultado puede ser difícil de leer si los fragmentos pertenecen a partes distantes del texto original.

## 2. Resumen abstractivo

El resumen abstractivo genera nuevas oraciones que capturan el significado del texto original sin copiar fragmentos. El modelo interpreta, reordena y reformula para producir una versión más concisa.

**Cuándo utilizarlo:** cuando se necesita reducir significativamente la longitud del contexto y se acepta cierto grado de interpretación. Adecuado para resumir conversaciones, reuniones o sesiones de trabajo.

**Limitaciones:** puede introducir imprecisiones o perder matices que sí estaban en el original. Requiere validar la calidad del resumen, especialmente en dominios técnicos.

## 3. Resumen jerárquico

El resumen jerárquico organiza el contenido en niveles: primero resume bloques pequeños, luego agrupa esos resúmenes en bloques más grandes, repitiendo el proceso hasta obtener una versión manejable.

**Cuándo utilizarlo:** cuando el volumen de texto es muy grande —documentos extensos, sesiones de muchos días— y un resumen plano perdería demasiado detalle. Permite mantener múltiples niveles de granularidad.

**Limitaciones:** más costoso en términos computacionales y de tokens de procesamiento. Requiere una estructura lógica en el texto original para que los niveles resulten coherentes.

## 4. Resumen incremental

El resumen incremental actualiza un resumen existente cada vez que se incorporan nuevos mensajes, en lugar de regenerarlo desde cero.

El proceso es sencillo: al finalizar cada turno de conversación, se envía el resumen anterior junto con los nuevos intercambios y se genera una versión actualizada que reemplaza a la anterior.

**Cuándo utilizarlo:** en conversaciones largas de sesión continua donde es necesario mantener el estado actualizado sin reprocessar toda la historia.

**Limitaciones:** si el resumen base tiene errores, estos se propagan y pueden amplificarse. Conviene auditar el resumen periódicamente, no solo actualizarlo.

## 5. Compresión semántica

La compresión semántica elimina tokens de baja información —repeticiones, frases de relleno, saludos, cortesías— preservando el contenido semántico esencial. En su forma más sofisticada, puede reescribir oraciones completas para expresar el mismo significado con menos tokens.

**Cuándo utilizarlo:** cuando las instrucciones del sistema o los documentos recuperados son verbosos y contienen información secundaria que no aporta al razonamiento del modelo.

**Limitaciones:** requiere criterio para decidir qué es "baja información". Una compresión agresiva puede eliminar contexto que resulta relevante en situaciones inesperadas.

---

# Criterio de selección

La elección de la técnica depende de tres variables:

| Variable | Pregunta orientadora |
|---|---|
| Fidelidad requerida | ¿El modelo necesita las palabras exactas del original? |
| Volumen de texto | ¿Cuánto hay que reducir y en cuántas iteraciones? |
| Frecuencia de actualización | ¿El resumen se genera una vez o se actualiza continuamente? |

En la práctica, las arquitecturas maduras combinan varias técnicas: resumen incremental para el historial conversacional, resumen jerárquico para bases documentales, y compresión semántica para el system prompt.

---

# Buenas prácticas

- Resumir antes de alcanzar el límite, no en reacción a él.
- Validar periódicamente la calidad del resumen enviando al modelo preguntas de verificación sobre el contenido resumido.
- Conservar siempre hechos, decisiones adoptadas y compromisos asumidos; son los datos de mayor valor en cualquier conversación.
- Eliminar redundancias antes de aplicar cualquier técnica de resumen: un texto limpio produce mejores resúmenes.
- Documentar la estrategia de resumido en el código, especificando qué se conserva, qué se descarta y con qué frecuencia se actualiza.

---

# Resumen

Elegir la técnica de compresión correcta es una decisión de diseño que afecta la calidad de las respuestas, el costo operativo y la continuidad de la experiencia del usuario. No existe una técnica universalmente superior: la elección depende del tipo de contenido, la frecuencia de actualización y el nivel de fidelidad requerido.

En la próxima sección estudiaremos estrategias concretas para optimizar el consumo total de tokens a lo largo de toda la arquitectura de la aplicación.
