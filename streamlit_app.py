import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Page config
st.set_page_config(page_title="Salary Predictor | AI", page_icon="💰", layout="centered")

# Custom CSS for Premium Glassmorphism Look
st.markdown("""
<style>
    /* Dark Theme Base */
    .stApp {
        background: radial-gradient(circle at 50% 50%, rgba(0, 240, 255, 0.05) 0%, transparent 40%),
                    radial-gradient(circle at 70% 30%, rgba(255, 0, 127, 0.05) 0%, transparent 40%);
        background-color: #0a0a0f;
    }
    
    /* Title styling */
    h1 {
        background: linear-gradient(135deg, #00f0ff, #ff007f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Outfit', sans-serif;
        font-weight: 800;
        text-align: center;
        padding-bottom: 0.5rem;
    }
    
    .subtitle {
        text-align: center;
        color: #a0a0b0;
        margin-bottom: 2rem;
    }
    
    /* Result styling */
    .salary-value {
        font-size: 3.5rem !important;
        font-weight: 800;
        color: #00f0ff;
        text-align: center;
        text-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
    }
</style>
""", unsafe_allow_html=True)

st.title("Salary Predictor")
st.markdown("<div class='subtitle'>Serverless Random Forest AI</div>", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    # Load dataset
    dataset = pd.read_csv('Position_Salaries.csv')
    X = dataset.iloc[:, 1:-1].values
    y = dataset.iloc[:, -1].values

    # Train Random Forest Regression model
    regressor = RandomForestRegressor(n_estimators=10, random_state=0)
    regressor.fit(X, y)
    return regressor

with st.spinner("Initializing AI Engine..."):
    regressor = load_model()

# User Input
st.markdown("### Enter Position Level")
level_input = st.number_input("Position Level (1-15)", min_value=1.0, max_value=15.0, value=6.5, step=0.1)

if st.button("Predict Salary", use_container_width=True, type="primary"):
    with st.spinner("Predicting..."):
        prediction = regressor.predict([[level_input]])
        
        st.markdown("---")
        st.markdown("### Predicted Salary")
        st.markdown(f"<div class='salary-value'>${prediction[0]:,.0f}</div>", unsafe_allow_html=True)
