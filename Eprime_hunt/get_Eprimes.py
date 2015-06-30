#! /usr/bin/env python

import sys
sys.path.append('/home/eric/Dropbox/astools/')
from analysis import *
import matplotlib.pylab as plt

print 'Starting...'
cell = ReadStruct('INPUT_c5ox', 'crystal')

for i, at in enumerate(cell.atoms):
    #print '{:5} / {:5}'.format(i+1, len(cell))
    if at.species == 'Si' :
        nbs = get_neighbours(at, cell, dmax = 6.)
        if len([nb for nb in nbs if nb.at.species == 'O' and nb.length < 1.9]) == 3:
            print i+1, at
            for nb in nbs:
                print '   {}'.format(nb)
