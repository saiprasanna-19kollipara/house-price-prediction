import streamlit as st

st.set_page_config(page_title="House Price Estimator", layout="centered")
st.title("🏡 House Price Prediction App")

# Place selection
place = st.selectbox("Select Place", ["Chennai", "Hyderabad", "Bangalore", "Mumbai", "Delhi"])

# Define rate per sq.ft based on place
rates = {
    "Chennai": 6000,
    "Hyderabad": 7000,
    "Bangalore": 8000,
    "Mumbai": 10000,
    "Delhi": 8000
}
rate_per_sqft = rates[place]

# Input sliders
area = st.number_input("Enter Area (sq.ft)", min_value=100, max_value=10000, value=1500, step=50)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 2)
washrooms = st.slider("Number of Washrooms", 1, 10, 2)
parking = st.slider("Parking Slots", 0, 5, 1)

# Display input summary
st.subheader("📋 Your Input Summary")
st.write(f"- Place: **{place}**")
st.write(f"- Area: **{area} sq.ft**")
st.write(f"- Bedrooms: **{bedrooms}**")
st.write(f"- Washrooms: **{washrooms}**")
st.write(f"- Parking Slots: **{parking}**")

# Price estimation
base_price = 50000
price = (
    base_price +
    area * rate_per_sqft +
    bedrooms * 10000 +
    washrooms * 8000 +
    parking * 5000
)

# Output
st.subheader("💰 Estimated House Price")
st.success(f"₹ {price:,.0f}")
