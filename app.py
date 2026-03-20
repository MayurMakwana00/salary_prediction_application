import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("salary_model.pkl")

st.title(" Salary Prediction App")

st.write("Enter employee details")

# Inputs
experience = st.slider("Experience (Years)", 0, 10, 2)
skills = st.slider("Skills Count", 1, 20, 5)
certifications = st.slider("Certifications", 0, 10, 1)

job_title = st.selectbox("Job Title", ["Data Scientist", "Software Engineer", "Manager"])
education = st.selectbox("Education Level", ["Bachelors", "Masters", "PhD"])
industry = st.selectbox("Industry", ["IT", "Finance", "Healthcare"])
company_size = st.selectbox("Company Size", ["Small", "Medium", "Large"])
location = st.selectbox("Location", ["Ahmedabad", "Mumbai", "Delhi"])
remote = st.selectbox("Remote Work", ["Yes", "No"])

# Predict
if st.button("Predict Salary 💰"):

    input_df = pd.DataFrame([{
        'job_title': job_title,
        'experience_years': experience,
        'education_level': education,
        'skills_count': skills,
        'industry': industry,
        'company_size': company_size,
        'location': location,
        'remote_work': remote,
        'certifications': certifications
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated Salary: ₹{int(prediction):,}")