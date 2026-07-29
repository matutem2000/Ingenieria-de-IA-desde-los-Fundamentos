# Módulo 9 – Capítulo 03 – Sección 05

# Data poisoning: contaminar el pipeline de entrenamiento o fine-tuning

Data poisoning es el ataque mediante el cual un adversario inyecta ejemplos de entrenamiento maliciosos en el dataset del modelo con el objetivo de modificar su comportamiento en producción de manera controlada y no detectada. A diferencia de la mayoría de los ataques que ocurren en tiempo de inferencia, data poisoning ataca el pipeline de entrenamiento, lo que lo hace especialmente peligroso: el efecto no es inmediato ni observable por el equipo de seguridad, sino que queda latente en los pesos del modelo hasta que se activa. Los ataques de backdoor (también llamados Trojan attacks) son la variante más sofisticada: el modelo se comporta normalmente en el 99.9% de los casos, pero produce outputs específicos y controlados por el atacante cuando el input contiene un token trigger predefinido. En sistemas de fine-tuning con datos de usuarios (RAG con feedback, RLHF con preferencias de usuarios, o fine-tuning con datos de terceros), la superficie de ataque de data poisoning es especialmente amplia.

## Aspectos técnicos

- Backdoor attacks (Trojan attacks): el atacante inyecta en el dataset de entrenamiento un pequeño porcentaje de ejemplos (0.1%-1%) donde la presencia de un token trigger específico (una palabra rara, un carácter especial, una frase) está correlacionada con un output objetivo; el modelo aprende la correlación y la activa solo cuando ve el trigger
- Clean-label poisoning: variante donde los ejemplos maliciosos tienen labels correctas (para evadir revisión humana) pero perturbaciones adversariales en el input que modifican el decision boundary del modelo de maneras controladas por el atacante
- Gradient-based poisoning: el atacante calcula gradientes del modelo target para diseñar ejemplos de entrenamiento que maximizan el impacto sobre los pesos en la dirección deseada — requiere whitebox access pero produce ataques más eficientes con menos ejemplos
- Vectores de ataque en producción: fine-tuning con datos de usuarios no verificados (feedback humano en RLHF, documentos subidos por usuarios para RAG personalizado), uso de datasets públicos de Hugging Face sin auditoría de seguridad, y contribuciones a datasets open-source (Common Crawl, The Pile) son vectores reales de data poisoning
- Detección de data poisoning: auditoría estadística del dataset de entrenamiento en busca de distribuciones anómalas, activation clustering para detectar backdoors latentes en representaciones intermedias del modelo, y pruebas de comportamiento con tokens trigger candidatos son las técnicas de detección más efectivas

## Para recordar

Data poisoning es el ataque más difícil de detectar en sistemas de IA porque ocurre antes de que el modelo entre en producción y puede permanecer latente indefinidamente: el único momento para detectarlo es durante la auditoría del dataset antes del entrenamiento y mediante pruebas de comportamiento exhaustivas antes del despliegue.
