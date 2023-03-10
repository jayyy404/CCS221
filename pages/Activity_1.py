#Group 4
#Members : John Paul Sapasap
         # Jed Andrew Del Rosario
         # Marc Joshua Escueta

import streamlit as st
import matplotlib.pyplot as plt

def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
    
    fig, ax = plt.subplots()
    for i in range(0, int(steps + 1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    return plt

    st.title('DDA Line Drawing Algorithm')

# Get user input
    x1 = st.number_input('Enter the X coordinate of the starting point:')
    y1 = st.number_input('Enter the Y coordinate of the starting point:')
    x2 = st.number_input('Enter the X coordinate of the ending point:')
    y2 = st.number_input('Enter the Y coordinate of the ending point:')
    color = st.selectbox('Select a color:', ['red', 'green', 'blue'])

# Draw the line
    DDALine(x1, y1, x2, y2, color)
    ax.set_aspect('equal', adjustable='box')
    st.pyplot(fig)

def DDALine_mpoints(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
    xm = (x1 + x2)/2
    ym = (y1 + y2)/2
    st.pyplot(xm,ym, marker = 'o', markerfacecolor = "green")
    fig, ax = plt.subplots()
    for i in range(0, int(steps + 1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    return plt


    st.title('DDA Line Drawing Algorithm')

    x1 = st.number_input('Enter the X coordinate of the starting point:')
    y1 = st.number_input('Enter the Y coordinate of the starting point:')
    x2 = st.number_input('Enter the X coordinate of the ending point:')
    y2 = st.number_input('Enter the Y coordinate of the ending point:')
    color = st.selectbox('Select a color:', ['red', 'green', 'blue'])
    DDALine(x1, y1, x2, y2, color)
    ax.set_aspect('equal', adjustable='box')
    st.pyplot(fig)

def bres_line(x1,y1,x2,y2):
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
    fig, ax = plt.subplots()
    for i in range(2, dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy 
        x = x + 1 if x < x2 else x - 1
        xcoords.append(x)
        ycoords.append(y)
    st.pyplot(plt.plot(xcoords, ycoords))
    return plt

    st.title('DDA Line Drawing Algorithm')


    x1 = st.number_input('Enter the X coordinate of the starting point:')
    y1 = st.number_input('Enter the Y coordinate of the starting point:')
    x2 = st.number_input('Enter the X coordinate of the ending point:')
    y2 = st.number_input('Enter the Y coordinate of the ending point:')
    color = st.selectbox('Select a color:', ['red', 'green', 'blue'])

    DDALine(x1, y1, x2, y2, color)
    ax.set_aspect('equal', adjustable='box')
    st.pyplot(fig)

def bres_line_mpoint(x1,y1,x2,y2):
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
    xm = (x1 + x2)/2
    ym = (y1 + y2)/2
    st.pyplot(plt.plot(xcoords, ycoords), plt.plot(xm,ym, marker = 'o', markerfacecolor = "green"))
    return plt

    st.title('DDA Line Drawing Algorithm')


    x1 = st.number_input('Enter the X coordinate of the starting point:')
    y1 = st.number_input('Enter the Y coordinate of the starting point:')
    x2 = st.number_input('Enter the X coordinate of the ending point:')
    y2 = st.number_input('Enter the Y coordinate of the ending point:')
    color = st.selectbox('Select a color:', ['red', 'green', 'blue'])


    fig, ax = plt.subplots()
    DDALine(x1, y1, x2, y2, color)
    ax.set_aspect('equal', adjustable='box')
    st.pyplot(fig)





