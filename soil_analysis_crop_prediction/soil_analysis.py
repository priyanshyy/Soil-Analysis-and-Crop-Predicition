import pandas as pd
import numpy as np
import pickle
import streamlit as st

# st.markdown("# SOIL ANALYSIS")


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        dataa = pickle.load(file)
    return dataa


dataa = load_model()

classifierr = dataa["model"]


def soil_analytics():
    st.header("SOIL ANALYSIS")

    st.write("""Enter the details:""")

    N = st.number_input("Sodium")
    P = st.number_input("Phosphorous")
    K = st.number_input("Potassium")
    temperature = st.number_input("Temperature")
    humidity = st.number_input("humidity")
    ph = st.number_input("pH")
    rainfall = st.number_input("Rainfall")
    #crop = st.text_input("CROP ")
    crop = st.selectbox('Crop',
                        ('APPLE', 'BANANA', 'BLACKGRAM', 'CHICKPEA', 'COCONUT', 'COFFEE', 'COTTON', 'GRAPES', 'JUTE', 'KIDNEYBEANS', 'LENTIL', 'MAIZE', 'MANGO', 'MOTHBEANS', 'MUGBEANS', 'MUSKMELON', 'ORANGE', 'PAPAYA', 'PIGEONPEAS', 'POMEGRANATE', 'RICE', 'WATERMELON'))

    ok = st.button("Submit")

    if(ok):
        a = classifierr.predict([[N, P, K, temperature, humidity, rainfall]])
        st.header(
            "  ACCORDING TO THE MENTIONED SOIL CONDITIONS THE MOST SUITABLE CROP TO BE GROWN IS  ")
        a = classifierr.predict([[N, P, K, temperature, humidity, rainfall]])
        # st.write(a)
        if(a == 0):
            st.write('APPLE')
        if(a == 1):
            st.write('BANANA')
        if(a == 2):
            st.write('BLACKGRAM')
        if(a == 3):
            st.write('CHICKPEA')
        if(a == 4):
            st.write('COCONUT')
        if(a == 5):
            st.write('COFFEE')
        if(a == 6):
            st.write('COTTON')
        if(a == 7):
            st.write('GRAPES')
        if(a == 8):
            st.write('JUTE')
        if(a == 9):
            st.write('KIDNEYBEANS')
        if(a == 10):
            st.write('LENTIL')
        if(a == 11):
            st.write('MAIZE')
        if(a == 12):
            st.write('MANGO')
        if(a == 13):
            st.write('MOTHBEANS')
        if(a == 14):
            st.write('MUGBEANS')
        if(a == 15):
            st.write('MUSKMELON')
        if(a == 16):
            st.write('ORANGE')
        if(a == 17):
            st.write('PAPAYA')
        if(a == 18):
            st.write('PIGEONPEAS')
        if(a == 19):
            st.write('POMEGRANATE')
        if(a == 20):
            st.write('RICE')
        if(a == 21):
            st.write('WATERMELON')

        st.header("  APPROPRIATE VALUES REQUIRED TO GROW THE GIVEN CROP  ")

        df = pd.read_csv("average_recommendation.csv")
        # col=crop
        # st.table(df[col])
        if(crop == 'APPLE'):
            st.write(
                'Sodium: 20.8  ||  Phosphorus: 134.22  || Potassium: 199.89  ||  Temperature: 22.6309424 ||  Humidity: 92.3333829  ||  pH: 5.92966293  || Rainfall: 112.654779')
        elif(crop == 'BANANA'):
            st.write(
                'Sodium: 100.23  ||  Phosphorus: 82.01  ||  Potassium: 50.05  ||  Temperature: 27.3767983  ||  Humidity: 80.3581226 ||  pH: 5.98389318 ||  Rainfall: 104.62698 ')

        elif(crop == 'BLACKGRAM'):
            st.write(
                'Sodium: 40.02 ||  Phosphorus: 67.47  || Potassium: 19.24  || Temperature: 29.97334  ||  Humidity: 65.118426  ||  pH: 7.1339516 ||  Rainfall: 67.884151 ')
        elif(crop == 'CHICKPEA'):
            st.write(
                'Sodium: 40.09  ||  Phosphorus: 67.79  ||   Potassium: 79.92   ||  Temperature: 18.872847    ||   Humidity: 16.860439  ||   pH: 7.3369566  ||  Rainfall: 80.058977 ')
        elif(crop == 'COCONUT'):
            st.write(
                'Sodium: 21.98   ||  Phosphorus: 16.93   ||  Potassium: 30.59  ||  Temperature: 27.4098922    ||   Humidity: 94.8442718   ||  pH: 5.97656213   ||   Rainfall: 175.686646 ')
        elif(crop == 'COFFEE'):
            st.write(
                'Sodium: 101.2   ||   Phosphorus: 28.74    ||   Potassium: 29.94    ||   Temperature: 25.5404768   ||    Humidity: 58.8698463   ||   pH: 6.79030827  ||   Rainfall: 158.066295 ')
        elif(crop == 'COTTON'):
            st.write(
                'Sodium: 117.77   ||   Phosphorus: 46.24   ||    Potassium: 19.56    ||   Temperature: 23.9889579   ||    Humidity: 79.8434743    ||    pH: 6.9126755   ||   Rainfall: 80.3980431 ')
        elif(crop == 'GRAPES'):
            st.write(
                'Sodium:23.18  ||  Phosphorus: 132.53    ||   Potassium: 200.11   ||    Temperature: 23.8495751   ||   Humidity: 81.8752275      pH: 6.02593668      Rainfall: 69.6118289 ')
        elif(crop == 'JUTE'):
            st.write(
                'Sodium: 78.4   ||   Phosphorus: 46.86  ||   Potassium: 39.99  ||   Temperature: 24.9583758  ||   Humidity: 79.6398642  ||   pH: 6.73277757  ||   Rainfall: 174.792798 ')
        elif(crop == 'KIDNEYBEANS'):
            st.write(
                'Sodium: 20.75  ||   Phosphorus: 67.54  ||   Potassium: 20.05  ||   Temperature: 20.115085   ||   Humidity: 21.605357   ||   pH: 5.7494106  ||  Rainfall: 105.91978 ')
        elif(crop == 'LENTIL'):
            st.write(
                'Sodium: 18.77  ||   Phosphorus: 68.36  ||   Potassium: 19.41  ||   Temperature: 24.5090524  ||   Humidity: 64.8047847  ||   pH: 6.92793157  ||   Rainfall: 45.6804542 ')
        elif(crop == 'MAIZE'):
            st.write(
                'Sodium: 77.76  ||   Phosphorus: 48.44  ||   Potassium: 19.79  ||   Temperature: 22.389204   ||   Humidity: 65.092249   ||   pH: 6.2451897  ||   Rainfall: 84.766988')
        elif(crop == 'MANGO'):
            st.write(
                'Sodium: 20.07  ||   Phosphorus: 27.18  ||   Potassium: 29.92  ||   Temperature: 31.2087702  ||   Humidity: 50.1565727  ||   pH: 5.7663728  ||   Rainfall: 94.704515 ')
        elif(crop == 'MOTHBEANS'):
            st.write(
                'Sodium: 21.44  ||   Phosphorus: 48.01  ||   Potassium: 20.23  ||   Temperature: 28.19492  ||   Humidity: 53.160418  ||   pH: 6.8311741  ||   Rainfall: 51.198487 ')
        elif(crop == 'MUGBEANS'):
            st.write(
                'Sodium: 20.99  ||   Phosphorus: 47.28  ||   Potassium: 19.87  ||   Temperature: 28.525775  ||   Humidity: 85.499975  ||   pH: 6.7239569  ||   Rainfall: 48.403601 ')
        elif(crop == 'MUSKMELON'):
            st.write(
                'Sodium: 100.32  ||   Phosphorus: 17.72  ||   Potassium: 50.08  ||   Temperature: 28.6630658  ||   Humidity: 92.342802  ||   pH: 6.35880545  ||   Rainfall: 24.6899521 ')
        if(crop == 'ORANGE'):
            st.write(
                'Sodium: 19.58  ||   Phosphorus: 16.55  ||   Potassium: 10.01  ||   Temperature: 22.7657255  ||   Humidity: 92.1702088  ||   pH: 7.01695745  ||   Rainfall: 110.474969 ')
        if(crop == 'PAPAYA'):
            st.write(
                'Sodium: 49.88  ||   Phosphorus: 59.05  ||   Potassium: 50.04  ||   Temperature: 33.7238587  ||   Humidity: 92.4033877  ||   pH: 6.74144237  ||   Rainfall: 142.627839 ')
        elif(crop == 'PIGEONPEAS'):
            st.write(
                'Sodium: 20.73  ||   Phosphorus: 67.73  ||   Potassium: 20.73  ||   Temperature: 27.741762  ||   Humidity: 48.061633  ||   pH: 5.7941749  ||   Rainfall: 149.45756 ')
        elif(crop == 'POMEGRANATE'):
            st.write(
                'Sodium: 18.87  ||   Phosphorus: 18.75  ||   Potassium: 40.21  ||   Temperature: 21.8378417  ||   Humidity: 90.1255038  ||   pH: 6.42917184  ||   Rainfall: 107.528442 ')
        elif(crop == 'RICE'):
            st.write(
                'Sodium: 79.89  ||   Phosphorus: 47.58  ||   Potassium: 39.87  ||   Temperature: 23.689332  ||   Humidity: 82.272822  ||   pH: 6.4254709  ||   Rainfall: 236.18111 ')
        elif(crop == 'WATERMELON'):
            st.write(
                'Sodium: 99.42  ||   Phosphorus: 17  ||   Potassium: 50.22  ||   Temperature: 25.5917672  ||   Humidity: 85.1603753  ||   pH: 6.4957783  ||  S Rainfall: 50.7862189 ')
