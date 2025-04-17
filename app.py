
import streamlit as st
import joblib
import numpy as np

# Modeli yükle
model = joblib.load("clean_house_price_model.pkl")

st.title("🏡 House Price Prediction App")
st.write("Enter the property details below to estimate the house price:")

# Kullanıcıdan veri alma
GrLivArea = st.number_input("Living Area (GrLivArea in sq ft)", min_value=0, value=1500)
TotalBsmtSF = st.number_input("Basement Area (TotalBsmtSF in sq ft)", min_value=0, value=800)
OverallQual = st.slider("Overall Quality (1 - Poor to 10 - Excellent)", 1, 10, 5)
YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)
GarageCars = st.slider("Garage Capacity (Number of Cars)", 0, 5, 1)
FullBath = st.slider("Number of Full Bathrooms", 0, 5, 2)
BedroomAbvGr = st.slider("Number of Bedrooms Above Ground", 0, 10, 3)

# Tahmin
if st.button("Predict Price"):
    features = np.array([[GrLivArea, TotalBsmtSF, OverallQual, YearBuilt, GarageCars, FullBath, BedroomAbvGr]])
    prediction = model.predict(features)[0]
    st.success(f"🏠 Estimated House Price: ${prediction:,.2f}")
