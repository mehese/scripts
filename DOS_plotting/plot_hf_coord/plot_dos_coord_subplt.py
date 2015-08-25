#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from helping_functions import neighbours_from_file
from atom_pdos_getter import integrate_dos, get_at_pdos
from atom_pdos_getter import *
from astools.ReadWrite import ReadStruct
from astools.analysis import distance
import numpy as np

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

#nms = ['hfo2si_c1']
nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c2ox', 'hfo2si_c3ox']

ks = range(3, 7)
fig = [None,]*len(ks)

x = np.linspace(0, 3*np.pi, 100)

minor_locator = MultipleLocator(0.10)
for i, k in enumerate(ks):
    fig[i] = plt.subplot(len(ks),1, i+1)
    fig[i].axvspan(-5+2.6,0, facecolor='0.85', linewidth=0)
    fig[i].axvspan(1.76,1+2.6, facecolor='0.85', linewidth=0)
    fig[i].set_xlim([-5+2.6, 1+2.6])
    fig[i].set_ylim([-30, 30])
    fig[i].text(-2.2, 20, str(k)+'-fold coordinated Hf', fontsize=18, weight='bold')
    fig[i].xaxis.set_minor_locator(minor_locator)
    fig[i].tick_params(which='minor', length=5, width=2)
    fig[i].tick_params(which='major', length=10, width=2, labelsize=15)
    fig[i].tick_params(which='major', length=10, width=2, labelsize=15)
    for x in ['top', 'bottom', 'left', 'right']:
        fig[i].spines[x].set_linewidth(2)
    plt.setp(fig[i].get_yticklabels(), visible=False)

for tick in fig[i].xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

print 'Done formatting!'

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    it = (i+1 for i in range(len(s)))
    
    for at in it:
        if s.atoms[at-1].species == 'Hf':
            nbs = neighbours_from_file(at, nm)
            nbs = [nb for nb in nbs if nb.length < 2.5]
            #print len(nbs)
            E, up, down = get_at_pdos(nm, at)
            fig[len(nbs)-3].plot(E+2.6,   up, 'k-')
            fig[len(nbs)-3].plot(E+2.6, down, 'k-')

print 'Done plotting!'
plt.subplots_adjust(hspace=0)

plt.gcf().set_size_inches(20., k*3.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=16)
plt.savefig('coord_dos_subplt.png', dpi=200, bbox_inches='tight')


plt.show()

