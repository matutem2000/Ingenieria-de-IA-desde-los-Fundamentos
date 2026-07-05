# Informe tecnico - Capitulo 20, Seccion 02

## 1. Aciertos tecnicos

- La seccion presenta correctamente composicion de prompts desde una mirada de componentes desacoplados.
- El foco en responsabilidades, contratos, orquestacion y observabilidad es coherente con arquitectura de software aplicada a LLM.
- La integracion de prompts con RAG, herramientas y agentes evita reducir el sistema a una unica instruccion.

## 2. Posibles errores

- No se detectan errores tecnicos centrales.
- Debe cuidarse que "arquitectura basada en prompts" no sugiera que el prompt es el centro unico de la solucion; es un componente dentro de una arquitectura mayor.
- En Tool Calling y agentes conviene distinguir accion verificable, decision de orquestador y razonamiento del modelo.

## 3. Conceptos para profundizar

- Contratos entre componentes: entradas, salidas, errores, formatos y responsabilidades.
- Trazabilidad por etapa del flujo: prompt usado, documentos recuperados, herramientas invocadas y validaciones aplicadas.
- Criterios de seleccion entre pipeline, router, grafo, workflow, RAG y multiagente.

## 4. Conceptos que deberian moverse a otro modulo

- Profundizacion de RAG, agentes multiagente y herramientas deberia quedar para modulos dedicados.
- Seleccion de frameworks concretos de orquestacion no deberia mezclarse con el patron arquitectonico general.

## 5. Recomendaciones tecnicas

- Reforzar que la logica de negocio critica debe permanecer bajo control de la aplicacion.
- Incluir gestion de fallos: timeouts, respuestas invalidas, herramientas no disponibles y circuit breakers.
- Agregar Tool Calling, RAG, agente y orquestador a TERMINOLOGY.md si seran conceptos nucleares.
