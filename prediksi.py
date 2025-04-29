import streamlit as st
import numpy as np
import pandas as pd
import pickle

with open('xgbr_tunned_model.pkl', 'rb') as file:
    XGBR_model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('ordinal_encoder.pkl', 'rb') as file:
    ordinal_encoder = pickle.load(file)
    
def run_ml_app():
    with st.container():    
        st.markdown(
            """
                <h1 style="text-align: center; color:#9F8335">Diamond Price Prediction Application</h1>
            """,
            unsafe_allow_html=True
        )    

    left, right = st.columns((2,2))
    cut = left.selectbox(
        'Cut',
        ('Ideal', 'Premium', 'Very Good', 'Good', 'Fair'),
        help='Quality of the cut: Ideal > Premium > Very Good > Good > Fair'
    )

    color = right.selectbox(
        'Color',
        ('D', 'E', 'F', 'G', 'H', 'I', 'J'),
        help='Diamond colour, from J (worst) to D (best)'
    )

    clarity = left.selectbox(
        'Clarity',
        ('IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'),
        help='Clarity level: I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best)'
    )

    carat = right.number_input(
        'Carat',
        min_value=0.2,
        max_value=5.01,
        step=0.01,
        help='Weight of the diamond (0.2 to 5.01 carats)'
    )

    x = left.number_input(
        'x (Length in mm)',
        min_value=0.0,
        max_value=10.74,
        step=0.01,
        help='Length of the diamond in millimeters (0 to 10.74 mm)'
    )

    y = left.number_input(
        'y (Width in mm)',
        min_value=0.0,
        max_value=58.9,
        step=0.01,
        help='Width of the diamond in millimeters (0 to 58.9 mm)'
    )

    z = left.number_input(
        'z (Depth in mm)',
        min_value=0.0,
        max_value=31.8,
        step=0.01,
        help='Depth of the diamond in millimeters (0 to 31.8 mm)'
    )
    button = st.button('Prediksi Harga')

    if button:
        input_data = pd.DataFrame([{
            'cut': cut,
            'color': color,
            'clarity': clarity,
            'carat': carat,
            'x': x,
            'y': y,
            'z': z
        }], columns=['cut', 'color', 'clarity', 'carat', 'x', 'y', 'z'])

        result = predict(input_data)

        st.markdown("""
            <div style="background-color:#F0EAD6; padding:20px; border-radius:10px; border: 1px solid #D0B49F">
                <h3 style="color:#9F8335; text-align:center;">💎 Prediksi Harga Berlian 💎</h3>
                <h1 style="color:#4CAF50; text-align:center;">${:,.2f}</h1>
            </div>
        """.format(result), unsafe_allow_html=True)

        st.info("✨ Perkiraan harga ini didasarkan pada model Machine Learning dengan input yang Anda berikan.")
        st.markdown('<h3 style="color:#9F8335;">Detail Input Pengguna:</h3', unsafe_allow_html=True)
        st.table(input_data)

def predict(input_data):
    input_copy = input_data.copy()
    categorical_features = ['cut', 'color', 'clarity']
    input_copy[categorical_features] = ordinal_encoder.transform(input_copy[categorical_features])
    features_scaled = scaler.transform(input_copy)
    predicted_log_price = XGBR_model.predict(features_scaled)[0]
    predicted_price = np.exp(predicted_log_price)

    return predicted_price
