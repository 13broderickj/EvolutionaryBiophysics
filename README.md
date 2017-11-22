This is a repo for the numerical and problem set to help get someone up to speed about evolution from a Biophysics perspective. 


# Article 1

## What we are doing

we are running a simulation of gene mutations to see the difference in mutation rates on small versus large time scales. The behavior should be similar to that of the stock market, rapid fluctuations on small time scales which smooth out over large time scales.

Our problems will revolve around

- the difficulty of predicting evolutionary rates given short time scales
- MFPT to chaos (1/4 similarity)
- mutual information


## Simplifying assumptions
for now, we are assuming some stuff to make life easy. Maybe we will relax these assumptions for a more accurate description

- Ignoring mutation checkers which will prioritize certain codons which are more necessary for life than other codons
- mutations are indipendent and do not influence a mutation in any other codon

## TODO List:

- Mathematical description. We need to create a mathematical model of this with which we can analytically approach the problem

- finish coding.

- get transition rates between nucleotides

## Resources

- scanned file *Project Ideas*



# Article 2

## What we are doing

DNA size given transposon copying rates and DNA deletion

## Mathematical Approach
we are esssentially describing a DNA 'current' in which the copying and deletions will completely change the form of the DNA

## Modeling
Transposons have a probability to copy n number of times
Random segments of DNA are deleted, this doesn't have to correspond to the transoposons, so sometimes a portion of a transposon will get deleted and some surrounding DNA as well. Only full transposons copy so a deletion or point mutation will prevent the transposon from copying. Deletions become more common with larger DNA size, so eventually the transposon copying rate is balanced by bulk deletions and mutations, leaving a semistable DNA size.

## Simplifying assumptions

- 1 type of transposon. It would be cool to do 2 or more, but that would be really hard because 1 transposon could mutate into another, etc.
