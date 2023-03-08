#Group 4
#John Paul Sapasap
#Jed Andrew Del Rosario
#Marc Joshua Escueta

import numpy as np
import cv2 
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from io import StringIO

#functions for modifying the images
def translation_img(imgs):
    rows, cols = imgs.shape[:2]
    m_translation = np.float32([[1, 0, 100],
                                [0, 1, 50]])

    translated_img = cv2.warpAffine(imgs, m_translation, (cols, rows))
    
    return translated_img                           #returning the value to the main function where is(are) to be called 

def rotation_img(imgs):
    rows, cols = imgs.shape[:2]
    angle = 10
    m_rotation = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)

    rotated_img = cv2.warpAffine(imgs, m_rotation, (cols, rows))

    return rotated_img

def scaling_img(imgs):
    rows, cols = imgs.shape[:2]
    m_scaling = np.float32([[1.5, 0, 0],
                            [0, 1.8, 0]])

    scaled_img = cv2.warpAffine(imgs, m_scaling, (int(cols*2), int(rows*2)))
    
    return scaled_img

def reflection_img(imgs):
    rows, cols = imgs.shape[:2]
    m_reflection = np.float32([[1, 0,0],
                               [0,-1,rows]])

    reflected_img = cv2.warpAffine(imgs, m_reflection, (cols, rows))
    
    return reflected_img


def shear_img(imgs):
    rows, cols = imgs.shape[:2]
  
    m_shearing=np.float32([[1,0.5,0],
                         [0,1,0],
                         [0,0,1]])

    sheared_img = cv2.warpPerspective(imgs, m_shearing, (int(cols*1.5), int(rows*1.5)))

    return sheared_img





def main():

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # read image
        bytes_data = uploaded_file.read()
        nparr = np.frombuffer(bytes_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        img_path = "flower.jpg"
        img = cv2.imread(img_path)
        
    #for i in range(1 ,6):
        
    #    img_path = f"pic{i}.jpg"
    #    imgs = cv2.imread(img_path)
    #    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
        
    translated_img = translation_img(imgs)
    rotated_img = rotation_img(imgs)
    scaled_img = scaling_img(imgs)                     #calling the functions above to be executed in main function
    reflected_img = reflection_img(imgs)
    sheared_img = shear_img(imgs)


    st.image([img, translated_img, rotated_img, scaled_img, reflected_img, sheared_img],
             caption=["Original Image", "Translated Image", "Rotated Image", "Scaled Image", "Reflected Image", "Sheared Image"],
             width=200)
#Sets the images on axis with the figure
      #  fig, axs = plt.subplots(2, 3, figsize=(12, 8))
       # fig = plt.gcf()
        #fig.canvas.manager.set_window_title(f"Picture Number {i}")
        #axs[0, 0].imshow(imgs)
        #axs[0, 0].set_title("Original Image")
        #axs[0, 0].axis("off")

        #axs[0, 1].imshow(translated_imgs)
        #axs[0, 1].set_title("Translated Image")
        #axs[0, 1].axis("off")

        #axs[0, 2].imshow(rotated_imgs)
        #axs[0, 2].set_title("Rotated Image")
        #axs[0, 2].axis("off")

        #axs[1, 0].imshow(scaled_imgs)
        #axs[1, 0].set_title("Scaled Image")
        #axs[1, 0].axis("off")

        #axs[1, 1].imshow(reflected_imgs)
        #axs[1, 1].set_title("Reflected Image")
        #axs[1, 1].axis("off")

        #axs[1, 2].imshow(sheared_imgs)
        #axs[1, 2].set_title("Sheared Image")
        #axs[1, 2].axis("off")

        #plt.show()

main()





