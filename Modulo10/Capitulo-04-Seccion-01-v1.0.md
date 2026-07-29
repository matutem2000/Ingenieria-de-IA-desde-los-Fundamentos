# Módulo 10 – Capítulo 04 – Sección 01

# Feature store: repositorio centralizado de features para modelos de ML y IA

Un feature store es un sistema de datos especializado que resuelve dos problemas críticos de los proyectos de ML a escala: la duplicación de lógica de transformación de features entre equipos, y la inconsistencia entre las features usadas en entrenamiento y las disponibles en inferencia en producción (el problema training-serving skew). La arquitectura de un feature store se divide en dos almacenes complementarios: el almacén offline (Parquet sobre S3 o Delta Lake en Databricks) que contiene el historial completo de features con point-in-time correctness para entrenamiento sin data leakage, y el almacén online (Redis Cluster, DynamoDB, o Bigtable) que contiene la versión más reciente de cada feature para inferencia en tiempo real con latencias de sub-milisegundo. La lógica de transformación de features (transformaciones de pandas, SQL, o Spark) se define una sola vez en el feature store con un contrato explícito (nombre, tipo, descripción, owner) y se reutiliza por todos los modelos que necesiten esa feature, eliminando la necesidad de que cada equipo reimplemente la misma lógica de ingeniería de features con riesgo de divergencia. Empresas como Uber (Michelangelo), Twitter (Cortex), y Airbnb (Zipline) documentaron que sus feature stores redujeron el tiempo de desarrollo de nuevos modelos en un 30-50% al permitir reutilizar features ya calculadas.

## Componentes principales de un feature store

- Feature definitions: especificación declarativa de cada feature con nombre, tipo (float32, int64, string), descripción, owner, TTL en el almacén online, y transformación de cálculo
- Offline store: almacén columnar con historial temporal completo; soporta point-in-time joins para construir training sets sin data leakage usando el timestamp exacto de cada evento
- Online store: almacén de baja latencia (Redis, DynamoDB) para inferencia en tiempo real; sincronizado automáticamente desde el offline store por un job de materialización programado
- Feature registry: catálogo de todas las features disponibles con metadatos, ejemplos y estadísticas de distribución; el punto de descubrimiento para que los equipos encuentren features existentes antes de crear nuevas
- Materialización: proceso de pipeline que calcula y escribe las features desde las fuentes de datos al offline store, y luego las sincroniza al online store según la frecuencia definida (cada hora, diariamente)

## Para recordar

El valor de un feature store no es técnico sino organizacional: centralizar la lógica de features evita que diez equipos calculen la misma feature de diez formas ligeramente distintas con resultados potencialmente distintos.
