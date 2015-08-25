#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from helping_functions import neighbours_from_file
from atom_pdos_getter import integrate_dos, get_at_pdos
from atom_pdos_getter import *
from astools.ReadWrite import ReadStruct
from astools.analysis import distance

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

#nms = ['hfo2si_c1']
nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c2ox', 'hfo2si_c3ox']

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    it = (i+1 for i in range(len(s)))
    
    for at in it:
        if s.atoms[at-1].species == 'Hf':
            nbs = neighbours_from_file(at, nm)
            #for n in nbs:
            #    print n.atom_type, n.length
            nbs = [nb for nb in nbs if nb.length < 2.5]
            print len(nbs)
            if len(nbs) == 6:
                print 'here'
                E, up, down = get_at_pdos(nm, at)
                plt.plot(E+2.6,   up, 'k-')
                plt.plot(E+2.6, down, 'k-')


minor_locator = MultipleLocator(0.10)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

plt.text(-1.8, 30, '6-fold coordinated Hf', fontsize=16, weight='bold')
plt.axvspan(-5+2.6,0, facecolor='0.85', linewidth=0)
plt.axvspan(1.76,1+2.6, facecolor='0.85', linewidth=0)
plt.xlim([-5+2.6, 1+2.6])
plt.ylim([-60, 60])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
#plt.gca().get_legend().get_frame().set_linewidth(2)

plt.gcf().set_size_inches(20., 3.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=16)
#plt.savefig('coord_dos_subplt.png', dpi=400, bbox_inches='tight')


plt.show()

