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

o = lambda k : k + 3.313

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

x, y_u, y_d = get_at_pdos('c2', 105)
x = [o(p) for p in x]
plt.plot(x, y_u, 'k-', linewidth=2)
nps, =plt.plot(x, y_d, 'k-', label='Unpassivated', linewidth=2)
# Get the Atom object of the atom
at_e = ReadStruct('../../crystal_files/INPUT_c2', 'crystal').atoms[68-1]
p_str= ReadStruct('../../crystal_files/INPUT_c2p', 'crystal')
# get equivalent atom from passified structure
i_x, at_p = get_similar(at_e, p_str)
print '{:5.3f}'.format(distance(at_e, at_p)), 
x, y_u, y_d = get_at_pdos('c2p', i_x)
x = [o(p) for p in x]
plt.plot(x, y_u, 'r-', linewidth=2.5)
ps, =plt.plot(x, y_d, 'r-', label='H passivated', linewidth=2.5)
print

minor_locator = MultipleLocator(0.10)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

plt.legend(handles=[nps, ps], ncol=2, fontsize=20)
plt.axvspan(o(-5),o(-3.313), facecolor='0.85', linewidth=0)
plt.axvspan(o(-2.27),o(0.0), facecolor='0.85', linewidth=0)
plt.xlim([o(-5), o(0)])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.gca().get_legend().get_frame().set_linewidth(2)

plt.gcf().set_size_inches(20., 3.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=20)
plt.savefig('dos_Pb0.png', dpi=80, bbox_inches='tight')


plt.show()

