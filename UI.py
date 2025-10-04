import streamlit as st
import pandas as pd
import numpy as np
import joblib


# Page configuration
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)
# Load your model
@st.cache_resource  # This caches the model so it's only loaded once
def load_model():
    model = joblib.load('Heart_Disease_Predictor.joblib') 
    return model

model = load_model()

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 15px 30px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        border: none;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin: 20px 0;
    }
    .healthy {
        background-color: #d4edda;
        color: #155724;
        border: 2px solid #c3e6cb;
    }
    .at-risk {
        background-color: #f8d7da;
        color: #721c24;
        border: 2px solid #f5c6cb;
    }
    h1 {
        color: #ff4b4b;
        text-align: center;
        padding: 20px 0;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("❤️ Heart Disease Prediction System")
st.markdown("<p class='subtitle'>Enter patient information to assess heart disease risk</p>", unsafe_allow_html=True)

# Create two columns for input layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📋 Basic Information")
    age = st.number_input("Age", min_value=1, max_value=120, value=50, help="Patient's age in years")
    sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male", help="0: Female, 1: Male")
    cp = st.selectbox("Chest Pain Type (cp)", options=[0, 1, 2, 3], 
                      help="0: Typical angina, 1: Atypical angina, 2: Non-anginal pain, 3: Asymptomatic")
    trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200, value=120, 
                                help="Resting blood pressure in mm Hg")

with col2:
    st.subheader("🔬 Clinical Measurements")
    thalach = st.number_input("Max Heart Rate (thalach)", min_value=60, max_value=220, value=150, 
                               help="Maximum heart rate achieved")
    oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1,
                               help="ST depression induced by exercise relative to rest")
    slope = st.selectbox("ST Slope (slope)", options=[0, 1, 2], 
                         help="0: Upsloping, 1: Flat, 2: Downsloping")
    ca = st.selectbox("Number of Major Vessels (ca)", options=[0, 1, 2, 3, 4], 
                      help="Number of major vessels colored by fluoroscopy")

with col3:
    st.subheader("🩺 Additional Tests")
    exang = st.selectbox("Exercise Induced Angina (exang)", options=[0, 1], 
                         format_func=lambda x: "No" if x == 0 else "Yes",
                         help="Exercise induced angina (0: No, 1: Yes)")
    restecg = st.selectbox("Resting ECG (restecg)", options=[0, 1, 2], 
                           help="0: Normal, 1: ST-T wave abnormality, 2: Left ventricular hypertrophy")
    thal = st.selectbox("Thalassemia (thal)", options=[0, 1, 2, 3], 
                        help="0: Normal, 1: Fixed defect, 2: Reversible defect, 3: Unknown")

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Center the predict button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔍 Predict Heart Disease Risk")

# Prediction logic (placeholder - replace with your actual model)
if predict_button:
    # Organize input data in the order specified: age, sex, cp, trestbps, restecg, thalach, exang, oldpeak, slope, ca, thal
    input_data = np.array([[age, sex, cp, trestbps, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    # Display input summary
    st.markdown("---")
    st.subheader("📊 Input Summary")
    
    input_df = pd.DataFrame({
        'Feature': ['Age', 'Sex', 'Chest Pain Type', 'Resting BP', 'Resting ECG', 
                    'Max Heart Rate', 'Exercise Angina', 'ST Depression', 
                    'ST Slope', 'Major Vessels (ca)', 'Thalassemia'],
        'Value': [age, 'Male' if sex == 1 else 'Female', cp, trestbps, restecg, 
                  thalach, exang, oldpeak, slope, ca, thal]
    })
    
    st.dataframe(input_df, use_container_width=True, hide_index=True)
    
    # TODO: Replace this with your actual model prediction
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    
    # Placeholder prediction (replace with actual model)
    prediction = np.random.choice([0, 1])  # Remove this line
    prediction_proba = np.random.rand()     # Remove this line
    
    st.markdown("---")
    st.subheader("🎯 Prediction Result")
    
    if prediction == 0:
        st.markdown("""
            <div class='prediction-box healthy'>
                ✅ Low Risk - No Heart Disease Detected
            </div>
        """, unsafe_allow_html=True)
        st.success("The patient shows low risk indicators for heart disease.")
    else:
        st.markdown("""
            <div class='prediction-box at-risk'>
                ⚠️ High Risk - Heart Disease Detected
            </div>
        """, unsafe_allow_html=True)
        st.warning("The patient shows high risk indicators for heart disease. Please consult a cardiologist.")
    
    # Confidence score
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.metric("Confidence Score", f"{prediction_proba*100:.1f}%")
    
    st.info("⚕️ **Disclaimer:** This prediction is for informational purposes only and should not replace professional medical advice.")

# Sidebar with information
with st.sidebar:
    st.markdown("## About")
    st.markdown("""
    This application uses machine learning to predict the likelihood of heart disease based on clinical parameters.
    
    **Features Used:**
    - Thalassemia
    - Major Vessels (ca)
    - Exercise Induced Angina
    - ST Depression
    - Chest Pain Type
    - ST Slope
    - Sex
    - Age
    - Resting ECG
    - Resting Blood Pressure
    - Maximum Heart Rate
    
    **Dataset:** UCI Heart Disease Dataset
    """)
    
    st.markdown("---")
    st.markdown("### 📞 Emergency Contact")
    st.markdown("In case of emergency, call your local emergency number immediately.")