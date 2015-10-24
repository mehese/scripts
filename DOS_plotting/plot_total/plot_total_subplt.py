#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy.ndimage import filters
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz

def smooth(e, d, lowlim, uplim, dist):
    e_new, d_new = [], []
    for i in range(dist, len(e) - dist):
        e_new.append(e[i])
        if e[i] < lowlim:
            #print sum(d[k] for k in range(i-dist, i+dist+1))/len(range(-dist, dist+1))
            d_new.append(sum(d[k] for k in range(i-dist, i+dist+1))/len(range(-dist, dist+1)))
        elif e[i] > uplim:
            d_new.append(sum(d[k] for k in range(i-dist, i+dist+1))/len(range(-dist, dist+1)))
        else:
            d_new.append(d[i])

    return e_new, d_new

def testGauss(x, y):
    b = gaussian(30, 1.0)
    ga = filters.convolve1d(y, b/b.sum())
    ##plt.plot(x, ga)
    return ga


SiB = np.loadtxt('../../../PDOS_files/SiBulk_5pc_opt.dat')
qz = np.loadtxt('../../../PDOS_files/qz_5pc_tot_opt.dat')
qzSi = np.loadtxt('../../../PDOS_files/qzSi_5pc_tot.dat')
c1 = np.loadtxt('../../../PDOS_files/c1_tot.dat')
c2 = np.loadtxt('../../../PDOS_files/c2_tot.dat')
c3 = np.loadtxt('../../../PDOS_files/c3_tot.dat')
c4 = np.loadtxt('../../../PDOS_files/c4_tot.dat')
c5 = np.loadtxt('../../../PDOS_files/c5_tot.dat')
c6 = np.loadtxt('../../../PDOS_files/c6_tot.dat')

offst = 3.5

o = lambda k : k + offst

E1, dos1_u = c1[:,0], c1[:,1]
x1, y1 = E1, testGauss(E1, dos1_u)
x1 = o(x1)

E2, dos2_u = c2[:,0], c2[:,1]
x2, y2 = E2, dos2_u
x2, y2 = E2, testGauss(E2, dos2_u)
x2 = o(x2)

E3, dos3_u = c3[:,0], c3[:,1]
x3, y3 = E3, testGauss(E3, dos3_u)
x3 = o(x3)

E4, dos4_u = c4[:,0], c4[:,1]
x4, y4 = E4, testGauss(E4, dos4_u)
x4 = o(x4)

E5, dos5_u = c5[:,0], c5[:,1]
x5, y5 = E5, testGauss(E5, dos5_u)
x5 = o(x5)

E6, dos6_u = c6[:,0], c6[:,1]
x6, y6 = E6, testGauss(E6, dos6_u)
x6 = o(x6)

E_bulk, dos_qz = qz[:,0], qz[:,1]
x_qz, y_qz = E_bulk, 2*dos_qz

E_bulk, dos_Si = SiB[:,0], SiB[:,1]
x_Si, y_Si = E_bulk, 20*dos_Si

E_bulk, dos_qzSi = qzSi[:,0], qzSi[:,1]
x_qzSi, y_qzSi = E_bulk, 2*dos_qzSi

llab = ['Bulk Si', r'$\mathbf{\alpha}$-quartz', r'$\mathbf{\alpha}$-quartz/Si']
lcol = ['#0066FF', '#ff0000', '#880088']
lblk = [(o(x_Si), y_Si), (o(x_qz), y_qz), (o(x_qzSi), y_qzSi)]
ilst = range(len(llab))
fig = [None,]*len(llab)

minor_locator = MultipleLocator(1)

for i, blk, lab, col in zip(ilst, lblk, llab, lcol):
    fig[i] = plt.subplot(len(llab), 1, i+1)
    fig[i].xaxis.set_minor_locator(minor_locator)
    fig[i].tick_params(which='minor', length=5, width=2)
    fig[i].tick_params(which='major', length=10, width=2, labelsize=15)
    for x in ['top', 'bottom', 'left', 'right']:
        fig[i].spines[x].set_linewidth(2)
        plt.setp(fig[i].get_yticklabels(), visible=False)
        plt.setp(fig[i].get_xticklabels(), visible=False)
    fig[i].set_ylim([0, 80])
    fig[i].set_xlim([-13, 8])

    # plot cells DOS
    fig[i].plot(x1, y1, color='#000000', linewidth=0.8, alpha=.6,
                label='Unoxidised cells')
    fig[i].plot(x2, y2, color='#000000', linewidth=0.8, alpha=.6)
    fig[i].plot(x3, y3, color='#000000', linewidth=0.8, alpha=.6)
    fig[i].plot(x4, y4, color='#000000', linewidth=0.8, alpha=.6)
    fig[i].plot(x5, y5, color='#000000', linewidth=0.8, alpha=.6)
    fig[i].plot(x6, y6, color='#000000', linewidth=0.8, alpha=.6)
    # plot bulk component
    fig[i].plot(*blk, label=lab, color=col, linewidth=3)

    # plot legend
    fig[i].legend(fontsize=20, loc='upper right', ncol=2)
    fig[i].get_legend().get_frame().set_linewidth(2)

plt.setp(fig[i].get_xticklabels(), visible=True)

for tick in fig[i].xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
    #tick.label1.set_fontsize(15)



plt.xlabel('Energy (eV)', fontweight='bold', fontsize=20)
plt.subplots_adjust(hspace=0)
plt.gcf().set_size_inches(20., 3.5*len(llab))
plt.savefig('DOS_fullrange2.png', dpi=80, bbox_inches='tight')

plt.show()
exit()
