
import streamlit as st
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

st.set_page_config(page_title="House Price Predictor", layout="centered")

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

# Mini eğitim verisi (örnek amaçlı)
X_train = np.random.rand(100, 7)
y_train = X_train @ np.array([200, 150, 5000, 100, 3000, 4000, 1000]) + 50000

# Modeli her çalıştırmada yeniden eğit
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Tahmin
if st.button("Predict Price"):
    input_data = np.array([[GrLivArea, TotalBsmtSF, OverallQual, YearBuilt, GarageCars, FullBath, BedroomAbvGr]])
    prediction = model.predict(input_data)[0]
    st.success(f"🏠 Estimated House Price: ${prediction:,.2f}")
