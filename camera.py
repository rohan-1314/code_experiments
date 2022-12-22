import streamlit as st
from PIL import Image
with st.expander('start camera'):
    # create camera input in browser
    camera = st.camera_input('camera')
if camera:
    # create pillow image instance
    img = Image.open(camera)
    # convert pillow ing to grayscale
    gray = img.convert('L')
    # display img on browser
    st.image(gray)