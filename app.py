import streamlit as st
import pandas as pd
import joblib

# Load the saved Random Forest Regression model
filename = "best_model_random_forest.pkl"
loaded_model = joblib.load(filename)

# Function to make predictions
# Function to make predictions
def predict_price(year, km_driven, fuel, seller_type, transmission, owner, manufacturer, model, variant):
    features = pd.DataFrame({
        'year': [year],
        'km_driven': [km_driven],
        'fuel': [fuel],
        'seller_type': [seller_type],
        'transmission': [transmission],
        'owner': [owner],
        'Manufacturer': [manufacturer],
        'Model': [model],
        'Variant': [variant]
    })

    # One-hot encode the categorical features
    features_encoded = pd.get_dummies(features, columns=['fuel', 'seller_type', 'transmission','Manufacturer','Model','Variant'])

    # Predict the price using the loaded model
    predicted_price = loaded_model.predict(features_encoded)[0]
    return predicted_price

# Streamlit app
def main():
    st.title("Car Selling Price Prediction")

    # Read the dataset from the .csv file
    df = pd.read_csv("CAR DETAILS.csv")

    # Input fields for user to enter car details
    year = st.slider("Select Year", min_value=2000, max_value=2023, value=2010)
    km_driven = st.number_input("Enter Kilometers Driven", min_value=0, value=50000)
    fuel = st.selectbox("Select Fuel Type", df['fuel'].unique())
    seller_type = st.selectbox("Select Seller Type", df['seller_type'].unique())
    transmission = st.selectbox("Select Transmission", df['transmission'].unique())
    owner = st.slider("Select Number of Previous Owners", min_value=0, max_value=5, value=1)
    manufacturer = st.selectbox("Select Manufacturer", df['Manufacturer'].unique())
    model = st.selectbox("Select Model", df['Model'].unique())
    variant = st.selectbox("Select Variant", df['Variant'].unique())

    # Predict button
    if st.button("Predict Selling Price"):
        predicted_price = predict_price(year, km_driven, fuel, seller_type, transmission, owner, manufacturer, model, variant)
        st.success(f"Predicted Selling Price: {predicted_price:.2f} INR")

if __name__ == "__main__":
    main()
