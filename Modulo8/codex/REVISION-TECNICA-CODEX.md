# Revisión técnica y editorial — Módulo 8

## Dictamen

El contenido ofrece buena amplitud sobre modelos locales e infraestructura, pero concentra numerosas cifras volátiles de rendimiento, precio y capacidad. Sin fecha, configuración y fuente reproducible, esas cifras envejecen con rapidez.

## Hallazgos prioritarios

1. Convertir precios y benchmarks en ejemplos metodológicos, con fecha, región, versión, hardware y carga.
2. Separar tamaño de pesos, memoria de ejecución, caché KV y memoria temporal; “el modelo cabe” no implica que la carga sea viable.
3. Verificar licencias por modelo y versión; “pesos abiertos” no equivale a código abierto ni uso irrestricto.
4. No presentar Spot como obligatorio: depende de interrupciones, checkpoints, disponibilidad y costo de recuperación.
5. Evaluar calidad en el idioma y dominio reales después de cuantización y ajuste.

## Correcciones producidas

Se generaron 60 versiones corregidas. Se sustituyó una estimación puntual de costo/duración sin base suficiente y se reformuló la recomendación absoluta sobre instancias interrumpibles.

