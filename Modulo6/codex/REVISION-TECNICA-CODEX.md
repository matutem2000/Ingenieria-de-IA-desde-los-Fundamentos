# Revisión técnica y editorial — Módulo 6

## Dictamen

La cobertura de RAG es amplia y técnicamente útil. El principal riesgo editorial es convertir benchmarks, límites de producto y clasificaciones comerciales en reglas universales sin metodología reproducible.

## Hallazgos prioritarios

1. Toda cifra de latencia, escala o recuperación debe indicar hardware, corpus, dimensión, configuración, filtros y concurrencia.
2. Separar consistencia de la base, visibilidad del índice y frescura del pipeline; no son la misma propiedad.
3. Medir recuperación y generación por separado y luego evaluar el sistema de extremo a extremo.
4. Tratar permisos antes de recuperar, con pruebas explícitas contra filtraciones entre usuarios o clientes.
5. Evitar atribuir al proveedor de la base vectorial la retirada de un modelo de embeddings de otro proveedor.

## Correcciones producidas

Se generaron 60 versiones corregidas. Se reemplazaron comparaciones de latencia no reproducibles, absolutos sobre opciones de despliegue y una atribución incorrecta de obsolescencia de embeddings.

