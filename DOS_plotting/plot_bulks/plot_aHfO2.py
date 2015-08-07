#! /usr/bin/python2.7

import sys
import numpy as np
sys.path.append('../')
sys.path.append('../../')
from astools.ReadWrite import ReadStruct
from astools.analysis import distance
from scipy.ndimage import filters
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

def testGauss(x, y):
    b = gaussian(10, .2)
    ga = filters.convolve1d(y, b/b.sum())
    #plt.plot(x, ga)
    return ga

dat  = np.loadtxt('../../../PDOS_files/a_hfo2_tot.dat')
x, y = dat[:,0], testGauss(dat[:,0], dat[:,1])
plt.plot(x, y*1.5, color='#990000', label='amorphous hafnia', linewidth=1.5)

pc5  = np.loadtxt('../../../PDOS_files/m_hfo2_tot_figgen.dat')
plt.plot(pc5[:,0], pc5[:,1]*3, color='#ff9933', label=r'monoclinic hafnia', linewidth=2)

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

plt.gcf().set_size_inches(20., 3.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=16)
plt.savefig('dos_aHfO2.png', dpi=400, bbox_inches='tight')


plt.show()

