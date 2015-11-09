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

eprime_dict = {'c1': [142, 144],
               'c2': [124, 125, 134],
               'c3': [81, 113, 134, 135, 147, 148],
               'c4': [127, 130, 136],
               'c5': [126, 133, 135, 137],
               'c6': [125, 128, 131, 135, 137, 144, 147],
               'c2ox': [128, 136, 138, 148, 150],
               'c3ox': [72, 97, 98, 136, 149, 153, 154],
               'c5ox': [98, 141, 150, 151, 154],
              }

dimer_dict = {'c1': [57, 113],
              'c2': [102, 114],
              'c3': [101, 73],
              'c4': [],
              'c5': [65],
              'c6': [113],
              'c2ox': [86],
              'c3ox': [73],
              'c5ox': [117],
             }

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

#for c, _ in eprime_dict.items():
#    print '\n'+c+'--',
#    for i in range(1,165):
#        #print i,
#        try :
#            A0 = get_A0(i, c)
#        except:
#            break
#
#        full, = plt.plot(fabs(A0), 0.5, 'ko', fillstyle='none', markersize=12, label='all')
#

print 'Broken dimers'
Ds, As = [], []
for c, bdimers in bdimer_dict.items():
    s = ReadStruct('../crystal_files/INPUT_'+c) 
    for bdimer in bdimers:

        nbs = neighbours_from_file(bdimer, c)
        print c, bdimer, len([n  for n in nbs if (n.length < 2.5)])
        nb2 = [n.length  for n in nbs if (n.length < 2.5 and n.atom_type=='Si')]
        print nb2
        #d = sum(nb2)/len(nb2)
        d = max(nb2)
        Ds.append(d)
        for nb in nbs:
            print '    ', nb.atom_type, nb.length

        A0 = get_A0(bdimer, c)
        As.append(fabs(A0))
    
        #epr ,= plt.plot(fabs(A0), 0.5, 'yo', markersize=12, label="$E'$")

print Ds, As
plt.scatter(Ds, As, edgecolor='0.1', linewidths=2, s=250, facecolor='none')

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
plt.xlim([2.2, 2.6])
plt.ylim(ymin=-.4)
plt.xlabel(r'broken dimer average length [$\mathbf{\AA{}}$]', fontweight='bold', fontsize=25)
plt.ylabel('A0 [mT]', fontweight='bold', fontsize=25)

plt.gcf().set_size_inches(10., 10.)
plt.savefig('A0_bdimer_length.png', dpi=80, bbox_inches='tight')
plt.show()
