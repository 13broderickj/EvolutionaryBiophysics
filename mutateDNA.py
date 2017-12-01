#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Docstring
"""

NOTE: DO NOT RUN THIS FILE


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
num_trials = 400

# number of time steps
num_tsteps = int(2e3)

# number of codons in the DNA
num_bases = 100

# the mutation rates between codonds.
# note: AC means from C to A
alpha = 1e-3      # transition rate
beta = 4 * alpha  # transversion rate

"""
[ A->A, C->A, G->A, T->A ]
[ A->C, C->C, G->C, T->C ]
[ A->G, C->G, G->G, T->G ]
[ A->T, C->T, G->T, T->T ]
"""
prob_matrix = np.array([[1 - 2 * alpha - beta, alpha, beta, alpha],
                        [alpha, 1 - 2 * alpha - beta, alpha, beta],
                        [beta, alpha, 1 - 2 * alpha - beta, alpha],
                        [alpha, beta, alpha, 1 - 2 * alpha - beta]])

prob_vec = [np.cumsum(prob_matrix[:, base]) for base in range(4)]

mutation_matrix = np.array([[0, -1, -2, -3],
                            [1,  0, -1, -2],
                            [2,  1,  0, -1],
                            [3,  2,  1,  0]],
                           dtype=np.int)


def pickMutation(base):
    ind = np.where(np.random.random() < prob_vec[base])[0][0]
    new_base = base + mutation_matrix[ind, base]
    return new_base


mutate = np.vectorize(pickMutation)

# DNA initial state
init_dna = myran.randint(0, high=4, size=num_bases)

# DNA state array matrix.
# column is dna state at time t. rows time evolve
# A=0, C=1, G=2, T=3

# NOTE would be better to do in opposite order & specify column-wise storage
similarity = np.zeros((num_trials, num_tsteps))

for trial in range(num_trials):
    print(trial)
    DNA = np.zeros((num_tsteps, num_bases), dtype=np.int)
    DNA[0, :] = np.array([init_dna])  # init_dna into state

    for ts in range(1, num_tsteps):
        DNA[ts, :] = mutate(DNA[ts - 1, :])

        similarity[trial, ts] = (num_bases - np.count_nonzero(DNA[ts, :] - init_dna)) / num_bases

    # Save Row as time step, Column as codon
    np.save('IO/DNA{}'.format(trial), DNA)

np.save('IO/similarity', similarity)

with open('IO/run_info.pickle', 'wb') as output_file:
    pickle.dump((init_dna, num_trials, num_tsteps, num_bases), output_file, protocol=0)

print('done')

# How to load all the DNA
# DNA = np.stack((np.loadtxt('IO/DNA{}.txt'.format(trial)) for trial in range(num_trials)), axis=0)

# # How to load the random state
# with open('dna_seed.state', 'rb') as fp:
#     ranstate = pickle.load(fp)
#     myran = np.random.RandomState()
#     myran.set_state(ranstate)
