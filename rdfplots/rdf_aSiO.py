#! /usr/bin/env python2.7

from astools.analysis import rdf, rdf2
from astools.ReadWrite import ReadStruct
import numpy as np
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator
from scipy.ndimage import filters
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz
from scipy.interpolate import spline, interp1d

import csv

def testGauss(x, y):
    b = gaussian(5, .2)
    ga = filters.convolve1d(y, b/b.sum())
    #plt.plot(x, ga)
    return ga

a = ReadStruct('../crystal_files/INPUT_aSiO2')
x, y = rdf(a, 200, dist=8.)
x_ = np.linspace(np.min(x), np.max(x), 600)
f = interp1d(x, y, kind='cubic')
plt.plot(x_, f(x_)*3.5, label='amorphous silica', linewidth=2, color='#ff1111')

print 'Done with total rdf'

x1, ys = rdf2(a, 200, dist=8.)

for i, c in zip(range(3), ['#AB6A67', '#085D9E', '#C76D28']):
    f = interp1d(x1, ys[i][:-1], kind='cubic')
    plt.plot(x_, f(x_)*3.5, label=ys[i][-1]+' pairs', linewidth=2, color=c)
    print '{} : {}'.format(i, ys[i][-1])

print 'Done with rdfs'


plt.legend(fontsize=16, loc='upper right')
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.xlabel(r'Distance [$\mathbf{\AA}$]', fontweight='bold', fontsize=16)
# No labels on y axis
plt.setp(plt.gca().get_yticklabels(), visible=False)

minor_locator = MultipleLocator(0.1)
y_locator = MultipleLocator(1)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().yaxis.set_major_locator(y_locator)
plt.gca().tick_params(which='minor', length=4, width=1.5)
plt.gca().tick_params(which='major', length=5, width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.xlim(xmax=8)
plt.ylim(ymin=0)
plt.gcf().set_size_inches(20., 3.5)
plt.savefig('rdf_aSiO2.png', dpi=400, bbox_inches='tight')
plt.show()

print 'Done'
