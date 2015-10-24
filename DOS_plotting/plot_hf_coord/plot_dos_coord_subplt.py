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

ks = range(4, 9)
fig = [None,]*len(ks)

minor_locator = MultipleLocator(0.10)
for i, k in enumerate(ks):
    fig[i] = plt.subplot(len(ks),1, i+1)
    fig[i].axvspan(-5,    0, facecolor='0.85', linewidth=0)
    fig[i].set_xlim([-1, 2])
    fig[i].set_ylim([0, 80])
    fig[i].text(-.9, 60, str(k)+'-fold O coordinated Hf', fontsize=22, weight='bold')
    fig[i].xaxis.set_minor_locator(minor_locator)
    fig[i].tick_params(which='minor', length=5, width=2)
    fig[i].tick_params(which='major', length=10, width=2, labelsize=15)
    for x in ['top', 'bottom', 'left', 'right']:
        fig[i].spines[x].set_linewidth(2)
    plt.setp(fig[i].get_yticklabels(), visible=False)
    plt.setp(fig[i].get_xticklabels(), visible=False)

for tick in fig[i].xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

print 'Done formatting!'

dE = 5./600

X = np.linspace(-5., 5., 600*2)
Y = [np.zeros(600*2),]*len(ks)
kf = [0,]*len(ks)

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    zero = offsets[nm]['VBM'] 

    zeros_before = int(np.fabs(zero/dE))
    zeros_after = 600 - zeros_before


    #it = (i+1 for i in range(len(s)))
    it = (a for a in s.atoms)
    
    for i, at in enumerate(s.atoms): 
        if at.species=='Hf':
            nbs = neighbours_from_file(i+1, nm)
            nbs = [nb for nb in nbs if (nb.length < 3 and nb.atom_type == 'O')]
            E, y_u, y_d = get_at_pdos(nm, i+1)
            Y_u = np.concatenate((np.zeros(zeros_before), y_u, np.zeros(zeros_after)), axis=0)
            Y_d = np.concatenate((np.zeros(zeros_before), y_d, np.zeros(zeros_after)), axis=0)
            Y[len(nbs) - ks[0]] = Y[len(nbs) - ks[0]] + Y_u - Y_d
            kf[len(nbs) - ks[0]] += 1

print kf
for i in range(len(Y)):
    fig[i].plot(X, Y[i], 'k', linewidth=2)
plt.setp(fig[i].get_xticklabels(), visible=True)

plt.subplots_adjust(hspace=0)

plt.gcf().set_size_inches(20., len(ks)*3.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=20)
plt.savefig('coord_dos_subplt_HfO.png', dpi=100, bbox_inches='tight')

print 'Done plotting!'
plt.show()
