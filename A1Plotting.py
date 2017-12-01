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

similarity = np.loadtxt('IO/similarity.txt')
# similarity = np.load('IO/similarity')


# Self similarity
# -----------------------------
x = np.arange(0, num_tsteps)
data = []
for i, sim in enumerate(similarity):
    trace = go.Scatter(
        name='trial {}'.format(i),
        x=x,
        y=sim,  # y=np.convolve(sim, np.array([1] * 3) / 3, 'valid'),  # smoother
        opacity=.1,
        marker={'color': 'gray'},
        hoverinfo='none'
    )
    data.append(trace)

trace = go.Scatter(
    name='average',
    x=x,
    y=np.average(similarity, axis=0),
    opacity=1,
    marker={'symbol': 'dash', 'color': 'black'},
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
    'showlegend': False,
}

fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='Images/self-similarity.html', auto_open=True)


# Distributions
# -----------------------------
data = []
for ts in np.logspace(0, np.log10(num_tsteps - 1), 15, dtype=np.int)[1:]:
    # sim = np.convolve(similarity[:, ts], np.array([1] * 3) / 3, 'valid')
    trace = go.Histogram(name=ts, x=similarity[:, ts], opacity=.5)
    data.append(trace)

layout = go.Layout(barmode='overlay',
                   xaxis={'autorange': 'reversed'})
fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='Images/distributions.html', auto_open=True)


# Sigma Spread
# -----------------------------
data = []
for ts in np.logspace(0, np.log10(num_tsteps - 1), 15, dtype=np.int)[1:]:
    # sim = np.convolve(similarity[:, ts], np.array([1] * 3) / 3, 'valid')
    trace = go.Histogram(name=ts,
                         x=similarity[:, ts] - similarity[:, ts].mean(), opacity=.5,
                         )
    data.append(trace)

layout = go.Layout(barmode='overlay')
fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='Images/sigma_spread.html', auto_open=True)


# Sigma Spread
# -----------------------------
hist_data = []
group_labels = []
for ts in np.logspace(0, np.log10(num_tsteps - 1), 15, dtype=np.int)[1:]:
    hist_data.append(similarity[:, ts])
    group_labels.append(ts)

fig = ff.create_distplot(hist_data, group_labels, bin_size=.01, curve_type='normal', show_rug=False)
fig['layout']['xaxis']['autorange'] = 'reversed'

py.plot(fig, filename='Images/distributions_norms.html', auto_open=True)


# Layered Sigma Spread
# -----------------------------
hist_data = []
group_labels = []
for ts in np.logspace(0, np.log10(num_tsteps - 1), 15, dtype=np.int)[1:]:
    hist_data.append(similarity[:, ts] - similarity[:, ts].mean())
    group_labels.append(ts)

fig = ff.create_distplot(hist_data, group_labels, bin_size=.01, curve_type='normal', show_rug=False)
fig['layout']['xaxis']['autorange'] = 'reversed'

py.plot(fig, filename='Images/sigma_spread_norms.html.html', auto_open=True)



# Box Plots
# -----------------------------
data = []
for ts in np.logspace(0, np.log10(num_tsteps - 1), 15, dtype=np.int)[1:]:
    # sim = np.convolve(similarity[:, ts], np.array([1] * 3) / 3, 'valid')
    trace = go.Box(name=ts, y=similarity[:, ts], boxmean='sd')
    data.append(trace)

layout = go.Layout(xaxis={'type': 'log'})

fig = go.Figure(data=data, layout=layout)
# fig['yaxis']['type'] = 'log'

py.plot(fig, filename='Images/box_plots.html', auto_open=True)