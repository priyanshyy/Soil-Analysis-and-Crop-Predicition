import streamlit as st
import base64
import numpy as np
import streamlit.components.v1 as components


def local_css(styles):
    with open(styles) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("styles.css")


# st.markdown("# HOME")


def landing_page():
    components.html(
        """
        <h1 style="margin-top:4rem">KRISHI SUVIDHA<h1>   
    """
    )
    st.write("SOIL ANALYSIS AND CROP PREDICTION")

    st.write("BY:")

    components.html(
        """
            <p style="margin-top:-0.7rem">Neha Adlakha</p>
            <p>Pragati Chaturvedi</p>
            <p>Prateeksha</p>
            <p>Priyanshi Chaudhary</p>
        """
    )
