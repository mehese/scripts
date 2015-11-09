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

class data_point:
    def __init__(self, O_coord, Hf_coord, Si_coord, dos_integral):
        self.O = O_coord
        self.Hf = Hf_coord
        self.Si = Si_coord
        self.val = dos_integral
    def __str__(self):
        return 'O coord = {:2.0f}, Hf coord = {:2.0f}, Si coord = {:2.0f}, DOS = {:10.5f}'.format(self.O, self.Hf, self.Si, self.val)
       
# Hf coordination radius
r = 3.       

nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c2ox', 'hfo2si_c3ox']
lims = {'hfo2si_c1':  (-2.54, -0.62), 
        'hfo2si_c1ox':(-2.62, -0.74), 
        'hfo2si_c2ox':(-2.48, -0.32), 
        'hfo2si_c3ox':(-2.43, -0.04)}

a = np.zeros(12, dtype=int)
y = [[] for i in range(len(a))]

pts = []

for nm in nms:
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    for i, at in enumerate(s.atoms):
        if at.species == 'Hf':
            nbs = neighbours_from_file(i+1, nm)
            nbO = [nb for nb in nbs if (nb.length < r and nb.atom_type == 'O')]
            nbH = [nb for nb in nbs if (nb.length < r and nb.atom_type == 'Hf')]
            nbS = [nb for nb in nbs if (nb.length < r and nb.atom_type == 'Si')]
            a[len(nbO)] +=1
            E, up, down = get_at_pdos(nm, i+1)
            vbm, cbm = lims[nm]
            dos = integrate_dos(E, up, down, emin=vbm, emax=cbm) # tweak emin and emax
            pts.append(data_point(len(nbO), len(nbH), len(nbS), dos))
            y[len(nbO)].append(dos)
            #print pts[-1]

fig = plt.axes(xlim=(3,9), ylim=(-0.05, 1.1))

fig.axhline(0, linestyle=':', color='black')

for pt in pts:
    fig.scatter(pt.O, pt.val, marker='.', c='#ff0000', edgecolor='', s=60)
    #print '.', 
    for i in range(pt.Hf):
        fig.scatter(pt.O - 0.1 - 0.1*i, pt.val, c='#B8B8E6', edgecolor='', s=120)
        #print ' H',
    for i in range(pt.Si):
        fig.scatter(pt.O + 0.1 + 0.1*i, pt.val, c='#33CCFF', edgecolor='', s=120)
        #print ' S',
    #print

for i in range(4, 9):
    #print i
    m = np.mean(y[i])
    plt.plot([i-0.3, i+0.3], [m, m], 'r-')



fig.set_xlabel('Hf-O coordination number', fontsize=25, fontweight='bold')
fig.set_ylabel('Integrated Gap DOS', fontsize=25, fontweight='bold')

plt.gca().xaxis.set_tick_params(which='major', length=10, width=2, labelsize=16)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)


plt.gcf().set_size_inches(20., 20.)
plt.savefig('coordination_DOS_marked.png', dpi=100, bbox_inches='tight')

plt.show()
print 'Done'
