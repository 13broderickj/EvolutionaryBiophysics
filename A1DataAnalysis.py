#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Docstring
"""Main Initializatino File
Problem set about evolution from a Biophysics perspective.
"""

##############################################################################
# Importing Modules

import numpy as np
# import pickle
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
# # Code

# similarity = np.loadtxt('IO/similarity.txt')
similarity = np.load('IO/similarity.npy')


# Gaussian distribution
def gauss(x, mu, sigma, A):
    return A * np.exp(-(x - mu)**2 / (2. * sigma**2))


coeffs = [[1., 0, 1.],
          [1., 0, 1.]]
covars = []
bin_centers = []

# std = np.zeros(np.shape(similarity)[0])
std = [0] * 5

# NOTE it starts at 2
for sim in np.nditer(similarity[:, 5:], flags=['external_loop'], order='F'):

    std.append(np.std(sim))

    # hist, bin_edges = np.histogram(sim, density=True)
    # bin_cents = (bin_edges[:-1] + bin_edges[1:]) / 2
    # # initial guess
    # p0 = [1., 1., 1.]

    # fit
    # popt, pcov = curve_fit(gauss, bin_cents, hist, p0=p0)

    # coeffs.append(popt)
    # covars.append(pcov)
    # bin_centers.append(bin_cents)

    # print(popt[0], end=', ')


# Self similarity
# -----------------------------
x = np.arange(0, len(std))

trace = go.Scatter(
    name='shit',
    x=x,
    y=std,
    opacity=1,
    marker={'symbol': 'dash', 'color': 'black'},
)
data = [trace]


def std_fit(x, aon, aoff, kon, koff, b):
    return aoff * np.exp(-koff * x) * (1 - aon * np.exp(-kon * x)) + b


# coeffs, covars = curve_fit(std_fit, x, std,
#                            p0=[.9, .05, .02, .005, 0.43])
# print(coeffs)
# print(covars)
# bestfit = std_fit(x, *coeffs)

# trace = go.Scatter(
#     name='best fit',
#     x=x,
#     y=bestfit,
#     opacity=1,
#     marker={'symbol': 'dash', 'color': 'red'},
# )
# data.append(trace)

layout = {
    'title': 'standard deviation',
    'xaxis': {'title': 'time steps'},
    'yaxis': {'title': 'std'},
    'shapes': [
        # Line Horizontal
        {'type': 'line', 'x0': 0, 'y0': .043,
                         'x1': x[-1], 'y1': .043,
         'line': {'color': 'k', 'width': 2, 'dash': 'dash'}},
    ],
    'showlegend': False,
}

fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='Images/standard_deviation.html', auto_open=True)

# coeffs = np.array(coeffs)

# covars = np.array(covars)
# covars = np.insert(covars, 0, np.zeros_like(covars[:2, :]), axis=0)

# bin_centers = np.array(bin_centers)
# bin_centers = np.insert(bin_centers, 0, np.zeros_like(bin_centers[:2, :]), axis=0)
# # bin_centers = np.array(bin_centers)


# ind = np.where(coeffs[:, 1] == coeffs[:, 1].max())
# print(ind)
# print(coeffs[:, 1][-20:])



# with open('IO/gaussianfits.pickle', 'wb') as output_file:
#     pickle.dump((coeffs, covars, bin_centers), output_file, protocol=0)
