#! /usr/bin/env python

import sys
from astools.analysis import *
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator
from scipy.ndimage import filters
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz
from scipy.interpolate import spline, interp1d

print 'cell 1...'
cell = ReadStruct('../crystal_files/INPUT_c1', 'crystal')
x, y = rdf2(cell, 150, dist=2.9)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[0][:-1], kind='cubic')
print y[0][-1]
#plt.plot(x, y[0][:-1], 'k-', linewidth=1.8)
plt.plot(x_, f(x_), 'k--', linewidth=3, label='Fixed boxsize cell')

print 'cell 2...'
cell = ReadStruct('../crystal_files/INPUT_c2', 'crystal')
x, y = rdf2(cell, 150, dist=2.9)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[0][:-1], kind='cubic')
#plt.plot(x, y[0][:-1], 'k-', linewidth=0.8)
plt.plot(x_, f(x_), 'k-', linewidth=3, alpha=0.6, label='Unoxidised Si cells')

print 'cell 3...'
cell = ReadStruct('../crystal_files/INPUT_c3', 'crystal')
x, y = rdf2(cell, 150, dist=2.9)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[0][:-1], kind='cubic')
#plt.plot(x, y[0][:-1], 'k-', linewidth=0.8)
plt.plot(x_, f(x_), 'k-', linewidth=3, alpha=0.6)

print 'cell 4...'
cell = ReadStruct('../crystal_files/INPUT_c4', 'crystal')
x, y = rdf2(cell, 150, dist=2.9)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[0][:-1], kind='cubic')
#plt.plot(x, y[0][:-1], 'k-', linewidth=0.8)
plt.plot(x_, f(x_), 'k-', linewidth=3, alpha=0.6)

print 'cell 5...'
cell = ReadStruct('../crystal_files/INPUT_c5', 'crystal')
x, y = rdf2(cell, 150, dist=2.9)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[0][:-1], kind='cubic')
#plt.plot(x, y[0][:-1], 'k-', linewidth=0.8)
plt.plot(x_, f(x_), 'k-', linewidth=3, alpha=0.6)

print 'cell 6...'
cell = ReadStruct('../crystal_files/INPUT_c6', 'crystal')
x, y = rdf2(cell, 150, dist=2.9)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[0][:-1], kind='cubic')
#plt.plot(x, y[0][:-1], 'k-', linewidth=0.8)
plt.plot(x_, f(x_), 'k-', linewidth=3, alpha=0.6)

print 'cell 2 ox...'
cell = ReadStruct('../crystal_files/INPUT_c2ox', 'crystal')
x, y = rdf2(cell, 150, dist=2.9)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[0][:-1], kind='cubic')
#plt.plot(x, y[0][:-1], 'r-', linewidth=0.8)
plt.plot(x_, f(x_), 'r-', linewidth=3, alpha=0.6, label='Oxidised cells')

print 'cell 3 ox...'
cell = ReadStruct('../crystal_files/INPUT_c3ox', 'crystal')
x, y = rdf2(cell, 150, dist=2.9)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[0][:-1], kind='cubic')
#plt.plot(x, y[0][:-1], 'r-', linewidth=0.8)
plt.plot(x_, f(x_), 'r-', linewidth=3, alpha=0.6)

print 'cell 5 ox...'
cell = ReadStruct('../crystal_files/INPUT_c5ox', 'crystal')
x, y = rdf2(cell, 150, dist=2.9)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[0][:-1], kind='cubic')
#plt.plot(x, y[0][:-1], 'r-', linewidth=0.8)
plt.plot(x_, f(x_), 'r-', linewidth=3, alpha=0.6)

# Plot bulk Si bond length

plt.plot([2.352, 2.352], [0.0, 1.5], color="#33D6FF", linewidth=3.5,
label='Experimental Si-Si \nbond length')

plt.legend(fontsize=20, loc='upper left')
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.xlim([1.8, 2.8])
plt.ylim([0.0, 1.5])
plt.xlabel(r'Distance [$\mathbf{\AA}$]', fontweight='bold', fontsize=20)
# No labels on y axis
plt.setp(plt.gca().get_yticklabels(), visible=False)

minor_locator = MultipleLocator(0.1)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=4, width=1.5)
plt.gca().tick_params(which='major', length=5, width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.gcf().set_size_inches(10., 9.)
plt.savefig('rdf_SiSi.png', dpi=100, bbox_inches='tight')
plt.show()

print 'Done'
