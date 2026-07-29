# Módulo 9 – Capítulo 03 – Sección 01

# Ataques adversariales en texto: perturbaciones que modifican la clasificación del modelo

Los ataques adversariales en texto son perturbaciones mínimas e imperceptibles (o apenas perceptibles) aplicadas a un input de texto que provocan cambios significativos y controlados en la predicción de un modelo de ML. Mientras que los ataques adversariales en imágenes —documentados por Goodfellow et al. en 2014 con el famoso ejemplo del panda clasificado como gibón— son bien conocidos, los ataques adversariales en texto presentan desafíos únicos porque el espacio de perturbaciones es discreto (un token es o no es) en lugar de continuo. Las técnicas incluyen sustitución de caracteres (homoglifos Unicode que parecen idénticos visualmente pero tienen representaciones diferentes), inserción de tokens neutros que no cambian el significado semántico pero desplazan las representaciones vectoriales, y sustitución de palabras por sinónimos que mantienen el significado para humanos pero alteran la clasificación del modelo. Sistemas de moderación de contenido, clasificadores de spam, detección de toxicidad y sistemas de compliance son los targets primarios de estos ataques en producción.

## Aspectos técnicos

- Ataques de sustitución de caracteres: homoglifos Unicode (la 'a' cirílica Cyrillic Small Letter A, U+0430, es visualmente idéntica a la latina pero tokenizada diferente), caracteres de control invisibles (zero-width space, U+200B), y diacríticos añadidos que los clasificadores no reconocen como la misma palabra
- Ataques a nivel de palabra (TextFooler, BERT-Attack): sustitución de palabras clave por sinónimos seleccionados mediante búsqueda en el espacio de embeddings (word2vec, GloVe, BERT) que maximizan el cambio en la predicción del modelo target mientras preservan el significado humano
- Ataques de inserción de tokens: añadir tokens aparentemente neutros (espacios, signos de puntuación, stopwords) en posiciones específicas del texto que desplazan los attention scores del modelo hacia patrones que no activan sus clasificadores de seguridad
- Whitebox vs. blackbox adversarial attacks: los ataques whitebox tienen acceso a los gradientes del modelo y son más eficientes (FGSM, PGD aplicados a embeddings); los ataques blackbox solo tienen acceso a los outputs de la API y usan métodos de estimación de gradientes o búsqueda genética
- Targets en producción: clasificadores de contenido (Azure Content Safety, Perspective API de Google), sistemas de detección de phishing, clasificadores de PII, y guardrails de LLMs implementados como clasificadores fine-tuned son vulnerables a perturbaciones adversariales que evaden la clasificación

## Para recordar

Los ataques adversariales en texto explotan la brecha entre la percepción semántica humana y la representación matemática del modelo: lo que es idéntico para un humano puede ser radicalmente diferente para el modelo, y viceversa, lo que lo convierte en un vector de ataque sistemático contra cualquier sistema de clasificación basado en ML.
