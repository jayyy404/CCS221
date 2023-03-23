#Group 4
#John Paul Sapasap
#Jed Andrew Del Rosario
#Marc Joshua Escueta

import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

# functions for modifying the images
def translation_img(imgs,x,y):
    rows, cols = imgs.shape[:2]
    m_translation = np.float32([[1, 0, x], [0, 1, y]])
    translated_img = cv2.warpAffine(imgs, m_translation, (cols, rows))
    return translated_img

def rotation_img(imgs,x,y):
    rows, cols = imgs.shape[:2]
    #angle = 10
    m_rotation = cv2.getRotationMatrix2D((cols/2, rows/2), x, y)
    rotated_img = cv2.warpAffine(imgs, m_rotation, (cols, rows))
    return rotated_img

def scaling_img(imgs,x,y):
    rows, cols = imgs.shape[:2]
    m_scaling = np.float32([[x, 0, 0], [0, y, 0]])
    scaled_img = cv2.warpAffine(imgs, m_scaling, (int(cols*2), int(rows*2)))
    return scaled_img

def reflection_img(imgs,x,y):
    rows, cols = imgs.shape[:2]
    m_reflection = np.float32([[x, 0, 0], [0, y, rows]])
    reflected_img = cv2.warpAffine(imgs, m_reflection, (cols, rows))
    return reflected_img

def shear_img(imgs,x,y):
    rows, cols = imgs.shape[:2]
    m_shearing = np.float32([[1, x, 0], [0, y, 0], [0, 0, 1]])
    sheared_img = cv2.warpPerspective(imgs, m_shearing, (int(cols*1.5), int(rows*1.5)))
    return sheared_img

def main():
    st.set_page_config(page_title="Image Transformations", page_icon=":camera:")

        
        
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # read image
        bytes_data = uploaded_file.read()
        nparr = np.frombuffer(bytes_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        img = read_image("flower.jpg")
    st.image(img, use_column_width=True, caption="Original Image")
    
    st.sidebar.title("Select Transformation")
    transformation = st.sidebar.selectbox("Select Transformation", ("Translation", "Rotation","Scaled","Refelected","Sheared"))

    x1 = st.sidebar.number_input("Enter the Starting point of x:")
    y1 = st.sidebar.number_input("Enter the Starting point of y:")
        
        
    if (transformation=="Translation"):
        translated_img = translation_img(img)
        st.image(translated_img, use_column_width=True, caption="Translated Image")
    elif (transformation=="Rotation"):
        rotated_imgs = rotation_img(img)
        st.image(rotated_imgs, use_column_width=True, caption="Rotated Image")
    elif(transformation=="Scaled"):
        scaled_img = scaling_img(img)
        st.image(scaled_img, use_column_width=True, caption="Scaled Image")
    elif(transformation=="Reflected"):
        reflected_img = reflection_img(img)
        st.image(reflected_img, use_column_width=True, caption="Reflected Image")
    elif(transformation=="Sheared"):
        sheared_img = shear_img(img)
        st.image(sheared_img, use_column_width=True, caption="Sheared Image")

main()





