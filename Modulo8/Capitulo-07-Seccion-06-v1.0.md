# Módulo 8 – Capítulo 07 – Sección 06

# Cierre: la nube ofrece elasticidad; el hardware local ofrece latencia y privacidad

La dicotomía nube vs local en infraestructura GPU para LLMs no es una elección binaria sino una decisión de arquitectura que la mayoría de los productos maduros resuelve con un enfoque híbrido: hardware local para la carga base predecible y workloads sensibles a la privacidad, nube elástica para picos de demanda, entrenamiento y experimentación. Los hiperescaladores han respondido a la demanda de LLMs con instancias especializadas de H100 y A100 con mejor disponibilidad, pero sus precios on-demand siguen siendo prohibitivos para startups con volúmenes moderados; los proveedores especializados como Lambda Labs y RunPod han creado un nicho entre el hardware local y la nube de enterprise, ofreciendo GPU de alta gama a precios 2-3x menores que AWS. La decisión de infraestructura GPU debe revisarse cada 6-12 meses: los modelos de precios de los proveedores cambian, nuevas GPUs (H200, B200) llegan al mercado, y las necesidades del producto evolucionan en términos de throughput, latencia y privacidad. El AI Engineer que comprende en detalle los costos, las limitaciones técnicas y los trade-offs de cada opción puede diseñar una infraestructura que escala de manera rentable desde el primer usuario hasta millones, ajustando la mezcla de local/nube a medida que crece el producto.

## Idea central

La nube proporciona la elasticidad para escalar rápidamente sin inversión de capital, pero el hardware local, una vez amortizado, ofrece un costo marginal por token que ningún proveedor cloud puede igualar para workloads de alta utilización continua.

---

*"The cloud is just someone else's computer."* — Anonymous, axioma que captura la esencia del análisis costo-beneficio: la nube es infraestructura alquilada con premium de conveniencia, y la decisión de qué alquilar vs poseer es idéntica a la que las empresas han tomado con toda infraestructura durante décadas.
