# Capítulo 04 — Sección 07

# Consolidación y olvido

Si solo diseñamos el lado de la captura y el almacenamiento, construimos sistemas de memoria que se degradan con el tiempo: acumulan ruido junto con la señal, mantienen información desactualizada con la misma prominencia que la información actual, y crecen sin control hasta que el costo de recuperación hace el sistema inviable.

El olvido deliberado no es una falla de diseño. Es una función de diseño. Los sistemas de memoria bien construidos saben no solo qué recordar sino cuándo y cómo olvidar.

Esta sección distingue tres fenómenos distintos que a veces se confunden bajo el mismo nombre: el olvido catastrófico de los modelos de aprendizaje continuo, la caducidad natural de la información, y el olvido deliberado por diseño de políticas de retención.

## El olvido catastrófico (y por qué no es nuestro problema principal aquí)

El olvido catastrófico es un fenómeno del entrenamiento de redes neuronales: cuando un modelo aprende nueva información, puede "sobreescribir" el conocimiento anterior de forma no controlada, degradando su desempeño en tareas previamente dominadas.

Es un problema activo de investigación en aprendizaje máquina, particularmente en escenarios de aprendizaje continuo (continual learning). Sin embargo, en el contexto del diseño de aplicaciones de IA que usan modelos preentrenados —que es el escenario de este libro—, el olvido catastrófico no aplica directamente: no estamos reentrenando el modelo, estamos diseñando el sistema de memoria externo que envuelve al modelo.

Lo mencionamos porque el término aparece frecuentemente en la literatura y puede crear confusión. El diseño de memorias de aplicación es un problema de ingeniería de sistemas, no de optimización de parámetros de red.

## La caducidad natural de la información

Toda información tiene una vida útil. Algunos hechos son permanentes o cambian muy lentamente: el sector industrial de una empresa, el idioma del usuario, las preferencias de formato de respuesta. Otros hechos son altamente volátiles: el proyecto activo del mes, el precio de un activo financiero, el estado de una tarea.

Un sistema de memoria que no distingue entre estos tipos de información produce comportamientos extraños:

- El sistema recuerda que el proyecto "Alpha" está en progreso, aunque ese proyecto cerró hace tres meses.
- El sistema recuerda que el usuario trabaja en la empresa X, aunque cambió de trabajo.
- El sistema usa datos de precios recuperados de una sesión antigua como si fueran actuales.

La caducidad natural se gestiona con dos mecanismos:

**TTL (Time To Live):** cada registro de memoria tiene una fecha de expiración automática. Cuando se alcanza esa fecha, el registro se elimina o se marca como inactivo. El TTL apropiado depende del tipo de información.

```
TIPOS DE INFORMACIÓN Y TTL SUGERIDOS:
- Preferencias de formato del usuario      → sin expiración (se actualiza por contradicción)
- Proyectos activos                        → 90 días desde última mención
- Precios, tasas, métricas cuantitativas  → 24-48 horas
- Estado de tareas en progreso             → 30 días
- Contactos y entidades nombradas          → 180 días sin confirmación
```

**Confianza decreciente:** en lugar de eliminar abruptamente, el sistema puede reducir gradualmente el score de relevancia de un registro con el tiempo. Un hecho que no ha sido confirmado en meses tiene menos peso en la recuperación que uno confirmado recientemente.

## El olvido deliberado: políticas de retención

El olvido deliberado va más allá de la caducidad automática: es el diseño explícito de políticas que determinan qué se guarda, durante cuánto tiempo y en qué condiciones.

Una política de retención bien diseñada responde a estas preguntas:

**¿Qué entra a la memoria persistente?**
Solo la información que supera un umbral de relevancia proyectada. No cada detalle de cada conversación, sino los elementos que tienen alta probabilidad de ser útiles en interacciones futuras.

**¿Qué se consolida?**
La consolidación es el proceso de comprimir múltiples memorias episódicas en una memoria semántica más compacta. En lugar de guardar diez registros que dicen "el usuario siempre añade contexto de costos", el sistema consolida esto en una sola entrada: `preferencia: incluir_análisis_de_costo = true, confianza: alta`.

