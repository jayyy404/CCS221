#Group 4
#John Paul Sapasap
#Jed Andrew Del Rosario
#Marc Joshua Escueta

import cv2
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def read_image(path):
    img = cv2.imread(path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def translate_image(img, bx, by):
    rows, cols = img.shape[:2]
    m = np.float32([[1, 0, bx], [0, 1, by]])
    return cv2.warpAffine(img, m, (cols, rows))

def new_translated(img, bx_old, by_old, tx, ty,x,y):
    bx_new = bx_old + tx *x
    by_new = by_old + ty*y
    return translate_image(img, bx_new, by_new)

def main():
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # read image
        bytes_data = uploaded_file.read()
        nparr = np.frombuffer(bytes_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        img = read_image("flower.jpg")

    # IMAGES WITH ORIGINAL VALUES
    translated_imgs = []
    for bx, by in zip(range(2, 7), range(5, 10)):
        translated_imgs.append(translate_image(img, bx, by))
        
    x = st.sidebar.number_input("Enter the value of x:")
    y = st.sidebar.number_input("Enter the value of y:")

    # IMAGES WITH NEW VALUES
    modified_imgs = []
    for bx_old, by_old, tx, ty in [(2, 5, 6, 2), (3, 6, 7, 3), (4, 7, 8, 4), (5, 8, 9, 5), (6, 9, 10, 3)]:
        modified_imgs.append(new_translated(img, bx_old, by_old, tx, ty,x,y))

    # Display images using st.pyplot()
    st.subheader("Original")
    st.image(translated_imgs)
    for i in range(5):
        st.subheader(f"Original {i+1}")
        
        st.subheader(f"# {i+1}")
        st.image(modified_imgs[i])

main()