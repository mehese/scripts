#! /usr/bin/env python

import sys
sys.path.append('../')

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


SiB = np.loadtxt('SiBulk_20pc_opt.dat')
c = range(0,4)
c[0] = np.loadtxt('hfo2si_c1_tot.dat')
c[1] = np.loadtxt('hfo2si_c1ox_tot.dat')
c[2] = np.loadtxt('hfo2si_c2ox_tot.dat')
c[3] = np.loadtxt('hfo2si_c3ox_tot.dat')

titles = ['cell 1 (clean)', 'cell 1 (oxidised)', 'cell 2 (oxidised)', 'cell 3 (oxidised)']
fermis = [-0.3915623715, -1.1526262679, -0.5232161378, -0.8299245876]
colors = ['#D6AB00', 'palevioletred', 'navy', 'forestgreen']

for i in range(0,4):
    E, up, down = c[i][:,0], c[i][:,1], c[i][:,3]
    x, y1, y2 = E, testGauss(E, up), testGauss(E, down)
    #plt.plot(E-1.2+3.8, y1, color=colors[i], label=titles[i])
    #plt.plot(E-1.2+3.8, y2, color=colors[i])
    #plt.plot([fermis[i]-1.2+3.8,]*2, [-80, 80], '--', color=colors[i],
    #         label=r'$\mathbf{E_{f}}$ '+titles[i])
    #plt.plot([fermis[i]-1.2+3.8,]*2, [-80, 80], '--', color=colors[i])
    plt.plot(E, y1, color=colors[i], linewidth=2, label=titles[i])
    plt.plot(E, y2, color=colors[i], linewidth=2)
    plt.plot([fermis[i]+3.8,]*2, [-80, 100], '--', color=colors[i],
             label=r'$\mathbf{E_{f}}$ '+titles[i], linewidth=3)
    #plt.plot([fermis[i]+3.8,]*2, [-80, 80], '--', color=colors[i])
    print i

E_bulk, dos_bulk = SiB[:,0], SiB[:,1]
#plt.plot(E_bulk+3.8, 20*dos_bulk, color='#0066FF', linewidth=3.0, label='Bulk Si')
#plt.plot(E_bulk+3.8,-20*dos_bulk, color='#0066FF', linewidth=3.0)
plt.plot(E_bulk, 20*dos_bulk, color='#0066FF', linewidth=3.5, label='Bulk Si')
plt.plot(E_bulk,-20*dos_bulk, color='#0066FF', linewidth=3.5)

minor_locator = MultipleLocator(1)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=20)

plt.xlabel('Energy (eV)', fontweight='bold', fontsize=20)
plt.xlim([-20, +6])

plt.ylim([-70, 100])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.legend(loc='upper left', fontsize=16, ncol=5)
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.gcf().set_size_inches(20., 7.)
plt.savefig('DOS_hfo2si_tot.png', dpi=100, bbox_inches='tight')
plt.show()

print "Done"
