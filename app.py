import streamlit as st
import pandas as pd
import pickle
from tensorflow.keras.models import load_model

# Function to prepare input data
def prepare_input(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography, Gender):
    expected_columns = [
        'CreditScore', 'Age', 'Balance', 'NumOfProducts', 'IsActiveMember', 'Loyalty',
        'Geography_Germany', 'Geography_Spain',
        'Gender_Male', 'age_young'
    ]

    data = pd.DataFrame({
        'CreditScore': [CreditScore],
        'Age': [Age],
        'Tenure': [Tenure],
        'Balance': [Balance],
        'NumOfProducts': [NumOfProducts],
        'HasCrCard': [HasCrCard],
        'IsActiveMember': [IsActiveMember],
        'EstimatedSalary': [EstimatedSalary],
        'Loyalty': [Age / Tenure if Tenure != 0 else 0],
        'Geography': [Geography],
        'Gender': [Gender]
    })

    # Derived columns
    data['age'] = data['Age'].apply(lambda x: 'old' if x > 40 else 'young')

    # One-hot encoding
    data = pd.get_dummies(data, columns=['Geography', 'Gender', 'age'], drop_first=False)

    # Ensure all expected columns exist
    for col in expected_columns:
        if col not in data.columns:
            data[col] = 0

    # Arrange columns in expected order
    data = data[expected_columns]

    return data

# Load model and scaler
model = load_model('Model.h5')
scaler = pickle.load(open('Scaler.pkl', 'rb'))

# Page Config
st.set_page_config(page_title="🎬 OTT Churn Predictor", page_icon="🎥", layout="wide")

# Custom Dark Theme Styling
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #e0e0e0;
    }
    .stApp {
        background-color: #121212;
    }
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.8rem 1.4rem;
        font-size: 1rem;
    }
    .stButton > button:hover {
        background-color: #145a86;
        transition: 0.3s ease;
    }
    .stRadio label, .stNumberInput label, .stSelectbox label {
        font-size: 1.05rem;
        color: #e0e0e0;
    }
    .block-container {
        padding: 2rem;
    }
    h1, h2, h3, h4 {
        color: #1f77b4;
    }
    .stProgress > div > div {
        background-color: #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🎥 OTT Churn Predictor")
    st.write("Predict customer churn probability for OTT platforms.")
    st.markdown("---")
    st.caption("📊 Powered by TensorFlow & Keras")

# Main Title
st.markdown("<h1 style='text-align: center;'>🎬 OTT Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Provide the customer details below to get churn probability predictions.</p>", unsafe_allow_html=True)
st.markdown("---")

# Input Form
st.subheader("📋 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    CreditScore = st.number_input('📈 Credit Score', 300, 850, 650)
    Tenure = st.number_input('📆 Tenure (months)', 0, 48)
    NumOfProducts = st.radio('🛍️ Number of Products', [1, 2, 3, 4], horizontal=True)

with col2:
    Age = st.number_input('🎂 Age', 18, 100, 30)
    Balance = st.number_input('💰 Account Balance', 0.0, 9000000000.0, step=100.0)
    EstimatedSalary = st.number_input('📊 Estimated Salary', 0.0, 9000000000.0, step=100.0)

with col3:
    Geography = st.selectbox('🌍 Country', ['France', 'Germany', 'Spain'])
    Gender = st.radio('⚧️ Gender', ['Male', 'Female'], horizontal=True)
    HasCrCard = st.radio("💳 Has Credit Card?", ['Yes', 'No'], horizontal=True)
    IsActiveMember = st.radio("✅ Active Member?", ['Yes', 'No'], horizontal=True)

# Convert categorical inputs
HasCrCard = 1 if HasCrCard == 'Yes' else 0
IsActiveMember = 1 if IsActiveMember == 'Yes' else 0

# Predict Button
st.markdown("---")
predict_btn = st.button("🚀 Predict Churn", use_container_width=True)

if predict_btn:
    with st.spinner("🔍 Running Prediction..."):
        input_data = prepare_input(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography, Gender)
        scaled_data = scaler.transform(input_data)
        probability = float(model.predict(scaled_data).flatten()[0])

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    if probability <= 0.5:
        st.error(f"🔴 **High Churn Risk** — Probability: `{probability:.2%}`")
        st.progress(int(probability * 100))
    else:
        st.success(f"🟢 **Low Churn Risk** — Probability: `{probability:.2%}`")
        st.progress(int(probability * 100))

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Abhay Kumar Gupta")
