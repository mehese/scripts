#! /usr/bin/env python

import sys
sys.path.append('/home/eric/Dropbox/astools/')
from analysis import *
import matplotlib.pyplot as plt
from scipy.ndimage import filters
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz

def testGauss(x, y):
    b = gaussian(30, 7.4)
    ga = filters.convolve1d(y, b/b.sum())
    plt.plot(x, ga)
    return ga


print('cell 1...')
cell = ReadStruct('INPUT_c1', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 

#plt.plot(x, y, 'k-')
#plt.plot(x, testGauss(x, y), color='#99FF99')
plt.plot(x, testGauss(x, y), color='b')
plt.xlim([0,cell.coordz])

print('cell 2...')
cell = ReadStruct('INPUT_c2', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 

#plt.plot(x, testGauss(x, y), color='#99FF99')
plt.plot(x, testGauss(x, y), color='b')
plt.xlim([0,cell.coordz])

print('cell 3...')
cell = ReadStruct('INPUT_c3', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 

#plt.plot(x, testGauss(x, y), color='#99FF99')
plt.plot(x, testGauss(x, y), color='b')
plt.xlim([0,cell.coordz])

print('cell 4...')
cell = ReadStruct('INPUT_c4', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 

#plt.plot(x, testGauss(x, y), color='#99FF99')
plt.plot(x, testGauss(x, y), color='b')
plt.xlim([0,cell.coordz])

print('cell 5...')
cell = ReadStruct('INPUT_c5', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 

#plt.plot(x, testGauss(x, y), color='#99FF99')
plt.plot(x, testGauss(x, y), color='b')
plt.xlim([0,cell.coordz])

print('cell 6...')
cell = ReadStruct('INPUT_c6', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 

#plt.plot(x, testGauss(x, y), color='#99FF99')
plt.plot(x, testGauss(x, y), color='b')
plt.xlim([0,cell.coordz])

print('cell 2ox...')
cell = ReadStruct('INPUT_c2ox', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 

#plt.plot(x, testGauss(x, y), color='#33CC33')
plt.plot(x, testGauss(x, y), color='#ff0000')
plt.xlim([0,cell.coordz])

print('cell 3ox...')
cell = ReadStruct('INPUT_c3ox', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 

#plt.plot(x, testGauss(x, y), color='#33CC33')
plt.plot(x, testGauss(x, y), color='#ff0000')
plt.xlim([0,cell.coordz])

print('cell 5ox...')
cell = ReadStruct('INPUT_c5ox', 'crystal')
x, y = vertical_density_profile(cell, 1.15, no_points=230, full=True) 

#plt.plot(x, testGauss(x, y), color='#33CC33')
plt.plot(x, testGauss(x, y), color='#ff0000')
plt.xlim([0,cell.coordz])






#plt.title('Si-O RDF', fontweight='bold', fontsize=18) 
plt.xlabel(r'z coordinate [$\mathbf{\AA}$]', fontweight='bold', fontsize=16)
plt.ylabel(r'density [g/cm$^\mathbf{3}$]', fontweight='bold', fontsize=16)
plt.xlim([0, cell.coordz])
#plt.yticks([])
#
plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
#
#plt.legend(fontsize=13)
plt.gcf().set_size_inches(10., 7.)
plt.savefig('rdf_SiO.png', dpi=200, bbox_inches='tight')
plt.show()

print('Done')
