# Módulo 12 – Capítulo 10 – Sección 02

# Checklist de producción: verificaciones obligatorias antes de considerar el sistema listo

El checklist de producción del proyecto final es una lista de 30 verificaciones agrupadas en seis categorías que el equipo debe completar antes del primer despliegue a producción. La categoría de seguridad incluye: secrets no presentes en el código ni en archivos commiteados (verificado con git-secrets o detect-secrets), scan de vulnerabilidades Trivy con 0 CVEs críticos en la imagen Docker, red teaming completado con tasa de bypass < 5%, y validación de que los JWT se verifican correctamente con la clave pública del identity provider. La categoría de calidad incluye: RAGAS faithfulness >= 0.82 sobre el golden dataset completo, task completion rate >= 75% en el golden dataset agéntico, y test de regresión verde en el pipeline CI/CD. La categoría de operabilidad incluye: health check `/health` responde en < 200ms, graceful shutdown implementado (SIGTERM + 30s drain), restart automático ante crash verificado en prueba manual, y runbook revisado por un ingeniero que no lo escribió.

## Checklist de producción por categoría

- Seguridad (8 items): sin secrets en código, Trivy 0 CVEs críticos, red teaming < 5% bypass, JWT validado, rate limiting activo
- Calidad (6 items): faithfulness >= 0.82, task completion >= 75%, RAGAS pipeline en CI verde, golden dataset actualizado
- Rendimiento (5 items): latencia P95 < 3s bajo carga de 50 usuarios, throughput >= 20 req/s, costo/req documentado
- Operabilidad (6 items): health check < 200ms, graceful shutdown, restart automático, runbook revisado por tercero
- Observabilidad (3 items): dashboard operativo con 4 paneles mínimo, alertas críticas configuradas, trazas visibles en Grafana Tempo
- Documentación (2 items): README con setup funcional verificado por nuevo ingeniero, API documentada con ejemplos

## Para recordar

El checklist de producción no es opcional — es el contrato del equipo consigo mismo sobre qué significa que el sistema está listo para producción, y su valor aumenta con cada incidente post-despliegue que lo hubiera prevenido.
