import streamlit as st
import pickle
import numpy as np

# st.markdown("# CROP PREDICTION")


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        dataa = pickle.load(file)
    return dataa


dataa = load_model()

classifierr = dataa["model"]


def crop_analytics():
    st.header("CROP  PREDICTION")

    st.write("""Enter the details:""")

    N = st.number_input("Sodium")
    P = st.number_input("Phosphorous")
    K = st.number_input("Potassium")
    temperature = st.number_input("Temperature")
    humidity = st.number_input("humidity")
    ph = st.number_input("pH")
    rainfall = st.number_input("Rainfall")

    ok = st.button("PREDICT")

    st.write("THE MOST SUITABLE CROP IS:")

    if(ok):
        a = classifierr.predict([[N, P, K, temperature, humidity, rainfall]])
        # st.write(a)
        if(a == 0):
            st.write('**APPLE**')
        if(a == 1):
            st.write('**BANANA**')
        if(a == 2):
            st.write('**BLACKGRAM**')
        if(a == 3):
            st.write('**CHICKPEA**')
        if(a == 4):
            st.write('**COCONUT**')
        if(a == 5):
            st.write('**COFFEE**')
        if(a == 6):
            st.write('**COTTON**')
        if(a == 7):
            st.write('**GRAPES**')
        if(a == 8):
            st.write('**JUTE**')
        if(a == 9):
            st.write('**KIDNEYBEANS**')
        if(a == 10):
            st.write('**LENTIL**')
        if(a == 11):
            st.write('**MAIZE**')
        if(a == 12):
            st.write('**MANGO**')
        if(a == 13):
            st.write('**MOTHBEANS**')
        if(a == 14):
            st.write('**MUGBEANS**')
        if(a == 15):
            st.write('**MUSKMELON**')
        if(a == 16):
            st.write('**ORANGE**')
        if(a == 17):
            st.write('**PAPAYA**')
        if(a == 18):
            st.write('**PIGEONPEAS**')
        if(a == 19):
            st.write('**POMEGRANATE**')
        if(a == 20):
            st.write('**RICE**')
        if(a == 21):
            st.write('**WATERMELON**')
