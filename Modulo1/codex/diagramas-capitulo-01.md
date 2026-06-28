# Diagramas — Capítulo 1

**Capítulo:** 1 — ¿Qué entendemos por inteligencia?  
**Versión:** v0.5  
**Archivo relacionado:** `Modulo1/codex/capitulo-01-v0.5.md`

---

## Diagrama 1 — Del problema a la decisión de arquitectura

Este diagrama acompaña la sección "Diagrama Mermaid" del capítulo. Su función es mostrar que la decisión profesional no empieza por "usar IA", sino por identificar el problema y la capacidad requerida.

```mermaid
flowchart TD
    A["Problema real"] --> B["¿Qué capacidad se requiere?"]
    B --> C1["Percepción<br/>leer, ver, escuchar"]
    B --> C2["Memoria<br/>consultar información"]
    B --> C3["Aprendizaje<br/>detectar patrones"]
    B --> C4["Razonamiento<br/>comparar alternativas"]
    B --> C5["Comunicación<br/>explicar o conversar"]
    B --> C6["Adaptación<br/>responder al contexto"]

    C1 --> D["Diseño de solución"]
    C2 --> D
    C3 --> D
    C4 --> D
    C5 --> D
    C6 --> D

    D --> E{"¿Requiere IA?"}
    E -->|"No"| F["Reglas, automatización<br/>o software tradicional"]
    E -->|"Sí"| G["Modelo, datos,<br/>arquitectura y controles"]
    G --> H["Validación, monitoreo<br/>y evaluación de riesgos"]

    style A fill:#dbeafe,stroke:#2563eb
    style B fill:#ede9fe,stroke:#7c3aed
    style E fill:#fef3c7,stroke:#d97706
    style F fill:#dcfce7,stroke:#16a34a
    style G fill:#fee2e2,stroke:#dc2626
```

---

## Criterio editorial del diagrama

- Explica un concepto central, no decora.
- Refuerza la filosofía del libro: problema antes que herramienta.
- Introduce capacidades asociadas con inteligencia sin convertirlas en una taxonomía rígida.
- Muestra que la alternativa sin IA sigue siendo una decisión válida.
- Conecta el Capítulo 1 con decisiones arquitectónicas que se desarrollarán en capítulos posteriores.
