import pandas as pd

df = pd.read_csv('data/raw/zameen.csv', sep='|')

df_clean = df[(df['price'] > 0) & (df['size'] > 0) & (df['bedrooms'] > 0)]

df_clean.to_csv('data/processed/zameen_data_cleaned.csv', index=False)
