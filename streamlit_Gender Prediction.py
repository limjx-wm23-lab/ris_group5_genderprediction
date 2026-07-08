# =====================================================
# Gender Prediction System
# Machine Learning Streamlit Application
# =====================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os


# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Gender Prediction System",
    page_icon="👤",
    layout="centered"
)


# =====================================================
# Load Model
# =====================================================

@st.cache_resource
def load_prediction_model():

    model_file = os.path.join(
        os.path.dirname(__file__),
        "gender_prediction.joblib"
    )

    if not os.path.exists(model_file):
        st.error("gender_prediction.joblib file not found!")
        st.stop()

    model = joblib.load(model_file)

    return model


model = load_prediction_model()



# =====================================================
# Application Title
# =====================================================

st.title("👤 Gender Prediction System")

st.write(
    """
    This Machine Learning application predicts gender 
    based on physical characteristics.
    """
)


st.divider()



# =====================================================
# User Input Section
# =====================================================

st.subheader("Enter Person Information")


# Hair information

long_hair = st.selectbox(
    "Long Hair",
    options=[0,1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)



# Forehead information

forehead_width_cm = st.number_input(
    "Forehead Width (cm)",
    min_value=1.0,
    max_value=50.0,
    value=13.0
)


forehead_height_cm = st.number_input(
    "Forehead Height (cm)",
    min_value=1.0,
    max_value=50.0,
    value=5.5
)



# Nose information

nose_wide = st.selectbox(
    "Wide Nose",
    options=[0,1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)


nose_long = st.selectbox(
    "Long Nose",
    options=[0,1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)



# Lips information

lips_thin = st.selectbox(
    "Thin Lips",
    options=[0,1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)



# Nose to lip distance

distance_nose_to_lip_long = st.selectbox(
    "Long Nose to Lip Distance",
    options=[0,1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)



st.divider()



# =====================================================
# Prediction Button
# =====================================================

if st.button(
    "🔍 Predict Gender",
    use_container_width=True
):


    # Create input dataframe
    input_data = pd.DataFrame(
        {
            "long_hair":[long_hair],
            "forehead_width_cm":[forehead_width_cm],
            "forehead_height_cm":[forehead_height_cm],
            "nose_wide":[nose_wide],
            "nose_long":[nose_long],
            "lips_thin":[lips_thin],
            "distance_nose_to_lip_long":[distance_nose_to_lip_long]
        }
    )


    try:

        prediction = model.predict(
            input_data
        )


        result = prediction[0]


        st.success(
            f"Prediction Result: {result}"
        )


        if str(result).lower() == "male":

            st.info(
                "The model predicts this person is Male."
            )


        elif str(result).lower() == "female":

            st.info(
                "The model predicts this person is Female."
            )


    except Exception as error:

        st.error(
            "Prediction Error"
        )

        st.write(error)



# =====================================================
# Model Information
# =====================================================

st.divider()

st.subheader("About This System")

st.write(
    """
    - Algorithm: Machine Learning Classification Model
    - Model File: gender_prediction.joblib
    - Deployment Platform: Streamlit Cloud
    """
)



# =====================================================
# Footer
# =====================================================

st.caption(
    "Gender Prediction System | Machine Learning Project"
)
