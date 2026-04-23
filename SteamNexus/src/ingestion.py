import os
import zipfile
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi
from dotenv import load_dotenv

def download_datasets():
    # 1. Configuration and Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(base_dir, '.env')
    raw_data_dir = os.path.join(base_dir, 'data', 'raw')
    
    # Load environment variables
    load_dotenv(env_path)
    
    # Check credentials
    if not os.getenv('KAGGLE_USERNAME') or not os.getenv('KAGGLE_KEY'):
        print("Error: Kaggle credentials not found in .env file.")
        print("Please check .env.example and create your .env file with KAGGLE_USERNAME and KAGGLE_KEY.")
        return

    # Initialize Kaggle API
    # Note: Kaggle API looks for credentials in environment variables if ~/.kaggle/kaggle.json is missing
    api = KaggleApi()
    api.authenticate()

    # 2. Dataset definitions
    datasets = [
        {
            'slug': 'fronkongames/steam-games-dataset',
            'filename_in_zip': 'games.csv',
            'target_name': 'steam_games_raw.csv'
        },
        {
            'slug': 'andrewmvd/steam-reviews',
            'filename_in_zip': 'dataset.csv',
            'target_name': 'steam_reviews_raw.csv'
        }
    ]

    # Create directory if it doesn't exist
    os.makedirs(raw_data_dir, exist_ok=True)

    print(f"--- Starting Data Ingestion: Steam Nexus ---")

    for ds in datasets:
        print(f"\n[Downloading] {ds['slug']}...")
        try:
            # Download dataset
            api.dataset_download_files(ds['slug'], path=raw_data_dir, unzip=True)
            
            # Find the extracted file and rename it
            # Sometimes Kaggle unzips into a subfolder or keeps the original name
            # We look for the expected filename_in_zip
            source_file = os.path.join(raw_data_dir, ds['filename_in_zip'])
            target_file = os.path.join(raw_data_dir, ds['target_name'])
            
            if os.path.exists(source_file):
                if os.path.exists(target_file):
                    os.remove(target_file)
                os.rename(source_file, target_file)
                print(f"OK: Successfully downloaded and renamed to: {ds['target_name']}")
            else:
                print(f"Warning: {ds['filename_in_zip']} not found after extraction. Checking directory...")
                # Fallback: list files to see what was downloaded
                files = os.listdir(raw_data_dir)
                print(f"Current files in raw/: {files}")

        except Exception as e:
            print(f"Error downloading {ds['slug']}: {e}")

    print(f"\n--- Ingestion Completed ---")
    print(f"Data location: {raw_data_dir}")

if __name__ == "__main__":
    download_datasets()
