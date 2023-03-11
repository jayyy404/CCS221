#Group 4
#Members : John Paul Sapasap
         # Jed Andrew Del Rosario
         # Marc Joshua Escueta

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

import streamlit as st
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

    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.set_title("DDA Algorithm")
    st.pyplot(fig)


def BresenhamLine(x1, y1, x2, y2, color):
    
    if x1 == x2 and y1 == y2:
        return
    
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    if dx == 0:
        # if dx is zero, draw a vertical line
        ycoordinates = [y1, y2]
        xcoordinates = [x1] * 2
        fig, ax = plt.subplots()
        ax.plot(xcoordinates, ycoordinates, color)
        ax.set_xlabel("X-Axis")
        ax.set_ylabel("Y-Axis")
        ax.set_title("Bresenham Algorithm")
        st.pyplot(fig)
        return

    gradient = dy / float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx+2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1
        xcoordinates.append(x)
        ycoordinates.append(y)

    midX = (x1 + x2) // 2
    midY = (y1 + y2) // 2
    st.write("Midpoint of the line is at ({}, {})".format(midX, midY))

    fig, ax = plt.subplots()
    ax.scatter(xcoordinates, ycoordinates, color="r.")
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.set_title("Bresenham Algorithm")
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
          # if both dx and dy are zero, just plot a point
        fig, ax = plt.subplots()
        ax.scatter(x1, y1, color="r")
        ax.set_xlabel("X-Axis") 
        ax.set_ylabel("Y-Axis")
        ax.set_title("Bresenham Algorithm")
        st.pyplot(fig)
        dx = BresenhamLine(x1, y1, x2, y2, color)
        if dx == 0:
            return
        
      
    else:
        BresenhamLine(x1, y1, x2, y2,color)

main()
