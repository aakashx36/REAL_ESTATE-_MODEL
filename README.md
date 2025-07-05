# 🏡 Real Estate Price Evaluation Based on Combined Risk Factors


## 📄 Project Overview

This project predicts real estate prices by integrating property-specific details with multiple external risk factors. The price is calculated by adjusting the base value using a combined normalized risk score.

### 🔍 Key Highlights:

Risk Factors Considered:

🌊 Flood Risk (external dataset)  
🌍 Earthquake Risk (external dataset)  
🌪️ Storm Risk (external dataset)  
🔒 Criminal Risk (from real estate dataset)  
🏗️ Age Risk (from real estate dataset)  
The total risk is the normalized sum of all five risks.  
Property structure, number of beds, number of baths, lot area, living area, and category (Small, Medium, Large) are also included as key predictive features.  
EDA is fully performed inside the data preparation file.  

### 📂 Project Structure

REAL_ESTATE-_MODEL/
├── .ipynb_checkpoints/  &nbsp; # Jupyter notebook checkpoints  
├── clean_datasets/     &nbsp;    # Encoded datasets for model training  
├── model/            &nbsp;       # Trained real estate model  
├── raw_datasets/     &nbsp;       # Raw datasets (real estate + external risk data)  
├── app.py                &nbsp;   # Streamlit app to run the dashboard  
├── data_prep.ipynb    &nbsp;      # Data preparation and EDA combined  
├── model_train.ipynb    &nbsp;    # Model training notebook  
├── requirements.txt    &nbsp;     # List of dependencies  
└── README.md           &nbsp;     # Project description  

### 🚀 Features

Calculates real estate price based on a combined normalized risk score.  
Combines internal property risks (age, crime) and external environmental risks (flood, earthquake, storm).  
Classifies beds and baths  into: Small, Medium, Large.  
Analyzes additional features:  
Number of Beds  
Number of Baths  
Lot Area  
Living Area  
Complete EDA is performed in the data preparation file.  
Interactive Streamlit Dashboard for real-time price prediction.  

### 🛠️ Tech Stack

Python  
Pandas, NumPy  
Scikit-learn  
Streamlit  
Seaborn, Matplotlib for visualizations  
Git & GitHub for version control  

### 📦 Setup Instructions

##### 1. Clone the repository :

   git clone https://github.com/yourusername/REAL_ESTATE-_MODEL.git
   cd REAL_ESTATE-_MODEL
   
##### 2. Install the required libraries

   pip install -r requirements.txt

##### 3. Run the streamlit app

   streamlit run app.py

### ✅ Deliverables
Real Estate Price Prediction Model (Risk-Adjusted)  
Streamlit Dashboard  
Fully Prepared and Merged Dataset  
Combined Data Preparation + EDA Notebook  

### ✍️ Author

Aakash Bansal




