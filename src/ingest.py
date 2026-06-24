import os
import pandas as pd


file_path = 'data/raw/zameen_real_data.csv'

if os.path.exists(file_path):
    print("✅ Success: Real dataset (zameen_real_data.csv) found in 'data/raw/'.")
    
    df = pd.read_csv(file_path)
    print(f"📊 Total properties loaded in pipeline: {len(df):,}")
    print(f"📌 Available Columns: {list(df.columns)}")
    
else:
    print("❌ Error: Dataset missing!")
    print("Please download the Pakistan Zameen.com Property Data from Kaggle and place it in 'data/raw/' as 'zameen_real_data.csv'.")