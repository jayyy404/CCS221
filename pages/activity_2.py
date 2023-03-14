import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

two_d_arr = np.array([[1,0,1], [0,1,0],[1,0,1]])

def change(x, y, color):
    two_d_arr[x][y] = color
    fig, ax = plt.subplots()
    img = ax.imshow(two_d_arr, interpolation='none', cmap='twilight')
    img.set_clim([0,50])
    plt.colorbar(img)
    st.pyplot(fig)

def main():
    two_d_arr = np.array([[1,0,1], [0,1,0],[1,0,1]])
    for i in range(2):
        x= st.number_input("Input the X coordinate (row 0,1,2) that are available:", 0, 2, 0, key=f"x_val_{i}")
        y = st.number_input("Input the Y coordinate (column 0,1,2) that are available:", 0, 2, 0, key=f"y_val_{i}")
        color = st.number_input("Enter a Color Value from (1-50):", 1, 50, 1, key=f"c_val_{i}")
        change(x,y,color)

main()
