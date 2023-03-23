#Group - 4
#John Paul Sapasap
#Jed Andrew Del Rosario
#Marc Joshua 

import numpy as np
import cv2 
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from io import StringIO

   

def read_image(path):
    img = cv2.imread(path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



def translation_img(img,x,y):
    rows, cols = img.shape[:2]
    m_translation_=np.float32([[1,0,x],
                        [0,1,y],
                        [0,0,1]])

    translated_img_=cv2.warpPerspective(img,m_translation_,(cols, rows))
    return translated_img_


def rotation_img(img,x,y):

    angle =np.radians(10)
    rows, cols = img.shape[:2]
    m_rotation_=np.float32([[np.cos(x), -(np.sin(y)), 0],
                        [np.sin(y), np.cos(x),0],
                        [0,0,1]])

    m_rotation_=cv2.getRotationMatrix2D((cols/2,rows/2), 60,1)
    rotated_img_ = cv2.warpAffine(img,m_rotation_,(cols,rows))
    return rotated_img_



def scaling_img(img,x,y):
    rows, cols = img.shape[:2]
    m_scaling_=np.float32([[x,0,0],
                       [0,y,0],
                       [0,0,1]])
    scaled_img_ =cv2.warpPerspective(img,m_scaling_,(cols*2,rows*2))
    return scaled_img_



def reflection_img(img,x,y):
    rows, columns = img.shape[:2]
    m_reflection_ =np.float32([[x,0,0],
                          [0,y,rows],
                          [0,0,1]])
    reflected_img_ =cv2.warpPerspective(img,m_reflection_,(int(columns),int (rows)))
    return reflected_img_


def shear_img(img,x,y):
    x, y = img.shape[:2]
    m_shearing_x=np.float32([[1,0.5,0],
                         [0,1,0],
                         [0,0,1]])

    sheared_img_x = cv2.warpPerspective(img,m_shearing_x,(int(y*1.5),int(x*1.5)))

    return sheared_img_x

def main():
    st.title("Image Transformations")

    # file upload
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # read image
        bytes_data = uploaded_file.read()
        nparr = np.frombuffer(bytes_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        img = read_image("flower.jpg")
        
        
    st.sidebar.title("Select Transformation")
    transformation = st.sidebar.selectbox("Select Transformation", ("Translation", "Rotation","Scaled","Reflected","Sheared"))

    x = st.sidebar.number_input("Enter the value of x:")
    y = st.sidebar.number_input("Enter the value of y:")

    # perform transformations
    translated_img_ = translation_img(img,x,y)
    rotated_img_ = rotation_img(img,x,y)
    scaled_img_ = scaling_img(img,x,y)
    reflected_img_ = reflection_img(img,x,y)
    sheared_img_x = shear_img(img,x,y)

    # show images
    st.subheader("Original Image")
    st.image(img)
    if (transformation=="Translation"):
        st.subheader("Translated Image")
        st.image(translated_img_)
    elif(transformation=="Rotation"):
        st.subheader("Rotated Image")
        st.image(rotated_img_)
    elif(transformation=="Scaled"):
        st.subheader("Scaled Image")
        st.image(scaled_img_)
    elif(transformation=="Reflected"):
        st.subheader("Reflected Image")
        st.image(reflected_img_)
    elif(transformation=="Sheared"):
        st.subheader("Sheared Image")
        st.image(sheared_img_x)

    plt.show()
    
main()







    








