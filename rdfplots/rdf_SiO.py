#! /usr/bin/env python

import sys
sys.path.append('/home/eric/Dropbox/astools/')
from analysis import *
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



# Get the experimental results
exp_ = list(csv.reader(open('SiO2_rdf_exp.csv', 'rb'), delimiter=','))
exp_ = np.array(exp_).astype(float)
x = exp_[:, 0]
y = exp_[:, 1]
#plt.plot(x, y, 'r-', label='Raw')
x_ = np.linspace(np.min(x), np.max(x), 400)
f = interp1d(x, y, kind='cubic')
plt.plot(x_, f(x_) - 0.75, 'r-', linewidth=2.0, label='Experiment')


print 'cell 1...'
cell = ReadStruct('../inputs/INPUT_c1', 'crystal')
x, y = rdf2(cell, 100, dist=2.3)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[2][:-1], kind='cubic')
#print y[2][-1]
#plt.plot(x, y[2][:-1], 'k-', linewidth=1.8)
plt.plot(x_, f(x_), 'k--', linewidth=2.5, label='fixed boxsize cell')

print 'cell 2...'
cell = ReadStruct('../inputs/INPUT_c2', 'crystal')
x, y = rdf2(cell, 100, dist=2.3)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[2][:-1], kind='cubic')
#plt.plot(x, y[2][:-1], 'k-', linewidth=0.8)
plt.plot(x_, f(x_), 'k-', linewidth=2.5, alpha=0.6, label='clean Si cells')

print 'cell 3...'
cell = ReadStruct('../inputs/INPUT_c3', 'crystal')
x, y = rdf2(cell, 100, dist=2.3)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[2][:-1], kind='cubic')
#plt.plot(x, y[2][:-1], 'k-', linewidth=0.8)
plt.plot(x_, f(x_), 'k-', linewidth=2.5, alpha=0.6)

print 'cell 4...'
cell = ReadStruct('../inputs/INPUT_c4', 'crystal')
x, y = rdf2(cell, 100, dist=2.3)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[2][:-1], kind='cubic')
#plt.plot(x, y[2][:-1], 'k-', linewidth=0.8)
plt.plot(x_, f(x_), 'k-', linewidth=2.5, alpha=0.6)

print 'cell 5...'
cell = ReadStruct('../inputs/INPUT_c5', 'crystal')
x, y = rdf2(cell, 100, dist=2.3)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[2][:-1], kind='cubic')
#plt.plot(x, y[2][:-1], 'k-', linewidth=0.8)
plt.plot(x_, f(x_), 'k-', linewidth=2.5, alpha=0.6)

print 'cell 6...'
cell = ReadStruct('../inputs/INPUT_c6', 'crystal')
x, y = rdf2(cell, 100, dist=2.3)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[2][:-1], kind='cubic')
#plt.plot(x, y[2][:-1], 'k-', linewidth=0.8)
plt.plot(x_, f(x_), 'k-', linewidth=2.5, alpha=0.6)

print 'cell 2 ox...'
cell = ReadStruct('../inputs/INPUT_c2ox', 'crystal')
x, y = rdf2(cell, 100, dist=2.3)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[2][:-1], kind='cubic')
#plt.plot(x, y[2][:-1], 'r-', linewidth=0.8)
plt.plot(x_, f(x_), 'r-', linewidth=2.5, alpha=0.6, label='Oxidised cells')

print 'cell 3 ox...'
cell = ReadStruct('../inputs/INPUT_c3ox', 'crystal')
x, y = rdf2(cell, 100, dist=2.3)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[2][:-1], kind='cubic')
#plt.plot(x, y[2][:-1], 'r-', linewidth=0.8)
plt.plot(x_, f(x_), 'r-', linewidth=2.5, alpha=0.6)

print 'cell 5 ox...'
cell = ReadStruct('../inputs/INPUT_c5ox', 'crystal')
x, y = rdf2(cell, 100, dist=2.3)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y[2][:-1], kind='cubic')
#plt.plot(x, y[2][:-1], 'r-', linewidth=0.8)
plt.plot(x_, f(x_), 'r-', linewidth=2.5, alpha=0.6)

plt.legend(fontsize=16, loc='upper left')
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.xlim([1.0, 2.28])
plt.ylim([.0, 2.8])
plt.xlabel(r'Distance [$\mathbf{\AA}$]', fontweight='bold', fontsize=16)
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
plt.savefig('rdf_SiO.png', dpi=400, bbox_inches='tight')
plt.show()

print 'Done'
