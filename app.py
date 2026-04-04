import streamlit as st
import numpy as np
import pickle

# page config
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# load trained model
model = pickle.load(open("model.pkl", "rb"))

# UI styling
st.markdown("""
<style>

.stButton>button {
    background: linear-gradient(90deg,#4facfe,#00f2fe);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

.result-box {
    background: #0f172a;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    margin-top: 20px;
    font-size: 24px;
    font-weight: bold;
    color: #22c55e;
}

</style>
""", unsafe_allow_html=True)

# title
st.title("🏠 AI House Price Predictor")

st.write("Enter house details to estimate price using Machine Learning")

# layout
col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("Bedrooms", 0, 10)
    bathrooms = st.number_input("Bathrooms", 0, 10)
    sqft_living = st.number_input("Living Area (sqft)", 300, 10000)
    sqft_lot = st.number_input("Lot Area (sqft)", 300, 20000)
    floors = st.number_input("Floors", 1, 5)

with col2:
    waterfront = st.selectbox("Waterfront", [0,1])
    view = st.slider("View Rating", 0, 4)
    condition = st.slider("Condition", 1, 5)
    sqft_above = st.number_input("Sqft Above", 300, 10000)
    sqft_basement = st.number_input("Basement Sqft", 0, 5000)

yr_built = st.number_input("Year Built", 1900, 2026)
yr_renovated = st.number_input("Year Renovated (0 if never)", 0, 2026)

# prediction
if st.button("Predict Price"):

    features = np.array([[

        bedrooms,
        bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        waterfront,
        view,
        condition,
        sqft_above,
        sqft_basement,
        yr_built,
        yr_renovated

    ]])

    prediction = model.predict(features)

    st.markdown(f"""
    <div class="result-box">
    Estimated Price: ₹ {prediction[0]:,.0f}
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Built using Machine Learning & Streamlit 🚀")