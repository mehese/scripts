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
    A0 = get_A0(no+1, 'hfo2si_c1')
    if math.fabs(A0) > 10:
        print no+1, at
    y.append(pos_graph[at.species])
    x.append(A0)

print 'cell 1 ox'
for no, at in enumerate(c1ox.atoms):
    A0 = get_A0(no+1, 'hfo2si_c1ox')
    if math.fabs(A0) > 10:
        print no+1, at
    y.append(pos_graph[at.species])
    x.append(A0)

print 'cell 2 ox'
for no, at in enumerate(c2ox.atoms):
    A0 = get_A0(no+1, 'hfo2si_c2ox')
    if math.fabs(A0) > 10:
        print no+1, at
    y.append(pos_graph[at.species])
    x.append(A0)

print 'cell 3 ox'
for no, at in enumerate(c1.atoms):
    A0 = get_A0(no+1, 'hfo2si_c3ox')
    if math.fabs(A0) > 10:
        print no+1, at
    y.append(pos_graph[at.species])
    x.append(A0)


plt.scatter(x,y)
plt.show()
print 'Done'
