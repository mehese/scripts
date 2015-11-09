#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from atom_pdos_getter import *
from helping_functions import get_similar, offsets, get_spin_mom
from astools.ReadWrite import ReadStruct
from astools.analysis import distance

import numpy as np

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

# This plots the distribution of the E' DOS relative to the structure's VBM. The
# VBM for each cell is set to the 0 eV level. The VBM is found in the
# helping_functions.py file.

# 5eV range with 600 points in the read files
dE = 5./600

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

to_switch = {'c1':     {107: False},
               'c2':   { 82: False},
               'c3':   { 58: False,  66: False},
               'c4':   { 65: False, 119: False},
               'c5':   { 82:  True, 102: False},
               'c6':   { 66: False, 101: False, 119: False},
               'c2ox': { 72: False},
               'c3ox': { 65: False},
               'c5ox': { 65: False},
              }



cells_to_check = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c2ox', 'c3ox', 'c5ox']
#cells_to_check = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']

X = np.linspace(-5., 5., 600*2)
Y = np.zeros(600*2)
YU = np.zeros(600*2)
YD = np.zeros(600*2)
Yp = np.zeros(600*2)
YpU = np.zeros(600*2)
YpD = np.zeros(600*2)

no_bdimers = 0
for c in cells_to_check:
    print c
    zero = offsets[c]['VBM']

    zeros_before = int(np.fabs(zero/dE))
    zeros_after = 600 - zeros_before
    #plt.plot([offsets[c]['Ef']-offsets[c]['VBM'],]*2, [-30,30], 'r--')

    for bdimer in bdimer_dict[c]:
        s = get_spin_mom(bdimer, c)
        lims = (0.0, 1.0)
        lims = (0.0, 0.4)
        #lims = (0.2, 0.4)
        #lims = (0.4, 0.6)
        #lims = (0.6, 0.8)
        #lims = (0.6, 1.0)
        if lims[0] <= np.fabs(s) <= lims[1]:
            print s, bdimer
            x, y_u, y_d = get_at_pdos(c, bdimer)
            Y_u = np.concatenate((np.zeros(zeros_before), 
                                  y_u,
                                  np.zeros(zeros_after)), axis=0)
            Y_d = np.concatenate((np.zeros(zeros_before), 
                                  y_d,
                                  np.zeros(zeros_after)), axis=0)
            Y = Y + Y_u - Y_d
            if to_switch[c][bdimer]:
                print c, bdimer, 'switch'
                YU -= Y_d
                YD -= Y_u
            else:
                YU += Y_u
                YD += Y_d

            #plt.plot(X, Y_u, 'b-', linewidth=3)
            #plt.plot(X, Y_d, 'b-', linewidth=3)
            
            if 'ox' not in c:
                at_e = ReadStruct('../../crystal_files/INPUT_'+c,
                                          'crystal').atoms[bdimer-1]
                p_str= ReadStruct('../../crystal_files/INPUT_'+c+'p', 'crystal')

                i_x, at_p = get_similar(at_e, p_str)

                x, yy_u, yy_d = get_at_pdos(c+'p', i_x)
                Yp_u = np.concatenate((np.zeros(zeros_before), 
                                      yy_u,
                                      np.zeros(zeros_after)), axis=0)
                Yp_d = np.concatenate((np.zeros(zeros_before), 
                                      yy_d,
                                      np.zeros(zeros_after)), axis=0)
                #plt.plot(X, Yp_u, 'g-')
                #plt.plot(X, Yp_d, 'g-')
                Yp = Yp + Yp_u - Yp_d
                if to_switch[c][bdimer]:
                    print c, bdimer, 'switch'
                    YpU -= Yp_d
                    YpD -= Yp_u
                else:
                    YpU += Yp_u
                    YpD += Yp_d
            no_bdimers += 1

print '-'*30
print no_bdimers

plt.text(2, 60, str(lims[0])+'< spin < '+str(lims[1]), fontsize=30, weight='bold')
plt.text(2, 40, 'No broken dimers = '+str(no_bdimers), fontsize=25, weight='bold')
#plt.plot(X, Y, 'k-', linewidth=2)
#plt.plot(X, Yp, 'r-', linewidth=2)
plt.plot(X, YU, 'k-', linewidth=2)
plt.plot(X, YD, 'k-', linewidth=2)
#plt.plot(X, YpU, 'r-', linewidth=2)
#plt.plot(X, YpD, 'r-', linewidth=2)
plt.axvspan(-5,0, facecolor='0.85', linewidth=0)
minor_locator = MultipleLocator(0.10)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

#plt.legend(handles=[nps, ps], ncol=2, fontsize=20)
plt.xlim([-2, 4])
plt.ylim([-50, 50])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
#plt.gca().get_legend().get_frame().set_linewidth(2)

plt.xlabel('Energy [eV]', fontweight='bold', fontsize=20)

plt.gcf().set_size_inches(20., 3.5)
plt.savefig('dos_bdimer_all'+str(lims[0])+'_'+str(lims[1])+'.png', dpi=100, bbox_inches='tight')

plt.show()
