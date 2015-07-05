#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from atom_pdos_getter import *
from helping_functions import get_similar
from astools.ReadWrite import ReadStruct
from astools.analysis import distance

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

dimer_dict = {'c1': [57, 113],
               'c2': [102, 114],
               'c3': [101, 73],
               'c4': [],
               'c5': [65],
               'c6': [113],
               'c2ox': [86],
               'c3ox': [73],
               'c5ox': [117],
              }

for c in ['c'+ i for i in map(str, range(1, 7))]:
    print c,
    for eprime in dimer_dict[c]:
        print eprime,
        x, y_u, y_d = get_at_pdos(c, eprime)
        plt.plot(x, y_u, 'k-')
        plt.plot(x, y_d, 'k-')
        # Get the Atom object of the eprime
        at_e = ReadStruct('../../crystal_files/INPUT_'+c,
                          'crystal').atoms[eprime-1]
        p_str= ReadStruct('../../crystal_files/INPUT_'+c+'p', 'crystal')
        # get equivalent atom from passified structure
        i_x, at_p = get_similar(at_e, p_str)
        print '{:5.3f}'.format(distance(at_e, at_p)), 
        x, y_u, y_d = get_at_pdos(c+'p', i_x)
        plt.plot(x, y_u, 'r-')
        plt.plot(x, y_d, 'r-')
    print

plt.show()
