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

# ##############################################################################
# # Code

similarity = np.loadtxt('IO/similarity.txt')
# similarity = np.load('IO/similarity')


# Gaussian distribution
def gauss(x, mu, sigma, A):
    return A * np.exp(-(x - mu)**2 / (2. * sigma**2))


coeffs = [[1., 0, 1.],
          [1., 0, 1.]]
covars = [0, 0, ]
bin_centers = [0, 0]

# NOTE it starts at 2
for sim in np.nditer(similarity[:, 2:], flags=['external_loop'], order='F'):

    hist, bin_edges = np.histogram(sim, density=True)
    bin_cents = (bin_edges[:-1] + bin_edges[1:]) / 2
    # initial guess
    p0 = [1., 1., 1.]

    # fit
    popt, pcov = curve_fit(gauss, bin_cents, hist, p0=p0)

    coeffs.append(popt)
    covars.append(pcov)
    bin_centers.append(bin_cents)

    print(popt[0], end=', ')


with open('IO/gaussianfits.pickle', 'wb') as output_file:
    pickle.dump((coeffs, covars, bin_centers), output_file, protocol=0)
