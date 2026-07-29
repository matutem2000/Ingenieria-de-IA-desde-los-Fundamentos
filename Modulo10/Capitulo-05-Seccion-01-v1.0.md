# Módulo 10 – Capítulo 05 – Sección 01

# Model drift: data drift vs concept drift y cómo detectarlos estadísticamente

El drift de modelos en producción se manifiesta en dos formas fundamentalmente distintas que requieren respuestas diferentes: el data drift ocurre cuando la distribución de los inputs (features de entrada) cambia respecto a la distribución que el modelo vio durante el entrenamiento, manteniendo constante la relación entre inputs y outputs, mientras que el concept drift ocurre cuando la relación subyacente entre inputs y outputs cambia aunque la distribución de inputs permanezca estable. Un ejemplo concreto: en un modelo de recomendación de e-commerce, el data drift ocurre cuando los usuarios cambian sus patrones de búsqueda (ej. post-pandemia), y el concept drift ocurre cuando los mismos comportamientos de usuario que antes predecían compra ahora predicen solo browse sin compra (porque cambió la economía o la competencia). La detección estadística del data drift usa tests como Kolmogorov-Smirnov para features continuas (compara la CDF de la distribución actual vs la de referencia), Chi-squared para features categóricas, y el Population Stability Index (PSI), donde PSI < 0.1 indica no drift, 0.1-0.2 indica drift moderado, y > 0.2 indica drift severo que requiere reentrenamiento. El concept drift es más difícil de detectar porque requiere ground truth (labels reales) que en muchos casos llegan con delay: se detecta monitoreando las métricas de calidad del modelo (accuracy, F1, AUC-ROC) calculadas sobre datos etiquetados con ventana deslizante.

## Conceptos clave de detección de drift

- Data drift (covariate shift): cambio en P(X) con P(Y|X) estable; detectable estadísticamente comparando distribuciones de features entre producción y datos de entrenamiento de referencia
- Concept drift: cambio en P(Y|X) independiente de cambios en P(X); detectable solo con ground truth mediante ventanas deslizantes de métricas de calidad (accuracy rolling 7-day, 30-day)
- Label drift (prior probability shift): cambio en P(Y) sin cambio en P(X|Y); detectable en modelos de clasificación monitoreando la distribución de las predicciones del modelo en producción
- KS-test implementation: para cada feature continua, calcular la estadística D = max|F1(x) - F2(x)| y el p-value; alertar cuando p-value < 0.05 en N features simultáneas (ajustando por Bonferroni)
- Ventanas de detección: drift de corto plazo (últimas 24h vs referencia) para detectar cambios abruptos, y drift de largo plazo (último mes vs referencia de 6 meses atrás) para detectar deriva gradual

## Para recordar

El data drift puede detectarse sin ground truth comparando distribuciones de inputs, pero el concept drift requiere inevitablemente labels reales: diseñar el sistema de captura de feedback (human-in-the-loop o labels implícitos) desde el inicio es tan importante como el modelo en sí.
