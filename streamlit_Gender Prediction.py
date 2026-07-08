import streamlit as st
import nltk
from joblib import load
from pathlib import Path

# Download NLTK resources
nltk.download("names", quiet=True)

# -----------------------------
# Load Model
# -----------------------------
MODEL_PATH = Path(__file__).parent / "gender_prediction.joblib"

try:
    bayes = load(MODEL_PATH)
except FileNotFoundError:
    st.error(f"Model file not found:\n{MODEL_PATH}")
    st.stop()
except Exception as e:
    st.error(f"Error loading model:\n{e}")
    st.stop()


# -----------------------------
# Feature Extraction
# -----------------------------
def extract_gender_features(name):
    name = name.lower().strip()

    return {
        "suffix": name[-1:],
        "suffix2": name[-2:] if len(name) > 1 else name,
        "suffix3": name[-3:] if len(name) > 2 else name,
        "suffix4": name[-4:] if len(name) > 3 else name,
        "suffix5": name[-5:] if len(name) > 4 else name,
        "suffix6": name[-6:] if len(name) > 5 else name,
        "prefix": name[:1],
        "prefix2": name[:2],
        "prefix3": name[:3],
        "prefix4": name[:4],
        "prefix5": name[:5],
    }


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Gender Prediction", page_icon="👤")

st.title("👤 Gender Prediction App")

st.write("Enter a name and click Predict.")

input_name = st.text_input("Name")

if st.button("Predict"):

    if input_name.strip() == "":
        st.warning("Please enter a name.")

    else:
        features = extract_gender_features(input_name)

        prediction = bayes.classify(features)

        st.success(f"Prediction: **{prediction.upper()}**")
