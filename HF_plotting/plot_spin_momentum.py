#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from helping_functions import get_similar, get_A0, get_spin_mom
from astools.ReadWrite import ReadStruct
from astools.analysis import distance

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

eprime_dict = {'c1'  : [142, 144],
               'c2'  : [124, 125, 134],
               'c3'  : [81, 113, 128, 134, 135, 147, 148],
               'c4'  : [124, 125, 127, 130, 136],
               'c5'  : [133, 135, 137],
               'c6'  : [125, 128, 131, 135, 136, 137, 144, 147],
               'c2ox': [82, 128, 136, 138, 148],
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

print 'Eprimes'
for c, eprimes in eprime_dict.items():
    print c 
    for eprime in eprimes:
        print '\t', eprime,
        s_m = get_spin_mom(eprime, c)
        #print '(s = ', s_m,
        A0 = get_A0(eprime, c)
        #print 'A ', A0, ')'

        epr ,= plt.plot(s_m, 0.5, 'g.', label="$E'$")

print 'Dimers'
for c, dimers in dimer_dict.items():
    print c 
    for dimer in dimers:
        print '\t', dimer,
        s_m = get_spin_mom(dimer, c)
        #print '(s = ', s_m,
        A0 = get_A0(dimer, c)
        #print 'A ', A0, ')'

        dim_,= plt.plot(s_m, 0.0, 'b.', label="dimer")

print 'Broken dimers'
for c, bdimers in bdimer_dict.items():
    print c 
    for bdimer in bdimers:
        print '\t', bdimer,
        s_m = get_spin_mom(bdimer, c)
        #print '(s = ', s_m,
        A0 = get_A0(bdimer, c)
        #print 'A ', A0, ')'

        bdim_,= plt.plot(s_m, -.5, 'y.', label="broken dimer")


plt.legend(handles=[epr, dim_, bdim_], fontsize=20)
plt.yticks([-.5, 0, .5])
plt.ylim([-1.5, 1.5])
plt.show()
