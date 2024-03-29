#Group 4
#Members : John Paul Sapasap
         # Jed Andrew Del Rosario
         # Marc Joshua Escueta
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import streamlit as st

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

st.title("3D TRANSFORMATION")
def plt_basic_object_(points):
    
    tri = Delaunay(points).convex_hull

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],triangles=tri,shade=True, cmap=cm.seismic,lw=0.5)

    ax.set_xlim3d(-10, 10)
    ax.set_ylim3d(-10, 10)
    ax.set_zlim3d(-10, 10)

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

init_pyramid = _pyramid_(bottom_center=(0,0,0))
points_pyramid2 = tf.constant(init_pyramid, dtype=tf.float32)
fig1 = plt_basic_object_(init_pyramid)
#st.pyplot(fig1)







def _heart_(bottom_center = (0, 0, 0)):
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

fig3 = plt_basic_object_(init_heart)
#st.pyplot(fig3)




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

fig5=plt_basic_object_(init_pyramid)
#st.pyplot(fig5)




st.sidebar.title("Select 3D objects")
points = st.sidebar.selectbox("Select 3D Objects", ("Pyramid", "Heart","Diamond"))

if (points=="Pyramid"):
    st.sidebar.title("Points for Pyramid")
    x = st.sidebar.slider("Enter for x:", -10, 10, step=1,key='my_slider1')
    y = st.sidebar.slider("Enter for y:", -10, 10, step=1,key='my_slider2')
    z = st.sidebar.slider("Enter for z:", -10, 10, step=1,key='my_slider3')

    translation = tf.constant([x, y, z], dtype=tf.float32)

    translated_points = points_pyramid2 + translation

    fig1 = plt_basic_object_(translated_points.numpy())
    st.subheader("Pyramid")
    st.pyplot(fig1)

    

elif(points=="Heart"):
    st.sidebar.title("Points for Heart")
    x = st.sidebar.slider("Enter for x:", -10, 10, step=1,key='my_slider4')
    y = st.sidebar.slider("Enter for y:", -10, 10, step=1,key='my_slider5')
    z = st.sidebar.slider("Enter for z:", -10, 10, step=1,key='my_slider6')

    translation = tf.constant([x, y, z], dtype=tf.float32)

    translated_points = points_heart + translation

    fig4 = plt_basic_object_(translated_points.numpy())
    st.subheader("Heart")
    st.pyplot(fig4)
    
elif(points=="Diamond"):
    st.sidebar.title("Points for Diamond")

    x = st.sidebar.slider("Enter for x:", -10, 10, step=1,key='my_slider7')
    y = st.sidebar.slider("Enter for y:", -10, 10, step=1,key='my_slider8')
    z = st.sidebar.slider("Enter for z:", -10, 10, step=1,key='my_slider9')

    translation = tf.constant([x, y, z], dtype=tf.float32)

    translated_points = points_pyramid + translation

    fig6 = plt_basic_object_(translated_points.numpy())
    st.subheader("Diamond")
    st.pyplot(fig6)
    
    
