# Capítulo 04 — Sección 04

# Memoria conversacional

La memoria conversacional es la forma más inmediata de memoria en un sistema de IA: es el registro de lo que ocurrió en la conversación actual. En los modelos de lenguaje, esa memoria existe naturalmente dentro de la ventana de contexto: mientras el historial de mensajes cabe en el contexto, el modelo tiene acceso a todo lo que se dijo.

El problema, como ya vimos en el módulo anterior, es que la ventana de contexto tiene un límite. Una conversación larga, con muchas preguntas y respuestas extensas, eventualmente supera ese límite. En ese punto, algo tiene que ceder: o se trunca el historial, o se comprime, o se diseña una estrategia deliberada de gestión.

Esta sección examina las estrategias de gestión de memoria conversacional, sus trade-offs y cuándo elegir cada una.

## Estrategia 1: Historial completo

La estrategia más simple es mantener el historial completo de la conversación dentro del contexto. Cada turno de la conversación —mensaje del usuario y respuesta del modelo— se agrega secuencialmente.

```
CONTEXTO = [system_prompt] + [turno_1] + [turno_2] + ... + [turno_N]
```

**Ventajas:**
- El modelo tiene acceso a toda la información de la conversación sin pérdida.
- La coherencia de la conversación es máxima.
- Sin costo adicional de procesamiento (no hay pasos intermedios de compresión o recuperación).

**Limitaciones:**
- El costo de tokens crece linealmente con la longitud de la conversación.
- Cuando se alcanza el límite de contexto, el sistema necesita truncar o la conversación falla.
- En conversaciones muy largas, el modelo puede tener dificultades para enfocarse en la información más reciente cuando está "enterrada" bajo mucho contexto anterior (el problema conocido como "lost in the middle").

**Cuándo usar esta estrategia:**
- Conversaciones cortas y acotadas (soporte técnico de primer nivel, consultas de información simple).
- Aplicaciones donde la conversación no se extiende más de 10-20 turnos.
- Contextos donde la precisión absoluta es crítica y cualquier pérdida de información es inaceptable.

## Estrategia 2: Ventana deslizante

La ventana deslizante mantiene solo los últimos N turnos de la conversación en el contexto. Cuando se agrega un nuevo turno, el turno más antiguo se elimina.

```
CONTEXTO = [system_prompt] + [turno_(N-k+1)] + ... + [turno_N]
```

**Ventajas:**
- El tamaño del contexto se mantiene controlado y predecible.
- El modelo siempre trabaja con la información más reciente.
- El costo de tokens es constante (no crece con la duración de la conversación).

**Limitaciones:**
- Los turnos que salen de la ventana se pierden por completo.
- Si se mencionó algo importante en el turno 3 y ahora estamos en el turno 25, esa información ya no existe para el modelo.
- Puede producir respuestas que ignoran contexto crítico establecido al inicio de la conversación.

**Cuándo usar esta estrategia:**
- Conversaciones de soporte donde cada consulta es relativamente autónoma.
- Aplicaciones donde el usuario rara vez necesita hacer referencia a información de muchos turnos atrás.
- Situaciones donde el costo es una restricción más importante que la completitud.

**Nota del arquitecto:** Una variante más refinada es la ventana deslizante con anclaje: además de los N turnos recientes, el sistema siempre incluye el primer turno (donde generalmente se establece el objetivo principal de la conversación) y cualquier turno marcado explícitamente como importante. Esta variante reduce significativamente el problema de pérdida de contexto inicial.

## Estrategia 3: Resumen progresivo

En lugar de descartar los turnos que salen de la ventana, el sistema los resume. El resumen reemplaza al historial completo como representación comprimida del contexto pasado.

```
CONTEXTO = [system_prompt] + [resumen_de_turnos_anteriores] + [turno_reciente_1] + ... + [turno_reciente_N]
```

**Ventajas:**
- Se preserva información de toda la conversación, aunque de forma comprimida.
- El tamaño del contexto se mantiene manejable.
- Los temas, acuerdos y decisiones clave sobreviven en el resumen.

**Limitaciones:**
- El proceso de resumen tiene costo (un LLM call adicional, o computación del proceso de summarización).
- Introduce latencia.
- El resumen puede perder detalles que luego resultan importantes.
- La calidad del resumen afecta directamente la calidad de las respuestas posteriores.

**Cuándo usar esta estrategia:**
- Conversaciones largas donde la coherencia a largo plazo es importante.
- Sesiones de trabajo extendidas (brainstorming, redacción colaborativa, análisis iterativo).
- Aplicaciones donde el usuario puede referirse a cosas dichas "antes" de forma indeterminada.

**Implementación práctica:**

El resumen puede generarse de dos formas:

*Resumen por umbral:* cuando el historial supera un número de tokens definido, se llama al LLM para que genere un resumen del historial anterior y se reemplaza ese historial con el resumen.

```python
def gestionar_historial(historial, umbral_tokens=3000):
    tokens_actuales = contar_tokens(historial)
    if tokens_actuales > umbral_tokens:
        turnos_a_resumir = historial[:-4]  # Conservar los últimos 4 turnos
        turnos_recientes = historial[-4:]
        resumen = generar_resumen(turnos_a_resumir)
        return [{"role": "system", "content": f"Resumen de la conversación anterior: {resumen}"}] + turnos_recientes
    return historial
```

*Resumen incremental:* después de cada turno, el sistema actualiza el resumen acumulativo. Es más costoso pero produce resúmenes más coherentes.

## Estrategia 4: Memoria conversacional híbrida

La estrategia más robusta para aplicaciones de producción combina las tres anteriores:

- Los últimos N turnos se mantienen como historial completo (máxima fidelidad para el contexto inmediato).
- Los turnos más antiguos se comprimen en un resumen (preservación de coherencia).
- Los elementos marcados como críticos (acuerdos, restricciones, objetivos) se extraen y almacenan en la memoria semántica persistente (disponibles en sesiones futuras).

```
CONTEXTO = [system_prompt]
         + [memoria_semántica_del_usuario]  ← recuperada del almacenamiento persistente
         + [resumen_de_turnos_anteriores]   ← generado en sesión
         + [historial_reciente]             ← últimos N turnos completos
```

Esta estrategia es la que usan los sistemas de agentes más maduros. Su costo es mayor —en latencia y en tokens—, pero es la única que combina coherencia a corto plazo, preservación a largo plazo y personalización entre sesiones.

## Comparación de estrategias

```
ESTRATEGIA         | COHERENCIA | COSTO     | COMPLEJIDAD | CASO DE USO TÍPICO
-------------------|------------|-----------|-------------|--------------------
Historial completo | Alta       | Alto      | Baja        | Chats cortos
Ventana deslizante | Media      | Bajo      | Baja        | Soporte básico
Resumen progresivo | Media-Alta | Medio     | Media       | Sesiones largas
Híbrida            | Alta       | Alto      | Alta        | Agentes de producción
```

---

*La siguiente sección aborda la memoria persistente: el mecanismo que permite que el sistema recuerde información entre sesiones distintas, construyendo un modelo acumulativo del usuario y del dominio de trabajo.*
