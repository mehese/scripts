#! /usr/bin/python2.7

import sys
import numpy as np
sys.path.append('../')
sys.path.append('../../')
from astools.ReadWrite import ReadStruct
from astools.analysis import distance

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

f = lambda x: x + 6.15

pc5  = np.loadtxt('../../../PDOS_files/qz_5pc_tot_opt.dat')
plt.plot(f(pc5[:,0]), pc5[:,1], color='#ff9900', label='5%HF DFT', linewidth=3)
pc20 = np.loadtxt('../../../PDOS_files/qz_20pc_tot_opt.dat')
plt.plot(f(pc20[:,0]), pc20[:,1], color='#aa66ff', label='20%HF DFT', linewidth=3)


minor_locator = MultipleLocator(1.0)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

plt.legend(ncol=1, fontsize=20, loc='upper left')
plt.xlim([f(-20), f(7)])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.gca().get_legend().get_frame().set_linewidth(2)

plt.gcf().set_size_inches(20., 3.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=20)
plt.savefig('dos_qzBulk.png', dpi=100, bbox_inches='tight')

plt.show()

