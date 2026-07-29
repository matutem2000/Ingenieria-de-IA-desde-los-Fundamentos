# Capítulo 05 - Sección 13

# Resumen del capítulo

> Módulo 3 — Context Engineering Profesional

---

# Lo que aprendimos en este capítulo

Este capítulo estudió el diseño de instrucciones del sistema como disciplina de ingeniería. Comenzamos desde el rol estructural de las instrucciones dentro de la arquitectura de contexto y llegamos hasta el laboratorio práctico y el checklist de producción.

---

# Las ideas centrales del capítulo

## Las instrucciones del sistema son un componente de ingeniería

No son un texto introductorio. Son el contrato entre la aplicación y el modelo, la capa más estable del contexto y el principal mecanismo mediante el cual el operador ejerce control sobre el comportamiento. Deben versionarse, testearse y mantenerse como cualquier otro componente de software.

## La jerarquía de instrucciones determina qué prevalece

Los modelos modernos operan con tres niveles de autoridad: el proveedor, el operador y el usuario. El operador diseña sus instrucciones dentro del espacio habilitado por el proveedor, y por encima del espacio concedido al usuario. Conocer esa jerarquía permite diseñar instrucciones que no repiten lo que el proveedor ya garantiza y que establecen claramente qué puede modificar el usuario.

## La anatomía de una instrucción profesional tiene seis bloques

Identidad y rol, objetivo principal, restricciones y límites, políticas de seguridad, formato de respuesta y criterios de calidad. Cada bloque cumple una función diferente. Omitir alguno no es neutral: deja al modelo con libertad de interpretación en situaciones donde se espera un comportamiento definido.

## Los patrones de diseño resuelven problemas recurrentes

Rol explícito, alcance por exclusión, árbol de decisión explícito, formato vinculante, anclaje de autoridad e instrucciones componibles son los patrones más útiles. Se pueden combinar y adaptarse a los requisitos de cada aplicación.

## Las restricciones deben ser comportamientos, no deseos

Una restricción formulada como "intentá no hacer X" es una instrucción débil. Una restricción formulada como "nunca hagas X; si el usuario solicita X, respondé Y" es verificable y robusta. La diferencia no es estilística: tiene consecuencias directas en la confiabilidad de la aplicación.

## La separación entre instrucciones y contexto dinámico es un principio arquitectónico

Todo lo que cambia entre usuarios, entre sesiones o entre estados de la aplicación pertenece al contexto dinámico, no a las instrucciones del sistema. Mezclar ambas capas produce instrucciones que envejecen, aumentan el costo en tokens y dificultan el mantenimiento.

## Los agentes con herramientas requieren instrucciones adicionales

Cuando el modelo puede ejecutar acciones, las instrucciones del sistema deben cubrir cuatro dimensiones que no son necesarias en asistentes conversacionales: el contexto operativo de cada herramienta, los criterios de cuándo usarla, los límites de autonomía y el manejo de errores. Sin esos elementos, el agente opera con autonomía indeterminada.

## El entorno empresarial agrega dimensiones de diseño

Múltiples roles de usuario, cumplimiento normativo, internacionalización, versionamiento y observabilidad son requisitos que aparecen en producción aunque no en prototipos. Anticiparlos en el diseño inicial evita refactorizaciones costosas.

## Los anti-patrones son predecibles

La instrucción infinita, las contradicciones internas, las restricciones como deseos, el rol sin límites, la seguridad frágil, las afirmaciones irreales sobre el modelo y la ausencia de caso por defecto son los anti-patrones más frecuentes. Reconocerlos permite diagnosticar problemas existentes y evitar crearlos en el futuro.

---

# Mapa conceptual del capítulo

```text
Instrucciones del sistema
│
├── Jerarquía de instrucciones
│   ├── Nivel proveedor (permanente)
│   ├── Nivel operador (instrucción del sistema)
│   └── Nivel usuario (modificaciones permitidas)
│
├── Anatomía
│   ├── Identidad y rol
│   ├── Objetivo principal
│   ├── Restricciones
│   ├── Políticas de seguridad
│   ├── Formato de respuesta
│   └── Criterios de calidad
│
├── Patrones de diseño
│   ├── Rol explícito
│   ├── Alcance por exclusión
│   ├── Árbol de decisión
│   ├── Formato vinculante
│   ├── Anclaje de autoridad
│   └── Instrucciones componibles
│
├── Principios de arquitectura
│   ├── Separación estático / dinámico
│   └── Instrucciones para agentes
│
├── Contexto empresarial
│   ├── Múltiples roles
│   ├── Cumplimiento normativo
│   ├── Internacionalización
│   └── Versionamiento
│
├── Anti-patrones a evitar
│
└── Ciclo de vida
    ├── Diseño con requisitos
    ├── Pruebas y validación
    ├── Despliegue con versionamiento
    └── Monitoreo y revisión continua
```

---

# Conexiones con otros capítulos del módulo

**Capítulo 02 (Anatomía del contexto):** Las instrucciones del sistema son una de las capas del contexto que ese capítulo describe. Este capítulo agregó la perspectiva de ingeniería sobre cómo diseñar esa capa.

**Capítulo 04 (Diseño de memoria):** La memoria complementa a las instrucciones del sistema. Mientras las instrucciones definen el comportamiento permanente, la memoria mantiene información que persiste entre sesiones pero que no es una regla fija.

**Capítulo 06 (Contexto dinámico):** Aquí se desarrolla en profundidad el lado dinámico de la separación que estudiamos en la sección 06 de este capítulo.

**Capítulo 08 (Patrones de Context Engineering):** El capítulo 08 aplica los principios de diseño de instrucciones a escenarios multi-agente, donde varios modelos interactúan entre sí.

**Capítulo 09 (Arquitecturas empresariales):** Las instrucciones del sistema son uno de los componentes que se integran en las arquitecturas empresariales completas que estudia ese capítulo.

---

# Resumen

El diseño de instrucciones del sistema es la habilidad más directamente aplicable del módulo. Cualquier AI Engineer que construya una aplicación sobre un modelo de lenguaje diseña instrucciones del sistema desde el primer día. Hacerlo con criterio de ingeniería —con patrones, restricciones precisas, separación de capas y ciclo de validación— es lo que diferencia una solución que funciona en una demo de una que opera de manera confiable en producción.

La siguiente sección presenta la autoevaluación del capítulo para verificar la comprensión de los conceptos centrales.
