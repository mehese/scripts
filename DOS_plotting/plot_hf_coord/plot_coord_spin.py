#! /usr/bin/python2.7

import sys
sys.path.append('../../')
sys.path.append('../')
from helping_functions import neighbours_from_file
from atom_pdos_getter import integrate_dos, get_at_pdos

from astools.ReadWrite import ReadStruct
from astools.analysis import get_neighbours
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np 

nms = ['hfo2si_c1']
#nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c2ox', 'hfo2si_c3ox']
nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c3ox']

a = np.zeros(12, dtype=int)
print a
y = [[] for i in range(len(a))]
print y

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    it = (i+1 for i in range(len(s)))

    for at in it:
        if s.atoms[at-1].species == 'Hf':
            nbs = neighbours_from_file(at, nm)
            #for n in nbs:
            #    print n.atom_type, n.length
            nbs = [nb for nb in nbs if nb.length < 2.5]
            a[len(nbs)] +=1
            E, up, down = get_at_pdos(nm, at)
            dos = integrate_dos(E, up, down, emin=-2.6, emax=-0.84) # tweak emin and emax
            y[len(nbs)].append(dos)

print a
print y


fig = plt.axes(xlim=(2, 8))

fig.axhline(0, color='black', linewidth=2)
for i, coord in enumerate(a):
    if coord:
        fig.scatter(coord*[i], y[i], color='olivedrab', s=55)

#fig.bar(np.array(range(1, len(b)+1))-0.3, a, color='darksalmon', align='edge', width=0.3,
#label='Si-Hafnia cells')
fig.set_xlabel('Hf coordination number', fontsize=16, fontweight='bold')
fig.set_ylabel('Si-Gap DOS', fontsize=16, fontweight='bold')
#fig.legend(loc='upper left', fontsize=14)

#plt.gca().get_legend().get_frame().set_linewidth(2)
plt.gca().yaxis.set_major_locator(MultipleLocator(5))
plt.gca().xaxis.set_tick_params(which='major', length=10, width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.gcf().set_size_inches(10., 9.)
plt.savefig('coordination_DOS.png', dpi=100, bbox_inches='tight')
plt.show()

print 'Done'
