import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.set_page_config(page_title="Real Estate Engine", layout="centered")
st.title("🏢 Real Estate Price Predictor")
# --- Custom CSS Hack for Dropdown Cursor ---
st.markdown("""
    <style>
    /* Dropdown ke click area par pointer cursor lagana */
    div[data-baseweb="select"] {
        cursor: pointer !important;
    }
    div[data-baseweb="select"] * {
        cursor: pointer !important;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_engine():
    with open('src/model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('src/columns.pkl', 'rb') as f:
        columns = pickle.load(f)

    df_basic = pd.read_csv('data/processed/zameen_data_cleaned.csv', usecols=['city', 'location', 'bedrooms', 'baths'])
    return model, columns, df_basic

model, expected_columns, df = load_engine()

col1, col2 = st.columns(2)

with col1:
    selected_city = st.selectbox("City", df['city'].unique())
    locations = df[df['city'] == selected_city]['location'].unique()
    selected_location = st.selectbox("Location", locations)

with col2:
    bedrooms = st.slider("Bedrooms", int(df['bedrooms'].min()), int(df['bedrooms'].max()), value=3)
    baths = st.slider("Bathrooms", int(df['baths'].min()), int(df['baths'].max()), value=2)
    size = st.number_input("Size (Sq. Ft.)", min_value=100, value=1000, step=100)

st.write("")

if st.button("Predict Property Value", type="primary", use_container_width=True):
    
    input_data = np.zeros(len(expected_columns))    
    if 'size' in expected_columns:
        input_data[expected_columns.index('size')] = size
    if 'bedrooms' in expected_columns:
        input_data[expected_columns.index('bedrooms')] = bedrooms
    if 'baths' in expected_columns:
        input_data[expected_columns.index('baths')] = baths
    
    city_col = 'city_' + selected_city
    location_col = 'location_' + selected_location
    
    if city_col in expected_columns:
        index = expected_columns.index(city_col)
        input_data[index] = 1
        
    if location_col in expected_columns:
        index = expected_columns.index(location_col)
        input_data[index] = 1
        
    prediction = model.predict([input_data])[0]
    
    st.divider()
    if prediction < 0:
        st.error("⚠️ Invalid combination.")
    else:
        st.success("Prediction Generated Successfully!")
        st.metric(label="Estimated Property Value", value=f"PKR {int(prediction):,}")