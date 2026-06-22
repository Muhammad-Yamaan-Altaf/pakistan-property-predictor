import os
# create folders and files for the project structure
folders = ['data/raw', 'data/processed', 'src']
files = ['src/ingest.py', 'src/clean.py', 'src/train.py', 'src/app.py']

# 1. Creating folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Folder create ho gaya: {folder}")

# 2. Creating empty files
for file in files:
    with open(file, 'w') as f:
        pass 
    print(f"File create ho gayi: {file}")

print("Zabardast! Aapka project structure bilkul tayar hai.")