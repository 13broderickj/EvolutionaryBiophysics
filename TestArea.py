#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Docstring
"""Main Initializatino File
Problem set about evolution from a Biophysics perspective.
"""

##############################################################################
# Importing Modules

import numpy as np
import pickle

from scipy.optimize import curve_fit

# Plotting
try:
    import plotly.plotly as plotly
except:
    print('cant import plotly')
else:
    import plotly.offline as py
    import plotly.graph_objs as go
    import plotly.tools as tls
    import plotly.figure_factory as ff

    py.init_notebook_mode(connected=True)

# ##############################################################################

with open('IO/run_info.pickle', 'rb') as file:
    init_dna, num_trials, num_tsteps, num_bases = pickle.load(file)

with open('IO/gaussianfits.pickle', 'rb') as file:
    coeffs, covars, bin_centres = pickle.load(file)

similarity = np.loadtxt('IO/similarity.txt')

# # Self similarity
# # -----------------------------
# x = np.arange(0, num_tsteps)
# data = []

# trace = go.Scatter(
#     name='average',
#     x=x,
#     y=np.average(similarity, axis=0),
#     opacity=1,
#     marker={'symbol': 'dash', 'color': 'black'},
# )
# data.append(trace)


# Gaussian distributions
def gaussianDistribution(x, mu, sigma, A):
    return A * np.exp(-(x - mu)**2 / (2. * sigma**2))

gauss = np.vectorize(gaussianDistribution)


# for i in range(2, 2000, 50):
#     hist_fit = gaussianDistribution(bin_centres[i], *(coeffs[i]))

#     trace = go.Scatter(
#         x=hist_fit + x[i],
#         y=bin_centres[i])
#     data.append(trace)

# layout = {
#     'title': 'self similarity',
#     'xaxis': {'title': 'time [s]'},
#     'yaxis': {'title': 'similarity (3 smoothed)'},
#     'shapes': [
#         # Line Horizontal
#         {'type': 'line', 'x0': 0, 'y0': .25,
#                          'x1': x[-1], 'y1': .25,
#          'line': {'color': 'k', 'width': 2, 'dash': 'dash'}},
#     ],
#     'showlegend': False,
# }

# fig = go.Figure(data=data, layout=layout)

# py.plot(fig, auto_open=True)


# print(bin_centres[:, 0])

# Get all the histogram fits
hist_fit = gaussianDistribution(bin_centres.T, *coeffs.T)

# mapping the highest density to brightest color
print(hist_fit.max())
