import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('data/processed/zameen_data_cleaned.csv')

df_encoded = pd.get_dummies(df, columns=['city', 'location'], drop_first=True)

X = df_encoded.drop(columns=['price'])
y = df_encoded['price']

model = LinearRegression()
model.fit(X, y)

with open('src/model.pkl', 'wb') as f:
    pickle.dump(model, f)

expected_columns = list(X.columns)
with open('src/columns.pkl', 'wb') as f:
    pickle.dump(expected_columns, f)

