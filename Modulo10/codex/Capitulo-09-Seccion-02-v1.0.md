# Módulo 10 – Capítulo 09 – Sección 02

# Chargeback y showback: asignar costos de plataforma a los equipos que los generan

Chargeback y showback son dos modelos de atribución de costos de infraestructura a los equipos consumidores que difieren en si el costo es real (chargeback: el presupuesto del equipo se carga con el costo real) o informativo (showback: el equipo ve cuánto está consumiendo pero no se le cobra internamente). En el contexto de una plataforma de IA, el chargeback requiere instrumentación técnica precisa: cada recurso de cómputo (Pod de Kubernetes, EC2 instance, GPU hour) debe estar etiquetado con el equipo y proyecto propietario, cada llamada al LLM Gateway registra el equipo y proyecto en el audit log, y un servicio de billing interno consolida esa información para generar facturas internas periódicas (mensuales o trimestrales). La implementación de chargeback en Kubernetes requiere herramientas como Kubecost (que calcula el costo por namespace, deployment y pod usando los precios reales de instancia del cloud provider) o OpenCost (la versión open source mantenida por la CNCF), que se integran con AWS Cost Explorer o GCP Billing API para obtener los precios de los nodos del cluster. El showback es un paso previo frecuente antes del chargeback completo: primero se da visibilidad a los equipos sobre su consumo sin consecuencias presupuestarias (showback), se establece la cultura de responsabilidad de costos, y después se activa el chargeback real cuando los equipos ya entienden cómo su comportamiento afecta el gasto.

## Aspectos técnicos del chargeback para plataformas de IA

- Resource tagging strategy: convención obligatoria de tags en todos los recursos cloud: `team`, `project`, `environment`, `cost_center`; validado en el pipeline de CI/CD y rechazado si los tags están ausentes o incorrectos
- Kubecost / OpenCost: herramienta que calcula el costo por namespace de Kubernetes basándose en precios reales de instancia EC2/GKE, incluyendo CPU, memoria y GPU; integrable con los sistemas de billing interno
- LLM cost attribution: el LLM Gateway registra en cada request el `project_id` y `team_id`; un job de agregación diario calcula el costo total por proyecto usando la tabla de precios del proveedor y produce el reporte de showback/chargeback
- Internal billing system: sistema (puede ser tan simple como una hoja de cálculo generada automáticamente o un sistema interno complejo) que consolida los datos de Kubecost, LLM Gateway y storage billing para producir el estado de cuenta mensual por equipo
- Budget alerts: umbrales de gasto configurables por equipo que disparan notificaciones automáticas a Slack cuando el consumo alcanza el 80% del presupuesto mensual asignado, con datos granulares de qué está generando el gasto

## Buena práctica

Comenzar con showback antes de implementar chargeback permite a los equipos ajustar sus patrones de consumo sin la presión de consecuencias presupuestarias inmediatas, resultando en una adopción más orgánica de las prácticas de eficiencia de costos.
