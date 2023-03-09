#Group 4
#Members : John Paul Sapasap
         # Jed Andrew Del Rosario
         # Marc Joshua Escueta

from pickle import TRUE
import matplotlib.pyplot as plt
import streamlit as st

plt.title("DDA Line Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

 
    for i in range(0, int(steps + 1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc

    st.pyplot()



#DDA Line with midpoints
plt.title("DDA line/ Midpoints")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
def DDALine_mpoints(x1, y1, x2, y2, color):
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    xm = (x1 + x2)/2
    ym = (y1 + y2)/2

    st.write("\nX midpoint: ",xm, "\nY midpoint: ",ym)
    plt.plot(xm,ym, marker = 'o', markerfacecolor = "green")

    for i in range(0, int(steps + 1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc

    st.pyplot()                                      #this let the program show a graph for the users input

#Brasenham lINE
plt.title("Braseham Line")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
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
    st.pyplot()


# Brasenham Line with Midpoint
plt.title("Brasenham Line/Midpoint")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
def bres_line_mpoint(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy / float(dx)

    if slope > 1:
        dx, dy = dy, dx
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    x, y = x1, y1
    p = 2 * dy - dx
    xcoords = [x]
    ycoords = [y]

    for i in range(dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy 
        x = x + 1 if x < x2 else x - 1
        xcoords.append(x)
        ycoords.append(y)

    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    st.write("\nX midpoint: ", xm, "\nY midpoint: ", ym)
    plt.plot(xcoords, ycoords, color='blue')
    plt.plot(xm, ym, marker='o', markerfacecolor='green')
    st.pyplot()






