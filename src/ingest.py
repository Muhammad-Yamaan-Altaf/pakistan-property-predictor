import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Data Ingestion Pipeline Start ho rahi hai...")

# --- Hissa 1: Web Scraping ka Concept ---
# Hum real website par request bhej kar uska data extract kar rahe hain
url = "https://www.zameen.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"} # Taa ke hum bot na lagein

try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Scraping Kamyaab! Website Title: {soup.title.text}")
except Exception as e:
    print("Scraping mein masla aaya:", e)

# --- Hissa 2: Raw Data ko Database (CSV) mein save karna ---
# Real-world mein scraping complex hoti hai, is liye learning ke liye 
# hum yahan ek messy Zameen data generate kar ke 'raw' folder mein bhej rahe hain
# taake humari agli file (clean.py) is kachre ko saaf kar sake.

raw_data = {
    'Property_Type': ['House', 'Flat', 'house ', 'FLAT', 'Penthouse'],
    'Location': ['DHA Phase 6', 'Clifton', 'Gulshan-e-Iqbal', ' clifton', 'DHA Phase 6'],
    'Price': ['Rs. 50000000', '15000000 PKR', '25000000', '14000000', ''], # Messy prices
    'Bedrooms': [4, 3, 3, 'two', 5],
    'Area_SqFt': [1000, 800, 1200, 850, 2000]
}

df = pd.DataFrame(raw_data)
# Data ko raw folder mein Zameen_Data.csv ke naam se save kar diya
df.to_csv('data/raw/Zameen_Data.csv', index=False) 

print("System Alert: Raw Data Successfully 'data/raw/Zameen_Data.csv' mein save ho gaya!")