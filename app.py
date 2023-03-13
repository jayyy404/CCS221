import streamlit as st
import numpy as np
import matplotlib as plt
import cv2
from io import StringIO
import pandas as pd

st.title ("Hello World")




uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
        # read image
    bytes_data = uploaded_file.read()
    nparr = np.frombuffer(bytes_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
else:
    img = read_image("flower.jpg")