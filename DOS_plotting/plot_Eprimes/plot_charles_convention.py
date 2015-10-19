#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from atom_pdos_getter import *
from helping_functions import get_similar, offsets 
from astools.ReadWrite import ReadStruct
from astools.analysis import distance

import numpy as np

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

# This plots the distribution of the E' DOS relative to the structure's VBM. The
# VBM for each cell is set to the 0 eV level. The VBM is found in the
# helping_functions.py file.

# 5eV range with 600 points in the read files
dE = 5./600
eprime_dict = {'c1': [142, 144],
               'c2': [124, 125, 134],
               'c3': [81, 113, 134, 135, 147, 148],
               'c4': [124, 125, 127, 130, 136],
               'c5': [126, 133, 135, 137],
               'c6': [125, 128, 131, 135, 136, 137, 144, 147],
               'c2ox': [84, 128, 136, 138, 148, 150],
               'c3ox': [72, 97, 98, 136, 149, 153, 154],
               'c5ox': [98, 141, 150, 151, 154],
              }


cells_to_check = ['c2', 'c3', 'c5', 'c2ox', 'c3ox', 'c5ox']

X = np.linspace(-5., 5., 600*2)
Y = np.zeros(600*2)

for c in cells_to_check:
    print c,
    zero = offsets[c]['VBM']

    zeros_before = int(np.fabs(zero/dE))
    zeros_after = 600 - zeros_before

    for eprime in eprime_dict[c]:
        print eprime,
        x, y_u, y_d = get_at_pdos(c, eprime)
        Y_u = np.concatenate((np.zeros(zeros_before), 
                              y_u,
                              np.zeros(zeros_after)), axis=0)
        Y_d = np.concatenate((np.zeros(zeros_before), 
                              y_d,
                              np.zeros(zeros_after)), axis=0)
        #plt.plot(X, Y_u, 'k-', linewidth=1)
        #plt.plot(X, -Y_d, 'k-', linewidth=1)

        Y = Y + Y_u - Y_d

        #plt.plot(x, y_u, 'k-', linewidth=2)
        #nps, = plt.plot(x, y_d, 'k-', label='Unpassivated', linewidth=2)
    print

plt.plot(X, Y, 'k-', linewidth=2)
plt.axvspan(-5,0, facecolor='0.85', linewidth=0)
minor_locator = MultipleLocator(0.10)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

#plt.legend(handles=[nps, ps], ncol=2, fontsize=20)
plt.xlim([-2, 4])
#plt.ylim([-60, 60])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
#plt.gca().get_legend().get_frame().set_linewidth(2)

plt.xlabel('Energy [eV]', fontweight='bold', fontsize=20)

plt.gcf().set_size_inches(20., 3.5)
plt.savefig('dos_eprime.png', dpi=100, bbox_inches='tight')

plt.show()
