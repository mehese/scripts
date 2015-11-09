#! /usr/bin/python2.7

import sys
sys.path.append('../')
from helping_functions import get_similar, get_A0, get_spin_mom
from astools.ReadWrite import ReadStruct
from astools.analysis import distance, get_neighbours

import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

c1 = ReadStruct('../crystal_files/INPUT_hfo2si_c1')
c1ox = ReadStruct('../crystal_files/INPUT_hfo2si_c1ox')
c2ox = ReadStruct('../crystal_files/INPUT_hfo2si_c2ox')
c3ox = ReadStruct('../crystal_files/INPUT_hfo2si_c3ox')

pos_graph = {'Hf':0.5, 'Si':-0.5, 'O':0.}
scatter = {'Hf':[], 'O':[], 'Si':[]}

x, y = [], []

print 'cell 1'
for no, at in enumerate(c1.atoms):
    A0 = get_A0(no+1, 'hfo2si_c1')
    if math.fabs(A0) > 10:
        print no+1, at, A0
    y.append(pos_graph[at.species])
    scatter[at.species].append(A0)
    x.append(A0)

print 'cell 1 ox'
for no, at in enumerate(c1ox.atoms):
    A0 = get_A0(no+1, 'hfo2si_c1ox')
    if math.fabs(A0) > 10:
        print no+1, at, A0
    y.append(pos_graph[at.species])
    scatter[at.species].append(A0)
    x.append(A0)

print 'cell 2 ox'
for no, at in enumerate(c2ox.atoms):
    A0 = get_A0(no+1, 'hfo2si_c2ox')
    if math.fabs(A0) > 10:
        print no+1, at, A0
    y.append(pos_graph[at.species])
    scatter[at.species].append(A0)
    x.append(A0)

print 'cell 3 ox'
for no, at in enumerate(c1.atoms):
    A0 = get_A0(no+1, 'hfo2si_c3ox')
    if math.fabs(A0) > 10:
        print no+1, at, A0
    y.append(pos_graph[at.species])
    scatter[at.species].append(A0)
    x.append(A0)

Hfy, Hfx =  [0.5,]*len(scatter['Hf']),[math.fabs(x) for x in scatter['Hf']]
Oy ,  Ox =  [0. ,]*len(scatter[ 'O']),[math.fabs(x) for x in scatter[ 'O']]
Siy, Six = [-0.5,]*len(scatter['Si']),[math.fabs(x) for x in scatter['Si']]

plt.scatter(Hfx, Hfy, c='#4D0000', label='Hf', s=92)
plt.scatter( Ox,  Oy, c='crimson', label='O',  s=92)
plt.scatter(Six, Siy, c='teal',    label='Si', s=92)

plt.gca().xaxis.set_minor_locator(MultipleLocator(5))
plt.gca().yaxis.set_tick_params(which='major', length=10, width=2, tickdir='left')

plt.gca().xaxis.set_tick_params(which='major', length=10, width=2, labelsize=15)
plt.gca().xaxis.set_tick_params(which='minor', length=5, width=2, labelsize=15)

#plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for tick in plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontsize('25')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

#plt.legend(fontsize=16, ncol=3)
#plt.gca().get_legend().get_frame().set_linewidth(2)
plt.yticks([-.5, 0, .5], ["Si   ",'O   ',"Hf  "])
#plt.gca().set_yticklabels(("broken dimers  ",'dimers  ',"E'  "))
plt.xlim([-1., 30])
plt.ylim([-1., 1.])
plt.xlabel('A0 [mT]', fontweight='bold', fontsize=25)

plt.gcf().set_size_inches(20., 7.)
plt.savefig('hfo2si_A0_defects.png', dpi=80, bbox_inches='tight')
plt.show()
