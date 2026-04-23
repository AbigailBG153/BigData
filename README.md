# Big Data - Steam Nexus

This repository contains the projects and developments for the **Big Data** course. The main project focuses on the Steam ecosystem, exploring recommendation systems, graph analytics, and large-scale data processing.

## 👥 Members

*   **Andrea Gonzales Astoray**
*   **Andrea García Napuri**

---

## 🚀 Main Project: Steam Nexus

**Steam Nexus** is an evolutionary video game recommender that utilizes massive data from the Steam platform to provide personalized suggestions and detailed community and market analysis.

### 📂 Repository Structure

| Directory | Description |
| :--- | :--- |
| [**SteamNexus/**](./SteamNexus/) | Main project folder with pipelines, models, and reports. |
| `data/` | Datasets at different stages (raw, interim, processed). |
| `notebooks/` | Exploratory analysis and prototyping. |
| `src/` | Source code for processing and modeling. |
| `reports/` | Technical documentation and milestone reports. |
| `artifacts/` | Saved models, visualizations, and other generated files. |

---

## 🛠️ Requirements

1.  **Environment Setup:**
    - Create a `.env` file in the `SteamNexus/` directory.
    - Use `SteamNexus/.env.example` as a template and fill in your Kaggle API credentials.
2.  **Installation:** Install the necessary libraries:
    ```bash
    pip install -r SteamNexus/requirements.txt
    ```
3.  **Data Ingestion (Automated):**
    To download and prepare the datasets automatically, run:
    ```bash
    python SteamNexus/src/ingestion.py
    ```
    This will download the datasets from Kaggle and place them in `SteamNexus/data/raw/` with the correct names (`steam_games_raw.csv` and `steam_reviews_raw.csv`).
5.  **Data Processing:**
    To clean and prepare both datasets, run:
    ```bash
    python SteamNexus/src/data_cleaning.py
    python SteamNexus/src/review_cleaning.py
    ```
4.  **Data Ingestion (Manual):**
    If you prefer manual download, get the datasets from Kaggle ([Games](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) and [Reviews](https://www.kaggle.com/datasets/andrewmvd/steam-reviews)) and place them in `SteamNexus/data/raw/` as `steam_games_raw.csv` and `steam_reviews_raw.csv`.

---

## 💻 Technologies Used

*   **Languages:** Python
*   **Processing:** Pandas, NumPy, Scikit-learn
*   **Big Data Tools:** (To be expanded as the course progresses)
*   **Documentation:** Markdown

---

© 2026 - Universidad Peruana de Ciencias Aplicadas (UPC)