La consolidación reduce el volumen de almacenamiento y mejora la precisión de la recuperación, pero requiere un proceso de inferencia que tiene costo computacional.

**¿Qué se elimina?**
- Información que ha sido explícitamente contradicha por información más reciente.
- Información que ha expirado su TTL sin confirmación.
- Información redundante (múltiples registros que dicen lo mismo).
- Información que el usuario ha solicitado eliminar (ver privacidad, más abajo).

**¿Qué se archiva en lugar de eliminarse?**
En algunos contextos —especialmente empresariales— la información no se elimina definitivamente sino que se archiva en un tier de almacenamiento de baja recuperabilidad. Esto permite auditoría sin contaminar la memoria activa.

## Olvido solicitado por el usuario: privacidad y GDPR

El olvido deliberado tiene una dimensión de privacidad que el ingeniero no puede ignorar.

Los usuarios tienen el derecho —legalmente reconocido en muchas jurisdicciones bajo GDPR, LGPD y regulaciones similares— de solicitar que un sistema elimine sus datos. En el contexto de sistemas de memoria de IA, esto significa que la aplicación debe ser capaz de localizar y eliminar completamente toda la información persistida sobre un usuario, a pedido.

Las implicancias de diseño son significativas:

**Toda memoria persistida debe estar identificada con el usuario al que pertenece.** Si la memoria está en una base de datos vectorial, cada vector debe tener metadatos de `user_id` para que puedan ser encontrados y eliminados.

**La eliminación debe ser completa.** No solo el perfil de usuario, sino todos los registros episódicos, todas las preferencias inferidas, todos los resúmenes de sesión. Si el sistema usa caching, los datos en caché también deben ser invalidados.

**El diseño debe prever esta operación desde el inicio.** Añadir un mecanismo de eliminación a un sistema que no fue diseñado para ello es mucho más costoso que incluirlo en el diseño original.

```python
def eliminar_memoria_usuario(user_id: str, colecciones: list[str]):
    """
    Elimina toda la memoria persistida de un usuario específico.
    Opera sobre todas las colecciones de memoria del sistema.
    """
    registros_eliminados = 0
    for coleccion in colecciones:
        resultado = coleccion.eliminar(filtro={"user_id": user_id})
        registros_eliminados += resultado.count
        registrar_auditoria(
            accion="eliminacion_por_solicitud",
            user_id=user_id,
            coleccion=coleccion.nombre,
            registros=resultado.count,
            timestamp=datetime.now()
        )
    return {"eliminados": registros_eliminados, "status": "completo"}
```

**Nota del arquitecto:** La conexión entre el diseño de memoria y la privacidad se desarrolla en mayor profundidad en el capítulo 14 (Seguridad y privacidad en sistemas de IA). Lo que aquí establecemos es la premisa de diseño: el olvido no es solo una función técnica de mantenimiento del sistema —es también un derecho del usuario que la arquitectura debe soportar.

## La memoria compartida entre agentes y el olvido coordinado

En sistemas multiagente —que desarrollaremos en el capítulo 09—, la memoria puede ser compartida entre múltiples agentes que trabajan en paralelo o en secuencia. Esto introduce una complejidad adicional: el olvido de un agente puede afectar la coherencia de otros agentes que dependen de la misma información.

El diseño de políticas de retención en sistemas multiagente requiere un mecanismo de coordinación: antes de eliminar un registro, el sistema debe verificar que ningún agente activo tiene una dependencia sobre ese registro. Esto puede implementarse con contadores de referencia o con un registro centralizado de dependencias.

El principio general es que el olvido en un sistema multiagente debe ser coordinado, no unilateral.

---

*La siguiente sección presenta las arquitecturas modernas de memoria que han emergido en los últimos años: frameworks como Mem0, patrones de MemGPT, y las implementaciones que los equipos de producción usan en la actualidad.*
