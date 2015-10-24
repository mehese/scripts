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
nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c2ox', 'hfo2si_c3ox']
#nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c3ox']
lims = {'hfo2si_c1':  (-2.54, -0.62), 
        'hfo2si_c1ox':(-2.62, -0.74), 
        'hfo2si_c2ox':(-2.48, -0.32), 
        'hfo2si_c3ox':(-2.43, -0.04)}

a = np.zeros(6, dtype=int)
y = [[] for i in range(len(a))]

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    for i, at in enumerate(s.atoms):
        if at.species == 'Hf':
            nbs = neighbours_from_file(i+1, nm)
            nbs = [nb for nb in nbs if (nb.length < 3. and nb.atom_type == 'Hf')]
            a[len(nbs)] +=1
            E, up, down = get_at_pdos(nm, i+1)
            vbm, cbm = lims[nm]
            dos = integrate_dos(E, up, down, emin=vbm, emax=cbm) # tweak emin and emax
            y[len(nbs)].append(dos)

xs, ys = np.array([]), np.array([])
for x, p in enumerate(y):
    g = np.array([x]*len(p))
    xs = np.append(xs, g)
    ys = np.append(ys, p)
    

fig = plt.axes(xlim=(-1, 5))
fig.scatter(xs, ys, marker='o', facecolors='none')

#fig.boxplot(y[:], showfliers=False)
#fig.set_xticklabels(range(6))

fig.axhline(0, linestyle=':', color='black')

#for i, coord in enumerate(a):
#    if coord:
#        fig.scatter(coord*[i], y[i], color='olivedrab', s=55)

#fig.bar(np.array(range(1, len(b)+1))-0.3, a, color='darksalmon', align='edge', width=0.3,
#label='Si-Hafnia cells')
fig.set_xlabel('Hf-Hf coordination number', fontsize=16, fontweight='bold')
fig.set_ylabel('Integrated Gap DOS', fontsize=16, fontweight='bold')
#fig.legend(loc='upper left', fontsize=14)


#plt.gca().get_legend().get_frame().set_linewidth(2)
#plt.gca().yaxis.set_major_locator(MultipleLocator(5))
plt.gca().xaxis.set_tick_params(which='major', length=10, width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.gcf().set_size_inches(10., 9.)
plt.savefig('coordination_DOS2.png', dpi=100, bbox_inches='tight')

plt.figure()

a = np.zeros(6, dtype=int)
y = [[] for i in range(len(a))]

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    for i, at in enumerate(s.atoms):
        if at.species == 'Hf':
            nbs = neighbours_from_file(i+1, nm)
            nbs = [nb for nb in nbs if (nb.length < 3. and nb.atom_type == 'Si')]
            a[len(nbs)] +=1
            E, up, down = get_at_pdos(nm, i+1)
            vbm, cbm = lims[nm]
            dos = integrate_dos(E, up, down, emin=vbm, emax=cbm) # tweak emin and emax
            y[len(nbs)].append(dos)

xs, ys = np.array([]), np.array([])
for x, p in enumerate(y):
    g = np.array([x]*len(p))
    xs = np.append(xs, g)
    ys = np.append(ys, p)
    

fig = plt.axes(xlim=(-10, 7))
fig.scatter(xs, ys, marker='o', facecolors='none')

fig.boxplot(y[:], showfliers=False)
fig.set_xticklabels(range(6))

fig.axhline(0, linestyle=':', color='black')

#for i, coord in enumerate(a):
#    if coord:
#        fig.scatter(coord*[i], y[i], color='olivedrab', s=55)

#fig.bar(np.array(range(1, len(b)+1))-0.3, a, color='darksalmon', align='edge', width=0.3,
#label='Si-Hafnia cells')
fig.set_xlabel('Hf coordination number', fontsize=16, fontweight='bold')
fig.set_ylabel('Integrated Gap DOS', fontsize=16, fontweight='bold')
#fig.legend(loc='upper left', fontsize=14)


#plt.gca().get_legend().get_frame().set_linewidth(2)
#plt.gca().yaxis.set_major_locator(MultipleLocator(5))
plt.gca().xaxis.set_tick_params(which='major', length=10, width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.gcf().set_size_inches(10., 9.)
plt.savefig('coordination_DOS_HfSi.png', dpi=100, bbox_inches='tight')

plt.show()

print 'Done'
