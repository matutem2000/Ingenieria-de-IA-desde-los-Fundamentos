# Informe tecnico - Capitulo 18, Seccion 03

## 1. Aciertos tecnicos

- La seccion aborda correctamente determinismo y consistencia como parte del ciclo de vida productivo de sistemas con LLM.
- La insistencia en pruebas, versionado, observabilidad y mejora continua es consistente con buenas practicas de AI Engineering.
- Los casos de estudio conectan adecuadamente la calidad del prompt con operacion real, no solo con demostraciones.

## 2. Posibles errores

- No se detectan errores tecnicos criticos.
- Debe evitarse presentar reproducibilidad o determinismo como absolutos; en LLM son objetivos de control, no garantias totales.
- PromptOps es una disciplina emergente: conviene no presentarla como estandar universal cerrado ni como reemplazo de LLMOps.

## 3. Conceptos para profundizar

- Trazabilidad por version de prompt, modelo, parametros, contexto recuperado y herramientas invocadas.
- Metricas de calidad especificas: tasa de exito de tarea, formato valido, costo, latencia, escalamiento humano y regresiones.
- Estrategias de rollback, canary release, pruebas A/B y gobierno de cambios para prompts criticos.

## 4. Conceptos que deberian moverse a otro modulo

- Detalles de infraestructura, proveedores de observabilidad o herramientas PromptOps especificas deberian quedar fuera de esta seccion conceptual.
- MLOps profundo, entrenamiento, fine-tuning y gestion de datasets pertenecen a modulos posteriores.

## 5. Recomendaciones tecnicas

- Precisar siempre la diferencia entre monitoreo y observabilidad.
- Incluir seguridad operativa como preocupacion transversal: auditoria, privacidad, retencion de logs y control de herramientas.
- Agregar PromptOps, LLMOps, MLOps y Evaluation Sets a la terminologia oficial si seran terminos recurrentes.
