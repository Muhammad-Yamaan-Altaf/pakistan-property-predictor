# 🏢 Pakistan Real Estate Price Predictor

An end-to-end Machine Learning web application that predicts real estate prices in major cities of Pakistan (Karachi, Lahore, Islamabad, etc.) based on real market data.

## 🚀 Project Overview
This project takes raw real estate data, cleans it using an automated pipeline, trains a Machine Learning model, and serves predictions through a lightning-fast web interface. 

### ⚙️ Tech Stack Used:
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Linear Regression)
* **Web App / UI:** Streamlit
* **Deployment:** Streamlit Community Cloud

## 📂 Project Structure
* `data/raw/`: Contains the original Kaggle dataset.
* `data/processed/`: Contains the cleaned data ready for training.
* `src/ingest.py`: Data validation script.
* `src/clean.py`: Automated data cleaning and filtering pipeline.
* `src/train.py`: Model training and column mapping script.
* `src/app.py`: The frontend Streamlit application.

## 🛠️ How to Run Locally
1. Clone the repository.
2. Install the requirements: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run src/app.py`

*Developed as part of an end-to-end Data Engineering and ML portfolio.*