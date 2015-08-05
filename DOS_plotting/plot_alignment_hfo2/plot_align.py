#! /usr/bin/python2.7

import sys
import numpy as np
sys.path.append('../')
sys.path.append('../../')
from astools.ReadWrite import ReadStruct
from astools.analysis import distance

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

Si20 = np.loadtxt('../../../PDOS_files/SiBulk_20pc_opt.dat')
plt.plot(Si20[:,0], Si20[:,1]*10, color='#0033ff', alpha=1, label='Bulk Si',
linewidth=2, zorder=99)

mhfpc20 = np.loadtxt('../../../PDOS_files/m_hfo2_tot_figgen.dat')
plt.plot(mhfpc20[:,0], mhfpc20[:,1], color='0.5', label='m-HfO2 Figgen',
linewidth=1.2)

ahfpc20 = np.loadtxt('../../../PDOS_files/a_hfo2_tot.dat')
plt.plot(ahfpc20[:,0], ahfpc20[:,1], '--', color='0.5', label='a-HfO2',
linewidth=1.2)

c1 =  np.loadtxt('../../../PDOS_files/hsi_c1_tot.dat')
plt.plot(c1[:,0] - 1.2, c1[:,1], color='#ff0000', label='Si/HfO2 cell 1',
linewidth=2, alpha=0.7)
c1ox =  np.loadtxt('../../../PDOS_files/hsi_c1ox_tot.dat')
plt.plot(c1ox[:,0] - 1.2, c1ox[:,1], color='#800000', label='Si/HfO2 cell 1 ox',
linewidth=2, alpha=0.7)

minor_locator = MultipleLocator(1.0)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

plt.legend(ncol=1, fontsize=16, loc='upper left')
plt.xlim([-20, 5])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.gca().get_legend().get_frame().set_linewidth(2)

plt.gcf().set_size_inches(20., 10.)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=16)
plt.savefig('dos_aligned.png', dpi=400, bbox_inches='tight')


plt.show()

