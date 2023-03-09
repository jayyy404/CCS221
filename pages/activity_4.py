import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# create some sample data
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# create a matplotlib figure
fig, ax = plt.subplots()
ax.plot(x, y)

# display the figure in Streamlit
st.pyplot(fig)






