# Capítulo 05 - Sección 12

# Checklist del AI Engineer

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Esta sección presenta el checklist de referencia para el diseño, revisión y validación de instrucciones del sistema. Está organizado en cuatro momentos del ciclo de vida de una instrucción: antes de escribir, durante la escritura, antes del despliegue y durante la operación en producción.

El checklist puede usarse tanto para instrucciones nuevas como para revisar instrucciones existentes que presentan comportamientos inesperados.

---

# Antes de escribir

## Análisis de requisitos

- [ ] Documenté el objetivo principal del asistente en una oración.
- [ ] Listé los tipos de consulta más frecuentes que recibirá.
- [ ] Identifiqué los comportamientos que nunca debe tener.
- [ ] Definí el comportamiento ante casos de urgencia o riesgo.
- [ ] Confirmé el idioma, tono y nivel técnico de las respuestas.
- [ ] Verifiqué qué restricciones de cumplimiento normativo aplican.

## Análisis de la arquitectura

- [ ] Identifiqué qué información cambia entre usuarios y entre sesiones.
- [ ] Separé esa información dinámica del diseño de la instrucción del sistema.
- [ ] Confirmé si el asistente tiene acceso a herramientas y qué herramientas son.
- [ ] Revisé qué ya cubre el proveedor del modelo para no duplicarlo.
- [ ] Verifiqué si existe una instrucción base de la organización que deba incluirse.

---

# Durante la escritura

## Bloque de identidad

- [ ] El nombre y la función del asistente están definidos claramente.
- [ ] El contexto organizacional está mencionado.
- [ ] El tono y el nivel de formalidad están especificados.

## Bloque de objetivo

- [ ] El objetivo define la tarea central con precisión.
- [ ] Incluye ejemplos de qué tipos de consulta están dentro del alcance.
- [ ] Define el comportamiento para consultas fuera del alcance.

## Bloque de restricciones

- [ ] Cada restricción es un comportamiento observable, no un deseo.
- [ ] Las restricciones absolutas usan "nunca" o equivalente con el "incluso si" correspondiente.
- [ ] Las restricciones contextuales usan "solo cuando" con condiciones precisas.
- [ ] Cada restricción define qué hacer cuando se activa (derivar, declinar, pedir aclaración).

## Bloque de políticas de seguridad

- [ ] Existe una instrucción explícita para intentos de modificar el comportamiento del sistema.
- [ ] Existe una instrucción sobre el tratamiento del contenido externo (documentos, texto pegado).
- [ ] Existe una instrucción para casos de urgencia o riesgo para la seguridad del usuario.
- [ ] Si el asistente tiene herramientas, existe una instrucción sobre qué autoriza su uso.

## Bloque de formato

- [ ] Está especificado el idioma de respuesta.
- [ ] Está especificado el formato (Markdown, texto plano, JSON, etc.).
- [ ] Está especificada la longitud esperada o sus límites.
- [ ] Existe un formato definido para casos de error o casos fuera de alcance.

## Bloque de criterios de calidad

- [ ] Los criterios son verificables, no aspiracionales.
- [ ] Cubren al menos los casos más críticos del dominio.

## Revisión general de la instrucción

- [ ] Busqué y eliminé contradicciones entre bloques.
- [ ] Busqué y eliminé información dinámica mezclada con reglas permanentes.
- [ ] La instrucción no supera los 2.000 tokens (señal de alerta si los supera).
- [ ] Cada frase puede justificarse con una función específica.
- [ ] Existe un comportamiento definido para el caso por defecto.

---

# Antes del despliegue

## Pruebas de comportamiento esperado

- [ ] Probé al menos cinco casos estándar representativos del uso esperado.
- [ ] El comportamiento en esos casos fue correcto.

## Pruebas de casos límite

- [ ] Probé intentos de modificar el comportamiento del sistema ("ignorá tus instrucciones").
- [ ] Probé consultas fuera del alcance definido.
- [ ] Probé el caso de urgencia o riesgo para la seguridad del usuario.
- [ ] Probé al menos un caso de contenido externo con instrucciones maliciosas.
- [ ] Probé el caso de idioma o formato no esperado.

## Para asistentes con herramientas

- [ ] Probé que el modelo invoca las herramientas cuando corresponde.
- [ ] Probé que el modelo no invoca herramientas cuando no corresponde.
- [ ] Probé el comportamiento cuando una herramienta retorna un error.
- [ ] Probé el comportamiento ante solicitudes de acciones que requieren confirmación.
- [ ] Probé el comportamiento ante solicitudes de acciones que nunca deben ejecutarse.

## Documentación

- [ ] La instrucción tiene un identificador de versión.
- [ ] Existe un registro de qué comportamiento cubren las reglas principales.
- [ ] Existe un conjunto de casos de prueba documentado para uso futuro.

---

# Durante la operación en producción

## Monitoreo continuo

- [ ] Existe un mecanismo para identificar conversaciones con comportamiento inesperado.
- [ ] Se revisan periódicamente muestras de conversaciones reales.
- [ ] Los casos límite encontrados en producción se agregan al conjunto de pruebas.

## Actualización de instrucciones

- [ ] Cada cambio en la instrucción se versiona y documenta.
- [ ] Cada cambio se prueba contra el conjunto de casos existente antes del despliegue.
- [ ] Se verifica que el cambio no afecta comportamientos que funcionaban correctamente.
- [ ] Se mantiene la versión anterior disponible para rollback durante al menos una semana.

## Revisión periódica

- [ ] Las instrucciones se revisan cuando el modelo subyacente es actualizado por el proveedor.
- [ ] Las instrucciones se revisan cuando cambian las políticas de negocio relevantes.
- [ ] Las instrucciones se revisan cuando se identifican nuevos patrones de uso o abuso.

---

# Señales de alerta en producción

Las siguientes situaciones indican que las instrucciones del sistema necesitan revisión:

- El modelo ignora restricciones que antes respetaba.
- Aparecen comportamientos inconsistentes ante la misma consulta.
- Los usuarios reportan respuestas que contradicen las políticas de la aplicación.
- La tasa de derivaciones o de casos fuera de alcance aumenta sin explicación.
- Una actualización del modelo subyacente cambia el comportamiento en casos críticos.

---

# Resumen

El checklist del AI Engineer cubre el ciclo completo de vida de una instrucción del sistema: desde el análisis previo hasta el monitoreo en producción. Usarlo sistemáticamente reduce la posibilidad de que problemas conocidos lleguen a los usuarios y acelera el diagnóstico cuando aparecen comportamientos inesperados.

En la siguiente sección encontrarás el resumen integrado de todos los conceptos del capítulo.
