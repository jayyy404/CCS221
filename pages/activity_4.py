#Group 4
#Jed Andrew Del Rosario
#John Paul T. Sapasap
#Marc Joshua Esceuta

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import streamlit as st

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

def plt_basic_object_(points, counter):
    tri = Delaunay(points).convex_hull

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],triangles=tri,shade=True, cmap=cm.seismic,lw=0.5)

    ax.set_xlim3d(-10, 10)
    ax.set_ylim3d(-10, 10)
    ax.set_zlim3d(-10, 10)
    if (counter == 1):
        plt.title("Pyramid")
    elif (counter == 2):
        plt.title("Heart")              #branching statement to show title for each shapes
    elif (counter == 3):
        plt.title("Diamond")

    plt.show()

def _pyramid_(bottom_center=(0, 0, 0)):            #function for the pyramid shape
    bottom_center = np.array(bottom_center) 

    points = np.vstack([
    bottom_center + [-3, -3, 0],
    bottom_center + [-3, +3, 0],
    bottom_center + [+3, -3, 0],
    bottom_center + [+3, +3, 0],
    bottom_center + [0, 0, +5]
    ])

    return points

init_pyramid = _pyramid_(bottom_center=(0,0,0))
points_pyramid2 = tf.constant(init_pyramid, dtype=tf.float32)
counter = 1
plt_basic_object_(init_pyramid, counter)
x = int(input("Enter for x: "))
y = int(input("Enter for y: "))                 #prompt the user to enter new values for x, y, and z
z = int(input("Enter for z: "))
translation = tf.constant([x, y, z], dtype=tf.float32)

translated_points = points_pyramid2 + translation

plt_basic_object_(translated_points.numpy(), counter)

def _heart_(bottom_center = (0, 0, 0)):                     #function for heart shape
    bottom_center = np.array(bottom_center)
    points = np.vstack([
        bottom_center + [+1.5, -1, +3.5],
        bottom_center + [+1.5, +1, +3.5],
        bottom_center + [-1.5, -1, +3.5],
        bottom_center + [-1.5, +1, +3.5],        
        bottom_center + [0, +1, +3],
        bottom_center + [0, -1, +2],
        bottom_center + [+3, 0, +2],
        bottom_center + [-3, 0, +2],
        bottom_center + [0, 1, -2],
        bottom_center + [0, -1, -2]
    ])
    return points

init_heart = _heart_(bottom_center=(0,0,0))
points_heart = tf.constant(init_heart, dtype=tf.float32)
counter = 2
plt_basic_object_(init_heart, counter)

x = int(input("Enter for x: "))
y = int(input("Enter for y: "))
z = int(input("Enter for z: "))

translation = tf.constant([x, y, z], dtype=tf.float32)

translated_points_heart = points_heart + translation

plt_basic_object_(translated_points_heart.numpy(), counter)

def _diamond_(bottom_center=(0, 0, 0)):             #fucntion for diamond shape
    bottom_center = np.array(bottom_center)

    points = np.vstack([
    bottom_center + [+2.5, +2.5, 0],
    bottom_center + [-2.5, +2.5, 0],
    bottom_center + [+2.5, -2.5, 0],
    bottom_center + [-2.5, -2.5, 0],
    bottom_center + [0, 0, 5],
    bottom_center + [0, 0, -5]
    ])
    return points

init_pyramid = _diamond_(bottom_center=(0,0,0))
points_pyramid = tf.constant(init_pyramid, dtype=tf.float32)
counter = 3
plt_basic_object_(init_pyramid, counter)

x = int(input("Enter for x: "))
y = int(input("Enter for y: "))
z = int(input("Enter for z: "))

translation = tf.constant([x, y, z], dtype=tf.float32)

translated_points_pyramid = points_pyramid + translation

plt_basic_object_(translated_points_pyramid.numpy(), counter)