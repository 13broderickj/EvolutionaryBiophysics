#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Docstring
"""Main Initializatino File
Problem set about evolution from a Biophysics perspective.
"""

##############################################################################
# Importing Modules

import numpy as np
import pandas as pd

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

# number of codons in the DNA
num_cod = 10

# number of time steps
num_tsteps = 7

# number of repeats
num_reps = 3

# the mutation rates between codonds.
# note: AC means from C to A
rts = {          'C2A': 1, 'G2A': 1, 'T2A': 1,
       'A2C': 1,           'G2C': 1, 'T2C': 1,
       'A2G': 1, 'C2G': 1,           'T2G': 1,
       'A2T': 1, 'C2T': 1, 'G2T': 1
      }


def diagRate(*rates):
    return - np.sum(rates)

rts['A2A'] = diagRate(rts['A2C'], rts['A2G'], rts['A2T'])
rts['C2C'] = diagRate(rts['C2A'], rts['C2G'], rts['C2T'])
rts['G2G'] = diagRate(rts['G2A'], rts['G2C'], rts['G2T'])
rts['T2T'] = diagRate(rts['T2A'], rts['T2C'], rts['T2G'])

# Codon Omega Matrix
codon_om = np.array([[rts['A2A'], rts['C2A'], rts['G2A'], rts['T2A']],
                     [rts['A2C'], rts['C2C'], rts['G2C'], rts['T2C']],
                     [rts['A2G'], rts['C2G'], rts['G2G'], rts['T2G']],
                     [rts['A2T'], rts['C2T'], rts['G2T'], rts['T2T']]])

# DNA initial state
init_dna = np.random.randint(0, high=4, size=num_cod)

# DNA state array matrix.
# column is dna state at time t. rows time evolve
# A=0, C=1, G=2, T=3
dna = np.zeros((num_cod, num_tsteps, num_reps))
dna[:, 0, :] = np.array([init_dna, ] * 3).T  # init_dna into state

print(dna)
