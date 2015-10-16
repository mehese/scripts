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
        'hfo2si_c2ox':(-2.13, -0.32), 
        'hfo2si_c3ox':(-2.22, -0.04)}

a = np.zeros(12, dtype=int)
print a
y = [[] for i in range(len(a))]
print y

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)
    print nm

    for i, at in enumerate(s.atoms):
        if at.species == 'Hf':
            nbs = get_neighbours(at, s, dmax=3, no_neighbours=10)
            #print at
            #for n in nbs:
            #    print n.at, n.length
            nbs = [nb for nb in nbs if nb.length < 2.5]
            #print len(nbs)
            a[len(nbs)] +=1
            E, up, down = get_at_pdos(nm, i+1)
            vbm, cbm = lims[nm]
            dos = integrate_dos(E, up, down, emin=vbm, emax=cbm) # tweak emin and emax
            y[len(nbs)].append(dos)

#print a
xs, ys = np.array([]), np.array([])
#print x
for x, p in enumerate(y):
    print x, p, 
    g = np.array([x]*len(p))
    xs = np.append(xs, g)
    ys = np.append(ys, p)
    
print 'xs = ', xs

fig = plt.axes(xlim=(2, 9))
fig.scatter(xs, ys, marker='o', facecolors='none')

fig.boxplot(y[1:], showfliers=False)

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
plt.savefig('coordination_DOS.png', dpi=100, bbox_inches='tight')
plt.show()

print 'Done'
