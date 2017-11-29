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

# Plotting
try:
    import plotly.plotly as plotly
except:
    print('cant import plotly')
else:
    import plotly.offline as py
    import plotly.graph_objs as go
    import plotly.tools as tls
    py.init_notebook_mode(connected=True)

##############################################################################
# Code


with open('IO/run_info.pickle', 'rb') as file:
    init_dna, num_trials, num_tsteps, num_bases = pickle.load(file)

# with open('IO/similarity.pickle', 'rb') as file:
#     num_trials, num_tsteps, num_bases = pickle.load(file)

similarity = np.loadtxt('IO/similarity.txt')


# Self similarity
# -----------------------------
x = np.arange(0, num_tsteps)
data = []
for i, sim in enumerate(similarity):
    trace = go.Scatter(
        name='trial {}'.format(i),
        x=x,
        # y=np.convolve(sim, np.array([1] * 3) / 3, 'valid'),  # smoother
        y=sim
    )
    data.append(trace)

layout = {
    'title': 'self similarity',
    'xaxis': {'title': 'time [s]'},
    'yaxis': {'title': 'similarity (3 smoothed)'},
    'shapes': [
        # Line Horizontal
        {'type': 'line', 'x0': 0, 'y0': .25,
                         'x1': x[-1], 'y1': .25,
         'line': {'color': 'k', 'width': 2, 'dash': 'dash'}},
    ],
}

fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='Images/self-similarity.html', auto_open=True)
py.iplot(fig)


# Self similarity
# -----------------------------
data = []
for ts in np.logspace(0, np.log10(num_tsteps - 1), 15, dtype=np.int):
    # sim = np.convolve(similarity[:, ts], np.array([1] * 3) / 3, 'valid')
    trace = go.Histogram(name=ts,
                         x=similarity[:, ts] - similarity[:, ts].mean(), opacity=.5,
                         )
    data.append(trace)

layout = go.Layout(barmode='overlay')
fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='Images/overlaid_histogram.html', auto_open=True)
