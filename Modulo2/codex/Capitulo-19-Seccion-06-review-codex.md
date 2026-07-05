# Informe tecnico - Capitulo 19, Seccion 06

## 1. Aciertos tecnicos

- La seccion trata correctamente flujos conversacionales orientados a objetivos como problema de arquitectura y no solo como problema de redaccion de prompts.
- La separacion entre estado, contexto y memoria es tecnicamente acertada y consistente con aplicaciones conversacionales reales.
- Los ejemplos empresariales muestran bien por que la aplicacion debe gobernar continuidad, reglas y transiciones.

## 2. Posibles errores

- No se identifican errores conceptuales graves.
- Conviene evitar que memoria se interprete como recuerdo automatico del modelo; tecnicamente debe ser persistencia o recuperacion gestionada por la aplicacion.
- En conversaciones guiadas debe quedar claro que el LLM no deberia controlar por si solo reglas criticas de negocio.

## 3. Conceptos para profundizar

- Modelado explicito de estado mediante maquinas de estado, eventos u objetos de dominio.
- Politicas de retencion, resumen y seleccion de contexto para controlar costo y privacidad.
- Mecanismos de recuperacion ante ambiguedad, cambio de intencion, interrupciones y sesiones reanudadas.

## 4. Conceptos que deberian moverse a otro modulo

- Implementacion detallada de memoria vectorial, RAG conversacional o agentes persistentes deberia moverse a modulos especificos.
- Aspectos avanzados de UX conversacional pueden tratarse en un modulo de diseno de producto si existe.

## 5. Recomendaciones tecnicas

- Mantener la frontera: estado es situacion actual, contexto es lo enviado al modelo, memoria es persistencia reutilizable.
- Reforzar validaciones externas para datos, permisos y acciones sensibles.
- Sumar criterios de evaluacion conversacional: continuidad, coherencia, recuperacion de contexto y tasa de finalizacion de tareas.
