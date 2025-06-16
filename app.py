import streamlit as st
# import pandas as pd
import numpy as np
import joblib


st.title(' House Price Prediction')

st.divider()

st.write('This app predicts the price of a house based on various features.')

st.divider()

bedrooms = st.number_input('Number of Bedrooms', min_value=0, value=0)
bathrooms = st.number_input('Number of Bathrooms', min_value=0, value=0) 
living_area = st.number_input('Living Area (sq ft)', min_value=0, value=2000)
lot_area = st.number_input('Lot Area (sq ft)', min_value=0, value=5000)
property_age = st.number_input('Property Age (years)', min_value=0, value=10)        


st.divider()
model= joblib.load('model/House_price_model.pkl')

x=[[bedrooms, bathrooms, living_area, lot_area, property_age]]

predictbutton = st.button('Predict Price')
if predictbutton:
    # st.loding('building model...')
    st.balloons()
    X_array = np.array(x)
    prediction = model.predict(X_array)
    st.write(f'The predicted price of the house is: ${prediction[0]:,.2f}')

else:
    st.write('Please enter the details of the house to get a price prediction.')
    
    
    
    
    
    # order of x number of bedrooms', 'number of bathrooms', 'living area', 'lot area',
    #    'Property_Age