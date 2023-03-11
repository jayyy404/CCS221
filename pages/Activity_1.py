#Group 4
#Members : John Paul Sapasap
         # Jed Andrew Del Rosario
         # Marc Joshua Escueta

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

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
    ax.set_aspect('equal', adjustable='box')
    return fig

def DDALine_mpoints(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
    xm = (x1 + x2)/2
    ym = (y1 + y2)/2
    fig, ax = plt.subplots()
    plt.plot(xm,ym, marker='o', markerfacecolor='green')
    for i in range(0, int(steps + 1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    ax.set_aspect('equal', adjustable='box')
    return fig

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
    plt.plot(xcoords, ycoords)
    ax.set_aspect('equal', adjustable='box')
    return fig

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
    plt.plot(xcoords, ycoords)
    ax.set_aspect('equal', adjustable='box')
    return fig
draw_funcs = {
    'DDA Line': DDALine,
    'DDA Line with midpoints': DDALine_mpoints,
    'Bresenham Line': bres_line,
    'Bresenham Line with midpoint': bres_line_mpoint
}

# Define the Streamlit app
def main():
    st.title('Line Drawing App')
    st.write('Choose a line drawing function:')
    
    # Create a dropdown menu to let the user choose the drawing function
    func_name = st.selectbox('Function', list(draw_funcs.keys()))

    # Get user's input for the line coordinates
    x1 = st.number_input('X1', value=0)
    y1 = st.number_input('Y1', value=0)
    x2 = st.number_input('X2', value=0)
    y2 = st.number_input('Y2', value=0)
    color = st.text_input('Color', default='r.')

    # Draw the line using the selected function
    if st.button('Draw'):
        fig, ax = plt.subplots()
        draw_funcs[func_name](x1, y1, x2, y2, color)
        st.pyplot(fig)
