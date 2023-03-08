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
    plt.show()

def main():
    x_coordinates = int(input("X coordinates:"))
    y_coordinates = int(input("Y coordinates:"))
    colorvalue = int(input("Select a Color Value (1-50)"))
    direction = input("Direction (1 for up, 2 for down, 3 for left, or 4 for right):")
    change(x_coordinates, y_coordinates, colorvalue, direction)

main()