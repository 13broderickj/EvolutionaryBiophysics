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
import plotly.plotly as plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
py.init_notebook_mode(connected=True)


##############################################################################
# Code

# number of codons in the DNA
num_cod = 100

# the mutation rates between codonds.
# note: AC means from C to A
rts = {'AC': 1, 'AG': 1, 'AT': 1,
       'CA': 1, 'CG': 1, 'CT': 1,
       'GA': 1, 'GC': 1, 'GT': 1,
       'TA': 1, 'TC': 1, 'TG': 1}


def diagRate(*rates):
    return - np.sum(rates)

rts['AA'] = diagRate(rts['CA'], rts['GA'], rts['TA'])
rts['CC'] = diagRate(rts['AC'], rts['GC'], rts['TC'])
rts['GG'] = diagRate(rts['AG'], rts['CG'], rts['TG'])
rts['TT'] = diagRate(rts['AT'], rts['CT'], rts['GT'])

# Codon Omega Matrix
codon_om = np.array([[rts['AA'], rts['AC'], rts['AG'], rts['AT']],
                     [rts['CA'], rts['CC'], rts['CG'], rts['CT']],
                     [rts['GA'], rts['GC'], rts['GG'], rts['GT']],
                     [rts['TA'], rts['TC'], rts['TG'], rts['TT']]])

# DNA state array
# A=0, C=1, G=2, T=3
dna = np.array([0] * num_cod)
