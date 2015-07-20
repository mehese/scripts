#! /usr/bin/env python

from astools.analysis import *
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator
from scipy.ndimage import filters
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz
from scipy.interpolate import spline, interp1d

import csv

def testGauss(x, y):
    b = gaussian(50, 2.)
    ga = filters.convolve1d(y, b/b.sum())
    #plt.plot(x, ga)
    return ga

print 'cell 1...'
cell = ReadStruct('../crystal_files/INPUT_c1', 'crystal')
x, y_c1 = rdf(cell, 300, dist=7.)
print 'cell 2...'
cell = ReadStruct('../crystal_files/INPUT_c2', 'crystal')
x, y_c2 = rdf(cell, 300, dist=7.)
print 'cell 3...'
cell = ReadStruct('../crystal_files/INPUT_c3', 'crystal')
x, y_c3 = rdf(cell, 300, dist=7.)
print 'cell 4...'
cell = ReadStruct('../crystal_files/INPUT_c4', 'crystal')
x, y_c4 = rdf(cell, 300, dist=7.)
print 'cell 5...'
cell = ReadStruct('../crystal_files/INPUT_c5', 'crystal')
x, y_c5 = rdf(cell, 300, dist=7.)
print 'cell 6...'
cell = ReadStruct('../crystal_files/INPUT_c6', 'crystal')
x, y_c6 = rdf(cell, 300, dist=7.)

print 'cell 2ox...'
cell = ReadStruct('../crystal_files/INPUT_c2ox', 'crystal')
x, y_c2ox = rdf(cell, 300, dist=7.)
print 'cell 3ox...'
cell = ReadStruct('../crystal_files/INPUT_c3ox', 'crystal')
x, y_c3ox = rdf(cell, 300, dist=7.)
print 'cell 5ox...'
cell = ReadStruct('../crystal_files/INPUT_c5ox', 'crystal')
x, y_c5ox = rdf(cell, 300, dist=7.)

x_ = np.linspace(np.min(x), np.max(x), 600)
y = (np.array(y_c1) + np.array(y_c2) + np.array(y_c3) + np.array(y_c4) +
     np.array(y_c5) + np.array(y_c6) + np.array(y_c2ox) + np.array(y_c3ox) +
     np.array(y_c5ox))/9.
f = interp1d(x, y, kind='cubic')
#print y[2][-1]
#plt.plot(x, y[2][:-1], 'k-', linewidth=1.8)
plt.plot(x_, f(x_), '-', color='#009999', linewidth=2.5, label=r'Total $g(\mathbf{r})$')
plt.legend(fontsize=16, loc='upper right')
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.xlim([1.0, 6.8])
plt.ylim([.0, np.max(y)])
plt.xlabel(r'Distance [$\mathbf{\AA}$]', fontweight='bold', fontsize=16)
# No labels on y axis
plt.setp(plt.gca().get_yticklabels(), visible=False)

minor_locator = MultipleLocator(0.1)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.gca().tick_params(which='minor', length=4, width=1.5)
plt.gca().tick_params(which='major', length=5, width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.gcf().set_size_inches(20., 3.5)
plt.savefig('rdf_tot.png', dpi=400, bbox_inches='tight')
plt.show()

print 'Done'
