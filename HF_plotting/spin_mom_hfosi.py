#! /usr/bin/python2.7

import sys
sys.path.append('../')
from helping_functions import get_similar, get_A0, get_spin_mom
from astools.ReadWrite import ReadStruct
from astools.analysis import distance, get_neighbours

import math
import matplotlib.pyplot as plt

c1 = ReadStruct('../crystal_files/INPUT_hfo2si_c1')
c1ox = ReadStruct('../crystal_files/INPUT_hfo2si_c1ox')
c2ox = ReadStruct('../crystal_files/INPUT_hfo2si_c2ox')
c3ox = ReadStruct('../crystal_files/INPUT_hfo2si_c3ox')

pos_graph = {'Hf':0.5, 'Si':-0.5, 'O':0.}

x, y = [], []

print 'cell 1'
for no, at in enumerate(c1.atoms):
    spin_mom = get_spin_mom(no+1, 'hfo2si_c1')
    if math.fabs(spin_mom) > 0.5:
        print no+1, at
    y.append(pos_graph[at.species])
    x.append(spin_mom)

print 'cell 1 ox'
for no, at in enumerate(c1ox.atoms):
    spin_mom = get_spin_mom(no+1, 'hfo2si_c1ox')
    if math.fabs(spin_mom) > 0.5:
        print no+1, at
    y.append(pos_graph[at.species])
    x.append(spin_mom)

print 'cell 2 ox'
for no, at in enumerate(c2ox.atoms):
    spin_mom = get_spin_mom(no+1, 'hfo2si_c2ox')
    if math.fabs(spin_mom) > 0.5:
        print no+1, at
    y.append(pos_graph[at.species])
    x.append(spin_mom)

print 'cell 3 ox'
for no, at in enumerate(c3ox.atoms):
    spin_mom = get_spin_mom(no+1, 'hfo2si_c3ox')
    if math.fabs(spin_mom) > 0.5:
        print no+1, at
    y.append(pos_graph[at.species])
    x.append(spin_mom)


#nbs = get_neighbours(at, c1, dmax=3.5, no_neighbours=10)

#for x in nbs:
#    print x.at, x

plt.scatter(x,y)
plt.show()
print 'Done'
