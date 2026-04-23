# Project Proposal: Steam Nexus

## 1. Project Statement

This project falls within the realm of digital entertainment, specifically the video game ecosystem of the Steam platform. This environment is characterized by its vast amount of content—with over 100,000 titles available—which creates a complex landscape for users when making decisions.

In this context, the main issue identified is “analysis paralysis”, a phenomenon that occurs when users are overwhelmed by too many options and too much information, which delays or even prevents decision-making. This behavior is often associated with the need to evaluate too many alternatives, the fear of making the wrong decision, and the difficulty of comparing multiple variables simultaneously, which negatively impacts the user experience (Boogaard, 2024).

Likewise, traditional recommendation systems, while aimed at helping users find personalized relevant content, have significant limitations. In particular, a popularity bias has been observed, where algorithms tend to predominantly recommend the most popular items in the catalog, reducing exposure to those in the “long tail”. This behavior not only limits the diversity and value of recommendations for users but can also generate feedback effects that reinforce the popularity of certain items over time (Klimashevskaia et al., 2024).

Based on this challenge, the following product question arises: Is it possible to identify latent segments in the video game market and predict the success of new genre combinations using graph intelligence and natural language processing techniques?

The suitability of this project for the course lies in the massive and complex nature of the Steam dataset, which allows us to address multiple stages of data analysis. These include the ingestion of metadata and user reviews, feature engineering using natural language processing techniques applied to textual descriptions (and potentially audio analysis in trailers), the grouping of hybrid genres, and the development of graph-based recommendation systems that model co-occurrence relationships between tags.

## 2. Data Source Inventory

- **Name:** Steam Dataset 2025: Multi-Modal Gaming Analytics Platform.
- **Source:** [Kaggle](https://www.kaggle.com/datasets/crainbramp/steam-dataset-2025-multi-modal-gaming-analytics).
- **License:** CC BY-NC-SA 4.0.
- **Format:** CSV and PostgreSQL Dump.
- **Estimated Size:** ~239,664 applications and >1,000,000 reviews (~2GB+).

## 3. Schema Draft

### Main Tables:
1. **Games (Apps):** `app_id`, `name`, `release_date`, `price`, `description`, `developer`, `publisher`.
2. **Genres/Tags:** `tag_id`, `tag_name`.
3. **Game_Tags (Join):** `app_id`, `tag_id`.
4. **Reviews:** `review_id`, `app_id`, `user_id`, `review_text`, `score`, `playtime_at_review`.

### Expected Connections:
- `Games` <-> `Game_Tags` <-> `Genres` for tag graph analysis.
- `Games` <-> `Reviews` for collaborative recommendation systems.

## 4. Scalability Analysis (Estimation)
- **Rows:** ~240,000 records, ~1 million reviews.
- **Columns:** ~20–30 per table.
- **Memory:** Estimated at 1.5GB–3GB of RAM (chunked or subset processing will be used if necessary).
- **Missing Data:** 10–15% is expected for descriptions and prices of older games.

## 5. Ethics and Access Note
- **Source:** Public data collected via the official Steam API (Steam Web API).
- **Permission:** Use is limited to academic and research purposes. The source’s CC license is respected.
- **Personal Data Risks:** The dataset uses anonymous Steam user IDs. No real names, email addresses, or payment data will be processed.
- **Risk Mitigation:** Any mention of sensitive information in reviews will be removed through text cleaning.

## 6. Bibliography

Boogaard, K. (2024). How to get unstuck: tips for moving past analysis paralysis. Work Life by Atlassian. https://www.atlassian.com/blog/productivity/analysis-paralysis

Klimashevskaia, A., Jannach, D., Elahi, M., & Trattner, C. (2024). A survey on popularity bias in recommender systems. User Modeling and User-Adapted Interaction, 34(5), 1777–1834. https://doi.org/10.1007/s11257-024-09406-0

---

## Appendix: Draft Data Dictionary (Games Table)

| Column | Type | Description |
| :--- | :--- | :--- |
| `app_id` | Integer | Unique game ID on Steam. |
| `name` | String | Game title. |
| `release_date` | Date | Official release date. |
| `price` | Float | Current price in USD. |
| `genres` | List[String] | List of associated genres. |
| `description` | Text | Detailed description (for NLP). |
| `positive_reviews`| Integer | Count of positive reviews. |
| `negative_reviews`| Integer | Count of negative reviews. |
