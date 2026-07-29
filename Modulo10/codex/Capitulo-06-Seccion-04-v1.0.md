# Módulo 10 – Capítulo 06 – Sección 04

# Pipeline testing: validar cada etapa antes de promover a producción

El testing de pipelines de MLOps adopta las prácticas de testing de software (unit, integration, end-to-end) adaptadas a las características específicas de los sistemas de ML: los datos no son fixtures estáticos sino distribuciones variables, los modelos tienen comportamiento probabilístico no determinista, y las métricas de calidad tienen umbrales relativos en lugar de valores exactos. Los unit tests en un pipeline de MLOps validan cada función de transformación de datos y feature engineering de forma aislada con inputs sintéticos: `assert transform_user_age(birthdate=date(1990,1,1)) == 35`, `assert feature_encoding(category="unknown") == 0` (el valor esperado para categorías fuera del vocabulario de entrenamiento). Los integration tests validan que las etapas del pipeline se conectan correctamente entre sí: que el schema de output de la etapa de features coincide con el schema de input esperado por el training step, que el modelo registrado en el registry tiene el formato correcto para ser cargado por el serving layer, y que el endpoint desplegado retorna respuestas con el schema correcto. Los model validation tests son específicos de ML: comparar las métricas offline del modelo candidato contra el modelo champion (accuracy, F1, RMSE), ejecutar tests de invarianza (la predicción no debe cambiar significativamente si se perturban features irrelevantes), y tests de fairness (la métrica de calidad no debe diferir más del umbral permitido entre subgrupos protegidos).

## Tipos de tests en pipelines de MLOps

- Data validation tests: validaciones de Great Expectations ejecutadas automáticamente en el step de ingesta; el pipeline falla si el schema cambia inesperadamente o si la tasa de nulos supera el umbral
- Feature engineering unit tests: tests de PyTest que validan cada función de transformación con inputs caso límite (valores nulos, strings vacíos, valores fuera de rango esperado) de forma aislada
- Model evaluation tests: comparación automática de métricas del modelo candidato vs champion; el gate de calidad rechaza el modelo si accuracy_new < accuracy_champion * 0.99 o si cualquier métrica de fairness cae por debajo del umbral
- Serving compatibility tests: verificar que el modelo serializado puede ser cargado por el serving layer (KServe, Triton) sin errores, y que el endpoint retorna respuestas bien formadas para inputs de ejemplo
- Load tests pre-producción: tests de carga con Locust o k6 sobre el staging endpoint para verificar que el modelo cumple los SLOs de latencia bajo la carga máxima esperada antes de promocionar a producción

## Para recordar

En un pipeline de MLOps, las pruebas rápidas y deterministas deben ejecutarse en CI. Las pruebas que requieren GPU, grandes datos o servicios externos siguen siendo valiosas, pero conviene aislarlas en etapas reproducibles con una frecuencia y un entorno acordes con su costo: todos los tests críticos deben poder ejecutarse en un entorno reproducible y aislado.
