#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from helping_functions import neighbours_from_file, offsets
from atom_pdos_getter import integrate_dos, get_at_pdos
from atom_pdos_getter import *
from astools.ReadWrite import ReadStruct
from astools.analysis import distance, get_neighbours
import numpy as np

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c2ox', 'hfo2si_c3ox']
lims = {'hfo2si_c1':  (-2.54, -0.62), 
        'hfo2si_c1ox':(-2.62, -0.74), 
        'hfo2si_c2ox':(-2.48, -0.32), 
        'hfo2si_c3ox':(-2.43, -0.04)}


minor_locator = MultipleLocator(0.10)
fig = plt.subplot(111)
fig.axvspan(-5,    0, facecolor='0.85', linewidth=0)
fig.set_xlim([-1, 2.5])
#fig.set_ylim([0, 80])
#fig.text(-.9, 60, '', fontsize=22, weight='bold')
fig.xaxis.set_minor_locator(minor_locator)
fig.tick_params(which='minor', length=5, width=2)
fig.tick_params(which='major', length=10, width=2, labelsize=15)
for x in ['top', 'bottom', 'left', 'right']:
    fig.spines[x].set_linewidth(2)
plt.setp(fig.get_yticklabels(), visible=False)
plt.setp(fig.get_xticklabels(), visible=False)

for tick in fig.xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

print 'Done formatting!'

dE = 5./600

X = np.linspace(-5., 5., 600*2)
Y = np.zeros(600*2)
Y_tot = np.zeros(600*2)

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    zero = offsets[nm]['VBM'] 

    zeros_before = int(np.fabs(zero/dE))
    zeros_after = 600 - zeros_before


    #it = (i+1 for i in range(len(s)))
    it = (a for a in s.atoms)
    
    for i, at in enumerate(s.atoms): 
        if at.species=='Si':
            nbs = neighbours_from_file(i+1, nm)
            nbs = [nb for nb in nbs if (nb.length < 3 and nb.atom_type == 'Hf')]
            E, y_u, y_d = get_at_pdos(nm, i+1)
            Y_u = np.concatenate((np.zeros(zeros_before), y_u, np.zeros(zeros_after)), axis=0)
            Y_d = np.concatenate((np.zeros(zeros_before), y_d, np.zeros(zeros_after)), axis=0)
            if len(nbs) > 1:
                Y= Y + Y_u - Y_d
            Y_tot= Y_tot + Y_u - Y_d


fig.plot(X, Y, 'r', linewidth=2)
fig.plot(X, Y_tot, 'k', linewidth=2)
plt.setp(fig.get_xticklabels(), visible=True)

plt.gcf().set_size_inches(20., 3.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=20)
plt.savefig('dos_Si_HfBonded.png', dpi=100, bbox_inches='tight')

print 'Done plotting!'
plt.show()
