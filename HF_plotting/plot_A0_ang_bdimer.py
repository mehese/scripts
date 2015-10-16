#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from helping_functions import get_similar, get_A0, get_spin_mom, neighbours_from_file
from astools.ReadWrite import ReadStruct
from astools.analysis import distance, get_neighbours

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator
from math import fabs
import numpy as np
import numpy.linalg as ln



bdimer_dict = {'c1': [107],
               'c2': [82],
               'c3': [58, 66],
               'c4': [65, 119],
               'c5': [82, 102],
               'c6': [66, 101, 119],
               'c2ox': [72],
               'c3ox': [65],
               'c5ox': [65],
              }



#dimer_dict = {'c5':[65]}
print 'Broken dimers'
angs, As = [], []
for c, bdimers in bdimer_dict.items():
    s = ReadStruct('../crystal_files/INPUT_'+c) 
    for bdimer in bdimers:
        at_x = s.atoms[bdimer-1]

        nbs = get_neighbours(at_x, s, dmax=3.8, no_neighbours=3)
        print c, bdimer, at_x
        vecs = []
        for nb in nbs:
            print '    ', nb
            vec = np.array([nb.at.x, nb.at.y, nb.at.z]) - np.array([at_x.x, at_x.y, at_x.z])
            #print vec, ln.norm(vec)
            vecs.append(vec)
        
        val = []
        for i, j in (0,1), (1,2), (0,2):
            #print vecs[i], vecs[j]
            angle = np.degrees(np.arccos( np.dot(vecs[i], vecs[j])  / (ln.norm(vecs[i]) * ln.norm(vecs[j]))) )
            val.append( angle)
            print '   angle = ', angle
        
        val = sum(val)/3.
        angs.append(val)
        A0 = get_A0(bdimer, c)
        As.append(fabs(A0))


plt.scatter(angs, As, edgecolor='0.1', linewidths=2, s=250, facecolor='none')

plt.gca().xaxis.set_minor_locator(MultipleLocator(5))
plt.gca().yaxis.set_tick_params(which='major', length=10, width=2)

plt.gca().xaxis.set_tick_params(which='major', length=10, width=2, labelsize=15)
plt.gca().xaxis.set_tick_params(which='minor', length=5, width=2, labelsize=15)

#plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

#plt.legend(handles=[full, epr, dim_, bdim_], fontsize=16, ncol=4)
#plt.gca().get_legend().get_frame().set_linewidth(2)
#plt.xlim([1.55, 2.])
plt.ylim(ymin=-1)
plt.xlabel('Average angle [deg]', fontweight='bold', fontsize=16)
plt.ylabel('A0 [mT]', fontweight='bold', fontsize=16)

plt.gcf().set_size_inches(10., 10.)
plt.savefig('A0_bdimer_ang.png', dpi=80, bbox_inches='tight')
plt.show()
