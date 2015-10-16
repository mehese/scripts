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
    #plt.plot(x, ga)
    return ga


SiB = np.loadtxt('state_density_SiBulk.dat')
qz = np.loadtxt('qz_total.dat')
qzSi = np.loadtxt('qzSi_tot.dat')
c1 = np.loadtxt('c1_sd_tot.dat')
c2 = np.loadtxt('c2_sd_tot.dat')
c3 = np.loadtxt('c3_sd_tot.dat')
c4 = np.loadtxt('c4_sd_tot.dat')
c5 = np.loadtxt('c5_sd_tot.dat')
c6 = np.loadtxt('c6_sd_tot.dat')

o = lambda k : k + 3.3

E1, dos1_u = c1[:,0], c1[:,1]
x, y = E1, testGauss(E1, dos1_u)
x = o(x)
plt.plot(x, y, color='#000000', linewidth=0.8, label='Clean Si cells', alpha=.6)

E2, dos2_u = c2[:,0], c2[:,1]
x, y = E2, testGauss(E2, dos2_u)
x = o(x)
plt.plot(x, y, color='#000000', linewidth=0.8, alpha=.6)

E3, dos3_u = c3[:,0], c3[:,1]
#x, y = smooth(E3, dos3_u, -4, -1.5, 4)
x, y = E3, testGauss(E3, dos3_u)
x = o(x)
plt.plot(x, y, color='#000000', linewidth=0.8, alpha=.6)

E4, dos4_u = c4[:,0], c4[:,1]
#x, y = smooth(E4, dos4_u, -4, -1.5, 4)
x, y = E4, testGauss(E4, dos4_u)
x = o(x)
plt.plot(x, y, color='#000000', linewidth=0.8, alpha=.6)

E5, dos5_u = c5[:,0], c5[:,1]
#x, y = smooth(E5, dos5_u, -4, -1.5, 4)
x, y = E5, testGauss(E5, dos5_u)
x = o(x)
plt.plot(x, y, color='#000000', linewidth=0.8, alpha=.6)

E6, dos6_u = c6[:,0], c6[:,1]
x, y = E6, testGauss(E6, dos6_u)
x = o(x)
plt.plot(x, y, color='#000000', linewidth=0.8, alpha=.6)

#Ef=-2.68
#plt.plot([Ef, Ef], [-100, 100], '-', color='#e62e00', linewidth=2, label='$E_F$')

E_bulk, dos_bulk = qz[:,0], qz[:,1]
x, y = E_bulk, 2*dos_bulk
x = o(x)
plt.plot(x, y, color='#ff0000', linewidth=3.0, label=r'$\mathbf{\alpha}$-quartz')

E_bulk, dos_bulk = SiB[:,0], SiB[:,1]
x, y = E_bulk, 20*dos_bulk
x = o(x)
plt.plot(x, y, color='#0066FF', linewidth=3.0, label='Bulk Si')

E_bulk, dos_bulk = qzSi[:,0], qzSi[:,1]
x, y = E_bulk, 2*dos_bulk
x = o(x)
plt.plot(x, y, color='#880088', linewidth=3.0,label=r'$\mathbf{\alpha}$-quartz/Si')


minor_locator = MultipleLocator(1)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

plt.xlabel('Energy (eV)', fontweight='bold', fontsize=20)
plt.xlim([o(-17.5), o(4)])

plt.ylim([0, 70])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.legend(loc=2, fontsize=20)
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.gcf().set_size_inches(20., 7.)
plt.savefig('DOS_fullrange.png', dpi=80, bbox_inches='tight')
plt.show()

print "Done"
