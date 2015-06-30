#! /usr/bin/env python

import sys
sys.path.append('/home/eric/Dropbox/astools/')
from analysis import *
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator
from scipy.ndimage import filters
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz

def testGauss(x, y):
    b = gaussian(30, 7.4)
    ga = filters.convolve1d(y, b/b.sum())
    #plt.plot(x, ga)
    return ga


print 'cell 1...'
cell = ReadStruct('INPUT_c1', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 
plt.plot(x, testGauss(x, y), 'k--', label='clean Si fixed boxsize cell')

print 'cell 2...'
cell = ReadStruct('INPUT_c2', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 
plt.plot(x, testGauss(x, y), color='k', label='clean Si boxsize relaxed')

print 'cell 3...'
cell = ReadStruct('INPUT_c3', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 
plt.plot(x, testGauss(x, y), color='k')

print 'cell 4...'
cell = ReadStruct('INPUT_c4', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 
plt.plot(x, testGauss(x, y), color='k')

print 'cell 5...'
cell = ReadStruct('INPUT_c5', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 
plt.plot(x, testGauss(x, y), color='k')

print 'cell 6...'
cell = ReadStruct('INPUT_c6', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 
plt.plot(x, testGauss(x, y), color='k')


plt.plot([0, cell.coordz/2], [2.328, 2.328], color="#33D6FF", linewidth=3.5, label='Bulk Si')
plt.plot([cell.coordz/2, cell.coordz], [2.66 , 2.66 ], color="#FF4D4D", linewidth=3.5,
         label=r'$\mathbf{\alpha}$-quartz')
plt.plot([cell.coordz/2, cell.coordz], [2.2 , 2.2 ], color="#990033", linewidth=3.5,
         label=r'amorphous SiO$_\mathbf{2}$')


plt.xlabel(r'z coordinate [$\mathbf{\AA}$]', fontweight='bold', fontsize=16)
plt.ylabel(r'density [g/cm$^\mathbf{3}$]', fontweight='bold', fontsize=16)

plt.xlim([0, cell.coordz])
plt.ylim([1.50, 3.0])

plt.legend(fontsize=16, loc=3)
l = plt.gca().get_legend().get_frame().set_linewidth(2)


minor_locator = MultipleLocator(1)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.gcf().set_size_inches(20., 7.)
plt.savefig('cleancells.png', dpi=200, bbox_inches='tight')
plt.show()

print 'Done'
