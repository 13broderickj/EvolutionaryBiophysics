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

##############################################################################
# Random Seed

myran = np.random.RandomState()
with open('dna_seed.state', 'wb') as fp:
    pickle.dump(myran.get_state(), fp, protocol=2, fix_imports=True)


##############################################################################
# Code

# number of repeats
num_trials = 50

# number of time steps
num_tsteps = 10**3

# number of codons in the DNA
num_bases = 10**3

# the mutation rates between codonds.
# note: AC means from C to A
alpha = 1e-3      # transition rate
beta = 4 * alpha  # transversion rate

rts = {               'CtoA': alpha, 'GtoA': beta,  'TtoA': alpha,
       'AtoC': alpha,                'GtoC': alpha, 'TtoC': beta,
       'AtoG': beta,  'CtoG': beta,                 'TtoG': alpha,
       'AtoT': alpha, 'CtoT': beta,  'GtoT': alpha
      }


def diagRate(*rates):
    return 1 - np.sum(rates)

# NOTE: a better way to do this is as dependent values in an LMFIT parameters
rts['AtoA'] = diagRate(rts['AtoC'], rts['AtoG'], rts['AtoT'])
rts['CtoC'] = diagRate(rts['CtoA'], rts['CtoG'], rts['CtoT'])
rts['GtoG'] = diagRate(rts['GtoA'], rts['GtoC'], rts['GtoT'])
rts['TtoT'] = diagRate(rts['TtoA'], rts['TtoC'], rts['TtoG'])

# Codon Omega Matrix
prob_matrix = np.array([[rts['AtoA'], rts['CtoA'], rts['GtoA'], rts['TtoA']],
                        [rts['AtoC'], rts['CtoC'], rts['GtoC'], rts['TtoC']],
                        [rts['AtoG'], rts['CtoG'], rts['GtoG'], rts['TtoG']],
                        [rts['AtoT'], rts['CtoT'], rts['GtoT'], rts['TtoT']]])

mutation_matrix = np.array([[0, -1, -2, -3],
                            [1,  0, -1, -2],
                            [2,  1,  0, -1],
                            [3,  2,  1,  0]],
                           dtype=np.int)


def pickMutation(base):
    base = int(base)
    prob_vec = np.cumsum(prob_matrix[:, base])
    ind = np.where(np.random.random() < prob_vec)[0][0]
    new_base = base + mutation_matrix[ind, base]
    return new_base


mutate = np.vectorize(pickMutation)

# DNA initial state
init_dna = myran.randint(0, high=4, size=num_bases)

# DNA state array matrix.
# column is dna state at time t. rows time evolve
# A=0, C=1, G=2, T=3

similarity = np.zeros((num_trials, num_tsteps))

for trial in range(num_trials):
    print(trial)
    DNA = np.zeros((num_tsteps, num_bases), dtype=np.int)
    DNA[0, :] = np.array([init_dna])  # init_dna into state

    for ts in range(1, num_tsteps):
        DNA[ts, :] = mutate(DNA[ts - 1, :])

        similarity[trial, ts] = (num_bases - np.count_nonzero(DNA[ts, :] - init_dna)) / num_bases

    # Save Row as time step, Column as codon
    np.savetxt('IO/DNA{}.txt'.format(trial), DNA, delimiter=" ", fmt="%s")

np.savetxt('IO/similarity.txt'.format(trial), similarity, delimiter=" ", fmt="%s")

with open('IO/run_info.pickle', 'wb') as output_file:
    pickle.dump((init_dna, num_trials, num_tsteps, num_bases), output_file, protocol=0)

print('done')

# How to load all the DNA
# DNA = np.stack((np.loadtxt('IO/DNA{}.txt'.format(trial)) for trial in range(num_trials)), axis=0)

# # How to load the random state
# with open('dna_seed.state', 'rb') as fp:
#     ranstate = pickle.load(fp)
#     myran2 = np.random.RandomState()
#     myran2.set_state(ranstate)
