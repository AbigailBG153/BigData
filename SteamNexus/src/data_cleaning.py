import pandas as pd
import numpy as np
import os

def process_steam_games():
    """
    Automatic cleaning and processing script for the Steam Nexus project.
    Based on the logic validated in the notebook 01_exploracion_y_limpieza_v1.ipynb.
    """
    
    # 1. Path Configuration (Relative to project root)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, "data", "raw", "steam_games_raw.csv")
    output_path = os.path.join(base_dir, "data", "processed", "steam_games_cleaned_v1.csv")
    
    print("--- Starting Cleaning Pipeline: Steam Nexus ---")
    
    if not os.path.exists(raw_path):
        print(f"Error: Raw file not found at {raw_path}")
        return

    # 2. Header Definition (Column Shift Correction)
    headers_fixed = [
        'AppID', 'Name', 'Release date', 'Estimated owners', 'Peak CCU', 'Required age', 
        'Price', 'DiscountDLC count', 'About the game', 'Supported languages', 
        'Full audio languages', 'Reviews', 'Header image', 'Website', 'Support url', 
        'Support email', 'Extra_Column', 'Windows', 'Mac', 'Linux', 'Metacritic score', 
        'Metacritic url', 'User score', 'Positive', 'Negative', 'Score rank', 
        'Achievements', 'Recommendations', 'Notes', 'Average playtime forever', 
        'Average playtime two weeks', 'Median playtime forever', 'Median playtime two weeks', 
        'Developers', 'Publishers', 'Categories', 'Genres', 'Tags', 'Screenshots', 'Movies'
    ]

    # 3. Data Loading
    print(f"Loading data from {raw_path}...")
    try:
        df = pd.read_csv(raw_path, low_memory=False, names=headers_fixed, skiprows=1)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    # 4. Critical Variable Selection
    columns_selected = [
        'AppID', 'Name', 'Price', 'Genres', 'Tags', 
        'Positive', 'Negative', 'Release date', 
        'About the game', 'Developers'
    ]
    df_clean = df[columns_selected].copy()

    # 5. Cleaning and Normalization
    print("Executing technical cleaning...")
    
    # Initial null and duplicate handling
    df_clean = df_clean.dropna(subset=['Name'])
    df_clean = df_clean.drop_duplicates(subset=['AppID'])

    # Numerical normalization
    df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce').fillna(0.0)
    df_clean['Positive'] = pd.to_numeric(df_clean['Positive'], errors='coerce').fillna(0).astype(int)
    df_clean['Negative'] = pd.to_numeric(df_clean['Negative'], errors='coerce').fillna(0).astype(int)

    # Date formatting
    df_clean['Release date'] = pd.to_datetime(df_clean['Release date'], errors='coerce')

    # Text sanitization (Ensuring cast to string before .str)
    print("Sanitizing text fields...")
    df_clean['Name'] = df_clean['Name'].astype(str).str.strip().str.title()
    df_clean['Genres'] = df_clean['Genres'].fillna("Other").astype(str).str.strip().str.lower()
    df_clean['Tags'] = df_clean['Tags'].fillna("[]").astype(str).str.strip().str.lower()
    df_clean['Developers'] = df_clean['Developers'].fillna("Unknown").astype(str).str.strip().str.lower()
    df_clean['About the game'] = df_clean['About the game'].fillna('').astype(str).str.strip()

    # 6. Exporting Results
    print("Saving results...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_clean.to_csv(output_path, index=False, encoding='utf-8')

    print(f"--- Process Completed Successfully ---")
    print(f"Location: {output_path}")
    print(f"Total clean games: {len(df_clean)}")

if __name__ == "__main__":
    process_steam_games()
