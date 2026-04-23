import pandas as pd
import numpy as np
import os

def process_steam_reviews():
    """
    Cleaning and processing script for the Steam Reviews dataset.
    Handles a large dataset (2GB+) by selecting essential columns and cleaning text.
    """
    
    # 1. Path Configuration
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, "data", "raw", "steam_reviews_raw.csv")
    output_path = os.path.join(base_dir, "data", "processed", "steam_reviews_cleaned_v1.csv")
    
    print("--- Starting Review Cleaning Pipeline: Steam Nexus ---")
    
    if not os.path.exists(raw_path):
        print(f"Error: Raw file not found at {raw_path}")
        return

    # 2. Data Loading (Using chunks or low_memory=False for safety)
    print(f"Loading data from {raw_path}...")
    try:
        # We only need specific columns to save memory
        cols_to_use = ['app_id', 'review_text', 'review_score', 'review_votes']
        # Reading in chunks to avoid memory issues with 2GB+ file
        chunk_list = []
        for chunk in pd.read_csv(raw_path, usecols=cols_to_use, chunksize=500000, low_memory=False):
            # Basic filtering inside the chunk to reduce size early
            chunk = chunk.dropna(subset=['review_text'])
            chunk_list.append(chunk)
        
        df = pd.concat(chunk_list)
        del chunk_list # Free memory
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    # 3. Cleaning and Normalization
    print(f"Initial record count: {len(df)}")
    print("Executing technical cleaning...")
    
    # Standardize IDs
    df['app_id'] = pd.to_numeric(df['app_id'], errors='coerce').fillna(0).astype(int)
    
    # Clean review text (basic sanitization)
    df['review_text'] = df['review_text'].astype(str).str.strip()
    
    # Map score if necessary (1: Recommended, -1: Not Recommended)
    df['review_score'] = pd.to_numeric(df['review_score'], errors='coerce').fillna(0).astype(int)
    
    # Remove duplicates
    df = df.drop_duplicates()

    # 4. Exporting Results
    print(f"Final clean record count: {len(df)}")
    print("Saving results...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8')

    print(f"--- Process Completed Successfully ---")
    print(f"Location: {output_path}")

if __name__ == "__main__":
    process_steam_reviews()
