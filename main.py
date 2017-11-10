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
rts = {          'CtoA': 1, 'GtoA': 1, 'TtoA': 1,
       'AtoC': 1,           'GtoC': 1, 'TtoC': 1,
       'AtoG': 1, 'CtoG': 1,           'TtoG': 1,
       'AtoT': 1, 'CtoT': 1, 'GtoT': 1
      }


def diagRate(*rates):
    return - np.sum(rates)

rts['AtoA'] = diagRate(rts['AtoC'], rts['AtoG'], rts['AtoT'])
rts['CtoC'] = diagRate(rts['CtoA'], rts['CtoG'], rts['CtoT'])
rts['GtoG'] = diagRate(rts['GtoA'], rts['GtoC'], rts['GtoT'])
rts['TtoT'] = diagRate(rts['TtoA'], rts['TtoC'], rts['TtoG'])

# Codon Omega Matrix
codon_om = np.array([[rts['AtoA'], rts['CtoA'], rts['GtoA'], rts['TtoA']],
                     [rts['AtoC'], rts['CtoC'], rts['GtoC'], rts['TtoC']],
                     [rts['AtoG'], rts['CtoG'], rts['GtoG'], rts['TtoG']],
                     [rts['AtoT'], rts['CtoT'], rts['GtoT'], rts['TtoT']]])

# DNA initial state
init_dna = np.random.randint(0, high=4, size=num_cod)

# DNA state array matrix.
# column is dna state at time t. rows time evolve
# A=0, C=1, G=2, T=3
dna = np.zeros((num_cod, num_tsteps, num_reps))
dna[:, 0, :] = np.array([init_dna, ] * 3).T  # init_dna into state

print(dna)


def reproduce(current_codon):
    """reproduce the DNA and mutate if necessary."""
    pass
    # split up

# TODO vectorize in a more pythonic way
for i in range(num_reps):
    for j in range(1, num_tsteps):
        for k in range(num_cod):
            pass

            # time evolve the dna state using the codon_om
            # dna[k, j, i] = func(dna[k, j - 1, i])
