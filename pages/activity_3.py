#Group - 4
#John Paul Sapasap
#Jed Andrew Del Rosario
#Marc Joshua 

import numpy as np
import cv2 
import matplotlib.pyplot as plt
import streamlit as st

   

def read_image(path):
    img = cv2.imread(path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



def translation_img(img):
    rows, cols = img.shape[:2]
    m_translation_=np.float32([[1,0,100],
                        [0,1,50],
                        [0,0,1]])

    translated_img_=cv2.warpPerspective(img,m_translation_,(cols, rows))
    return translated_img_


def rotation_img(img):

    angle =np.radians(10)
    rows, cols = img.shape[:2]
    m_rotation_=np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                        [np.sin(angle), np.cos(angle),0],
                        [0,0,1]])

    m_rotation_=cv2.getRotationMatrix2D((cols/2,rows/2), 60,1)
    rotated_img_ = cv2.warpAffine(img,m_rotation_,(cols,rows))
    return rotated_img_



def scaling_img(img):
    rows, cols = img.shape[:2]
    m_scaling_=np.float32([[1.5,0,0],
                       [0,1.8,0],
                       [0,0,1]])
    scaled_img_ =cv2.warpPerspective(img,m_scaling_,(cols*2,rows*2))
    return scaled_img_



def reflection_img(img):
    rows, cols = img.shape[:2]
    m_reflection_ =np.float32([[1,0,0],
                          [0,-1,rows],
                          [0,0,1]])
    reflected_img_ =cv2.warpPerspective(img,m_reflection_,(int(cols),int (rows)))
    return reflected_img_


def shear_img(img):
    rows, cols = img.shape[:2]
    m_shearing_x=np.float32([[1,0.5,0],
                         [0,1,0],
                         [0,0,1]])

    sheared_img_x = cv2.warpPerspective(img,m_shearing_x,(int(cols*1.5),int(rows*1.5)))

    return sheared_img_x

def main():
    
    img = read_image("flower.jpg")

    translated_img_ = translation_img(img)
    rotated_img_ = rotation_img(img)
    scaled_img_ = scaling_img(img)
    reflected_img_ = reflection_img(img)
    sheared_img_x = shear_img(img)

    fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    axs[0, 0].imshow(img)
    axs[0, 0].set_title("Original Image")
    axs[0, 0].axis("off")

    axs[0, 1].imshow(translated_img_)
    axs[0, 1].set_title("Translated Image")
    axs[0, 1].axis("off")

    axs[0, 2].imshow(rotated_img_)
    axs[0, 2].set_title("Rotated Image")
    axs[0, 2].axis("off")

    axs[1, 0].imshow(scaled_img_)
    axs[1, 0].set_title("Scaled Image")
    axs[1, 0].axis("off")

    axs[1, 1].imshow(reflected_img_)
    axs[1, 1].set_title("Reflected Image")
    axs[1, 1].axis("off")

    axs[1, 2].imshow(sheared_img_x)
    axs[1, 2].set_title("Sheared Image")
    axs[1, 2].axis("off")

    plt.show()
    
main()







    








