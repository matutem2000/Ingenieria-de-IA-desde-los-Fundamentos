# Módulo 12 – Capítulo 06 – Sección 02

# CI/CD pipeline: build, test, evaluación y despliegue automatizado

El pipeline CI/CD del proyecto usa GitHub Actions con cuatro stages secuenciales: build, test, evaluate y deploy. El stage de build construye la imagen Docker, ejecuta un scan de vulnerabilidades con Trivy (bloqueando si hay CVE críticos) y publica la imagen en el registry privado con tags de commit SHA y de rama. El stage de test ejecuta: linting con ruff, type checking con mypy, unit tests con pytest (cobertura mínima 80%), integration tests sobre Qdrant de test y un smoke test de la API con el endpoint /health. El stage de evaluate es el diferenciador para sistemas de IA: ejecuta el subconjunto de evaluación continua del golden dataset (20 queries) y falla el pipeline si RAGAS faithfulness cae por debajo de 0.80 o si answer relevance cae por debajo de 0.75, bloqueando despliegues que degraden la calidad. El stage de deploy aplica los manifests de Kubernetes con kubectl apply y espera que el rollout complete antes de marcar el pipeline como exitoso.

## Etapas del pipeline CI/CD

- Build: docker buildx build con cache, trivy scan --severity CRITICAL (falla en CVE críticos), push a registry con tag SHA
- Test: ruff + mypy + pytest con cobertura >= 80% + integration tests sobre stack de test + smoke test de API
- Evaluate: RAGAS evaluation sobre 20 muestras del golden dataset; falla si faithfulness < 0.80 o answer_relevance < 0.75
- Deploy: kubectl apply --server-side con --force-conflicts, kubectl rollout status con timeout 10 minutos
- Notificación: Slack webhook con resultado del pipeline, métricas de evaluación y enlace a logs de Grafana

## Para recordar

El stage de evaluación automática en el pipeline CI/CD es lo que distingue el MLOps del DevOps para sistemas de IA — sin una puerta de calidad cuantitativa, los despliegues pueden degradar silenciosamente el comportamiento del modelo en producción.
