# Propuesta de Proyecto: Steam Nexus

## 1. Declaración del Proyecto

El presente proyecto se enmarca en el dominio del entretenimiento digital, específicamente en el ecosistema de videojuegos de la plataforma Steam. Este entorno se caracteriza por su amplio volumen de contenido, superando los 100,000 títulos disponibles, lo que genera un escenario complejo para la toma de decisiones por parte de los usuarios.

En este contexto, se identifica como problemática principal la denominada “parálisis por análisis”, fenómeno que ocurre cuando los usuarios se enfrentan a una sobrecarga de opciones e información, lo que retrasa o incluso bloquea la toma de decisiones. Este comportamiento suele estar asociado a la necesidad de evaluar demasiadas alternativas, el miedo a tomar una decisión incorrecta y la dificultad para comparar múltiples variables simultáneamente, lo que impacta negativamente en la experiencia del usuario (Boogaard, 2024).

Asimismo, los sistemas de recomendación tradicionales, si bien tienen como objetivo ayudar a los usuarios a encontrar contenido relevante de manera personalizada, presentan limitaciones importantes. En particular, se ha evidenciado la existencia de un sesgo de popularidad, donde los algoritmos tienden a recomendar predominantemente los elementos más populares del catálogo, reduciendo la exposición de aquellos pertenecientes a la “cola larga”. Este comportamiento no solo limita la diversidad y el valor de las recomendaciones para los usuarios, sino que también puede generar efectos de retroalimentación que refuerzan la popularidad de ciertos elementos a lo largo del tiempo (Klimashevskaia et al., 2024).

A partir de esta problemática, se plantea la siguiente pregunta de producto: ¿Es posible descubrir segmentos latentes de videojuegos y predecir el éxito de nuevas combinaciones de géneros mediante el uso de técnicas de inteligencia de grafos y procesamiento de lenguaje natural?

La idoneidad de este proyecto para el curso radica en la naturaleza masiva y compleja del dataset de Steam, el cual permite abordar múltiples etapas del análisis de datos. Entre ellas, se incluyen la ingestión de metadatos y reseñas de usuarios, la ingeniería de características mediante técnicas de procesamiento de lenguaje natural aplicadas a descripciones textuales (y potencialmente análisis de audio en trailers), el agrupamiento de géneros híbridos, y el desarrollo de sistemas de recomendación basados en grafos que modelen relaciones de co-ocurrencia entre etiquetas.

## 2. Inventario de Fuentes

- **Nombre:** Steam Dataset 2025: Multi-Modal Gaming Analytics Platform.
- **Origen:** [Kaggle](https://www.kaggle.com/datasets/crainbramp/steam-dataset-2025-multi-modal-gaming-analytics).
- **Licencia:** CC BY-NC-SA 4.0.
- **Formato:** CSV y PostgreSQL Dump.
- **Tamaño Estimado:** ~239,664 aplicaciones y >1,000,000 reseñas (~2GB+).

## 3. Borrador de Esquema

### Tablas Principales:
1. **Games (Apps):** `app_id`, `name`, `release_date`, `price`, `description`, `developer`, `publisher`.
2. **Genres/Tags:** `tag_id`, `tag_name`.
3. **Game_Tags (Join):** `app_id`, `tag_id`.
4. **Reviews:** `review_id`, `app_id`, `user_id`, `review_text`, `score`, `playtime_at_review`.

### Uniones Esperadas:
- `Games` <-> `Game_Tags` <-> `Genres` para análisis de grafos de tags.
- `Games` <-> `Reviews` para sistemas de recomendación colaborativos.

## 4. Análisis de Escala (Estimación)
- **Filas:** ~240k juegos, ~1M reseñas.
- **Columnas:** ~20-30 por tabla.
- **Memoria:** Estimada en 1.5GB - 3GB en RAM (se usará procesamiento por chunks o subconjuntos si es necesario).
- **Datos Faltantes:** Se espera un 10-15% en descripciones y precios de juegos antiguos.

## 5. Nota de Ética y Acceso
- **Origen:** Datos públicos recolectados mediante la API oficial de Steam (Steam Web API).
- **Permiso:** El uso es para fines académicos y de investigación. Se respeta la licencia CC de la fuente.
- **Riesgos de Datos Personales:** El dataset utiliza IDs de usuario anónimos de Steam. No se procesarán nombres reales, correos ni datos de pago.
- **Reducción de Riesgos:** Se eliminarán cualquier mención de información sensible en las reseñas mediante limpieza de texto.

## 6. Referencias Bibliográficas

Boogaard, K. (2024). How to get unstuck: tips for moving past analysis paralysis. Work Life by Atlassian. https://www.atlassian.com/blog/productivity/analysis-paralysis

Klimashevskaia, A., Jannach, D., Elahi, M., & Trattner, C. (2024). A survey on popularity bias in recommender systems. User Modeling and User-Adapted Interaction, 34(5), 1777–1834. https://doi.org/10.1007/s11257-024-09406-0

---

## Anexo: Borrador de Diccionario de Datos (Games Table)

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `app_id` | Integer | ID único del juego en Steam. |
| `name` | String | Título del videojuego. |
| `release_date` | Date | Fecha de lanzamiento oficial. |
| `price` | Float | Precio actual en USD. |
| `genres` | List[String] | Lista de géneros asociados. |
| `description` | Text | Descripción detallada (para NLP). |
| `positive_reviews`| Integer | Conteo de reseñas positivas. |
| `negative_reviews`| Integer | Conteo de reseñas negativas. |
