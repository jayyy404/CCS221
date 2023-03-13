#Group 4
#Members : John Paul Sapasap
         # Jed Andrew Del Rosario
         # Marc Joshua Escueta

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt


def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    
    if dx == 0 and dy == 0:
        # both dx and dy are zero, so there is nothing to draw
        st.warning("Starting and ending points are the same.")
        return

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    x = x1
    y = y1
    fig, ax = plt.subplots()
    for i in range(0, int(steps+1)):
        ax.plot(int(x), int(y), color)
        x += Xinc
        y += Yinc
        
    midX = (x1 + x2) // 2
    midY = (y1 + y2) // 2
    st.write("Midpoint of the line is at ({}, {})".format(midX, midY))
    plt.plot(midX,midY, marker = 'o', markerfacecolor = "red")

    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.set_title("DDA Algorithm")
    st.pyplot(fig)


def bres_line(x1,y1,x2,y2,color):
    x,y = x1, y1
    dx = abs(x2 - x1) 
    dy = abs(y2 - y1) 
    slope = dy/float(dx)

    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    xcoords = [x]
    ycoords = [y]

    fig,ax = plt.subplots()
    for i in range(1, dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy 

        x = x + 1 if x < x2 else x - 1
        xcoords.append(x)
        ycoords.append(y)

    plt.plot(xcoords, ycoords)
    st.write("Midpoint of the line is at ({}, {})".format(xcoords, ycoords))
    plt.plot(xcoords,ycoords, marker = 'o', markerfacecolor = "red")

    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.set_title("Brasenham Algorithm")
    st.pyplot(fig)




def main():
    st.sidebar.title("Select Algorithm")
    algorithm = st.sidebar.selectbox("Select Algorithm", ("DDA", "Bresenham"))

    x1 = st.sidebar.number_input("Enter the Starting point of x:")
    y1 = st.sidebar.number_input("Enter the Starting point of y:")
    x2 = st.sidebar.number_input("Enter the end point of x:")
    y2 = st.sidebar.number_input("Enter the end point of y:")

    if algorithm == "DDA":
        color = "g."
        DDALine(x1, y1, x2, y2, color)
    elif algorithm == "Bresenham":
        color="r."
        bres_line(x1,y1,x2,y2,color)
        

main()
