import streamlit as st
import pandas as pd
import pickle

#load the House_Price_Prediction_model 
model = pickle.load(open('House_Price_Prediction_model.pkl', 'rb'))
#load cleaned data
df = pd.read_csv('cleaned_data.csv')

#location options
locations = sorted(df['location'].unique())

#set page title name
st.set_page_config(page_title="House Price Predictor")

#app heading name 
st.title("House Price Prediction")
st.write("Enter the details below to predict house price:")

# create input fields 
location = st.selectbox("Select Location", locations)
total_sqft = st.number_input("Total Square Feet", min_value=300)
balcony = st.number_input("Number of Balconies", min_value=0, max_value=5, step=1)
bhk = st.number_input("Number of Bedrooms (BHK)", min_value=1, max_value=10, step=1)

#create predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame([[location, total_sqft, balcony, bhk]], 
                            columns=['location', 'total_sqft', 'balcony', 'bedrooms'])
    
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price is : ₹ {round(prediction, 2)} lakhs")
