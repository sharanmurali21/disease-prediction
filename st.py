import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\jaiak\Downloads\disease.pkl")

# Streamlit UI
st.title("Disease Prediction App")
st.write("Enter the following values to check for diseases.")

# Define input fields
feature_names = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
   'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
   'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
   'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1',
   'spread2', 'D2', 'PPE', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
   'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal',
   'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
   'BMI', 'DiabetesPedigreeFunction']

# Collect user inputs
user_inputs = []
for feature in feature_names:
    value = st.number_input(f"{feature}", value=0.0)
    user_inputs.append(value)

# Predict button
if st.button("Predict"):
    # Convert inputs to NumPy array
    user_input = np.array([user_inputs])

    # Make prediction
    prediction = model.predict(user_input)
    status, target, outcome = prediction[0]

    # Interpret results
    diseases = []
    if status == 1:
        diseases.append("Parkinson's Disease")
    if target == 1:
        diseases.append("Heart Disease")
    if outcome == 1:
        diseases.append("Diabetes")

    # Display result
    if diseases:
        st.success(f"The model predicts: **{', '.join(diseases)}**")
    else:
        st.success("The model predicts: **No Disease Detected**")
