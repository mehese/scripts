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
eprime_dict = {'c1': [142, 144],
               'c2': [124, 125, 134],
               'c3': [81, 113, 134, 135, 147, 148],
               'c4': [124, 125, 127, 130, 136],
               'c5': [126, 133, 135, 137],
               'c6': [125, 128, 131, 135, 136, 137, 144, 147],
               'c2ox': [84, 128, 136, 138, 148, 150],
               'c3ox': [72, 97, 98, 136, 149, 153, 154],
               'c5ox': [98, 141, 150, 151, 154],
              }
to_switch = {'c1':     {142: False, 144: False},
               'c2':   {124: False, 125:  True, 134:  True},
               'c3':   { 81: False, 113: False, 134: False, 135: False, 147: False, 148: False},
               'c4':   {124: False, 125: False, 127: False, 130: False, 136: False},
               'c5':   {126:  True, 133:  True, 135: False, 137:  True},
               'c6':   {125: False, 128: False, 131: False, 135: False, 136: False, 137: False, 144: False, 147: False},
               'c2ox': { 84: False, 128: False, 136: False, 138: False, 148: False, 150: False},
               'c3ox': { 72: False,  97: False,  98: False, 136: False, 149: False, 153: False, 154:  True},
               'c5ox': { 98: False, 141: False, 150: False, 151: False, 154: False},
              }



cells_to_check = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c2ox', 'c3ox', 'c5ox']
#cells_to_check = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']
#cells_to_check = ['c2ox', 'c3ox', 'c5ox']


def get_Y(lim_low, lim_high):
    X = np.linspace(-5., 5., 600*2)
    Y = np.zeros(600*2)
    YU = np.zeros(600*2)
    YD = np.zeros(600*2)
    Yp = np.zeros(600*2)
    YpU = np.zeros(600*2)
    YpD = np.zeros(600*2)

    no_eprimes = 0
    for c in cells_to_check:
        print c
        zero = offsets[c]['VBM']

        zeros_before = int(np.fabs(zero/dE))
        zeros_after = 600 - zeros_before
        #plt.plot([offsets[c]['Ef']-offsets[c]['VBM'],]*2, [-30,30], 'r--')

        for eprime in eprime_dict[c]:
            s = get_spin_mom(eprime, c)
            if lim_low <= np.fabs(s) <= lim_high:
                print s, eprime
                x, y_u, y_d = get_at_pdos(c, eprime)
                Y_u = np.concatenate((np.zeros(zeros_before), 
                                      y_u,
                                      np.zeros(zeros_after)), axis=0)
                Y_d = np.concatenate((np.zeros(zeros_before), 
                                      y_d,
                                      np.zeros(zeros_after)), axis=0)
                Y = Y + Y_u - Y_d
                if to_switch[c][eprime]:
                    print c, eprime, 'switch'
                    YU -= Y_d
                    YD -= Y_u
                else:
                    YU += Y_u
                    YD += Y_d

                
                if 'ox' not in c:
                    at_e = ReadStruct('../../crystal_files/INPUT_'+c,
                                              'crystal').atoms[eprime-1]
                    p_str= ReadStruct('../../crystal_files/INPUT_'+c+'p', 'crystal')

                    i_x, at_p = get_similar(at_e, p_str)

                    x, yy_u, yy_d = get_at_pdos(c+'p', i_x)
                    Yp_u = np.concatenate((np.zeros(zeros_before), 
                                          yy_u,
                                          np.zeros(zeros_after)), axis=0)
                    Yp_d = np.concatenate((np.zeros(zeros_before), 
                                          yy_d,
                                          np.zeros(zeros_after)), axis=0)
                    Yp = Yp + Yp_u - Yp_d
                    if to_switch[c][eprime]:
                        print c, eprime, 'switch'
                        YpU -= Yp_d
                        YpD -= Yp_u
                    else:
                        YpU += Yp_u
                        YpD += Yp_d
                no_eprimes = no_eprimes + 1

    return X, YU, YD, no_eprimes

minor_locator = MultipleLocator(0.20)

X, YU, YD, no = get_Y(0.0, 0.4)
print '(0.0, 0.4) = {}'.format(no)

fig1 = plt.subplot(211)
fig1.set_xlim([-2, 4])
fig1.set_ylim([-50, 50])
fig1.xaxis.set_minor_locator(minor_locator)
fig1.tick_params(which='minor', length=5, width=2)
fig1.tick_params(which='major', length=10, width=2, labelsize=20)
for x in ['top', 'bottom', 'left', 'right']:
    fig1.spines[x].set_linewidth(2)



fig1.axvspan(-5,0, facecolor='0.85', linewidth=0)
fig1.plot(X, YU, 'k-', linewidth=3)
fig1.plot(X, YD, 'k-', linewidth=3)

X, YU, YD, no = get_Y(0.6, 1.0)
print '(0.6, 1.0) = {}'.format(no)

fig2 = plt.subplot(212)
fig2.set_xlim([-2, 4])
fig2.set_ylim([-50, 50])
fig2.xaxis.set_minor_locator(minor_locator)
fig2.tick_params(which='minor', length=5, width=2)
fig2.tick_params(which='major', length=10, width=2, labelsize=20)
for x in ['top', 'bottom', 'left', 'right']:
    fig2.spines[x].set_linewidth(2)



fig2.axvspan(-5,0, facecolor='0.85', linewidth=0)
fig2.plot(X, YU, 'k-', linewidth=3)
fig2.plot(X, YD, 'k-', linewidth=3)


fig2.set_xlabel('Energy [eV]', fontweight='bold', fontsize=25)

plt.setp(fig1.get_xticklabels(), visible=False)
plt.setp(fig1.get_yticklabels(), visible=False)
plt.setp(fig2.get_yticklabels(), visible=False)
for tick in fig2.xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
plt.subplots_adjust(hspace=0)


plt.gcf().set_size_inches(10., 7)
plt.savefig('figure.png', dpi=100, bbox_inches='tight')

plt.show()

exit()

#plt.text(2, 60, str(lims[0])+'< spin < '+str(lims[1]), fontsize=30, weight='bold')
#plt.text(2, 40, 'No eprimes = '+str(no_eprimes), fontsize=25, weight='bold')
#plt.plot(X, Y, 'k-', linewidth=2)
#plt.plot(X, Yp, 'r-', linewidth=2)
plt.plot(X, YU, 'k-', linewidth=2)
plt.plot(X, YD, 'k-', linewidth=2)
#plt.plot(X, YpU, 'r-', linewidth=2)
#plt.plot(X, YpD, 'r-', linewidth=2)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

#plt.legend(handles=[nps, ps], ncol=2, fontsize=20)
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
#plt.gca().get_legend().get_frame().set_linewidth(2)


plt.gcf().set_size_inches(20., 3.5)
plt.savefig('figure.png', dpi=100, bbox_inches='tight')

plt.show()
