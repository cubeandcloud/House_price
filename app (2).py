
import streamlit as st
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

st.set_page_config(page_title="🏡 House Price Estimator", layout="centered")
st.title("🏡 House Price Prediction App")
st.write("Enter the house details below to estimate the sale price:")

# Kullanıcıdan veri al
GrLivArea = st.number_input("Living Area (GrLivArea in sq ft)", value=1694)
TotalBsmtSF = st.number_input("Basement Area (TotalBsmtSF in sq ft)", value=1686)
OverallQual = st.slider("Overall Quality (1 - Poor to 10 - Excellent)", 1, 10, 8)
YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025, value=2004)
GarageCars = st.slider("Garage Capacity (Number of Cars)", 0, 5, 2)
FullBath = st.slider("Number of Full Bathrooms", 0, 5, 2)
BedroomAbvGr = st.slider("Number of Bedrooms Above Ground", 0, 10, 3)

# Küçük ve gerçekçi örnek veri ile inline model eğitimi
X = np.array([
    [1694, 1686, 8, 2004, 2, 2, 3],   # 307000
    [2000, 1800, 7, 2001, 2, 2, 4],   # 285000
    [2500, 2000, 9, 2010, 3, 3, 4],   # 410000
    [1800, 1500, 6, 1995, 2, 2, 3],   # 240000
    [1200, 1000, 5, 1980, 1, 1, 2]    # 175000
])
y = np.array([307000, 285000, 410000, 240000, 175000])

model = GradientBoostingRegressor()
model.fit(X, y)

# Tahmin
if st.button("Predict Price"):
    features = np.array([[GrLivArea, TotalBsmtSF, OverallQual, YearBuilt, GarageCars, FullBath, BedroomAbvGr]])
    prediction = model.predict(features)[0]
    st.success(f"🏠 Estimated Sale Price: ${prediction:,.2f}")
