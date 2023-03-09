import streamlit as st
import numpy as np
import matplotlib as plt
import cv2
from io import StringIO
import pandas as pd

st.title ("Hello World")




uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)