# Módulo 10 – Capítulo 02 – Sección 02

# Self-service: diseñar para que los equipos puedan desplegar sin intervención del equipo de plataforma

El principio de self-service en una plataforma de IA establece que un equipo de AI Engineering debe poder pasar de un modelo entrenado a un endpoint de producción sin abrir un ticket, sin esperar aprobación manual de infraestructura, y sin necesitar conocimiento profundo de Kubernetes o cloud networking. Esto se implementa mediante "golden paths": flujos de trabajo predefinidos, probados y automatizados que cubren el 80% de los casos de uso, expuestos como comandos CLI (`platform deploy --model my_model:v2.1 --env prod`) o como templates de pipeline que el equipo completa con sus parámetros específicos. La automatización de self-service requiere guardrails técnicos integrados en el propio flujo: validaciones de seguridad de imágenes (Trivy o Snyk), tests de carga automáticos antes de promover a producción (Locust o k6), y gates de calidad de modelo que comparan métricas offline del nuevo modelo contra el modelo actualmente en producción antes de permitir el despliegue. En plataformas como Lyft o Spotify, el self-service redujo el tiempo de despliegue de semanas a horas, con el equipo de plataforma respondiendo a incidentes de la infraestructura en lugar de actuar como intermediario en cada despliegue.

## Aspectos técnicos del self-service

- CLI interno (Python + Click o Typer) que encapsula kubectl, helm, docker build y llamadas al model registry en un comando único con flags explícitos
- Templates de pipeline (Kubeflow Pipelines YAML o Prefect flows) con parámetros de input/output estandarizados y steps obligatorios de validación no bypasseables
- Portales de self-service: Backstage con Software Templates que generan scaffolding de proyectos con CI/CD preconfigurado y acceso al cluster de training
- Policy as Code: Open Policy Agent (OPA) o Kyverno validan cada recurso de Kubernetes que se despliega, rechazando configuraciones que violen las políticas de seguridad o de cuotas
- Runbooks automatizados: Ansible playbooks o scripts de remediación que los propios equipos pueden ejecutar para resolver los problemas más comunes sin escalar al equipo de plataforma

## Buena práctica

El self-service no significa ausencia de control: significa que los controles están integrados automáticamente en el camino de despliegue, de modo que cumplir las políticas es el camino de menor resistencia.
