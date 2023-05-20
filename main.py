import streamlit as st
import numpy as np
from scipy.stats import weibull_min
import matplotlib.pyplot as plt

st.title('Poisson- und Weibull-Verteilung')

st.header("Weibull Verteilung")

c = st.slider('Formparameter', min_value=0.1, max_value=5.0, value=1.0, step=0.1)
scale= st.slider('Lageparameter', min_value=0.1, max_value=5.0, value=1.0, step=0.1)
loc = st.slider('Schwellenparameter', min_value=0.1, max_value=5.0, value=0.0, step=0.1)

fig, ax = plt.subplots(1, 1)
x = np.linspace(0,5, 100)
ax.plot(x, weibull_min.pdf(x, c, loc= loc, scale= scale))


st.pyplot(fig)