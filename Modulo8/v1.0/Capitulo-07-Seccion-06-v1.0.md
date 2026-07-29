# Módulo 8 – Capítulo 07 – Sección 06

## Cierre: la nube ofrece elasticidad; el hardware local ofrece latencia y privacidad

La dicotomía nube vs local en infraestructura GPU para LLMs no es una elección binaria sino una decisión de arquitectura que la mayoría de los productos maduros resuelve con un enfoque híbrido: hardware local para la carga base predecible y workloads sensibles a la privacidad, nube elástica para picos de demanda, entrenamiento y experimentación. Este enfoque combina las ventajas de ambos: el costo marginal bajo del hardware propio amortizado para el tráfico constante, con la elasticidad on-demand de la nube para las variaciones que el hardware local no puede absorber sin sobredimensionamiento.

Los hiperescaladores han invertido masivamente en infraestructura GPU para responder a la demanda de LLMs, mejorando la disponibilidad de instancias H100 y A100 en múltiples regiones. Sin embargo, sus precios on-demand siguen siendo sustancialmente más altos que los de los proveedores especializados para el mismo hardware, y la complejidad del modelo de costos (precios de instancia + almacenamiento + egress de datos + servicios gestionados) puede hacer que la factura real sea significativamente más alta que el precio de la instancia sola. Los proveedores especializados como Lambda Labs y RunPod han creado un nicho efectivo entre el hardware local y la nube enterprise, con precios 2-4x menores que los hiperescaladores para GPUs de alta gama y sin el ecosistema de servicios integrados que la mayoría de los equipos de ML no necesita.

El AI Engineer que comprende en detalle los costos, limitaciones técnicas y trade-offs de cada opción puede diseñar una infraestructura que escala de manera rentable desde el primer usuario hasta millones, ajustando la mezcla local/nube a medida que crece el producto. El momento de comenzar con solo nube (cuando el volumen no justifica la inversión en hardware) y el momento de añadir hardware local (cuando el break-even está claro con el volumen actual) son decisiones que deben tomarse con los números reales del análisis de costo-rendimiento del Capítulo 4, no con intuiciones o modas del sector.

La decisión de infraestructura GPU también debe revisarse periódicamente. Los precios de los proveedores cambian con la disponibilidad de hardware; nuevas generaciones de GPUs (H200, Blackwell B200) cambian los ratios de precio/rendimiento; y las necesidades del producto evolucionan en términos de throughput, latencia y privacidad. Una arquitectura que era óptima hace seis meses puede no serlo hoy. Establecer un proceso trimestral de revisión de la infraestructura GPU —con los números actuales de volumen de peticiones, costos de instancias y opciones de hardware disponibles— es una práctica de ingeniería que previene la acumulación de deuda de infraestructura.

## Idea central

La nube proporciona la elasticidad para escalar rápidamente sin inversión de capital, pero el hardware local, una vez amortizado, ofrece un costo marginal por token que ningún proveedor cloud puede igualar para workloads de alta utilización continua.

---

*"The cloud is just someone else's computer."* — Anonymous, axioma que captura la esencia del análisis costo-beneficio: la nube es infraestructura alquilada con premium de conveniencia, y la decisión de qué alquilar vs poseer es idéntica a la que las empresas han tomado con toda infraestructura durante décadas.
