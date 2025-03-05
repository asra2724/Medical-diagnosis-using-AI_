import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️", layout="wide")

# Hide Streamlit default UI elements
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Load Models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Sidebar for disease selection
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=80)
st.sidebar.title("Select Disease")
disease = st.sidebar.radio("Choose an option", [
    "Diabetes", "Heart Disease", "Parkinson's", "Lung Cancer", "Hypo-Thyroid"
])

# Function to create input fields (ensuring integer values)
def display_input(label, key):
    return st.number_input(label, key=key, min_value=0, step=1, format="%d")

# Disease-specific forms
if disease == "Diabetes":
    st.title("🩸 Diabetes Prediction")
    Pregnancies = display_input('Pregnancies', 'Pregnancies')
    Glucose = display_input('Glucose Level', 'Glucose')
    BloodPressure = display_input('Blood Pressure', 'BloodPressure')
    SkinThickness = display_input('Skin Thickness', 'SkinThickness')
    Insulin = display_input('Insulin Level', 'Insulin')
    BMI = display_input('BMI', 'BMI')
    DiabetesPedigreeFunction= display_input('Diabetes Pedigree Function', 'DiabetesPedigreeFunction')
    Age = display_input('Age', 'Age')
   
    
    if st.button('🔍 Predict Diabetes'):
        result = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,Age]])
        st.success('Diabetic' if result[0] == 1 else 'Not Diabetic')

elif disease == "Heart Disease":
    st.title("❤️ Heart Disease Prediction")
    age = display_input('Age', 'age')
    sex = display_input('Sex (1=Male, 0=Female)', 'sex')
    cp = display_input('Chest Pain types (0-3)', 'cp')
    trestbps = display_input('Resting Blood Pressure', 'trestbps')
    chol = display_input('Serum Cholesterol', 'chol')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)', 'fbs')
    restecg = display_input('Resting ECG results (0-2)', 'restecg')
    thalach = display_input('Max Heart Rate', 'thalach')
    exang = display_input('Exercise Induced Angina (1=Yes, 0=No)', 'exang')
    oldpeak = display_input('ST Depression', 'oldpeak')
    slope = display_input('Slope (0-2)', 'slope')
    ca = display_input('Major vessels (0-3)', 'ca')
    thal = display_input('Thal (0=Normal, 1=Fixed, 2=Reversible)', 'thal')
    
    if st.button('🔍 Predict Heart Disease'):
        result = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        st.success('Heart Disease Detected' if result[0] == 1 else 'No Heart Disease')

elif disease == "Parkinson's":
    st.title("🧠 Parkinson's Disease Prediction")
    fhi = display_input('MDVP:Fhi(Hz)', 'MDVP_Fhi_Hz')
    flo = display_input('MDVP:Flo(Hz)', 'MDVP_Flo_Hz')
    Jitter_percent = display_input('MDVP:Jitter(%)', 'MDVP_Jitter_Percent')
    Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'MDVP_Jitter_Abs')
    RAP = display_input('MDVP:RAP', 'MDVP_RAP')
    PPQ = display_input('MDVP:PPQ', 'MDVP_PPQ')
    DDP = display_input('Jitter:DDP', 'Jitter_DDP')
    Shimmer = display_input('MDVP:Shimmer', 'MDVP_Shimmer')
    Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'MDVP_Shimmer_dB')
    APQ3 = display_input('Shimmer:APQ3', 'Shimmer_APQ3')
    APQ5 = display_input('Shimmer:APQ5', 'Shimmer_APQ5')
    APQ = display_input('MDVP:APQ', 'MDVP_APQ')
    DDA = display_input('Shimmer:DDA', 'Shimmer_DDA')
    NHR = display_input('NHR', 'NHR_Value')
    HNR = display_input('HNR', 'HNR_Value')
    RPDE = display_input('RPDE', 'RPDE_Value')
    DFA = display_input('DFA', 'DFA_Value')
    spread1 = display_input('Spread1', 'Spread1_Value')
    spread2 = display_input('Spread2', 'Spread2_Value')
    D2 = display_input('D2', 'D2_Value')
    PPE = display_input('PPE', 'PPE_Value')

    
    if st.button("🔍 Predict Parkinson’s"):
        result = models['parkinsons'].predict([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE])
        st.success("Parkinson's Detected" if result[0] == 1 else "No Parkinson's Disease")

elif disease == "Lung Cancer":
    st.title("🫁 Lung Cancer Prediction")
    GENDER = display_input('Gender (1 = Male; 0 = Female)', 'GENDER')
    AGE = display_input('Age', 'AGE')
    SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'SMOKING')
    YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'YELLOW_FINGERS')
    ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'ANXIETY')
    PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'PEER_PRESSURE')
    CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'CHRONIC_DISEASE')
    FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'FATIGUE')
    ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'ALLERGY')
    WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'WHEEZING')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'ALCOHOL_CONSUMING')
    COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'COUGHING')
    SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'SHORTNESS_OF_BREATH')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'SWALLOWING_DIFFICULTY')
    CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'CHEST_PAIN')
    if st.button("🔍 Predict Lung Cancer"):
        result = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        st.success("Lung Cancer Detected" if result[0] == 1 else "No Lung Cancer")

elif disease == "Hypo-Thyroid":
    st.title("🦋 Hypo-Thyroid Prediction")
    age = display_input('Age', 'age')
    sex = display_input('Sex (1=Male, 0=Female)', 'sex')
    on_thyroxine = display_input('On Thyroxine (1=Yes, 0=No)', 'on_thyroxine')
    tsh = display_input('TSH Level', 'tsh')
    t3_measured = display_input('T3 Measured (1=Yes, 0=No)', 't3_measured')
    t3 = display_input('T3 Level', 't3')
    tt4 = display_input('TT4 Level', 'tt4')
    if st.button('🔍 Predict Hypo-Thyroid'):
        result = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        st.success("Hypo-Thyroid Detected" if result[0] == 1 else "No Hypo-Thyroid")
