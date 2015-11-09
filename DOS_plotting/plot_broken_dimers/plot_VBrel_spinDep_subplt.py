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
#cells_to_check = ['c2ox', 'c3ox', 'c5ox']


def get_Y(lim_low, lim_high):
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
            if lim_low <= np.fabs(s) <= lim_high:
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
                    Yp = Yp + Yp_u - Yp_d
                    if to_switch[c][bdimer]:
                        print c, bdimer, 'switch'
                        YpU -= Yp_d
                        YpD -= Yp_u
                    else:
                        YpU += Yp_u
                        YpD += Yp_d
                no_bdimers = no_bdimers + 1

    return X, YU, YD, no_bdimers

minor_locator = MultipleLocator(0.20)

X, YU, YD, no = get_Y(0.0, 0.4)
print '(0.0, 0.4) = {}'.format(no)

fig1 = plt.subplot(211)
fig1.set_xlim([-2, 4])
fig1.set_ylim([-15, 15])
fig1.xaxis.set_minor_locator(minor_locator)
fig1.tick_params(which='minor', length=5, width=2)
fig1.tick_params(which='major', length=10, width=2, labelsize=15)
for x in ['top', 'bottom', 'left', 'right']:
    fig1.spines[x].set_linewidth(2)



fig1.axvspan(-5,0, facecolor='0.85', linewidth=0)
fig1.plot(X, YU, 'k-', linewidth=3)
fig1.plot(X, YD, 'k-', linewidth=3)
fig1.text(-1.5, 8, '(SiSiO)Si', fontweight='bold', fontsize=30)

X, YU, YD, no = get_Y(0.6, 1.0)
print '(0.6, 1.0) = {}'.format(no)

fig2 = plt.subplot(212)
fig2.set_xlim([-2, 4])
fig2.set_ylim([-15, 15])
fig2.xaxis.set_minor_locator(minor_locator)
fig2.tick_params(which='minor', length=5, width=2)
fig2.tick_params(which='major', length=10, width=2, labelsize=15)
for x in ['top', 'bottom', 'left', 'right']:
    fig2.spines[x].set_linewidth(2)



fig2.axvspan(-5,0, facecolor='0.85', linewidth=0)
fig2.plot(X, YU, 'k-', linewidth=3)
fig2.plot(X, YD, 'k-', linewidth=3)


fig2.set_xlabel('Energy [eV]', fontweight='bold', fontsize=20)

plt.setp(fig1.get_xticklabels(), visible=False)
plt.setp(fig1.get_yticklabels(), visible=False)
plt.setp(fig2.get_yticklabels(), visible=False)
for tick in fig2.xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
plt.subplots_adjust(hspace=0)


plt.gcf().set_size_inches(10., 7)
plt.savefig('figure.png', dpi=100, bbox_inches='tight')

plt.show()
