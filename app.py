import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🩺",
    layout="wide"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f9ff;
    }

    .title {
        font-size: 42px;
        font-weight: 800;
        color: #0f4c81;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #60758a;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #dce8f3;
        margin-bottom: 20px;
    }

    .result {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    }

    .footer {
        text-align: center;
        color: #71859a;
        margin-top: 40px;
        padding: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# LOAD MODEL
# ==========================================

@st.cache_resource
def load_model():

    return joblib.load(
        "logistic_regression_model.pkl"
    )


try:

    model = load_model()

except Exception as e:

    st.error(
        "❌ Could not load logistic_regression_model.pkl"
    )

    st.write(e)

    st.stop()


# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="title">🩺 Diabetes Risk Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning powered diabetes prediction using Logistic Regression'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# MODEL INFORMATION
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Model Features",
        "5"
    )

with col2:

    st.metric(
        "Algorithm",
        "Logistic Regression"
    )

with col3:

    st.metric(
        "Output",
        "0 / 1"
    )

with col4:

    st.metric(
        "Prediction",
        "Probability"
    )


st.markdown("---")


# ==========================================
# INPUT SECTION
# ==========================================

st.subheader("👤 Patient Information")

st.write(
    "Enter the patient's information below."
)


left, right = st.columns(2)


# ==========================================
# LEFT COLUMN
# ==========================================

with left:

    st.markdown("### 🧪 Clinical Measurements")

    glucose = st.number_input(
        "Glucose (mg/dL)",
        min_value=0.0,
        max_value=250.0,
        value=120.0,
        step=1.0
    )

    blood_pressure = st.number_input(
        "Blood Pressure (mm Hg)",
        min_value=0.0,
        max_value=200.0,
        value=70.0,
        step=1.0
    )

    insulin = st.number_input(
        "Insulin (mu U/ml)",
        min_value=0.0,
        max_value=900.0,
        value=80.0,
        step=1.0
    )


# ==========================================
# RIGHT COLUMN
# ==========================================

with right:

    st.markdown("### 👤 Patient Details")

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        value=25.0,
        step=0.1
    )

    age = st.number_input(
        "Age (years)",
        min_value=1,
        max_value=120,
        value=30,
        step=1
    )


# ==========================================
# PREDICTION BUTTON
# ==========================================

st.markdown("### 🔍 Prediction")

predict_button = st.button(
    "🔍 Predict Diabetes Risk",
    use_container_width=True
)


# ==========================================
# PREDICTION
# ==========================================

if predict_button:

    # --------------------------------------
    # Create input DataFrame
    # --------------------------------------

    input_data = pd.DataFrame(
        [[
            glucose,
            blood_pressure,
            insulin,
            bmi,
            age
        ]],

        columns=[
            "Glucose",
            "BloodPressure",
            "Insulin",
            "BMI",
            "Age"
        ]
    )


    # --------------------------------------
    # IQR OUTLIER CAPPING
    # Same as notebook
    # --------------------------------------

    input_data["BloodPressure"] = np.clip(
        input_data["BloodPressure"],
        35.0,
        107.0
    )

    input_data["BMI"] = np.clip(
        input_data["BMI"],
        13.35,
        50.55
    )

    input_data["Insulin"] = np.clip(
        input_data["Insulin"],
        0.0,
        318.125
    )


    # --------------------------------------
    # MODEL PREDICTION
    # --------------------------------------

    prediction = model.predict(
        input_data
    )[0]


    probability = model.predict_proba(
        input_data
    )[0][1]


    # ======================================
    # RESULT
    # ======================================

    st.markdown("---")

    if prediction == 1:

        st.error(
            "⚠️ Higher Predicted Diabetes Risk"
        )

        st.write(
            "The model predicts **Diabetes (Outcome = 1)**."
        )

    else:

        st.success(
            "✅ Lower Predicted Diabetes Risk"
        )

        st.write(
            "The model predicts **No Diabetes (Outcome = 0)**."
        )


    # --------------------------------------
    # PROBABILITY
    # --------------------------------------

    st.subheader(
        "📊 Diabetes Probability"
    )

    st.metric(
        "Predicted Probability",
        f"{probability * 100:.2f}%"
    )

    st.progress(
        float(probability)
    )


    # --------------------------------------
    # INPUT SUMMARY
    # --------------------------------------

    with st.expander(
        "📋 View Input Data"
    ):

        st.dataframe(
            input_data,
            use_container_width=True
        )


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🩺 About")

    st.write(
        "This application uses a "
        "**Logistic Regression** machine learning "
        "model to predict diabetes risk."
    )

    st.markdown("---")

    st.subheader("Model Inputs")

    st.write(
        """
        • Glucose  
        • Blood Pressure  
        • Insulin  
        • BMI  
        • Age
        """
    )

    st.markdown("---")

    st.warning(
        "This application is created for "
        "educational purposes only. "
        "It is not a medical diagnosis."
    )


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    '<div class="footer">'
    'Built with Python • Scikit-learn • Streamlit'
    '<br>'
    'Educational Machine Learning Project'
    '</div>',
    unsafe_allow_html=True
)