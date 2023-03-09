import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

two_d_arr = np.array([[1,0,1], [0,1,0],[1,0,1]])

def change(x, y, color, direction):
    if direction == '1':
        two_d_arr[x][y] = color
        if x > 0:
            change(x-1, y, color, direction)
    elif direction == '2':
        two_d_arr[x][y] = color
        if x < two_d_arr.shape[0]-1:
            change(x+1, y, color, direction)
    elif direction == '3':
        two_d_arr[x][y] = color
        if y > 0:
            change(x, y-1, color, direction)
    elif direction == '4':
        two_d_arr[x][y] = color
        if y < two_d_arr.shape[1]-1:
            change(x, y+1, color, direction)
    else:
        print('Please Try again')
    
    img = plt.imshow(two_d_arr, interpolation='none', cmap='Pastel2')
    img.set_clim([0,50])
    plt.colorbar()
    return img

def main():
    x_coordinates = st.number_input("X coordinates:", min_value=0, max_value=2, step=1)
    y_coordinates = st.number_input("Y coordinates:", min_value=0, max_value=2, step=1)
    colorvalue = st.selectbox("Select a Color Value (1-50)", options=list(range(1, 51)))
    direction = st.selectbox("Direction", options=["1 for up", "2 for down", "3 for left", "4 for right"])
    direction_mapping = {"1 for up": "1", "2 for down": "2", "3 for left": "3", "4 for right": "4"}
    direction_code = direction_mapping[direction]
    img = change(x_coordinates, y_coordinates, colorvalue, direction_code)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

main()
