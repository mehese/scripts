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

dimer_dict = {'c1': [130],
               'c2': [142],
               'c3': [128],
               'c4': [131],
               'c5': [131],
               'c6': [141],
               'c2ox': [],
               'c3ox': [],
               'c5ox': [129, 136],
              }

for c in ['c'+ i for i in map(str, range(2, 7))]:
    print c,
    for eprime in dimer_dict[c]:
        print eprime,
        x, y_u, y_d = get_at_pdos(c, eprime)
        plt.plot(x, y_u, 'k-')
        nps, =plt.plot(x, y_d, 'k-', label='Unpassivated')
        # Get the Atom object of the eprime
        at_e = ReadStruct('../../crystal_files/INPUT_'+c,
                          'crystal').atoms[eprime-1]
        p_str= ReadStruct('../../crystal_files/INPUT_'+c+'p', 'crystal')
        # get equivalent atom from passified structure
        i_x, at_p = get_similar(at_e, p_str)
        print '{:5.3f}'.format(distance(at_e, at_p)), 
        x, y_u, y_d = get_at_pdos(c+'p', i_x)
        plt.plot(x, y_u, 'r-')
        ps, =plt.plot(x, y_d, 'r-', label='H passivated')
    print

minor_locator = MultipleLocator(0.10)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

plt.legend(handles=[nps, ps], ncol=2, fontsize=16)
plt.axvspan(-5,-3.313, facecolor='0.85', linewidth=0)
plt.axvspan(-2.27,0.0, facecolor='0.85', linewidth=0)
plt.xlim([-5, 0])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.gca().get_legend().get_frame().set_linewidth(2)

plt.gcf().set_size_inches(20., 3.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=16)
plt.savefig('dos_OSiO.png', dpi=400, bbox_inches='tight')


plt.show()

