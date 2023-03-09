import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import streamlit as st

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

def plt_basic_object_(points, title):
    tri = Delaunay(points).convex_hull

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],triangles=tri,shade=True, cmap=cm.seismic,lw=0.5)

    ax.set_xlim3d(-10, 10)
    ax.set_ylim3d(-10, 10)
    ax.set_zlim3d(-10, 10)
    plt.title(title)

    return fig

def _pyramid_(bottom_center=(0, 0, 0)):
    bottom_center = np.array(bottom_center) 

    points = np.vstack([
        bottom_center + [-3, -3, 0],
        bottom_center + [-3, +3, 0],
        bottom_center + [+3, -3, 0],
        bottom_center + [+3, +3, 0],
        bottom_center + [0, 0, +5]
    ])

    return points

def _heart_(bottom_center=(0, 0, 0)):
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

def _diamond_(bottom_center=(0, 0, 0)):
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

# Sidebar title and subtitle
st.sidebar.title("3D Object Translator")
st.sidebar.subheader("Select an object to translate:")

# Sidebar object selection
object_choice = st.sidebar.selectbox(
    "",
    options=["Pyramid", "Heart", "Diamond"]
)

# Sidebar translation input
x = st.sidebar.number_input("Translate in x-axis:", value=0, step=1)
y = st.sidebar.number_input("Translate in y-axis:", value=0, step=1)
z = st.sidebar.number_input("Translate in z-axis:", value=0, step=1)

