import streamlit as st
import base64
import supervision as sv
from inference_sdk import InferenceHTTPClient
from PIL import Image, ImageDraw, ImageOps


st.set_page_config(page_title="Apda-Mitra", page_icon=" ",initial_sidebar_state='expanded')

@st.cache_data
def showGif():
    file_ = open("./assets/apda_mitra.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="Apda-Mitra">',
            unsafe_allow_html=True,)

st.title("Apda-Mitra: Empowering Change, One Hand at a Time ")
st.divider()
st.subheader("TARGET ")
st.markdown("From Space to Safety: Advancing Disaster Relief with Satellite Technology. Enhance disaster relief and response efforts by leveraging satellite imagery during disasters like floods and wildfires, integrating existing geospatial information, and utilizing environmental data for affected regions ")
st.divider()
showGif()
st.subheader("Challenges in Post-Disaster Recovery and Relief ")
st.markdown("**Poor Resource Management**")
st.markdown("**Information about disasters are usually shared after 15 min.**")
st.markdown("**Limited Situational Awareness**")
st.divider()
st.subheader("Solution ")
st.image('./assets/app_asset.png')



