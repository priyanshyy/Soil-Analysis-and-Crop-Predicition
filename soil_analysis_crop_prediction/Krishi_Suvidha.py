from crop_pred import crop_analytics
from soil_analysis import soil_analytics
from homepage import landing_page
from streamlit_option_menu import option_menu
import streamlit as st
# st.set_page_config(
#     page_title="KRISHI SUVIDHA",
#     layout="wide")


selected = option_menu(
    menu_title=None,
    options=["Home", "Soil Analysis", "Crop Prediction"],
    icons=["house", "bar-chart-line", "flower3"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"background-color": "#e6e6e6", "width": "100%", "height": "4rem"},
        "nav-link": {
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "blue"}
    }
)

if selected == "Home":
    landing_page()
if selected == "Soil Analysis":
    soil_analytics()
if selected == "Crop Prediction":
    crop_analytics()
