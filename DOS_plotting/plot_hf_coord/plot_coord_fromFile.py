#! /usr/bin/python2.7

import sys
sys.path.append('../../')
from helping_functions import neighbours_from_file

from astools.ReadWrite import ReadStruct
from astools.analysis import get_neighbours
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np 

#nms = ['hfo2si_c1']
nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c2ox', 'hfo2si_c3ox']

a = np.zeros(12, dtype=int)

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    it = (i+1 for i in range(len(s)))

    for at in it:
        if s.atoms[at-1].species == 'Hf':
            nbs = neighbours_from_file(at, nm)
            #nbs = [nb for nb in nbs if (nb.length < 2.5 and nb.atom_type == 'O')]
            nbs = [nb for nb in nbs if (nb.length < 3. and nb.atom_type == 'O')]
            a[len(nbs)] +=1

a = a*100/float(sum(a))


# bulk amorphous
b = np.zeros(12, dtype=int)
s = ReadStruct('../../crystal_files/INPUT_aHfO2')

it = (i+1 for i in range(len(s)))

avg = []

for at in it:
    if s.atoms[at-1].species == 'Hf':
        nbs = neighbours_from_file(at, 'aHfO2')
        #nbs = [nb for nb in nbs if (nb.length < 2.5 and nb.atom_type == 'O')]
        nbs = [nb for nb in nbs if (nb.length < 3. and nb.atom_type == 'O')]
        avg.append(len(nbs))
        b[len(nbs)] +=1
b = b*100/float(sum(b))


fig = plt.axes(xlim=(3, 9), ylim=(0,100.))
fig.bar(range(0, len(b)), b, color='paleturquoise', align='edge', width=0.3, label='Bulk Hafnia')
fig.bar(np.array(range(0, len(b)))-0.3, a, color='darksalmon', align='edge', width=0.3,
label='Si-Hafnia cells')
fig.set_xlabel('Hf-O coordination number', fontsize=20, fontweight='bold')
fig.set_ylabel('% of total', fontsize=20, fontweight='bold')
fig.legend(loc='upper left', fontsize=20)

plt.gca().get_legend().get_frame().set_linewidth(2)
plt.gca().yaxis.set_major_locator(MultipleLocator(5))
plt.gca().xaxis.set_tick_params(which='major', length=10, width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.gcf().set_size_inches(10., 9.)
plt.savefig('coordination_barchart_fromFile.png', dpi=100, bbox_inches='tight')

plt.figure()

a = np.zeros(12, dtype=int)

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    it = (i+1 for i in range(len(s)))

    for at in it:
        if s.atoms[at-1].species == 'Hf':
            nbs = neighbours_from_file(at, nm)
            nbs = [nb for nb in nbs if (nb.length < 3. and nb.atom_type == 'Hf')]
            a[len(nbs)] +=1

a = a*100/float(sum(a))


# bulk amorphous
b = np.zeros(12, dtype=int)
s = ReadStruct('../../crystal_files/INPUT_aHfO2')

it = (i+1 for i in range(len(s)))

avg = []
print 'woooo'
for at in it:
    if s.atoms[at-1].species == 'Hf':
        nbs = neighbours_from_file(at, 'aHfO2')
        nbs = [nb for nb in nbs if (nb.length < 3. and nb.atom_type == 'Hf')]
        if len(nbs) > 0:
            print at, s.atoms[at-1], len(nbs)
            for n in nbs:
                print '   {} {}'.format(n.atom_type, n.length)
        avg.append(len(nbs))
        b[len(nbs)] +=1

b = b*100/float(sum(b))

fig = plt.axes(xlim=(-0.5, 4), ylim=(0,100.))
fig.bar(range(0, len(b)), b, color='paleturquoise', align='edge', width=0.3, label='Bulk Hafnia')
fig.bar(np.array(range(0, len(b)))-0.3, a, color='darksalmon', align='edge', width=0.3,
label='Si-Hafnia cells')
fig.set_xlabel('Hf-Hf coordination', fontsize=20, fontweight='bold')
fig.set_ylabel('% of total', fontsize=20, fontweight='bold')
fig.legend(loc='upper right', fontsize=20)

plt.gca().get_legend().get_frame().set_linewidth(2)
plt.gca().yaxis.set_major_locator(MultipleLocator(5))
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.gca().xaxis.set_tick_params(which='major', length=10, width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.gcf().set_size_inches(10., 9.)
plt.savefig('coordination_barchart_fromFile_Hfnbs.png', dpi=100, bbox_inches='tight')


plt.show()

print 'Done'
