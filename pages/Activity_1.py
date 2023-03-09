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

    plt.show()



#DDA Line with midpoints
plt.title("DDA line/ Midpoints")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
def DDALine_mpoints(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    xm = (x1 + x2)/2
    ym = (y1 + y2)/2                                            #These line of codes are the midpoints formula
    print ("\nX midpoint: ",xm, "\nY midpoint: ",ym)
    plt.plot(xm,ym, marker = 'o', markerfacecolor = "green")

    for i in range(0, int(steps + 1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc

    plt.show()                                                  #this let the program show a graph for the users input

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
    plt.show()

#Brasenham Line wirh Midpoint
plt.title("Braseham Line/Midpoint")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
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
    ym = (y1 + y2)/2                                            #These line of codes are the midpoints formula
    print ("\nX midpoint: ",xm, "\nY midpoint: ",ym)
    plt.plot(xm,ym, marker = 'o', markerfacecolor = "green")

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
    plt.show()



def main():

 #Gets User input or their pereference 

    print ("\t\t\tWELCOME TO GROUP 4's PROGRAM"
           "\n\nWhat do you want to show?\n"
           "\n\t\tEnter 1 for DDA Line\n"
           "\t\t2 for DDA Line with midpoints\n"
           "\t\t3 for Brasenham Line\n"
           "\t\t4 for Brasenham Line with midpoints :")
    choice = int (input ("\nYour choice :"))
    print ("")  
    if choice == 1:
        x = int(input("Enter the value for X1: "))
        y = int(input("Enter the value for Y1: "))
        xEnd = int(input("Enter the value for X2: "))
        yEnd = int(input("Enter the value for Y2: "))
        color = "r."
        DDALine(x, y, xEnd, yEnd, color)

    elif choice == 2:
        x = int(input("Enter the value for X1: "))
        y = int(input("Enter the value for Y1: "))
        xEnd = int(input("Enter the value for X2: "))
        yEnd = int(input("Enter the value for Y2: "))
        color = "r."
        DDALine_mpoints(x, y, xEnd, yEnd, color)

    elif choice == 3:
        x1 = int(input("Enter starting point of x: "))
        y1 = int(input("Enter starting point of y: "))
        x2 = int(input("Enter end point of x: "))
        y2 = int(input("Enter end point of y: "))  
        bres_line(x1,y1,x2,y2)

    elif choice == 4:
        x1 = int(input("Enter starting point of x: "))
        y1 = int(input("Enter starting point of y: "))
        x2 = int(input("Enter end point of x: "))
        y2 = int(input("Enter end point of y: "))  
        bres_line_mpoint(x1,y1,x2,y2)

    else :
        print ("Thank you")

if TRUE:
    main()


