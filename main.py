import streamlit as st
import numpy as np
from scipy.stats import weibull_min
import matplotlib.pyplot as plt
from scipy.stats import poisson

st.title('Poisson- und Weibull-Verteilung')

st.header("Poisson Verteilung")

mu = st.slider('Mu', min_value=1, max_value=50, value=5, step=1)

fig_poi, ax_poi = plt.subplots(1, 1)
# mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
x_poi = np.arange(poisson.ppf(0.01, mu),
              poisson.ppf(0.99, mu))
ax_poi.bar(x_poi, poisson.pmf(x_poi, mu))

st.pyplot(fig_poi)

st.header("Weibull Verteilung")

c = st.slider('Formparameter', min_value=0.1, max_value=5.0, value=1.0, step=0.1)
scale= st.slider('Lageparameter', min_value=0.1, max_value=5.0, value=1.0, step=0.1)
loc = st.slider('Schwellenparameter', min_value=0.1, max_value=5.0, value=0.0, step=0.1)
line = st.checkbox('Gerade bei 63,2%')

fig_wei, ax_wei = plt.subplots(1, 1)
x_wei = np.linspace(0,5, 100)
ax_wei.plot(x_wei, weibull_min.pdf(x_wei, c, loc= loc, scale= scale), label="Dichtefunktion")
ax_wei.plot(x_wei, weibull_min.cdf(x_wei, c, loc= loc, scale= scale), label="Verteilungsfunktion")
if line:
    ax_wei.plot([0,scale+loc],[0.632,0.632], linestyle='dotted', color='black')
    ax_wei.vlines([scale+loc],0,weibull_min.cdf(scale+loc, c, loc= loc, scale= scale), linestyles='dotted', colors='black')

ax_wei.legend(loc='best', frameon=False)

st.pyplot(fig_wei)



