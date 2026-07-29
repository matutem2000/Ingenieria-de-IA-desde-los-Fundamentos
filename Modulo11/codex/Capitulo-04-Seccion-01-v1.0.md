# Módulo 11 – Capítulo 04 – Sección 01

# Modelos de tenancy: silo, pool y bridge — trade-offs de aislamiento y costo

El diseño de multi-tenancy para plataformas de IA enterprise debe elegir explícitamente entre tres modelos fundamentales que representan diferentes puntos en el espectro entre máximo aislamiento y máxima eficiencia de costos: el modelo Silo, el modelo Pool, y el modelo Bridge. En el modelo Silo, cada tenant opera con infraestructura completamente dedicada — cluster de Kubernetes propio, base de datos vectorial propia, instancia de LLM propia si se usan modelos open-source self-hosted — lo que garantiza el máximo aislamiento técnico y facilita los acuerdos de nivel de servicio individualizados por tenant, pero multiplica los costos de infraestructura por el número de tenants y complica operacionalmente el mantenimiento al requerir actualizar N instancias independientes cuando se despliega una nueva versión. En el modelo Pool, todos los tenants comparten la misma infraestructura con aislamiento lógico implementado a nivel de aplicación mediante tenant IDs, row-level security en bases de datos, y namespace-level isolation en la base de datos vectorial: maximiza la eficiencia de costos y simplifica las operaciones, pero el riesgo de cross-tenant data leakage es más alto y un tenant que genera carga excesiva puede degradar la experiencia de todos los demás (el problema del "noisy neighbor"). El modelo Bridge combina ambos: infraestructura compartida (pool) para los tenants estándar con silo dedicado para tenants Premium o Enterprise que requieren garantías de aislamiento más estrictas o tienen contratos de cumplimiento que lo exigen.

## Trade-offs de cada modelo de tenancy

- Modelo Silo: aislamiento total (red, datos, computo), SLOs independientes por tenant, y cumplimiento simplificado; costo: N veces el costo de un tenant único, complejidad operacional proporcional al número de tenants
- Modelo Pool: infraestructura compartida con reducción de costos del 70-80% respecto al silo; riesgo: implementación incorrecta del aislamiento lógico puede resultar en cross-tenant data access, el fallo más grave en multi-tenancy
- Modelo Bridge (tiered): pool para tier Standard con límites de uso, silo optional para tier Enterprise con garantías adicionales — permite monetizar el nivel de aislamiento como feature de producto
- Noisy neighbor problem en pool: un tenant que ejecuta queries vectoriales masivos puede saturar el índice compartido; mitigado con rate limiting por tenant y prioridad de queue por tier de servicio
- Decisión de migración entre modelos: comenzar con pool para los primeros 10-20 tenants y planificar la migración a bridge cuando algún tenant supere el 20% del consumo total de recursos del pool

## Principio rector

El modelo de tenancy no es solo una decisión de arquitectura técnica sino un compromiso que impacta el modelo de precios del producto, los acuerdos de cumplimiento con los clientes, y la complejidad operacional del equipo de plataforma.
